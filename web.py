from flask import Flask, request, render_template
from app import tm_api
import json

app = Flask(__name__)


@app.route('/form-example', methods=['GET', 'POST']) #allow both GET and POST requests
def form_example():
    if request.method == 'POST': #this block is only entered when the form is submitted
        date = request.form.get('date')
        location = request.form.get('location')
        category = request.form.get('category')
        radius = request.form.get('radius')
        lst = tm_api(date, location, category, radius)
##        return '''<h1>The date value is: {}</h1>
##                  <h1>The location value is: {}</h1>
##                  <h1>The category is: {}</h1>
##                  <h1>The max distances is: {}</h1>'''.format(date, location, category, radius)
        return render_template('index.html', lst=lst)
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
