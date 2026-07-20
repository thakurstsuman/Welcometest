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

# Vercel ke liye
app = app
