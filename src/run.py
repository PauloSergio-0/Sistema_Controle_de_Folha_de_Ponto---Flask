from settings.flask_app import app_config

if __name__ == "__main__":
    app = app_config()
    app.run(host = "0.0.0.0", port = 5050, debug =True)