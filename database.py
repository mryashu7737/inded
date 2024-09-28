# # database.py

# # ... (other imports and connection setup)

# # Create the 'Income' table 
# c.execute('''
#     CREATE TABLE IF NOT EXISTS Income (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         user TEXT,
#         source TEXT,
#         amount REAL,
#         date_received TEXT
#     )
# ''')

# # Create the 'Deductions' table 
# c.execute('''
#     CREATE TABLE IF NOT EXISTS Deductions (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         user TEXT,
#         category TEXT, # Or adjust to 'deduction_type' if that's what you use in app.py
#         amount REAL,
#         date_incurred TEXT
#     )
# ''')

# # Create the 'TaxCredit' table
# c.execute('''
#     CREATE TABLE IF NOT EXISTS TaxCredit (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         user TEXT,
#         credit_type TEXT,
#         amount REAL,
#         date_claimed TEXT
#     )
# ''')

# # ... (commit and close connection)
import sqlite3

conn = sqlite3.connect('tax_tracking.db')
c = conn.cursor()

# Create tables
c.execute('''
    CREATE TABLE IF NOT EXISTS Income (
        id INTEGER PRIMARY KEY,
        user TEXT,
        source TEXT,
        amount REAL,
        date_received TEXT
    )
''')

c.execute('''
    CREATE TABLE IF NOT EXISTS Deduction (
        id INTEGER PRIMARY KEY,
        user TEXT,
        deduction_type TEXT,
        amount REAL,
        date_incurred TEXT
    )
''')

c.execute('''
    CREATE TABLE IF NOT EXISTS TaxCredit (
        id INTEGER PRIMARY KEY,
        user TEXT,
        credit_type TEXT,
        amount REAL,
        date_claimed TEXT
    )
''')

conn.commit()
conn.close()
