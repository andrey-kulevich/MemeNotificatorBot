-- -----------------------------------------------------
-- Schema meme_notification
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `meme_notification` DEFAULT CHARACTER SET utf8 ;
USE `meme_notification` ;

-- -----------------------------------------------------
-- Table `meme_notification`.`preferences`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `meme_notification`.`preferences` (
	`id` INT NOT NULL AUTO_INCREMENT,
	`value` VARCHAR(100) NOT NULL,
	PRIMARY KEY (`id`)
);

-- -----------------------------------------------------
-- Table `meme_notification`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `meme_notification`.`users` (
	`id` INT NOT NULL UNIQUE,
	`preferences` INT NULL,
	`name` VARCHAR(45) NOT NULL,
	PRIMARY KEY (`id`),
	INDEX `preferences_idx` (`preferences` ASC) VISIBLE,
	FOREIGN KEY (`preferences`) REFERENCES `meme_notification`.`preferences` (`id`)
);

-- -----------------------------------------------------
-- Table `meme_notification`.`notes`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `meme_notification`.`notes` (
	`id` INT NOT NULL AUTO_INCREMENT,
	`notification_date` DATETIME NULL,
	`notification_frequency` INT NOT NULL,
	`content` VARCHAR(1000) NOT NULL,
	`user` INT NOT NULL,
	PRIMARY KEY (`id`),
	INDEX `user_idx` (`user` ASC) VISIBLE,
    FOREIGN KEY (`user`) REFERENCES `meme_notification`.`users` (`id`)
);
-- -----------------------------------------------------
-- Table `meme_notification`.`images`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `meme_notification`.`images` (
	`id` INT NOT NULL AUTO_INCREMENT,
	`name` VARCHAR(100) NOT NULL,
	`url` VARCHAR(300) NOT NULL,
	`preferences` INT NOT NULL,
	PRIMARY KEY (`id`),
	INDEX `preferences_idx` (`preferences` ASC) VISIBLE,
    FOREIGN KEY (`preferences`) REFERENCES `meme_notification`.`preferences` (`id`)
);