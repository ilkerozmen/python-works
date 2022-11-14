html_doc = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>İlk Web Sayfam</title>
</head>
<body>
    <h1 id="header">
        İlker ÖZMEN
    </h1>

    <div class="grup1">
        <h2>
            Programlama
        </h2>

        <ul>
            <li>Menü 1</li>
            <li>Menü 2</li>
            <li>Menü 3</li>
        </ul>
    </div>

    <div class="grup2">
        <h2>
            Modüller
        </h2>

        <ul>
            <li>Menü 1</li>
            <li>Menü 2</li>
            <li>Menü 3</li>
        </ul>
    </div>

    <div class="grup3">
        <h2>
            Django
        </h2>

        <ul>
            <li>Menü 1</li>
            <li>Menü 2</li>
            <li>Menü 3</li>
        </ul>
    </div>

    <img src="fred.jpg" alt="">

    <a class="sister" href="http://example1.com/elsie" id="link1">Link1</a>
    <a class="sister" href="http://example2.com/elsie" id="link2">Link2</a>
    <a class="sister" href="http://example3.com/elsie" id="link3">Link3</a>

</body>
</html>
"""

from bs4 import BeautifulSoup

soup = BeautifulSoup(html_doc, 'html.parser')

# result = soup.prettify()
# result = soup.title
# result = soup.title.name
# result = soup.title.string
# result = soup.head
# result = soup.body
# result = soup.h1
# result = soup.h2
# result = soup.h2.name
# result = soup.h2.string

# result = soup.find_all('h2')
# result = soup.find_all('h2')[0]
# result = soup.find_all('h2')[1]

# result = soup.div
# result = soup.find_all('div')[1]
# result = soup.find_all('div')[1].ul
# result = soup.find_all('div')[1].ul.li
# result = soup.find_all('div')[1].ul.find_all('li')

# result = soup.div.findChildren()
# result = soup.div.find_next_sibling().find_next_sibling().find_previous_sibling()
# result = soup.find_all('a')

# for link in result:
#     print(link)

# for link in result:
#     print(link.get('href'))