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

/* Insert new Books */
INSERT INTO prod."D_Book" ("Name") 
    SELECT DISTINCT
        sta."bookname"
    FROM staging."charinchapter" sta

    WHERE NOT EXISTS (
        SELECT 1 
        FROM prod."D_Book" bk
        WHERE bk."Name" = sta."bookname"
    );


/* Insert new Chapters */
INSERT INTO prod."D_Chapter" ("BookId", "ChapterOfBookNumber")
    SELECT DISTINCT
        bk."Id"
        , sta."chapternumber"
    FROM 
        staging."charinchapter" sta
    INNER JOIN prod."D_Book" bk ON bk."Name" = sta."bookname"

    WHERE NOT EXISTS (
        SELECT 1 
        FROM prod."D_Chapter" ch
        WHERE ch."ChapterOfBookNumber" = sta."chapternumber"
          AND ch."BookId" = bk."Id"
    );

/* Insert Fact */
INSERT INTO prod."F_PovCharacterInChapter" ("CharacterId", "ChapterId")
    SELECT
        ch."Id"
        , cp."Id"
    FROM staging."charinchapter" sta

    INNER JOIN prod."D_Character" ch ON ch."FirstName" = sta."charfirstname"
                                    AND ch."SurName" = sta."charsurname"

    INNER JOIN prod."D_Book" bk ON bk."Name" = sta."bookname"

    INNER JOIN prod."D_Chapter" cp ON cp."ChapterOfBookNumber" = sta."chapternumber"
                                  AND cp."BookId" = bk."Id"
    WHERE NOT EXISTS (
        SELECT 1
        FROM prod."F_PovCharacterInChapter" pov
        WHERE pov."ChapterId" = ch."Id"
          AND pov."ChapterId" = cp."Id"
        );



