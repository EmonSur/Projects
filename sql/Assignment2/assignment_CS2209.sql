--First lets create the various tables needed--
-----------------------------------------------
CREATE TABLE 'Users' (
    UserID INT PRIMARY KEY,
    'Username' VARCHAR(50),
    'Email' VARCHAR (50),
    'Password' VARCHAR(50),
    'Role' VARCHAR(50)
);

CREATE TABLE 'Templates' (
    TemplateID INT PRIMARY KEY,
    'TemplateName' VARCHAR(50),
    'Guidelines' VARCHAR(1000),
    'CreationDate' DATETIME,
    'ModifiedDate' DATETIME,
    'DefaultAIModel' VARCHAR(50)
);

CREATE TABLE 'TemplateCreation' (
    UserID INT,
    TemplateID INT,
    Primary KEY (UserID, TemplateID),
    FOREIGN KEY (UserID) REFERENCES 'Users'(UserID),
    FOREIGN KEY (TemplateID) REFERENCES 'Templates'(TemplateID)
);

CREATE TABLE 'TemplateSaves' (
    UserID INT,
    TemplateID INT,
    Primary KEY (UserID, TemplateID),
    FOREIGN KEY (UserID) REFERENCES 'Users'(UserID),
    FOREIGN KEY (TemplateID) REFERENCES 'Templates'(TemplateID)
);

CREATE TABLE 'Shortcuts' (
    ShortcutID INT PRIMARY KEY,
    TemplateID INT,
    'Action' VARCHAR(250),
    'KeyCombination' VARCHAR(50),
    FOREIGN KEY (TemplateID) REFERENCES 'Templates'(TemplateID)
);

CREATE TABLE 'Labels' (
    LabelID INT PRIMARY KEY,
    TemplateID INT,
    'LabelName' VARCHAR(255),
    'Colour' VARCHAR(255),
    FOREIGN KEY (TemplateID) REFERENCES 'Templates'(TemplateID)
);

CREATE TABLE 'LabelAttributes' (
    LabelAttributeID INT PRIMARY KEY,
    LabelID INT,
    'AttributeName' VARCHAR(255),
    'ValueType' VARCHAR(255),
    'DefaultValue' VARCHAR(255),
    FOREIGN KEY (LabelID) REFERENCES 'Labels'(LabelID)
);


--Now lets insert some dummy data into these tables--
-----------------------------------------------------
INSERT INTO 'Users' (UserID, 'Username', 'Email', 'Password', 'Role')
VALUES
    (1, 'John Doe', 'johndoe@gmail.com', 'password1', 'Admin'),
    (2, 'Jane Doe', 'janedoe@gmail.com', 'password2', 'Admin'),
    (3, 'Sean Doe', 'seandoe@gmail.com', 'password3', 'User');


INSERT INTO 'Templates' (TemplateID, 'TemplateName', 'Guidelines', 'CreationDate', 'ModifiedDate', 'DefaultAIModel')
VALUES 
    (1, 'Vehicle Detection', 'Use boxes when annotating vehicles. Pay special attention to bicycles and motorcycles, which might be less visible', '2023-02-01 14:22:56', '2024-04-12 23:43:11', 'YOLOv4'),
    (2, 'Customer Tracking', 'Use ovals when annotating all the people entering and leaving the shop, and tag each which actions such as entering, leaving, or browsing. Ensure the right timestamp is used for actions', '2025-09-30 07:55:56', '2029-10-07 11:09:11', 'DeepLabv3+'),
    (3, 'Park Animal Tracking', 'Labels should be tagged by the species of the animal, and any interactions between animals should also be noted. If part of a group of the same species, note group size.', '2024-11-23 19:57:57', '2024-11-23 19:57:57', 'Mask R-CNN');

INSERT INTO 'TemplateCreation' (UserID, TemplateID)
VALUES
    (1, 3),
    (2, 2), 
    (1, 1);

INSERT INTO 'TemplateSaves' (UserID, TemplateID)
VALUES
    (1, 1),
    (1, 2),
    (1, 3),
    (2, 2), 
    (3, 1), 
    (3, 2);

INSERT INTO Shortcuts (ShortcutID, TemplateID, 'Action', 'KeyCombination')
VALUES
    (1, 1, 'Continue to the next frame', 'Ctrl+Right'),
    (2, 1, 'Go back to the last frame', 'Ctrl+Left'),
    (3, 1, 'Mark this frame as important', 'Ctrl+I'),
    (4, 2, 'Continue to the next frame', 'Ctrl+Right'),
    (5, 2, 'Go back to the last frame', 'Ctrl+Left'),
    (6, 2, 'Mark this frame for deletion', 'Ctrl+D+L'),
    (7, 2, 'Return to this frame later', 'Ctrl+L'),
    (8, 3, 'Continue to the next frame', 'Ctrl+Right'),
    (9, 3, 'Go back to the last frame', 'Ctrl+Left');

INSERT INTO Labels (labelID, TemplateID, 'LabelName', 'Colour')
VALUES
    (1, 1, 'Car', '#000000'),
    (2, 1, 'Bicycle', '#ff0000'),
    (3, 2, 'Employee', '#000000'),
    (4, 2, 'Customer', '#0000ff'),
    (5, 3, 'Owl', '#000000');

INSERT INTO LabelAttributes (LabelAttributeID, LabelID, 'AttributeName', 'ValueType', 'DefaultValue')
VALUES
    (1, 1, 'Vehicle Type', 'String', 'Car'),
    (2, 2, 'Vehicle Type', 'String', 'Bicycle'),
    (3, 1, 'Condition', 'String', 'Used'),
    (4, 2, 'Colour', 'String', 'Red'),
    (5, 3, 'Activity', 'String', 'Folding T-shirts'),
    (6, 4, 'Age Group', 'String', 'Teen'),
    (7, 5, 'Species', 'String', 'Bird'),
    (8, 5, 'Group Size', 'Integer', '1');



--Finally lets use some SQL queries to illustrate my ideas--
------------------------------------------------------------

--Find all the templates created by a specific user, and also note the number of times each has been saved to a users 'Favourites'--
SELECT t.TemplateName, COUNT(ts.UserID) as TimesSaved
FROM Templates as t JOIN TemplateCreation as tc ON t.TemplateID = tc.TemplateID
LEFT JOIN TemplateSaves as ts ON t.TemplateID = ts.TemplateID
WHERE tc.UserID = 1
GROUP BY t.TemplateID, t.TemplateName;

--Get all the details related to a specific template, including all labels and the labels's default attributes--
SELECT t.TemplateName, t.Guidelines, l.LabelName, l.Colour, la.AttributeName, la.DefaultValue
FROM Templates as t JOIN Labels as l ON t.TemplateID = l.TemplateID JOIN LabelAttributes as la ON l.LabelID = la.LabelID
WHERE t.TemplateID = 1;

--Get all the shortcuts related to a specific template--
SELECT t.TemplateName, s.Action, s.KeyCombination
FROM Templates as t JOIN Shortcuts as s ON t.TemplateID = s.TemplateID
WHERE t.TemplateID = 1;

--Display the stats related to the templates, including who created it, how many times it has been saved, and the most recent occasion it was modified--
SELECT t.TemplateName, u.Username as Creator, COUNT(ts.UserID) as TimesSaved, MAX(t.ModifiedDate) as LastModified
FROM Templates as t JOIN TemplateCreation as tc ON T.TemplateID = tc.TemplateID JOIN Users as U ON tc.UserID = u.UserID
LEFT JOIN TemplateSaves as ts ON t.TemplateID = ts.TemplateID
GROUP BY t.TemplateID, t.TemplateName, u.Username;

