from lxml import html
import requests
import csv

heads_list = []         #headers list
prices_list = []        #prices lis
pictureLinks_list = []  #picture links list

for j in range (12):     #pagination (13 pages)
    j += 1
    page = requests.get('https://navi-expert.ru/product_list/page_'+str(j)+'?bss0=2381')    
    tree = html.fromstring(page.content)

    for i in range(23): #products on page (24 items)
        i += 1
        heads = tree.xpath('/html/body/div[6]/div[2]/div[1]/div/ul/li['+str(i)+']/a[5]')[0].text            #product header xpath addres
        prices = tree.xpath('/html/body/div[6]/div[2]/div[1]/div/ul/li['+str(i)+']/div[2]/span')[0].text    #proguct price xpath addres
        pictureLinks = tree.xpath('/html/body/div[6]/div[2]/div[1]/div/ul/li['+str(i)+']/a[4]/img/@src')    #proguct picture link xpath addres
        heads_list.append(heads)
        prices_list.append(prices)
        pictureLinks_list.append(pictureLinks)

print('Parsing complete. Wait for file creating')   #Successful message


with open('parce.csv', "w") as csv_file:                                #write result to .csv file...
    writer = csv.writer(csv_file, delimiter=';')
    writer.writerows(zip(heads_list, prices_list, pictureLinks_list))   #... in 3 columns
