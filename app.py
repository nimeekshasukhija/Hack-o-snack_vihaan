from flask import Flask, render_template, request
from model import analyze_pedigree
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    child_data = {
        'age': request.form['age'],
        'sleep': request.form['sleep'],
        'nutrition': request.form['nutrition'],
        'vaccination': request.form['vaccination'],
        'symptoms': request.form['symptoms']
    }

    ancestors = []
    for i in range(1, 4):
        ancestor = {
            'relation': request.form[f'relation{i}'],
            'disease': request.form[f'disease{i}'],
            'symptoms': request.form[f'symptoms{i}'],
            'status': request.form[f'status{i}'],
            'death_reason': request.form[f'death_reason{i}']
        }
        ancestors.append(ancestor)

    result_data = analyze_pedigree(child_data, ancestors)
    return render_template('result.html', result=result_data)

if __name__ == '__main__':
    app.run(debug=True)
