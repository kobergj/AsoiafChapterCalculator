DROP TABLE IF EXISTS prod."D_Culture";

CREATE TABLE prod."D_Culture" (
    "Id"        SERIAL      PRIMARY KEY
    , "Name"    VARCHAR(50) NOT NULL
);