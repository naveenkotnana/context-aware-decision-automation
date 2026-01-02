import sqlite3
import os


class Database:
    def __init__(self, db_name="decisions.db"):
        self.db_name = db_name
        self._initialized = False

    def _get_connection(self):
        return sqlite3.connect(self.db_name, check_same_thread=False)

    def initialize(self):
        """Call this ONCE, not during import"""
        if self._initialized:
            return

        try:
            conn = self._get_connection()
            cursor = conn.cursor()

            cursor.execute("""
            CREATE TABLE IF NOT EXISTS decisions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                request_text TEXT,
                urgency TEXT,
                action TEXT
            )
            """)

            conn.commit()
            conn.close()
            self._initialized = True

        except Exception as e:
            print("Database init failed:", e)

    def insert_decision(self, request_text, urgency, action):
        try:
            conn = self._get_connection()
            cursor = conn.cursor()

            cursor.execute("""
            INSERT INTO decisions (request_text, urgency, action)
            VALUES (?, ?, ?)
            """, (request_text, urgency, action))

            conn.commit()
            conn.close()

        except Exception as e:
            print("DB insert failed:", e)
