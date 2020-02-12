#############################################################################
#Project #4
#
#import math library and define episilon
#create function to print the options menu
#create function to calculate the sum of natural squares 
#   this will be based on the user's input
#   this will use exception handling to determine valid input
#create function to calculate the approximate value of pi
#   using the summation approximation formula, which requires a while loop
#create function to calculate the aproximate sine value
#   this will be based off the user's input
#   use exception handling to determine a valid input
#create function to calculate the approximate sine value
#   this will be based off the user's input
#   use exception hndling to determine a valid input
#create a main function that will call all the other functions
#   use whlle loop based off user's response to tell which function to run
#   use exception handling to determine a valid input
#   if the user's input is x,end the program and send a goodbye message
#############################################################################

import math
EPSILON = 1.0e-7
def display_options():
    
    """
    This function doesn't take any arguments and displays the menu of options
    for the user to select from. 
    """
    
    ''' This function displays the menu of options'''

    MENU = ('''\nPlease choose one of the options below:
             A. Display the sum of squares of the first N natural numbers.
             B. Display the approximate value of Pi.
             C. Display the approximate value of the sine of X.
             D. Display the approximate value of the cosine of X.
             M. Display the menu of options.
             X. Exit from the program.''')
    print(MENU)

def sum_natural_squares(string):
    
    """
    This function takes a string as an argument. It uses exception handling to
    determine if the argument can actually be converted to an integer. If it
    can't, then return None. If it can, created a for loop from 1 to the 
    argument + 1, and square the iterable variable in the loop. Return
    the squared variable.
    """
    try:
        string_integer= int(string)
    except ValueError:
        return None
    squared= 0
    if string.isdigit()==False or string=="0":
        return None 
    for i in range(1,string_integer+1):
        squared+= i **2
    return squared

def approximate_pi():
    
    """
    This function doesn't take an argument. Using the summation formula,
    create a variable that store each term and a variable that will 
    increment by 1. Create a while loop where the absolute value of the term
    is greater than or equal to EPSILON. Return the pi approximation and
    multipy it by 4 since that is apart of the formula. Round to 10 decimal
    places.
    """
    
    n=0
    term= ((-1)**n)/(2*n + 1)
    pi_approximation= 0
    while abs(term)>=EPSILON:
        pi_approximation+=term
        n=n+1
        term=((-1)**n)/(2*n + 1)
    return round(4*pi_approximation,10)
    


def approximate_sin(x):
    
    """
    This function takes a string as an argument. Use exception handling 
    to determine if the argument can be converted to a float, if it can't,
    then return None. Use the summation formula to calculate the 
    approximation of sine. Create a variable that stores the term 
    and create a variable that will increment by 1. Create a
    while loop the absolute value of the term is greater than or
    equal to EPSILON, Create a variable that will store the sum of all the
    terms in the loop. Return the approximation.
    """
    try:
        x = float(x)
    except ValueError:
        return None
    n=0
    term= (((-1)**(n))*(x)**(2*n+1))/(math.factorial(2*n+1))
    sine_approximation= 0
    while abs(term)>=EPSILON:
        sine_approximation+=term
        n=n+1
        term= (((-1)**(n))*(x)**(2*n+1))/(math.factorial(2*n+1))
    return round(sine_approximation,10)
        



def approximate_cos(x):
    
    """
    This function takes a string as an argument. Use exception handling 
    to determine if the argument can be converted to a float, if it can't,
    then return None. Use the summation formula to calculate the 
    approximation of cosine. Create a variable that stores the term 
    and create a variable that will increment by 1. Create a
    while loop the absolute value of the term is greater than or
    equal to EPSILON, Create a variable that will store the sum of all the
    terms in the loop. Return the aproximation. 
    """
    
    try:
        x= float(x)
    except ValueError:
        return None
    n=0
    term= (((-1)**(n))*x**(2*n))/(math.factorial(2*n))
    cosine_approximation= 0
    while abs(term)>=EPSILON:
        cosine_approximation+=term
        n=n+1
        term= (((-1)**(n))*x**(2*n))/(math.factorial(2*n))
    return round(cosine_approximation,10)
        

def main():
    
    """
    This function doesnt take an argument. Call the display options function
    to display the menu. Ask the user to select an option. If the
    selected option is invalid, print an error message, and 
    call display_options() to display the menu of options. Create a while 
    loop for when the user enters a valid response and the response is not x,
    create if statements for each option. Re-prompt the user to enter 
    another option. If the user's input is x, then print a goodbye message
    and exit the function.
    """
    display_options()  #Call function
    option= input("\n\tEnter option: ").lower() #Ask for user option


    while option != 'x': #Loop for when option isn't x.
            
        if option == 'a': #If option is A, call sum_natural_squares
            user_number=input("Enter N: ")#Ask user to enter a number
            #Pass the number in the sum_natural_squares function. 
            sum_of_squares = sum_natural_squares(user_number)
            if sum_of_squares == None: #Condition for invalid responses
                #print error message
                print("\n\tError: N was not a valid natural number. [{}]"\
                      .format(user_number.upper()))
            else: #if input is valid
                print("\n\tThe sum: ",sum_of_squares) #print sum of squares
            
            
        elif option == 'b': #if option is b, call approximate_pi()
            
            val = approximate_pi() #val stores pi approximation value
            math_pi = math.pi # Stores actual value from math library
            math_pi_rounded= round(math_pi,10) 
            #Difference between approximation and actual value. 
            difference= abs(math_pi-val) 
            difference_rounded=round(difference,10)
            print("\n\tApproximation: {:.10f}".format(val))
            print("\tMath module:   {:.10f}".format(math_pi_rounded))
            print("\tdifference:    {:.10f}".format(difference_rounded))

        elif option=="c": #If option is c, call approximate_sin()
            user_input= input("\n\tEnter X: ") #ask user for input
            check= approximate_sin(user_input)# pass input in approximate_sin()
            if check==None: #If input is invalid 
                #print error message
                print("\n\tError: X was not a valid float. [{}]"\
                      .format(user_input))
            else: #if input is valid
                user_number= float(user_input) #convert input to float 
                #pass the user number in math.sin function to get 
                #actual value.
                sine_value= math.sin(user_number) 
                sine_value_rounded= round(sine_value,10)
                #pass the user number in approximate_sin function to get 
                #the sin approximation value
                sin_approximation= approximate_sin(user_number)
                #Difference between the sine value and the approximation
                difference= abs(sine_value-sin_approximation)
                print("\n\tApproximation: {:.10f}".format(sin_approximation))
                print("\tMath module:   {:.10f}".format(sine_value_rounded))
                print("\tdifference:    {:.10f}".format(difference))
            
        elif option=="d": #if option is d, call approximate_cos()
            user_input= input("\n\tEnter X: ") #ask for input
            #Pass input in approximate_cos()
            check= approximate_cos(user_input)
            if check==None: #if input is invalid 
                #print error message
                print("\n\tError: X was not a valid float. [{}]"\
                      .format(user_input))
            else: #if input is valid 
                user_number= float(user_input) #convert to float
                #pass the number in math.cos() for actual value
                cosine_value= math.cos(user_number) 
                cosine_value_rounded= round(cosine_value,10)
                #pass number in approximate_cos() for approximation value
                cosine_approximation= approximate_cos(user_number)
                #Difference between actual value and the approximation.
                difference= abs(cosine_value-cosine_approximation)
                print("\n\tApproximation: {:.10f}".format(cosine_approximation))
                print("\tMath module:   {:.10f}".format(cosine_value_rounded))
                print("\tdifference:    {:.10f}".format(difference))
            
        elif option=="m": #if option is m, call display_options()
            display_options()
        else: #print error message if option input is invalid
            print("\nError:  unrecognized option [{}]".format(option.upper()))
            display_options() #print menu again
            
            
        option= input("\n\tEnter option: ").lower() #ask user to pick option
    print("Hope to see you again.") #if option equal x, print goodbye message
     
#Call the function
if __name__ == "__main__": 
    main()