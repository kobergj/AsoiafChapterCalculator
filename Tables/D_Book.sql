DROP TABLE IF EXISTS dbo.D_Book;

CREATE TABLE dbo.D_Book (
    Id              SERIAL      PRIMARY KEY
    , Name          VARCHAR(50) NOT NULL
);