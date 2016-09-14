/* Insert New Regions */
INSERT INTO prod."D_Region" ("Name")
    SELECT DISTINCT sta."region" FROM staging."house" sta
    WHERE sta."region" IS NOT NULL
      AND NOT EXISTS ( SELECT 1 FROM prod."D_Region" rg WHERE rg."Name" = sta."region")

/* Insert New Characters */
; WITH Characters as (
    SELECT "founderfirst" as first, "foundersur" as sur FROM staging."house" UNION ALL
    SELECT "heirfirst"    as first, "heirsur"    as sur FROM staging."house" UNION ALL
    SELECT "lordfirst"    as first, "lordsur"    as sur FROM staging."house"
)

INSERT INTO prod."D_Character" ("FirstName", "SurName")
    SELECT DISTINCT sta."first", sta."sur" FROM Characters sta
    WHERE sta."first" IS NOT NULL
      AND sta."sur" IS NOT NULL
      AND NOT EXISTS ( SELECT 1 FROM prod."D_Character" ch
                       WHERE ch."FirstName" = sta."first" AND ch."SurName" = sta."sur")

; WITH Houses as (
    SELECT "name" as name, "branch" as branch FROM staging."house" UNION ALL
    SELECT "overlord" as name, "overlordbranch" as branch FROM staging."house"
)

INSERT INTO prod."D_House" ("Name", "Branch")
    SELECT DISTINCT sta."name", sta."branch" FROM Houses sta
    WHERE sta."name" IS NOT NULL
      AND sta."branch" IS NOT NULL
      AND NOT EXISTS ( SELECT 1 FROM prod."D_House" ho
                       WHERE ho."Name" = sta."name" AND ho."Branch" = sta."branch")


; WITH LastLoaded as (
    SELECT
        *
        , ROW_NUMBER() OVER ( PARTITION BY ("name", "branch")
                            ORDER BY "insertiontime" DESC ) as rn
    FROM staging."house"
)

UPDATE prod."D_House" hou
    SET
        "CurrentLordId"             = COALESCE(cl."Id", hou."CurrentLordId")
        , "HeirId"                  = COALESCE(hr."Id", hou."HeirId")
        , "FounderId"               = COALESCE(fd."Id", hou."FounderId")

        , "OverlordHouseId"         = COALESCE(ov."Id", hou."OverlordHouseId")
        , "RegionId"                = COALESCE(rg."Id", hou."RegionId")

        , "FoundedAt"               = COALESCE(sta."founded", hou."FoundedAt")
        , "DiedOutAt"               = COALESCE(sta."diedout", hou."DiedOutAt")
        , "Words"                   = COALESCE(sta."words", hou."Words")
        , "CoatOfArmsDescription"   = COALESCE(sta."coatofarms", hou."CoatOfArmsDescription")

    FROM LastLoaded as sta

    LEFT JOIN prod."D_Character" cl ON cl."FirstName" = sta."lordfirst"
                                    AND cl."SurName" = sta."lordsur"
    LEFT JOIN prod."D_Character" hr ON hr."FirstName" = sta."heirfirst"
                                    AND hr."SurName" = sta."heirsur"
    LEFT JOIN prod."D_Character" fd ON fd."FirstName" = sta."founderfirst"
                                    AND fd."SurName" = sta."foundersur"
    LEFT JOIN prod."D_House" ov ON ov."Name" = sta."overlord"
                                AND ov."Branch" = sta."overlordbranch"
    LEFT JOIN prod."D_Region" rg ON rg."Name" = sta."region"

    WHERE sta."rn" = 1
      AND hou."Name" = sta."name"
      AND hou."Branch" = sta."branch"