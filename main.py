from flask import Flask, render_template
import config


app = Flask(__name__)
app.config.from_object(config)


@app.route('/index')
def index_page():
    return render_template('index.html')


@app.route('/compute_time')
def compute_time_page():
    return render_template('compute_time.html')


@app.route('/')
def login():
    return  render_template('login.html')


if __name__ == "__main__":
    app.run()
