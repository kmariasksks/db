DROP DATABASE IF EXISTS InvoiceMessage;
CREATE DATABASE IF NOT EXISTS InvoiceMessage;
USE InvoiceMessage;

DROP TABLE IF EXISTS Terminals;

CREATE TABLE Terminals (
  TerminalID INT AUTO_INCREMENT PRIMARY KEY,
  GPSCoordinates VARCHAR(100) NOT NULL,
  DateInService DATE NOT NULL,
  INDEX idx_DateInService (DateInService)
) ENGINE = InnoDB;

INSERT INTO Terminals (TerminalID, GPSCoordinates, DateInService) VALUES
(1, '49.930201862070824, 27.125798578782064', '2023-07-03'),
(2, '49.930201384950824, 27.145938578782064', '2023-08-04'),
(3, '49.238590862070824, 27.125798374659064', '2022-10-11'),
(4, '49.354678905647285, 27.768496083647285', '2022-09-09' ),
(5, '49.567483907856472, 27.345267890126574', '2022-11-07'),
(6, '49.109876538967456, 27.354678908273663', '2023-01-09'),
(7, '49.874568478265983, 27.297593049476458', '2023-10-10'),
(8, '49.474950893845859, 27.274885756284959', '2023-03-12'),
(9, '49.474839829549084, 27.143747289982744', '2023-04-04'),
(10, '49.473882394388433, 27.784389289329044', '2023-10-01');

DROP TABLE IF EXISTS Technicians;

CREATE TABLE Technicians (
  TechnicianID INT AUTO_INCREMENT PRIMARY KEY,
  TechnicianSurname VARCHAR(45) NOT NULL,
  TechnicianName VARCHAR(45) NOT NULL,
  TechnicianFathersname VARCHAR(45) NOT NULL,
  INDEX idx_TechnicianSurname (TechnicianSurname)
) ENGINE = InnoDB;

INSERT INTO Technicians (TechnicianID, TechnicianSurname, TechnicianName,
TechnicianFathersname) VALUES
(1, 'Троян', 'Ростислав' , 'Віталійович'),
(2, 'Дишкант', 'Ігор' , 'Олегович'),
(3, 'Гентош', 'Олег' , 'Дмитрович');

DROP TABLE IF EXISTS ServiceTypes;

CREATE TABLE ServiceTypes (
  ServiceTypeID INT AUTO_INCREMENT PRIMARY KEY,
  ServiceTypesName VARCHAR(60) NOT NULL,
  TechnicianID INT NOT NULL,
  INDEX idx_ServiceTypesName (ServiceTypesName)
) ENGINE = InnoDB;

 ALTER TABLE ServiceTypes
 ADD CONSTRAINT FK_ServiceTypes_TechnicianID
 FOREIGN KEY (TechnicianID)
 REFERENCES Technicians (TechnicianID);
 
 INSERT INTO ServiceTypes (ServiceTypeID, ServiceTypesName, TechnicianID) VALUES
(1, 'Звичайне обслуговування', '1'),
(2, 'Капітальний ремонт', '2'),
(3, 'Забирання готівки', '3');

DROP TABLE IF EXISTS Service;

CREATE TABLE Service (
  ServiceID INT AUTO_INCREMENT PRIMARY KEY,
  ServiceDate DATE NOT NULL,
  DurationDays INT NOT NULL,
  ServiceCost DECIMAL(10,2) NOT NULL,
  TechnicianID INT NOT NULL,
  TerminalID INT NOT NULL,
  ServiceTypeID INT NOT NULL,
  INDEX idx_DurationDays (DurationDays),
  INDEX idx_ServiceCost (ServiceCost)
) ENGINE = InnoDB;

ALTER TABLE Service
 ADD CONSTRAINT FK_Service_TechnicianID
 FOREIGN KEY (TechnicianID)
 REFERENCES Technicians (TechnicianID),
 
 ADD CONSTRAINT FK_Service_TerminalID
 FOREIGN KEY (TerminalID)
 REFERENCES Terminals (TerminalID),
 
 ADD CONSTRAINT FK_Service_ServiceTypeID
 FOREIGN KEY (ServiceTypeID)
 REFERENCES ServiceTypes (ServiceTypeID);
 
 INSERT INTO Service (ServiceID, ServiceDate, DurationDays, 
 ServiceCost, TechnicianID, TerminalID, ServiceTypeID) VALUES
 (1, '2023-03-21', 3, 2545.00, 1, 1, 1),
 (2, '2023-08-21', 4, 3005.00, 2, 2, 2),
 (3, '2023-10-21', 2, 1600.00, 3, 3, 3),
 (4, '2022-01-21', 2, 1000.00, 1, 4, 1),
 (5, '2023-04-21', 3, 2300.00, 2, 5, 2),
 (6, '2023-09-21', 2, 1450.00, 3, 6, 3),
 (7, '2022-06-21', 3, 1900.00, 1, 7, 1),
 (8, '2023-08-21', 5, 3460.00, 2, 8, 2),
 (9, '2022-12-21', 1, 700.00, 3, 9, 3),
 (10, '2022-11-21', 3, 1780.00, 1, 10, 1);

DROP TABLE IF EXISTS Ivoice; 

CREATE TABLE Invoice (
  InvoiceID INT AUTO_INCREMENT PRIMARY KEY,
  InvoiceDate DATE NOT NULL,
  InvoiceCost DECIMAL(10,2) NOT NULL,
  ServiceID INT NOT NULL,
  INDEX idx_InvoiceDate (InvoiceDate),
  INDEX idx_InvoiceCost (InvoiceCost),
  FOREIGN KEY (ServiceID) REFERENCES `Service` (`ServiceID`)
) ENGINE = InnoDB;

INSERT INTO Invoice (InvoiceID, InvoiceDate, InvoiceCost, ServiceID) VALUES
(1, '2023-07-03', '3500.00', 1),
(2, '2023-08-04', '2000.00', 2),
(3, '2022-10-11', '1850.00', 3),
(4, '2022-09-09', '900.00', 4),
(5, '2022-11-07', '2670.00', 5),
(6, '2023-01-09', '2200.00', 6),
(7, '2023-10-10', '1870.00', 7),
(8, '2023-03-12', '1600.00', 8),
(9, '2023-04-04', '3190.00', 9),
(10, '2023-10-01', '1700.00', 10);

DROP TABLE IF EXISTS Payment; 

CREATE TABLE Payment (
  PaymentID INT AUTO_INCREMENT PRIMARY KEY,
  PaymentDate DATE NOT NULL,
  AmountPaid DECIMAL(10,2) NOT NULL,
  InvoiceID INT NOT NULL,
  FOREIGN KEY (InvoiceID) REFERENCES `Invoice` (`InvoiceID`)
) ENGINE = InnoDB;

INSERT INTO Payment (PaymentID, PaymentDate, AmountPaid, InvoiceID) VALUES
(1, '2023-07-03', '3500.00', 1),
(2, '2023-08-04', '2000.00', 2),
(3, '2022-10-11', '1850.00', 3),
(4, '2022-09-09', '900.00', 4),
(5, '2022-11-07', '2670.00', 5),
(6, '2023-01-09', '2200.00', 6),
(7, '2023-10-10', '1870.00', 7),
(8, '2023-03-12', '1600.00', 8),
(9, '2023-04-04', '3190.00', 9),
(10, '2023-10-01', '1700.00', 10);

DROP TABLE IF EXISTS TerminalsLocation;

CREATE TABLE TerminalsLocation (
  LocationID INT AUTO_INCREMENT PRIMARY KEY,
  StreetName VARCHAR(45) NOT NULL,
  BuildingNumber VARCHAR(45) NOT NULL,
  PostalCode VARCHAR(45) NOT NULL,
  TerminalID INT NOT NULL,
  INDEX idx_StreetName (StreetName),
  INDEX idx_PostalCode (PostalCode)
) ENGINE = InnoDB;

ALTER TABLE TerminalsLocation
 ADD CONSTRAINT FK_TerminalsLocation_TerminalID
 FOREIGN KEY (TerminalID)
 REFERENCES Terminals (TerminalID);
 
 INSERT INTO TerminalsLocation ( LocationID, StreetName, BuildingNumber, PostalCode, 
 TerminalID) VALUES
 (1, 'Шевченка', '34', '01001', '1'),
 (2, 'Mickiewicza', '20a', '00-426', '2'),
 (3, 'Rue de la Liberté', '53', '75011', '3'),
 (4, 'Calle de la Paz', '4', '28004', '4'),
 (5, 'Via Roma', '22', '00185', '5'),
 (6, 'Main Street ', '35', 'SW1A 1AA', '6'),
 (7, 'Pääkatu', '1', '00100', '7'),
 (8, 'Hauptstraße', '78', '1010', '8'),
 (9, 'Oxford Street ', '17', 'W1D 1BS', '9'),
 (10, 'Drottninggatan', '10', '111 21', '10');

DROP TABLE IF EXISTS TerminalCity;

CREATE TABLE TerminalCity (
  TerminalCityID INT AUTO_INCREMENT PRIMARY KEY,
  City VARCHAR(45) NOT NULL,
  LocationID INT NOT NULL,
  INDEX idx_City (City),
  FOREIGN KEY (LocationID) REFERENCES `TerminalsLocation` (`LocationID`)
);

 
 INSERT INTO TerminalCity (TerminalCityID, City, LocationID) VALUES
 (1, 'Київ', '1'),
 (2, 'Варшава', '2'),
 (3, 'Париж', '3'),
 (4, 'Мадрид', '4'),
 (5, 'Рим', '5'),
 (6, 'Дублін', '6'),
 (7, 'Гельсінкі', '7'),
 (8, 'Відень', '8'),
 (9, 'Берн', '9'),
 (10, 'Стокгольм', '10');

DROP TABLE IF EXISTS TerminalCountry;

CREATE TABLE TerminalCountry (
  CountryID INT AUTO_INCREMENT PRIMARY KEY,
  Country VARCHAR(45) NOT NULL,
  TerminalCityID INT NOT NULL,
  INDEX idx_Country (Country),
  FOREIGN KEY (TerminalCityID) REFERENCES `TerminalCity` (`TerminalCityID`)
) ENGINE = InnoDB;

INSERT INTO TerminalCountry (CountryID, Country, TerminalCityID) VALUES
 (1, 'Україна', '1'),
 (2, 'Польща', '2'),
 (3, 'Франція', '3'),
 (4, 'Іспанія', '4'),
 (5, 'Італія', '5'),
 (6, 'Ірландія', '6'),
 (7, 'Фінляндія', '7'),
 (8, 'Австрія', '8'),
 (9, 'Швейцарія', '9'),
 (10, 'Швеція', '10');
 
 DROP TABLE IF EXISTS TechnicalsManufacturers;

CREATE TABLE TechnicalsManufacturers (
  TechnicalsManufacturersID INT AUTO_INCREMENT PRIMARY KEY,
  Manufacturername VARCHAR(60) NOT NULL,
  ManufacturerContact VARCHAR(15) NOT NULL,
  TerminalID INT NOT NULL,
  INDEX idx_Manufacturername (Manufacturername),
  INDEX idx_ManufacturerContact (ManufacturerContact)
) ENGINE = InnoDB;

ALTER TABLE TechnicalsManufacturers
 ADD CONSTRAINT FK_TechnicalsManufacturers_TerminalID
 FOREIGN KEY (TerminalID)
 REFERENCES Terminals (TerminalID);
 
 INSERT INTO TechnicalsManufacturers (TechnicalsManufacturersID, Manufacturername, ManufacturerContact, TerminalID) VALUES
 (1, 'NCR Corporation', '+380978364728', '1'),
 (2, 'Ingenico Group', '+380978452678', '2'),
 (3, 'VeriFone Inc.', '+380978462377', '3'),
 (4, 'PAX Technology Limited', '+380978667328', '4'),
 (5, 'Diebold Nixdorf Incorporated', '+380978431631', '5'),
 (6, 'Kernel', '+380973657893', '6'),
 (7, 'Exxon Mobil', '+380971748598', '7'),
 (8, 'Broadcasting Corporation', '+380972647389', '8'),
 (9, 'David Dodge', '+380973748956', '9'),
 (10, 'JD.com', '+3809748930745', '10');
 
 DROP TABLE IF EXISTS ServiceTypes_has_Service;
 
CREATE TABLE ServiceTypes_has_Service (
  ServiceTypeID INT NOT NULL,
  ServiceID INT NOT NULL, 
  CONSTRAINT FK_ServiceTypes_has_Service_ServiceTypeID
  FOREIGN KEY ( ServiceTypeID)
  REFERENCES  ServiceTypes ( ServiceTypeID),
  CONSTRAINT FK_ServiceTypes_has_Service_ServiceID
  FOREIGN KEY ( ServiceID)
  REFERENCES  Service ( ServiceID)
) ENGINE = InnoDB;

INSERT INTO ServiceTypes_has_Service (ServiceTypeID, ServiceID) VALUES
(1, '1'),
(2, '2'),
(3, '3'),
(1, '1'),
(2, '2'),
(3, '3'),
(1, '1'),
(2, '2'),
(3, '3'),
(1, '1');

 -- 1. 
 
 DROP TABLE IF EXISTS TechniciansContact;
 
CREATE TABLE TechniciansContact (
  TechniciansContactID INT AUTO_INCREMENT PRIMARY KEY,
  TechniciansNumber VARCHAR(45) NOT NULL,
  TechniciansEmail VARCHAR(45) NOT NULL,
  TechnicianID INT NOT NULL, 
  INDEX idx_TechnicianID (TechnicianID), 
  CONSTRAINT FK_TechniciansContact_TechnicianID
  FOREIGN KEY (TechnicianID)
  REFERENCES Technicians (TechnicianID)
) ENGINE = InnoDB;

INSERT INTO TechniciansContact (TechniciansContactID, TechnicianID, TechniciansNumber, TechniciansEmail) VALUES
(1, '1', '+380978364728', 'troyan25@gmail.com'),
(2, '2', '+380978452678', 'dyshant78@gmail.com'),
(3, '3', '+380978462377', 'hentosholeg@gmail.com');

-- triger 1

DELIMITER //

CREATE TRIGGER before_insert_TechniciansContact
BEFORE INSERT ON TechniciansContact
FOR EACH ROW
BEGIN
     IF LEFT(NEW.TechniciansNumber, 1) != '3' THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Invalid TechniciansNumber - Must start with 3';
    END IF;
END;
//

DELIMITER ;


-- procedure 2.a

DROP PROCEDURE IF EXISTS insertIntoTechniciansContact;
DELIMITER //
CREATE PROCEDURE insertIntoTechniciansContact (
     TechniciansNumber VARCHAR(45),
     TechniciansEmail VARCHAR(45),
     TechnicianID INT
)
BEGIN
    INSERT INTO TechniciansContact (TechniciansNumber, TechniciansEmail, TechnicianID) 
    VALUES (TechniciansNumber, TechniciansEmail, TechnicianID);
END //

DELIMITER ;

-- 2 b 
DROP TABLE IF EXISTS TechnicalsManufacturers_has_Terminals;
 
CREATE TABLE Manufacturers_has_Terminals (
  ManufacturersID INT NOT NULL,
  TerminalID INT NOT NULL,
  DateInstalled DATE NOT NULL, 
  CONSTRAINT FK_Manufacturers_has_Terminals_TerminalID
  FOREIGN KEY (TerminalID)
  REFERENCES Terminals (TerminalID),
CONSTRAINT FK_Manufacturers_has_Terminals_ManufacturersID
FOREIGN KEY (ManufacturersID)
REFERENCES TechnicalsManufacturers(TechnicalsManufacturersID)
) ENGINE = InnoDB;

INSERT INTO Manufacturers_has_Terminals (ManufacturersID, TerminalID, DateInstalled) VALUES
(1, '1', '2023-07-03'),
(2, '2', '2023-08-04'),
(3, '3', '2022-10-11'),
(4, '4', '2022-09-09'),
(5, '5', '2022-11-07'),
(6, '6', '2023-01-09'),
(7, '7', '2023-10-10'),
(8, '8', '2023-03-12'),
(9, '9', '2023-04-04'),
(10, '10', '2023-10-01');

-- create procedure for 2b
DROP PROCEDURE IF EXISTS insert_TechnicalsManufacturers; 

DELIMITER //
CREATE PROCEDURE insert_Manufacturers_has_Terminals (
IN ManufacturerContact_ varchar(25),
IN DateInService_ DATE
)
BEGIN
	DECLARE Technicalsmanufacturers INT; 
    DECLARE Terminals INT;
    SELECT TechnicalsManufacturersID INTO TechnicalsManufacturers FROM TechnicalsManufacturers WHERE ManufacturerContact = ManufacturerContact_;
	SELECT TerminalID INTO Terminals FROM Terminals WHERE DateInService = DateInService_;
    INSERT INTO insert_Manufacturers_has_Terminals (ManufacturersID, TerminalID) VALUES (TechnicalsManufacturersstores, Terminals);
END;
//

-- 2с 
DROP PROCEDURE IF NOT EXISTS insert_TerminalCountry;

DELIMITER //
CREATE PROCEDURE insert_TerminalCountry (
)
BEGIN
	Insert INTO TerminalCountry (Country) VALUES 
		('Noname1'), ('Noname2'), 
		('Noname3'), ('Noname4'), 
		('Noname5'), ('Noname6'), 
		('Noname7'), ('Noname8'), 
		('Noname9'), ('Noname10');
        
END;
//

-- 2d
DROP PROCEDURE IF NOT EXISTS make_operation;


DELIMITER //
CREATE FUNCTION make_operation(
    operation VARCHAR(45)
)
RETURNS INT
DETERMINISTIC
READS SQL DATA
BEGIN
    DECLARE result DECIMAL(10,2) DEFAULT 0.0;

    IF operation = 'min' THEN
        SELECT MIN(ServiceCost) INTO result FROM Service;
    ELSEIF operation = 'max' THEN
        SELECT MAX(ServiceCost) INTO result FROM Service;
    ELSEIF operation = 'avg'  THEN
        SELECT AVG(ServiceCost) INTO result FROM Service;
	ELSEIF operation = 'sum'  THEN
        SELECT SUM(ServiceCost) INTO result FROM Service;
    END IF;
    RETURN result;
END;
//

DROP PROCEDURE IF NOT EXISTS make_operation_products;

DELIMITER //
CREATE 
PROCEDURE make_operation_products(
	operation VARCHAR(45)
)
BEGIN
	DECLARE result DECIMAL(10,2);
    SET result = make_operation(operation);
    SELECT result AS operation_result;
END;
//

-- cursore (?)
DELIMITER $$

CREATE PROCEDURE create_tables_for_cursor()
BEGIN
    DECLARE done INT DEFAULT FALSE;
    DECLARE tableName VARCHAR(30);
    DECLARE numColumns INT;
    DECLARE sqlQuery VARCHAR(1000);

    DECLARE cur CURSOR FOR SELECT REPLACE(CAST(InvoiceCost AS CHAR), '.', '_') FROM Invoice;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;

    OPEN cur;

    read_loop: LOOP
        FETCH cur INTO tableName;
        IF done THEN
            LEAVE read_loop;
        END IF;

        SET tableName = CONCAT('table_', tableName, '_', DATE_FORMAT(NOW(), '%Y%m%d%H%i%s'));

        SET numColumns = FLOOR(1 + RAND() * 9);

        SET @sqlQuery = CONCAT('CREATE TABLE ', tableName, ' (');

        SET @i = 1;
        WHILE @i <= numColumns DO
            SET @sqlQuery = CONCAT(@sqlQuery, 'column', @i, ' VARCHAR(100)');
            IF @i < numColumns THEN
                SET @sqlQuery = CONCAT(@sqlQuery, ', ');
            END IF;
            SET @i = @i + 1;
        END WHILE;

        SET @sqlQuery = CONCAT(@sqlQuery, ')');

        PREPARE stmt FROM @sqlQuery;
        EXECUTE stmt;
        DEALLOCATE PREPARE stmt;
    END LOOP;

    CLOSE cur;

END $$

DELIMITER ;


CALL create_tables_for_cursor();
-- 3а
DELIMITER //

CREATE TRIGGER check_coordinates
BEFORE INSERT ON Terminals
FOR EACH ROW
BEGIN
    IF SUBSTRING(NEW.GPSCoordinates, -2) = '00' THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Error: GPSCoordinates cannot end with two zeros';
    END IF;
END;

//

DELIMITER ;

-- checking
-- INSERT INTO Terminals (GPSCoordinates, DateInService) VALUES
-- ('49.12345600, 27.98765400', '2023-12-14');

-- 3b
DELIMITER //

CREATE TRIGGER block_modifications_Service
BEFORE INSERT ON Service
FOR EACH ROW
BEGIN
    SIGNAL SQLSTATE '45000'
    SET MESSAGE_TEXT = 'Inserting data into Service table is not allowed';
END;

CREATE TRIGGER block_modifications_update_Service
BEFORE UPDATE ON Service
FOR EACH ROW
BEGIN
    SIGNAL SQLSTATE '45000'
    SET MESSAGE_TEXT = 'Updating data in Service table is not allowed';
END;

CREATE TRIGGER block_modifications_delete_Service
BEFORE DELETE ON Service
FOR EACH ROW
BEGIN
    SIGNAL SQLSTATE '45000'
    SET MESSAGE_TEXT = 'Deleting data from Service table is not allowed';
END;

//

DELIMITER ;

-- checking
-- INSERT INTO Service (ServiceDate, DurationDays, ServiceCost, TechnicianID, TerminalID, ServiceTypeID)
-- VALUES ('2023-12-01', 2, 1500.00, 4, 8, 3);

-- 3c
DELIMITER //

CREATE TRIGGER prevent_payment_deletion
BEFORE DELETE ON Payment
FOR EACH ROW
BEGIN
    SIGNAL SQLSTATE '45000'
    SET MESSAGE_TEXT = 'Deleting rows from Payment table is not allowed';
END;

//

DELIMITER ;

-- checking
-- DELETE FROM Payment WHERE PaymentID = 2;

