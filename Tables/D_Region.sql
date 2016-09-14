DROP TABLE IF EXISTS prod."D_Region";

CREATE TABLE prod."D_Region" (
    "Id"        SERIAL PRIMARY KEY
    , "Name"    VARCHAR(50) NOT NULL
);