CREATE TABLE Users (email NVARCHAR(320), password VARCHAR(255), PRIMARY KEY(email));

CREATE TABLE Bidders (
	email NVARCHAR(320),
	first_name VARCHAR(255),
	last_name VARCHAR(255),
	gender VARCHAR(50),
	age INTEGER,
	home_address_id VARCHAR(255),
	major VARCHAR(255) --
	
);


CREATE TABLE Summary (
	submission_number VARCHAR(20),
	date_obtained DATE,
	page_number INTEGER,
	text_embedded VARCHAR,
	text_ocr VARCHAR,
	
);


ALTER TABLE Bidders
	add constraint pk PRIMARY KEY(email),
	add constraint fk_home FOREIGN KEY(email) REFERENCES Users(email) ON DELETE CASCADE,
	add constraint fk_billing FOREIGN KEY(home_address_id) REFERENCES Address(address_id)
;

CREATE TABLE Credit_Cards (
	credit_card_num NVARCHAR(20),
	card_type VARCHAR(20),
	expire_month INTEGER,
	expire_year INTEGER,
	security_code VARCHAR(6),
	Owner_email NVARCHAR(320),
	PRIMARY KEY(credit_card_num),
	FOREIGN KEY(Owner_email) REFERENCES Bidders(email) ON DELETE CASCADE
);

CREATE TABLE Address(
	address_id VARCHAR(255),
	zipcode VARCHAR(50),
	street_num VARCHAR(20),
	street_name VARCHAR(255),
	PRIMARY KEY(address_id),
	FOREIGN KEY(zipcode) REFERENCES Zipcode_Info(zipcode)
);

CREATE TABLE Zipcode_Info(
	zipcode VARCHAR(50),
	city VARCHAR(255),
	state_id VARCHAR(6),
	PRIMARY KEY(zipcode)
);

CREATE TABLE Sellers(
	email NVARCHAR(320),
	routing_number NVARCHAR(100),
	account_number VARCHAR(100),
	balance INTEGER,
	PRIMARY KEY(email),
	FOREIGN KEY(email) REFERENCES Users(email) ON DELETE CASCADE
);

CREATE TABLE Local_Vendors(
	email NVARCHAR(320),
	business_name VARCHAR(255),
	business_address_id VARCHAR(255),
	customer_service_number NVARCHAR(100),
	PRIMARY KEY(email),
	FOREIGN KEY(email) REFERENCES Sellers(email) ON DELETE CASCADE,
	FOREIGN KEY(business_address_id) REFERENCES Address(address_id)
);

CREATE TABLE Categories(
	parent VARCHAR(255),
	category VARCHAR(255),
	PRIMARY KEY(category)
);

CREATE TABLE Auction_Listings(
	seller_email NVARCHAR(320),
	listing_id VARCHAR(100),
	category VARCHAR(255),
	auction_title VARCHAR(255),
	product_name VARCHAR(255),
	product_description VARCHAR(255),
	quantity INTEGER,
	reserve_price NVARCHAR(100),
	max_bids INTEGER,
	listing_status INTEGER,
	PRIMARY KEY(seller_email, listing_id),
	FOREIGN KEY(category) REFERENCES Categories(category) ON DELETE CASCADE
);

CREATE TABLE Bids(
	bid_id NVARCHAR(255),
	seller_email NVARCHAR(320),
	listing_id VARCHAR(100),
	bidder_email NVARCHAR(320),
	bid_price FLOAT, --
	PRIMARY KEY(bid_id)
);


CREATE TABLE Rating(
	bidder_email NVARCHAR(320),
	seller_email NVARCHAR(320),
	rating_date DATE,
	rating INTEGER,
	rating_desc NVARCHAR(500),
	PRIMARY KEY(bidder_email,seller_email,rating_date)
);