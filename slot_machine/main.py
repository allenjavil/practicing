import random #randomizing for the slot machine 

# 1 line = top, 2 = top 2, 3 = all of them. Not fully how a slot machine works, but for the sake of this project
# building kind of a slot machine
print("RUNNING FILE:", __file__)
print("TOP OF FILE EXECUTED")
# constants
MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

#setting up a square slot machine
ROWS = 3
COLS = 3

# the values of the slot machine, going from more valuable to less
# dictionary for the symbols 
symbol_count = {
    "A": 2,
    "B": 4, 
    "C": 6, 
    "D": 8
}

# the rarer the symbol is the higher the bet gets multiplied
symbol_value = {
    "A": 5,
    "B": 4, 
    "C": 3, 
    "D": 2
}

def check_winnings(columns, lines, bet, values):
    # only looking at the lines the user betted on
    winnings = 0
    winning_lines = []
    for line in range(lines): 
        # checking if every single symbol in the line is the same 
        symbol = columns[0][line] # assume there's always a symbol to the right 
        for column in columns: 
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break # if one symbol not equal, we break out of for loop. 
        else: 
            winnings += values[symbol] * bet 
            winning_lines.append(line + 1)
                # what lines they won at

    return winnings, winning_lines
# ^^ every line in lines (looping through every row). We want to check the symbol that's first on each row (bc they all need to be same.)
# ^^ loop through every single column and check for that symbol. If symbols not same, we break out, and move onto next row. 
# ^^ if same at some point, then, we multiply the value of the symbol times what they bet on that line. 
# ^^ Basically, they can lose in one line but win on another one. 


# have a doubt 
def get_slot_machine_spin(rows, cols, symbols):
    # list
    all_symbols = []
    # since dictionary, we have this function that directly refers to keys(ABCD) and their values (2,4,6,8)
    for symbol, symbol_count in symbols.items():
        # telling something to loop but don't care about how many times
        for _ in range(symbol_count):
            all_symbols.append(symbol)
# represents values in our call? Confused on this too
    
    columns = []
    #### 
        # We start by defining our columns list. Then, we gernerate a column for every single column we have. 
        # So, if we have 3 cols, we do all of the for loops below 3 times.
        # The code is picking random values for each row in our column. 
    ####
    # somehow we don't need either the col or row, so we place underscore instead. 
    for _ in range(cols):
        # for every column we need to generate certain number of symbols
        column = []
        # we copy the list from all symbols 
        current_symbols = all_symbols[:]
        for _ in range(rows):
            # once we pick a value we need to remove that value from the list so the next one doesn't repeat
            value = random.choice(current_symbols)
            # gonna find first instance of the value chosen, and remove it from the copied list
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
    return columns 

def print_slot_machine(columns):
    # not easy to print bcause we have it all on the [], row format (but it's columns, not row)
    # how do we change that? We are TRANSPOSINGGG (LIN ALGEBRA OMGG)
    for row in range(len(columns[0])):
        # assumes that we have AT LEAST one column. If we had 0 columns, it'd crash because there's nothing to index
        for i, column in enumerate(columns): 
            if i != len(columns) - 1: 
                print(column[row], end= " | ")
            else: 
                print(column[row], end= "")
        print()
        # prints first row, next line character etc     
# "end" says what to end the line with. By default 
# collects user input 
def deposit():
    while True: 
        # ensure that what the user inputs is a valid amount
        amount = input("What would you like to deposit? $")
        if amount.isdigit():
            #checking if it's a digit. By default user input is string, so we make it a numeric value (int)
            amount = int(amount) 
            if amount > 0: 
                break 
            else:
                print("Amount must be greater that 0.")
        else: 
            print ("Please enter a number: ")
            
    return amount

# ask number of lines, and then how much they want to bet in each line
def get_number_of_lines():
    while True: 
        # ensure that what the user inputs is a valid line amount
        # made max_lines a string so that it wouldn't get added to the 1, as we want to show what's the constant max
        lines = input("Enter the number of lines you want to bet on (1 - " + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            #checking if it's a digit. By default user input is string, so we make it a numeric value (int)
            lines = int(lines) 
            if 1 <= lines <= MAX_LINES: 
                break 
            else:
                print("Enter a valid number of lines")
        else: 
            print ("Please enter a number: ")

    return lines

def get_bet():
    while True:
        amount = input("What would you like to bet? $")
        if amount.isdigit():
            amount = int(amount)
            # python allows to have this kind of double conditioning in if statement
            if MIN_BET <= amount <= MAX_BET:
                break 
            else: 
                # by placing the f and the {}, the constant int immediately transformed into string w/o having to directly convert.
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.")
        else: 
            print("Please enter a number.")
    return amount

def spin(balance):
    lines = get_number_of_lines()
    # checking that they have enough balance to bet on all the lines they want (based on initial amount input)
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance: 
            print(f"You do not have enough to bet that amount, your current balance: ${balance}")
        else: 
            break

    print(f"You are betting ${bet} on {lines} lines. Your total bet is equal to: ${total_bet}")
# we have all of the columns in our slot spin
    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won $ {winnings}.")
    # the * is a splat (or unpack operator), which passes every line from winning_lines list to that function below.
    # ex, if user won 1 and 2, it'll pass lines 1 and 2 through the *. So those will be the printed ones.
    print(f"You won on lines:", *winning_lines)
    return winnings - total_bet

def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        answer = input("Press enter to play (q to quit).")
        if answer == "q":
            break 
        balance += spin(balance)
        
    print(f"You left with ${balance}")


main()
