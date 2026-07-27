"""
Program name: database_ops.py
Author: Aaron Schelfo
Date last updated: July 13, 2026
Purpose: Modular functions executing specialized inserts, modifications, and atomic transactions.
"""

from datetime import get_connection
from mysql.connector import Error

def insert_platform(name, year):
    """Add Table Option #1: Platforms"""
    query = "INSERT INTO Platforms (platform_name, release_year) VALUES (%s, %s);"
    _run_modification(query, (name, year))

def insert_game(title, condition, platform_id):
    """Add Table Option #2: Games"""
    query = "INSERT INTO Games (game_title, game_condition, platform_id) VALUES (%s, %s, %s);"
    _run_modification(query, (title, condition, platform_id))

def update_game_condition(game_id, status):
    """Update Table Option #1: Games"""
    query = "UPDATE Games SET game_condition = %s WHERE game_id = %s;"
    _run_modification(query, (status, game_id))

def update_store_phone(store_id, phone):
    """Update Table Option #2: Stores"""
    query = "UPDATE Stores SET phone_number = %s WHERE store_id = %s;"
    _run_modification(query, (phone, store_id))

def delete_platform(platform_id):
    """Delete Table Option: Platforms (Requires dynamic prompt lookup value)"""
    query = "DELETE FROM Platforms WHERE platform_id = %s;"
    _run_modification(query, (platform_id,))

def process_checkout_transaction(store_id, sale_date, total_revenue, game_id):
    """Mandatory Multi-Statement Transaction logic protecting row parity."""
    conn = get_connection()
    if not conn: return
    try:
        conn.autocommit = False  # Explicit transaction boundary context lock
        cursor = conn.cursor()
        
         # 1. Insert header record tracking checkout location
        sales_sql = "INSERT INTO Sales (store_id, sale_date, total_revenue) VALUES (%s, %s, %s);"
        cursor.execute(sales_sql, (store_id, sale_date, total_revenue))

        invoice_ref = cursor.lastrowid
        
        # 2. Insert corresponding child line item records mapped to inventory
        tx_query = "INSERT INTO Transaction (game_id, sale_id) VALUES (%s, %s)"
        cursor.execute(tx_query, (game_id, invoice_ref))
        
        conn.commit()
        print(f"Transaction verified! Generated Ledger Order Number: #{invoice_ref}")
    except Error as e:
        conn.rollback()  # Safely reverse updates if constraint fails
        print(f"Transaction aborted automatically: {e}")
    finally:
        cursor.close()
        conn.close()

def _run_modification(query, params):
    """Private operational helper executing isolated single statements cleanly."""
    conn = get_connection()
    if not conn: return
    try:
        cursor = conn.cursor()
        cursor.execute(query, params)
        conn.commit()
        print("Database reference state tracking successfully adjusted.")
    except Error as e:
        print(f"Operation failure: {e}")
    finally:
        cursor.close()
        conn.close()
  
