-- ============================================================
--  Portfolio Website - MySQL Database Schema
--  Student: Padmapriya R
-- ============================================================
--  Run this file in MySQL to set up the database:
--    mysql -u root -p < database.sql
-- ============================================================

-- Step 1: Create the database
CREATE DATABASE IF NOT EXISTS portfolio_db
    CHARACTER SET utf8mb4
    COLLATE utf8mb4_unicode_ci;

-- Step 2: Use the database
USE portfolio_db;

-- ── Table: contacts ──────────────────────────────────────────
-- Stores messages submitted via the Contact Form
CREATE TABLE IF NOT EXISTS contacts (
    id              INT AUTO_INCREMENT PRIMARY KEY,  -- Unique ID for each message
    name            VARCHAR(100) NOT NULL,           -- Sender's full name
    email           VARCHAR(150) NOT NULL,           -- Sender's email address
    message         TEXT NOT NULL,                  -- Message content
    submitted_at    DATETIME DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of submission
    is_read         BOOLEAN DEFAULT FALSE,           -- Mark as read/unread (optional admin use)

    -- Indexes for faster lookups
    INDEX idx_email (email),
    INDEX idx_submitted_at (submitted_at)
);

-- ── Table: projects (optional - for dynamic project data) ────
-- You can populate this if you want to serve projects dynamically
CREATE TABLE IF NOT EXISTS projects (
    id              INT AUTO_INCREMENT PRIMARY KEY,
    title           VARCHAR(200) NOT NULL,
    description     TEXT,
    tech_stack      VARCHAR(300),         -- e.g. "Python, Flask, MySQL"
    github_url      VARCHAR(300),
    image_filename  VARCHAR(200),
    display_order   INT DEFAULT 0,
    created_at      DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- ── Table: certifications (optional - for dynamic cert data) ─
CREATE TABLE IF NOT EXISTS certifications (
    id              INT AUTO_INCREMENT PRIMARY KEY,
    title           VARCHAR(200) NOT NULL,
    issuer          VARCHAR(200),
    issue_date      DATE,
    credential_url  VARCHAR(300),
    display_order   INT DEFAULT 0
);

-- ── Sample Data: Projects ─────────────────────────────────────
INSERT INTO projects (title, description, tech_stack, github_url, display_order) VALUES
(
    'Student Portfolio Website',
    'A full-stack personal portfolio website built with Flask and MySQL to showcase skills, projects, and certifications.',
    'HTML, CSS, JavaScript, Python, Flask, MySQL',
    'https://github.com/ppadmapriya807-cell/portfolio',
    1
),
(
    'Library Management System',
    'A desktop application to manage library books, members, and transactions with a clean GUI.',
    'Python, Tkinter, SQLite',
    'https://github.com/ppadmapriya807-cell/library-management',
    2
),
(
    'Weather Dashboard',
    'A responsive weather app fetching real-time data from OpenWeatherMap API with search and 5-day forecast.',
    'HTML, CSS, JavaScript, REST API',
    'https://github.com/ppadmapriya807-cell/weather-dashboard',
    3
);

-- ── Sample Data: Certifications ───────────────────────────────
INSERT INTO certifications (title, issuer, issue_date, credential_url, display_order) VALUES
(
    'Python for Everybody',
    'Coursera / University of Michigan',
    '2024-03-15',
    'https://coursera.org/verify/example',
    1
),
(
    'Responsive Web Design',
    'freeCodeCamp',
    '2024-06-01',
    'https://freecodecamp.org/certification/example',
    2
),
(
    'SQL and Relational Databases',
    'IBM / Cognitive Class',
    '2024-08-10',
    'https://cognitiveclass.ai/courses/example',
    3
);

-- ── Verification Queries ──────────────────────────────────────
-- Run these to verify setup:
-- SHOW TABLES;
-- DESCRIBE contacts;
-- SELECT * FROM projects;
-- SELECT * FROM certifications;

-- ============================================================
--  End of Schema
-- ============================================================
