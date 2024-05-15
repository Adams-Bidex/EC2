def bmi(x):
    if x < 18.5:
        return 'Under Weight'
    elif x < 24.5:
        return 'Normal Weight'
    elif x < 29.5:
        return 'Overweight'
    else:
        return 'Obese'