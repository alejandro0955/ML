from flask import Flask, render_template
import pandas as pd

df = pd.read_csv('results.csv')
names = df["Name"].values
difficulties = df["Difficulty"]
languages = df["Language"]
links = df["Link"]

data = []
for i in range(len(names)):
    entry = dict(name=names[i], language=languages[i], link=links[i], difficulty=difficulties[i])
    data.append(entry)

print(data)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('/index.html')

name='test'

@app.route('/results')
def results():
    return render_template('/results.html', results=data)

@app.route('/aboutus')
def aboutus():
    return render_template('/aboutus.html')


# if __name__ == '__main__':
#     app.run()