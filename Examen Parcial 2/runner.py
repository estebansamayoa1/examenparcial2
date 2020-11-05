import yaml
from flask import Flask, render_template, request, url_for, redirect
from jinja2 import Template, Environment, FileSystemLoader

file_loader=FileSystemLoader('templates')
env=Environment(loader=file_loader)

app=Flask(__name__)
with open('backend.yaml') as f:
    info=yaml.load(f, Loader=yaml.FullLoader)


@app.route('/', methods=['GET', 'POST'])
def index():
    template = env.get_template('palabra.html')
    if request.method == 'POST':
        palabra = request.form['palabra']
        print (f'{palabra}')
        palabra = request.form['palabra']
        reverse=palabra[::-1]
        upper=palabra.upper()
        lower=palabra.lower()
    return template.render(palabra=palabra, reverse=reverse, upper=upper, lower=lower)





if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=true)
