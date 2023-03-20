from flask import Flask, render_template, request
import pickle

FILE = "model_0.pickle"
model= pickle.load(open(f"{FILE}", "rb"))

def calc_expected(model, param):
    intercept = model.intercept_
    coef = list(model.coef_[0])

    effects = [coef * param for coef, param in zip(coef, param)]
    effects_sum = sum(effects)

    return float(intercept + effects_sum)


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("app.html", expectancy=0)

@app.route("/handle", methods=['POST'])
def handle_data():
    genetic = float(request.form['genetic'])
    length = float(request.form['length'])
    mass = float(request.form['mass'])
    exercise = float(request.form['exercise'])
    smoking = float(request.form['smoking'])
    alcohol = float(request.form['alcohol'])
    sugar = float(request.form['sugar'])

    BMI = mass / ((length/100) **2)
    BMI_under = 0 if BMI > 18.5 else (18.5 - BMI)
    BMI_over = 0 if BMI < 25 else (BMI - 25)

    parameters = [genetic, length, mass, exercise, smoking, alcohol, sugar, BMI_under, BMI_over]

    expectancy = calc_expected(model, parameters)

    return render_template("app.html", expectancy=expectancy)


