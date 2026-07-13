from datetime import date
import mysql.connector

def insert_new_game(conn, title, condition, platform_id):
    """Option 1: Add a record to the Games table."""
    cursor = conn.cursor()
    query = "INSERT INTO Games (game_title, game_condition, platform_id) VALUES (%s, %s, %s)"
    cursor.execute(query, (title, condition, platform_id))
    conn.commit()
    cursor.close()
    print("✨ Game cataloged successfully!")

def change_game_condition(conn, game_id, new_condition):
    """Option 2: Update a record in the Games table."""
    cursor = conn.cursor()
    query = "UPDATE Games SET game_condition = %s WHERE game_id = %s"
    cursor.execute(query, (new_condition, game_id))
    conn.commit()
    cursor.close()
    print("✏️ Condition matrix updated!")

def remove_game(conn, game_id):
    """Option 3: Delete a record from the Games table."""
    cursor = conn.cursor()
    query = "DELETE FROM Games WHERE game_id = %s"
    cursor.execute(query, (game_id,))
    conn.commit()
    cursor.close()
    print("🗑️ Game removed from active inventory.")

def process_sales_transaction(conn, store_id, game_id, price):
    """Option 4: Multi-statement transaction sequence."""
    today = date.today().strftime('%Y-%m-%d')
    cursor = conn.cursor()
    try:
        conn.start_transaction()
        
        # Action 1: Create master invoice record
        sales_query = "INSERT INTO Sales (store_id, sale_date, total_revenue) VALUES (%s, %s, %s)"
        cursor.execute(sales_query, (store_id, today, price))
        invoice_id = cursor.lastrowid
        
        # Action 2: Link game entry item
        tx_query = "INSERT INTO Transaction (game_id, sale_id) VALUES (%s, %s)"
        cursor.execute(tx_query, (game_id, invoice_id))
        
        conn.commit()
        print(f"✅ Transaction secured! Invoice #{invoice_id} locked in.")
    except mysql.connector.Error as error:
        conn.rollback()
        print(f"❌ Warning trace detected. Rolling back transaction: {error}")
    finally:
        cursor.close()
