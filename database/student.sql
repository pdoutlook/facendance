-- MySQL dump 10.13  Distrib 8.0.28, for Win64 (x86_64)
--
-- Host: localhost    Database: facendance
-- ------------------------------------------------------
-- Server version	8.0.28

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `student`
--

DROP TABLE IF EXISTS `student`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `student` (
  `Department` varchar(45) DEFAULT NULL,
  `Year` varchar(45) DEFAULT NULL,
  `Student Id` varchar(45) NOT NULL,
  `Name` varchar(45) DEFAULT NULL,
  `Course` varchar(45) DEFAULT NULL,
  `Semester` varchar(45) DEFAULT NULL,
  `Roll No` varchar(45) DEFAULT NULL,
  `Gender` varchar(45) DEFAULT NULL,
  `DoB` varchar(45) DEFAULT NULL,
  `Email` varchar(45) DEFAULT NULL,
  `Address` varchar(100) DEFAULT NULL,
  `Teacher` varchar(45) DEFAULT NULL,
  `Phone` bigint DEFAULT NULL,
  `Section` varchar(45) DEFAULT NULL,
  `Photo Sample` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`Student Id`),
  UNIQUE KEY `Student Id_UNIQUE` (`Student Id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `student`
--

LOCK TABLES `student` WRITE;
/*!40000 ALTER TABLE `student` DISABLE KEYS */;
INSERT INTO `student` VALUES ('Computer Science','2022-23','1','Prince Dwivedi','Machine Learning','Spring','120','Male','28/12/2000','pd365000@outlook.com','Bhopal','Leslie Kaebling',7440236443,'A','Yes'),('Information Technology','2023-24','2','Khushi Tiwari','Compiler Design','Spring','121','Female','01/01/2007','khushi@gmail.com','Bhopal','Someone',9783527383,'B','Yes'),('Mechanical','2022-23','3','Kalpana Dwivedi','Data Analytics Lab','Fall','122','Female','7/6/1973','kalpana365000@gmail.com','Bhopal','Someone',6475738274,'B','Yes');
/*!40000 ALTER TABLE `student` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-04-22 23:34:18
