#!/bin/bash

# Be pretty
echo -e " "
echo -e " Amazon Web Service S3 Mysql Backup Script "
echo -e " "

# Basic variables
mysqluser="admin"
mysqlpass="invtus3r"
bucket="s3://staging-area-innovative/data_warehouse"

# Timestamp (sortable AND readable)
stamp=`date +"%s - %A %d %B %Y @ %H%M"`

# List all the databases and eliminate the default
databases=`mysql -h inno-ai-db-1.cpsxv0hr2fjp.us-west-2.rds.amazonaws.com -P 3306 -u admin -p$mysqlpass -e "SHOW DATABASES;" | tr -d "| " | grep -v "\(Database\|information_schema\|performance_schema\|mysql\|test\)"`

# Feedback
echo -e "Dumping to \e[1;32m$bucket/$stamp/\e[00m"

# Loop the databases
for db in $databases; do

  # Define our filenames
  filename="$db-$stamp.sql.gz"
  tmpfile="/tmp/$filename"
  object="$bucket/$stamp/$filename"

  # Feedback
  echo -e "\e[1;34m$db\e[00m"

  # Dump and zip
  echo -e "  creating \e[0;35m$tmpfile\e[00m"
  mysqldump -h inno-ai-db-1.cpsxv0hr2fjp.us-west-2.rds.amazonaws.com -u$mysqluser -p$mysqlpass --all-databases --triggers --routines --events "$db" | gzip -c > "$tmpfile"

  # Upload
  echo -e "  uploading..."
  s3cmd put "$tmpfile" "$object"

  # Delete
  rm -f "$tmpfile"

done;

# Jobs a goodun
echo -e "\e[1;32mJob completed\e[00m"
