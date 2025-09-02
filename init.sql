DROP TABLE IF EXISTS real_estate_analytics;
CREATE TABLE IF NOT EXISTS real_estate_analytics (
    property_type VARCHAR(50),
    district VARCHAR(100), 
    avg_price DECIMAL(12,2),
    avg_area DECIMAL(10,2),
    total_ads INTEGER,
    avg_price_per_sqm DECIMAL(10,2),
    PRIMARY KEY (property_type, district)
);

CREATE INDEX IF NOT EXISTS idx_district ON real_estate_analytics(district);
CREATE INDEX IF NOT EXISTS idx_type ON real_estate_analytics(property_type);
