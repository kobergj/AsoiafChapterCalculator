DROP TABLE IF EXISTS prod."D_House";

CREATE TABLE prod."D_House" (
    "Id"                        SERIAL          PRIMARY KEY
    , "Name"                    VARCHAR(50)     NOT NULL
    , "Branch"                  VARCHAR(50)     NULL -- only NULL if no other branches exist
    -- Related Characters
    , "CurrentLordId"           INTEGER         NULL -- Reference to D_Character
    , "HeirId"                  INTEGER         NULL -- Reference to D_Character
    , "FounderId"               INTEGER         NULL -- Reference to D_Character
    -- References
    , "OverlordHouseId"         INTEGER         NULL -- Reference to D_House
    , "RegionId"                INTEGER         NULL -- Reference to D_Region
    -- Descriptives
    , "FoundedAt"               INTEGER         NULL
    , "DiedOutAt"               INTEGER         NULL
    , "Words"                   VARCHAR(200)    NULL
    , "CoatOfArmsDescription"   VARCHAR(500)    NULL
)