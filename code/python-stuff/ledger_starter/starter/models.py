import sqlite3
from pathlib import Path
from typing import Any

# specify where the database will be located
ROOT = Path(__file__).parent
DB_PATH = ROOT / "ledger.db"


# initialize the database
def initialize() -> None:
    connection = sqlite3.connect(DB_PATH)
    connection.executescript((ROOT / "schema.sql").read_text())
    connection.commit()
    connection.close()

# query the database

# by the way, the tuple has to have a definitive shape, adding an ellipsis indicates that a tuple with an underfined shape can be passed
def query(sql: str, values: tuple[str | float, ...] | tuple[()] = ()) -> list[Any]:
    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row
    rows = connection.execute(sql, values).fetchall()
    connection.commit()
    connection.close()
    return rows

# get expenses
def get_expenses() -> list[Any]:
    return query("SELECT * FROM expenses ORDER BY entry_date DESC, id DESC")

# add expenses
def add_expense(entry_date: str, description: str, category: str, amount: float) -> None:
    query(
        "INSERT INTO expenses (entry_date, description, category, amount) VALUES (?, ?, ?, ?)",
        (entry_date, description, category, amount),
    )

# get revenues
def get_revenues() -> list[Any]: 
    return query(
        '''
        SELECT * 
        FROM revenues 
        ORDER BY entry_date DESC, id DESC
        '''
    )

# add revenues
def add_revenue(entry_date: str, description: str, category: str, amount: float) -> None:
    query(
        "INSERT INTO revenues (entry_date, description, category, amount) VALUES (?, ?, ?, ?)",
        (entry_date, description, category, amount)
    )


# Sprint 1: add get_revenues() and add_revenue().
# Sprint 2: add summary() with separate SUM queries for each table.
