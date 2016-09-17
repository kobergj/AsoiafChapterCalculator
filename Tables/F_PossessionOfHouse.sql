DROP TABLE IF EXISTS prod."F_PossessionOfHouse";

CREATE TABLE prod."F_PossessionOfHouse" (
    "HouseId"           INTEGER         NOT NULL    -- Reference to D_House
    , "PossessionId"    INTEGER         NOT NULL    -- Reference to D_Possession
    -- Descriptives
    , "GotPossesion"    INTEGER         NULL        -- The Year the House got the Possession
    , "GotReason"       VARCHAR(250)    NULL        -- Story of Possession Begin

    , "LostPossesion"   INTEGER         NULL        -- The Year the House lost the Possession
    , "LostReason"      VARCHAR(250)    NULL        -- Story of Possession End
);