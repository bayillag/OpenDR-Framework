CREATE TABLE amhara_health_alerts (
    woreda_id INTEGER,
    woreda_name TEXT,
    malaria_risk_index INT,
    precip_30day_sum FLOAT,
    last_update TIMESTAMPTZ DEFAULT NOW(),
    geom GEOMETRY(MultiPolygon, 4326)
);

-- Spatial index for rapid dashboard rendering
CREATE INDEX idx_health_geom ON amhara_health_alerts USING GIST (geom);