import requests
import bs4

res = requests.get("https://en.wikipedia.org/wiki/Deep_Blue_(chess_computer)")

soup = bs4.BeautifulSoup(res.text, 'lxml')

# Image 1 download & save to folder

computer = soup.find(attrs={"alt": "Deep Blue.jpg"})
image_link_1 = "http:" + computer.get('src')
print(image_link_1)

image_src_1 = requests.get(image_link_1)
print(image_src_1.content)

f = open('./images_folder/deep_blue.jpg', 'wb')
f.write(image_src_1.content)
f.close()

# Image 2 download & save to folder

chess = soup.find(attrs={"height": "165"})
image_link_2 = "http:" + chess.get('src')
print(image_link_2)

image_src_2 = requests.get(image_link_2)
print(image_src_2.content)

f = open('./images_folder/chess_player.png', 'wb')
f.write(image_src_2.content)
f.close()

# print(soup.img['src'], "\n")

# images = soup.findAll('img')
# for elem in images:
#    print(elem['src'])

# pics = soup.find_all('img')
# for p in pics:
#     if p.has_attr('src'):
#         print(p['src'])
