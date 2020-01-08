from flask import Flask
import os

app = Flask(_name_)

@app.route("/")
def hello();
    return "Latihan membuat aplikasi menggunakan phyton+flask pada Docker!!"


if _name_ == "_main_":
    port = int(os.environ.get("PORT",5000))
    app.run(debug=True,host='0.0.0.0',port=port)
