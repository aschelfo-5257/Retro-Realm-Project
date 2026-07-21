# Program Name: connection.py
# Author: Aaron Schelfo
# Date Last Updated: July 21, 2026
# Purpose:

import mysql.connector
from config.database_config import DB_CONFIG

class DBConnection:
  """Custom context manager class to automatically handle open/close cycles."""
  def __init__(self):
    self.conn = None
    self.cursor = None

  def __enter__(self):
    # Open the connection and create a dictionary-based cursor for scannable results
    self.conn = mysql.connector.connect(**DB_CONFIG)
    self.cursor = self.conn.cursor(dictionary=True)
    return self.cursor

  def __exit__(self, exc_type, exc_val, exc_tb):
    # Handle transaction results if an unhandled exception occurred
    if exc_type is not None:
      print(f"\n[Error] Database exception encounter: {exc_val}")
      print("Rolling back any active structural adjustments...")
      self.conn.rollback()
    else:
      self.conn.commit()

    # Clean up database resources
    if self.cursor:
      self.cursor.close()
    if self.conn:
      self.conn.close()
