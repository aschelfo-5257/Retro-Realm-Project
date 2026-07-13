"""
Program Name: main.py
Author: Aaron Schelfo
Date last updated: July 13, 2026
Purpose: Orchestrates the user menu loop and pulls data from separate project modules.
"""

import database_config
import database_ops
import reports

def main():
  conn = database_config.get_connection()
  if not conn:
    return

  while True:
        print("\n===== RETRO REALM MENU =====")
        print("1. Add a Game")
        print("2. Delete a Game")
        print("3. Process a Sale Transaction")
        print("4. View Inventory Report")
        print("5. Exit")
        
        choice = input("Select an option (1-5): ")
        
        if choice == '1':
            title = input("Game Title: ")
            cond = input("Condition: ")
            plat = input("Platform ID: ")
            database_ops.add_game(conn, title, cond, plat)
        elif choice == '2':
            g_id = input("Game ID to delete: ")
            database_ops.delete_game(conn, g_id)
        elif choice == '3':
            s_id = input("Store ID: ")
            g_id = input("Game ID: ")
            price = input("Price: ")
            database_ops.execute_sale_transaction(conn, s_id, g_id, price)
        elif choice == '4':
            reports.print_inventory_report(conn)
        elif choice == '5':
            print("Goodbye!")
            break
            
    conn.close()

if __name__ == '__main__':
    main()
