DROP TABLE IF EXISTS prod."F_PossessionOfHouse";

CREATE TABLE prod."F_PossessionOfHouse" (
    "HouseId"           INTEGER     NOT NULL    -- Reference to D_House
    , "PossessionId"    INTEGER     NOT NULL    -- Reference to D_Possession
    -- Descriptives
    , "GotPossesion"    INTEGER     NULL        -- The Year the House got the Possession
    , "LostPossesion"   INTEGER     NULL        -- The Year the House lost the Possession
);