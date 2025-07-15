from Server.app import create_app, db

# This exposes the app to Flask CLI (e.g., flask run, flask db migrate)
app = create_app()