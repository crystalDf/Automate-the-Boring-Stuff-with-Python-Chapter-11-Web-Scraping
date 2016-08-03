import requests
import bs4

res = requests.get("https://www.nostarch.com")
res.raise_for_status()
no_starch_soup = bs4.BeautifulSoup(res.text)
print(type(no_starch_soup))

example_file = open("example.html")
example_soup = bs4.BeautifulSoup(example_file)
print(type(example_soup))

elems = example_soup.select('#author')
print(type(elems))
print(len(elems))
print(type(elems[0]))
print(elems[0].getText())
print(str(elems[0]))
print(elems[0].attrs)

p_elems = example_soup.select('p')
print(str(p_elems[0]))
print(p_elems[0].getText())
print(str(p_elems[1]))
print(p_elems[1].getText())
print(str(p_elems[2]))
print(p_elems[2].getText())

span_elem = example_soup.select('span')[0]
print(str(span_elem))
print(span_elem.get('id'))
print(span_elem.get('some_nonexistent_addr') is None)
print(span_elem.attrs)
