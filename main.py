from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>
<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}

            textarea{{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
        <form action="/encrypt" method="post">
            <label for="rot">
            Rotate by
        <input type="text" id="rot" name="rot" value="0">
        </label>
        <textarea name="text">{0}
        </textarea>
        <input type="submit" value="Submit">
        </form>
    </body>
</html>
"""

@app.route("/")
def index():
    return form.format("text")

@app.route("/encrypt", methods=["POST"])
def encrypt():
    rotation = request.form["rot"]
    rot = int(rotation)
    text = request.form["text"]
    codedmsg = rotate_string(text, rot)
    finalmsg = "<h1>" + codedmsg + "</h1>"
    return form.format(codedmsg)

app.run()    