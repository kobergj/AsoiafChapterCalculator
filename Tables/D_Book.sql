DROP TABLE IF EXISTS prod."D_Book";

CREATE TABLE prod."D_Book" (
    "Id"              SERIAL      PRIMARY KEY
    , "Name"          VARCHAR(50) NOT NULL
);