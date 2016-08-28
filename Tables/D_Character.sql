DROP TABLE IF EXISTS prod."D_Character";

CREATE TABLE prod."D_Character" (
    "Id"              SERIAL      PRIMARY KEY
    , "FirstName"     VARCHAR(50) NOT NULL
    , "SurName"       VARCHAR(50) NOT NULL
    , "Gender"        VARCHAR(10) NULL
    , "YearOfBirth"   INTEGER     NULL
    , "YearOfDeath"   INTEGER     NULL
);