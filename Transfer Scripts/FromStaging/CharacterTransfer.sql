/* Insert new Cultures */
WITH LastLoaded AS (
    SELECT
        *
        , ROW_NUMBER() OVER (PARTITION BY ("culture")
                             ORDER BY "insertiontime" DESC) AS rn
    FROM staging."character"
    )

INSERT INTO prod."D_Culture" ("Name")
    SELECT DISTINCT sta."culture"
    FROM lastloaded sta
    WHERE sta."rn" = 1
      AND sta."culture" IS NOT NULL
      AND NOT EXISTS (
        SELECT 1 FROM prod."D_Culture" cul WHERE cul."Name" = sta."culture"
    )

/* Insert new Characters */
; WITH characters as (
    SELECT "firstname"   as firstname, "surname"   as surname FROM staging."character" UNION ALL
    SELECT "fatherfirst" as firstname, "fathersur" as surname FROM staging."character" UNION ALL
    SELECT "motherfirst" as firstname, "mothersur" as surname FROM staging."character" UNION ALL
    SELECT "spousefirst" as firstname, "spousesur" as surname FROM staging."character"
)

INSERT INTO prod."D_Character" ("FirstName", "SurName") 
    SELECT DISTINCT
        sta."firstname"
        , sta."surname"
    FROM characters sta

    WHERE sta."firstname" IS NOT NULL
      AND sta."surname" IS NOT NULL
      AND NOT EXISTS (
        SELECT 1 
        FROM prod."D_Character" ch
        WHERE ch."FirstName" = sta."firstname"
          AND ch."SurName" = sta."surname"
    )

/* Extract Newest Lines */
; WITH lastloaded as (
    SELECT
        *
        , ROW_NUMBER() OVER (PARTITION BY ("firstname", "surname")
                             ORDER BY "insertiontime" DESC) AS rn
    FROM 
        staging."character" sta
)

/* Update Characters */
UPDATE prod."D_Character" chr
    SET
        "GenderId"      = COALESCE(gen."Id",     chr."GenderId")
        , "YearOfBirth" = COALESCE(st."born",    chr."YearOfBirth")
        , "YearOfDeath" = COALESCE(st."died",    chr."YearOfDeath")
        , "CultureId"   = COALESCE(cul."Id",     chr."CultureId")
        , "FatherId"    = COALESCE(ft."Id",      chr."FatherId")
        , "MotherId"    = COALESCE(mt."Id",      chr."MotherId")
        , "SpouseId"    = COALESCE(sp."Id",      chr."SpouseId")

    FROM lastloaded st
    LEFT JOIN
        prod."D_Gender" gen ON gen."Gendername" = st."gender"
    LEFT JOIN
        prod."D_Character" ft ON ft."FirstName" = st."fatherfirst"
                             AND ft."SurName"  = st."fathersur"
    LEFT JOIN
        prod."D_Character" mt ON mt."FirstName" = st."motherfirst"
                             AND mt."SurName"  = st."mothersur"
    LEFT JOIN
        prod."D_Character" sp ON sp."FirstName" = st."spousefirst"
                             AND sp."SurName"  = st."spousesur"
    LEFT JOIN
        prod."D_Culture" cul  ON cul."Name" = st."culture"

    WHERE st."rn" = 1
      AND chr."FirstName" = st."firstname"
      AND chr."SurName" = st."surname"
