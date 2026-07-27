"""
Program Name: main.py
Author: Aaron Schelfo
Date last updated: July 13, 2026
Purpose: Orchestrates the user menu loop and pulls data from separate project modules.
"""

from database import database_ops as ops
from modules import reports as rpt


def run_add_menu():
    print("\nAdd record")
    print("1. Add platform")
    print("2. Add game")
    choice = input("Choose an option: ")
    if choice == "1":
        name = input("Platform name: ")
        year = input("Release year: ")
        ops.insert_platform(name, year)
    elif choice == "2":
        title = input("Game title: ")
        condition = input("Condition: ")
        platform_id = input("Platform ID: ")
        ops.insert_game(title, condition, platform_id)


def run_update_menu():
    print("\nUpdate record")
    print("1. Update game condition")
    print("2. Update store phone")
    choice = input("Choose an option: ")
    if choice == "1":
        game_id = input("Game ID: ")
        status = input("New condition: ")
        ops.update_game_condition(game_id, status)
    elif choice == "2":
        store_id = input("Store ID: ")
        phone = input("New phone number: ")
        ops.update_store_phone(store_id, phone)


def run_delete_menu():
    print("\nDelete record")
    platform_id = input("Platform ID: ")
    ops.delete_platform(platform_id)


def run_transaction_menu():
    print("\nCreate sale")
    store_id = input("Store ID: ")
    sale_date = input("Sale date (YYYY-MM-DD): ")
    total_revenue = input("Total revenue: ")
    game_id = input("Game ID: ")
    ops.process_checkout_transaction(store_id, sale_date, total_revenue, game_id)


def run_reports_menu():
    print("\nReports")
    print("1. Games by platform")
    print("2. Sales by store")
    choice = input("Choose an option: ")
    if choice == "1":
        data = rpt.get_games_catalog_report()
        for row in data:
            print(f"Game ID: {row[0]} | Title: {row[1]} | Condition: {row[2]} | Platform: {row[3]}")
    elif choice == "2":
        data = rpt.get_store_revenue_report()
        for row in data:
            print(f"Sale ID: {row[0]} | Store: {row[1]} | Date: {row[2]} | Amount: ${row[3]}")


def main():
    while True:
        print("\n=== RETRO REALM GAME MENU ===")
        print("1) Add records")
        print("2) Update records")
        print("3) Delete records")
        print("4) Create sale")
        print("5) View reports")
        print("6) Exit")

        selection = input("Choose an option (1-6): ")
        if selection == "1":
            run_add_menu()
        elif selection == "2":
            run_update_menu()
        elif selection == "3":
            run_delete_menu()
        elif selection == "4":
            run_transaction_menu()
        elif selection == "5":
            run_reports_menu()
        elif selection == "6":
            print("Goodbye!")
            break
        else:
            print("Please enter a valid option.")


if __name__ == "__main__":
    main()
