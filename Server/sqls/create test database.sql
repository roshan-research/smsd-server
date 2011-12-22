# --------------------------------------------------------
# Host:                         127.0.0.1
# Server version:               5.5.8-log
# Server OS:                    Win32
# HeidiSQL version:             6.0.0.3603
# Date/time:                    2011-12-21 17:37:22
# --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

# Dumping database structure for payambar
CREATE DATABASE IF NOT EXISTS `payambar` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `payambar`;


# Dumping structure for table payambar.clients
CREATE TABLE IF NOT EXISTS `clients` (
  `id` int(10) unsigned NOT NULL,
  `name` varchar(50) DEFAULT NULL,
  `key` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

# Dumping data for table payambar.clients: ~0 rows (approximately)
/*!40000 ALTER TABLE `clients` DISABLE KEYS */;
REPLACE INTO `clients` (`id`, `name`, `key`) VALUES
	(1, 'emenbar.ir', '3feb37410508bb51a60bcad7cf227e75');
/*!40000 ALTER TABLE `clients` ENABLE KEYS */;


# Dumping structure for table payambar.mobiles
CREATE TABLE IF NOT EXISTS `mobiles` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(50) DEFAULT NULL,
  `key` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

# Dumping data for table payambar.mobiles: ~1 rows (approximately)
/*!40000 ALTER TABLE `mobiles` DISABLE KEYS */;
REPLACE INTO `mobiles` (`id`, `name`, `key`) VALUES
	(1, 'htc-tatto', '039c86abf0a5d67205d40d756eb0c9c5');
/*!40000 ALTER TABLE `mobiles` ENABLE KEYS */;


# Dumping structure for table payambar.transactions
CREATE TABLE IF NOT EXISTS `transactions` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `to` varchar(20) NOT NULL,
  `text` varchar(1000) NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `sent_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

# Dumping data for table payambar.transactions: ~3 rows (approximately)
/*!40000 ALTER TABLE `transactions` DISABLE KEYS */;
REPLACE INTO `transactions` (`id`, `to`, `text`, `created_at`, `sent_at`) VALUES
	(1, '09128216439', 'سلام یاسر خان. امیدوارم منبر را دوست داشته باشید.', '2011-12-21 17:04:24', NULL),
	(2, '09376970224', 'سلام علیرضا خان. حال شما خوب است؟', '2011-12-21 17:05:15', NULL),
	(3, '09128216439', 'hello!!!!/nHow are you?', '2011-12-21 17:06:29', NULL);
/*!40000 ALTER TABLE `transactions` ENABLE KEYS */;
/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;