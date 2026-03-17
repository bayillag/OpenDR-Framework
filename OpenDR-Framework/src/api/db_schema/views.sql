-- Create a Real-time Exposure View
-- Intersects Open Buildings with active Flood Extents
CREATE OR REPLACE VIEW building_exposure_v1 AS
SELECT 
    b.id as building_id,
    b.height,
    f.basin_name,
    f.event_date,
    ST_Intersection(b.geom, f.geom) as impact_geom,
    (ST_Area(ST_Intersection(b.geom, f.geom)) / ST_Area(b.geom)) * 100 as pct_inundated
FROM 
    open_buildings b, 
    flood_extents f
WHERE 
    ST_Intersects(b.geom, f.geom)
    AND f.event_date > NOW() - INTERVAL '24 hours';