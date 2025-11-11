# Name- Anupam Kumar Singh, Date-10/11/25 ,Title- DAILY CALORIE TRACKER
print("Welcome, This is a Python-Based tool for quick and simple way to monitor \nyour daily calorie intake.")



#ALL FUNCTIONS HERE
def do_you_want_permission(question_prompt):
    while True:
        user_input = input(f"{question_prompt} (yes/no)? - ").lower().strip()
        if (user_input == "yes"):
            return True
        elif (user_input == "no"):
            return False
        else:
            print("Please enter a valid answer (Yes or No)")

def calc_avg_calorie():
    avg_calorie = calorie_sum / num_MEALS
    rounded_avg_calorie = round(avg_calorie,2)
    return rounded_avg_calorie



Meal = []
Calories = []
num_MEALS = int(input("Enter the number of meals you want to add - "))
for i in range(1,num_MEALS + 1):
    Meal_name = input("Enter the name of your meal - ")
    Meal.append(Meal_name)
    calorie_amt = float(input("Enter the amount of your calorie intake - "))
    Calories.append(calorie_amt)



calorie_sum = 0
for p in Calories:
    calorie_sum += p
print("Total amount of your calorie intake is - ", float(calorie_sum))



if do_you_want_permission("Do you want to see the average calories per meal?"):
    print("Calculating your data...") 
    print(calc_avg_calorie())
else:
    print("Action cancelled")



#daily calorie limit according to google it was 3000 for an avg healthy human so i set it to this
daily_limit = 3000



if do_you_want_permission("Do you want to set your own daily calorie limit?"):
    daily_limit = float(input("Enter your daily calorie limit: "))
    print("Daily calorie limit Set to - ",daily_limit)
else:
    print("Using default daily calorie limit of 3000.")
    daily_limit = 3000



if calorie_sum > daily_limit:
    print("Your calorie intake for today exceeded your daily limit!!!")
else:
    print("Your calorie intake for today is in your daily limit.")



print("Meal name\tCalories"  )
print("--------------------------")
print(f"{Meal[0]}\t{Calories[0]}")
for j in range(1,num_MEALS):
    print(f"{Meal[j]}\t\t{Calories[j]}")
print(f"Total calorie\t{calorie_sum}")
print(f"Average calorie\t{calc_avg_calorie()}")

if do_you_want_permission("Do you want to save todays report"):
    print("Proceeding with action")
    filename = input("Enter the name as of the file to be created! - ").strip
    Date = input("Enter todays date in any format - ").strip
    with open(filename + Date, "a") as report:
        report.write(f"{Date}\n")
        report.write("Meal name\tCalories\n")
        report.write("--------------------------\n")
        report.write(f"{Meal[0]}\t{Calories[0]}\n")
        for j in range(1, num_MEALS):
            report.write(f"{Meal[j]}\t\t{Calories[j]}\n")
        report.write(f"Total calorie\t{calorie_sum}\n")
        report.write(f"Average calorie\t{calc_avg_calorie()}\n")
else:
    print("Action Cancelled!")