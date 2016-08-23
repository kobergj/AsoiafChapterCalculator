DROP TABLE IF EXISTS dbo.D_Character;

CREATE TABLE dbo.D_Character (
    Id                      SERIAL      PRIMARY KEY
    , Name                  VARCHAR(50) NOT NULL
);