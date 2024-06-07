-- OM 2021.02.56
-- FICHIER MYSQL POUR FAIRE FONCTIONNER LES EXEMPLES
-- DE REQUETES MYSQL
-- Database: dario_dibella_expi1a_entreprise_logistique_i164_2024

-- Destruction de la BD si elle existe.
-- Pour être certain d'avoir la dernière version des données

DROP DATABASE IF EXISTS dario_dibella_expi1a_entreprise_logistique_i164_2024;

-- Création d'un nouvelle base de donnée

CREATE DATABASE IF NOT EXISTS dario_dibella_expi1a_entreprise_logistique_i164_2024;

-- Utilisation de cette base de donnée

USE dario_dibella_expi1a_entreprise_logistique_i164_2024;

-- --------------------------------------------------------
-- Hôte:                         127.0.0.1
-- Version du serveur:           8.0.30 - MySQL Community Server - GPL
-- SE du serveur:                Win64
-- HeidiSQL Version:             12.1.0.6537
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Listage de la structure de la base pour dario_dibella_expi1a_entreprise_logistique_i164_2024
DROP DATABASE IF EXISTS `dario_dibella_expi1a_entreprise_logistique_i164_2024`;
CREATE DATABASE IF NOT EXISTS `dario_dibella_expi1a_entreprise_logistique_i164_2024` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `dario_dibella_expi1a_entreprise_logistique_i164_2024`;

-- Listage de la structure de table dario_dibella_expi1a_entreprise_logistique_i164_2024. t_chauffeur
DROP TABLE IF EXISTS `t_chauffeur`;
CREATE TABLE IF NOT EXISTS `t_chauffeur` (
  `ID_chauffeur` int NOT NULL AUTO_INCREMENT,
  `nom_chauffeur` varchar(255) DEFAULT NULL,
  `prenom_chauffeur` varchar(255) DEFAULT NULL,
  `telephone_chauffeur` varchar(15) DEFAULT NULL,
  PRIMARY KEY (`ID_chauffeur`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Listage des données de la table dario_dibella_expi1a_entreprise_logistique_i164_2024.t_chauffeur : ~15 rows (environ)
INSERT INTO `t_chauffeur` (`ID_chauffeur`, `nom_chauffeur`, `prenom_chauffeur`, `telephone_chauffeur`) VALUES
	(1, 'Johnson', 'Michael', '021 555 10 90'),
	(2, 'Smith', 'Emily', '021 555 10 91'),
	(3, 'Rodriguez', 'Juan', '021 555 10 92'),
	(4, 'Martinez', 'Sofia', '021 555 10 93'),
	(5, 'Nguyen', 'Alexander', '021 555 10 94'),
	(6, 'Brown', 'Olivia', '021 555 10 95'),
	(7, 'Ali', 'Mohammed', '021 555 10 96'),
	(8, 'Taylor', 'Isabella', '021 555 10 97'),
	(9, 'Wilson', 'Liam', '021 555 10 98'),
	(10, 'Garcia', 'Sophia', '021 555 10 99'),
	(11, 'Lee', 'Daniel', '021 555 11 00'),
	(12, 'Chen', 'Jessica', '021 555 11 01'),
	(13, 'Kumar', 'Aryan', '021 555 11 02'),
	(14, 'Wong', 'Emily', '021 555 11 03'),
	(15, 'Mueller', 'Lukas', '021 555 11 04');

-- Listage de la structure de table dario_dibella_expi1a_entreprise_logistique_i164_2024. t_client
DROP TABLE IF EXISTS `t_client`;
CREATE TABLE IF NOT EXISTS `t_client` (
  `ID_client` int NOT NULL AUTO_INCREMENT,
  `nom_client` varchar(255) DEFAULT NULL,
  `prenom_client` varchar(255) DEFAULT NULL,
  `adresse_client` varchar(255) DEFAULT NULL,
  `numero_telephone_client` varchar(15) DEFAULT NULL,
  PRIMARY KEY (`ID_client`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Listage des données de la table dario_dibella_expi1a_entreprise_logistique_i164_2024.t_client : ~15 rows (environ)
INSERT INTO `t_client` (`ID_client`, `nom_client`, `prenom_client`, `adresse_client`, `numero_telephone_client`) VALUES
	(1, 'García', 'Miguel', 'Calle Mayor 123, Madrid', '076 123 45 67'),
	(2, 'Schneider', 'Hannah', 'Hauptstraße 45, Berlin', '076 909 80 12'),
	(3, 'Dubois', 'Marie', 'Rue de la Paix 7, Paris', '076 543 69 39'),
	(4, 'Rossi', 'Giuseppe', 'Via Roma 10, Rome', '076 105 94 28'),
	(5, 'Andersson', 'Erik', 'Drottninggatan 1, Stockholm', '078 695 39 43'),
	(6, 'Santos', 'Ana', 'Rua das Flores 25, Lisbon', '078 049 24 34'),
	(7, 'Nowak', 'Katarzyna', 'Aleje Jerozolimskie 100, Warsaw', '078 807 96 58'),
	(8, 'Ivanov', 'Dmitry', 'Tverskaya ulitsa 1, Moscow', '079 395 48 45'),
	(9, 'Papadopoulos', 'Maria', 'Aiolou 15, Athens', '079 222 11 11'),
	(10, 'Smith', 'John', '123 Main Street, New York', '079 999 99 99'),
	(11, 'Nguyen', 'Thi', 'Dien Bien Phu Street, Ho Chi Minh City', '079 564 45 65'),
	(12, 'Chen', 'Wei', 'Nanjing Road 100, Shanghai', '079 898 89 98'),
	(13, 'Gomez', 'Luis', 'Carrera 10, Bogotá', '079 174 65 34'),
	(14, 'Singh', 'Raj', 'Connaught Place, New Delhi', '079 548 39 43'),
	(15, 'Kim', 'Soo', 'Gangnam-gu, Seoul', '079 574 92 57');

-- Listage de la structure de table dario_dibella_expi1a_entreprise_logistique_i164_2024. t_employer
DROP TABLE IF EXISTS `t_employer`;
CREATE TABLE IF NOT EXISTS `t_employer` (
  `ID_employer` int NOT NULL AUTO_INCREMENT,
  `nom_employer` varchar(255) DEFAULT NULL,
  `prenom_employer` varchar(255) DEFAULT NULL,
  `numero_telephone_employer` varchar(15) DEFAULT NULL,
  PRIMARY KEY (`ID_employer`)
) ENGINE=InnoDB AUTO_INCREMENT=51 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Listage des données de la table dario_dibella_expi1a_entreprise_logistique_i164_2024.t_employer : ~15 rows (environ)
INSERT INTO `t_employer` (`ID_employer`, `nom_employer`, `prenom_employer`, `numero_telephone_employer`) VALUES
	(1, 'Müller', 'Hans', '021 555 00 01'),
	(2, 'Schneider', 'Anna', '021 555 00 02'),
	(3, 'Rossi', 'Giovanni', '021 555 00 03'),
	(4, 'dubois', 'Marla', '021 555 00 04'),
	(5, 'meier', 'Peter', '021 555 00 05'),
	(6, 'Fischer', 'Sandra', '021 555 00 06'),
	(7, 'Meyer', 'Thomas', '021 555 00 07'),
	(8, 'Wyss', 'Monika', '021 555 00 08'),
	(9, 'Schmid', 'Andreas', '021 555 00 09'),
	(10, 'Keller', 'Sarah', '021 555 00 10'),
	(11, 'lüthi', 'Markus', '021 555 00 11'),
	(12, 'Suter', 'Nadine', '021 555 00 12'),
	(13, 'brunner', 'Sabrina', '	021 555 00 13'),
	(14, 'Zimmermann', 'David', '021 555 00 14'),
	(15, 'Roth', 'Julia', '021 555 00 15');

-- Listage de la structure de table dario_dibella_expi1a_entreprise_logistique_i164_2024. t_fournisseur
DROP TABLE IF EXISTS `t_fournisseur`;
CREATE TABLE IF NOT EXISTS `t_fournisseur` (
  `ID_fournisseur` int NOT NULL AUTO_INCREMENT,
  `ID_produit` int DEFAULT NULL,
  `nom_fournisseur` varchar(255) DEFAULT NULL,
  `adresse_fournisseur` varchar(255) DEFAULT NULL,
  `numero_telephone_fournisseur` varchar(15) DEFAULT NULL,
  PRIMARY KEY (`ID_fournisseur`),
  KEY `FK_fournisseur_produit` (`ID_produit`),
  CONSTRAINT `FK_fournisseur_produit` FOREIGN KEY (`ID_produit`) REFERENCES `t_produit` (`ID_produit`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Listage des données de la table dario_dibella_expi1a_entreprise_logistique_i164_2024.t_fournisseur : ~15 rows (environ)
INSERT INTO `t_fournisseur` (`ID_fournisseur`, `ID_produit`, `nom_fournisseur`, `adresse_fournisseur`, `numero_telephone_fournisseur`) VALUES
	(1, 6, 'Dell', 'Piazza della Riforma 9, 6901 Lugano', '021 865 43 32'),
	(2, 9, 'Dell', 'Piazza della Riforma 9, 6901 Lugano', '021 865 43 32'),
	(3, 15, 'Bechtle', 'Avenue des Alpes 4, 1202 Genève', '021 355 32 54'),
	(4, 3, 'Bechtle', 'Avenue des Alpes 4, 1202 Genève', '021 355 32 54'),
	(5, 13, 'Bechtle', 'Avenue des Alpes 4, 1202 Genève', '021 355 32 54'),
	(6, 2, 'Dell', 'Piazza della Riforma 9, 6901 Lugano', '021 865 43 32'),
	(7, 5, 'Dell', 'Piazza della Riforma 9, 6901 Lugano', '021 865 43 32'),
	(8, 7, 'Dell', 'Piazza della Riforma 9, 6901 Lugano', '021 865 43 32'),
	(9, 14, 'Dell', 'Piazza della Riforma 9, 6901 Lugano', '021 865 43 32'),
	(10, 11, 'Dell', 'Piazza della Riforma 9, 6901 Lugano', '021 865 43 32'),
	(11, 1, 'Bechtle', 'Avenue des Alpes 4, 1202 Genève', '021 355 32 54'),
	(12, 12, 'Bechtle', 'Avenue des Alpes 4, 1202 Genève', '021 355 32 54'),
	(13, 10, 'Bechtle', 'Avenue des Alpes 4, 1202 Genève', '021 355 32 54'),
	(14, 4, 'Bechtle', 'Avenue des Alpes 4, 1202 Genève', '021 355 32 54'),
	(15, 8, 'Bechtle', 'Avenue des Alpes 4, 1202 Genève', '021 355 32 54');

-- Listage de la structure de table dario_dibella_expi1a_entreprise_logistique_i164_2024. t_fournisseur_produit
DROP TABLE IF EXISTS `t_fournisseur_produit`;
CREATE TABLE IF NOT EXISTS `t_fournisseur_produit` (
  `ID_fournisseur_produit` int NOT NULL AUTO_INCREMENT,
  `ID_fournisseur` int NOT NULL,
  `ID_produit` int NOT NULL,
  PRIMARY KEY (`ID_fournisseur_produit`),
  KEY `FK_fournisseur` (`ID_fournisseur`),
  KEY `FK_produit` (`ID_produit`),
  CONSTRAINT `FK_fournisseur` FOREIGN KEY (`ID_fournisseur`) REFERENCES `t_fournisseur` (`ID_fournisseur`),
  CONSTRAINT `FK_produit` FOREIGN KEY (`ID_produit`) REFERENCES `t_produit` (`ID_produit`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Listage des données de la table dario_dibella_expi1a_entreprise_logistique_i164_2024.t_fournisseur_produit : ~15 rows (environ)
INSERT INTO `t_fournisseur_produit` (`ID_fournisseur_produit`, `ID_fournisseur`, `ID_produit`) VALUES
	(1, 1, 6),
	(2, 2, 9),
	(3, 3, 15),
	(4, 4, 3),
	(5, 5, 13),
	(6, 6, 2),
	(7, 7, 5),
	(8, 8, 7),
	(9, 9, 14),
	(10, 10, 11),
	(11, 11, 1),
	(12, 12, 12),
	(13, 13, 10),
	(14, 14, 4),
	(15, 15, 8);

-- Listage de la structure de table dario_dibella_expi1a_entreprise_logistique_i164_2024. t_gestion_des_commandes
DROP TABLE IF EXISTS `t_gestion_des_commandes`;
CREATE TABLE IF NOT EXISTS `t_gestion_des_commandes` (
  `ID_gestion_des_commandes` int NOT NULL AUTO_INCREMENT,
  `ID_produit_1` int DEFAULT NULL,
  `ID_client_1` int DEFAULT NULL,
  `ID_livraison_1` int DEFAULT NULL,
  `ID_chauffeur_1` int DEFAULT NULL,
  `ID_employer_1` int DEFAULT NULL,
  `numero_commande` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  PRIMARY KEY (`ID_gestion_des_commandes`),
  KEY `FK_commandes_produit` (`ID_produit_1`) USING BTREE,
  KEY `FK_commandes_client` (`ID_client_1`) USING BTREE,
  KEY `FK_commandes_livraison` (`ID_livraison_1`) USING BTREE,
  KEY `FK_commandes_chauffeur` (`ID_chauffeur_1`) USING BTREE,
  KEY `FK_commandes_employer` (`ID_employer_1`) USING BTREE,
  CONSTRAINT `FK_commandes_chauffeur` FOREIGN KEY (`ID_chauffeur_1`) REFERENCES `t_chauffeur` (`ID_chauffeur`),
  CONSTRAINT `FK_commandes_client` FOREIGN KEY (`ID_client_1`) REFERENCES `t_client` (`ID_client`),
  CONSTRAINT `FK_commandes_employer` FOREIGN KEY (`ID_employer_1`) REFERENCES `t_employer` (`ID_employer`),
  CONSTRAINT `FK_commandes_livraison` FOREIGN KEY (`ID_livraison_1`) REFERENCES `t_livraison` (`ID_livraison`),
  CONSTRAINT `FK_commandes_produit` FOREIGN KEY (`ID_produit_1`) REFERENCES `t_produit` (`ID_produit`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Listage des données de la table dario_dibella_expi1a_entreprise_logistique_i164_2024.t_gestion_des_commandes : ~15 rows (environ)
INSERT INTO `t_gestion_des_commandes` (`ID_gestion_des_commandes`, `ID_produit_1`, `ID_client_1`, `ID_livraison_1`, `ID_chauffeur_1`, `ID_employer_1`, `numero_commande`) VALUES
	(1, 2, 5, 1, 7, 13, '10-200-01'),
	(2, 5, 12, 2, 6, 4, '10-200-02'),
	(3, 7, 3, 3, 12, 6, '10-200-03'),
	(4, 14, 1, 4, 10, 10, '10-200-04'),
	(5, 11, 13, 5, 1, 11, '10-200-05'),
	(6, 6, 8, 6, 13, 5, '10-200-06'),
	(7, 9, 15, 7, 11, 7, '10-200-07'),
	(8, 15, 11, 8, 4, 1, '10-200-08'),
	(9, 3, 7, 9, 15, 3, '10-200-09'),
	(10, 13, 9, 10, 5, 15, '10-200-10'),
	(11, 1, 4, 11, 3, 9, '10-200-11'),
	(12, 12, 6, 12, 2, 2, '10-200-12'),
	(13, 10, 2, 13, 8, 12, '10-200-13'),
	(14, 4, 14, 14, 9, 8, '10-200-14'),
	(15, 8, 10, 15, 14, 14, '10-200-15');

-- Listage de la structure de table dario_dibella_expi1a_entreprise_logistique_i164_2024. t_livraison
DROP TABLE IF EXISTS `t_livraison`;
CREATE TABLE IF NOT EXISTS `t_livraison` (
  `ID_livraison` int NOT NULL AUTO_INCREMENT,
  `ID_chauffeur` int DEFAULT NULL,
  `ID_produit` int DEFAULT NULL,
  `date_livraison` datetime DEFAULT NULL,
  PRIMARY KEY (`ID_livraison`),
  KEY `FK_livraison_chauffeur` (`ID_chauffeur`),
  KEY `FK_livraison_produit` (`ID_produit`),
  CONSTRAINT `FK_livraison_chauffeur` FOREIGN KEY (`ID_chauffeur`) REFERENCES `t_chauffeur` (`ID_chauffeur`),
  CONSTRAINT `FK_livraison_produit` FOREIGN KEY (`ID_produit`) REFERENCES `t_produit` (`ID_produit`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Listage des données de la table dario_dibella_expi1a_entreprise_logistique_i164_2024.t_livraison : ~15 rows (environ)
INSERT INTO `t_livraison` (`ID_livraison`, `ID_chauffeur`, `ID_produit`, `date_livraison`) VALUES
	(1, 7, 2, '2025-01-12 00:00:00'),
	(2, 6, 5, '2024-11-11 00:00:00'),
	(3, 12, 7, '2024-03-27 00:00:00'),
	(4, 10, 14, '2025-06-07 00:00:00'),
	(5, 1, 11, '2025-12-12 00:00:00'),
	(6, 13, 6, '2025-09-24 00:00:00'),
	(7, 11, 9, '2025-09-19 00:00:00'),
	(8, 4, 15, '2025-04-03 00:00:00'),
	(9, 15, 3, '2024-01-10 00:00:00'),
	(10, 5, 13, '2024-12-13 00:00:00'),
	(11, 3, 1, '2024-12-24 00:00:00'),
	(12, 2, 12, '2025-12-30 00:00:00'),
	(13, 8, 10, '2025-07-25 00:00:00'),
	(14, 9, 4, '2025-10-10 00:00:00'),
	(15, 14, 8, '2024-10-11 00:00:00');

-- Listage de la structure de table dario_dibella_expi1a_entreprise_logistique_i164_2024. t_produit
DROP TABLE IF EXISTS `t_produit`;
CREATE TABLE IF NOT EXISTS `t_produit` (
  `ID_produit` int NOT NULL AUTO_INCREMENT,
  `nom_produit` varchar(255) DEFAULT NULL,
  `description_produit` text,
  `poids_produit` decimal(10,2) DEFAULT NULL,
  `quantite_en_stock` int DEFAULT NULL,
  `prix_produit` decimal(10,2) DEFAULT NULL,
  PRIMARY KEY (`ID_produit`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Listage des données de la table dario_dibella_expi1a_entreprise_logistique_i164_2024.t_produit : ~15 rows (environ)
INSERT INTO `t_produit` (`ID_produit`, `nom_produit`, `description_produit`, `poids_produit`, `quantite_en_stock`, `prix_produit`) VALUES
	(1, 'Processeur ', 'haute performance pour des calculs rapides et une expérience informatique fluide', 0.10, 32, 200.00),
	(2, 'Carte graphique', 'Carte dédiée pour des graphismes époustouflants et des jeux fluides ', 1.00, 12, 500.00),
	(3, 'Mémoire RAM', 'Mémoire vive rapide pour des performances multitâches exceptionnelles', 0.01, 5, 100.00),
	(4, 'SSD', 'Stockage ultrarapide pour un accès rapide aux données et des temps de chargement réduits', 0.20, 22, 250.00),
	(5, 'Carte mère', 'Fondation centrale d\'un ordinateur, compatible avec une large gamme de composants', 0.50, 7, 150.00),
	(6, 'Écran LED Full HD', 'Écran haute résolution pour une expérience visuelle immersive', 3.00, 3, 300.00),
	(7, 'Casque audio', 'Casque confortable offrant un son de haute qualité pour une immersion totale', 0.30, 10, 80.00),
	(8, 'Webcam HD', 'Webcam haute définition pour des appels vidéo clairs et nets', 0.10, 17, 70.00),
	(9, 'Imprimante ', 'Imprimante polyvalente pour des impressions de qualité professionnelle', 10.00, 9, 200.00),
	(10, 'Souris ergonomique', 'Souris confortable et précise pour une navigation sans effort', 0.20, 13, 30.00),
	(11, 'Clavier sans fil', 'Clavier compact et sans fil avec touches réactives pour une saisie confortable et sans encombremen', 0.50, 12, 60.00),
	(12, 'Routeur Wi-Fi', 'Routeur haut débit avec la dernière norme Wi-Fi pour des connexions Internet ultra-rapides et stables', 0.50, 5, 120.00),
	(13, 'PC Gamer', 'Ordinateur de bureau puissant équipé des derniers processeurs et cartes graphiques pour des performances de jeu exceptionnelles', 15.00, 4, 2500.00),
	(14, 'Clavier rétroéclairé ', ' Clavier d\'ordinateur avec rétroéclairage LED ajustable, offrant une expérience de frappe confortable même dans des environnements peu éclairés', 0.80, 13, 70.00),
	(15, 'Laptop Ultra-léger', 'Ordinateur portable ultraportable offrant une combinaison parfaite de performance et de mobilité, avec un design élégant et une autonomie longue durée', 1.90, 10, 900.00);

-- Listage de la structure de table dario_dibella_expi1a_entreprise_logistique_i164_2024. t_rh
DROP TABLE IF EXISTS `t_rh`;
CREATE TABLE IF NOT EXISTS `t_rh` (
  `ID_rh` int NOT NULL AUTO_INCREMENT,
  `ID_employer` int DEFAULT NULL,
  `nom_employer_rh` varchar(255) DEFAULT NULL,
  `prenom_employer_rh` varchar(255) DEFAULT NULL,
  `numero_telephone_rh` varchar(15) DEFAULT NULL,
  PRIMARY KEY (`ID_rh`),
  KEY `FK_rh_employer` (`ID_employer`),
  CONSTRAINT `FK_rh_employer` FOREIGN KEY (`ID_employer`) REFERENCES `t_employer` (`ID_employer`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Listage des données de la table dario_dibella_expi1a_entreprise_logistique_i164_2024.t_rh : ~15 rows (environ)
INSERT INTO `t_rh` (`ID_rh`, `ID_employer`, `nom_employer_rh`, `prenom_employer_rh`, `numero_telephone_rh`) VALUES
	(1, 14, 'Rossi', 'Luca', '021 555 20 00'),
	(2, 8, 'Rossi', 'Luca', '021 555 20 00'),
	(3, 12, 'Rossi', 'Luca', '021 555 20 00'),
	(4, 2, 'Abdullah', 'Ahmed', '021 555 20 01'),
	(5, 9, 'Abdullah', 'Ahmed', '021 555 20 01'),
	(6, 15, 'Abdullah', 'Ahmed', '021 555 20 01'),
	(7, 3, 'Abdullah', 'Ahmed', '021 555 20 01'),
	(8, 1, 'Santos', 'Maria', '021 555 20 02'),
	(9, 7, 'Santos', 'Maria', '021 555 20 02'),
	(10, 5, 'Santos', 'Maria', '021 555 20 02'),
	(11, 11, 'Santos', 'Maria', '021 555 20 02'),
	(12, 10, 'Dupont', 'Jean', '021 555 20 03'),
	(13, 6, 'Dupont', 'Jean', '021 555 20 03'),
	(14, 4, 'Dupont', 'Jean', '021 555 20 03'),
	(15, 13, 'Dupont', 'Jean', '021 555 20 03');

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
