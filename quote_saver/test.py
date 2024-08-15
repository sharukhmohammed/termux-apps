import json

json_str = u'{"quoteText":"He can who thinks he can, and he can\'t who thinks he can\'t. This is an inexorable, indisputable law.", "quoteAuthor":"Pablo Picasso", "senderName":"", "senderLink":"", "quoteLink":"http://forismatic.com/en/fbcc8a13d4/"}'
obj = json.loads(json_str)

print(obj)