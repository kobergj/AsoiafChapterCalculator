/* Insert New Houses */
; WITH Houses as (
    SELECT "master" as house, "masterbranch"    as branch FROM staging."cadetbranches" UNION ALL
    SELECT "cadet"  as house, "cadetbranch"     as branch FROM staging."cadetbranches"
)

INSERT INTO prod."D_House" ("Name", "Branch")
    SELECT sta."house", sta."branch" FROM Houses sta
    WHERE sta."house" IS NOT NULL
      AND NOT EXISTS ( SELECT 1 FROM prod."D_House" ho
                       WHERE ho."Name" = sta."house"
                       AND ho."Branch" = sta."branch") -- OR ho."Branch" IS NULL)

/* Insert Fact */
; INSERT INTO prod."F_HouseCadetBranches" ("MasterId", "CadetId")
    SELECT
        mas."Id"
        , cad."Id"
    FROM staging."cadetbranches" sta
    INNER JOIN prod."D_House" mas ON mas."Name" = sta."master"
                                  AND mas."Branch" = sta."masterbranch"
    INNER JOIN prod."D_House" cad ON cad."Name" = sta."cadet"
                                  AND cad."Branch" = sta."cadetbranch"
    WHERE NOT EXISTS ( SELECT 1 FROM prod."F_HouseCadetBranches" hdb
                       WHERE hdb."MasterId" = mas."Id"
                         AND hdb."CadetId" = cad."Id"
                      )