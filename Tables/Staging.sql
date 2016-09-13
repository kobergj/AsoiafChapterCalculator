DROP TABLE IF EXISTS staging."character";

CREATE TABLE staging."character" (
    "firstname"         VARCHAR(50)     NULL
    , "surname"         VARCHAR(50)     NULL
    , "gender"          VARCHAR(10)     NULL
    , "born"            INTEGER         NULL
    , "died"            INTEGER         NULL
    , "culture"         VARCHAR(50)     NULL
    , "fatherfirst"     VARCHAR(50)     NULL
    , "fathersur"       VARCHAR(50)     NULL
    , "motherfirst"     VARCHAR(50)     NULL
    , "mothersur"       VARCHAR(50)     NULL
    , "spousefirst"     VARCHAR(50)     NULL
    , "spousesur"       VARCHAR(50)     NULL
    , "insertiontime"   TIMESTAMP       NOT NULL
);

DROP TABLE IF EXISTS staging."charinchapter";

CREATE TABLE staging."charinchapter" (
    "charfirstname"     VARCHAR(50)     NULL
    , "charsurname"     VARCHAR(50)     NULL
    , "chapname"        VARCHAR(50)     NULL
    , "insertiontime"   TIMESTAMP       NOT NULL
);

DROP TABLE IF EXISTS staging."chapter";

CREATE TABLE staging."chapter" (
    "bookname"          VARCHAR(20)     NULL
    , "chaptername"     VARCHAR(50)     NULL
    , "chapternumber"   INTEGER         NULL
    , "insertiontime"   TIMESTAMP       NOT NULL
);
