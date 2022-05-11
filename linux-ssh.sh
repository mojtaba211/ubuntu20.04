#linux-run.sh LINUX_USER_PASSWORD NGROK_AUTH_TOKEN LINUX_USERNAME LINUX_MACHINE_NAME
#!/bin/bash
# /home/runner/.ngrok2/ngrok.yml
sudo apt update
sudo useradd -m $LINUX_USERNAME
sudo adduser $LINUX_USERNAME sudo
echo "$LINUX_USERNAME:$LINUX_USER_PASSWORD" | sudo chpasswd
sed -i 's/\/bin\/sh/\/bin\/bash/g' /etc/passwd
sudo hostname $LINUX_MACHINE_NAME

if [[ -z "$NGROK_AUTH_TOKEN" ]]; then
  echo "Please set 'NGROK_AUTH_TOKEN'"
  exit 2
fi

if [[ -z "$LINUX_USER_PASSWORD" ]]; then
  echo "Please set 'LINUX_USER_PASSWORD' for user: $USER"
  exit 3
fi

echo "### Install ngrok ###"
id
curl ipv4.icanhazip.com
wget https://chromedriver.storage.googleapis.com/101.0.4951.41/chromedriver_linux64.zip
unzip chromedriver_linux64.zip
pip install selenium
echo "remove config chrome ..."
sudo rm /usr/bin/google-chrome
screen -dmS MySession
screen -S MySession -p 0 -X stuff "python test.py\n"


#wget -q https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-386.zip
#unzip ngrok-stable-linux-386.zip
#chmod +x ./ngrok
pwd
ls
echo "### Update user: $USER password ###"
echo -e "$LINUX_USER_PASSWORD\n$LINUX_USER_PASSWORD" | sudo passwd "$USER"
id
echo "root:123456@" | sudo chpasswd
echo "### Start ngrok proxy for 22 port ###"


rm -f .ngrok.log
#./ngrok authtoken "$NGROK_AUTH_TOKEN"
#./ngrok tcp 22 --log ".ngrok.log" &
#sudo apt-get install keyboard-configuration
#sudo DEBIAN_FRONTEND=noninteractive apt-get install keyboard-configuration -y
#sudo apt install -y xfce4 xfce4-goodies > /dev/null 2>&1
#sudo apt install firefox -y
#sudo apt-get install -y xrdp
#sudo apt-get install -y xfce4-terminal
#sudo apt-get install xrdp xorg -y
#sudo apt-get install xserver-xorg-core -y
#echo xfce4-session >~/.xsession
#sudo service xrdp start
sudo apt install screen wget unzip nano curl ssh -y
sleep 10

#sudo rm /usr/bin/google-chrome
#sudo mv google-chrome /usr/bin/google-chrome

#echo xfce4-session >~/.xsession
HAS_ERRORS=$(grep "command failed" < .ngrok.log)
#sudo service xrdp start
#echo xfce4-session >~/.xsession

if [[ -z "$HAS_ERRORS" ]]; then
  echo ""
  echo "=========================================="
  #echo "To connect: $(grep -o -E "tcp://(.+)" < .ngrok.log | sed "s/tcp:\/\//ssh $USER@/" | sed "s/:/ -p /")"
 # echo "or conenct with $(grep -o -E "tcp://(.+)" < .ngrok.log | sed "s/tcp:\/\//ssh (Your Linux Username)@/" | sed "s/:/ -p /")"
  echo "=========================================="
else
  echo "$HAS_ERRORS"
  exit 4
fi
