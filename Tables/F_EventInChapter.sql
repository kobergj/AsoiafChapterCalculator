DROP TABLE IF EXISTS prod."F_EventInChapter";

CREATE TABLE prod."F_EventInChapter" (
    "ChapterId"                 INT             NOT NULL    -- Reference to D_Chapter
    , "MainCharacterId"         INT             NOT NULL    -- POV Character of the Chapter - Ref to D_Character

    -- Descriptives
    , "InteractingCharacterId"  INT             NULL        -- Secondary Character of the Event - Ref to D_Character
    , "EventDescription"        VARCHAR(250)    NULL        -- Short Description of Event
);