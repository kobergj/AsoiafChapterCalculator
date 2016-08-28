DROP TABLE IF EXISTS staging."character";

CREATE TABLE staging."character" (
    "firstname"         VARCHAR(50)     NULL
    , "surname"         VARCHAR(50)     NULL
    , "gender"          VARCHAR(10)     NULL
    , "born"            INTEGER         NULL
    , "died"            INTEGER         NULL
    , "insertiontime"   TIMESTAMP       NOT NULL
);

DROP TABLE IF EXISTS staging."charinchapter";

CREATE TABLE staging."charinchapter" (
    "charfirstname"     VARCHAR(50)     NULL
    , "charsurname"     VARCHAR(50)     NULL
    , "bookname"        VARCHAR(20)     NULL
    , "chaptername"     VARCHAR(50)     NULL
    , "chapternumber"   INTEGER         NULL
    , "insertiontime"   TIMESTAMP       NOT NULL
);
