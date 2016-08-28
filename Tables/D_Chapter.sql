
DROP TABLE IF EXISTS prod."D_Chapter";

CREATE TABLE prod."D_Chapter" (
    "Id"                    SERIAL      PRIMARY KEY
    , "Name"                VARCHAR(50) NULL
    , "BookId"              INT         NOT NULL        -- Reference to D_Book
    , "MainCharacterId"     INT         NULL            -- Reference to D_Character
    , "ChapterOfBookNumber" INT         NOT NULL        -- Number if Chapter in Book

);
