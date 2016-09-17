DROP TABLE IF EXISTS prod."F_HouseCadetBranches";

CREATE TABLE prod."F_HouseCadetBranches" (
    "CadetId"               INTEGER         NOT NULL    -- Reference to D_House
    , "MasterId"            INTEGER         NOT NULL    -- Reference to D_House
    -- Branchingbegin
    , "YearOfBranching"     INTEGER         NULL        -- Year
    , "ReasonOfBranching"   VARCHAR(250)    NULL        -- Story of Branching
);