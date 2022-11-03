# This program creates a random math question that have to do with percentages, and checks if the answer is right or wrong.
import random
import time

# Create random variables for the percentage (ranPercent), the cost (ranCost), an array of random products (products) and different expenses (expenses).
products = ["apple", "green t-shirt", "yellow trouser", "bannana at the grocery store", "gray jacket", "watermelon shirt", "blue shirt", "yellow t-shirt", "loaf of whole wheat bread",
            "loaf of white bread", "baguette", "orange shirt", "pajamma", "gallon of milk at a grocery store", "bagel at a coffe shop", "cup of coffe at a coffe shop", "herb slab", "bin of ice cream", "fork", "hamburger", "watermelon at the local grocery store"]
expenses = ["transportation", "advertising", "marketing", "production", "storage",
            "rent", "payroll", "taxes", "utilities", "facilitrtaes", "enteinment", "shipping"]

# Print the math question


def printQuestion(products, expenses, questionType):
    # Generate random numbers for the percentage (ranPercent), the cost (ranCost), the product (ranProduct) and the expense (ranExpense)
    ranPercent = random.randint(10, 40)
    ranCost = random.randint(5, 40)
    ranProduct = random.randint(0, (len(products) - 1))
    ranExpense = random.randint(0, (len(expenses) - 1))

    # Print the math question and calculate the correct answer
    if questionType == 1:
        print("A " + products[ranProduct] + " costs $" + str(ranCost) + ".\n\n" + str(ranPercent) + "%" +
              " of the total cost is spent on " + expenses[ranExpense] + ".\n\nHow many dollars are spent on " + expenses[ranExpense] + "?\n")
        return (round((ranCost / 100) * ranPercent))
    elif questionType == 2:
        print("A " + products[ranProduct] + " costs $" + str(ranCost) + ".\n\nThere is a " + str(ranPercent) +
              "%" " discount on the " + products[ranProduct] + ".\n\nHow many dollars will the discount save?\n")
        return (round((ranCost / 100) * ranPercent))
    elif questionType == 3:
        print("A " + products[ranProduct] + " costs $" + str(ranCost) + ".\n\nThere is a " + str(ranPercent) + "%" + " discount on the " +
              products[ranProduct] + ".\n\nHow many dollars does the " + products[ranProduct] + " cost with the discount?\n")
        return (round(ranCost - ((ranCost / 100) * ranPercent)))
    elif questionType == 4:
        print("A " + products[ranProduct] + " has a " + str(ranPercent) + "%" + " discount.\n\nIt costs $" + str(
            ranCost) + " with the discount.\n\nHow many dollars did the " + products[ranProduct] + " originally cost?\n")
        return (round((ranCost / (100 - ranPercent)) * 100))
    elif questionType == 5:
        print("$" + str(ranCost) + " of the total price are spent on " + expenses[ranExpense] + ".\n\nCosts of " + expenses[ranExpense] + " account for " + str(
            ranPercent) + "%" + " of the total price.\n\nHow many dollars is the total price?")
        return (round((ranCost / ranPercent) * 100))
    else:
        print("Error: Invalid question number: " + questionType)


print("\nWelcome to Percentage Math! In this game, you will have to find the answer to various percentage questions. Answers will be rounded to the nearest one digit.\n\n")
time.sleep(2)

while 1 == 1:
    # Generate a random question number and then call the "printQuestion" function
    ranQuestion = random.randint(1, 5)
    answer = printQuestion(products, expenses, ranQuestion)

    # Get the user input, and then changes it to an integer so it can round it
    userInput = round(int(input()))

    # Check if the answer is correct and give feedback accordingly
    if str(userInput) == str(answer):
        print("\nCorrect!\n\n\n")
    elif ranQuestion == 4:
        print("\nIncorrect. The answer was " + str(answer) + "%.\n\n\n")
    else:
        print("\nIncorrect. The answer was $" + str(answer) + ".\n\n\n")
    time.sleep(1)
