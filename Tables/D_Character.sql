DROP TABLE IF EXISTS dbo.D_Character;

CREATE TABLE dbo.D_Character (
    Id              SERIAL      PRIMARY KEY
    , FirstName     VARCHAR(50) NOT NULL
    , SurName       VARCHAR(50) NOT NULL
    , Gender        VARCHAR(10) NULL
    , YearOfBirth   INTEGER     NULL
    , YearOfDeath   INTEGER     NULL
);