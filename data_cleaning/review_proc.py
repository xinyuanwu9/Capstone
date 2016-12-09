import re
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import numpy as np
import pandas as pd
import pickle

### proc_test function is used for test cleaning results
### proc_full function is used for cleaning all reviews
### result is a nested list. Each element is a list of words generated from a review

# function set 1. get nested list of words
def get_review_full():
    '''output: list, each element is a review str'''
    part1 = pd.read_csv('github/ScrapedData/beerreview1_13.csv', usecols = ['review'])
    part2 = pd.read_csv('github/ScrapedData/beerreview14_26.csv', usecols = ['review'])
    part3 = pd.read_csv('github/ScrapedData/beerreview27_39.csv', usecols = ['review'])
    part4 = pd.read_csv('github/ScrapedData/beerreview40_51.csv', usecols = ['review'])
    full = pd.concat([part1, part2, part3, part4], axis = 0, ignore_index = True)
    return ['' if type(x) is not str else x for x in list(full['review'])]

def get_random_review(n = 20, seed = 0):
    '''input: n = number of review you want to generate, seed = random seed number
       output: list, each element is a review str'''
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
    rev = list(pd.read_csv('github/ScrapedData/beerreview' + r1, usecols = ['review'])['review'])
    rev = ['' if type(x) is not str else x for x in rev]
    return [rev[x] for x in r2]

def get_beername_full():
    '''output: list of all reviews, each element is a review str'''
    part1 = pd.read_csv('github/ScrapedData/beerreview1_13.csv', usecols = ['beer_name'])
    part2 = pd.read_csv('github/ScrapedData/beerreview14_26.csv', usecols = ['beer_name'])
    part3 = pd.read_csv('github/ScrapedData/beerreview27_39.csv', usecols = ['beer_name'])
    part4 = pd.read_csv('github/ScrapedData/beerreview40_51.csv', usecols = ['beer_name'])
    full = pd.concat([part1, part2, part3, part4], axis = 0, ignore_index = True)
    print 'beer name loaded'
    print '='*100
    return list(full['beer_name'])


def clean_str(s):
    '''input: review str
       output: list of words'''
    s = s.lower().replace('\xe2\x80\x99', '\'').replace('|', ' ').\
        replace('\r', ' ').replace('\n', ' ').replace('/', ' ')
    s = re.sub('[.:\',\-!;"()?]', '', s)
    lst = re.sub('\s+', ' ', s).strip().split(' ')
    stop_words = set(stopwords.words('english') + stopwords.words('german') + ['&'])
    lst = [word for word in lst if word not in stop_words]
    lmtizer = WordNetLemmatizer()
    lst = map(lambda x: lmtizer.lemmatize(x.decode('utf-8')).encode('ascii', 'ignore'), lst)
    return lst

def proc_review_test(n = 20, seed = 0):
    '''test function'''
    l = get_random_review(n, seed)
    return map(clean_str, l)

def proc_review_full():
    '''output: nested list, each inner list is a list of words, all reviews are processed'''
    l = get_review_full()
    print 'all reviews are loaded'
    print '='*100
    result = []
    i = 0
    for review in l:
        result.append(clean_str(review))
        i += 1
        print 'number of review finished:', i
    return result





# function set 2. for getting nested list
def org_tuple(name, z):
    '''input: beer name, list of tuple
       output: list of words for a single beer, all reviews considered'''
    ls = []
    for i in z:
        if i[0] == name:
            ls.append(i[1])
    return [item for sublist in ls for item in sublist]

def group_words(name_lst, rev_lst):
    '''input: name list, revies list
       output: list of tuple'''
    assert len(name_lst) == len(rev_lst), 'name_lst must equal to rev_lst'
    z = zip(name_lst, rev_lst)
    s = list(set(name_lst))
    s.sort()
    ls = []
    for name in s:
        ls.append((name, org_tuple(name, z)))
        print 'review of beer:', name, 'has been processed'
    return ls



def do_this_shit():
    '''run this for the entire process, make sure you set the right path for each file'''
    name_lst = get_beername_full()
    print 'name_lst generated'
    print '='*100, '\n\n'
    rev_lst = proc_review_full()
    print 'all reviews processed'
    print '='*100, '\n\n'
    result_all = group_words(name_lst, rev_lst)
    print 'finished!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'
    print '='*100, '\n\n'
    nest_lst = map(lambda x: x[1], result_all)
    name_lst = map(lambda x: x[0], result_all)
    print 'word and name list generated\n\n'
    print 'dumping files'
    pickle.dump(nest_lst, open('words_lst.p', 'wb'))
    pickle.dump(name_lst, open('name_lst.p', 'wb'))
    print 'files dumped!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'
    print 'job done!'



def test_this_shit(n = 5, seed = 0):
    '''test function'''
    name_lst = np.random.choice(range(5), size = n, replace = True)
    rev_lst = proc_review_test(n, seed)
    return group_words(name_lst, rev_lst)












# function set 3. spell check assist

## input a list of words, return the sum of individual word length + space between words
def count_lst_chr(lst):
    l = 0
    for i in lst:
        l += len(i)
    return l + len(lst) - 1



