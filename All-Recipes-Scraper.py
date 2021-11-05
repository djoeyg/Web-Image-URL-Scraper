import requests
import bs4

# res = requests.get("https://www.allrecipes.com/recipe/228966/mango-tofu-tacos/")
# res = requests.get("https://www.allrecipes.com/recipe/83557/juicy-roasted-chicken/")
# res = requests.get("https://www.allrecipes.com/recipe/72405/chicken-marsala-with-portobello-mushrooms/")
res = requests.get("https://www.allrecipes.com/recipe/278174/chili-with-chorizo-and-chocolate/")
soup = bs4.BeautifulSoup(res.text, 'lxml')

computer = soup.find(attrs={"class": "icon-image-zoom"})
# computer = soup.find(attrs={"data-title": "Juicy Roasted Chicken"})
image_link_1 = computer.get('data-image')
print(image_link_1)

image_src_1 = requests.get(image_link_1)
# print(image_src_1.content)

f = open('./images_folder/chili_chorizo.jpg', 'wb')
f.write(image_src_1.content)
f.close()