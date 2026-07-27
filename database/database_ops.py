# Program name: database_ops.py
# Author: Aaron Schelfo
# Date last updated: July 13, 2026
# Purpose: Modular functions executing specialized inserts, modifications, and atomic transactions.

from mysql.connector import Error

from .connection import get_connection


def insert_platform(name, year):
    """Insert a new platform into the database."""
    query = "INSERT INTO Platforms (platform_name, release_year) VALUES (%s, %s);"
    _run_modification(query, (name, year))


def insert_game(title, condition, platform_id):
    """Insert a new game into the database."""
    query = "INSERT INTO Games (game_title, game_condition, platform_id) VALUES (%s, %s, %s);"
    _run_modification(query, (title, condition, platform_id))


def update_game_condition(game_id, status):
    """Update a game's condition."""
    query = "UPDATE Games SET game_condition = %s WHERE game_id = %s;"
    _run_modification(query, (status, game_id))


def update_store_phone(store_id, phone):
    """Update a store phone number."""
    query = "UPDATE Stores SET phone_number = %s WHERE store_id = %s;"
    _run_modification(query, (phone, store_id))


def delete_platform(platform_id):
    """Delete a platform record."""
    query = "DELETE FROM Platforms WHERE platform_id = %s;"
    _run_modification(query, (platform_id,))


def process_checkout_transaction(store_id, sale_date, total_revenue, game_id):
    """Create a sale and link it to a game."""
    conn = get_connection()
    if not conn:
        return

    cursor = None
    try:
        conn.autocommit = False
        cursor = conn.cursor()

        sales_sql = "INSERT INTO Sales (store_id, sale_date, total_revenue) VALUES (%s, %s, %s);"
        cursor.execute(sales_sql, (store_id, sale_date, total_revenue))
        sale_id = cursor.lastrowid

        tx_query = "INSERT INTO Transaction (game_id, sale_id) VALUES (%s, %s)"
        cursor.execute(tx_query, (game_id, sale_id))

        conn.commit()
        print(f"Transaction complete. Sale ID: {sale_id}")
    except Error as exc:
        if conn:
            conn.rollback()
        print(f"Transaction failed: {exc}")
    finally:
        if cursor:
            cursor.close()
        conn.close()


def _run_modification(query, params):
    """Run a single SQL statement and commit it."""
    conn = get_connection()
    if not conn:
        return

    cursor = None
    try:
        cursor = conn.cursor()
        cursor.execute(query, params)
        conn.commit()
        print("Record updated successfully.")
    except Error as exc:
        print(f"Operation failed: {exc}")
    finally:
        if cursor:
            cursor.close()
        conn.close()
        
