DROP TABLE IF EXISTS prod."D_Character";

CREATE TABLE prod."D_Character" (
    "Id"              SERIAL      PRIMARY KEY
    -- Business Keys
    , "FirstName"     VARCHAR(50) NOT NULL
    , "SurName"       VARCHAR(50) NOT NULL
    -- Descriptives
    , "GenderId"      INTEGER     NULL  -- Reference to D_Gender
    , "YearOfBirth"   INTEGER     NULL
    , "YearOfDeath"   INTEGER     NULL
);