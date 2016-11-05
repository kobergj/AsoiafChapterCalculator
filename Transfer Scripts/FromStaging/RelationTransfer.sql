/* Insert New Characters */
; WITH LastLoaded as (
    SELECT
        *
        , ROW_NUMBER() OVER (PARTITION BY ("first", "sur")
                            ORDER BY "insertiontime" DESC) as rn
    FROM staging."charhouserelation"
)

INSERT INTO prod."D_Character" ("FirstName", "SurName")
    SELECT sta."first", sta."sur" FROM LastLoaded sta
    WHERE sta."rn" = 1
      AND sta."first" IS NOT NULL
      AND sta."sur" IS NOT NULL
      AND NOT EXISTS ( SELECT 1 FROM prod."D_Character" ch
                       WHERE ch."FirstName" = sta."first" AND ch."SurName" = sta."sur")

/* Insert New Houses */
; WITH LastLoaded as (
    SELECT
        *
        , ROW_NUMBER() OVER (PARTITION BY ("house", "branch")
                            ORDER BY "insertiontime" DESC) as rn
    FROM staging."charhouserelation"
)

 INSERT INTO prod."D_House" ("Name", "Branch")
    SELECT sta."house", sta."branch" FROM LastLoaded sta
    WHERE sta."rn" = 1
      AND sta."house" IS NOT NULL
      AND NOT EXISTS ( SELECT 1 FROM prod."D_House" ho
                       WHERE ho."Name" = sta."house"
                       AND (ho."Branch" = sta."branch" 
                            OR (ho."Branch" IS NULL AND sta."branch" IS NULL)
                            )
                       )

/* Insert Fact */
; WITH LastLoaded as (
    SELECT
        *
        , ROW_NUMBER() OVER (PARTITION BY ("house", "branch", "first", "sur", "relationtype")
                            ORDER BY "insertiontime" DESC) as rn
    FROM staging."charhouserelation"
)


INSERT INTO prod."F_CharacterHouseRelation" ("HouseId", "CharacterId", "RelationTypeId")
    SELECT
        hou."Id"
        , cha."Id"
        , rel."Id"
    FROM LastLoaded sta
    INNER JOIN prod."D_House" hou ON hou."Name" = sta."house"
                                  AND hou."Branch" = sta."branch"
    INNER JOIN prod."D_RelationType" rel ON rel."Name" = sta."relationtype"
    INNER JOIN prod."D_Character" cha ON cha."FirstName" = sta."first"
                                       AND cha."SurName" = sta."sur"
    WHERE sta."rn" = 1
      AND NOT EXISTS ( SELECT 1 FROM prod."F_CharacterHouseRelation" chr
                       WHERE chr."HouseId" = hou."Id"
                         AND chr."CharacterId" = cha."Id"
                         AND chr."RelationTypeId" = rel."Id"
                         )

