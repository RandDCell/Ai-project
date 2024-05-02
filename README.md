import requests
from bs4 import BeautifulSoup
import pandas as pd
url = "https://www.iplt20.com/auction/2024"
r = requests.get(url)
#print(r)
soup = BeautifulSoup(r.text, "html.parser")
#print(soup)
table = soup.find("table", class_="ih-td-tab auction-tbl")
title = table.find_all("th")
header =[]
for i in title:
    header.append(i.text)
#print(header)
df = pd.DataFrame(columns = header)
rows = table.find_all("tr")
for i in rows[1:]:
    first_td=i.find_all("td")[0].find("div",class_="ih-pt-ic").text.strip()
    data = i.find_all("td")[1:]
    row=[tr.text for tr in data]
    row.insert(0,first_td)
    df.loc[len(df)] = row


print(df)
df.to_csv("C:/Users/WB-CY/PycharmProjects/ipl.csv")




