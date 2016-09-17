/* Get Last Loaded Info */
WITH LastLoaded AS (
    SELECT
        *
        , ROW_NUMBER() OVER (PARTITION BY ("charfirstname", "charsurname")
                             ORDER BY "insertiontime" DESC) AS rn
    FROM
        staging."charinchapter"
    WHERE "charfirstname" IS NOT NULL
      AND "charsurname" IS NOT NULL
    )

/* InsertNewCharacters */
INSERT INTO prod."D_Character" ("FirstName", "SurName") 
    SELECT
        sta."charfirstname"
        , sta."charsurname"
    FROM LastLoaded sta
    WHERE sta."rn" = 1
      AND NOT EXISTS ( SELECT 1 FROM prod."D_Character" ch
                        WHERE ch."FirstName" = sta."charfirstname"
                          AND ch."SurName" = sta."charsurname"
                )

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
    SELECT
        chp."Id"
        , cha."Id"
    FROM LastLoaded sta
    LEFT JOIN prod."D_Character" cha ON cha."FirstName" = sta."charfirstname"
                                    AND cha."SurName" = sta."charsurname"
    INNER JOIN prod."D_Chapter" chp ON chp."Name" = sta."chapname"

    WHERE sta."rn" = 1
      AND NOT EXISTS ( SELECT 1 FROM prod."F_EventInChapter" eic
                       WHERE eic."ChapterId" = chp."Id" AND eic."MainCharacterId" = cha."Id" )
