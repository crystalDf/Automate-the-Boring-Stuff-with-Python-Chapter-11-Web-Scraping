import requests

res = requests.get('http://www.gutenberg.org/cache/epub/1112/pg1112.txt')
print(type(res))

print(res.status_code == requests.codes.ok)

print(len(res.text))

print(res.text[:250])

# res = requests.get('http://inventwithpython.com/page_that_does_not_exist')

try:
    res.raise_for_status()
    play_file = open('RomeoAndJuliet.txt', 'wb')
    for chunk in res.iter_content(100000):
        print(play_file.write(chunk))
    play_file.close()
except Exception as exc:
    print('There was a problem: %s' % exc)

# The iter_content() method returns “chunks” of the content on each iteration
# through the loop. Each chunk is of the bytes data type, and you get to
# specify how many bytes each chunk will contain. One hundred thousand bytes
# is generally a good size, so pass 100000 as the argument to iter_content().
