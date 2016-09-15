DROP TABLE IF EXISTS prod."D_Gender";

CREATE TABLE prod."D_Gender" (
    "Id"            SERIAL      PRIMARY KEY
    , "Gendername"  VARCHAR(7)  NOT NULL
);
