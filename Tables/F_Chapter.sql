
IF OBJECT_ID('[dbo].[F_Chapter]') IS NOT NULL
    DROP TABLE [dbo].[F_Chapter]
GO

CREATE TABLE [dbo].[F_Chapter] (
    [Id]    INT     IDENTITY(1,1)    CONSTRAINT [PK_dbo_F_Chapter] PRIMARY KEY
    , Name NvarChar(50)
)

GO
