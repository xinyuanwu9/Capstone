import re
#import nltk
#import urllib2
import numpy as np
import pandas as pd

# proc_test function is used for test cleaning results
# proc_full function is used for cleaning all reviews
# result is a nested list. Each element is a list of words generated from a review

def get_review_full():
    part1 = pd.read_csv('../ScrapedData/beerreview1_13.csv', usecols = ['review'])
    part2 = pd.read_csv('../ScrapedData/beerreview14_26.csv', usecols = ['review'])
    part3 = pd.read_csv('../ScrapedData/beerreview27_39.csv', usecols = ['review'])
    part4 = pd.read_csv('../ScrapedData/beerreview40_51.csv', usecols = ['review'])
    full = pd.concat([part1, part2, part3, part4], axis = 0, ignore_index = True)
    return list(full['review'])

def get_random_review(n = 20, seed = 0):
    assert n > 0, 'number of reviews must be greater than 0'
    assert n <= 100, 'don\'t do more than 100...'
    assert type(n) is int, 'number of reviews must be an integer'
    lst0 = range(4)
    lst1 = ['1_13.csv', '14_26.csv', '27_39.csv', '40_51.csv']
    lst2 = [111426, 68132, 61043, 36093]
    np.random.seed(seed)
    r0 = int(np.random.choice(lst0, size = 1)[0])
    r1 = lst1[r0]
    r2 = list(np.random.choice(range(lst2[r0]), size = n, replace = False))
    rev = list(pd.read_csv('../ScrapedData/beerreview' + r1, usecols = ['review'])['review'])
    return [rev[x] for x in r2]

def clean_str(s):
    s = s.lower().replace('\xe2\x80\x99', '\'').replace('|', ' ').\
        replace('\r', ' ').replace('\n', ' ').replace('/', ' ')
    s = re.sub('[.:\',\-!;"()?]', '', s)
    s = re.sub('\s+', ' ', s).strip().split(' ')
    return s

def proc_test(n = 20, seed = 0):
    l = get_random_review(n, seed)
    return map(clean_str, l)

def proc_full():
    l = get_review_full()
    return map(clean_str, l)





