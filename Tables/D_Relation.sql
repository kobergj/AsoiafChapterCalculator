DROP TABLE IF EXISTS prod."D_RelationType";

CREATE TABLE prod."D_RelationType" (
    "Id"        SERIAL      PRIMARY KEY
    , "Name"    VARCHAR(20) NOT NULL
);