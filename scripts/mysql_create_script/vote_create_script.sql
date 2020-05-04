DROP TABLE IF EXISTS `candidate`;
DROP TABLE IF EXISTS `election`;
DROP TABLE IF EXISTS `user`;
DROP TABLE IF EXISTS `vote`;

-- Create syntax for TABLE 'candidate'
CREATE TABLE IF NOT EXISTS `candidate` (
    `id` INT(11) UNSIGNED NOT NULL AUTO_INCREMENT,
    `name` VARCHAR(255) NOT NULL,
    `election_id` INT(11) UNSIGNED NULL DEFAULT NULL,
    PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Create syntax for TABLE 'election'
CREATE TABLE IF NOT EXISTS `election` (
    `id` INT(11) UNSIGNED NOT NULL AUTO_INCREMENT,
    `name` VARCHAR(255) NOT NULL,
    `start_date_utc` datetime NOT NULL,
    `duration` smallint(5) unsigned NOT NULL,
    `type` enum('single','ranked') DEFAULT 'single',
    PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Create syntax for TABLE 'user'
CREATE TABLE IF NOT EXISTS `user` (
    `id` INT(11) UNSIGNED NOT NULL AUTO_INCREMENT,
    `name` VARCHAR(255) NOT NULL,
    `username` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT '',
    `password` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT '',
    PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Create syntax for TABLE 'vote'
CREATE TABLE IF NOT EXISTS `vote` (
    `id` INT(11) UNSIGNED NOT NULL AUTO_INCREMENT,
    `user_id` INT(11) UNSIGNED NULL DEFAULT NULL,
    `election_id` INT(11) UNSIGNED NULL DEFAULT NULL,
    `candidate_id` INT(11) UNSIGNED NULL DEFAULT NULL,
    `cast_date_utc` DATETIME NULL DEFAULT NULL,
    PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
