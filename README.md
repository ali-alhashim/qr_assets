Custom addon for Odoo 19 Community Edition.

[!IMPORTANT]
This addon requires the Employees module and must be installed after it.

Requirements

[!NOTE]
Tested on Ubuntu and Linux Mint

Linux (Ubuntu / Linux Mint)

Python 3.10+

PostgreSQL

Git

Python venv

Installation
1. Download Odoo 19 Community
git clone https://github.com/odoo/odoo.git --branch 19.0 --depth 1
cd odoo

2. Create Custom Addons Directory
mkdir myAddon


[!TIP]
Place your addon inside the myAddon folder.

Example structure:

odoo/
├── addons/
├── myAddon/
│   └── asset/
│       ├── __manifest__.py
│       ├── models/
│       ├── views/
│       └── security/
└── odoo-bin

3. Create Odoo Configuration File

Create odoo.conf:

[options]
addons_path = addons,myAddon
admin_passwd = admin
db_host = False
db_port = False
db_user = odoo
db_password = False

4. Create Python Virtual Environment
python3 -m venv venv
source venv/bin/activate

5. Install Dependencies
pip install --upgrade pip
pip install -r requirements.txt


Install OS dependencies:

sudo apt update
sudo apt install -y \
  build-essential \
  python3-dev \
  libpq-dev \
  libldap2-dev \
  libsasl2-dev \
  libssl-dev \
  node-less \
  npm

6. Run Odoo
./odoo-bin -c odoo.conf


Open in browser:

http://localhost:8069

Module Installation Order

[!IMPORTANT]
You must install modules in this order:

Open Apps

Enable Developer Mode

Search for Employees

Install Employees

Search for Asset

Install MyAddon (Asset)

Notes

[!WARNING]
This addon works only with Odoo 19 Community Edition

PostgreSQL must be running before starting Odoo

Make sure myAddon is included in addons_path