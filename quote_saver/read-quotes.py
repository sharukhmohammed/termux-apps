import sqlite3
import argparse

def get_all_quotes(conn):
	cursor = conn.cursor()
	cursor.execute('SELECT * FROM quotes')
	return cursor.fetchall()

def get_latest_quotes(conn, number):
	cursor = conn.cursor()
	cursor.execute('SELECT * FROM quotes ORDER BY rowid DESC LIMIT ?', (number,))
	return cursor.fetchall()

def get_one_quote(conn):
	cursor = conn.cursor()
	cursor.execute('SELECT * FROM quotes ORDER BY RANDOM() LIMIT 1')
	return cursor.fetchone()

def main(args):
	conn = sqlite3.connect('quotes.db')
	if args.option == 'get_all':
		quotes = get_all_quotes(conn)
		for quote in quotes:
			print(quote)
	elif args.option == 'get_latest':
		quotes = get_latest_quotes(conn, args.number)
		for quote in quotes:
			print(quote)
	elif args.option == 'get_one':
		quote = get_one_quote(conn)
		print(quote)
	conn.close()

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description="Read quotes from the database.")
	parser.add_argument("option", type=str, choices=['get_all', 'get_latest', 'get_one'], help="Operation to perform.")
	parser.add_argument("--number", type=int, default=1, help="Number of latest quotes to fetch.")
	args = parser.parse_args()
	main(args)
