#!/bin/bash

#Install python
sudo apt-get update 
sudo apt-get install python3

#Install Pip
sudo apt-get install python3-pip

#Install requeriments.txt pip
pip3 install -r requeriments.txt

#Add permissions
sudo chmod 777 /var/log

#Add cron
crontab -l > mycron
echo "*/32 * * * * python3 $(pwd)/main.py" >> mycron
crontab mycron
rm mycron

# Execute server cleaner 
python3 $(pwd)/main.py