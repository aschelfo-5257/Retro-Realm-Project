"""
Program Name: main.py
Author: Aaron Schelfo
Date last updated: July 13, 2026
Purpose: Orchestrates the user menu loop and pulls data from separate project modules.
"""

import database_ops as ops
import reports as rpt

def run_add_menu():
    print("\n[Add Target Choice]")
    print("1. New Hardware Console System Type")
    print("2. New Game Cartridge Unit Entry")
    choice = input("Enter option row choice: ")
    if choice == '1':
        name = input("Console system name: ")
        yr = input("Launch year integer: ")
        ops.insert_platform(name, yr)
    elif choice == '2':
        title = input("Game title string: ")
        cond = input("Condition (e.g. Scratched Condition): ")
        p_id = input("Platform reference key index ID: ")
        ops.insert_game(title, cond, p_id)

def run_update_menu():
    print("\n[Update Target Choice]")
    print("1. Modify Existing Game Physical Wear Quality")
    print("2. Update Branch Store Front Phone Reference")
    choice = input("Enter option row choice: ")
    if choice == '1':
        gid = input("Target game database record tracking ID: ")
        status = input("New update value text string: ")
        ops.update_game_condition(gid, status)
    elif choice == '2':
        sid = input("Target branch storefront identifier tracking ID: ")
        phone = input("New phone contact configuration format string: ")
        ops.update_store_phone(sid, phone)

def run_delete_menu():
    print("\n[Delete Target Choice]")
    pid = input("Enter target unique Platform ID value to completely clear: ")
    ops.delete_platform(pid)

def run_transaction_menu():
    print("\n[Transaction POS Ledger Checkout Checkout Entry Interface]")
    sid = input("Processing store branch node ID index: ")
    s_date = input("Checkout collection log date structure (YYYY-MM-DD): ")
    rev = input("Invoice line grand total transaction price context value: ")
    gid = input("Target structural retail software game product barcode tracking asset ID: ")
    ops.process_checkout_transaction(sid, s_date, rev, gid)

def run_reports_menu():
    print("\n[Data Synthesis Reports]")
    print("1. Product Systems Cross Reference Chart")
    print("2. Location Invoicing Auditing Record Ledger")
    choice = input("Select processing log variant index: ")
    if choice == '1':
        data = rpt.get_games_catalog_report()
        for row in data: print(f"Game ID: {row[0]} | Title: {row[1]} ({row[2]}) | Base Console: {row[3]}")
    elif choice == '2':
        data = rpt.get_store_revenue_report()
        for row in data: print(f"Sale #{row[0]} | Location: {row[1]} | Processed: {row[2]} | Amount: ${row[3]}")

def main():
    while True:
        print("\n=== RETRO REALM INTERACTIVE DATA MANAGEMENT MODULE ===")
        print("1) Insert Registry Data Rows")
        print("2) Modify Structural Registry Records")
        print("3) Clear Record Registry Reference Data Rows")
        print("4) Create Order POS Ticket Invoice (Transaction Run)")
        print("5) Compile Analytical Joint Structural Overview Summaries")
        print("6) Shut Down Operations Console Environment")
        
        sel = input("Select system control registry sequence command (1-6): ")
        if sel == '1': run_add_menu()
        elif sel == '2': run_update_menu()
        elif sel == '3': run_delete_menu()
        elif sel == '4': run_transaction_menu()
        elif sel == '5': run_reports_menu()
        elif sel == '6':
            print("Closing application. Great job planning ahead this week!")
            break
        else:
            print("Input error. Provide a valid execution flag option identifier integer.")

if __name__ == '__main__':
    main()
