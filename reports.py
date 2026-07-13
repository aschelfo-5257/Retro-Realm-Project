def inventory_breakdown(conn):
    """Option 5 - Report 1: 2-Table Join Matrix."""
    cursor = conn.cursor()
    query = """
        SELECT G.game_id, G.game_title, P.platform_name 
        FROM Games G
        INNER JOIN Platforms P ON G.platform_id = P.platform_id;
    """
    cursor.execute(query)
    print("\n--- Relational Inventory Matrix ---")
    for (g_id, title, platform) in cursor.fetchall():
        print(f"[{g_id}] {title} -> Platform: {platform}")
    cursor.close()
