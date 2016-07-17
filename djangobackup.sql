-- MySQL dump 10.13  Distrib 5.6.19, for Win64 (x86_64)
--
-- Host: localhost    Database: midas
-- ------------------------------------------------------
-- Server version	5.6.19

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `assignments`
--

DROP TABLE IF EXISTS `assignments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `assignments` (
  `challanid` int(10) NOT NULL DEFAULT '0',
  `process` varchar(10) NOT NULL,
  `karigar` varchar(20) NOT NULL,
  `product` varchar(100) NOT NULL,
  `qty` int(10) NOT NULL DEFAULT '0',
  `assignmentdate` date NOT NULL,
  `assignment_id` int(10) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`assignment_id`),
  KEY `karigar` (`karigar`),
  KEY `product` (`product`),
  CONSTRAINT `assignments_ibfk_1` FOREIGN KEY (`karigar`) REFERENCES `karigars` (`name`),
  CONSTRAINT `assignments_ibfk_2` FOREIGN KEY (`product`) REFERENCES `products` (`prodid`)
) ENGINE=InnoDB AUTO_INCREMENT=63 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `assignments`
--

LOCK TABLES `assignments` WRITE;
/*!40000 ALTER TABLE `assignments` DISABLE KEYS */;
INSERT INTO `assignments` VALUES (2,'issue','Swati','PROD1',60,'2016-06-16',1),(1,'issue','Rohit','PROD1',30,'2016-06-16',2),(1,'issue','Rohit','PROD2',40,'2016-06-16',3),(3,'receive','Swati','PROD1',40,'2016-06-28',4),(3,'issue','Swati','PROD2',70,'2016-06-28',5),(4,'issue','Saba','PROD2',30,'2016-06-17',6),(4,'issue','Saba','PROD1',100,'2016-06-17',7),(8,'issue','Vinay','PROD2',67,'2016-06-18',9),(10,'receive','Geeta','PROD1',20,'2016-06-26',10),(11,'issue','Rohit','PROD2',90,'2016-06-27',13),(12,'issue','Swati','PROD3',50,'2016-07-03',14),(14,'issue','Vinay','PROD3',50,'2016-07-01',15),(14,'issue','Vinay','PROD4',60,'2016-07-01',16),(17,'receive','Swati','PROD1',10,'2016-07-04',19),(20,'issue','Swati','PROD1',100,'2016-07-07',20),(21,'receive','Swati','PROD1',15,'2016-07-08',21),(22,'receive','Swati','PROD1',10,'2016-07-09',22),(23,'receive','Swati','PROD1',10,'2016-07-09',23),(25,'receive','Swati','PROD1',10,'2016-07-11',24),(26,'receive','Swati','PROD1',10,'2016-07-12',25),(27,'receive','Swati','PROD1',10,'2016-07-13',26),(28,'receive','Swati','PROD1',10,'2016-07-14',27),(29,'receive','Swati','PROD1',10,'2016-07-15',28),(29,'receive','Swati','PROD2',10,'2016-07-15',29),(30,'receive','Swati','PROD1',5,'2016-07-16',30),(1234,'issue','Swati','PROD3',100,'2016-07-07',31),(1234,'issue','Swati','PROD4',100,'2016-07-07',32),(1235,'receive','Swati','PROD3',50,'2016-07-07',34),(1235,'receive','Swati','PROD4',25,'2016-07-07',35),(1245,'reissue','Swati','PROD1',10,'2016-07-07',37),(1256,'reissue','Swati','PROD1',15,'2016-07-08',38),(30,'issue','Vinay','MID-PINK',50,'2016-07-10',39),(31,'issue','Saba','MID-PINK',100,'2016-07-10',40),(34,'issue','Geeta','PROD4',40,'2016-07-10',41),(42,'issue','Saba','MID-PINK',30,'2016-07-10',44),(43,'receive','Vinay','PROD1',20,'2016-07-10',45),(453,'issue','Madhu','PROD1',100,'2016-07-11',47),(234,'issue','Madhu','MID-PINK',20,'2016-07-11',48),(235,'issue','Madhu','PROD2',40,'2016-07-11',49),(567,'issue','Swati','MID-PINK',100,'2016-07-11',50),(378,'reissue','Vinay','PROD1',20,'2016-07-11',52),(789,'issue','Vinay','MID-417',100,'2016-07-11',53),(789,'issue','Vinay','MID-PINK',10,'2016-07-11',54),(7889,'issue','Aditi','PROD1',100,'2016-06-30',55),(555,'receive','Vinay','PROD1',20,'2016-07-11',57),(100,'receive','Madhu','MID-PINK',20,'2016-07-11',58),(111,'receive','Saba','MID-PINK',70,'2016-07-09',59),(113,'receive','Swati','MID-PINK',75,'2016-07-07',60),(156,'receive','Vinay','MID-PINK',40,'2016-07-11',61),(765,'receive','Rohit','MID-PINK',30,'2016-07-09',62);
/*!40000 ALTER TABLE `assignments` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
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
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissi_permission_id_84c5c92e_fk_auth_permission_id` (`permission_id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_group_permissi_permission_id_84c5c92e_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
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
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permissi_content_type_id_2f476e4b_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=43 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can add permission',2,'add_permission'),(5,'Can change permission',2,'change_permission'),(6,'Can delete permission',2,'delete_permission'),(7,'Can add group',3,'add_group'),(8,'Can change group',3,'change_group'),(9,'Can delete group',3,'delete_group'),(10,'Can add user',4,'add_user'),(11,'Can change user',4,'change_user'),(12,'Can delete user',4,'delete_user'),(13,'Can add content type',5,'add_contenttype'),(14,'Can change content type',5,'change_contenttype'),(15,'Can delete content type',5,'delete_contenttype'),(16,'Can add session',6,'add_session'),(17,'Can change session',6,'change_session'),(18,'Can delete session',6,'delete_session'),(31,'Can add assignment',11,'add_assignment'),(32,'Can change assignment',11,'change_assignment'),(33,'Can delete assignment',11,'delete_assignment'),(34,'Can add bill',12,'add_bill'),(35,'Can change bill',12,'change_bill'),(36,'Can delete bill',12,'delete_bill'),(37,'Can add karigar',13,'add_karigar'),(38,'Can change karigar',13,'change_karigar'),(39,'Can delete karigar',13,'delete_karigar'),(40,'Can add product',14,'add_product'),(41,'Can change product',14,'change_product'),(42,'Can delete product',14,'delete_product');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(30) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$24000$6h9jnAitZ9kU$tBMCpXhCtAnvjk5BhjRZQ4tcEOR3u/X1YsIzXXu6nIQ=','2016-07-14 11:42:51',1,'swati','','','swati.lmgclko@gmail.com',1,1,'2016-06-22 19:50:34'),(2,'pbkdf2_sha256$24000$Yng7Dpu6cEKd$tvOjcsa/J6trW8rIRH0XvOPvDu63DcUzRZ2VN+IZEDQ=','2016-07-14 11:41:12',1,'anurag','Anuarg','Agarwal','anuraglko.imt@gmail.com',1,1,'2016-07-13 07:46:12'),(3,'pbkdf2_sha256$24000$goEiq8jCqlSh$4O2dGb7XMinL21ZhDuw1y13dveDZGaiAnh6g5K/64lM=',NULL,1,'smita','Smita','Agarwal','',1,1,'2016-07-13 07:46:51'),(4,'pbkdf2_sha256$24000$VR1OYBaIYVP0$wdcXPF4zEYB4hRF2HYW9lUiKk0VRFbBmiFt4goXyxXM=','2016-07-13 11:20:13',0,'neha','Neha','','',0,1,'2016-07-13 10:39:45');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
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
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_perm_permission_id_1fbb5f2c_fk_auth_permission_id` (`permission_id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `auth_user_user_perm_permission_id_1fbb5f2c_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=73 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
INSERT INTO `auth_user_user_permissions` VALUES (31,2,1),(32,2,2),(33,2,3),(34,2,4),(35,2,5),(36,2,6),(37,2,7),(38,2,8),(39,2,9),(40,2,10),(41,2,11),(42,2,12),(43,2,13),(44,2,14),(45,2,15),(46,2,16),(47,2,17),(48,2,18),(49,2,31),(50,2,32),(51,2,33),(52,2,34),(53,2,35),(54,2,36),(55,2,37),(56,2,38),(57,2,39),(58,2,40),(59,2,41),(60,2,42),(1,3,1),(2,3,2),(3,3,3),(4,3,4),(5,3,5),(6,3,6),(7,3,7),(8,3,8),(9,3,9),(10,3,10),(11,3,11),(12,3,12),(13,3,13),(14,3,14),(15,3,15),(16,3,16),(17,3,17),(18,3,18),(19,3,31),(20,3,32),(21,3,33),(22,3,34),(23,3,35),(24,3,36),(25,3,37),(26,3,38),(27,3,39),(28,3,40),(29,3,41),(30,3,42),(72,4,31),(61,4,32),(62,4,33),(63,4,34),(64,4,35),(65,4,36),(66,4,37),(67,4,38),(68,4,39),(69,4,40),(70,4,41),(71,4,42);
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bills`
--

DROP TABLE IF EXISTS `bills`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `bills` (
  `billingid` int(10) NOT NULL,
  `karigar` varchar(20) DEFAULT NULL,
  `billingdate` date DEFAULT NULL,
  `amountpaid` int(10) DEFAULT NULL,
  PRIMARY KEY (`billingid`),
  KEY `karigar` (`karigar`),
  CONSTRAINT `bills_ibfk_1` FOREIGN KEY (`karigar`) REFERENCES `karigars` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bills`
--

LOCK TABLES `bills` WRITE;
/*!40000 ALTER TABLE `bills` DISABLE KEYS */;
/*!40000 ALTER TABLE `bills` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin__content_type_id_c4bce8eb_fk_django_content_type_id` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin__content_type_id_c4bce8eb_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2016-06-28 09:49:40','Swati','Swati',2,'Changed profile.',13,1),(2,'2016-06-29 15:02:37','PROD2','PROD2',1,'Added.',14,1),(3,'2016-07-09 15:28:58','MID-PINK','MID-PINK',3,'',14,1),(4,'2016-07-13 07:46:12','2','anurag',1,'Added.',4,1),(5,'2016-07-13 07:46:51','3','smita',1,'Added.',4,1),(6,'2016-07-13 07:48:02','3','smita',2,'Changed first_name, last_name, is_staff, is_superuser and user_permissions.',4,1),(7,'2016-07-13 07:48:35','2','anurag',2,'Changed first_name, last_name, email, is_staff, is_superuser and user_permissions.',4,1),(8,'2016-07-13 10:39:45','4','neha',1,'Added.',4,2),(9,'2016-07-13 10:41:26','4','neha',2,'Changed first_name and user_permissions.',4,2),(10,'2016-07-14 13:39:37','FAB-PINK','FAB-PINK',3,'',14,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(11,'AnIndianStory','assignment'),(12,'AnIndianStory','bill'),(13,'AnIndianStory','karigar'),(14,'AnIndianStory','product'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(6,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'AnIndianStory','0001_initial','2016-06-22 19:45:37'),(2,'contenttypes','0001_initial','2016-06-22 19:45:38'),(3,'auth','0001_initial','2016-06-22 19:45:46'),(4,'admin','0001_initial','2016-06-22 19:45:47'),(5,'admin','0002_logentry_remove_auto_add','2016-06-22 19:45:47'),(6,'contenttypes','0002_remove_content_type_name','2016-06-22 19:45:49'),(7,'auth','0002_alter_permission_name_max_length','2016-06-22 19:45:49'),(8,'auth','0003_alter_user_email_max_length','2016-06-22 19:45:50'),(9,'auth','0004_alter_user_username_opts','2016-06-22 19:45:50'),(10,'auth','0005_alter_user_last_login_null','2016-06-22 19:45:51'),(11,'auth','0006_require_contenttypes_0002','2016-06-22 19:45:51'),(12,'auth','0007_alter_validators_add_error_messages','2016-06-22 19:45:51'),(13,'sessions','0001_initial','2016-06-22 19:45:51'),(14,'AnIndianStory','0002_auto_20160627_1749','2016-06-27 12:20:01'),(15,'AnIndianStory','0003_assignment_bill_karigar_product','2016-06-28 09:44:35');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_de54fa62` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('036t4boys6f44tpfoh7boup73f5l1gs2','YTA3ZmQ3NGIwODVjYzhjYjhhY2EwMTFjN2Y3YThiYzE2ZmIzYmRkOTp7Il9hdXRoX3VzZXJfaGFzaCI6IjVkYmU2OTExNDk1ODgyMmMwNzlkMDhlNTUxNzU1OGZiNWRmOGI0YjQiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=','2016-07-28 11:42:51'),('ikrn3zs3hsqku8sfjrbyowaklecusg6x','YTA3ZmQ3NGIwODVjYzhjYjhhY2EwMTFjN2Y3YThiYzE2ZmIzYmRkOTp7Il9hdXRoX3VzZXJfaGFzaCI6IjVkYmU2OTExNDk1ODgyMmMwNzlkMDhlNTUxNzU1OGZiNWRmOGI0YjQiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=','2016-07-06 19:50:41');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `karigars`
--

DROP TABLE IF EXISTS `karigars`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `karigars` (
  `name` varchar(20) NOT NULL DEFAULT '',
  `profile` varchar(20) NOT NULL,
  `phone` varchar(13) DEFAULT NULL,
  `photo` varchar(255) DEFAULT NULL,
  `address` varchar(255) DEFAULT NULL,
  `pan` varchar(11) DEFAULT NULL,
  PRIMARY KEY (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `karigars`
--

LOCK TABLES `karigars` WRITE;
/*!40000 ALTER TABLE `karigars` DISABLE KEYS */;
INSERT INTO `karigars` VALUES ('Aditi','block','9044169052','karigars/IMG_20150713_131053.jpg','Home',''),('Geeta','stitch','8130044567','karigars/_20151205_232540.JPG','',''),('Madhu','addon','','','Chowk',''),('Rohit','wash','9839014100','','',''),('Saba','stitch','8154638048','karigars/propic.jpg','',''),('Swati','block','7658749374','karigars/IMG_20150805_222548.jpg','188, Eldeco Greens, Gomti Nagar, Lucknow',''),('Vinay','emb','8130022768','','','');
/*!40000 ALTER TABLE `karigars` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `products`
--

DROP TABLE IF EXISTS `products`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `products` (
  `prodid` varchar(100) NOT NULL DEFAULT '',
  `colour` varchar(100) DEFAULT NULL,
  `fabric` varchar(100) DEFAULT NULL,
  `photo` varchar(255) DEFAULT NULL,
  `cost_stitch` int(10) DEFAULT '0',
  `cost_block` int(10) DEFAULT '0',
  `cost_emb` int(10) DEFAULT '0',
  `cost_wash` int(10) DEFAULT '0',
  `cost_addon` int(10) DEFAULT '0',
  PRIMARY KEY (`prodid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `products`
--

LOCK TABLES `products` WRITE;
/*!40000 ALTER TABLE `products` DISABLE KEYS */;
INSERT INTO `products` VALUES ('MID-417','teal','silk','products/_20150814_193836.JPG',80,10,110,30,10),('MID-PINK','pink','cotton','',2,2,2,2,2),('PROD1','white','cotton','',4,5,3,3,3),('PROD2','yellow','camric','',4,5,5,5,5),('PROD3','pink','cotton','products/kurti.jpg',4,5,3,5,3),('PROD4','beige','cotton','products/jacket.jpg',3,4,4,4,4);
/*!40000 ALTER TABLE `products` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2016-07-15 19:23:05
