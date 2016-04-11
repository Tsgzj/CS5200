-- MySQL dump 10.13  Distrib 5.5.46, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: ecom
-- ------------------------------------------------------
-- Server version	5.5.46-0ubuntu0.14.04.2

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
-- Table structure for table `Address`
--

DROP TABLE IF EXISTS `Address`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Address` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `cust_id` int(11) NOT NULL,
  `street` varchar(20) NOT NULL,
  `city` varchar(20) NOT NULL,
  `state` enum('MA','NY','FL') NOT NULL,
  `zip` int(5) NOT NULL,
  `type` enum('shipping','billing') NOT NULL,
  PRIMARY KEY (`id`),
  KEY `cust_id` (`cust_id`),
  CONSTRAINT `Address_ibfk_1` FOREIGN KEY (`cust_id`) REFERENCES `Customer` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Address`
--

LOCK TABLES `Address` WRITE;
/*!40000 ALTER TABLE `Address` DISABLE KEYS */;
INSERT INTO `Address` VALUES (1,1,'100 huntington','Boston','MA',2165,'billing'),(2,1,'100 huntington','Boston','MA',2165,'shipping'),(3,2,'50 main','Boston','MA',2165,'shipping');
/*!40000 ALTER TABLE `Address` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Card`
--

DROP TABLE IF EXISTS `Card`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Card` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `custid` int(11) NOT NULL,
  `cardnumber` varchar(16) NOT NULL,
  `address` varchar(50) NOT NULL,
  `expirationdate` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `type` enum('visa','master','americanexpress') DEFAULT NULL,
  PRIMARY KEY (`id`,`custid`),
  UNIQUE KEY `cardnumber` (`cardnumber`),
  KEY `custid` (`custid`),
  CONSTRAINT `Card_ibfk_1` FOREIGN KEY (`custid`) REFERENCES `Customer` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Card`
--

LOCK TABLES `Card` WRITE;
/*!40000 ALTER TABLE `Card` DISABLE KEYS */;
INSERT INTO `Card` VALUES (3,1,'0123456987452','18hyde park','2016-04-11 04:00:00','master'),(4,1,'123456789015','0','2016-04-11 15:18:27','visa'),(5,2,'123456589015','0','2016-04-11 15:18:27','master'),(6,1,'123456777715','0','2016-04-11 15:18:27','visa'),(7,1,'128856777715','0','2016-04-11 15:18:27','visa'),(8,3,'123400789012','0','2016-04-11 15:18:27','visa'),(11,1,'123456789012','0','2016-04-11 15:18:27','master');
/*!40000 ALTER TABLE `Card` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `CartOrder`
--

DROP TABLE IF EXISTS `CartOrder`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `CartOrder` (
  `id` int(11) NOT NULL,
  `status` enum('pending','confirmed','shipped','delivered') NOT NULL,
  `shipsto` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `CartOrder_ibfk_2` (`shipsto`),
  CONSTRAINT `CartOrder_ibfk_1` FOREIGN KEY (`id`) REFERENCES `ShoppingCart` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `CartOrder_ibfk_2` FOREIGN KEY (`shipsto`) REFERENCES `Address` (`id`) ON DELETE SET NULL ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `CartOrder`
--

LOCK TABLES `CartOrder` WRITE;
/*!40000 ALTER TABLE `CartOrder` DISABLE KEYS */;
INSERT INTO `CartOrder` VALUES (1,'confirmed',1);
/*!40000 ALTER TABLE `CartOrder` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Customer`
--

DROP TABLE IF EXISTS `Customer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Customer` (
  `id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `Customer_ibfk_1` FOREIGN KEY (`id`) REFERENCES `User` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Customer`
--

LOCK TABLES `Customer` WRITE;
/*!40000 ALTER TABLE `Customer` DISABLE KEYS */;
INSERT INTO `Customer` VALUES (1),(2),(3);
/*!40000 ALTER TABLE `Customer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `CustomerContact`
--

DROP TABLE IF EXISTS `CustomerContact`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `CustomerContact` (
  `custid` int(11) NOT NULL,
  `contact` varchar(10) NOT NULL,
  PRIMARY KEY (`custid`,`contact`),
  CONSTRAINT `CustomerContact_ibfk_1` FOREIGN KEY (`custid`) REFERENCES `Customer` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `CustomerContact`
--

LOCK TABLES `CustomerContact` WRITE;
/*!40000 ALTER TABLE `CustomerContact` DISABLE KEYS */;
INSERT INTO `CustomerContact` VALUES (1,'1248625974'),(1,'1548625974'),(1,'5684521569'),(1,'8945621378'),(2,'8248625974');
/*!40000 ALTER TABLE `CustomerContact` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Delivery`
--

DROP TABLE IF EXISTS `Delivery`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Delivery` (
  `id` int(11) NOT NULL,
  `carrier` enum('ups','usps','fedex') NOT NULL,
  `est_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  CONSTRAINT `Delivery_ibfk_1` FOREIGN KEY (`id`) REFERENCES `CartOrder` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Delivery`
--

LOCK TABLES `Delivery` WRITE;
/*!40000 ALTER TABLE `Delivery` DISABLE KEYS */;
INSERT INTO `Delivery` VALUES (1,'ups','2016-05-21 04:00:00');
/*!40000 ALTER TABLE `Delivery` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `DeliveryManager`
--

DROP TABLE IF EXISTS `DeliveryManager`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `DeliveryManager` (
  `id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `DeliveryManager_ibfk_1` FOREIGN KEY (`id`) REFERENCES `User` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `DeliveryManager`
--

LOCK TABLES `DeliveryManager` WRITE;
/*!40000 ALTER TABLE `DeliveryManager` DISABLE KEYS */;
/*!40000 ALTER TABLE `DeliveryManager` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Inventory`
--

DROP TABLE IF EXISTS `Inventory`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Inventory` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `managedby` int(11) DEFAULT NULL,
  `title` varchar(30) NOT NULL,
  `description` varchar(150) DEFAULT NULL,
  `price` double NOT NULL,
  `discount` double DEFAULT NULL,
  `category` enum('fashion','electronics','home') NOT NULL,
  `available` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `managedby` (`managedby`),
  CONSTRAINT `Inventory_ibfk_1` FOREIGN KEY (`managedby`) REFERENCES `InventoryManager` (`id`) ON DELETE SET NULL ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Inventory`
--

LOCK TABLES `Inventory` WRITE;
/*!40000 ALTER TABLE `Inventory` DISABLE KEYS */;
INSERT INTO `Inventory` VALUES (1,4,'keyboard','it hase buttons',45.35,3.2,'electronics',52),(2,4,'mouse','it has 2 buttons',20.35,1.5,'electronics',100),(7,4,'monitor','to see things',200,1,'electronics',15);
/*!40000 ALTER TABLE `Inventory` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `InventoryManager`
--

DROP TABLE IF EXISTS `InventoryManager`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `InventoryManager` (
  `id` int(11) NOT NULL,
  `Position` enum('fashion','electronics','home') NOT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `InventoryManager_ibfk_1` FOREIGN KEY (`id`) REFERENCES `User` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `InventoryManager`
--

LOCK TABLES `InventoryManager` WRITE;
/*!40000 ALTER TABLE `InventoryManager` DISABLE KEYS */;
INSERT INTO `InventoryManager` VALUES (3,'fashion'),(4,'electronics');
/*!40000 ALTER TABLE `InventoryManager` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Item`
--

DROP TABLE IF EXISTS `Item`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Item` (
  `quantity` int(11) NOT NULL,
  `inv_id` int(11) NOT NULL DEFAULT '0',
  `shopcart_id` int(11) NOT NULL,
  PRIMARY KEY (`inv_id`,`shopcart_id`),
  KEY `shopcart_id` (`shopcart_id`),
  CONSTRAINT `Item_ibfk_1` FOREIGN KEY (`inv_id`) REFERENCES `Inventory` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `Item_ibfk_2` FOREIGN KEY (`shopcart_id`) REFERENCES `ShoppingCart` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Item`
--

LOCK TABLES `Item` WRITE;
/*!40000 ALTER TABLE `Item` DISABLE KEYS */;
INSERT INTO `Item` VALUES (5,1,1),(10,2,1),(10,2,2);
/*!40000 ALTER TABLE `Item` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Payment`
--

DROP TABLE IF EXISTS `Payment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Payment` (
  `cust_id` int(11) NOT NULL,
  `order_id` int(11) NOT NULL,
  `paidwith` int(11) NOT NULL,
  `transaction_number` int(11) NOT NULL AUTO_INCREMENT,
  UNIQUE KEY `transaction_number` (`transaction_number`),
  KEY `cust_id` (`cust_id`),
  KEY `order_id` (`order_id`),
  KEY `paidwith` (`paidwith`),
  CONSTRAINT `Payment_ibfk_1` FOREIGN KEY (`cust_id`) REFERENCES `Customer` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `Payment_ibfk_2` FOREIGN KEY (`order_id`) REFERENCES `CartOrder` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `Payment_ibfk_3` FOREIGN KEY (`paidwith`) REFERENCES `Card` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Payment`
--

LOCK TABLES `Payment` WRITE;
/*!40000 ALTER TABLE `Payment` DISABLE KEYS */;
INSERT INTO `Payment` VALUES (1,1,3,2);
/*!40000 ALTER TABLE `Payment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `PaymentManager`
--

DROP TABLE IF EXISTS `PaymentManager`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `PaymentManager` (
  `id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `PaymentManager_ibfk_1` FOREIGN KEY (`id`) REFERENCES `User` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `PaymentManager`
--

LOCK TABLES `PaymentManager` WRITE;
/*!40000 ALTER TABLE `PaymentManager` DISABLE KEYS */;
/*!40000 ALTER TABLE `PaymentManager` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ShoppingCart`
--

DROP TABLE IF EXISTS `ShoppingCart`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ShoppingCart` (
  `price` double NOT NULL,
  `addedby` int(11) NOT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`),
  KEY `ShoppingCart_ibfk_1` (`addedby`),
  CONSTRAINT `ShoppingCart_ibfk_1` FOREIGN KEY (`addedby`) REFERENCES `Customer` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ShoppingCart`
--

LOCK TABLES `ShoppingCart` WRITE;
/*!40000 ALTER TABLE `ShoppingCart` DISABLE KEYS */;
INSERT INTO `ShoppingCart` VALUES (0,1,1),(188.5,1,2),(0,2,5),(0,3,6);
/*!40000 ALTER TABLE `ShoppingCart` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `User`
--

DROP TABLE IF EXISTS `User`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `User` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(20) NOT NULL,
  `password` varchar(20) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `User`
--

LOCK TABLES `User` WRITE;
/*!40000 ALTER TABLE `User` DISABLE KEYS */;
INSERT INTO `User` VALUES (1,'tanmay','123456'),(2,'Jane','Doe'),(3,'hbd','lol'),(4,'joe','123dsfr');
/*!40000 ALTER TABLE `User` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2016-04-11 18:30:42
