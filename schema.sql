-- DATA BASE SCHEMA  -- 

CREATE TABLE COMPANY (
  ID INT PRIMARY KEY,
  NAME VARCHAR(50) NOT NULL UNIQUE
);

CREATE TABLE VEHICLE_TYPE (
  ID INT PRIMARY KEY,
  NAME VARCHAR(50) NOT NULL UNIQUE,
  CAPACITY INT NOT NULL,
  MANUFACTURER VARCHAR(50) ,
  COMPANY_ID INT NOT NULL,
  FOREIGN KEY (COMPANY_ID) REFERENCES COMPANY(ID)
);

CREATE TABLE VEHICLE (
  ID INT PRIMARY KEY,
  VIN VARCHAR(50) NOT NULL UNIQUE,
  LAST_MSG_DATE TIME,
  PNB INT,
  VEHICLE_TYPE_ID INT NOT NULL,
  FOREIGN KEY (VEHICLE_TYPE_ID) REFERENCES VEHICLE_TYPE(ID)
);
   


