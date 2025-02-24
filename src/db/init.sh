#!/bin/bash

# Update package list
sudo apt-get update

# Install PostgreSQL
sudo apt-get install -y postgresql postgresql-contrib

# Start PostgreSQL service
sudo service postgresql start

# Switch to postgres user and create database and user
sudo -u postgres psql <<EOF

CREATE DATABASE text2sql;
ALTER USER postgres WITH PASSWORD 'postgres';
\c text2sql
EOF

echo "PostgreSQL has been installed and configured:"
echo "Database: text2sql"
echo "User: postgres"
echo "Password: postgres"
echo "To connect to the database, use: psql -U postgres -d text2sql"
