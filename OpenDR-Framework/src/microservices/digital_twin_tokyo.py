import sedona.sql
from pyspark.sql import SparkSession

def evaluate_urban_vulnerability(flood_vector_path, citygml_parquet_path):
    """
    Uses Apache Sedona to perform a 3D spatial join between 
    Project PLATEAU building models and flood inundation vectors.
    """
    spark = SparkSession.builder.appName("OpenDR-Tokyo").getOrCreate()
    
    # Load 3D Building Models (Project PLATEAU)
    buildings = spark.read.parquet(citygml_parquet_path)
    
    # Load Real-time Flood Extent
    flood_zones = spark.read.format("geoparquet").load(flood_vector_path)
    
    # Perform 3D Spatial Join
    # Identifies buildings where flood_depth > floor_height
    at_risk = buildings.alias("b").join(
        flood_zones.alias("f"),
        "ST_Intersects(b.geometry, f.geometry)"
    ).filter("f.depth > b.measured_height")
    
    return at_risk