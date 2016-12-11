import pandas as pd

beer_rating1 = pd.read_csv('../Scraped_Review_Data/beerreview1_13.csv')
beer_rating2 = pd.read_csv('../Scraped_Review_Data/beerreview14_26.csv')
beer_rating3 = pd.read_csv('../Scraped_Review_Data/beerreview27_39.csv')
beer_rating4 = pd.read_csv('../Scraped_Review_Data/beerreview40_51.csv')

beer_rating = pd.concat([beer_rating1,beer_rating2,beer_rating3,beer_rating4], ignore_index=True)
beer_rating = beer_rating[['user_name','user_rating','beer_name']]

beer_rating.to_csv('beer_ratings_only.csv', index = False)
