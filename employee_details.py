from audioop import add
from curses.ascii import isdigit
import random
import json


def welcome_worker():
    print("....Welcome to Yellow Garden....")
    print("Please fill and sign required feilds.")

def employee_name():

    name = input("Please enter your full name: ")

    while True:

        if name == "":
            print("This field cannot be empty")
            name = input("Please enter your full name: ")

        elif name.isdigit():
            print("This field cannot be a number")
            name = input("Please enter your full name: ")
        else:
            
            return name
    
def employee_surname():
    surname = input("Please enter your surname: ")

    while True:
        if surname == "":
            print("This field cannot be empty")
            surname = input("Please enter your surname: ")

        elif surname.isdigit():
            print("This field cannot be a number")
            surname = input("Please enter your surname: ")
        else:
            return surname


def read_json():
    out = []
    for _ in range(5):
        name = employee_name()
        surname = employee_surname()
        employ_number = [0,0,0,0]

        for i in range(4):
            number = random.randint(0,9)
            employ_number[i] = number
        print(employ_number)

        data = {}
        
        data["Name"] = name
        data["Surname"] = surname
        data["Employee Number"] = employ_number

        out.append(data)



    with open("file.json", "w") as file:
        json.dump(out,file,indent=1)

    f = open("file.json")

    json_data = json.load(f)
    employee_login(json_data)



def employee_login(json_data):

    secrete_number = input("Please enter your employee number: ")

    while True:
        for i in range(len(json_data)):

            x_random_employee_num = json_data[i]
            secrete_employee_number = "".join([str(element) for element in x_random_employee_num["Employee Number"]])

            if secrete_number == secrete_employee_number:
                print("Logged in successfully....")
                purchase_item()
                return secrete_number
        if secrete_number != secrete_employee_number:
            secrete_number = input("Please enter your correct employee number: ")
       

def purchase_item():

    sales_dict = {}
    print("Please enter the items you would like to buy.")
    print("Enter 'done' to proceed.")
    customer_purchase = input("What would you like to buy: ")
    product_price = input("Price: R- ")

    check_price_input(sales_dict,customer_purchase,product_price)


    while True:
        if customer_purchase.lower() != "done":
            customer_purchase = input("What would you like to buy next: ")

            # sales_dict["".join(str(customer_purchase))] = customer_purchase

        if customer_purchase.lower() != "done":
            product_price = input("Price: R- ")
            product_price = check_price_input(sales_dict,customer_purchase,product_price)


        elif customer_purchase.lower() == "done":
            print("Thank you for shopping with us your products are being processed for payment..\n")
            sum_of_products(sales_dict)
            return sales_dict

def check_price_input(sales_dict, customer_purchase,product_price):
    while True:
        if product_price.isdigit():
            sales_dict["".join(str(customer_purchase))] = product_price
            return product_price

        elif product_price.isdigit() == False:
            print("Enter correct amount")
            product_price = input("Price: R- ")

        
def sum_of_products(sales_dictionary):

    customer_payment = receive_payment()
    customer_payment_int = int(customer_payment)
    
    total_cost = []

    for i in sales_dictionary:

        print(f"Product: {i}       R {sales_dictionary[i]}.00 \n")

        if sales_dictionary[i].isdigit():
            x = int(sales_dictionary[i])
            total_cost.append(x)
    
    


    print(f"Amount Due:           R {sum(total_cost)}.00 \nAmount Payed:         R {customer_payment}.00 \nChange:               R {customer_payment_int-sum(total_cost)}.00")
   
def receive_payment():
    
    get_payment = input("Enter payment amount: ")

    while True:
        if get_payment.isdigit():
            return get_payment
        else:
            get_payment = input("Enter payment amount: ")
        
        

if __name__ == "__main__":
    welcome_worker()


    read_json()
