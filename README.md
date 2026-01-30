<h1>Asset Management Addon - Odoo 19</h1>
<p><strong>Custom asset tracking module for Odoo 19 Community Edition</strong></p>

<h2>⚠️ Requirements</h2>
<ul>
<li>Odoo 19 Community Edition</li>
<li>Employees module (must be installed first)</li>
<li>Ubuntu/Linux Mint</li>
<li>Python 3.10+</li>
<li>PostgreSQL</li>
</ul>

<h2>🚀 Quick Installation</h2>

<h3>1. Clone Odoo</h3>
<pre><code>git clone https://github.com/odoo/odoo.git --branch 19.0 --depth 1
cd odoo</code></pre>

<h3>2. Setup Addon Directory</h3>
<pre><code>mkdir myAddon
# Place your 'asset' module inside myAddon/</code></pre>

<h3>3. Create odoo.conf</h3>
<pre><code>[options]
addons_path = addons,myAddon
admin_passwd = admin
db_host = False
db_port = False
db_user = odoo
db_password = False</code></pre>

<h3>4. Install Dependencies</h3>
<pre><code>python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt</code></pre>

<h3>5. Run Odoo</h3>
<pre><code>./odoo-bin -c odoo.conf</code></pre>
<p>Access: <code>http://localhost:8069</code></p>

<h2>📦 Installation Order</h2>
<ol>
<li>Install <strong>Employees</strong> module</li>
<li>Install <strong>Asset</strong> module</li>
</ol>

<h2>⚠️ Notes</h2>
<ul>
<li>Works only with Odoo 19 Community Edition</li>
<li>PostgreSQL must be running</li>
<li>Addon path must include 'myAddon'</li>
</ul>