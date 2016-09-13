/* D_Gender */
WITH GenderNames AS (
    SELECT 'Male'    as Gendername    UNION ALL
    SELECT 'Female'  as Gendername
)

INSERT INTO prod."D_Gender" ("Gendername")
SELECT *
FROM GenderNames

/* D_Book */
; WITH BookNames AS (
    SELECT 'A Game of Thrones'    as Bookname UNION ALL
    SELECT 'A Clash of Kings'     as Bookname UNION ALL
    SELECT 'A Storm of Swords'    as Bookname UNION ALL
    SELECT 'A Dance With Dragons' as Bookname UNION ALL
    SELECT 'A Feast For Crows'    as Bookname
)

INSERT INTO prod."D_Book" ("Name")
SELECT *
FROM BookNames
