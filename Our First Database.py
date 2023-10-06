CREATE TABLE Ages (
  name VARCHAR(128),
  age INTEGER
)

DELETE FROM Ages;
INSERT INTO Ages (name, age) VALUES ('Zubair', 13);
INSERT INTO Ages (name, age) VALUES ('Alessandra', 25);
INSERT INTO Ages (name, age) VALUES ('Angali', 18);
INSERT INTO Ages (name, age) VALUES ('Natalia', 28);
INSERT INTO Ages (name, age) VALUES ('Corinn', 40);

SELECT hex(name || age) AS X FROM Ages ORDER BY X