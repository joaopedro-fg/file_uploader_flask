from flask import Flask, render_template, request
import os
app = Flask(__name__)
wsgi_app = app.wsgi_app
@app.route('/', methods =   ["GET","POST"])
def hello():
    if request.method == "POST":
        file = request.files["arquivo"]
        file.save(os.path.join("uploads",file.filename))
        return render_template("upload.html", message = "Arquivo enviado com sucesso")
    return render_template("upload.html",message = "Envie arquivos")
if __name__ == '__main__':
    app.debug = True
    app.run()