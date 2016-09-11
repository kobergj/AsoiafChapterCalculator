WITH LastLoaded AS (
    SELECT
        *
        , ROW_NUMBER() OVER (PARTITION BY ("bookname")
                             ORDER BY "insertiontime" DESC) AS rn
    FROM
        staging."chapter"
    )

/* Insert new Books */
INSERT INTO prod."D_Book" ("Name")
    SELECT DISTINCT sta."bookname"
    FROM lastloaded sta
    WHERE sta."rn" = 1
      AND NOT EXISTS (
        SELECT 1 FROM prod."D_Book" bk WHERE bk."Name" = sta."bookname"
    )

; WITH LastLoaded AS (
    SELECT
        *
        , ROW_NUMBER() OVER (PARTITION BY ("bookname", "chapternumber")
                             ORDER BY "insertiontime" DESC) AS rn
    FROM
        staging."chapter"
    )

/* Insert new Chapters */
INSERT INTO prod."D_Chapter" ("ChapterOfBookNumber", "BookId")
    SELECT DISTINCT
        sta."chapternumber"
        , bk."Id"
    FROM lastloaded sta
    INNER JOIN prod."D_Book" bk ON bk."Name" = sta."bookname"
    WHERE sta."rn" = 1
      AND NOT EXISTS (
        SELECT 1 
        FROM prod."D_Chapter" ch
        WHERE ch."ChapterOfBookNumber" = sta."chapternumber"
          AND ch."BookId" = bk."Id"
        )

/* Get Last Loaded Line */
; WITH LastLoaded AS (
    SELECT
        *
        , ROW_NUMBER() OVER (PARTITION BY ("bookname", "chapternumber")
                             ORDER BY "insertiontime" DESC) AS rn
    FROM
        staging."chapter"
    )

/* Update Chapters */
UPDATE prod."D_Chapter"
    SET
        "Name" = sta."chaptername"
    FROM 
        lastloaded sta
    INNER JOIN
        prod."D_Book" bk ON bk."Name" = sta."bookname"
    WHERE "BookId" = bk."Id"
      AND "ChapterOfBookNumber" = sta."chapternumber"

