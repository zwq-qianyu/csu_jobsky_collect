/*
 Navicat Premium Data Transfer

 Source Server         : mysql
 Source Server Type    : MySQL
 Source Server Version : 80012
 Source Host           : localhost:3306
 Source Schema         : csu_jobsky_collect

 Target Server Type    : MySQL
 Target Server Version : 80012
 File Encoding         : 65001

 Date: 04/10/2018 17:52:07
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for auth_group
-- ----------------------------
DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for auth_group_permissions
-- ----------------------------
DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for auth_permission
-- ----------------------------
DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_permission
-- ----------------------------
BEGIN;
INSERT INTO `auth_permission` VALUES (1, 'Can add log entry', 1, 'add_logentry');
INSERT INTO `auth_permission` VALUES (2, 'Can change log entry', 1, 'change_logentry');
INSERT INTO `auth_permission` VALUES (3, 'Can delete log entry', 1, 'delete_logentry');
INSERT INTO `auth_permission` VALUES (4, 'Can add permission', 2, 'add_permission');
INSERT INTO `auth_permission` VALUES (5, 'Can change permission', 2, 'change_permission');
INSERT INTO `auth_permission` VALUES (6, 'Can delete permission', 2, 'delete_permission');
INSERT INTO `auth_permission` VALUES (7, 'Can add group', 3, 'add_group');
INSERT INTO `auth_permission` VALUES (8, 'Can change group', 3, 'change_group');
INSERT INTO `auth_permission` VALUES (9, 'Can delete group', 3, 'delete_group');
INSERT INTO `auth_permission` VALUES (10, 'Can add user', 4, 'add_user');
INSERT INTO `auth_permission` VALUES (11, 'Can change user', 4, 'change_user');
INSERT INTO `auth_permission` VALUES (12, 'Can delete user', 4, 'delete_user');
INSERT INTO `auth_permission` VALUES (13, 'Can add content type', 5, 'add_contenttype');
INSERT INTO `auth_permission` VALUES (14, 'Can change content type', 5, 'change_contenttype');
INSERT INTO `auth_permission` VALUES (15, 'Can delete content type', 5, 'delete_contenttype');
INSERT INTO `auth_permission` VALUES (16, 'Can add session', 6, 'add_session');
INSERT INTO `auth_permission` VALUES (17, 'Can change session', 6, 'change_session');
INSERT INTO `auth_permission` VALUES (18, 'Can delete session', 6, 'delete_session');
INSERT INTO `auth_permission` VALUES (19, 'Can add enterprises', 7, 'add_enterprises');
INSERT INTO `auth_permission` VALUES (20, 'Can change enterprises', 7, 'change_enterprises');
INSERT INTO `auth_permission` VALUES (21, 'Can delete enterprises', 7, 'delete_enterprises');
INSERT INTO `auth_permission` VALUES (22, 'Can add sessions', 8, 'add_sessions');
INSERT INTO `auth_permission` VALUES (23, 'Can change sessions', 8, 'change_sessions');
INSERT INTO `auth_permission` VALUES (24, 'Can delete sessions', 8, 'delete_sessions');
INSERT INTO `auth_permission` VALUES (25, 'Can add students', 9, 'add_students');
INSERT INTO `auth_permission` VALUES (26, 'Can change students', 9, 'change_students');
INSERT INTO `auth_permission` VALUES (27, 'Can delete students', 9, 'delete_students');
INSERT INTO `auth_permission` VALUES (28, 'Can add users', 10, 'add_users');
INSERT INTO `auth_permission` VALUES (29, 'Can change users', 10, 'change_users');
INSERT INTO `auth_permission` VALUES (30, 'Can delete users', 10, 'delete_users');
COMMIT;

-- ----------------------------
-- Table structure for auth_user
-- ----------------------------
DROP TABLE IF EXISTS `auth_user`;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for auth_user_groups
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_groups`;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for auth_user_user_permissions
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_user_permissions`;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for django_admin_log
-- ----------------------------
DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for django_content_type
-- ----------------------------
DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_content_type
-- ----------------------------
BEGIN;
INSERT INTO `django_content_type` VALUES (1, 'admin', 'logentry');
INSERT INTO `django_content_type` VALUES (3, 'auth', 'group');
INSERT INTO `django_content_type` VALUES (2, 'auth', 'permission');
INSERT INTO `django_content_type` VALUES (4, 'auth', 'user');
INSERT INTO `django_content_type` VALUES (7, 'common', 'enterprises');
INSERT INTO `django_content_type` VALUES (8, 'common', 'sessions');
INSERT INTO `django_content_type` VALUES (9, 'common', 'students');
INSERT INTO `django_content_type` VALUES (10, 'common', 'users');
INSERT INTO `django_content_type` VALUES (5, 'contenttypes', 'contenttype');
INSERT INTO `django_content_type` VALUES (6, 'sessions', 'session');
COMMIT;

-- ----------------------------
-- Table structure for django_migrations
-- ----------------------------
DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_migrations
-- ----------------------------
BEGIN;
INSERT INTO `django_migrations` VALUES (1, 'contenttypes', '0001_initial', '2018-10-01 19:04:45.353156');
INSERT INTO `django_migrations` VALUES (2, 'auth', '0001_initial', '2018-10-01 19:04:45.671651');
INSERT INTO `django_migrations` VALUES (3, 'admin', '0001_initial', '2018-10-01 19:04:45.754573');
INSERT INTO `django_migrations` VALUES (4, 'admin', '0002_logentry_remove_auto_add', '2018-10-01 19:04:45.780427');
INSERT INTO `django_migrations` VALUES (5, 'contenttypes', '0002_remove_content_type_name', '2018-10-01 19:04:45.845903');
INSERT INTO `django_migrations` VALUES (6, 'auth', '0002_alter_permission_name_max_length', '2018-10-01 19:04:45.880475');
INSERT INTO `django_migrations` VALUES (7, 'auth', '0003_alter_user_email_max_length', '2018-10-01 19:04:45.926666');
INSERT INTO `django_migrations` VALUES (8, 'auth', '0004_alter_user_username_opts', '2018-10-01 19:04:45.938717');
INSERT INTO `django_migrations` VALUES (9, 'auth', '0005_alter_user_last_login_null', '2018-10-01 19:04:45.974951');
INSERT INTO `django_migrations` VALUES (10, 'auth', '0006_require_contenttypes_0002', '2018-10-01 19:04:45.979327');
INSERT INTO `django_migrations` VALUES (11, 'auth', '0007_alter_validators_add_error_messages', '2018-10-01 19:04:45.990953');
INSERT INTO `django_migrations` VALUES (12, 'auth', '0008_alter_user_username_max_length', '2018-10-01 19:04:46.038500');
INSERT INTO `django_migrations` VALUES (13, 'common', '0001_initial', '2018-10-01 19:04:46.107513');
INSERT INTO `django_migrations` VALUES (14, 'sessions', '0001_initial', '2018-10-01 19:12:42.359506');
INSERT INTO `django_migrations` VALUES (15, 'common', '0002_users_name', '2018-10-02 03:39:35.561170');
INSERT INTO `django_migrations` VALUES (16, 'common', '0003_sessions_uid', '2018-10-02 10:40:24.313522');
INSERT INTO `django_migrations` VALUES (17, 'common', '0004_auto_20181002_1908', '2018-10-02 11:08:30.949232');
INSERT INTO `django_migrations` VALUES (18, 'common', '0005_sessions_qr_imgname', '2018-10-02 11:58:56.054415');
INSERT INTO `django_migrations` VALUES (19, 'common', '0006_auto_20181003_1903', '2018-10-03 11:03:37.725907');
INSERT INTO `django_migrations` VALUES (20, 'common', '0007_auto_20181003_1912', '2018-10-03 11:13:01.829520');
INSERT INTO `django_migrations` VALUES (21, 'common', '0008_students_session_id', '2018-10-03 15:59:25.900552');
COMMIT;

-- ----------------------------
-- Table structure for django_session
-- ----------------------------
DROP TABLE IF EXISTS `django_session`;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_session
-- ----------------------------
BEGIN;
INSERT INTO `django_session` VALUES ('0bevnw63md9p0frxsq4o2748c36jm25l', 'MzExMjE5NWJkZDRmMzNlNjgwYjRlYzY5YWE2NmI1Y2NmZjA3ZGUyZjp7InZlcmlmeWNvZGUiOiI3NDM3Iiwidm9sdW50ZWVycyI6eyJpZCI6NSwic2V4IjoxLCJuYW1lIjoiXHU2ODkzXHU5MDM4XHU1YmI4IiwidXNlcm5hbWUiOiIxNTI0MzYwNjI1MCIsInBhc3N3b3JkIjoiZTEwYWRjMzk0OWJhNTlhYmJlNTZlMDU3ZjIwZjg4M2UiLCJzdHVkZW50X2lkIjoiMTMwMjE2MDEyNSIsInBob25lIjoiMTUyNDM2MDYyNTAiLCJlbWFpbCI6IjEzNDc2MzgwOTFAcXEuY29tIiwic3RhdGUiOjF9fQ==', '2018-10-17 03:11:17.856778');
INSERT INTO `django_session` VALUES ('3y7qjd0hro0umrgt01go830knuqla7l3', 'N2U2MzljYzFhMWZjOGIyMDQxZGUzMGY2MjViNDU1MjUyMDVhNGRmYTp7InZlcmlmeWNvZGUiOiIzMDIyIiwibXlhZG1pbnVzZXIiOnsiaWQiOjMsInNleCI6MSwibmFtZSI6Ilx1OTQ5Zlx1NGYwZFx1NTE2OCIsInVzZXJuYW1lIjoieml5aWNoZW4iLCJwYXNzd29yZCI6ImUxMGFkYzM5NDliYTU5YWJiZTU2ZTA1N2YyMGY4ODNlIiwic3R1ZGVudF9pZCI6IjEzMDIxNjAxMjUiLCJwaG9uZSI6IjE1MjQzNjA2MjUwIiwiZW1haWwiOiIxMzQ3NjM4MDkxQHFxLmNvbSIsInN0YXRlIjowfX0=', '2018-10-16 04:34:09.916774');
INSERT INTO `django_session` VALUES ('9md74vl5jqez648e1qfo2q1nlw5u16c4', 'OWE2ZjcyODM4YjQ5YWI0ZDUxMWM4NDMxMzhhYmUyNTcxYjZlMWE5ZDp7InZlcmlmeWNvZGUiOiI5NjA0IiwibXlhZG1pbnVzZXIiOnsiaWQiOjMsInNleCI6MSwibmFtZSI6Ilx1OTQ5Zlx1NGYwZFx1NTE2OCIsInVzZXJuYW1lIjoieml5aWNoZW4iLCJwYXNzd29yZCI6ImUxMGFkYzM5NDliYTU5YWJiZTU2ZTA1N2YyMGY4ODNlIiwic3R1ZGVudF9pZCI6IjEzMDIxNjAxMjUiLCJwaG9uZSI6IjE1MjQzNjA2MjUwIiwiZW1haWwiOiIxMzQ3NjM4MDkxQHFxLmNvbSIsInN0YXRlIjowfSwidm9sdW50ZWVycyI6eyJpZCI6NSwic2V4IjoxLCJuYW1lIjoiXHU2ODkzXHU5MDM4XHU1YmI4IiwidXNlcm5hbWUiOiIxNTI0MzYwNjI1MCIsInBhc3N3b3JkIjoiZTEwYWRjMzk0OWJhNTlhYmJlNTZlMDU3ZjIwZjg4M2UiLCJzdHVkZW50X2lkIjoiMTMwMjE2MDEyNiIsInBob25lIjoiMTUyNDM2MDYyNTAiLCJlbWFpbCI6IjEzNDc2MzgwOTFAcXEuY29tIiwic3RhdGUiOjF9fQ==', '2018-10-18 03:14:47.383976');
INSERT INTO `django_session` VALUES ('9plhfn0ik81ehzwxtahpsegmkxblki08', 'NGRjMTk3N2Q5YzdjN2NhMjk2Zjc1NGI0MTQyYTE3N2QyZDJjZDc0Nzp7InZlcmlmeWNvZGUiOiIzMjMxIiwidm9sdW50ZWVycyI6eyJpZCI6NSwic2V4IjoxLCJuYW1lIjoiXHU2ODkzXHU5MDM4XHU1YmI4IiwidXNlcm5hbWUiOiIxNTI0MzYwNjI1MCIsInBhc3N3b3JkIjoiZTEwYWRjMzk0OWJhNTlhYmJlNTZlMDU3ZjIwZjg4M2UiLCJzdHVkZW50X2lkIjoiMTMwMjE2MDEyNSIsInBob25lIjoiMTUyNDM2MDYyNTAiLCJlbWFpbCI6IjEzNDc2MzgwOTFAcXEuY29tIiwic3RhdGUiOjF9fQ==', '2018-10-16 15:59:50.976883');
INSERT INTO `django_session` VALUES ('aedkzlk8yhn3md19r0io8m21jjspy4ui', 'ZTA4ZDBjMmNiOGEwYzBhMDY2ZDVjZjRmNjQyN2FlYWNjZmQ4M2M2ZDp7InZlcmlmeWNvZGUiOiI2NDU4IiwiYWRtaW51c2VyIjp7ImlkIjoxLCJzZXgiOjEsIm5hbWUiOiJ6aXlpY2hlbiIsInVzZXJuYW1lIjoiYWRtaW4iLCJwYXNzd29yZCI6IjEyMzQ1NiIsInN0dWRlbnRfaWQiOiIxMzAyMTYwMTI1IiwicGhvbmUiOiIxMzU5NDgxOTk1NiIsImVtYWlsIjoiMTM0NzYzODA5MUBxcS5jb20iLCJzdGF0ZSI6MH0sIm15YWRtaW51c2VyIjp7ImlkIjoxLCJzZXgiOjEsIm5hbWUiOiJ6aXlpY2hlbiIsInVzZXJuYW1lIjoiYWRtaW4iLCJwYXNzd29yZCI6IjEyMzQ1NiIsInN0dWRlbnRfaWQiOiIxMzAyMTYwMTI1IiwicGhvbmUiOiIxMzU5NDgxOTk1NiIsImVtYWlsIjoiMTM0NzYzODA5MUBxcS5jb20iLCJzdGF0ZSI6MH19', '2018-10-16 04:14:33.015421');
INSERT INTO `django_session` VALUES ('cfke7dayxjz538574yum08u1hp68vba2', 'ZjFmYTcwYzNiMThhYmE3NWFhYmIwYjY0M2UyYjk0NTgzMzVmY2NmZTp7InZlcmlmeWNvZGUiOiI4NTcxIiwidm9sdW50ZWVycyI6eyJpZCI6NSwic2V4IjoxLCJuYW1lIjoiXHU2ODkzXHU5MDM4XHU1YmI4IiwidXNlcm5hbWUiOiIxNTI0MzYwNjI1MCIsInBhc3N3b3JkIjoiZTEwYWRjMzk0OWJhNTlhYmJlNTZlMDU3ZjIwZjg4M2UiLCJzdHVkZW50X2lkIjoiMTMwMjE2MDEyNSIsInBob25lIjoiMTUyNDM2MDYyNTAiLCJlbWFpbCI6IjEzNDc2MzgwOTFAcXEuY29tIiwic3RhdGUiOjF9fQ==', '2018-10-16 17:55:20.799517');
INSERT INTO `django_session` VALUES ('gqmd8j21e7bjbsqpiq696b1qj34ed6t3', 'ZDVhMDBiZmNiYmNlZjZlOWFmMDFkNTI5ZTk3NGRkMzNlNWFiMjA5MTp7InZlcmlmeWNvZGUiOiI1Mzk1Iiwidm9sdW50ZWVycyI6eyJpZCI6NSwic2V4IjoxLCJuYW1lIjoiXHU2ODkzXHU5MDM4XHU1YmI4IiwidXNlcm5hbWUiOiIxNTI0MzYwNjI1MCIsInBhc3N3b3JkIjoiZTEwYWRjMzk0OWJhNTlhYmJlNTZlMDU3ZjIwZjg4M2UiLCJzdHVkZW50X2lkIjoiMTMwMjE2MDEyNSIsInBob25lIjoiMTUyNDM2MDYyNTAiLCJlbWFpbCI6IjEzNDc2MzgwOTFAcXEuY29tIiwic3RhdGUiOjF9fQ==', '2018-10-17 12:51:58.945569');
INSERT INTO `django_session` VALUES ('h3bv0szgoumnxxkbn16c7xmvvmk6192d', 'NmFmZGZjZGRkOWNkYWU3MjAwM2FkODQ0ZTY5ZDI2N2NlNWEwMzczNDp7InZlcmlmeWNvZGUiOiI5NjczIiwidm9sdW50ZWVycyI6eyJpZCI6NSwic2V4IjoxLCJuYW1lIjoiXHU2ODkzXHU5MDM4XHU1YmI4IiwidXNlcm5hbWUiOiIxNTI0MzYwNjI1MCIsInBhc3N3b3JkIjoiZTEwYWRjMzk0OWJhNTlhYmJlNTZlMDU3ZjIwZjg4M2UiLCJzdHVkZW50X2lkIjoiMTMwMjE2MDEyNSIsInBob25lIjoiMTUyNDM2MDYyNTAiLCJlbWFpbCI6IjEzNDc2MzgwOTFAcXEuY29tIiwic3RhdGUiOjF9fQ==', '2018-10-17 17:55:02.572439');
INSERT INTO `django_session` VALUES ('iqlkq0pd2tlzuoqlicsql590mc5alchn', 'MDc3ZDFkZjdiNDc1OGQzODdhMzQ4ZTY5ZDcyYjk3YjQ2ODAyMmE0Yzp7InZlcmlmeWNvZGUiOiIzMzcyIiwidm9sdW50ZWVycyI6eyJpZCI6NSwic2V4IjoxLCJuYW1lIjoiXHU2ODkzXHU5MDM4XHU1YmI4IiwidXNlcm5hbWUiOiIxNTI0MzYwNjI1MCIsInBhc3N3b3JkIjoiZTEwYWRjMzk0OWJhNTlhYmJlNTZlMDU3ZjIwZjg4M2UiLCJzdHVkZW50X2lkIjoiMTMwMjE2MDEyNSIsInBob25lIjoiMTUyNDM2MDYyNTAiLCJlbWFpbCI6IjEzNDc2MzgwOTFAcXEuY29tIiwic3RhdGUiOjF9fQ==', '2018-10-17 02:22:37.463057');
INSERT INTO `django_session` VALUES ('kusys95qqr8w7ywc3k9q8zijd3i6q9zb', 'OWY3MWFmMmVmNDg5OTVhY2FkMTExZmE5YTE3YzBkODExOTBmMjllMzp7InZlcmlmeWNvZGUiOiI1MDI4Iiwidm9sdW50ZWVycyI6eyJpZCI6NSwic2V4IjoxLCJuYW1lIjoiXHU2ODkzXHU5MDM4XHU1YmI4IiwidXNlcm5hbWUiOiIxNTI0MzYwNjI1MCIsInBhc3N3b3JkIjoiZTEwYWRjMzk0OWJhNTlhYmJlNTZlMDU3ZjIwZjg4M2UiLCJzdHVkZW50X2lkIjoiMTMwMjE2MDEyNiIsInBob25lIjoiMTUyNDM2MDYyNTAiLCJlbWFpbCI6IjEzNDc2MzgwOTFAcXEuY29tIiwic3RhdGUiOjF9LCJteWFkbWludXNlciI6eyJpZCI6Mywic2V4IjoxLCJuYW1lIjoiXHU5NDlmXHU0ZjBkXHU1MTY4IiwidXNlcm5hbWUiOiJ6aXlpY2hlbiIsInBhc3N3b3JkIjoiZTEwYWRjMzk0OWJhNTlhYmJlNTZlMDU3ZjIwZjg4M2UiLCJzdHVkZW50X2lkIjoiMTMwMjE2MDEyNSIsInBob25lIjoiMTUyNDM2MDYyNTAiLCJlbWFpbCI6IjEzNDc2MzgwOTFAcXEuY29tIiwic3RhdGUiOjB9fQ==', '2018-10-18 08:50:53.684159');
INSERT INTO `django_session` VALUES ('o2fpfoxh4zglm7pxpnoq20tbjlm5m5a9', 'OWM1MmNiZDM3ODllNjM1OGIzNGNmOWRlMDk2NGNkMzY3YjY2M2I3Njp7InZlcmlmeWNvZGUiOiI3OTU1Iiwidm9sdW50ZWVycyI6eyJpZCI6NSwic2V4IjoxLCJuYW1lIjoiIiwidXNlcm5hbWUiOiIxNTI0MzYwNjI1MCIsInBhc3N3b3JkIjoiZTEwYWRjMzk0OWJhNTlhYmJlNTZlMDU3ZjIwZjg4M2UiLCJzdHVkZW50X2lkIjoiIiwicGhvbmUiOiIxNTI0MzYwNjI1MCIsImVtYWlsIjoiIiwic3RhdGUiOjF9fQ==', '2018-10-17 17:21:39.500310');
INSERT INTO `django_session` VALUES ('pnqrze0s1enpodu1df45yffuk4nlgs3o', 'ZGZkYzZmN2NhYzhmODJkYjEyNzYwZjhiYTdjMjVlYzlkZDRlZDJlOTp7InZlcmlmeWNvZGUiOiI0NjUwIiwidm9sdW50ZWVycyI6eyJpZCI6NSwic2V4IjoxLCJuYW1lIjoiXHU2ODkzXHU5MDM4XHU1YmI4IiwidXNlcm5hbWUiOiIxNTI0MzYwNjI1MCIsInBhc3N3b3JkIjoiZTEwYWRjMzk0OWJhNTlhYmJlNTZlMDU3ZjIwZjg4M2UiLCJzdHVkZW50X2lkIjoiMTMwMjE2MDEyNSIsInBob25lIjoiMTUyNDM2MDYyNTAiLCJlbWFpbCI6IjEzNDc2MzgwOTFAcXEuY29tIiwic3RhdGUiOjF9fQ==', '2018-10-17 17:21:47.699463');
INSERT INTO `django_session` VALUES ('pp0lweg6iczrxe8vqu8uo1eey343l4fm', 'NDZjZTgyYmIwYmMxZGVkMWRiNzhiOWQ2NDhmNjVmOTllMWNlODA4NTp7InZlcmlmeWNvZGUiOiI1NzM4IiwibXlhZG1pbnVzZXIiOnsiaWQiOjEsInNleCI6MSwidXNlcm5hbWUiOiJhZG1pbiIsInBhc3N3b3JkIjoiY3N1X2pvYnNreXp3cSIsInN0dWRlbnRfaWQiOiIxMzAyMTYwMTI1IiwicGhvbmUiOiIxMzU5NDgxOTk1NiIsImVtYWlsIjoiMTM0NzYzODA5MUBxcS5jb20iLCJzdGF0ZSI6MH19', '2018-10-15 19:17:41.077801');
INSERT INTO `django_session` VALUES ('qe2clbouu5l7l2csp52dolaoiuwhyndg', 'NTVlZTgxZmM3ODQzNjkwODM2MTk4NTQyZWYwNjE2ZjYwOWJhNWNmYjp7InZlcmlmeWNvZGUiOiIzMDAzIiwidm9sdW50ZWVycyI6eyJpZCI6NSwic2V4IjoxLCJuYW1lIjoiXHU2ODkzXHU5MDM4XHU1YmI4IiwidXNlcm5hbWUiOiIxNTI0MzYwNjI1MCIsInBhc3N3b3JkIjoiZTEwYWRjMzk0OWJhNTlhYmJlNTZlMDU3ZjIwZjg4M2UiLCJzdHVkZW50X2lkIjoiMTMwMjE2MDEyNSIsInBob25lIjoiMTUyNDM2MDYyNTAiLCJlbWFpbCI6IjEzNDc2MzgwOTFAcXEuY29tIiwic3RhdGUiOjF9fQ==', '2018-10-17 09:33:48.460192');
INSERT INTO `django_session` VALUES ('rnkxm1bnxhstzkphmrvw792hweeguqj3', 'NWMwOTkxZjk4NDg1YWI2YzcwNDEzZjRkZDJmMzFiNTJiZjg1ZTdkNzp7InZlcmlmeWNvZGUiOiI0NjAwIiwidm9sdW50ZWVycyI6eyJpZCI6NSwic2V4IjoxLCJuYW1lIjoiXHU2ODkzXHU5MDM4XHU1YmI4IiwidXNlcm5hbWUiOiIxNTI0MzYwNjI1MCIsInBhc3N3b3JkIjoiZTEwYWRjMzk0OWJhNTlhYmJlNTZlMDU3ZjIwZjg4M2UiLCJzdHVkZW50X2lkIjoiMTMwMjE2MDEyNSIsInBob25lIjoiMTUyNDM2MDYyNTAiLCJlbWFpbCI6IjEzNDc2MzgwOTFAcXEuY29tIiwic3RhdGUiOjF9fQ==', '2018-10-16 17:27:23.239729');
INSERT INTO `django_session` VALUES ('sprcuv5u8b5vua9g3j74qh83ycdx635i', 'Mjk5Nzc4MDkxOGVmMjM0ZDQ0YTJjMDJhY2RiMDMzMzU2ZGRiMjhjNzp7InZlcmlmeWNvZGUiOiI4MTIyIiwidm9sdW50ZWVycyI6eyJpZCI6NSwic2V4IjoxLCJuYW1lIjoiXHU2ODkzXHU5MDM4XHU1YmI4IiwidXNlcm5hbWUiOiIxNTI0MzYwNjI1MCIsInBhc3N3b3JkIjoiZTEwYWRjMzk0OWJhNTlhYmJlNTZlMDU3ZjIwZjg4M2UiLCJzdHVkZW50X2lkIjoiMTMwMjE2MDEyNiIsInBob25lIjoiMTUyNDM2MDYyNTAiLCJlbWFpbCI6IjEzNDc2MzgwOTFAcXEuY29tIiwic3RhdGUiOjF9fQ==', '2018-10-18 03:43:05.952261');
INSERT INTO `django_session` VALUES ('szndyesaok8bqdbcimnlbozktulqtwho', 'NTIyMzg0ZTk0OTE4NmIwYjMxZTdjZDk5YzMyMzllNWJkZDRhODYwZTp7InZlcmlmeWNvZGUiOiI1MTA5Iiwidm9sdW50ZWVycyI6eyJpZCI6NSwic2V4IjoxLCJuYW1lIjoiXHU2ODkzXHU5MDM4XHU1YmI4IiwidXNlcm5hbWUiOiIxNTI0MzYwNjI1MCIsInBhc3N3b3JkIjoiZTEwYWRjMzk0OWJhNTlhYmJlNTZlMDU3ZjIwZjg4M2UiLCJzdHVkZW50X2lkIjoiMTMwMjE2MDEyNSIsInBob25lIjoiMTUyNDM2MDYyNTAiLCJlbWFpbCI6IjEzNDc2MzgwOTFAcXEuY29tIiwic3RhdGUiOjF9fQ==', '2018-10-17 09:28:05.822878');
COMMIT;

-- ----------------------------
-- Table structure for enterprise
-- ----------------------------
DROP TABLE IF EXISTS `enterprise`;
CREATE TABLE `enterprise` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `contacts` varchar(32) NOT NULL,
  `phone` varchar(16) NOT NULL,
  `picname` varchar(255) NOT NULL,
  `session_id` int(11) NOT NULL,
  `uid` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of enterprise
-- ----------------------------
BEGIN;
INSERT INTO `enterprise` VALUES (5, '钟启', '15243606250', '', 11, 5);
INSERT INTO `enterprise` VALUES (6, '', '', '', 12, 5);
COMMIT;

-- ----------------------------
-- Table structure for session
-- ----------------------------
DROP TABLE IF EXISTS `session`;
CREATE TABLE `session` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `enterprise` varchar(100) NOT NULL,
  `start_time` datetime(6) NOT NULL,
  `place` varchar(100) NOT NULL,
  `volunteer` varchar(32) NOT NULL,
  `summary` longtext NOT NULL,
  `uid` int(11) NOT NULL,
  `qr_imgname` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of session
-- ----------------------------
BEGIN;
INSERT INTO `session` VALUES (11, '阿里巴巴', '2018-10-02 02:00:00.000000', '科教南楼304', '梓逸宸', '总结待填写...', 5, '1538571636.172457u5i11.png');
INSERT INTO `session` VALUES (12, '腾讯', '2018-10-04 16:00:00.000000', '科教北楼103', '梓逸宸', '<p><img src=\"/static/media/article/20181004/20181004114009723.png\" title=\"20181004/20181004114009723.png\" alt=\"20181004/20181004114009723.png\"/></p><p>有趣的一天</p>', 5, '1538586427.777494u5i12.png');
COMMIT;

-- ----------------------------
-- Table structure for student
-- ----------------------------
DROP TABLE IF EXISTS `student`;
CREATE TABLE `student` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `school` varchar(100) NOT NULL,
  `major` varchar(100) NOT NULL,
  `stu_name` varchar(32) NOT NULL,
  `phone` varchar(16) NOT NULL,
  `session_id` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of student
-- ----------------------------
BEGIN;
INSERT INTO `student` VALUES (1, '中南大学', '计算机科学与技术', '钟伍全', '15243606250', 11);
COMMIT;

-- ----------------------------
-- Table structure for user
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(32) NOT NULL,
  `password` varchar(32) NOT NULL,
  `sex` int(11) NOT NULL,
  `student_id` varchar(10) NOT NULL,
  `email` varchar(50) NOT NULL,
  `phone` varchar(16) NOT NULL,
  `state` int(11) NOT NULL,
  `addtime` datetime(6) NOT NULL,
  `name` varchar(16) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of user
-- ----------------------------
BEGIN;
INSERT INTO `user` VALUES (3, 'ziyichen', 'e10adc3949ba59abbe56e057f20f883e', 1, '1302160125', '1347638091@qq.com', '15243606250', 0, '2018-10-02 04:24:34.000000', '钟伍全');
INSERT INTO `user` VALUES (5, '15243606250', 'e10adc3949ba59abbe56e057f20f883e', 1, '1302160126', '1347638091@qq.com', '15243606250', 1, '2018-10-02 08:43:31.000000', '梓逸宸');
COMMIT;

SET FOREIGN_KEY_CHECKS = 1;
