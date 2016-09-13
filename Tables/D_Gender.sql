DROP TABLE IF EXISTS prod."D_Gender";

CREATE TABLE prod."D_Gender" (
    "Id"            SERIAL      PRIMARY KEY
    , "Gendername"  VARCHAR(7)  NOT NULL
);

WITH GenderNames AS (
    SELECT 'Male'    as Gendername    UNION ALL
    SELECT 'Female'  as Gendername    UNION ALL
    SELECT 'Unknown' as Gendername
)

-- Initial Data - TODO: Move to seperate File
INSERT INTO prod."D_Gender" ("Gendername")
SELECT *
FROM GenderNames
