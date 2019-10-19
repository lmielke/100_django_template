#!/bin/bash
cd /home
sudo apt -y update
sudo apt -y upgrade
sudo apt install -y python3-pip
sudo apt install build-essential libssl-dev libffi-dev python3-dev -y
sudo apt install apache2 -y
sudo apt install apache2-dev -y
sudo apt install nano
sudo apt install -y python3-venv
pip3 install mod_wsgi
python3 -m venv /home/100_django_template/venv
cd /home/100_django_template
source /home/100_django_template/venv/bin/activate
python -m pip install --upgrade pip
pip install --upgrade setuptools
sudo chown -R marvin:marvin /home/100_django_template
cd web_project
pip install -r /home/100_django_template/resources/requirements.txt
pip install mod_wsgi
sudo mkdir /etc/wsgi-port-80
sudo chown -R marvin:marvin /etc/wsgi-port-80
sudo groupadd  www-data
sudo adduser  www-data  www-data
sudo chown -R :www-data /home/100_django_template/web_project/media/
sudo chmod -R 775 /home/100_django_template/web_project/media/
sudo chown -R :www-data /home/100_django_template/web_project
sudo chmod 777 /home/100_django_template/web_project
sudo chown :www-data /home/100_django_template/web_project/100_django_template.sqlite3
sudo chmod 664 /home/100_django_template/web_project/100_django_template.sqlite3
python manage.py collectstatic
python manage.py runmodwsgi --server-root /etc/wsgi-port-80 --user www-data --group www-data --port 80 --url-alias /static static --url-alias /media media --setup-only
sudo apachectl stop
sudo /etc/wsgi-port-80/apachectl start
sudo cp /home/100_django_template/conf_files/sshd_config /etc/ssh/sshd_config
sudo systemctl restart sshd
sudo apt install ufw -y
y
sudo ufw default allow outgoing
sudo ufw default deny incoming
sudo ufw allow ssh
sudo ufw allow http/tcp
sudo ufw allow https/tcp
sudo ufw allow 3389
sudo ufw enable
y
sudo passwd marvin
Nihau_Ma1
Nihau_Ma1
netstat -nat | grep LISTEN
sudo ufw status
sudo /etc/wsgi-port-80/apachectl restart
sudo apt install xrdp
sudo apt remove lightdm
Y
sudo apt install xfce4
Y
sudo apt-get install xfce4-terminal tango-icon-theme
Y
echo xfce4-session > ~/.xsession
sudo apt install libexo-1-0
sudo apt install firefox
Y
sudo service xrdp restart
sudo /etc/wsgi-port-80/apachectl restart