from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)

persons = []

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/registransts')
def registransts():
    '''CSV
    with open("registered.csv", mode="r") as file:
        persons = list(csv.reader(file))
    '''
    '''TXT file'''
    with open("registered.txt", mode="r") as file:
        persons = list(file.readlines())
    return render_template("registered.html", persons=persons)

@app.route('/register', methods=["POST"])
def register():
    if not request.form.get("name") or not request.form.get("sport"):
        return render_template("failure.html")
    '''TXT file'''
    with open("registered.txt",  mode="a") as file:
        string = f"{request.form.get('name')} like {request.form.get('sport')}\n"
        file.write(string)
    '''CSV
    with open("registered.csv", mode="a") as file:
        writer = csv.writer(file)
        writer.writerow((request.form.get('name'), request.form.get('sport')))
    '''
    return render_template("success.html")


if __name__ == '__main__':
    app.run(debug=True)