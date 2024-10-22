CREATE DATABASE  IF NOT EXISTS `qr_python` /*!40100 DEFAULT CHARACTER SET utf8mb3 COLLATE utf8mb3_unicode_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `qr_python`;
-- MySQL dump 10.13  Distrib 8.0.34, for Win64 (x86_64)
--
-- Host: localhost    Database: qr_python
-- ------------------------------------------------------
-- Server version	8.0.34

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
-- Table structure for table `diadiem`
--

DROP TABLE IF EXISTS `diadiem`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `diadiem` (
  `id` int NOT NULL AUTO_INCREMENT,
  `ten` varchar(1000) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `url_google_map` varchar(2000) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `code` varchar(1000) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `ten_anh` varchar(100) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=42 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `diadiem`
--

LOCK TABLES `diadiem` WRITE;
/*!40000 ALTER TABLE `diadiem` DISABLE KEYS */;
INSERT INTO `diadiem` VALUES (34,'Đại học Cần Thơ','https://www.google.com/maps/place/Tr%C6%B0%E1%BB%9Dng+%C4%90%E1%BA%A1i+h%E1%BB%8Dc+C%E1%BA%A7n+Th%C6%A1/@10.0299337,105.7680404,17z/data=!3m1!4b1!4m6!3m5!1s0x31a0895a51d60719:0x9d76b0035f6d53d0!8m2!3d10.0299337!4d105.7706153!16s%2Fm%2F02r6wmy?hl=vi-VN&entry=ttu','2570778398673209303','DaiHocCanTho'),(35,'Đại học Y Dược Cần Thơ','https://www.google.com/maps/place/%C4%90%E1%BA%A1i+H%E1%BB%8Dc+Y+D%C6%B0%E1%BB%A3c+C%E1%BA%A7n+Th%C6%A1/@10.0334816,105.7520812,17z/data=!3m1!4b1!4m6!3m5!1s0x31a0886a7cfe14df:0x34602e2fdca1972d!8m2!3d10.0334816!4d105.7546561!16s%2Fg%2F11b7jqjfpd?hl=vi-VN&entry=ttu','4009944731194623991','YDuocCanTho'),(40,'Chợ Nổi Cái Răng','https://www.google.com/maps/search/ch%E1%BB%A3+n%E1%BB%95i+c%C3%A1i+r%C4%83ng/@10.0018262,105.7420821,17z/data=!3m1!4b1?hl=vi-VN&entry=ttu','4863937886466639599','chonoicairang'),(41,'Đền Hùng','https://www.google.com/maps/place/%C4%90%E1%BB%81n+th%E1%BB%9D+Vua+H%C3%B9ng/@10.0664845,105.7307572,17z/data=!3m1!4b1!4m6!3m5!1s0x31a0879d16b6a6db:0xc8dd3d9ac38a2192!8m2!3d10.0664845!4d105.7333321!16s%2Fg%2F11n5qrfbdv?hl=vi-VN&entry=ttu','1371809263458625015','DenHung');
/*!40000 ALTER TABLE `diadiem` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-03-27 23:36:34
