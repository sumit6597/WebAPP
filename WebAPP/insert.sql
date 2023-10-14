-- LOAD DATA LOCAL INFILE 'C:/Users/adria/Documents/431W/Project/NittanyMarketDataset-v8 (1)/NittanyMarketDataset-v8/Users.csv' INTO TABLE Users FIELDS TERMINATED BY ','ENCLOSED BY '"' LINES TERMINATED BY '\n' IGNORE 1 ROWS;

LOAD DATA LOCAL INFILE '/Users/kishorpallod/Downloads/lionproject/LionAuctionDataset-v5/Address.csv' INTO TABLE Address FIELDS TERMINATED BY ',' ENCLOSED BY '"' LINES TERMINATED BY '\n' IGNORE 1 ROWS;

LOAD DATA LOCAL INFILE '/Users/kishorpallod/Downloads/lionproject/LionAuctionDataset-v5/Bidders.csv' INTO TABLE Bidders FIELDS TERMINATED BY ',' ENCLOSED BY '"' LINES TERMINATED BY '\n' IGNORE 1 ROWS;

LOAD DATA LOCAL INFILE '/Users/kishorpallod/Downloads/lionproject/LionAuctionDataset-v5/Credit_Cards.csv' INTO TABLE Credit_Cards FIELDS TERMINATED BY ',' ENCLOSED BY '"' LINES TERMINATED BY '\n' IGNORE 1 ROWS;

LOAD DATA LOCAL INFILE '/Users/kishorpallod/Downloads/lionproject/LionAuctionDataset-v5/Zipcode_Info.csv' INTO TABLE Zipcode_Info FIELDS TERMINATED BY ','ENCLOSED BY '"' LINES TERMINATED BY '\n' IGNORE 1 ROWS;

LOAD DATA LOCAL INFILE '/Users/kishorpallod/Downloads/lionproject/LionAuctionDataset-v5/Sellers.csv' INTO TABLE Sellers FIELDS TERMINATED BY ',' ENCLOSED BY '"' LINES TERMINATED BY '\n' IGNORE 1 ROWS;

LOAD DATA LOCAL INFILE '/Users/kishorpallod/Downloads/lionproject/LionAuctionDataset-v5/Local_Vendors.csv' INTO TABLE Local_Vendors FIELDS TERMINATED BY ',' ENCLOSED BY '"' LINES TERMINATED BY '\n' IGNORE 1 ROWS;

LOAD DATA LOCAL INFILE '/Users/kishorpallod/Downloads/lionproject/LionAuctionDataset-v5/Categories.csv' INTO TABLE Categories FIELDS ENCLOSED BY '"' TERMINATED BY ',' LINES TERMINATED BY '\r\n' IGNORE 1 ROWS;

LOAD DATA LOCAL INFILE '/Users/kishorpallod/Downloads/lionproject/LionAuctionDataset-v5/Auction_Listings.csv' INTO TABLE Auction_Listings FIELDS TERMINATED BY ',' ENCLOSED BY '"' LINES TERMINATED BY '\r\n' IGNORE 1 ROWS;

LOAD DATA LOCAL INFILE '/Users/kishorpallod/Downloads/lionproject/LionAuctionDataset-v5/Bids.csv' INTO TABLE Bids FIELDS TERMINATED BY ',' ENCLOSED BY '"' LINES TERMINATED BY '\n' IGNORE 1 ROWS;

LOAD DATA LOCAL INFILE '/Users/kishorpallod/Downloads/lionproject/LionAuctionDataset-v5/Ratings.csv' INTO TABLE Rating FIELDS TERMINATED BY ',' ENCLOSED BY '"' LINES TERMINATED BY '\n' IGNORE 1 ROWS;

-- sudo /usr/local/mysql-8.0.12-macos10.13-x86_64/bin/mysql -u root -p --local-infile=1