psql AsoiafDWH -f InitialData/initial.sql

psql AsoiafDWH -f Transfer\ Scripts/FromStaging/ChapterTransfer.sql
psql AsoiafDWH -f Transfer\ Scripts/FromStaging/CharacterTransfer.sql
psql AsoiafDWH -f Transfer\ Scripts/FromStaging/HouseTransfer.sql

psql AsoiafDWH -f Transfer\ Scripts/FromStaging/MainCharInChapterTransfer.sql
