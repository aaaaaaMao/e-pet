pyinstaller.exe --clean -F -w --icon=app/favicon.ico app/main.py
Copy-Item -Path "app/img/*" -Destination "dist/img" -Recurse