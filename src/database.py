import sqlite3
import json
from typing import List
from src.models import Case

class Database:
    def __init__(self, db_path: str = "finance.db"):
        self.conn = sqlite3.connect(db_path)
        self._create_tables()
    
    def _create_tables(self):
        """Создать таблицы если их нет"""
        self.conn.execute("""
            CREATE TABLE IF NOT EXISTS cases (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                currency TEXT NOT NULL,
                balance REAL NOT NULL,
                hidden INTEGER DEFAULT 0
            )
        """)
        self.conn.commit()
    
    def save_case(self, case: Case):
        """Сохранить кейс"""
        self.conn.execute("""
            INSERT INTO cases (name, currency, balance, hidden)
            VALUES (?, ?, ?, ?)
        """, (case.name, case.currency, case.balance, int(case.hidden)))
        self.conn.commit()
    
    def load_all_cases(self) -> List[Case]:
        """Загрузить все кейсы"""
        cursor = self.conn.execute("SELECT name, currency, balance, hidden FROM cases")
        cases = []
        for row in cursor:
            case = Case(row[0], row[1], row[2], bool(row[3]))
            cases.append(case)
        return cases
    
    def close(self):
        self.conn.close()
    
    