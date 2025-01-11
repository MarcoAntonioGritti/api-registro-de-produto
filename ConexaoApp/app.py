from flask import Flask
from GET.rotas import rotas_get
from POST.rotas import rotas_post
from PUT.rotas import rotas_put
from DELETE.rotas import rota_delete

def criar_app():
    app = Flask(__name__)
    app.register_blueprint(rotas_get)
    app.register_blueprint(rotas_post)
    app.register_blueprint(rotas_put)
    app.register_blueprint(rota_delete)
    return app