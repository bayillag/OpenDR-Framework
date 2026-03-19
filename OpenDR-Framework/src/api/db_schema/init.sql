-- Enable PostGIS and 3D Support
CREATE EXTENSION IF NOT EXISTS postgis;
CREATE EXTENSION IF NOT EXISTS postgis_topology;

-- Tier 4: Active Hazard Tables
CREATE TABLE active_fires (
    id SERIAL PRIMARY KEY,
    fire_id TEXT UNIQUE,
    frp DOUBLE PRECISION,
    discovery_time TIMESTAMPTZ,
    geom GEOMETRY(MultiPolygon, 4326)
);

CREATE TABLE flood_extents (
    id SERIAL PRIMARY KEY,
    event_date DATE,
    basin_name TEXT,
    saturation_index FLOAT, -- Derived from GRACE
    geom GEOMETRY(Polygon, 4326)
);

-- Tier 5: Citizen Feedback Loop Table
CREATE TABLE field_validation (
    id SERIAL PRIMARY KEY,
    kobo_id TEXT,
    hazard_type TEXT,
    is_valid BOOLEAN,
    observation_date TIMESTAMPTZ,
    geom GEOMETRY(Point, 4326)
);

CREATE INDEX idx_flood_geom ON flood_extents USING GIST (geom);

CREATE EXTENSION IF NOT EXISTS postgis;

-- Table for Real-time Flood Extents
CREATE TABLE flood_alerts (
    id SERIAL PRIMARY KEY,
    event_date TIMESTAMPTZ,
    basin_name TEXT,
    geom GEOMETRY(Polygon, 4326)
);

-- Table for Active Wildfire Watch
CREATE TABLE fire_alerts (
    id SERIAL PRIMARY KEY,
    discovery_time TIMESTAMPTZ,
    intensity_frp FLOAT,
    geom GEOMETRY(MultiPolygon, 4326)
);

-- Table for Citizen Validation (Loop-in-the-Citizen)
CREATE TABLE field_validation (
    id SERIAL PRIMARY KEY,
    hazard_id INT,
    is_valid BOOLEAN, -- Confirmed by responder
    notes TEXT,
    geom GEOMETRY(Point, 4326)
);