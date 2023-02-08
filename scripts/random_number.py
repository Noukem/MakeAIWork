weight = float(input(85))
height = float(input(1.72))


BMI = (weight/(height**2))

if BMI <18.5:
    print("Underweight")

if BMI >=18.5 and BMI <25:
    print("Normal")

if BMI >=25 and BMI <30:
    print("Overweight")

if BMI >=30:
    print("Obesity")