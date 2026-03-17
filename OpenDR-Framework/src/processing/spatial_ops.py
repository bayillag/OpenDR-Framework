import subprocess

def push_to_postgis(geojson_path, table_name):
    """
    Uses GDAL/OGR to push intelligence vectors to Tier 4 storage.
    """
    cmd = [
        "ogr2ogr",
        "-f", "PostgreSQL",
        "PG:host=database dbname=opendr user=opendr_admin password=foss4g",
        geojson_path,
        "-nln", table_name,
        "-append",
        "-t_srs", "EPSG:4326"
    ]
    subprocess.run(cmd)