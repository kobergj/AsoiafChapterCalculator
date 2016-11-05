/* Insert New Houses */
; WITH Houses as (
    SELECT
        *
        , ROW_NUMBER() OVER ( PARTITION BY ("house", "branch")
                            ORDER BY "insertiontime" DESC ) as rn
    FROM staging."possession"
)

INSERT INTO prod."D_House" ("Name", "Branch")
    SELECT sta."house", sta."branch" 
    FROM Houses sta
    WHERE sta."house" IS NOT NULL
      AND sta."rn" = 1
      AND NOT EXISTS ( SELECT 1 FROM prod."D_House" ho
                       WHERE ho."Name" = sta."house"
                       AND ho."Branch" = sta."branch" -- OR ho."Branch" IS NULL
)

/* Insert New Possessions */
; WITH Possessions as (
    SELECT
        *
        , ROW_NUMBER() OVER ( PARTITION BY ("description", "possessiontype")
                            ORDER BY "insertiontime" DESC ) as rn
    FROM staging."possession"
)

INSERT INTO prod."D_Possession" ("Description", "PossessionTypeId")
    SELECT
        sta."description"
        , pt."Id"
    FROM Possessions sta
    INNER JOIN prod."D_PossessionType" pt ON pt."Name" = sta."possessiontype"
    WHERE sta."rn" = 1
      AND NOT EXISTS ( SELECT 1 FROM prod."D_Possession" ho
                       WHERE ho."Description" = sta."description" AND ho."PossessionTypeId" = pt."Id"
)

/* Insert Fact */
; INSERT INTO prod."F_PossessionOfHouse" ("HouseId", "PossessionId")
    SELECT DISTINCT
        hou."Id"
        , pos."Id"
    FROM staging."possession" sta
    INNER JOIN prod."D_House" hou ON hou."Name" = sta."house"
                                  AND hou."Branch" = sta."branch"
    INNER JOIN prod."D_PossessionType" pt ON pt."Name" = sta."possessiontype"
    INNER JOIN prod."D_Possession" pos ON pos."Description" = sta."description"
                                       AND pos."PossessionTypeId" = pt."Id"
    WHERE NOT EXISTS ( SELECT 1 FROM prod."F_PossessionOfHouse" poh
                       WHERE poh."HouseId" = hou."Id" AND poh."PossessionId" = pos."Id")
