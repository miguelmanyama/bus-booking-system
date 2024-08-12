-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1
-- Généré le : dim. 31 mars 2024 à 13:13
-- Version du serveur : 10.4.28-MariaDB
-- Version de PHP : 8.1.17

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `bookinng_system`
--

-- --------------------------------------------------------

--
-- Structure de la table `agency`
--

CREATE TABLE `agency` (
  `id` int(50) NOT NULL,
  `agencyname` varchar(255) NOT NULL,
  `address` varchar(255) NOT NULL,
  `country` varchar(255) NOT NULL,
  `town` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `phone` varchar(100) DEFAULT NULL,
  `fax` varchar(100) DEFAULT NULL,
  `manager_id` int(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `agency`
--

INSERT INTO `agency` (`id`, `agencyname`, `address`, `country`, `town`, `email`, `phone`, `fax`, `manager_id`) VALUES
(2, 'VATICAN', 'Bonaberri', 'Cameroon', 'Douala', 'johndoe@example.com', '678549100', '200,483,849', 1),
(4, 'Mogamo', 'Diedo', 'Cameroon', 'Douala', 'mogamo@example.com', '69843023', '478,002,637', 3),
(5, 'BUCA', 'City chemist', 'Cameroon', 'Bamenda', 'bucabuca@example.com', '672097849', '739,038,379', 2);

-- --------------------------------------------------------

--
-- Structure de la table `booking`
--

CREATE TABLE `booking` (
  `id` int(50) NOT NULL,
  `client_id` int(50) NOT NULL,
  `bus_id` int(50) NOT NULL,
  `trip_id` int(50) NOT NULL,
  `status` varchar(50) NOT NULL,
  `date` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `booking`
--

INSERT INTO `booking` (`id`, `client_id`, `bus_id`, `trip_id`, `status`, `date`) VALUES
(1, 1, 2, 1, 'Pending', '2024-03-31'),
(4, 5, 2, 1, 'Paid', '2024-03-31');

-- --------------------------------------------------------

--
-- Structure de la table `bus`
--

CREATE TABLE `bus` (
  `id` int(50) NOT NULL,
  `type` varchar(100) NOT NULL,
  `sits` varchar(100) NOT NULL,
  `agency_id` int(50) DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL,
  `name` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `bus`
--

INSERT INTO `bus` (`id`, `type`, `sits`, `agency_id`, `status`, `name`) VALUES
(1, 'Local', '40', 5, 'Inactive', 'Test'),
(2, 'Local', '40', 2, 'Active', 'LT0478v2'),
(3, 'Local', '40', 2, 'Active', 'Test'),
(5, 'Local', '40', 5, 'Inactive', 'Test');

-- --------------------------------------------------------

--
-- Structure de la table `trip`
--

CREATE TABLE `trip` (
  `id` int(50) NOT NULL,
  `start_destination` varchar(100) NOT NULL,
  `end_destination` varchar(100) NOT NULL,
  `departure_time` datetime(4) NOT NULL,
  `bus_id` int(50) NOT NULL,
  `agency_id` int(50) NOT NULL,
  `cost` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `trip`
--

INSERT INTO `trip` (`id`, `start_destination`, `end_destination`, `departure_time`, `bus_id`, `agency_id`, `cost`) VALUES
(1, 'Douala', 'Bamenda', '2004-03-31 05:55:00.0000', 2, 2, '5000'),
(2, 'Douala', 'Yaounde', '2004-03-31 05:55:00.0000', 3, 2, '5000');

-- --------------------------------------------------------

--
-- Structure de la table `users`
--

CREATE TABLE `users` (
  `id` int(50) NOT NULL,
  `name` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `phonenumber` varchar(100) NOT NULL,
  `password` varchar(50) NOT NULL,
  `role` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `users`
--

INSERT INTO `users` (`id`, `name`, `email`, `phonenumber`, `password`, `role`) VALUES
(1, 'Pouth Iris', 'Pouth@gmail.com', '674093792', 'p1234', 'manager'),
(2, 'Pouth Iris', 'Pouth@gmail.com', '674093792', 'p1234', 'manager'),
(3, 'Pouth Iris', 'Pouth@gmail.com', '674093792', 'p1234', 'manager'),
(5, 'Pouth Iris', 'Pouth@gmail.com', '674093792', 'p1234', 'manager'),
(6, 'Pouth Iris', 'Pouth@gmail.com', '674093792', 'p1234', 'manager'),
(7, 'Pouth Iris', 'Pouth@gmail.com', '674093792', 'p1234', 'manager'),
(8, 'Pouth Iris', 'Pouth@gmail.com', '674093792', 'p1234', 'manager'),
(9, 'Manager', 'manager@gmail.com', '698002648', '030hh30', 'manager');

--
-- Index pour les tables déchargées
--

--
-- Index pour la table `agency`
--
ALTER TABLE `agency`
  ADD PRIMARY KEY (`id`),
  ADD KEY `manager_id` (`manager_id`);

--
-- Index pour la table `booking`
--
ALTER TABLE `booking`
  ADD PRIMARY KEY (`id`),
  ADD KEY `client_id` (`client_id`),
  ADD KEY `bus_id` (`bus_id`),
  ADD KEY `trip_id` (`trip_id`);

--
-- Index pour la table `bus`
--
ALTER TABLE `bus`
  ADD PRIMARY KEY (`id`),
  ADD KEY `agency_id` (`agency_id`);

--
-- Index pour la table `trip`
--
ALTER TABLE `trip`
  ADD PRIMARY KEY (`id`),
  ADD KEY `bus_id` (`bus_id`),
  ADD KEY `agency_id` (`agency_id`);

--
-- Index pour la table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT pour les tables déchargées
--

--
-- AUTO_INCREMENT pour la table `agency`
--
ALTER TABLE `agency`
  MODIFY `id` int(50) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT pour la table `booking`
--
ALTER TABLE `booking`
  MODIFY `id` int(50) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT pour la table `bus`
--
ALTER TABLE `bus`
  MODIFY `id` int(50) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT pour la table `trip`
--
ALTER TABLE `trip`
  MODIFY `id` int(50) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT pour la table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(50) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- Contraintes pour les tables déchargées
--

--
-- Contraintes pour la table `agency`
--
ALTER TABLE `agency`
  ADD CONSTRAINT `agency_ibfk_1` FOREIGN KEY (`manager_id`) REFERENCES `users` (`id`);

--
-- Contraintes pour la table `booking`
--
ALTER TABLE `booking`
  ADD CONSTRAINT `booking_ibfk_1` FOREIGN KEY (`client_id`) REFERENCES `users` (`id`),
  ADD CONSTRAINT `booking_ibfk_2` FOREIGN KEY (`bus_id`) REFERENCES `bus` (`id`),
  ADD CONSTRAINT `booking_ibfk_3` FOREIGN KEY (`trip_id`) REFERENCES `trip` (`id`);

--
-- Contraintes pour la table `bus`
--
ALTER TABLE `bus`
  ADD CONSTRAINT `bus_ibfk_1` FOREIGN KEY (`agency_id`) REFERENCES `agency` (`id`);

--
-- Contraintes pour la table `trip`
--
ALTER TABLE `trip`
  ADD CONSTRAINT `trip_ibfk_1` FOREIGN KEY (`bus_id`) REFERENCES `bus` (`id`),
  ADD CONSTRAINT `trip_ibfk_2` FOREIGN KEY (`agency_id`) REFERENCES `agency` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
