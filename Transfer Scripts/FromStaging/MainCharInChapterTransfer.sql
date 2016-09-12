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

/* InsertNewCharacters */
INSERT INTO prod."F_EventInChapter" ("ChapterId", "MainCharacterId")
    SELECT DISTINCT
        chp."Id"
        , cha."Id"
    FROM LastLoaded sta
    LEFT JOIN prod."D_Character" cha ON cha."FirstName" = sta."charfirstname"
                                    AND cha."SurName" = sta."charsurname"
    INNER JOIN prod."D_Chapter" chp ON chp."Name" = sta."chapname"

    WHERE sta."rn" = 1
