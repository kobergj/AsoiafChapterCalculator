DROP TABLE IF EXISTS prod."D_Possession";

CREATE TABLE prod."D_Possession" (
    "Id"                    SERIAL          PRIMARY KEY
    , "PossessionTypeId"    INTEGER         NOT NULL    -- Reference to D_PossessionType
    , "Description"         VARCHAR(200)    NULL
);