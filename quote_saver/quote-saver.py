import argparse
import sqlite3
import json
import sys
import time

import requests


def get_quote():
    url = "https://api.forismatic.com/api/1.0/?method=getQuote&lang=en&format=json"
    response = requests.get(url)
    body = response.text.replace("\\'", "'")
    if response.status_code == 200:
        quote_data = json.loads(body)
        quote_dict = {
            "quoteText": quote_data.get("quoteText").strip(),
            "quoteAuthor": quote_data.get("quoteAuthor").strip(),
            "senderName": quote_data.get("senderName").strip(),
            "senderLink": quote_data.get("senderLink").strip(),
            "quoteLink": quote_data.get("quoteLink").strip()
        }
        return quote_dict
    else:
        return None


def insert_quote(quote, conn):
    cursor = conn.cursor()
    cursor.execute('''
		INSERT OR REPLACE INTO quotes (quoteText, quoteAuthor, senderName, senderLink, quoteLink) 
		VALUES (:quoteText, :quoteAuthor, :senderName, :senderLink, :quoteLink)
	''', quote)
    conn.commit()


def main(args):
    conn = sqlite3.connect('quotes.db')
    print(f'Quotes Saver === {sys.version}')
    print(f"Getting {args.num} Quotes ")
    for index in range(args.num):
        try:

            quote = get_quote()
            if quote:
                print(f'{index+1} => {quote}')
                insert_quote(quote, conn)
            else:
                print("Failed to retrieve quote.")
        except Exception as e:
            print(f"Getting {index} Quote ERROR! {e}")
        finally:
            time.sleep(1.5)
    conn.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Fetch quotes from Forismatic API and store in database.")
    parser.add_argument("num", type=int, help="Number of quotes to fetch.")
    args = parser.parse_args()
    main(args)
