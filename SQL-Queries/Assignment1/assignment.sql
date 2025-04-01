CREATE TABLE `Orders` (
    `orderID` INT AUTOINCREMENT PRIMARY KEY,
    `userID` INT,
    `date` DATETIME,
    `totalAmount` DECIMAL(10,2),
    `status` VARCHAR(500)
    FOREIGN KEY (`userId`) REFERENCES `users`(`userID`)
);

INSERT INTO `Orders` (`userID`, `date`, `totalAmount`, `status`) 
VALUES
    (1, '2023-11-11 10:00:00', 150.00, 'Processing'),
    (2, '2023-11-14 11:30:00', 200.50, 'Shipped'),
    (3, '2023-11-16 09:45:00', 99.99, 'Delivered'),
    (4, '2023-11-12 14:00:00', 300.00, 'Processing'),
    (5, '2023-11-11 16:00:00', 450.00, 'Cancelled'),
    (6, '2023-11-10 17:00:00', 850.00, 'Returned');




CREATE TABLE `OrderItems` (
    `orderItemsID` INT AUTOINCREMENT PRIMARY KEY,
    `productID` INT,
    `orderID` INT,
    `quantity` INT,
    FOREIGN KEY (`productID`) REFERENCES `product`(`productID`),
    FOREIGN KEY (`orderID`) REFERENCES `orders`(`orderID`)
);

INSERT INTO `OrderItems` (`productID`, `orderID`, `quantity`) 
VALUES
    (1, 1, 2),
    (2, 1, 1),
    (3, 2, 3),
    (4, 2, 1),
    (5, 3, 2),
    (1, 3, 1),
    (2, 4, 1),
    (3, 4, 2),
    (4, 5, 1),
    (5, 6, 3);




CREATE TABLE `Returns` (
    `returnsID` INT AUTOINCREMENT PRIMARY KEY,
    `orderitemID` INT,
    `userID` INT,
    `reason` VARCHAR(500),
    `requestDATE` DATETIME,
    `status` VARCHAR(100),
    `quantity` INT,
    `refundAmount` DECIMAL(10,2)
    FOREIGN KEY (`orderitemID`) REFERENCES `orderItems`(`orderItemID`)
    FOREIGN KEY (`userId`) REFERENCES `users`(`userID`)
);

INSERT INTO `Returns` (`orderitemID`, `userID`, `reason`, `requestDATE`, `status`, `quantity`, `refundAmount`) 
VALUES
    (1, 1, 'Too large', '2023-11-17 10:00:00', 'Pending', 1, 75.00),
    (2, 2, 'Incorrect item', '2023-11-17 12:30:00', 'Approved', 1, 200.50),
    (3, 3, 'Changed mind', '2023-11-17 14:45:00', 'Completed', 1, 99.99);




CREATE TABLE `ProductCategories` (
    `productCategoryID` INT AUTOINCREMENT PRIMARY KEY,
    `name` VARCHAR(200),
    `description` VARCHAR(500)
);

INSERT INTO `ProductCategories` (`name`, `description`) 
VALUES
    ('T-Shirts', 'Casual cotton T-shirts for everyday wear'),
    ('Jeans', 'Denim jeans available in various styles and sizes'),
    ('Dresses', 'Includes summer, cocktail, and evening dresses'),
    ('Jackets', 'Outdoor and fashion jackets for all seasons'),
    ('Shoes', 'Footwear including sneakers, formal shoes, and boots'),
    ('Accessories', 'Belts, hats, scarves, and more to complement your style');




CREATE TABLE `Colours` (
    `coloursID` INT AUTOINCREMENT PRIMARY KEY,
    `colourName` VARCHAR(100)
),

INSERT INTO `Colours` (`colourName`) 
VALUES
    ('Black'),
    ('White'),
    ('Red'),
    ('Blue'),
    ('Green'),
    ('Orange'),
    ('Grey');


CREATE TABLE ProductColours (
    `colourID` INT,
    `productID` INT,
    PRIMARY KEY (`colourID`, `productID`),
    FOREIGN KEY (`colourID`) REFERENCES `Colours`(`colourID`),
    FOREIGN KEY (`productID`) REFERENCES `Products`(`productID`)
);

INSERT INTO `ProductColours` (`colourID`, `productID`) 
VALUES
    (1, 1),
    (1, 2),
    (2, 3),
    (2, 4),
    (3, 5),
    (3, 6),
    (4, 7),
    (4, 8),
    (5, 9),
    (5, 10);

CREATE TABLE `users` (
    `userID` INT AUTO_INCREMENT PRIMARY KEY,
    `username` VARCHAR(100),
    `email` VARCHAR(100),
    `password` VARCHAR(100)
);

INSERT INTO `users` (`username`, `email`, `password`) VALUES
('user1', 'user1@example.com', 'pass1'),
('user2', 'user2@example.com', 'pass2'),
('user3', 'user3@example.com', 'pass3'),
('user4', 'user4@example.com', 'pass4'),
('user5', 'user5@example.com', 'pass5'),
('user6', 'user6@example.com', 'pass6');

CREATE TABLE `products` (
    `productID` INT AUTO_INCREMENT PRIMARY KEY,
    `productName` VARCHAR(200),
    `description` VARCHAR(500),
    `price` DECIMAL(10,2),
    `productCategoryID` INT,
    FOREIGN KEY (`productCategoryID`) REFERENCES `ProductCategories`(`productCategoryID`)
);

INSERT INTO `products` (`productName`, `description`, `price`, `productCategoryID`) VALUES
('Basic Tee', 'A plain t-shirt', 19.99, 1),
('Skinny Jeans', 'Slim fit denim jeans', 39.99, 2),
('Summer Dress', 'A light, floral dress', 29.99, 3),
('Leather Jacket', 'Genuine leather biker jacket', 89.99, 4),
('Running Shoes', 'Sneakers for everyday sport', 49.99, 5),
('Woolen Hat', 'Warm hat for winter', 14.99, 6),
('Silk Scarf', 'Elegant accessory for formal wear', 35.99, 6),
('Casual Socks', 'Cotton socks in various colours', 9.99, 6),
('Formal Shirt', 'Crisp white shirt for business or formal events', 24.99, 1),
('Winter Coat', 'Thick coat for cold weather', 99.99, 4);



