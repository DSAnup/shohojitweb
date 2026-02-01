-- MySQL dump 10.13  Distrib 8.0.37, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: test_db
-- ------------------------------------------------------
-- Server version	8.0.37

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `administrator_accessmodelname`
--

DROP TABLE IF EXISTS `administrator_accessmodelname`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `administrator_accessmodelname` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `identifier_name` varchar(15) COLLATE utf8mb4_unicode_ci NOT NULL,
  `created_by_id` int DEFAULT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_by_id` int DEFAULT NULL,
  `updated_at` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `administrator_accessmodelname_created_by_id_4cb080ab` (`created_by_id`),
  KEY `administrator_accessmodelname_updated_by_id_7a2a6e23` (`updated_by_id`),
  CONSTRAINT `administrator_access_created_by_id_4cb080ab_fk_auth_user` FOREIGN KEY (`created_by_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `administrator_access_updated_by_id_7a2a6e23_fk_auth_user` FOREIGN KEY (`updated_by_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `administrator_accessmodelname`
--

LOCK TABLES `administrator_accessmodelname` WRITE;
/*!40000 ALTER TABLE `administrator_accessmodelname` DISABLE KEYS */;
INSERT INTO `administrator_accessmodelname` VALUES (1,'default',1,'2024-08-25 14:19:21.628000',NULL,'2024-09-15 13:13:48.290000');
/*!40000 ALTER TABLE `administrator_accessmodelname` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `administrator_accessmodelname_content_type`
--

DROP TABLE IF EXISTS `administrator_accessmodelname_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `administrator_accessmodelname_content_type` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `accessmodelname_id` bigint NOT NULL,
  `contenttype_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `administrator_accessmode_accessmodelname_id_conte_93cc2af9_uniq` (`accessmodelname_id`,`contenttype_id`),
  KEY `administrator_access_contenttype_id_cfe1ba43_fk_django_co` (`contenttype_id`),
  CONSTRAINT `administrator_access_accessmodelname_id_68b76f89_fk_administr` FOREIGN KEY (`accessmodelname_id`) REFERENCES `administrator_accessmodelname` (`id`),
  CONSTRAINT `administrator_access_contenttype_id_cfe1ba43_fk_django_co` FOREIGN KEY (`contenttype_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `administrator_accessmodelname_content_type`
--

LOCK TABLES `administrator_accessmodelname_content_type` WRITE;
/*!40000 ALTER TABLE `administrator_accessmodelname_content_type` DISABLE KEYS */;
INSERT INTO `administrator_accessmodelname_content_type` VALUES (1,1,2),(2,1,3),(3,1,4),(4,1,7),(5,1,11);
/*!40000 ALTER TABLE `administrator_accessmodelname_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `administrator_companysettings`
--

DROP TABLE IF EXISTS `administrator_companysettings`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `administrator_companysettings` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `company_name` varchar(200) COLLATE utf8mb4_unicode_ci NOT NULL,
  `company_phone` varchar(20) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `company_email` varchar(150) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `company_logo` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `company_address` varchar(250) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `company_layout` varchar(2) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `company_import_option` tinyint(1) NOT NULL,
  `company_export_pdf` tinyint(1) NOT NULL,
  `company_export_csv` tinyint(1) NOT NULL,
  `company_delete_all` tinyint(1) NOT NULL,
  `company_datatable_column_visiable` tinyint(1) NOT NULL,
  `company_datatable_csv` tinyint(1) NOT NULL,
  `company_datatable_copy` tinyint(1) NOT NULL,
  `company_datatable_excel` tinyint(1) NOT NULL,
  `company_datatable_pdf` tinyint(1) NOT NULL,
  `company_datatable_print` tinyint(1) NOT NULL,
  `company_datatable_print_selected` tinyint(1) NOT NULL,
  `created_by_id` int DEFAULT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_by_id` int DEFAULT NULL,
  `updated_at` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `administrator_companysettings_created_by_id_752d88ae` (`created_by_id`),
  KEY `administrator_companysettings_updated_by_id_224094ca` (`updated_by_id`),
  CONSTRAINT `administrator_compan_created_by_id_752d88ae_fk_auth_user` FOREIGN KEY (`created_by_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `administrator_compan_updated_by_id_224094ca_fk_auth_user` FOREIGN KEY (`updated_by_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `administrator_companysettings`
--

LOCK TABLES `administrator_companysettings` WRITE;
/*!40000 ALTER TABLE `administrator_companysettings` DISABLE KEYS */;
INSERT INTO `administrator_companysettings` VALUES (1,'xyz',NULL,NULL,'',NULL,'D',1,1,0,0,0,0,0,0,0,0,0,1,'2024-09-16 06:19:33.370000',NULL,'2024-09-27 05:49:57.952755'),(2,'xyz',NULL,NULL,'',NULL,'D',0,0,0,0,0,0,0,0,0,0,0,1,'2024-09-16 06:44:48.399000',NULL,'2024-09-16 06:44:48.399000');
/*!40000 ALTER TABLE `administrator_companysettings` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `administrator_country`
--

DROP TABLE IF EXISTS `administrator_country`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `administrator_country` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `iso2` varchar(2) COLLATE utf8mb4_unicode_ci NOT NULL,
  `country_name` varchar(80) COLLATE utf8mb4_unicode_ci NOT NULL,
  `long_country_name` varchar(80) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `iso3` varchar(3) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `num_code` varchar(6) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `calling_code` varchar(8) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `created_by_id` int DEFAULT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_by_id` int DEFAULT NULL,
  `updated_at` datetime(6) NOT NULL,
  `international_region_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `administrator_countr_international_region_f1938852_fk_administr` (`international_region_id`),
  KEY `administrator_country_created_by_id_53daa615` (`created_by_id`),
  KEY `administrator_country_updated_by_id_3f80642f` (`updated_by_id`),
  CONSTRAINT `administrator_countr_international_region_f1938852_fk_administr` FOREIGN KEY (`international_region_id`) REFERENCES `administrator_internationalregion` (`id`),
  CONSTRAINT `administrator_country_created_by_id_53daa615_fk_auth_user_id` FOREIGN KEY (`created_by_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `administrator_country_updated_by_id_3f80642f_fk_auth_user_id` FOREIGN KEY (`updated_by_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=251 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `administrator_country`
--

LOCK TABLES `administrator_country` WRITE;
/*!40000 ALTER TABLE `administrator_country` DISABLE KEYS */;
INSERT INTO `administrator_country` VALUES (1,'AF','Afghanistan','Islamic Republic of Afghanistan','AFG','4','93',1,'2024-08-15 06:09:38.905000',NULL,'2024-08-15 06:09:38.905000',1),(2,'AX','Aland Islands','&Aring;land Islands','ALA','248','358',1,'2024-08-15 06:09:39.004000',NULL,'2024-08-15 06:09:39.004000',2),(3,'AL','Albania','Republic of Albania','ALB','8','355',1,'2024-08-15 06:09:39.085000',NULL,'2024-08-15 06:09:39.086000',3),(4,'DZ','Algeria','People\'s Democratic Republic of Algeria','DZA','12','213',1,'2024-08-15 06:09:39.158000',NULL,'2024-08-15 06:09:39.158000',4),(5,'AS','American Samoa','American Samoa','ASM','16','1+684',1,'2024-08-15 06:09:39.243000',NULL,'2024-08-15 06:09:39.243000',5),(6,'AD','Andorra','Principality of Andorra','AND','20','376',1,'2024-08-15 06:09:39.324000',NULL,'2024-08-15 06:09:39.324000',3),(7,'AO','Angola','Republic of Angola','AGO','24','244',1,'2024-08-15 06:09:39.403000',NULL,'2024-08-15 06:09:39.403000',4),(8,'AI','Anguilla','Anguilla','AIA','660','1+264',1,'2024-08-15 06:09:39.509000',NULL,'2024-08-15 06:09:39.509000',6),(9,'AQ','Antarctia','Antarctia','ATA','10','672',1,'2024-08-15 06:09:39.605000',NULL,'2024-08-15 06:09:39.605000',7),(10,'AG','Antigua and Barbuda','Antigua and Barbuda','ATG','28','1+268',1,'2024-08-15 06:09:39.705000',NULL,'2024-08-15 06:09:39.706000',6),(11,'AR','Argentina','Argentine Republic','ARG','32','54',1,'2024-08-15 06:09:39.806000',NULL,'2024-08-15 06:09:39.806000',8),(12,'AM','Armenia','Republic of Armenia','ARM','51','374',1,'2024-08-15 06:09:39.900000',NULL,'2024-08-15 06:09:39.900000',1),(13,'AW','Aruba','Aruba','ABW','533','297',1,'2024-08-15 06:09:39.982000',NULL,'2024-08-15 06:09:39.982000',6),(14,'AU','Australia','Commonwealth of Australia','AUS','36','61',1,'2024-08-15 06:09:40.064000',NULL,'2024-08-15 06:09:40.064000',5),(15,'AT','Austria','Republic of Austria','AUT','40','43',1,'2024-08-15 06:09:40.136000',NULL,'2024-08-15 06:09:40.136000',2),(16,'AZ','Azerbaijan','Republic of Azerbaijan','AZE','31','994',1,'2024-08-15 06:09:40.214000',NULL,'2024-08-15 06:09:40.214000',1),(17,'BS','Bahamas','Commonwealth of The Bahamas','BHS','44','1+242',1,'2024-08-15 06:09:40.292000',NULL,'2024-08-15 06:09:40.292000',6),(18,'BH','Bahrain','Kingdom of Bahrain','BHR','48','973',1,'2024-08-15 06:09:40.383000',NULL,'2024-08-15 06:09:40.383000',9),(19,'BD','Bangladesh','People\'s Republic of Bangladesh','BGD','50','880',1,'2024-08-15 06:09:40.459000',NULL,'2024-08-15 06:09:40.459000',1),(20,'BB','Barbados','Barbados','BRB','52','1+246',1,'2024-08-15 06:09:40.538000',NULL,'2024-08-15 06:09:40.538000',6),(21,'BY','Belarus','Republic of Belarus','BLR','112','375',1,'2024-08-15 06:09:40.626000',NULL,'2024-08-15 06:09:40.626000',3),(22,'BE','Belgium','Kingdom of Belgium','BEL','56','32',1,'2024-08-15 06:09:40.723000',NULL,'2024-08-15 06:09:40.723000',2),(23,'BZ','Belize','Belize','BLZ','84','501',1,'2024-08-15 06:09:40.826000',NULL,'2024-08-15 06:09:40.826000',11),(24,'BJ','Benin','Republic of Benin','BEN','204','229',1,'2024-08-15 06:09:40.936000',NULL,'2024-08-15 06:09:40.936000',4),(25,'BM','Bermuda','Bermuda Islands','BMU','60','1+441',1,'2024-08-15 06:09:41.022000',NULL,'2024-08-15 06:09:41.022000',10),(26,'BT','Bhutan','Kingdom of Bhutan','BTN','64','975',1,'2024-08-15 06:09:41.112000',NULL,'2024-08-15 06:09:41.112000',1),(27,'BO','Bolivia','Plurinational State of Bolivia','BOL','68','591',1,'2024-08-15 06:09:41.193000',NULL,'2024-08-15 06:09:41.193000',8),(28,'BQ','Bonaire, Sint Eustatius and Saba','Bonaire, Sint Eustatius and Saba','BES','535','599',1,'2024-08-15 06:09:41.380000',NULL,'2024-08-15 06:09:41.380000',6),(29,'BA','Bosnia and Herzegovina','Bosnia and Herzegovina','BIH','70','387',1,'2024-08-15 06:09:41.460000',NULL,'2024-08-15 06:09:41.460000',3),(30,'BW','Botswana','Republic of Botswana','BWA','72','267',1,'2024-08-15 06:09:41.537000',NULL,'2024-08-15 06:09:41.537000',4),(31,'BV','Bouvet Island','Bouvet Island','BVT','74','NONE',1,'2024-08-15 06:09:41.614000',NULL,'2024-08-15 06:09:41.614000',7),(32,'BR','Brazil','Federative Republic of Brazil','BRA','76','55',1,'2024-08-15 06:09:41.690000',NULL,'2024-08-15 06:09:41.692000',8),(33,'IO','British Indian Ocean Territory','British Indian Ocean Territory','IOT','86','246',1,'2024-08-15 06:09:41.804000',NULL,'2024-08-15 06:09:41.804000',1),(34,'BN','Brunei','Brunei Darussalam','BRN','96','673',1,'2024-08-15 06:09:41.897000',NULL,'2024-08-15 06:09:41.897000',1),(35,'BG','Bulgaria','Republic of Bulgaria','BGR','100','359',1,'2024-08-15 06:09:41.990000',NULL,'2024-08-15 06:09:41.990000',2),(36,'BF','Burkina Faso','Burkina Faso','BFA','854','226',1,'2024-08-15 06:09:42.090000',NULL,'2024-08-15 06:09:42.090000',4),(37,'BI','Burundi','Republic of Burundi','BDI','108','257',1,'2024-08-15 06:09:42.179000',NULL,'2024-08-15 06:09:42.179000',4),(38,'KH','Cambodia','Kingdom of Cambodia','KHM','116','855',1,'2024-08-15 06:09:42.284000',NULL,'2024-08-15 06:09:42.284000',1),(39,'CM','Cameroon','Republic of Cameroon','CMR','120','237',1,'2024-08-15 06:09:42.369000',NULL,'2024-08-15 06:09:42.369000',4),(40,'CA','Canada','Canada','CAN','124','1',1,'2024-08-15 06:09:42.451000',NULL,'2024-08-15 06:09:42.451000',10),(41,'CV','Cape Verde','Republic of Cape Verde','CPV','132','238',1,'2024-08-15 06:09:42.536000',NULL,'2024-08-15 06:09:42.536000',4),(42,'KY','Cayman Islands','The Cayman Islands','CYM','136','1+345',1,'2024-08-15 06:09:42.617000',NULL,'2024-08-15 06:09:42.617000',6),(43,'CF','Central 4n Republic','Central 4n Republic','CAF','140','236',1,'2024-08-15 06:09:42.691000',NULL,'2024-08-15 06:09:42.691000',4),(44,'TD','Chad','Republic of Chad','TCD','148','235',1,'2024-08-15 06:09:42.769000',NULL,'2024-08-15 06:09:42.769000',4),(45,'CL','Chile','Republic of Chile','CHL','152','56',1,'2024-08-15 06:09:42.857000',NULL,'2024-08-15 06:09:42.858000',8),(46,'CN','China','People\'s Republic of China','CHN','156','86',1,'2024-08-15 06:09:42.948000',NULL,'2024-08-15 06:09:42.948000',1),(47,'CX','Christmas Island','Christmas Island','CXR','162','61',1,'2024-08-15 06:09:43.043000',NULL,'2024-08-15 06:09:43.045000',5),(48,'CC','Cocos (Keeling) Islands','Cocos (Keeling) Islands','CCK','166','61',1,'2024-08-15 06:09:43.140000',NULL,'2024-08-15 06:09:43.140000',5),(49,'CO','Colombia','Republic of Colombia','COL','170','57',1,'2024-08-15 06:09:43.232000',NULL,'2024-08-15 06:09:43.232000',8),(50,'KM','Comoros','Union of the Comoros','COM','174','269',1,'2024-08-15 06:09:43.326000',NULL,'2024-08-15 06:09:43.326000',4),(51,'CG','Congo','Republic of the Congo','COG','178','242',1,'2024-08-15 06:09:43.416000',NULL,'2024-08-15 06:09:43.416000',4),(52,'CK','Cook Islands','Cook Islands','COK','184','682',1,'2024-08-15 06:09:43.493000',NULL,'2024-08-15 06:09:43.493000',5),(53,'CR','Costa Rica','Republic of Costa Rica','CRI','188','506',1,'2024-08-15 06:09:43.581000',NULL,'2024-08-15 06:09:43.581000',11),(54,'CI','Cote d\'ivoire (Ivory Coast)','Republic of C&ocirc;te D\'Ivoire (Ivory Coast)','CIV','384','225',1,'2024-08-15 06:09:43.659000',NULL,'2024-08-15 06:09:43.659000',4),(55,'HR','Croatia','Republic of Croatia','HRV','191','385',1,'2024-08-15 06:09:43.736000',NULL,'2024-08-15 06:09:43.736000',3),(56,'CU','Cuba','Republic of Cuba','CUB','192','53',1,'2024-08-15 06:09:43.818000',NULL,'2024-08-15 06:09:43.818000',6),(57,'CW','Curacao','Cura&ccedil;ao','CUW','531','599',1,'2024-08-15 06:09:43.893000',NULL,'2024-08-15 06:09:43.894000',6),(58,'CY','Cyprus','Republic of Cyprus','CYP','196','357',1,'2024-08-15 06:09:43.983000',NULL,'2024-08-15 06:09:43.983000',2),(59,'CZ','Czech Republic','Czech Republic','CZE','203','420',1,'2024-08-15 06:09:44.083000',NULL,'2024-08-15 06:09:44.083000',2),(60,'CD','Democratic Republic of the Congo','Democratic Republic of the Congo','COD','180','243',1,'2024-08-15 06:09:44.185000',NULL,'2024-08-15 06:09:44.185000',4),(61,'DK','Denmark','Kingdom of Denmark','DNK','208','45',1,'2024-08-15 06:09:44.289000',NULL,'2024-08-15 06:09:44.289000',2),(62,'DJ','Djibouti','Republic of Djibouti','DJI','262','253',1,'2024-08-15 06:09:44.383000',NULL,'2024-08-15 06:09:44.383000',4),(63,'DM','Dominica','Commonwealth of Dominica','DMA','212','1+767',1,'2024-08-15 06:09:44.466000',NULL,'2024-08-15 06:09:44.466000',6),(64,'DO','Dominican Republic','Dominican Republic','DOM','214','1+809, 8',1,'2024-08-15 06:09:44.550000',NULL,'2024-08-15 06:09:44.550000',6),(65,'EC','Ecuador','Republic of Ecuador','ECU','218','593',1,'2024-08-15 06:09:44.622000',NULL,'2024-08-15 06:09:44.623000',8),(66,'EG','Egypt','Arab Republic of Egypt','EGY','818','20',1,'2024-08-15 06:09:44.701000',NULL,'2024-08-15 06:09:44.701000',4),(67,'SV','El Salvador','Republic of El Salvador','SLV','222','503',1,'2024-08-15 06:09:44.777000',NULL,'2024-08-15 06:09:44.777000',11),(68,'GQ','Equatorial Guinea','Republic of Equatorial Guinea','GNQ','226','240',1,'2024-08-15 06:09:44.846000',NULL,'2024-08-15 06:09:44.846000',4),(69,'ER','Eritrea','State of Eritrea','ERI','232','291',1,'2024-08-15 06:09:44.925000',NULL,'2024-08-15 06:09:44.925000',4),(70,'EE','Estonia','Republic of Estonia','EST','233','372',1,'2024-08-15 06:09:45.104000',NULL,'2024-08-15 06:09:45.104000',2),(71,'ET','Ethiopia','Federal Democratic Republic of Ethiopia','ETH','231','251',1,'2024-08-15 06:09:45.191000',NULL,'2024-08-15 06:09:45.191000',4),(72,'FK','Falkland Islands (Malvinas)','The Falkland Islands (Malvinas)','FLK','238','500',1,'2024-08-15 06:09:45.282000',NULL,'2024-08-15 06:09:45.282000',8),(73,'FO','Faroe Islands','The Faroe Islands','FRO','234','298',1,'2024-08-15 06:09:45.387000',NULL,'2024-08-15 06:09:45.387000',3),(74,'FJ','Fiji','Republic of Fiji','FJI','242','679',1,'2024-08-15 06:09:45.483000',NULL,'2024-08-15 06:09:45.483000',5),(75,'FI','Finland','Republic of Finland','FIN','246','358',1,'2024-08-15 06:09:45.570000',NULL,'2024-08-15 06:09:45.570000',2),(76,'FR','France','French Republic','FRA','250','33',1,'2024-08-15 06:09:45.659000',NULL,'2024-08-15 06:09:45.659000',2),(77,'GF','French Guiana','French Guiana','GUF','254','594',1,'2024-08-15 06:09:45.748000',NULL,'2024-08-15 06:09:45.748000',8),(78,'PF','French Polynesia','French Polynesia','PYF','258','689',1,'2024-08-15 06:09:45.827000',NULL,'2024-08-15 06:09:45.827000',5),(79,'TF','French Southern Territories','French Southern Territories','ATF','260','NULL',1,'2024-08-15 06:09:45.904000',NULL,'2024-08-15 06:09:45.904000',7),(80,'GA','Gabon','Gabonese Republic','GAB','266','241',1,'2024-08-15 06:09:45.982000',NULL,'2024-08-15 06:09:45.982000',4),(81,'GM','Gambia','Republic of The Gambia','GMB','270','220',1,'2024-08-15 06:09:46.054000',NULL,'2024-08-15 06:09:46.054000',4),(82,'GE','Georgia','Georgia','GEO','268','995',1,'2024-08-15 06:09:46.125000',NULL,'2024-08-15 06:09:46.125000',1),(83,'DE','Germany','Federal Republic of Germany','DEU','276','49',1,'2024-08-15 06:09:46.214000',NULL,'2024-08-15 06:09:46.214000',2),(84,'GH','Ghana','Republic of Ghana','GHA','288','233',1,'2024-08-15 06:09:46.304000',NULL,'2024-08-15 06:09:46.304000',4),(85,'GI','Gibraltar','Gibraltar','GIB','292','350',1,'2024-08-15 06:09:46.402000',NULL,'2024-08-15 06:09:46.402000',3),(86,'GR','Greece','Hellenic Republic','GRC','300','30',1,'2024-08-15 06:09:46.489000',NULL,'2024-08-15 06:09:46.489000',2),(87,'GL','Greenland','Greenland','GRL','304','299',1,'2024-08-15 06:09:46.582000',NULL,'2024-08-15 06:09:46.582000',10),(88,'GD','Grenada','Grenada','GRD','308','1+473',1,'2024-08-15 06:09:46.661000',NULL,'2024-08-15 06:09:46.661000',6),(89,'GP','Guadeloupe','Guadeloupe','GLP','312','590',1,'2024-08-15 06:09:46.736000',NULL,'2024-08-15 06:09:46.737000',6),(90,'GU','Guam','Guam','GUM','316','1+671',1,'2024-08-15 06:09:46.817000',NULL,'2024-08-15 06:09:46.817000',5),(91,'GT','Guatemala','Republic of Guatemala','GTM','320','502',1,'2024-08-15 06:09:46.893000',NULL,'2024-08-15 06:09:46.893000',11),(92,'GG','Guernsey','Guernsey','GGY','831','44',1,'2024-08-15 06:09:46.971000',NULL,'2024-08-15 06:09:46.971000',3),(93,'GN','Guinea','Republic of Guinea','GIN','324','224',1,'2024-08-15 06:09:47.047000',NULL,'2024-08-15 06:09:47.048000',4),(94,'GW','Guinea-Bissau','Republic of Guinea-Bissau','GNB','624','245',1,'2024-08-15 06:09:47.127000',NULL,'2024-08-15 06:09:47.127000',4),(95,'GY','Guyana','Co-operative Republic of Guyana','GUY','328','592',1,'2024-08-15 06:09:47.215000',NULL,'2024-08-15 06:09:47.215000',8),(96,'HT','Haiti','Republic of Haiti','HTI','332','509',1,'2024-08-15 06:09:47.304000',NULL,'2024-08-15 06:09:47.304000',6),(97,'HM','Heard Island and McDonald Islands','Heard Island and McDonald Islands','HMD','334','NONE',1,'2024-08-15 06:09:47.402000',NULL,'2024-08-15 06:09:47.403000',7),(98,'HN','Honduras','Republic of Honduras','HND','340','504',1,'2024-08-15 06:09:47.504000',NULL,'2024-08-15 06:09:47.504000',11),(99,'HK','Hong Kong','Hong Kong','HKG','344','852',1,'2024-08-15 06:09:47.589000',NULL,'2024-08-15 06:09:47.589000',1),(100,'HU','Hungary','Hungary','HUN','348','36',1,'2024-08-15 06:09:47.671000',NULL,'2024-08-15 06:09:47.671000',2),(101,'IS','Iceland','Republic of Iceland','ISL','352','354',1,'2024-08-15 06:09:47.748000',NULL,'2024-08-15 06:09:47.748000',3),(102,'IN','India','Republic of India','IND','356','91',1,'2024-08-15 06:09:47.827000',NULL,'2024-08-15 06:09:47.828000',1),(103,'ID','Indonesia','Republic of Indonesia','IDN','360','62',1,'2024-08-15 06:09:47.903000',NULL,'2024-08-15 06:09:47.903000',1),(104,'IR','Iran','Islamic Republic of Iran','IRN','364','98',1,'2024-08-15 06:09:47.984000',NULL,'2024-08-15 06:09:47.984000',9),(105,'IQ','Iraq','Republic of Iraq','IRQ','368','964',1,'2024-08-15 06:09:48.057000',NULL,'2024-08-15 06:09:48.058000',9),(106,'IE','Ireland','Ireland','IRL','372','353',1,'2024-08-15 06:09:48.138000',NULL,'2024-08-15 06:09:48.138000',2),(107,'IM','Isle of Man','Isle of Man','IMN','833','44',1,'2024-08-15 06:09:48.237000',NULL,'2024-08-15 06:09:48.237000',2),(108,'IL','Israel','State of Israel','ISR','376','972',1,'2024-08-15 06:09:48.327000',NULL,'2024-08-15 06:09:48.327000',9),(109,'IT','Italy','Italian Republic','ITA','380','39',1,'2024-08-15 06:09:48.424000',NULL,'2024-08-15 06:09:48.424000',2),(110,'JM','Jamaica','Jamaica','JAM','388','1+876',1,'2024-08-15 06:09:48.527000',NULL,'2024-08-15 06:09:48.527000',6),(111,'JP','Japan','Japan','JPN','392','81',1,'2024-08-15 06:09:48.621000',NULL,'2024-08-15 06:09:48.621000',1),(112,'JE','Jersey','The Bailiwick of Jersey','JEY','832','44',1,'2024-08-15 06:09:48.715000',NULL,'2024-08-15 06:09:48.715000',3),(113,'JO','Jordan','Hashemite Kingdom of Jordan','JOR','400','962',1,'2024-08-15 06:09:48.914000',NULL,'2024-08-15 06:09:48.914000',9),(114,'KZ','Kazakhstan','Republic of Kazakhstan','KAZ','398','7',1,'2024-08-15 06:09:48.995000',NULL,'2024-08-15 06:09:48.995000',1),(115,'KE','Kenya','Republic of Kenya','KEN','404','254',1,'2024-08-15 06:09:49.115000',NULL,'2024-08-15 06:09:49.115000',4),(116,'KI','Kiribati','Republic of Kiribati','KIR','296','686',1,'2024-08-15 06:09:49.193000',NULL,'2024-08-15 06:09:49.193000',5),(117,'XK','Kosovo','Republic of Kosovo','---','---','381',1,'2024-08-15 06:09:49.269000',NULL,'2024-08-15 06:09:49.269000',3),(118,'KW','Kuwait','State of Kuwait','KWT','414','965',1,'2024-08-15 06:09:49.359000',NULL,'2024-08-15 06:09:49.360000',9),(119,'KG','Kyrgyzstan','Kyrgyz Republic','KGZ','417','996',1,'2024-08-15 06:09:49.458000',NULL,'2024-08-15 06:09:49.458000',1),(120,'LA','Laos','Lao People\'s Democratic Republic','LAO','418','856',1,'2024-08-15 06:09:49.539000',NULL,'2024-08-15 06:09:49.539000',1),(121,'LV','Latvia','Republic of Latvia','LVA','428','371',1,'2024-08-15 06:09:49.637000',NULL,'2024-08-15 06:09:49.637000',2),(122,'LB','Lebanon','Republic of Lebanon','LBN','422','961',1,'2024-08-15 06:09:49.736000',NULL,'2024-08-15 06:09:49.736000',9),(123,'LS','Lesotho','Kingdom of Lesotho','LSO','426','266',1,'2024-08-15 06:09:49.826000',NULL,'2024-08-15 06:09:49.826000',4),(124,'LR','Liberia','Republic of Liberia','LBR','430','231',1,'2024-08-15 06:09:49.916000',NULL,'2024-08-15 06:09:49.916000',4),(125,'LY','Libya','Libya','LBY','434','218',1,'2024-08-15 06:09:50.002000',NULL,'2024-08-15 06:09:50.002000',4),(126,'LI','Liechtenstein','Principality of Liechtenstein','LIE','438','423',1,'2024-08-15 06:09:50.083000',NULL,'2024-08-15 06:09:50.083000',3),(127,'LT','Lithuania','Republic of Lithuania','LTU','440','370',1,'2024-08-15 06:09:50.159000',NULL,'2024-08-15 06:09:50.159000',2),(128,'LU','Luxembourg','Grand Duchy of Luxembourg','LUX','442','352',1,'2024-08-15 06:09:50.240000',NULL,'2024-08-15 06:09:50.240000',2),(129,'MO','Macao','The Macao Special Administrative Region','MAC','446','853',1,'2024-08-15 06:09:50.314000',NULL,'2024-08-15 06:09:50.314000',1),(130,'MK','Macedonia','The Former Yugoslav Republic of Macedonia','MKD','807','389',1,'2024-08-15 06:09:50.394000',NULL,'2024-08-15 06:09:50.394000',3),(131,'MG','Madagascar','Republic of Madagascar','MDG','450','261',1,'2024-08-15 06:09:50.492000',NULL,'2024-08-15 06:09:50.492000',4),(132,'MW','Malawi','Republic of Malawi','MWI','454','265',1,'2024-08-15 06:09:50.582000',NULL,'2024-08-15 06:09:50.582000',4),(133,'MY','Malaysia','Malaysia','MYS','458','60',1,'2024-08-15 06:09:50.683000',NULL,'2024-08-15 06:09:50.683000',1),(134,'MV','Maldives','Republic of Maldives','MDV','462','960',1,'2024-08-15 06:09:50.790000',NULL,'2024-08-15 06:09:50.790000',1),(135,'ML','Mali','Republic of Mali','MLI','466','223',1,'2024-08-15 06:09:50.881000',NULL,'2024-08-15 06:09:50.881000',4),(136,'MT','Malta','Republic of Malta','MLT','470','356',1,'2024-08-15 06:09:50.984000',NULL,'2024-08-15 06:09:50.984000',2),(137,'MH','Marshall Islands','Republic of the Marshall Islands','MHL','584','692',1,'2024-08-15 06:09:51.058000',NULL,'2024-08-15 06:09:51.058000',5),(138,'MQ','Martinique','Martinique','MTQ','474','596',1,'2024-08-15 06:09:51.138000',NULL,'2024-08-15 06:09:51.138000',6),(139,'MR','Mauritania','Islamic Republic of Mauritania','MRT','478','222',1,'2024-08-15 06:09:51.215000',NULL,'2024-08-15 06:09:51.215000',4),(140,'MU','Mauritius','Republic of Mauritius','MUS','480','230',1,'2024-08-15 06:09:51.296000',NULL,'2024-08-15 06:09:51.296000',4),(141,'YT','Mayotte','Mayotte','MYT','175','262',1,'2024-08-15 06:09:51.370000',NULL,'2024-08-15 06:09:51.370000',4),(142,'MX','Mexico','United Mexican States','MEX','484','52',1,'2024-08-15 06:09:51.447000',NULL,'2024-08-15 06:09:51.448000',11),(143,'FM','Micronesia','Federated States of Micronesia','FSM','583','691',1,'2024-08-15 06:09:51.538000',NULL,'2024-08-15 06:09:51.538000',5),(144,'MD','Moldova','Republic of Moldova','MDA','498','373',1,'2024-08-15 06:09:51.628000',NULL,'2024-08-15 06:09:51.628000',3),(145,'MC','Monaco','Principality of Monaco','MCO','492','377',1,'2024-08-15 06:09:51.725000',NULL,'2024-08-15 06:09:51.725000',3),(146,'MN','Mongolia','Mongolia','MNG','496','976',1,'2024-08-15 06:09:51.834000',NULL,'2024-08-15 06:09:51.834000',1),(147,'ME','Montenegro','Montenegro','MNE','499','382',1,'2024-08-15 06:09:51.921000',NULL,'2024-08-15 06:09:51.921000',3),(148,'MS','Montserrat','Montserrat','MSR','500','1+664',1,'2024-08-15 06:09:52.003000',NULL,'2024-08-15 06:09:52.003000',6),(149,'MA','Morocco','Kingdom of Morocco','MAR','504','212',1,'2024-08-15 06:09:52.092000',NULL,'2024-08-15 06:09:52.092000',4),(150,'MZ','Mozambique','Republic of Mozambique','MOZ','508','258',1,'2024-08-15 06:09:52.171000',NULL,'2024-08-15 06:09:52.171000',4),(151,'MM','Myanmar (Burma)','Republic of the Union of Myanmar','MMR','104','95',1,'2024-08-15 06:09:52.249000',NULL,'2024-08-15 06:09:52.249000',1),(152,'NA','Namibia','Republic of Namibia','NAM','516','264',1,'2024-08-15 06:09:52.328000',NULL,'2024-08-15 06:09:52.329000',4),(153,'NR','Nauru','Republic of Nauru','NRU','520','674',1,'2024-08-15 06:09:52.403000',NULL,'2024-08-15 06:09:52.403000',5),(154,'NP','Nepal','Federal Democratic Republic of Nepal','NPL','524','977',1,'2024-08-15 06:09:52.482000',NULL,'2024-08-15 06:09:52.482000',1),(155,'NL','Netherlands','Kingdom of the Netherlands','NLD','528','31',1,'2024-08-15 06:09:52.685000',NULL,'2024-08-15 06:09:52.685000',2),(156,'NC','New Caledonia','New Caledonia','NCL','540','687',1,'2024-08-15 06:09:52.781000',NULL,'2024-08-15 06:09:52.781000',5),(157,'NZ','New Zealand','New Zealand','NZL','554','64',1,'2024-08-15 06:09:52.884000',NULL,'2024-08-15 06:09:52.884000',5),(158,'NI','Nicaragua','Republic of Nicaragua','NIC','558','505',1,'2024-08-15 06:09:53.000000',NULL,'2024-08-15 06:09:53.000000',11),(159,'NE','Niger','Republic of Niger','NER','562','227',1,'2024-08-15 06:09:53.091000',NULL,'2024-08-15 06:09:53.091000',4),(160,'NG','Nigeria','Federal Republic of Nigeria','NGA','566','234',1,'2024-08-15 06:09:53.167000',NULL,'2024-08-15 06:09:53.167000',4),(161,'NU','Niue','Niue','NIU','570','683',1,'2024-08-15 06:09:53.247000',NULL,'2024-08-15 06:09:53.247000',5),(162,'NF','Norfolk Island','Norfolk Island','NFK','574','672',1,'2024-08-15 06:09:53.327000',NULL,'2024-08-15 06:09:53.327000',5),(163,'KP','North Korea','Democratic People\'s Republic of Korea','PRK','408','850',1,'2024-08-15 06:09:53.403000',NULL,'2024-08-15 06:09:53.403000',1),(164,'MP','Northern Mariana Islands','Northern Mariana Islands','MNP','580','1+670',1,'2024-08-15 06:09:53.484000',NULL,'2024-08-15 06:09:53.484000',5),(165,'NO','Norway','Kingdom of Norway','NOR','578','47',1,'2024-08-15 06:09:53.561000',NULL,'2024-08-15 06:09:53.561000',3),(166,'OM','Oman','Sultanate of Oman','OMN','512','968',1,'2024-08-15 06:09:53.636000',NULL,'2024-08-15 06:09:53.636000',9),(167,'PK','Pakistan','Islamic Republic of Pakistan','PAK','586','92',1,'2024-08-15 06:09:53.725000',NULL,'2024-08-15 06:09:53.725000',1),(168,'PW','Palau','Republic of Palau','PLW','585','680',1,'2024-08-15 06:09:53.826000',NULL,'2024-08-15 06:09:53.826000',5),(169,'PS','Palestine','State of Palestine (or Occupied Palestinian Territory)','PSE','275','970',1,'2024-08-15 06:09:53.916000',NULL,'2024-08-15 06:09:53.916000',9),(170,'PA','Panama','Republic of Panama','PAN','591','507',1,'2024-08-15 06:09:54.013000',NULL,'2024-08-15 06:09:54.013000',11),(171,'PG','Papua New Guinea','Independent State of Papua New Guinea','PNG','598','675',1,'2024-08-15 06:09:54.090000',NULL,'2024-08-15 06:09:54.090000',5),(172,'PY','Paraguay','Republic of Paraguay','PRY','600','595',1,'2024-08-15 06:09:54.171000',NULL,'2024-08-15 06:09:54.171000',8),(173,'PE','Peru','Republic of Peru','PER','604','51',1,'2024-08-15 06:09:54.249000',NULL,'2024-08-15 06:09:54.249000',8),(174,'PH','Phillipines','Republic of the Philippines','PHL','608','63',1,'2024-08-15 06:09:54.329000',NULL,'2024-08-15 06:09:54.329000',1),(175,'PN','Pitcairn','Pitcairn','PCN','612','NONE',1,'2024-08-15 06:09:54.402000',NULL,'2024-08-15 06:09:54.402000',5),(176,'PL','Poland','Republic of Poland','POL','616','48',1,'2024-08-15 06:09:54.485000',NULL,'2024-08-15 06:09:54.485000',2),(177,'PT','Portugal','Portuguese Republic','PRT','620','351',1,'2024-08-15 06:09:54.557000',NULL,'2024-08-15 06:09:54.557000',2),(178,'PR','Puerto Rico','Commonwealth of Puerto Rico','PRI','630','1+939',1,'2024-08-15 06:09:54.637000',NULL,'2024-08-15 06:09:54.637000',6),(179,'QA','Qatar','State of Qatar','QAT','634','974',1,'2024-08-15 06:09:54.735000',NULL,'2024-08-15 06:09:54.735000',9),(180,'RE','Reunion','R&eacute;union','REU','638','262',1,'2024-08-15 06:09:54.826000',NULL,'2024-08-15 06:09:54.827000',4),(181,'RO','Romania','Romania','ROU','642','40',1,'2024-08-15 06:09:54.911000',NULL,'2024-08-15 06:09:54.911000',2),(182,'RU','Russia','Russian Federation','RUS','643','7',1,'2024-08-15 06:09:55.001000',NULL,'2024-08-15 06:09:55.001000',3),(183,'RW','Rwanda','Republic of Rwanda','RWA','646','250',1,'2024-08-15 06:09:55.076000',NULL,'2024-08-15 06:09:55.076000',4),(184,'BL','Saint Barthelemy','Saint Barth&eacute;lemy','BLM','652','590',1,'2024-08-15 06:09:55.158000',NULL,'2024-08-15 06:09:55.158000',6),(185,'SH','Saint Helena','Saint Helena, Ascension and Tristan da Cunha','SHN','654','290',1,'2024-08-15 06:09:55.236000',NULL,'2024-08-15 06:09:55.236000',4),(186,'KN','Saint Kitts and Nevis','Federation of Saint Christopher and Nevis','KNA','659','1+869',1,'2024-08-15 06:09:55.317000',NULL,'2024-08-15 06:09:55.317000',6),(187,'LC','Saint Lucia','Saint Lucia','LCA','662','1+758',1,'2024-08-15 06:09:55.392000',NULL,'2024-08-15 06:09:55.392000',6),(188,'MF','Saint Martin','Saint Martin','MAF','663','590',1,'2024-08-15 06:09:55.472000',NULL,'2024-08-15 06:09:55.472000',6),(189,'PM','Saint Pierre and Miquelon','Saint Pierre and Miquelon','SPM','666','508',1,'2024-08-15 06:09:55.548000',NULL,'2024-08-15 06:09:55.548000',10),(190,'VC','Saint Vincent and the Grenadines','Saint Vincent and the Grenadines','VCT','670','1+784',1,'2024-08-15 06:09:55.628000',NULL,'2024-08-15 06:09:55.628000',6),(191,'WS','Samoa','Independent State of Samoa','WSM','882','685',1,'2024-08-15 06:09:55.725000',NULL,'2024-08-15 06:09:55.725000',5),(192,'SM','San Marino','Republic of San Marino','SMR','674','378',1,'2024-08-15 06:09:55.818000',NULL,'2024-08-15 06:09:55.819000',3),(193,'ST','Sao Tome and Principe','Democratic Republic of S&atilde;o Tom&eacute; and Pr&iacute;ncipe','STP','678','239',1,'2024-08-15 06:09:55.925000',NULL,'2024-08-15 06:09:55.926000',4),(194,'SA','Saudi Arabia','Kingdom of Saudi Arabia','SAU','682','966',1,'2024-08-15 06:09:56.027000',NULL,'2024-08-15 06:09:56.027000',9),(195,'SN','Senegal','Republic of Senegal','SEN','686','221',1,'2024-08-15 06:09:56.117000',NULL,'2024-08-15 06:09:56.117000',4),(196,'RS','Serbia','Republic of Serbia','SRB','688','381',1,'2024-08-15 06:09:56.190000',NULL,'2024-08-15 06:09:56.190000',3),(197,'SC','Seychelles','Republic of Seychelles','SYC','690','248',1,'2024-08-15 06:09:56.382000',NULL,'2024-08-15 06:09:56.382000',4),(198,'SL','Sierra Leone','Republic of Sierra Leone','SLE','694','232',1,'2024-08-15 06:09:56.461000',NULL,'2024-08-15 06:09:56.461000',4),(199,'SG','Singapore','Republic of Singapore','SGP','702','65',1,'2024-08-15 06:09:56.536000',NULL,'2024-08-15 06:09:56.536000',1),(200,'SX','Sint Maarten','Sint Maarten','SXM','534','1+721',1,'2024-08-15 06:09:56.617000',NULL,'2024-08-15 06:09:56.617000',6),(201,'SK','Slovakia','Slovak Republic','SVK','703','421',1,'2024-08-15 06:09:56.692000',NULL,'2024-08-15 06:09:56.692000',2),(202,'SI','Slovenia','Republic of Slovenia','SVN','705','386',1,'2024-08-15 06:09:56.768000',NULL,'2024-08-15 06:09:56.768000',2),(203,'SB','Solomon Islands','Solomon Islands','SLB','90','677',1,'2024-08-15 06:09:56.856000',NULL,'2024-08-15 06:09:56.856000',5),(204,'SO','Somalia','Somali Republic','SOM','706','252',1,'2024-08-15 06:09:56.949000',NULL,'2024-08-15 06:09:56.949000',4),(205,'ZA','South 4','Republic of South 4','ZAF','710','27',1,'2024-08-15 06:09:57.057000',NULL,'2024-08-15 06:09:57.057000',4),(206,'GS','South Georgia and the South Sandwich Islands','South Georgia and the South Sandwich Islands','SGS','239','500',1,'2024-08-15 06:09:57.160000',NULL,'2024-08-15 06:09:57.160000',8),(207,'KR','South Korea','Republic of Korea','KOR','410','82',1,'2024-08-15 06:09:57.246000',NULL,'2024-08-15 06:09:57.246000',1),(208,'SS','South Sudan','Republic of South Sudan','SSD','728','211',1,'2024-08-15 06:09:57.326000',NULL,'2024-08-15 06:09:57.326000',4),(209,'ES','Spain','Kingdom of Spain','ESP','724','34',1,'2024-08-15 06:09:57.414000',NULL,'2024-08-15 06:09:57.414000',2),(210,'LK','Sri Lanka','Democratic Socialist Republic of Sri Lanka','LKA','144','94',1,'2024-08-15 06:09:57.494000',NULL,'2024-08-15 06:09:57.495000',1),(211,'SD','Sudan','Republic of the Sudan','SDN','729','249',1,'2024-08-15 06:09:57.568000',NULL,'2024-08-15 06:09:57.568000',4),(212,'SR','Suriname','Republic of Suriname','SUR','740','597',1,'2024-08-15 06:09:57.648000',NULL,'2024-08-15 06:09:57.648000',8),(213,'SJ','Svalbard and Jan Mayen','Svalbard and Jan Mayen','SJM','744','47',1,'2024-08-15 06:09:57.733000',NULL,'2024-08-15 06:09:57.733000',3),(214,'SZ','Swaziland','Kingdom of Swaziland','SWZ','748','268',1,'2024-08-15 06:09:57.813000',NULL,'2024-08-15 06:09:57.813000',4),(215,'SE','Sweden','Kingdom of Sweden','SWE','752','46',1,'2024-08-15 06:09:57.900000',NULL,'2024-08-15 06:09:57.900000',2),(216,'CH','Switzerland','Swiss Confederation','CHE','756','41',1,'2024-08-15 06:09:58.002000',NULL,'2024-08-15 06:09:58.002000',3),(217,'SY','Syria','Syrian Arab Republic','SYR','760','963',1,'2024-08-15 06:09:58.092000',NULL,'2024-08-15 06:09:58.092000',9),(218,'TW','Taiwan','Republic of China (Taiwan)','TWN','158','886',1,'2024-08-15 06:09:58.181000',NULL,'2024-08-15 06:09:58.181000',1),(219,'TJ','Tajikistan','Republic of Tajikistan','TJK','762','992',1,'2024-08-15 06:09:58.269000',NULL,'2024-08-15 06:09:58.269000',1),(220,'TZ','Tanzania','United Republic of Tanzania','TZA','834','255',1,'2024-08-15 06:09:58.347000',NULL,'2024-08-15 06:09:58.347000',4),(221,'TH','Thailand','Kingdom of Thailand','THA','764','66',1,'2024-08-15 06:09:58.436000',NULL,'2024-08-15 06:09:58.436000',1),(222,'TL','Timor-Leste (East Timor)','Democratic Republic of Timor-Leste','TLS','626','670',1,'2024-08-15 06:09:58.512000',NULL,'2024-08-15 06:09:58.512000',5),(223,'TG','Togo','Togolese Republic','TGO','768','228',1,'2024-08-15 06:09:58.580000',NULL,'2024-08-15 06:09:58.580000',4),(224,'TK','Tokelau','Tokelau','TKL','772','690',1,'2024-08-15 06:09:58.659000',NULL,'2024-08-15 06:09:58.660000',5),(225,'TO','Tonga','Kingdom of Tonga','TON','776','676',1,'2024-08-15 06:09:58.758000',NULL,'2024-08-15 06:09:58.758000',5),(226,'TT','Trinidad and Tobago','Republic of Trinidad and Tobago','TTO','780','1+868',1,'2024-08-15 06:09:58.862000',NULL,'2024-08-15 06:09:58.862000',6),(227,'TN','Tunisia','Republic of Tunisia','TUN','788','216',1,'2024-08-15 06:09:58.958000',NULL,'2024-08-15 06:09:58.959000',4),(228,'TR','Turkey','Republic of Turkey','TUR','792','90',1,'2024-08-15 06:09:59.051000',NULL,'2024-08-15 06:09:59.051000',3),(229,'TM','Turkmenistan','Turkmenistan','TKM','795','993',1,'2024-08-15 06:09:59.159000',NULL,'2024-08-15 06:09:59.159000',1),(230,'TC','Turks and Caicos Islands','Turks and Caicos Islands','TCA','796','1+649',1,'2024-08-15 06:09:59.261000',NULL,'2024-08-15 06:09:59.262000',6),(231,'TV','Tuvalu','Tuvalu','TUV','798','688',1,'2024-08-15 06:09:59.349000',NULL,'2024-08-15 06:09:59.349000',5),(232,'UG','Uganda','Republic of Uganda','UGA','800','256',1,'2024-08-15 06:09:59.423000',NULL,'2024-08-15 06:09:59.423000',4),(233,'UA','Ukraine','Ukraine','UKR','804','380',1,'2024-08-15 06:09:59.502000',NULL,'2024-08-15 06:09:59.502000',3),(234,'AE','United Arab Emirates','United Arab Emirates','ARE','784','971',1,'2024-08-15 06:09:59.583000',NULL,'2024-08-15 06:09:59.583000',9),(235,'GB','United Kingdom','United Kingdom of Great Britain and Nothern Ireland','GBR','826','44',1,'2024-08-15 06:09:59.658000',NULL,'2024-08-15 06:09:59.658000',2),(236,'US','United States','United States of America','USA','840','1',1,'2024-08-15 06:09:59.739000',NULL,'2024-08-15 06:09:59.739000',10),(237,'UM','United States Minor Outlying Islands','United States Minor Outlying Islands','UMI','581','NONE',1,'2024-08-15 06:09:59.826000',NULL,'2024-08-15 06:09:59.826000',5),(238,'UY','Uruguay','Eastern Republic of Uruguay','URY','858','598',1,'2024-08-15 06:09:59.917000',NULL,'2024-08-15 06:09:59.917000',8),(239,'UZ','Uzbekistan','Republic of Uzbekistan','UZB','860','998',1,'2024-08-15 06:10:00.016000',NULL,'2024-08-15 06:10:00.016000',1),(240,'VU','Vanuatu','Republic of Vanuatu','VUT','548','678',1,'2024-08-15 06:10:00.215000',NULL,'2024-08-15 06:10:00.215000',5),(241,'VA','Vatican City','State of the Vatican City','VAT','336','39',1,'2024-08-15 06:10:00.315000',NULL,'2024-08-15 06:10:00.315000',3),(242,'VE','Venezuela','Bolivarian Republic of Venezuela','VEN','862','58',1,'2024-08-15 06:10:00.405000',NULL,'2024-08-15 06:10:00.405000',8),(243,'VN','Vietnam','Socialist Republic of Vietnam','VNM','704','84',1,'2024-08-15 06:10:00.487000',NULL,'2024-08-15 06:10:00.487000',1),(244,'VG','Virgin Islands, British','British Virgin Islands','VGB','92','1+284',1,'2024-08-15 06:10:00.572000',NULL,'2024-08-15 06:10:00.572000',6),(245,'VI','Virgin Islands, US','Virgin Islands of the United States','VIR','850','1+340',1,'2024-08-15 06:10:00.647000',NULL,'2024-08-15 06:10:00.647000',6),(246,'WF','Wallis and Futuna','Wallis and Futuna','WLF','876','681',1,'2024-08-15 06:10:00.727000',NULL,'2024-08-15 06:10:00.727000',5),(247,'EH','Western Sahara','Western Sahara','ESH','732','212',1,'2024-08-15 06:10:00.802000',NULL,'2024-08-15 06:10:00.802000',4),(248,'YE','Yemen','Republic of Yemen','YEM','887','967',1,'2024-08-15 06:10:00.886000',NULL,'2024-08-15 06:10:00.886000',9),(249,'ZM','Zambia','Republic of Zambia','ZMB','894','260',1,'2024-08-15 06:10:00.957000',NULL,'2024-08-15 06:10:00.957000',4),(250,'ZW','Zimbabwe','Republic of Zimbabwe','ZWE','716','263',1,'2024-08-15 06:10:01.038000',NULL,'2024-08-15 06:10:01.038000',4);
/*!40000 ALTER TABLE `administrator_country` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `administrator_internationalregion`
--

DROP TABLE IF EXISTS `administrator_internationalregion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `administrator_internationalregion` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `international_region_name` varchar(80) COLLATE utf8mb4_unicode_ci NOT NULL,
  `created_by_id` int DEFAULT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_by_id` int DEFAULT NULL,
  `updated_at` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `administrator_internationalregion_created_by_id_c8aaac9d` (`created_by_id`),
  KEY `administrator_internationalregion_updated_by_id_87edca1e` (`updated_by_id`),
  CONSTRAINT `administrator_intern_created_by_id_c8aaac9d_fk_auth_user` FOREIGN KEY (`created_by_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `administrator_intern_updated_by_id_87edca1e_fk_auth_user` FOREIGN KEY (`updated_by_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `administrator_internationalregion`
--

LOCK TABLES `administrator_internationalregion` WRITE;
/*!40000 ALTER TABLE `administrator_internationalregion` DISABLE KEYS */;
INSERT INTO `administrator_internationalregion` VALUES (1,'Asia',1,'2024-08-15 06:09:27.094000',NULL,'2024-08-15 06:09:27.094000'),(2,'European Union',1,'2024-08-15 06:09:27.201000',NULL,'2024-08-15 06:09:27.201000'),(3,'Europe',1,'2024-08-15 06:09:27.299000',NULL,'2024-08-15 06:09:27.299000'),(4,'Africa',1,'2024-08-15 06:09:27.389000',NULL,'2024-08-15 06:09:27.390000'),(5,'Oceania',1,'2024-08-15 06:09:27.466000',NULL,'2024-08-15 06:09:27.466000'),(6,'The Caribbean',1,'2024-08-15 06:09:27.546000',NULL,'2024-08-15 06:09:27.546000'),(7,'Antarctia',1,'2024-08-15 06:09:27.634000',NULL,'2024-08-15 06:09:27.634000'),(8,'South America',1,'2024-08-15 06:09:27.713000',NULL,'2024-08-15 06:09:27.713000'),(9,'Middle East',1,'2024-08-15 06:09:27.788000',NULL,'2024-08-15 06:09:27.788000'),(10,'North America',1,'2024-08-15 06:09:27.868000',NULL,'2024-08-15 06:09:27.868000'),(11,'Central America',1,'2024-08-15 06:09:27.943000',NULL,'2024-08-15 06:09:27.943000'),(12,'dd',2,'2024-08-25 10:40:24.947000',NULL,'2024-08-25 10:40:24.947000');
/*!40000 ALTER TABLE `administrator_internationalregion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=45 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add company settings',7,'add_companysettings'),(26,'Can change company settings',7,'change_companysettings'),(27,'Can delete company settings',7,'delete_companysettings'),(28,'Can view company settings',7,'view_companysettings'),(29,'Can add internationalregion',8,'add_internationalregion'),(30,'Can change internationalregion',8,'change_internationalregion'),(31,'Can delete internationalregion',8,'delete_internationalregion'),(32,'Can view internationalregion',8,'view_internationalregion'),(33,'Can add access model name',9,'add_accessmodelname'),(34,'Can change access model name',9,'change_accessmodelname'),(35,'Can delete access model name',9,'delete_accessmodelname'),(36,'Can view access model name',9,'view_accessmodelname'),(37,'Can add country',10,'add_country'),(38,'Can change country',10,'change_country'),(39,'Can delete country',10,'delete_country'),(40,'Can view country',10,'view_country'),(41,'Can add profile',11,'add_profile'),(42,'Can change profile',11,'change_profile'),(43,'Can delete profile',11,'delete_profile'),(44,'Can view profile',11,'view_profile');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) COLLATE utf8mb4_unicode_ci NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) COLLATE utf8mb4_unicode_ci NOT NULL,
  `first_name` varchar(150) COLLATE utf8mb4_unicode_ci NOT NULL,
  `last_name` varchar(150) COLLATE utf8mb4_unicode_ci NOT NULL,
  `email` varchar(254) COLLATE utf8mb4_unicode_ci NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$870000$Xf6sam2qwsJw2MnTcdtx3B$Cho85mKNE2TNZp6np3rZ46zTIOrlmi1PUbnLd0Ygsbs=','2024-10-20 06:19:15.644884',1,'anup','Anup','Mondal','anup12.m@gmail.com',1,1,'2024-09-16 06:49:55.132000'),(2,'pbkdf2_sha256$870000$evb8xdjxpV4DZbAhG6SDE5$PhbxNwkUQ68JOr4V1EMycG2Gsf+ppOvJhkylafrnmgM=','2024-09-27 05:50:59.519127',0,'admin','','','admin@admin.com',1,1,'2024-09-16 07:35:17.044000'),(3,'pbkdf2_sha256$870000$OyooLy9K0pYJcMOU3MSNsR$FQCzBtV+YBpwG6PPBH5ROCH6VFuDzSOEhsqgSxkIEYM=',NULL,0,'staff','','','staff@staff.com',0,1,'2024-09-16 07:35:38.518000');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext COLLATE utf8mb4_unicode_ci,
  `object_repr` varchar(200) COLLATE utf8mb4_unicode_ci NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `model` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(9,'administrator','accessmodelname'),(7,'administrator','companysettings'),(10,'administrator','country'),(8,'administrator','internationalregion'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(6,'sessions','session'),(11,'userprofile','profile');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `name` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2024-09-20 09:54:22.512229'),(2,'auth','0001_initial','2024-09-20 09:54:23.468024'),(3,'admin','0001_initial','2024-09-20 09:54:23.705414'),(4,'admin','0002_logentry_remove_auto_add','2024-09-20 09:54:23.716944'),(5,'admin','0003_logentry_add_action_flag_choices','2024-09-20 09:54:23.727423'),(6,'contenttypes','0002_remove_content_type_name','2024-09-20 09:54:23.829297'),(7,'administrator','0001_initial','2024-09-20 09:54:24.135416'),(8,'auth','0002_alter_permission_name_max_length','2024-09-20 09:54:24.222349'),(9,'auth','0003_alter_user_email_max_length','2024-09-20 09:54:24.248929'),(10,'auth','0004_alter_user_username_opts','2024-09-20 09:54:24.258246'),(11,'auth','0005_alter_user_last_login_null','2024-09-20 09:54:24.341276'),(12,'auth','0006_require_contenttypes_0002','2024-09-20 09:54:24.345326'),(13,'auth','0007_alter_validators_add_error_messages','2024-09-20 09:54:24.357517'),(14,'auth','0008_alter_user_username_max_length','2024-09-20 09:54:24.444946'),(15,'auth','0009_alter_user_last_name_max_length','2024-09-20 09:54:24.529732'),(16,'auth','0010_alter_group_name_max_length','2024-09-20 09:54:24.552688'),(17,'auth','0011_update_proxy_permissions','2024-09-20 09:54:24.569206'),(18,'auth','0012_alter_user_first_name_max_length','2024-09-20 09:54:24.652175'),(19,'sessions','0001_initial','2024-09-20 09:54:24.699374'),(20,'userprofile','0001_initial','2024-09-20 09:54:24.904752'),(21,'administrator','0002_alter_accessmodelname_created_by_and_more','2024-10-20 06:19:03.274636'),(22,'userprofile','0002_alter_profile_created_by_alter_profile_updated_by','2024-10-20 06:19:03.638020');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) COLLATE utf8mb4_unicode_ci NOT NULL,
  `session_data` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('gnv8ihpc35nuxf8li5fpiau323gcm43s','.eJxVjEEOwiAQRe_C2hBwQKhL9z0DGYZBqgaS0q6Md7dNutDtf-_9twi4LiWsnecwJXEVWpx-t4j05LqD9MB6b5JaXeYpyl2RB-1ybIlft8P9OyjYy1Y7RRRJGWJD0XIC49mDy5Gcp2wVsEazgQHxbEFlZTUosibD4PiCXny-B_k4Vw:1stI17:UcFzfK3y9l1upB0u6vuvI9MA-qdREi2yYtNTggDVCYI','2024-10-09 02:44:37.816779'),('hcyxn0cuznl1t6dpgjakadfnv8i36xea','.eJxVjEEOwiAQRe_C2hBwQKhL9z0DGYZBqgaS0q6Md7dNutDtf-_9twi4LiWsnecwJXEVWpx-t4j05LqD9MB6b5JaXeYpyl2RB-1ybIlft8P9OyjYy1Y7RRRJGWJD0XIC49mDy5Gcp2wVsEazgQHxbEFlZTUosibD4PiCXny-B_k4Vw:1st3Bf:ZDvIRCO2mWCo-6k8lcTliPQCXXY6Mvc_iCzkRKVKnUs','2024-10-08 10:54:31.383501'),('jcqssb869677rxqche543ugmhhjcs6mf','.eJxVjkEOgyAURO_C2hBBRHDZfc9gPvBRWgsN4Krp3auJSdvMbubNZF5kgq0u01YwT8GRkXDS_HoG7B3jEbgbxDlRm2LNwdADoWda6DU5XC8n-zewQFn2tpWKca1QSXSiE7z1WnLvgFkQ2g6mVbvkgMz22jthhGGsc9h6ZTrTD2ofTTnMIcL6PcsaEh5PzCVFqCHOZKx5w_cHOQVHEQ:1su3sZ:wzxOJcXVmhtUlqkd3b_haf51RAuqyurVxZNWvVAzlc8','2024-10-11 05:50:59.594884'),('ot521qcvhr0w81iu3za1b5dgdmyeb5bn','.eJxVjEEOwiAQRe_C2hBwQKhL9z0DGYZBqgaS0q6Md7dNutDtf-_9twi4LiWsnecwJXEVWpx-t4j05LqD9MB6b5JaXeYpyl2RB-1ybIlft8P9OyjYy1Y7RRRJGWJD0XIC49mDy5Gcp2wVsEazgQHxbEFlZTUosibD4PiCXny-B_k4Vw:1sraLo:GHAx_yEvo5CET2SvmNkNpmw7CNXfkt-X8RYdESbn7dk','2024-10-04 09:54:56.906536'),('sbeo4wp586jgp3f4k20k7w7k2cy7ty7o','.eJxVjEEOwiAQRe_C2hBwQKhL9z0DGYZBqgaS0q6Md7dNutDtf-_9twi4LiWsnecwJXEVWpx-t4j05LqD9MB6b5JaXeYpyl2RB-1ybIlft8P9OyjYy1Y7RRRJGWJD0XIC49mDy5Gcp2wVsEazgQHxbEFlZTUosibD4PiCXny-B_k4Vw:1t2PHX:_Al7KrxZL2wwzD9Tvt5_OvDZc2Dqd2Ps7cdt1w7PJaU','2024-11-03 06:19:15.738563');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `userprofile_profile`
--

DROP TABLE IF EXISTS `userprofile_profile`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `userprofile_profile` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `sex` varchar(2) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `dob` date DEFAULT NULL,
  `profile_picture` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `personal_phone` varchar(20) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `work_phone` varchar(20) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `city` varchar(20) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `state` varchar(20) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `address` varchar(250) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `created_by_id` int DEFAULT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_by_id` int DEFAULT NULL,
  `updated_at` datetime(6) NOT NULL,
  `country_id` bigint DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`),
  KEY `userprofile_profile_country_id_bf6a045e_fk_administr` (`country_id`),
  KEY `userprofile_profile_created_by_id_986ae0e2` (`created_by_id`),
  KEY `userprofile_profile_updated_by_id_afaf0bc7` (`updated_by_id`),
  CONSTRAINT `userprofile_profile_country_id_bf6a045e_fk_administr` FOREIGN KEY (`country_id`) REFERENCES `administrator_country` (`id`),
  CONSTRAINT `userprofile_profile_created_by_id_986ae0e2_fk_auth_user_id` FOREIGN KEY (`created_by_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `userprofile_profile_updated_by_id_afaf0bc7_fk_auth_user_id` FOREIGN KEY (`updated_by_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `userprofile_profile_user_id_f37c6bb1_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `userprofile_profile`
--

LOCK TABLES `userprofile_profile` WRITE;
/*!40000 ALTER TABLE `userprofile_profile` DISABLE KEYS */;
INSERT INTO `userprofile_profile` VALUES (1,'M','2024-09-24','users/profile_picture/justin-schwartfigure-LVwbWJyOJro-unsplash_PYIlmWo.jpg',NULL,NULL,NULL,NULL,NULL,1,'2024-09-24 10:56:02.853424',1,'2024-09-24 10:56:17.969369',2,1);
/*!40000 ALTER TABLE `userprofile_profile` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-10-20 12:19:28
