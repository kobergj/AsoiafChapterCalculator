DROP TABLE IF EXISTS prod."D_PossessionType";

CREATE TABLE prod."D_PossessionType" (
    "Id"                    SERIAL      PRIMARY KEY
    , "Name"                VARCHAR(20) NOT NULL
);