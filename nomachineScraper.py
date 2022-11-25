
import requests
#import bs4
from bs4 import BeautifulSoup
import tqdm

url = 'https://downloads.nomachine.com/download/?id=5'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')
# print(soup)

#parse html and get link from id=link_download
link = soup.find(id='link_download')

#parse link and get only href
href = link.get('href')
print('Downloading '+href.split('/')[-1])

#download href file with tqdm
requests.get(href, stream=True)
response = requests.get(href, stream=True)
total_size_in_bytes= int(response.headers.get('content-length', 0))
block_size = 1024 #1 Kibibyte
progress_bar = tqdm.tqdm(total=total_size_in_bytes, unit='iB', unit_scale=True)


#with open get same name file from link
with open(href.split('/')[-1], 'wb') as file:
    for data in response.iter_content(block_size):
        progress_bar.update(len(data))
        file.write(data)
progress_bar.close()
if total_size_in_bytes != 0 and progress_bar.n != total_size_in_bytes:
    print("ERROR, something went wrong")





        



