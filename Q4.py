'''4. Provide a program to read the file from URL and display the content
in terminal.
• The file URL has to be input by the user.
• The program has to work from the terminal. The input and output have been taken/displayed
on the terminal.'''

import urllib3  # the lib that handles the url stuff
url = str(input("input url:"))
connection_pool = urllib3.PoolManager()
resp = connection_pool.request('GET',url )
print(resp.data)
