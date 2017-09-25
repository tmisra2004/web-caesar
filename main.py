from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
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
                textarea {
                    margin: 10px 0;
                    width: 540px;
                    height: 120px;
                }
            </style>
        </head>
        <body>
            <form action="/" method="POST">
                <label>
                    Rotate by: <input type="text" value="0" name="rot" />
                    <p>
                    <textarea name="text"></textarea>
                    <br />
                </label>
                <input type="submit" value="Submit Query" />
            </form>
        """
@app.route("/")
def index():
    return form

@app.route("/", methods=['POST'])
def encrypt(rot, text):
    rotated_by = int(rot)
    text_to_encrypt = text
    encrypted_text = rotate_string(text_to_encrypt, rotated_by)
    return "<h1>" + encrypted_text + "</h1>"

    



app.run()