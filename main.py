from flask import Flask, render_template, redirect

app = Flask(__name__)

dadesPosts = [
    {
        "autor": "Autor1",
        "titol": "Titol post 1",
        "contingut": "Text del post 1",
        "data": "19:18 - 8 de maig del 2024"
    }, {
        "autor": "Autor2",
        "titol": "Titol post 2",
        "contingut": "Text del post 2",
        "data": "19:20 - 8 de maig del 2024"
    }

]


@app.route("/")
@app.route("/inici")
def pagina_inici():
    return render_template("inici.html", titolPagina="sss", variable_dades=dadesPosts)


@app.route("/info")
def pagina_info():
    return render_template("info.html")


@app.route("/tarifas")
def pagina_tarifas():
    return render_template("tarifas.html")


@app.route("/contacte")
def pagina_contacte():
    return render_template("contacte.html")


@app.route("/documentacio")
def pagina_documentacio():
    return render_template("documentacio.html")

@app.route("/accesoempresas")
def pagina_empresas():
    return render_template("accesoempresas.html")


@app.errorhandler(404)
def pagina_no_trobada(e):
    return render_template('error.html'), 404


if __name__ == '__main__':
    app.run(debug=True)
