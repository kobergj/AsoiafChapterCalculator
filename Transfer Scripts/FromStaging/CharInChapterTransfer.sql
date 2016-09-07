/* Get Last Loaded Info */
WITH LastLoaded AS (
    SELECT
        *
        , ROW_NUMBER() OVER (PARTITION BY ("charfirstname", "charsurname")
                             ORDER BY "insertiontime" DESC) AS rn
    FROM
        staging."charinchapter"
    )

/* InsertNewCharacters */
    INSERT INTO prod."D_Character" ("FirstName", "SurName") 
        SELECT
            sta."charfirstname"
            , sta."charsurname"
        FROM LastLoaded sta
        LEFT JOIN prod."D_Character" ch ON ch."FirstName" = sta."charfirstname"
                                        AND ch."SurName" = sta."charsurname"

        WHERE sta."rn" = 1
          AND ch."FirstName" IS NULL

; WITH LastLoaded AS (
    SELECT
        *
        , ROW_NUMBER() OVER (PARTITION BY ("bookname")
                             ORDER BY "insertiontime" DESC) AS rn
    FROM
        staging."charinchapter"
    )
/* InsertNewBooks */
    INSERT INTO prod."D_Book" ("Name") 
        SELECT
            sta."bookname"
        FROM LastLoaded sta
        LEFT JOIN prod."D_Book" bk ON bk."Name" = sta."bookname"

        WHERE sta."rn" = 1
          AND bk."Name" IS NULL

; WITH LastLoaded AS (
    SELECT
        *
        , ROW_NUMBER() OVER (PARTITION BY ("bookname", "chapternumber")
                             ORDER BY "insertiontime" DESC) AS rn
    FROM
        staging."charinchapter"
    )

/* InsertNewChapters */
INSERT INTO prod."D_Chapter" ("ChapterOfBookNumber", "BookId", "Name", "MainCharacterId")
    SELECT
        sta."chapternumber"
        , bk."Id"
        , sta."chaptername"
        , ch."Id"
    FROM LastLoaded sta
    INNER JOIN prod."D_Book" bk ON bk."Name" = sta."bookname"
    INNER JOIN prod."D_Character" ch ON ch."FirstName" = sta."charfirstname"
                                    AND ch."SurName" = sta."charsurname"
    LEFT JOIN prod."D_Chapter" cp ON cp."ChapterOfBookNumber" = sta."chapternumber"
                                  AND cp."BookId" = bk."Id"
    WHERE sta."rn" = 1
      AND cp."ChapterOfBookNumber" IS NULL

; WITH LastLoaded AS (
    SELECT
        *
        , ROW_NUMBER() OVER (PARTITION BY ("bookname", "chapternumber", "charfirstname", "charsurname")
                             ORDER BY "insertiontime" DESC) AS rn
    FROM
        staging."charinchapter"
    )

/* Insert Fact */
INSERT INTO prod."F_PovCharacterInChapter" ("CharacterId", "ChapterId")
    SELECT
        ch."Id"
        , cp."Id"
    FROM LastLoaded sta

    INNER JOIN prod."D_Character" ch ON ch."FirstName" = sta."charfirstname"
                                    AND ch."SurName" = sta."charsurname"

    INNER JOIN prod."D_Book" bk ON bk."Name" = sta."bookname"

    INNER JOIN prod."D_Chapter" cp ON cp."ChapterOfBookNumber" = sta."chapternumber"
                                  AND cp."BookId" = bk."Id"
    LEFT JOIN prod."F_PovCharacterInChapter" pov ON pov."CharacterId" = ch."Id"
                                                AND pov."ChapterId" = cp."Id"
    WHERE sta."rn" = 1
      AND pov."ChapterId" IS NULL



