# Importing for random value generation
import random  

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

# Dictionary mapping symbols to their respective counts
symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

# Calculates winnings based on the slot machine spin
def check_winnings(columns, lines, bet, values):
    """
    Calculates winnings based on the slot machine spin.
    
    Args:
        columns (list of lists): Represents the slot machine spin.
        lines (int): The number of lines bet on.
        bet (int): The bet amount per line.
        values (dict): Dictionary mapping symbols to their values.

    Returns:
        int: Total winnings.
    """
    winnings = 0
    winning_lines = []
    for line in range(lines):  # Loop through each row
        symbol = columns[0][line]  # Get symbol from the first column of the current row
        for column in columns:  # Loop through each column to check for the symbol
            symbol_to_check = column[line]  
            if symbol != symbol_to_check:  # Break if symbols are different
                break
            else:
                winnings += values[symbol] * bet  # Calculate winnings
                winning_lines.append(line + 1)
                
    return winnings, winning_lines

# Generates a random spin of the slot machine
def get_slot_machine_spin(rows, cols, symbols):
    """
    Generates a random spin of the slot machine.
    
    Args:
        rows (int): Number of rows in the slot machine.
        cols (int): Number of columns in the slot machine.
        symbols (dict): Dictionary mapping symbols to their counts.

    Returns:
        list of lists: Represents the slot machine spin.
    """
    all_symbols = []  # Initialize list to store all symbols
    for symbol, symbol_count in symbols.items():  # Iterate over symbols
        for _ in range(symbol_count): 
            all_symbols.append(symbol)  # Add each symbol to the list
    
    columns = []  # Initialize list to store columns
    for _ in range(cols):  # Generate columns
        column = []
        current_symbols = all_symbols[:]  # Make a copy of all symbols
        for _ in range(rows):  # Generate values for each row
            value = random.choice(current_symbols)  # Choose a random value
            current_symbols.remove(value)  # Remove the selected value
            column.append(value)  # Add value to column
        columns.append(column)  # Add column to list
        
    return columns

# Prints the layout of the slot machine
def print_slot_machine(columns):
    """
    Prints the layout of the slot machine.
    
    Args:
        columns (list of lists): Represents the slot machine spin.
    """
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):  # Loop through columns
            if i != len(columns) - 1:
                print(column[row], end=" | ")  # Print symbol with separator
            else:
                print(column[row], end="")  # Print symbol without separator
        print()  # Move to the next row

# Collects the user's deposit amount
def deposit():
    """
    Collects the user's deposit amount.
    
    Returns:
        int: The deposit amount.
    """
    while True:
        amount = input("What would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number.") 
    return amount

# Collects the number of lines the user will bet on
def get_number_of_lines():
    """
    Collects the number of lines the user will bet on.
    
    Returns:
        int: The number of lines.
    """
    while True:
        lines = input(f"Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid amount of lines.")
        else:
            print("Please enter a number.")
    return lines

# Collects the amount the user would like to bet
def get_bet():
    """
    Collects the amount the user would like to bet.
    
    Returns:
        int: The bet amount.
    """
    while True:
        amount = input("What would you like to bet on each line? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("Please enter a valid bet.")
    return amount

# Main function to orchestrate the slot machine game
def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance: # type: ignore
            print(f"You do not have enough to bet that amount, your current balance is ${balance}") # type: ignore
        else:
            break
    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to ${total_bet}.") 

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}.")
    print(f"You won on lines:", *winning_lines) # * unpacking all elements of winning lines
    return winnings - total_bet

# Main function to orchestrate the slot machine game
def main():
    balance = deposit()
    while True:
        print(f"Current balance is: ${balance}")
        answer = input("Press enter to play (q to quit).")
        if answer == "q":
            break
        balance += spin(balance)
        
    print(f"You left with ${balance}")
        
main()