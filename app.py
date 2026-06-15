from flask import Flask, render_template
from config import Config
from models import db, Departamento, Colaborador
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/departamentos")
def listar_departamentos():

    departamentos = Departamento.query.all()

    return render_template(
        "departamentos.html",
        departamentos=departamentos
    )


@app.route("/colaboradores")
def listar_colaboradores():

    colaboradores = Colaborador.query.all()

    return render_template(
        "colaboradores.html",
        colaboradores=colaboradores
    )


@app.route("/relatorio-colaboradores")
def relatorio_colaboradores():

    colaboradores = Colaborador.query.all()

    resultado = []

    for colaborador in colaboradores:
        resultado.append({
            "matricula": colaborador.matricula,
            "nome": colaborador.nome,
            "salario": float(colaborador.salario) if colaborador.salario else None,
            "email": colaborador.email,
            "endereco": colaborador.endereco,
            "departamento": colaborador.departamento.nome,
            "sigla_departamento": colaborador.departamento.sigla
        })

    return resultado


@app.route("/relatorio-departamentos")
def relatorio_departamentos():

    departamentos = Departamento.query.all()

    resultado = []

    for departamento in departamentos:
        resultado.append({
            "codigo": departamento.codigo,
            "nome": departamento.nome,
            "sigla": departamento.sigla,
            "total_colaboradores": len(departamento.colaboradores)
        })

    return resultado


if __name__ == "__main__":
    app.run(debug=True)