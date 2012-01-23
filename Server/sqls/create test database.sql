# --------------------------------------------------------
# Host:                         127.0.0.1
# Server version:               5.5.8-log
# Server OS:                    Win32
# HeidiSQL version:             6.0.0.3603
# Date/time:                    2011-12-30 15:32:50
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

# Dumping data for table payambar.clients: ~1 rows (approximately)
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
	(1, 'htc-tatto', '2f1a5ee55fe8435b6aa82782d318f5e2');
/*!40000 ALTER TABLE `mobiles` ENABLE KEYS */;


# Dumping structure for table payambar.transactions
CREATE TABLE IF NOT EXISTS `transactions` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `to` varchar(20) NOT NULL,
  `text` varchar(1000) NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `delivered_at` timestamp NULL DEFAULT NULL,
  `sent_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=50 DEFAULT CHARSET=utf8;

# Dumping data for table payambar.transactions: ~27 rows (approximately)
/*!40000 ALTER TABLE `transactions` DISABLE KEYS */;
REPLACE INTO `transactions` (`id`, `to`, `text`, `created_at`, `delivered_at`, `sent_at`) VALUES
	(1, '09128216439', 'سلام یاسر خان. امیدوارم منبر را دوست داشته باشید.', '2011-12-29 18:17:43', '2011-12-29 18:17:42', NULL),
	(2, '09376970224', 'سلام علیرضا خان. حال شما خوب است؟', '2011-12-29 18:17:44', '2011-12-29 18:17:43', NULL),
	(3, '09128216439', 'hello!!!!/nHow are you?', '2011-12-29 18:19:51', '2011-12-29 18:19:50', '2011-12-29 18:19:51'),
	(4, '09128216439', 'سلام یاسر خان. امیدوارم منبر را دوست داشته باشید.', '2011-12-29 18:17:48', '2011-12-29 18:17:48', NULL),
	(5, '09128216439', 'hello!!!!/nHow are you?', '2011-12-29 18:17:50', '2011-12-29 18:17:49', NULL),
	(6, '09376970224', 'سلام علیرضا خان. حال شما خوب است؟', '2011-12-29 18:17:56', '2011-12-29 18:17:55', NULL),
	(7, '09128216439', 'سلام یاسر خان. امیدوارم منبر را دوست داشته باشید.', '2011-12-29 18:17:58', '2011-12-29 18:17:57', NULL),
	(8, '09128216439', 'سلام یاسر خان. امیدوارم منبر را دوست داشته باشید.', '2011-12-29 18:18:01', '2011-12-29 18:18:01', NULL),
	(9, '09128216439', 'سلام یاسر خان. امیدوارم منبر را دوست داشته باشید.', '2011-12-29 18:18:03', '2011-12-29 18:18:02', NULL),
	(10, '09376970224', 'alir431@nourNIA.ir/com@github.com', '2011-12-29 18:43:42', '2011-12-29 18:43:41', '2011-12-29 18:43:42'),
	(11, '09376970224', 'سلام علیرضا خان. حال شما خوب است؟', '2011-12-29 18:39:36', '2011-12-29 18:39:36', '2011-12-29 18:39:36'),
	(12, '09376970224', 'سلام علیرضا خان. حال شما خوب است؟', '2011-12-29 19:46:49', '2011-12-29 19:46:48', '2011-12-29 19:46:49'),
	(13, '09128216439', 'hello!!!!/nHow are you?', '2011-12-29 19:05:55', '2011-12-29 19:05:55', '2011-12-29 19:05:55'),
	(14, '09128216439', 'hello!!!!/nHow are you?', '2011-12-29 18:43:42', '2011-12-29 18:43:41', '2011-12-29 18:43:42'),
	(15, '09128216439', 'hello!!!!/nHow are you?', '2011-12-29 18:39:36', '2011-12-29 18:39:36', '2011-12-29 18:39:36'),
	(36, '+989128216439', 'سلام.\nبرای ارسال س م س به گروه تفسیر قرآن مثل زیر عمل کنید:\nsent to all\ntafsir\nدر این محل متن مورد نظری را که برای همه فرستاده می‌شود را بفرستید.', '2011-12-29 18:50:20', '2011-12-29 18:50:19', '2011-12-29 18:50:20'),
	(37, '+989128216439', 'sent to all\ntafsir', '2011-12-29 19:02:27', '2011-12-29 19:02:25', '2011-12-29 19:02:27'),
	(38, '+989128216439', 'sent to all\nسلام', '2011-12-29 19:05:05', '2011-12-29 19:05:05', '2011-12-29 19:05:05'),
	(40, '+989128216439', 'sent to all\nسلام', '2011-12-29 19:06:20', '2011-12-29 19:06:20', '2011-12-29 19:06:20'),
	(41, '+989128216439', 'sent to all\nسلام', '2011-12-29 19:06:30', '2011-12-29 19:06:30', '2011-12-29 19:06:30'),
	(42, '+989128216439', 'sent to all\ntafsir\nmatn', '2011-12-29 19:24:37', '2011-12-29 19:24:36', '2011-12-29 19:24:37'),
	(44, '+989128216439', 'sent to all\ntafsir\nmatn', '2011-12-29 19:37:56', '2011-12-29 19:37:55', '2011-12-29 19:37:56'),
	(45, '+989128216439', 'sent to all\ntafsir\nmatn', '2011-12-29 19:41:21', '2011-12-29 19:41:21', '2011-12-29 19:41:21'),
	(46, '9376970224', 'لا حول و لا قوة الا بالله', '2011-12-29 19:42:50', '2011-12-29 19:42:50', '2011-12-29 19:42:50'),
	(47, '9128216439', 'لا حول و لا قوة الا بالله', '2011-12-29 19:42:50', '2011-12-29 19:42:50', '2011-12-29 19:42:50'),
	(48, '9376970224', 'لا حول و لا قوة الا بالله', '2011-12-29 19:44:32', '2011-12-29 19:44:30', '2011-12-29 19:44:32'),
	(49, '9128216439', 'لا حول و لا قوة الا بالله', '2011-12-29 19:44:32', '2011-12-29 19:44:30', '2011-12-29 19:44:32');
/*!40000 ALTER TABLE `transactions` ENABLE KEYS */;
/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
