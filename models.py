from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Departamento(db.Model):
    __tablename__ = "departamento"

    codigo = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    sigla = db.Column(db.String(10), nullable=False)

    colaboradores = db.relationship(
        "Colaborador",
        backref="departamento",
        lazy=True,
        cascade="all, delete"
    )

    def to_dict(self):
        return {
            "codigo": self.codigo,
            "nome": self.nome,
            "sigla": self.sigla
        }


class Colaborador(db.Model):
    __tablename__ = "colaborador"

    matricula = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    salario = db.Column(db.Numeric(10, 2))
    email = db.Column(db.String(150))
    endereco = db.Column(db.String(200))

    codigo_dp = db.Column(
        db.Integer,
        db.ForeignKey("departamento.codigo"),
        nullable=False
    )

    def to_dict(self):
        return {
            "matricula": self.matricula,
            "nome": self.nome,
            "salario": float(self.salario) if self.salario else None,
            "email": self.email,
            "endereco": self.endereco,
            "codigo_dp": self.codigo_dp,
            "departamento": self.departamento.nome if self.departamento else None
        }
