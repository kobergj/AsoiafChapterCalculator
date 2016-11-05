DROP TABLE IF EXISTS staging."possession";

CREATE TABLE staging."possession" (
    "description"       VARCHAR(200)    NULL
    , "possessiontype"  VARCHAR(10)     NULL
    , "house"           VARCHAR(50)     NULL
    , "branch"          VARCHAR(50)     NULL
    , "charfirst"       VARCHAR(50)     NULL
    , "charsur"         VARCHAR(50)     NULL
    , "insertiontime"   TIMESTAMP       NOT NULL
);

DROP TABLE IF EXISTS staging."house";

CREATE TABLE staging."house" (
    "name"               VARCHAR(50)     NULL
    , "branch"           VARCHAR(50)     NULL
    , "founderfirst"     VARCHAR(50)     NULL
    , "foundersur"       VARCHAR(50)     NULL
    , "heirfirst"        VARCHAR(50)     NULL
    , "heirsur"          VARCHAR(50)     NULL
    , "lordfirst"        VARCHAR(50)     NULL
    , "lordsur"          VARCHAR(50)     NULL
    , "overlord"         VARCHAR(50)     NULL
    , "overlordbranch"   VARCHAR(50)     NULL
    , "region"           VARCHAR(50)     NULL
    , "founded"          INTEGER         NULL
    , "diedout"          INTEGER         NULL
    , "words"            VARCHAR(200)    NULL
    , "coatofarms"       VARCHAR(500)    NULL
    , "insertiontime"    TIMESTAMP       NOT NULL

);

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

DROP TABLE IF EXISTS staging."charhouserelation";

CREATE TABLE staging."charhouserelation" (
    "first"             VARCHAR(50) NULL
    , "sur"             VARCHAR(50) NULL
    , "house"           VARCHAR(50) NULL
    , "branch"          VARCHAR(50) NULL
    , "relationtype"    VARCHAR(50) NULL
    , "insertiontime"   TIMESTAMP   NOT NULL
);

DROP TABLE IF EXISTS staging."cadetbranches";

CREATE TABLE staging."cadetbranches" (
    "master"            VARCHAR(50) NULL
    , "masterbranch"    VARCHAR(50) NULL
    , "cadet"           VARCHAR(50) NULL
    , "cadetbranch"     VARCHAR(50) NULL
    , "insertiontime"   TIMESTAMP   NOT NULL
);
