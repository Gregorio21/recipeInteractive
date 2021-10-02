net stop MSSQLSERVER
net start MSSQLSERVER
cd /d %~dp0
cd mysite
python manage.py runserver
pause