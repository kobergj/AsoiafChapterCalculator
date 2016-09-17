DROP TABLE IF EXISTS prod."F_CharacterHouseRelation";

CREATE TABLE prod."F_CharacterHouseRelation" (
    , "CharacterId"     INTEGER         NOT NULL    -- Reference to D_Character
    , "HouseId"         INTEGER         NOT NULL    -- Reference to D_House
    , "RelationTypeId"  VARCHAR(20)     NOT NULL
    -- Beginning of Relation
    , "StartOfRelation" INTEGER         NULL        -- Year
    , "StartReason"     VARCHAR(250)    NULL        -- Story of RelationBegin
    -- End of Relation
    , "EndOfRelation"   INTEGER         NULL        -- Year
    , "EndReason"       VARCHAR(250)    NULL        -- Story of RelationEnd
);