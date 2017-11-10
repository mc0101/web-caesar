from flask import Flask

app = Flask(__name__)
app.config['DEBUG'] = True

codeform = """
<!DOCTYPE html>
<html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }

            textarea{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
        </style>
    </head>
    <body>
        <form action="/rotateby" method="post">
            <label for="rot">
            Rotate by
        <input type="text" id="rot" name="rot" value="0">
        </label>
        <textarea name="text" form="rot">
        </textarea>
        <input type="submit" value="Submit">
    </body>
</html>
"""

@app.route("/")
def index():
    return codeform


app.run()    