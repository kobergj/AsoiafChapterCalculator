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
        , ROW_NUMBER() OVER (PARTITION BY ("charfirstname", "charsurname", "chapname")
                             ORDER BY "insertiontime" DESC) AS rn
    FROM
        staging."charinchapter"
    )

/* InsertNewChapters */
UPDATE prod."D_Chapter"
    SET
        "MainCharacterId" = COALESCE(ch."Id", "MainCharacterId")
    FROM LastLoaded sta
    LEFT JOIN prod."D_Character" ch ON ch."FirstName" = sta."charfirstname"
                                    AND ch."SurName" = sta."charsurname"
    WHERE sta."rn" = 1
      AND "Name" = sta."chapname"
