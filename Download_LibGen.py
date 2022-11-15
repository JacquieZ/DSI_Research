import requests
from bs4 import BeautifulSoup
import pandas as p

df_Socio = p.read_csv('Socio_all.csv',error_bad_lines=False)
df_Psych = p.read_csv('Psych_all.csv',error_bad_lines=False)
df_OB = p.read_csv('OB_all.csv',error_bad_lines=False)
df_Neuro = p.read_csv('Neuro_all.csv',error_bad_lines=False)

DOIs = list(df_Socio['DOI']+df_Psych['DOI']+df_Neuro['DOI']+df_OB['DOI'])
print(len(DOIs))
#url = 'https://libgen.lc/ads.php?doi=10.1111/j.1469-7610.1993.tb00964.x'
file_num = 0
for DOI in DOIs:
    base_url = 'https://libgen.rocks/ads.php?doi='
    response = requests.get(base_url + DOI)
    soup = BeautifulSoup(response.content, 'html.parser')
    content = soup.find_all('a',href=True)
    for link in content:
       if link.get('href').startswith('get.php?'):
           url = "https://libgen.rocks/"+link.get('href')

           response = requests.get(url)
           pdf = open(str(file_num)+".pdf", 'wb')
           pdf.write(response.content)
           pdf.close()
           file_num+=1

# 98492 DOIs to search
