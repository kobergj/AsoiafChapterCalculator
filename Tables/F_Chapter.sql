
DROP TABLE IF EXISTS dbo.F_Chapter;

CREATE TABLE dbo.F_Chapter (
    Id              SERIAL      PRIMARY KEY
    , Name          VARCHAR(50) NOT NULL
    , BookId        INT         NULL        -- Reference to D_Book
    , CharacterId   INT         NULL        -- Reference to D_Character
    , ChapterNumber INT         NULL        -- Number if Chapter in Book

);
