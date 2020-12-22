CREATE TABLE `pokemon` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `number` VARCHAR(5) NOT NULL,
  `name` VARCHAR(20) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE `type` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(10) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE `pokemon_type` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `pokemon_id` INT UNSIGNED NOT NULL,
  `type_id` INT UNSIGNED NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE `evolution` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `pokemon_id` INT UNSIGNED NOT NULL,
  `evolution_id` INT UNSIGNED,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

INSERT INTO `pokemon` (id, number, name) VALUES
  (1, '001', 'Bulbasaur'),
  (2, '002', 'Ivysaur'),
  (3, '003', 'Venusaur'),
  (4, '004', 'Charmander');

INSERT INTO `type` (id, name) VALUES
  (1, 'Gross'),
  (2, 'Poison'),
  (3, 'Fire');

INSERT INTO `pokemon_type` (id, pokemon_id, type_id) VALUES
  (1, 1, 1),
  (2, 1, 2),
  (3, 2, 1),
  (4, 2, 2),
  (5, 3, 1),
  (6, 3, 2),
  (7, 4, 3);

INSERT INTO `evolution` (id, pokemon_id, evolution_id) VALUES
  (1, 1, 2),
  (2, 1, 3),
  (3, 2, 3);

