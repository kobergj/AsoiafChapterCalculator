/* Insert new Characters */
INSERT INTO prod."D_Character" ("FirstName", "SurName") 
    SELECT
        sta."firstname"
        , sta."surname"
    FROM staging."character" sta

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
        sta."firstname"
        , sta."surname"
        , max(sta."insertiontime") as insertiontime
    FROM 
        staging."character" sta
    GROUP BY
        sta."firstname"
        , sta."surname"
)

/* Update Characters */
UPDATE prod."D_Character"
    SET
        "Gender" = COALESCE(st."gender", "Gender")
        , "YearOfBirth" = COALESCE(st."born", "YearOfBirth")
        , "YearOfDeath" = COALESCE(st."died", "YearOfDeath")

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