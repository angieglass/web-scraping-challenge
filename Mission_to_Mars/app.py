from flask import Flask, render_template
import pymongo


app = Flask(__name__)
conn = 'mongodb://localhost:27017'


@app.route('/')
def index():
    # Store the entire team collection in a list


    # Return the template with the teams list passed in
    return render_template('index.html', )

if __name__ == "__main__":
    app.run(debug=True)
