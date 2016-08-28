DROP TABLE IF EXISTS prod."F_PovCharacterInChapter";

CREATE TABLE prod."F_PovCharacterInChapter" (
    "CharacterId"   INT         NOT NULL        -- Reference to D_Character
    , "ChapterId"     INT         NOT NULL        -- Reference to D_Chapter
);