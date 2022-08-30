-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Aug 29, 2022 at 10:00 AM
-- Server version: 10.4.24-MariaDB
-- PHP Version: 8.1.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `ethereum`
--

-- --------------------------------------------------------

--
-- Table structure for table `administrationlog`
--

CREATE TABLE `administrationlog` (
  `administrationID` varchar(20) NOT NULL,
  `administrationPass` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `administrationlog`
--

INSERT INTO `administrationlog` (`administrationID`, `administrationPass`) VALUES
('ahmed', '9911'),
('ahmed@201', '12345'),
('AhmedShahan', '12345'),
('nabila', '840223'),
('shahan', '840223'),
('shahan@201', '840223');

-- --------------------------------------------------------

--
-- Table structure for table `adminlog`
--

CREATE TABLE `adminlog` (
  `userId` varchar(20) NOT NULL,
  `pass` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `adminlog`
--

INSERT INTO `adminlog` (`userId`, `pass`) VALUES
('ahmed@201', '12345'),
('shahan@201', '840223');

-- --------------------------------------------------------

--
-- Table structure for table `chamberloc`
--

CREATE TABLE `chamberloc` (
  `LocID` int(5) NOT NULL,
  `Location` varchar(50) DEFAULT NULL,
  `zipCode` int(5) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `docchember`
--

CREATE TABLE `docchember` (
  `LocID` int(5) NOT NULL,
  `DocID` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `docspecialist`
--

CREATE TABLE `docspecialist` (
  `DocID` varchar(10) NOT NULL,
  `SpListID` int(3) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `docspecialist`
--

INSERT INTO `docspecialist` (`DocID`, `SpListID`) VALUES
('#12345', 3),
('#12345', 14),
('#12345', 15),
('#12345', 16),
('111222', 3),
('111222', 4),
('111222', 15),
('@2013168', 3),
('@2013168', 14),
('@2013168', 15),
('@2013168', 16);

-- --------------------------------------------------------

--
-- Table structure for table `doctorinfo`
--

CREATE TABLE `doctorinfo` (
  `BMDC_Reg` varchar(10) NOT NULL,
  `Dname` varchar(20) DEFAULT NULL,
  `DOB` date DEFAULT NULL,
  `Gender` varchar(7) DEFAULT NULL,
  `NID` varchar(15) DEFAULT NULL,
  `Passport` varchar(15) DEFAULT NULL,
  `Mobile` varchar(12) DEFAULT NULL,
  `Email` varchar(30) DEFAULT NULL,
  `PresentAddress` varchar(100) DEFAULT NULL,
  `ParmanentAddress` varchar(100) DEFAULT NULL,
  `Bloodgroup` varchar(10) DEFAULT NULL,
  `Docpass` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `doctorinfo`
--

INSERT INTO `doctorinfo` (`BMDC_Reg`, `Dname`, `DOB`, `Gender`, `NID`, `Passport`, `Mobile`, `Email`, `PresentAddress`, `ParmanentAddress`, `Bloodgroup`, `Docpass`) VALUES
('#12345', 'Zahid Hasan', '2010-08-05', NULL, '834848943289342', '84834289342', '434328943298', 'sfjasdjasd089123890231', 'Kuril, Dhaka, Bangladesh', 'Kuril, Dhaka, Bangladesh', NULL, '96653172'),
('#56789', 'Sabbir Mollah', '1996-08-01', NULL, '873458734879342', '8793879437834', '893428794328', 'jkasjhsdaj@jkhfdsjhkfd', 'sadbsdsd,asdsadsad,sadsad', 'sadbsdsd,asdsadsad,sadsad', NULL, 'shahan'),
('1000200', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '12345'),
('102030', 'Molla Ahmed ', '0000-00-00', 'Male', '2783468726487', '782637842', '328236482', '', 'None', 'None', 'A(-ve)', 'Verygood'),
('111222', 'Nabil Ahmed', '1991-05-24', NULL, '6345276482', '23672363482', '233786238', 'hkashd@ahskjsa', 'None', 'None', NULL, 'Nabu'),
('12345', 'Ahmed Shahan', '1993-08-05', 'Male', '87348957398', '32876823', '02398202243', 'shahan@gmail.com', 'None', 'None', 'B(+ve)', 'shahan'),
('333444', 'Max Rashid', '0000-00-00', 'Male', '3729847982', '3297932', '2338y8237912', '', 'None', 'None', 'A(-ve)', 'good'),
('444555', 'Moly Poly', '1990-08-17', 'Female', '6523461237', '34535252', '2543285389', 'jgd@Jkjkhj', 'None', 'None', 'O(-ve)', 'Notgood'),
('96651244', 'Nabila Rashid', '1996-08-14', 'Female', '2378985709', '484857983', '29840292204', 'nabila.rashid@gmail.com', 'None', 'None', 'B(+ve)', 'Nabila'),
('@2013168', 'Shahana Ahmed', '1998-09-02', 'Male', '7808214063', 'BC0318627', '01736666171', 'shahan.ahmed@northsouth.edu', 'Basundhara R/A, Dhaka, Bangladesh', 'Basundhara R/A, Dhaka, Bangladesh', NULL, 'shahan'),
('ahmedShaha', 'jkahsaS', '0000-00-00', 'Male', 'IOWEWQE', '343434', '3423434', '', '', '', NULL, '@northsouth');

-- --------------------------------------------------------

--
-- Table structure for table `healthdetails`
--

CREATE TABLE `healthdetails` (
  `Disease` varchar(30) DEFAULT NULL,
  `DiseaseId` int(3) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `healthdetails`
--

INSERT INTO `healthdetails` (`Disease`, `DiseaseId`) VALUES
('ABC', 801);

-- --------------------------------------------------------

--
-- Table structure for table `medicaldegree`
--

CREATE TABLE `medicaldegree` (
  `MedID` int(3) NOT NULL,
  `DegreeList` varchar(30) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `medicaldegree`
--

INSERT INTO `medicaldegree` (`MedID`, `DegreeList`) VALUES
(3, 'BCS (Health)'),
(6, 'DIPLOMA'),
(8, 'FCPS'),
(5, 'M PHIL'),
(4, 'MBBS'),
(7, 'MD/MS');

-- --------------------------------------------------------

--
-- Table structure for table `medicalhis`
--

CREATE TABLE `medicalhis` (
  `MedId` int(5) NOT NULL,
  `DocId` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `patientconsualtation`
--

CREATE TABLE `patientconsualtation` (
  `DocId` varchar(10) NOT NULL,
  `PatientID` int(4) NOT NULL,
  `NumberOfVisist` int(3) DEFAULT NULL,
  `TotalConsultationTimeMIN` int(5) DEFAULT NULL,
  `VisiteDate` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `patienthealth`
--

CREATE TABLE `patienthealth` (
  `DiseasID` int(3) NOT NULL,
  `PatientID` int(3) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `patientinfo`
--

CREATE TABLE `patientinfo` (
  `ID` int(4) NOT NULL,
  `Name` varchar(20) DEFAULT NULL,
  `DeathOfBirth` varchar(20) DEFAULT NULL,
  `Gender` varchar(20) DEFAULT NULL,
  `Age` varchar(20) DEFAULT NULL,
  `NID` varchar(20) DEFAULT NULL,
  `MobileNo` int(20) DEFAULT NULL,
  `Email` varchar(20) DEFAULT NULL,
  `PresentAddress` varchar(30) DEFAULT NULL,
  `PermanentAddress` varchar(30) DEFAULT NULL,
  `BloodGroup` varchar(30) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `specialist`
--

CREATE TABLE `specialist` (
  `SpID` int(3) NOT NULL,
  `SpList` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `specialist`
--

INSERT INTO `specialist` (`SpID`, `SpList`) VALUES
(3, 'Cardiologist'),
(16, 'Dermatologists'),
(15, 'Endocrinologists'),
(14, 'Gastroenterologists'),
(4, 'Gynecologist'),
(13, 'Nephrologists'),
(5, 'Neurologist'),
(12, 'Oncologists'),
(11, 'Ophthalmologists'),
(6, 'Orthopedics'),
(10, 'Pathologists'),
(9, 'Pediatricians'),
(17, 'Plastic Surgeons'),
(8, 'Psychiatrists'),
(7, 'Radiologists');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `administrationlog`
--
ALTER TABLE `administrationlog`
  ADD PRIMARY KEY (`administrationID`,`administrationPass`);

--
-- Indexes for table `adminlog`
--
ALTER TABLE `adminlog`
  ADD PRIMARY KEY (`userId`);

--
-- Indexes for table `chamberloc`
--
ALTER TABLE `chamberloc`
  ADD PRIMARY KEY (`LocID`);

--
-- Indexes for table `docchember`
--
ALTER TABLE `docchember`
  ADD PRIMARY KEY (`LocID`,`DocID`),
  ADD KEY `DocID` (`DocID`);

--
-- Indexes for table `docspecialist`
--
ALTER TABLE `docspecialist`
  ADD PRIMARY KEY (`DocID`,`SpListID`),
  ADD KEY `SpListID` (`SpListID`);

--
-- Indexes for table `doctorinfo`
--
ALTER TABLE `doctorinfo`
  ADD PRIMARY KEY (`BMDC_Reg`);

--
-- Indexes for table `healthdetails`
--
ALTER TABLE `healthdetails`
  ADD PRIMARY KEY (`DiseaseId`);

--
-- Indexes for table `medicaldegree`
--
ALTER TABLE `medicaldegree`
  ADD PRIMARY KEY (`MedID`),
  ADD UNIQUE KEY `DegreeList` (`DegreeList`);

--
-- Indexes for table `medicalhis`
--
ALTER TABLE `medicalhis`
  ADD PRIMARY KEY (`MedId`,`DocId`),
  ADD KEY `DocId` (`DocId`);

--
-- Indexes for table `patientconsualtation`
--
ALTER TABLE `patientconsualtation`
  ADD PRIMARY KEY (`DocId`,`PatientID`),
  ADD KEY `PatientID` (`PatientID`);

--
-- Indexes for table `patienthealth`
--
ALTER TABLE `patienthealth`
  ADD PRIMARY KEY (`DiseasID`,`PatientID`),
  ADD KEY `PatientID` (`PatientID`);

--
-- Indexes for table `patientinfo`
--
ALTER TABLE `patientinfo`
  ADD PRIMARY KEY (`ID`);

--
-- Indexes for table `specialist`
--
ALTER TABLE `specialist`
  ADD PRIMARY KEY (`SpID`),
  ADD UNIQUE KEY `SpList` (`SpList`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `chamberloc`
--
ALTER TABLE `chamberloc`
  MODIFY `LocID` int(5) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `healthdetails`
--
ALTER TABLE `healthdetails`
  MODIFY `DiseaseId` int(3) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=802;

--
-- AUTO_INCREMENT for table `medicaldegree`
--
ALTER TABLE `medicaldegree`
  MODIFY `MedID` int(3) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `patientinfo`
--
ALTER TABLE `patientinfo`
  MODIFY `ID` int(4) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=103;

--
-- AUTO_INCREMENT for table `specialist`
--
ALTER TABLE `specialist`
  MODIFY `SpID` int(3) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `docchember`
--
ALTER TABLE `docchember`
  ADD CONSTRAINT `docchember_ibfk_1` FOREIGN KEY (`LocID`) REFERENCES `chamberloc` (`LocID`) ON DELETE CASCADE,
  ADD CONSTRAINT `docchember_ibfk_2` FOREIGN KEY (`DocID`) REFERENCES `doctorinfo` (`BMDC_Reg`) ON DELETE CASCADE;

--
-- Constraints for table `docspecialist`
--
ALTER TABLE `docspecialist`
  ADD CONSTRAINT `docspecialist_ibfk_1` FOREIGN KEY (`DocID`) REFERENCES `doctorinfo` (`BMDC_Reg`) ON DELETE CASCADE,
  ADD CONSTRAINT `docspecialist_ibfk_2` FOREIGN KEY (`SpListID`) REFERENCES `specialist` (`SpID`) ON DELETE CASCADE;

--
-- Constraints for table `medicalhis`
--
ALTER TABLE `medicalhis`
  ADD CONSTRAINT `medicalhis_ibfk_1` FOREIGN KEY (`MedId`) REFERENCES `medicaldegree` (`MedID`) ON DELETE CASCADE,
  ADD CONSTRAINT `medicalhis_ibfk_2` FOREIGN KEY (`DocId`) REFERENCES `doctorinfo` (`BMDC_Reg`) ON DELETE CASCADE;

--
-- Constraints for table `patientconsualtation`
--
ALTER TABLE `patientconsualtation`
  ADD CONSTRAINT `patientconsualtation_ibfk_1` FOREIGN KEY (`DocId`) REFERENCES `docchember` (`DocID`) ON DELETE CASCADE,
  ADD CONSTRAINT `patientconsualtation_ibfk_2` FOREIGN KEY (`PatientID`) REFERENCES `patientinfo` (`ID`) ON DELETE CASCADE;

--
-- Constraints for table `patienthealth`
--
ALTER TABLE `patienthealth`
  ADD CONSTRAINT `patienthealth_ibfk_1` FOREIGN KEY (`DiseasID`) REFERENCES `healthdetails` (`DiseaseId`) ON DELETE CASCADE,
  ADD CONSTRAINT `patienthealth_ibfk_2` FOREIGN KEY (`PatientID`) REFERENCES `patientinfo` (`ID`) ON DELETE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
