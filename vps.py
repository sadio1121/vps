sudo apt-get update
sudo apt install vsftpd
sudo cp /etc/vsftpd.conf /etc/vsftpd.conf.orig
sudo ufw status
sudo ufw allow 20/tcp
sudo ufw allow 21/tcp
sudo ufw allow 990/tcp
sudo ufw allow 40000:50000/tcp
sudo ufw status
sudo adduser sadio
sudo mkdir /home/sadio/ftp
sudo chown nobody:nogroup /home/sadio/ftp
sudo chmod a-w /home/sadio/ftp
sudo mkdir /home/sadio/ftp/files
sudo chown sadio:sadio /home/sadio/ftp/files
echo "vsftpd test file" | sudo tee /home/sadio/ftp/files/test.txt
