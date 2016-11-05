echo Initial
psql AsoiafDWH -f InitialData/initial.sql
echo Chapters
psql AsoiafDWH -f Transfer\ Scripts/FromStaging/ChapterTransfer.sql
echo Characters
psql AsoiafDWH -f Transfer\ Scripts/FromStaging/CharacterTransfer.sql
echo Houses
psql AsoiafDWH -f Transfer\ Scripts/FromStaging/HouseTransfer.sql
echo Main Chars
psql AsoiafDWH -f Transfer\ Scripts/FromStaging/MainCharInChapterTransfer.sql
echo Possessions
psql AsoiafDWH -f Transfer\ Scripts/FromStaging/HousePossessionTransfer.sql
