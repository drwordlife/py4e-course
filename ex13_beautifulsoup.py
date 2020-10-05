import urllib.request
import re

from bs4 import BeautifulSoup


def get_word_counts(handle):
    counts = dict()
    for line in handle:
        words = line.decode().split()
        for word in words:
            counts[word] = counts.get(word, 0) + 1

    return counts


#  Sample data: http://py4e-data.dr-chuck.net/comments_42.html (Sum=2553)
#  Actual data: http://py4e-data.dr-chuck.net/comments_1008612.html (Sum ends with 42)
def find_sum_of_numbers(soup):
    tags = soup('span')
    total = 0
    for tag in tags:
        total = total + int(tag.contents[0])

    print(total)


# Sample problem: Start at http://py4e-data.dr-chuck.net/known_by_Fikret.html
# Find the link at position 3 (the first name is 1). Follow that link. Repeat this process 4 times. The answer is the last name that you retrieve.
# Sequence of names: Fikret Montgomery Mhairade Butchi Anayah
# Last name in sequence: Anayah
# Actual problem: Start at: http://py4e-data.dr-chuck.net/known_by_Safia.html
# Find the link at position 18 (the first name is 1). Follow that link. Repeat this process 7 times. The answer is the last name that you retrieve.
# Hint: The first character of the name of the last page that you will load is: M

url = input('Enter: ')
if len(url) < 1:
    url = 'http://py4e-data.dr-chuck.net/known_by_Safia.html'

count = int(input('Enter count: '))
pos = int(input('Enter position: '))

for i in range(count):
    handle = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(handle, 'html.parser')
    tags = soup('a')
    links = [tag['href'] for tag in tags[:pos]]
    names = [tag.string for tag in tags[:pos]]
    url = links[-1]
    name = names[-1]

print(name)