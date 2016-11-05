/* D_Gender */
WITH GenderNames AS (
    SELECT 'Male'    as gendername    UNION ALL
    SELECT 'Female'  as gendername
)

INSERT INTO prod."D_Gender" ("Gendername")
SELECT "gendername" FROM GenderNames
EXCEPT SELECT "Gendername" FROM prod."D_Gender"

/* D_Book */
; WITH BookNames AS (
    SELECT 'A Game of Thrones'    as bookname UNION ALL
    SELECT 'A Clash of Kings'     as bookname UNION ALL
    SELECT 'A Storm of Swords'    as bookname UNION ALL
    SELECT 'A Dance With Dragons' as bookname UNION ALL
    SELECT 'A Feast For Crows'    as bookname
)

INSERT INTO prod."D_Book" ("Name")
SELECT "bookname" FROM BookNames
EXCEPT SELECT "Name" FROM prod."D_Book"

/* D_PossessionType */
; WITH PossessionTypes AS (
    SELECT 'Seat'       as name UNION ALL
    SELECT 'Title'      as name UNION ALL
    SELECT 'Alias'      as name UNION ALL
    SELECT 'Weapon'     as name
)

INSERT INTO prod."D_PossessionType" ("Name")
SELECT "name" FROM PossessionTypes
EXCEPT SELECT "Name" FROM prod."D_PossessionType"

/* D_PossessionType */
; WITH RelationTypes AS (
    SELECT 'Member'     as name UNION ALL
    SELECT 'Allegiance' as name UNION ALL
    SELECT 'Enemy'      as name
)

INSERT INTO prod."D_RelationType" ("Name")
SELECT "name" FROM RelationTypes
EXCEPT SELECT "Name" FROM prod."D_RelationType"
