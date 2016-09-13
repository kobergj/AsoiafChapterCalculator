/* Update Chapters */
; WITH LastLoaded AS (
    SELECT
        *
        , ROW_NUMBER() OVER (PARTITION BY ("bookname", "chapternumber")
                             ORDER BY "insertiontime" DESC) AS rn
    FROM
        staging."chapter"
    )

UPDATE prod."D_Chapter"
    SET
        "Name" = sta."chaptername"
    FROM 
        lastloaded sta
    INNER JOIN
        prod."D_Book" bk ON bk."Name" = sta."bookname"
    WHERE "BookId" = bk."Id"
      AND "ChapterOfBookNumber" = sta."chapternumber"

/* Insert new Chapters */
; WITH LastLoaded AS (
    SELECT
        *
        , ROW_NUMBER() OVER (PARTITION BY ("bookname", "chapternumber")
                             ORDER BY "insertiontime" DESC) AS rn
    FROM
        staging."chapter"
    )

INSERT INTO prod."D_Chapter" ("ChapterOfBookNumber", "BookId", "Name")
    SELECT DISTINCT
        sta."chapternumber"
        , bk."Id"
        , sta."chaptername"
    FROM lastloaded sta
    INNER JOIN prod."D_Book" bk ON bk."Name" = sta."bookname"
    WHERE sta."rn" = 1
      AND NOT EXISTS (
        SELECT 1 
        FROM prod."D_Chapter" ch
        WHERE ch."ChapterOfBookNumber" = sta."chapternumber"
          AND ch."BookId" = bk."Id"
        )


