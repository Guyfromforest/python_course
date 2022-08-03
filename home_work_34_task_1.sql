СREATE DATABASE task1.db;
CREATE TABLE Ukrainian_city(
Post_code INTEGER PRIMERY KEY,
Name Varchar
);
INSERT INTO Ukrainian_city VALUES(01001, "Kyiv");
INSERT INTO Ukrainian_city VALUES(07400, "Brovary");
DELETE FROM Ukrainian_city
WHERE Name = "Brovary";
UPDATE INTO Ukrainian_city
SET Post_code = 01100
WHERE Name = "Kyiv";
DROP task1.db.Ukrainian_city;

