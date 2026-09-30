@echo off
REM SQLite Database Inspector - Command Line Version
REM Windows'ta cmd ile çalışan basit database inceleme

echo.
echo ======================================
echo SQLite Database Inspection Tool
echo ======================================
echo.

REM Database bilgisini göster
echo Checking database: reservations.db
sqlite3 reservations.db ".mode column" ".headers on" "SELECT COUNT(*) as 'TOTAL RESERVATIONS' FROM reservations;"

echo.
echo ======================================
echo Database Schema
echo ======================================
echo.

sqlite3 reservations.db ".schema reservations"

echo.
echo ======================================
echo Sample Reservations (First 5)
echo ======================================
echo.

sqlite3 reservations.db ".mode column" ".headers on" "SELECT id, name, email, bungalow, status FROM reservations LIMIT 5;"

echo.
pause
