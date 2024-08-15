import sqlite3

def create_database():
	# Connect to SQLite database (or create it if it doesn't exist)
	conn = sqlite3.connect('quotes.db')
	cursor = conn.cursor()
	
	# Create table
	cursor.execute('''
		CREATE TABLE IF NOT EXISTS quotes (
			quoteText TEXT PRIMARY KEY,
			quoteAuthor TEXT,
			senderName TEXT,
			senderLink TEXT,
			quoteLink TEXT
		)
	''')
	
	# Commit the changes and close the connection
	conn.commit()
	conn.close()

if __name__ == "__main__":
	create_database()
	print("Database and table created successfully.")
