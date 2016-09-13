DROP TABLE IF EXISTS prod."D_Gender";

CREATE TABLE prod."D_Gender" (
    "Id"            SERIAL      PRIMARY KEY
    , "Gendername"  VARCHAR(7)  NOT NULL
);

WITH GenderNames AS (
    SELECT
    "Male"      as Gendername    UNION ALL
    , "Female"  as Gendername    UNION ALL
    , "Unknown" as Gendername
)

-- Initial Data - TODO: Move to seperate File
INSERT INTO prod."Gender" ("Gendername")
SELECT "Gendername"
FROM GenderNames
