from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Built by batch 1 under the guidance of Hari Prasad Sir ! '

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000)
