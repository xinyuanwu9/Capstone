'''
Build .csv file with only username, user rating, and beer for Collaborative Filtering
written by Nelson Chen 12/10/16
'''

import pandas as pd

# beer csv files
beer_rating1 = pd.read_csv('../Scraped_Review_Data/beerreview1_13.csv')
beer_rating2 = pd.read_csv('../Scraped_Review_Data/beerreview14_26.csv')
beer_rating3 = pd.read_csv('../Scraped_Review_Data/beerreview27_39.csv')
beer_rating4 = pd.read_csv('../Scraped_Review_Data/beerreview40_51.csv')

# Combine into one csv
beer_rating = pd.concat([beer_rating1,beer_rating2,beer_rating3,beer_rating4], ignore_index=True)

# use only username, userrating, and beername columns
beer_rating = beer_rating[['user_name','overall','beer_name']]

# write to new csv
#beer_rating.to_csv('beer_ratings_only.csv', index = False)

print beer_rating['user_name'].unique().shape