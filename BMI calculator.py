height=float(input("What is your height in meters: "))
weight=float(input("What is your weight in kilograms: "))
height1 = height * height
BMI=(weight/height1)
if BMI >= 30:
    print("You are OBESE")
elif BMI < 30 and BMI >= 25:
    print("you are OVERWEIGHT (haha, loser)")
elif BMI < 25 and BMI >= 18:
    print("You are perfect")
else:
    print("You are underweight gain idiot")
print("your BMI is", BMI)
