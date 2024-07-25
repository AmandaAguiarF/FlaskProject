from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from models.employeeModel import db
from controllers.employeeController import employee_blueprint

app = Flask(__name__, template_folder="views")

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///employees.db' 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# Objeto que vai gerenciar as rotas, para não precisar fazer rota por rota
app.register_blueprint(employee_blueprint, url_prefix='/')

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)