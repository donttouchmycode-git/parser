from lxml import html
import requests
import csv
import os

heads_list = []
prices_list = []
pictureLinks_list = []
product_links = []
filename_list = []
output_directory = '/home/user/parcer/img/'

for j in range (12):
    j += 1
    page = requests.get('https://navi-expert.ru/product_list/page_'+str(j)+'?bss0=2381')
    tree = html.fromstring(page.content)

    for i in range(23):
        i += 1
        heads = tree.xpath('/html/body/div[6]/div[2]/div[1]/div/ul/li['+str(i)+']/a[5]')[0].text
        product_link = tree.xpath('/html/body/div[6]/div[2]/div/div/ul/li['+str(i)+']/a[5]')[0].get('href')
        prices = tree.xpath('/html/body/div[6]/div[2]/div[1]/div/ul/li['+str(i)+']/div[2]/span')[0].text
        pictureLinks1 = str(tree.xpath('/html/body/div[6]/div[2]/div[1]/div/ul/li['+str(i)+']/a[4]/img/@src'))
        pictureLinks2 = str(tree.xpath('/html/body/div[6]/div[2]/div[1]/div/ul/li['+str(i)+']/a[4]/img/@longdesc'))
        if "static" in pictureLinks1:
            pictureLinks = pictureLinks2
        else:
            pictureLinks = pictureLinks1
        pictureLinks = pictureLinks.replace('w200_h200', 'w640_h640')
        filename = pictureLinks.split("/")[-1][:-2]
        url = str(pictureLinks)[1:-1]
        #print(filename)
        #print(pictureLinks)
        #print(url)
        os.system('cd /home/user/parcer/img && wget '+ url)    #comment this string if only data save needed without downloading images
        heads_list.append(heads)
        prices_list.append(prices)
        pictureLinks_list.append(pictureLinks)
        filename_list.append(filename)

print('Parsing complete. Wait for file creating')


with open('/home/user/parcer/parce.csv', "w") as csv_file:
    writer = csv.writer(csv_file, delimiter=';')
    writer.writerows(zip(heads_list, prices_list, filename_list))
