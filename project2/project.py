""" Projekt o obliczaniu wskaźnika BMI"""
import sys
from prettytable import PrettyTable
import random
import sqlite3 as sql
import datetime
import matplotlib.pyplot as plt


def main():
    greeting()


def greeting():
    print()
    print("Enter the number depending on what you want to achieve.")
    print()
    myTable = PrettyTable(["Number", "Aiming"])
    myTable.add_row(["1", "if I have to calculate your BMI."])
    myTable.add_row(["2", "if I have to show you a sample random advice on how to lose weight / gain / maintain a good weight."])
    myTable.add_row(['3', 'if I have to show you 10 tips for "healthy living".'])
    myTable.add_row(["4", "if you want me to show you interesting charts about your health."])
    myTable.add_row(["5", "if you want to exit the program."])

    myTable.right_padding_width = 5
    myTable.align = "l"
    myTable.horizontal_char = "─"
    myTable.vertical_char = "│"

    print(myTable)
    print()

    try:
        ask = int(input("Welcome to the CS50 final project. Choose what I should do for you: ").strip())
        print()
        if ask not in [1, 2, 3, 4, 5]:
            raise ValueError
    except ValueError:
        sys.exit("Wrong numeric value entered.")
    else:
        if ask == 1:
            print(number_1())
            print()
            more()
        elif ask == 2:
            print(number_2())
            print()
            more()
        elif ask == 3:
            print(number_3())
            print()
            more()
        elif ask == 4:
            name = number_4()
            print()
            wykres(name)
            print()
            more()
        else:
            number_5()
            print()
            sys.exit()


def number_1(wsk=0):
    """BMI Calculator"""
    try:
        masa = input("Enter your body weight in kilograms: ").strip()
        if "kg" in masa:
            masa = masa.replace("kg", "")
        if "," in masa:
            masa = masa.replace(",", ".")
        masa = float(masa)

        wzrost = input("Enter your height in meters: ").strip()
        if "m" in wzrost:
            wzrost = wzrost.replace("m", "")
        if "," in wzrost:
            wzrost = wzrost.replace(",", ".")
        wzrost = float(wzrost)

    except ValueError:
        print("Podana nieprawidłowe wielkości. Wpisz je jeszcze raz.")
        pass
    else:
        bmi = masa/(wzrost*wzrost)
        bmi = round(bmi, 2)
        if wsk == 1:
            return masa, bmi
        print()
        myTable = PrettyTable(["Answer"])

        if bmi < 18.5:
            myTable.add_row([f"Your BMI is: {bmi}.\nYour Weight Status is Underweight 😢"])
            return myTable
        elif 18.5 <= bmi < 25:
            myTable.add_row([f"Your BMI is: {bmi}.\nYour Weight Status is Healthy Weight 🥳"])
            return myTable
        elif 25 <= bmi < 30:
            myTable.add_row([f"Your BMI is: {bmi}.\nYour Weight Status is Overweight 😢"])
            return myTable
        else:
            myTable.add_row([f"Your BMI is: {bmi}.\nYour Weight Status is Obesity 😭"])
            return myTable


def number_2():

    print("Enter the number depending on what you want to achieve.")
    print()
    print("1 if I have to show you a sample random advice on how to lose weight.")
    print("2 if I have to show you a sample random advice on how to gain weight.")
    print("3 if I have to show you a sample random advice on how to maintain a good weight.")
    print()

    try:
        number = input("What advice would you like to receive? ").strip()
        if number not in ["1", "2", "3"]:
            raise ValueError
        number = int(number)
    except ValueError:
        print("Podana nieprawidłowe wielkości. Wpisz je jeszcze raz.")
        pass
    else:
        print()
        if number == 1:
            liczba = random.randint(1, 13)
            advices = { 1:"Do not skip breakfast",
                       2:"Eat regular meals",
                       3:"Eat plenty of fruit and veg",
                       4:"Get more active",
                       5:"Drink plenty of water",
                       6:"Eat high fibre foods",
                       7:"Read food labels",
                       8:"Use a smaller plate",
                       9:"Do not ban foods",
                       10:"Do not stock junk food",
                       11:"Cut down on alcohol",
                       12:"Plan your meals"
            }
            myTable = PrettyTable(["Advice"])
            myTable.add_row([advices[liczba]])
            return myTable

        elif number == 2:
            liczba = random.randint(1, 14)
            advices = { 1:"Have an Extra Slice of Whole Grain Toast With Peanut Butter at Breakfast",
                       2:"Drink Whole Milk, 100\% Fruit Juice, or Vegetable Juice",
                       3:"Add Extra Cheese to an Omelet and Use an Extra Egg",
                       4:"Top Your Avocado Toast with an Egg",
                       5:"Slice an Apple and Serve With Nut Butter",
                       6:"Add Chopped Nuts, Oats, Fruit and Honey to Yogurt",
                       7:"Carry a Bag of Trail Mix for a Convenient Snack",
                       8:"Increase Protein Intake (and Calories) With Protein Bars",
                       9:"Use Sour Cream as a Go-To Topping",
                       10:"Eat Larger Portions of Starchy Vegetables Like Potatoes",
                       11:"Choose Creamed Soups Over Clear Soups",
                       12:"Add Cheese Sauces to Green Veggies",
                       13:"Eat Red Meat (and Choose Lean Cuts for a Healthy Heart)"
            }
            myTable = PrettyTable(["Advice"])
            myTable.add_row([advices[liczba]])
            return myTable

        else:
            liczba = random.randint(1, 11)
            advices = { 1:"Measure and Watch Your Weight",
                       2:"Limit Unhealthy Foods and Eat Healthy Meals",
                       3:"Take Multivitamin Supplements",
                       4:"Drink Water and Stay Hydrated, and Limit Sugared Beverages",
                       5:"Exercise Regularly and Be Physically Active",
                       6:"Reduce Sitting and Screen Time",
                       7:"Get Enough Good Sleep",
                       8:"Go Easy on Alcohol and Stay Sober",
                       9:"Find Ways to Manage Your Emotions",
                       10:"Use an App to Keep Track of Your Movement, Sleep, and Heart Rate",
            }
            myTable = PrettyTable(["Advice"])
            myTable.add_row([advices[liczba]])
            return myTable


def number_3():

    myTable = PrettyTable(["Number", "Advice"])

    # Add rows
    myTable.add_row(["1.", "Do not smoke"])
    myTable.add_row(["2.", "Protect yourself and others from passive smoking"])
    myTable.add_row(["3.", "Lose weight"])
    myTable.add_row(["4.", "Do sport"])
    myTable.add_row(["5.", "Eat healthy"])
    myTable.add_row(["6.", "Limit alcohol"])
    myTable.add_row(["7.", "Protect yourself from the sun and avoid solariums"])
    myTable.add_row(["8.", "Take care of your mental health"])
    myTable.add_row(["9.", "Take care of your sleep"])
    myTable.add_row(["10.", "Get tested regularly"])

    myTable.right_padding_width = 5
    myTable.align = "l"
    myTable.horizontal_char = "─"
    myTable.vertical_char = "│"

    return myTable


def number_4():
    """ Podaj swoje imie, potem wagę i wzrost, przeliczanie bmi i zapisywanie to w bazie sql oraz renderowanie wykresów """
    name = input("Enter your name: ").strip().lower()
    conn = sql.connect("baza.sqlite")
    c = conn.cursor()

    user_name = name.capitalize()

    if c.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{user_name}'").fetchone() is None:
        # Utwórz tabelę
        CREATE = "CREATE TABLE " + user_name + " (name TEXT, day TEXT, weight REAL, bmi REAL)"
        c.execute(CREATE)

    # pobrać dane do tabeli
    x = datetime.datetime.now()
    day = x.date().strftime('%d-%m-%Y')
    weight, bmi = number_1(wsk=1)

    # wprowadzenie danych do bazy danych
    c.execute("INSERT INTO " + user_name + " (name, day, weight, bmi) VALUES (?, ?, ?, ?)", (user_name, day, weight, bmi))

    conn.commit()

    conn.close()
    return user_name


def number_5():
    return "Thank you for using my program. See you next time. 🙂"


def more():
    answer = input("Help you with anything else? ").strip().lower()
    if answer in ["n", "no"]:
        number_5()
    elif answer in ["y", "yes"]:
        greeting()
    else:
        sys.exit("You add wrong answer, so I quit the program")


def wykres(name):
    answer = input("Would you like me to generate graphs of your progress for you? ").strip().lower()
    if answer in ["n", "no"]:
        return 0
    elif answer in ["y", "yes"]:
        print("What chart do you want to generate?\nIf weight chart, enter 1.\nIf the bmi chart, enter 2.\n")
        number = input("Enter the number: ").strip()
        if number not in ["1", "2"]:
            sys.exit("Podano złą wartość wykresu")

        if number == "1":
            #napisz funkcje tworzącą wykres
            conn = sql.connect("baza.sqlite")
            c = conn.cursor()

            c.execute('SELECT day, weight FROM ' + name)

            # Pobranie wyników zapytania SQL
            data = c.fetchall()

            # Przetworzenie danych do formatu zrozumiałego dla biblioteki `matplotlib`
            x_values = [row[0] for row in data]
            y_values = [row[1] for row in data]

            # Wygenerowanie wykresu
            plt.plot(x_values, y_values)
            plt.savefig('wykres.png', format='png')
            #plt.show()

            c.close()
            conn.close()

        else:
            #napisz funkcje tworzącą wykres
            conn = sql.connect("baza.sqlite")
            c = conn.cursor()

            c.execute('SELECT day, bmi FROM ' + name)

            # Pobranie wyników zapytania SQL
            data = c.fetchall()

            # Przetworzenie danych do formatu zrozumiałego dla biblioteki `matplotlib`
            x_values = [row[0] for row in data]
            y_values = [row[1] for row in data]

            # Wygenerowanie wykresu
            plt.plot(x_values, y_values)
            plt.savefig('wykres2.png', format='png')
            #plt.show()

            c.close()
            conn.close()

        return 0
    else:
        sys.exit("You add wrong answer, so I quit the program")

if __name__ == "__main__":
    main()