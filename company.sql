-- phpMyAdmin SQL Dump
-- version 4.5.1
-- http://www.phpmyadmin.net
--
-- Host: 127.0.0.1
-- Generation Time: 25 Jan 2023 pada 14.09
-- Versi Server: 10.1.9-MariaDB
-- PHP Version: 7.0.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `company`
--

-- --------------------------------------------------------

--
-- Struktur dari tabel `employes`
--

CREATE TABLE `employes` (
  `id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `telp` varchar(50) NOT NULL,
  `address` varchar(255) NOT NULL,
  `filename` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data untuk tabel `employes`
--

INSERT INTO `employes` (`id`, `name`, `email`, `telp`, `address`, `filename`) VALUES
(10, 'M. Imam Zarkasih', 'imam123@gmail.com', '087762534412', 'Aikmel, NTB', 'IMG-20210321-WA0034.jpg'),
(11, 'Muhafizil Adli', 'fizil123@gmail.com', '087763551441', 'Ranca, Masbagik, NTB', 'foto_almet3.jpg'),
(13, 'M. Azizan', 'zizna121@gmail.com', '087725836661', 'Rempung, NTB', '1669946830731.jpg'),
(14, 'M. Syamsul Hikami', 'ikma844@gmail.com', '081183774651', 'Kelayu, NTB', '1634318687978.jpg'),
(15, 'Jismi Bafadal', 'jsime9i439@gmail.com', '085529187310', 'Selong, NTB', '1540276247.jpg');

-- --------------------------------------------------------

--
-- Struktur dari tabel `tb_users`
--

CREATE TABLE `tb_users` (
  `id` int(11) NOT NULL,
  `username` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data untuk tabel `tb_users`
--

INSERT INTO `tb_users` (`id`, `username`, `email`, `password`) VALUES
(1, 'admin', 'admin123@gmail.com', 'pbkdf2:sha256:260000$LakUVQRKZefRXKIs$0c4dfb0fef59f27c9bf0aa1f0fee16f7392e78edc70265997183364c9d9845a3'),
(2, 'admin2', 'admin2@gmail.com', 'pbkdf2:sha256:260000$ZmmtRFHUyYoP38jE$64d68eb0dfbd2ad5c5e84f75a10242b8c4a1be6ee1b8b96df9e81475f28136a2'),
(3, 'admin3', 'admin3@gamil.com', 'pbkdf2:sha256:260000$6tliSOcSpinKGKwc$5f3be02069e053de4b104e06e0a7576fbf77c3749bacb4d0acf2ff986e57b3a3');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `employes`
--
ALTER TABLE `employes`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `tb_users`
--
ALTER TABLE `tb_users`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `employes`
--
ALTER TABLE `employes`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;
--
-- AUTO_INCREMENT for table `tb_users`
--
ALTER TABLE `tb_users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
