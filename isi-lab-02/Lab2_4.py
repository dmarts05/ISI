from urllib.request import urlopen
from urllib.error import URLError

url = input("Please, enter a url (https://example.com): ")
try:
    words = 0
    with urlopen(url) as response:
        for line in response:
            words += len(line.decode().strip().split())

    print(f"Number of words: {words}")
except URLError:
    print("Invalid or nonexistent URL, try again...")
