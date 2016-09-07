/* Insert new Books */
INSERT INTO prod."D_Book" ("Name")
    SELECT DISTINCT sta."bookname"
    FROM staging."charinchapter" sta
    WHERE NOT EXISTS (
        SELECT 1 FROM prod."D_Book" bk WHERE bk."Name" = sta."bookname"
    );

/* Insert new Chapters */
INSERT INTO prod."D_Chapter" ("ChapterOfBookNumber", "BookId")
    SELECT DISTINCT
        sta."chapternumber"
        , bk."Id"
    FROM staging."charinchapter" sta
    INNER JOIN prod."D_Book" bk ON bk."Name" = sta."bookname"
    WHERE NOT EXISTS (
        SELECT 1 
        FROM prod."D_Chapter" ch
        WHERE ch."ChapterOfBookNumber" = sta."chapternumber"
          AND ch."BookId" = bk."Id"
        );

/* Insert new Characters */
INSERT INTO prod."D_Character" ("FirstName", "SurName") 
    SELECT DISTINCT
        sta."charfirstname"
        , sta."charsurname"
    FROM staging."charinchapter" sta

    WHERE NOT EXISTS (
        SELECT 1 
        FROM prod."D_Character" ch
        WHERE ch."FirstName" = sta."charfirstname"
          AND ch."SurName" = sta."charsurname"
    );

/* Get Last Loaded Line */
WITH lastloaded AS (
    SELECT
        "chapternumber"
        , "bookname"
        , max("insertiontime") AS lastload
    FROM staging."charinchapter"
    GROUP BY 
        "chapternumber"
        , "bookname"
)

/* Update Chapters */
UPDATE prod."D_Chapter"
    SET
        "Name" = sta."chaptername"
        , "MainCharacterId" = cha."Id"
    FROM 
        staging."charinchapter" sta
    INNER JOIN
        lastloaded ll   ON ll."chapternumber" = sta."chapternumber"
                       AND ll."bookname" = sta."bookname"
                       AND ll."lastload" = sta."insertiontime"
    INNER JOIN
        prod."D_Book" bk ON bk."Name" = sta."bookname"
    INNER JOIN
        prod."D_Character" cha  ON cha."FirstName" = sta."charfirstname"
                               AND cha."SurName" = sta."charsurname"
    WHERE "BookId" = bk."Id"
      AND "ChapterOfBookNumber" = sta."chapternumber"

