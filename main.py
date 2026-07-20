import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Welcome</title>
        <style>
            body{
                margin:0;
                display:flex;
                justify-content:center;
                align-items:center;
                height:100vh;
                background:#111;
                color:white;
                font-family:Arial,sans-serif;
            }
            h1{
                font-size:50px;
            }
        </style>
    </head>
    <body>
        <h1>Welcome To This Site</h1>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
