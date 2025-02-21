from src.app import create_app
from src.config.server import Server_conf

app = create_app()

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int(Server_conf.SERVER_PORT))