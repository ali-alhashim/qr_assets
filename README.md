QR Assets for Odoo 19 Community
This addon is built for Odoo 19 Community Edition and requires the Employees module to be installed first.

📋 Requirements
Linux (Ubuntu or Linux Mint recommended)
Python 3.10+
PostgreSQL
Git
Virtual Environment (venv)
🚀 Installation Guide
Step 1: Download Odoo 19 Community
Clone the Odoo repository and navigate into the directory:

git clone https://github.com/odoo/odoo.git --branch 19.0 --depth 1cd odoo
Step 2: Create Addons Directory
Create a custom directory for your addons:

bash

mkdir myAddon
Step 3: Create Odoo Configuration File
Create a file named odoo.conf with the following configuration:

ini

[options]
addons_path = addons,myAddon
admin_passwd = admin
db_host = False
db_port = False
db_user = odoo
db_password = False
Step 4: Create Python Virtual Environment
Set up and activate the virtual environment:

bash

python3 -m venv venv
source venv/bin/activate
Step 5: Install Odoo Requirements
First, upgrade pip and install Python dependencies:

bash

pip install --upgrade pip
pip install -r requirements.txt
Next, ensure OS-level dependencies are installed:

bash

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
Step 6: Run Odoo
Start the Odoo server using your configuration file:

bash

./odoo-bin -c odoo.conf
Step 7: Install Required Modules
Follow these steps within the Odoo Interface:

Open Apps.
Enable Developer Mode.
Search for Employees.
Install the Employees module first.
Search for Asset.
Install the Asset addon.
⚠️ Important
Note: The Employees module must be installed before installing the Asset addon.

📝 Additional Notes
This addon works only with Odoo 19 Community.
Tested on Ubuntu & Linux Mint.
Make sure PostgreSQL is running before starting Odoo.