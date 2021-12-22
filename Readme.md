``` bash
git clone https://github.com/ACCS-R03TE4A/Service-to-record-outdoor-temperature.git
cd Service-to-record-outdoor-temperature
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
chmod +x start.sh
cp ACCS.service /etc/systemd/system
systemctl daemon-reload
systemctl enable ACCS
systemctl start ACCS
systemctl status ACCS
```
- APIキーを環境変数に登録しておくこと
