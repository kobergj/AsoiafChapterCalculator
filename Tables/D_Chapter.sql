
DROP TABLE IF EXISTS prod."D_Chapter";

CREATE TABLE prod."D_Chapter" (
    "Id"                    SERIAL      PRIMARY KEY
    --Business Keys
    , "BookId"              INT         NOT NULL        -- Reference to D_Book
    , "ChapterOfBookNumber" INT         NOT NULL        -- Number if Chapter in Book
    -- Descriptives
    , "Name"                VARCHAR(50) NULL
);
