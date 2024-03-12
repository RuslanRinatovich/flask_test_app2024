import os

from flask import Flask, url_for

app = Flask(__name__)


@app.route("/")
def index():
    return f'''<h2>картинка 1</h2>
        <p>
                    <img src="{url_for('static', filename='img/2.jpeg')}"
               alt="здесь должна была быть картинка, но не нашлась" width="600">
               </p>
               <h2>картинка 1</h2>
               <p>
               <img src="{url_for('static', filename='img/1.jpg')}"
               alt="здесь должна была быть картинка, но не нашлась" width="600">  </p>
               '''


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)