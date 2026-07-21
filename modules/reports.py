# Program name: reports.py
# Author: Aaron Schelfo
# Date last updated: July 13, 2026
# Purpose: Analytics parsing layer retrieving record arrays crossing structural table boundaries.

from database_config import get_connection

def get_games_catalog_report():
    """Report Option #1: Relates Games records back to Parent Platforms"""
    query = """
        SELECT G.game_id, G.game_title, G.game_condition, P.platform_name 
        FROM Games G
        INNER JOIN Platforms P ON G.platform_id = P.platform_id;
    """
    return _fetch_records(query)

def get_store_revenue_report():
    """Report Option #2: Tracks processed sales receipts by location profiles"""
    query = """
        SELECT S.sale_id, ST.store_name, S.sale_date, S.total_revenue 
        FROM Sales S
        INNER JOIN Stores ST ON S.store_id = ST.store_id; 
    """
    return _fetch_records(query)

def _fetch_records(query):
    conn = get_connection()
    if not conn: return []
    try:
        cursor = conn.cursor()
        cursor.execute(query)
        return cursor.fetchall()
    except Exception as e:
        print(f"Report formatting failed: {e}")
        return []
    finally:
        cursor.close()
        conn.close()
