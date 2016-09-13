/* Insert new Characters */
WITH characters as (
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
        , "Culture"     = COALESCE(st."culture", chr."Culture")
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

    WHERE st."rn" = 1
      AND chr."FirstName" = st."firstname"
      AND chr."SurName" = st."surname"

/*
UPDATE dbo."D_Character" ch
    SET
        gender = '%(gender)s'
        , yearofbirth = %(born)i
        , yearofdeath = %(died)i
    
    WHERE ch.firstname = '%(firstname)s'
      AND ch.surname = '%(surname)s';

    RETURNING ch.id;

SELECT id 
FROM dbo."D_Character"
WHERE firstname = '%(firstname)s'
  AND surname = '%(surname)s'
*/