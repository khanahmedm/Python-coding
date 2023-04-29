# Microsoft ODBC driver 18 for Ubuntu

## Perform the following steps:

sudo su
curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -

curl https://packages.microsoft.com/config/ubuntu/$(lsb_release -rs)/prod.list > /etc/apt/sources.list.d/mssql-release.list

exit

sudo apt-get update

sudo ACCEPT_EULA=Y apt-get install -y msodbcsql18

#### optional: for bcp and sqlcmd

sudo ACCEPT_EULA=Y apt-get install -y mssql-tools18

echo 'export PATH="$PATH:/opt/mssql-tools18/bin"' >> ~/.bashrc

source ~/.bashrc

#### optional: for unixODBC development headers

sudo apt-get install -y unixodbc-dev


#### Complete details and script is available <a href="https://learn.microsoft.com/en-us/sql/connect/odbc/linux-mac/installing-the-microsoft-odbc-driver-for-sql-server?view=sql-server-ver15&tabs=ubuntu18-install%2Calpine17-install%2Cdebian8-install%2Credhat7-13-install%2Crhel7-offline">here</a>

Update Ubuntu:

sudo apt-get update

Install pyodbc:

pip install pyodbc
