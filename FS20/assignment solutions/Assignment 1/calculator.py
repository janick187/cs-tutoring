# user should be able to do the following mathematical operations: multiply, divide, add, substract
# user should be able to terminate calculator with keyword end
# user should be able to print calculator-history with command "history"

# create initial flag
EndFlag = False

# create empty history
history_list = list()

# function to get a valid integer value from a user
def get_number():
    
    # repeat until user enters a valid number
    while True:
        
        # get user input from console
        value = input("Enter a number: ")
        
        # catch is user entered not a number
        try:
            # convert input to integer
            number = int(value)
        # if user did not enter a valid number an exception will be raised
        except ValueError:
            # do while loop another time
            continue
        
        # exit while loop as try statement could be executed successfully
        break;
    
    # return valid integer
    return number;

# repeat execution of calculator
while not EndFlag:
    
    # get desired operation from user
    operation = input("Gewünschte Operation: ")
    
    # check if user wants to end calculator
    if operation == "end":
        EndFlag = True
    
    # check if user wants to print history
    elif operation == "history":
        for element in history_list:
            print(element)
    
    # otherwise he wants to do another calculation
    else:
        # get values
        first_value = get_number()
        second_value = get_number()
        
        # do according mathematical operation
        if operation == "add":
            result = first_value + second_value
        elif operation == "substract":
            result = first_value - second_value
        elif operation == "multiply":
            result = first_value * second_value
        elif operation == "divide":
            result = first_value / second_value
        else:
            result = "Invalid operation, try again"
    
        print("Resultat: ", result)
    
        # add the executed calculation to the history
        string = operation + " " + str(first_value) + " " + str(second_value) + " " + str(result)
        history_list.append(string)