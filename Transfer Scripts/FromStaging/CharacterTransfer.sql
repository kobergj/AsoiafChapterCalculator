/* Insert new Characters */
WITH characters as (
    SELECT
        sta."firstname"   as firstname, sta."surname"   as surname UNION ALL
        sta."fatherfirst" as firstname, sta."fathersur" as surname UNION ALL
        sta."motherfirst" as firstname, sta."mothersur" as surname UNION ALL
        sta."spousefirst" as firstname, sta."spousesur" as surname
    FROM staging."character" sta
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
    );

/* Extract Newest Lines */
WITH lastloaded as (
    SELECT
        *
        , ROW_NUMBER() OVER (PARTITION BY ("firstname", "surname")
                             ORDER BY "insertiontime" DESC) AS rn
    FROM 
        staging."character" sta
)

/* Update Characters */
UPDATE prod."D_Character"
    SET
        "Gender" = COALESCE(st."gender", "Gender")
        , "YearOfBirth" = COALESCE(st."born", "YearOfBirth")
        , "YearOfDeath" = COALESCE(st."died", "YearOfDeath")
        , 

    FROM staging."character" st

    INNER JOIN lastloaded ll ON ll."firstname" = st."firstname"
                            AND ll."surname" = st."surname"
                            AND ll."insertiontime" = st."insertiontime"

    WHERE "FirstName" = st."firstname"
      AND "SurName" = st."surname"

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