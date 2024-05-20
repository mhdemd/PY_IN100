def evaluate_halth(age, weight, height):
    ''' Calculating Body Mass Index (BMI) '''
    bmi = weight / (height ** 2)

    # Evaluating health status based on BMI
    if bmi < 18.5:
        return "Needs attention: Underweight"
    elif 18.5 <= bmi <= 24.9:
        return "Healthy: Normal weight"
    else:
        return "Needs treatment: Overweight"
    
# Example usage
age = float(input("Please enter your age: "))
weight = float(input("Please enter your weight in kilograms: "))
height = float(input("Please enter your height in meters: "))
result = evaluate_halth(age, weight, height)
print("Your health status:", result)

# print(evaluate_halth.__doc__)