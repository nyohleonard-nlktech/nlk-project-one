# to get input from the user
def get_num():
    while True:
        try:
            n1 = float(input("what is number1: "))
            n2 = float(input("what is number2: "))
            return n1 , n2
        except ValueError:
            Print("when data you enterred is invalid try again") 

# this function perfrms addition  of the input data 
def add( n1 , n2):
    printf(f"{n1} + {n2} = {n1+n2}")

def mul_table(num):
    print("Here is the multiplication table of",num)
    for i in range(1,13):
        print(f"{num} * {i} = {num*i}")               
        
# this function performs division
def div(n1, n2):
    if n2 == 0:
        print("Division by zero is not possible")

    else:
        result = n1 / n2
        print(f"The division of {n1:.2f} / {n2:.2f} = {result:.2f}")

# this function output the factors of a number inputted
def factor(num):
    for i in range (2,num+1):
        if num % i ==0:
            print(i)

# list of menu
def menu_choice():
    print("\n____menu list____")  
    print("1.add")   
    print("2.mul_table")
    print("3.div")
    print("4.factor")
    print('5.exit') 
    print()

# main function
def main():
    while True:
        menu_choice()
        choice = int(input('from the menu give your choice from (1-5):  '))  
        print() 

        match choice:

            case 1:
                n1 , n2 = get_num()
                add(n1,n2)

            case 2:
                    num = float(input('enter the number you want it multiplicstion table: '))  
                    mul_table(num) 

            case 3:
                n1, n2 = get_num()
                div(n1,n2)  

            case 4:
                num = int(input("enter the numberyou want it factors: "))
                factor(num)
            case 5:
                print("Good Working With You")  
                break

main ()              

              