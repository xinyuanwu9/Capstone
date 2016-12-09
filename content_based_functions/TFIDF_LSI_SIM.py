################### td-idf then LSI finally similarity matrix ###################

from gensim import corpora, models, similarities
import collections

### Input to function is a nested list (of tokens) where each inner list is a document ###
def TFIDF_LSI_SIM(texts, ntopics = 500, filter_threshold = 10):

    # Flatten list to one large list of words
    textsFlatten = [item for sublist in texts for item in sublist]

    # Dictionary of word frequency count
    freq = collections.Counter(textsFlatten)

    # Filter out low frequency items (maintain nested list format)
    texts_filtered = [[item for item in text if freq[item] > filter_threshold] for text in texts]

    # Convert texts to corpora's dictionary object
    textDict = corpora.Dictionary(texts_filtered)

    # list of bag of words
    corpus = [textDict.doc2bow(text) for text in texts_filtered]

    # Build tf-idf model from corpus text
    tfidf = models.TfidfModel(corpus)

    # LSI based on tfidf format and the dimension reduction
    lsi = models.LsiModel(tfidf[corpus], id2word=textDict, num_topics=ntopics)

    # Compute similarity matrix (cosine similarity)
    index = similarities.MatrixSimilarity(lsi[corpus])

    return textDict, index

##### Test Case #####
if __name__ == '__main__':

    text = ['held with with lots melted decent amount honey more starting earthy with mossy mushroom melts tart graphite tang brings more notes finishes fruity reminiscent grigio with honey different expected more think this could killer restrained more poured with billowy with everlasting belgian with typical tropical fruit aromas with spice smooth sticky touches malty sweetness along with notes spices tropical fruits carbonation biting complements rather sweet ddespuma trappe chalice detective drier maybe this makes more spiced alcohol noticeable think prefer this isnt either fruit belgian hint alcohol berries sweetness belgian tart warming alcohol melle gold with snowy carpet more floral honey spice sweet tang slight banana hint tart smooth aimed girly unfortunately smooth easy spiced enough balance theres this coconut butter thats probably diacetyl arresting innocuous nowhere near worth kind booze pours gold with lacingsmells fruity belgian fruity banana apples pepper cloves slight floral sweetness aftertaste carbonation refreshing different enough seem necessary nonetheless nicely carbonated linger with sweet fruitiness this drinkable alcohol undectable poured corked belgian goblet appearance pours with moderate amount settles thin layer fruity driven with scent belgian style fruit esters spices belgian with scent spice hints clove coriander fruit hints lemon banana apple sweet scent belgian candied hints hints floral belgian fruity driven belgian with notes fruit spices belgian with clove pepper coriander fruit notes lemon banana apple notes sweet candied subtle notes floral mouthfeel bodied with carbonation drying somewhat acidic alcohol masked belgian fruit esters spices with smooth drying poured chalice glassappearance pours with fizzy fades rather fast slowing subdues then retention fades further foamy spotty with foamy surface quite yeasty fruity peach tons bubblegum this with probably actually strongest this complimented nicely coriander clove aromas balancing rather with mixed with with deliciously sweet robust begins drier then anticipating with rather crackery mixed with these flavors rather decently strong spice flavors coriander clove with both spice ramping advances candied upfront which fades more with replaced fruits detected while boozy flavors begin developing with starting more subdued getting decently strong with develop with rather boozy rather flavorful linger mouthfeel thin strong with carbonation average composed peppery although carbonation would more invigorating rather though complimented flavors nicely this rather refreshing strong enjoyable disappoints version poured slowly sidewalls corked gold with fizzy carbonation transparent typical belgian sweeter fruit slight spiceyness tastes wine apple juice peppery doesn seem prominent with blonde belgian more noticeable with aftertaste lingering flavors aftertaste more quencher dehydrator though which surprising easy favorite anyrhing summer this significant appeal chardonay chamagne poured somewhat gingerly snifter gold lots effervescence sprinting thick sudsy maybe mention deafening occurred when removed fizz erupting elephant batman delicate combination spice sweetness grainy bready citrus lemon booze hiding refreshing imitates however sweetness would dryness levels dryness makes more more spice spices used both guessed active carbonation fizzy refreshing aspect finishes super maybe those your satisfying pleasant reviewer mention shows theyre capable though typically thought male default unisex brouwerijj compliments bottled pours fairly with fairly dense fluffy with retention reduces lingers spotty soapy lacing clings with amount streaming carbonation retaining aromas lemon']
    text.append('lime apricot apple pepper earthiness damn aromas with balance complexity fruity earthy notes with lemon lime apricot apple pepper earthiness amount peppery spiciness bitterness with lingering notes lemon lime apricot apple pepper earthiness damn complexity balance fruity moderate flavors with balance cloying flavors carbonation bodied with smooth bready mouthfeel amount dryness alcohol with minimal warming present this excellent belgian strong complexity balance fruity moderate flavors smooth enjoyable with revamped drier spicier latest with fruity interwoven streams carbonation easily mistaken cottony froth with spice wine with lightest backdrop wafter thin sweetness floral upstart session simply blossoms effervescence engulfs with apple lemon tangy berries acts dissolves slender sweetness with ease ushers pepper clove freshly grated pepper seed coriander tart vinous acidity despite strong alcohol dryness resonate with balance fresh peppery aftertaste continues dryly fruit excellent this refreshing blond enjoyed highly recommend pairing with suitable instance corked marked sampled decent sized sits until pleasing with belgian belgian clean this style quite refreshing carbonation senses once belgian toasted sweetness poured corked goblet moderate reads dated presumably with exceptional clarity initial coarse sudsy retention scant lacing fruity belgian with flashes fruit yeasty spice yielding gradual finishes quite with lingering bitterness aftertaste clean alcohol presence carbonation with linger effervescence initially acquires texture settles fruit notes while this certainly distinct recollection snifter pours with fluffy active slowly fizzed thick film bready mild spiciness perfumey fruits earthy leafy hints fruits peach apricot biscuity earthy fruity slight mineraliness with addition vinous mint crips bready crackery doughy earthy leafy with bitterness wine fruits aftertaste lingering peppery spice slight fizzy active carbonation luckily drinkability texture reminds clean sweet mouthfeel while since this enjoyable belgian easy with wine appearance pours mildly aggressively with typical style with acceptable retention lacing pleasantly fruitiness citrus apple apricot exist seem quite delicate given picking hint akin while makes ridiculously delicate initial combination citrus candied makes think fruit with maltiness subdued favor esters complain more alcohol through actually once opens properly alcohol profile goes entirely leaving delicate citrus mouthfeel combination slender conspire mild booziness typical style quite fizzy chugging this weren feeling bloated prefer alcohol this effort bspas makes seem more delicate told this damn bspa sarcasm with belgian picked follow lemon belgian floral bitterness create belgian refreshing easy consume this poured goblet with appearance thin disappears lacing crackers booze pepper notes crackers sweet citrus notes lemon booze effervescent booze lingers drinkable though booze through this with swedish meatballs potatoes lingon held compliment this style moderate sweet newest female team information style belgian strong available bottles poured served fahrenheit appearance pours clarity carbonation plentiful vivacious retention excellent lacing moderately thick patchy with belgian strain characteristics with notes peppery spice floral cider fruit lemon notes subtle with equally bitterness potency moderate clean sweet with matching bitterness profile lends notes lemon rind mild mouthfeel texture clean moderately acidic carbonation mouthfeel style balance acidic sweet alcohol presence perceivable characters clean mouthfeel lady commend skilled together this clean collectively difficult assemble floral characteristics mild mannered volumes recommended sdeliria')
    text.append('Approximately 4 oz. from a 12 oz. can, consumed on 6-7-16. Pours a mostly clear but slightly hazy dull copper to dark amber with a small to moderate amount of beige head. Juicy, fruity, toffee aroma. Scents of apricot, watermelon, and melon-flavored gum. Way too fruity in aroma for my preferences. Milky, cardboard, plastic, off flavor. Drier than the aroma implies. Theres an astringency that is unpleasant. Awful at first but settles in to being merely very bad. Definitely flawed. Medium body. Reasonably lively. Forgettable palate effects. One of the worst bottled or canned beers Ive ever had. Id take a typical, boring, flavor-free, macro American pale lager over this any day')
    text.append('3.4 Minnesota Trip Beer #157. 12 ounce can from North Loop Spirits, 5/11/16. Hazy dark copper, large foamy tan head, good retention. Aroma of piney, tropical hops and caramel. The taste is toffee, caramel, leafy and piney hops. Thin. Nice aroma, kinda falls a little flat after that. A good start at least.  |1.6|3.4|3.5|2.9|3.7')
    text.append('Throw in from a trade with GreatDane 1632...Pours a golden amber color with big fluffy head. Aromas of sweet malts, hops, and some fruity notes. Flavor is hoppy malty with a nice dry finish')
    text.append('Dark amber/cider color; Medium creamy body; Aroma of toasted malt, caramel, hops, & some fruit; Flavor of sweet malt, toffee, caramel, and spicy hops; Finish is slightly bitter; Good')
    text.append('The aroma has much malt, and as I sip, I taste the herbal, vegetal hops. Taste is normal; not too sweet, not too bitter, not sour at all. The body is medium, with some soft carbonation. Overall, even though this beer has some good qualities, I didnt have much reaction to it')
    text.append('Tap at the taproom. Somewhat hazy reddish orange pour with a spotty white head. Citrusy aroma with a sweet malt and citrus taste. Crisp on the tongue. Good stuff')

    # Tokenize words
    for i,tex in enumerate(text):
        text[i] = tex.split(' ')

    # Run function
    textDict, index = TFIDF_LSI_SIM(text, 5)

    # Generate similarity numbers
    for similarities in index:
        print similarities