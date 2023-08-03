import random

from helper import get_int
from constants import *

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


def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbols_count in symbols.items():
        all_symbols += [symbol for _ in range(symbols_count)]

    columns = []
    for col in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        
        columns.append(column)

    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            print(column[row],end= " | " if i!=len(columns)-1 else "")
        print()

def deposit():
    '''Gets deposit number from user'''
    amount = get_int("What would you like to deposit? $", check_positive=True)
    return amount


def get_number_of_lines():
    while True:
        lines = get_int(
            f"Enter the number of lines to bet on (1-{MAX_LINES})? ")
        if 1 <= lines and lines <= MAX_LINES:
            break
        else:
            print("Enter a valid number of lines.")

    return lines

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)
    
    return winnings, winning_lines


def get_bet():
    while True:
        amount = get_int("What would you like to bet on each line? $")
        if MIN_BET <= amount <= MAX_BET:
            break
        else:
            print(f"Amount must be between ${MIN_BET} - ${MAX_BET}")

    return amount

def game(balance):
    lines = get_number_of_lines()

    while True:
        bet = get_bet()
        total_bet = bet*lines

        if total_bet > balance:
            print(
                f"You do not have enough to bet that amount, your current balance is: ${balance}")
        else:
            break

    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")
    
    slots = get_slot_machine_spin(ROWS,COLS,symbol_count)
    print_slot_machine(slots)

    winnings, winning_lines = check_winnings(slots,lines,bet, symbol_value)
    print(f"You've won ${winnings}.")
    print(f"You won on lines: ", *winning_lines)

    return winnings - total_bet


def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        spin = input("Press enter to play (q to quit).")
        if spin =='q':
            break
        balance += game(balance)


if __name__ == '__main__':
    main()
