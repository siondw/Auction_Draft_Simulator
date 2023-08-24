from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('welcome.html')  # Render the welcome.html template

@app.route('/draft')
def draft():
    return render_template('draft.html')


if __name__ == '__main__':
    app.run(debug=True)
