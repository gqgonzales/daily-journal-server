CREATE TABLE IF NOT EXISTS `Entries` (
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `entry_date` DATE NOT NULL,
    `concept` TEXT NOT NULL,
    `body` TEXT NOT NULL,
    `mood_id` INTEGER NOT NULL,
    FOREIGN KEY(`mood_id`) REFERENCES `Moods`(`id`)
);
CREATE TABLE IF NOT EXISTS `Moods` (
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `label` TEXT NOT NULL
);
INSERT INTO `Moods`
VALUES (null, "Happy");
INSERT INTO `Moods`
VALUES (null, "Sad");
INSERT INTO `Moods`
VALUES (null, "Frustrated");
INSERT INTO `Moods`
VALUES (null, "Ok");
INSERT INTO `Entries`
VALUES (
        null,
        "2021-01-01",
        "Learning about JavaScript",
        "Sample Entry Body Here",
        1
    );
INSERT INTO `Entries`
VALUES (
        null,
        "2021-01-10",
        "Understanding bridge tables",
        "Sample Entry Body Here",
        3
    );
INSERT INTO `Entries`
VALUES (
        null,
        "2021-01-31",
        "Getting comfortable with React",
        "Sample Entry Body Here",
        4
    );
INSERT INTO `Entries`
VALUES (
        null,
        "2021-02-05",
        "Advanced styling with Sass",
        "Sample Entry Body Here",
        1
    );
INSERT INTO `Entries`
VALUES (
        null,
        "2021-01-11",
        "Building tables with SQL",
        "Sample Entry Body Here",
        4
    );
INSERT INTO `Entries`
VALUES (
        null,
        "2021-01-18",
        "Navigating Python",
        "Sample Entry Body Here",
        2
    );
SELECT *
FROM Entries e
    JOIN Moods m ON m.id = e.mood_id;

DROP TABLE IF EXISTS `Entries`;