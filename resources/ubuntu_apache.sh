#!/bin/bash
cd /home
mv -r 100_django_template 100_django_project
apt -y update
apt -y upgrade
apt install -y python3-pip
apt install build-essential libssl-dev libffi-dev python3-dev -y
apt install apache2 -y
apt install apache2-dev -y
apt install nano
apt install -y python3-venv
pip3 install mod_wsgi
python3 -m venv /home/100_django_project/venv
cd /home/100_django_project
source /home/100_django_project/venv/bin/activate
python -m pip install --upgrade pip
pip install --upgrade setuptools
chown -R marvin:marvin /home/100_django_project
cd web_project
pip install -r /home/100_django_project/resources/requirements.txt
pip install mod_wsgi
mkdir /etc/wsgi-port-80
chown -R marvin:marvin /etc/wsgi-port-80
groupadd  www-data
adduser  www-data  www-data
chown -R :www-data /home/100_django_project/web_project/media/
chmod -R 775 /home/100_django_project/web_project/media/
chown -R :www-data /home/100_django_project/web_project
chmod 777 /home/100_django_project/web_project
chown :www-data /home/100_django_project/web_project/100_django_project.sqlite3
chmod 664 /home/100_django_project/web_project/100_django_project.sqlite3
python manage.py collectstatic
python manage.py runmodwsgi --server-root /etc/wsgi-port-80 --user www-data --group www-data --port 80 --url-alias /static static --url-alias /media media --setup-only
apachectl stop
/etc/wsgi-port-80/apachectl start
cp /home/100_django_project/conf_files/sshd_config /etc/ssh/sshd_config
systemctl restart sshd
apt install ufw -y
ufw default allow outgoing
ufw default deny incoming
ufw allow ssh
ufw allow http/tcp
ufw allow https/tcp
ufw allow 3389
ufw enable
passwd marvin
Nihau_Ma1
Nihau_Ma1
netstat -nat | grep LISTEN
ufw status
/etc/wsgi-port-80/apachectl restart
apt install xrdp
apt remove lightdm
apt install xfce4
apt-get install xfce4-terminal tango-icon-theme
echo xfce4-session > ~/.xsession
apt install libexo-1-0
apt install firefox
service xrdp restart
/etc/wsgi-port-80/apachectl restart
rm -r 100_django_template