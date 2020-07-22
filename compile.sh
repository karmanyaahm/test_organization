#!/bin/bash
pyinstaller --onefile \
-n "File Organizer" \
--paths .venv/lib/python3.8/site-packages/ \
--paths .venv/lib64/python3.8/site-packages/ \
--hidden-import packaging.requirements \
--hidden-import google-api-python-client \
--hidden-import google-auth-httplib2 \
--hidden-import google-auth-oauthlib \
--hidden-import appdirs \
--add-data .venv/lib/python3.8/site-packages/google_api_python_client-1.10.0.dist-info/*:google_api_python_client-1.10.0.dist-info \
main.py 
