# Troubleshooting Microsoft ODBC connection

Below are some of the links the helped with different errors that could happen when connection to MS SQL Server from a python program.

### Error 1:

ImportError: libodbc.so.2: cannot open shared object file: No such file or directory

This happens when ubuntu environment does not have odbc library.

Follow the steps mentioned in the link:

https://stackoverflow.com/questions/43417886/pyodbc-error-while-running-application-within-a-container


### Error 2:

[unixODBC][Driver Manager]Can't open lib 'ODBC Driver 18 for SQL Server'

This issue happens when microsoft odbc drivers are not installed.

Follow the steps in the below links:

https://github.com/mkleehammer/pyodbc/issues/717

https://learn.microsoft.com/en-us/sql/connect/odbc/linux-mac/installing-the-microsoft-odbc-driver-for-sql-server?view=sql-server-ver15&tabs=alpine18-install%2Calpine17-install%2Cdebian8-install%2Credhat7-13-install%2Crhel7-offline


### Error 3:

pyodbc.OperationalError: ('HYT00', '[HYT00] [Microsoft][ODBC Driver 18 for SQL Server]Login timeout expired

This issue happens where TCP connection is not enabled in SQL Server Network Configuration.

Use below links to correctly configure TCP:

https://learn.microsoft.com/en-us/answers/questions/1162115/pyodbc-operationalerror-(hyt00-(hyt00)-(microsoft)

https://stackoverflow.com/questions/54818373/how-do-i-connect-to-a-local-windows-sql-server-instance-from-wsl

https://webfiles.blackbaud.com/files/support/infinityinstaller/content/installermaster/tkenablenamedpipesandtcpipconnections.htm


### Error 4:

pyodbc.OperationalError: ('08001', '[08001] [Microsoft][ODBC Driver 18 for SQL Server]SSL Provider: [error:1416F086:SSL routines:tls_process_server_certificate:certificate verify failed:self signed certificate]

This issue happens when encryption is enabled in the connection string.

The workaround is to specify Encrypt=no in the connection string.

Use the below link for more details:

https://github.com/mkleehammer/pyodbc/issues/610
