apt update
apt install -y firefox python3-pip
pip3 install selenium
wget https://github.com/mozilla/geckodriver/releases/download/v0.29.1/geckodriver-v0.29.1-linux64.tar.gz
tar -xf geckodriver-v0.29.1-linux64.tar.gz
python3 run.py
