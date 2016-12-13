import urllib
import pandas as pd
import time

beer_data = pd.read_csv('beer_info_proc.csv')

for i in range(575,beer_data.shape[0]):
    time.sleep(1)
    url = beer_data.loc[i,'beer_img']
    beer_name = beer_data.loc[i,'beer_name']
    file_name = '../beer_images/' + beer_name + '.png'
    urllib.urlretrieve(url, file_name)
