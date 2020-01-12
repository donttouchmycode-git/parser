from lxml import html
import requests
import csv

heads_list = []
prices_list = []
pictureLinks_list = []

for j in range (12):
    j += 1
    page = requests.get('https://navi-expert.ru/product_list/page_'+str(j)+'?bss0=2381')
    tree = html.fromstring(page.content)

    for i in range(23):
        i += 1
        heads = tree.xpath('/html/body/div[6]/div[2]/div[1]/div/ul/li['+str(i)+']/a[5]')[0].text
        prices = tree.xpath('/html/body/div[6]/div[2]/div[1]/div/ul/li['+str(i)+']/div[2]/span')[0].text
        pictureLinks = tree.xpath('/html/body/div[6]/div[2]/div[1]/div/ul/li['+str(i)+']/a[4]/img/@src')
        heads_list.append(heads)
        prices_list.append(prices)
        pictureLinks_list.append(pictureLinks)

print('Parsing complete. Wait for file creating')


with open('parce.csv', "w") as csv_file:
    writer = csv.writer(csv_file, delimiter=';')
    writer.writerows(zip(heads_list, prices_list, pictureLinks_list))
