-- phpMyAdmin SQL Dump
-- version 3.2.0.1
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Oct 26, 2017 at 01:55 PM
-- Server version: 5.1.36
-- PHP Version: 5.3.0

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `exam_schedule`
--

-- --------------------------------------------------------

--
-- Table structure for table `batch`
--

CREATE TABLE IF NOT EXISTS `batch` (
  `batch_id` int(11) NOT NULL AUTO_INCREMENT,
  `course_id` varchar(111) NOT NULL,
  `course_name` varchar(111) NOT NULL,
  `department` varchar(111) NOT NULL,
  `slot` varchar(111) NOT NULL,
  `class` varchar(111) NOT NULL,
  PRIMARY KEY (`batch_id`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=3 ;

--
-- Dumping data for table `batch`
--

INSERT INTO `batch` (`batch_id`, `course_id`, `course_name`, `department`, `slot`, `class`) VALUES
(1, 'cse-1001', 'python', 'cs', 'A1', 'sjt512'),
(2, 'cse1002', 'sql', 'cs', 'A2', 'sjt415');

-- --------------------------------------------------------

--
-- Table structure for table `exam`
--

CREATE TABLE IF NOT EXISTS `exam` (
  `student_id` int(11) NOT NULL,
  `exam_id` int(11) NOT NULL,
  `batch_id` int(11) NOT NULL,
  `seat_no` int(11) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `exam`
--

INSERT INTO `exam` (`student_id`, `exam_id`, `batch_id`, `seat_no`) VALUES
(101, 111111, 2, 1),
(102, 222222, 1, 2),
(101, 222222, 1, 22);

-- --------------------------------------------------------

--
-- Table structure for table `e_info`
--

CREATE TABLE IF NOT EXISTS `e_info` (
  `exam_id` int(11) NOT NULL AUTO_INCREMENT,
  `venue` varchar(100) NOT NULL,
  `date` varchar(100) NOT NULL,
  `time` varchar(100) NOT NULL,
  PRIMARY KEY (`exam_id`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=222223 ;

--
-- Dumping data for table `e_info`
--

INSERT INTO `e_info` (`exam_id`, `venue`, `date`, `time`) VALUES
(111111, 'MB101', '2/11/2017', '10:00:00 AM'),
(222222, 'MB203', '5/11/2017', '08:00:00 AM');

-- --------------------------------------------------------

--
-- Table structure for table `faculty`
--

CREATE TABLE IF NOT EXISTS `faculty` (
  `faculty_id` int(11) NOT NULL AUTO_INCREMENT,
  `exam_id` int(11) NOT NULL,
  `first_name` varchar(100) NOT NULL,
  `last_name` varchar(100) NOT NULL,
  `department` varchar(100) NOT NULL,
  `designation` varchar(100) NOT NULL,
  PRIMARY KEY (`faculty_id`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=23 ;

--
-- Dumping data for table `faculty`
--

INSERT INTO `faculty` (`faculty_id`, `exam_id`, `first_name`, `last_name`, `department`, `designation`) VALUES
(11, 111111, 'ram', 'prakash', 'cs', 'Ass. Professor'),
(22, 222222, 'ramesh', 'jain', 'maths', 'professor');

-- --------------------------------------------------------

--
-- Table structure for table `student`
--

CREATE TABLE IF NOT EXISTS `student` (
  `student_id` int(11) NOT NULL AUTO_INCREMENT,
  `first_name` varchar(100) NOT NULL,
  `last_name` varchar(100) NOT NULL,
  PRIMARY KEY (`student_id`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=105 ;

--
-- Dumping data for table `student`
--

INSERT INTO `student` (`student_id`, `first_name`, `last_name`) VALUES
(101, 'ravi', 'jain'),
(102, 'pankaj', 'kapoor'),
(103, 'reena', 'rai'),
(104, 'pankaj', 'namdeo');
