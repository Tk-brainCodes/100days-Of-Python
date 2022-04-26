height = print(input("Enter your height in m:"));
weight = print(input("Enter your weight in kg:"));
BMI_Result = int(weight) / float(height) ** 2;

if BMI_Result < 18.5:
    print(f"You are underweight: {BMI_Result}");
elif BMI_Result < 25:
    print(f"Your weight is normal: {BMI_Result}")
elif BMI_Result > 30:
        print("you are overweight");
elif BMI_Result < 35:
    print("you are obessed");        
else: 
    print("you are clinically obessed");