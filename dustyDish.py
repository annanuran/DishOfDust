
#instead of generating houses, we generate gourmet cuisine
from threading import Thread
from num2words import num2words
from random import choice, choices
from datetime import datetime
import twitter

def log(message):
    with open("log.txt", "w") as f:
        f.write(message + "\n")
        f.write("   " + str(datetime.now()) + "\n")
        f.write("--------------------------------")

with open("tokens.txt", "r") as f:
    lines = f.readlines()
    SECRET = lines[0].strip()
    API_KEY= lines[1].strip()
    BEARER = lines[2].strip()
    ACCESS = lines[3].strip()
    ACCESS_SECRET = lines[4].strip()
    
def pluralize(food:str, plur:bool):
    return food + "s" if plur else "an " + food if food[0] in ['a', 'e', 'i', 'o', 'u'] else "a " + food

def tweeter(tweet:str):
    api = twitter.Api(consumer_key=API_KEY,
                      consumer_secret=SECRET,
                      access_token_secret=ACCESS_SECRET,
                      access_token_key=ACCESS)
    try:
        api.PostUpdate(tweet)
    except UnicodeDecodeError:
        log("Unicode error: " + tweet)
    except twitter.error.TwitterError:
        log("Twitter error.")
        
                      
    
food = ['rotisserie chicken', 'pringle', 'velveeta block', 'pot pie', 'mincemeat', \
    'green bean', 'onion', 'tater tot', 'sausage', 'creme brulee', 'meatball', 'fried rice', \
        'calzone', 'escargot', 'hamburger helper', 'chicken nugget', 'chicken salad', \
            'chicken wing', 'corn cob', 'tortilla chip', 'sushi roll', 'broccoli', 'cauliflower', \
                'cabbage', 'chicken', 'beef', 'pork', 'lamb', 'turkey', 'duck', 'goose', 'quail', \
                    'rat', 'goat shank', 'pork chop', 'pork shoulder', 'pork rib', 'pork loin', \
                        'milk', 'cheese', 'egg', 'celery stick', 'carrot', 'cucumber', 'lettuce', \
                            'pizza', 'linguine noodle', 'macaroni', 'lasagna', 'macaron', \
                                'herb', 'lettuce', 'cherry', 'apple', 'pear', 'peach', 'banana', 
                                    'orange', 'grape', 'strawberry', 'blueberry', 'raspberry', \
                                        'watermelon', 'crab', 'pepsi max']
 
ethnicity = [' French', ' German', 'n American', ' Japanese', ' Ukrainian', 'n English', ' Czech', ' Chinese', \
    ' Lebanese',' Yugoslavian', ' Mongolian', ' Somali', 'n Egyptian'] # et cetera

application = ['covered', 'sauteed', 'stir fried', 'broiled', 'blanched', 'poached', 'steamed', \
    'baked', 'roasted', 'air fried', 'braised', 'seared', 'blackened', 'pan fried', 'grilled', \
        'fried', 'deep fried',  'flambeed', 'ignited', 'smoked', 'simmered', 'sizzled', \
            'toasted', 'burned', 'slow-cooked', 'in a crock pot', 'in a pot', 'in a sauce pan', \
                'boiled']
application_method = ['with', 'in', 'overtop of', 'inside of', 'underneath', 'in a separate container than', 'widdershins of']

restaurant = [' street stall', ' bus stop', ' Michelin Star restaurant', ' food truck', \
' home', ' place which is neither here nor there', ' diner', ' buffet', 'n airplane', ' boat', \
' hospital', ' bed', ' bar', ' prison', ' mariott hotel', ' concert venue', ' community potluck'] #Some suggestions by tabnine AI autocomplete

time = range(1, 42)
                        #1.2096 second              ~90 seconds 14.4 minutes
duration = ['seconds', 'microfortnights', 'minutes', 'moments', 'kermits', 'hours', 'days', 'weeks', 'months', 'years'] # lol
#https://en.wikipedia.org/wiki/List_of_unusual_units_of_measurement#Microfortnight
#https://en.wikipedia.org/wiki/List_of_unusual_units_of_measurement#KerMetric_time

time_weights = (40, 20, 70, 60, 60, 30, 6, 5, 2, 1)

descriptor = ['Overdone', 'Crispy', 'Diseased', 'Fried', 'Frozen', 'Gourmet', 'Hot', 'Hot and Spicy',\
    'Raw', 'Delicious', 'Gross', 'Delectable', 'Magically Delicious', 'Delightful', 'Revolting', \
        'Mouth-watering', 'Venomous', 'Fitting', 'Fantastic', 'Fantabulous', 'Meh', \
            'Frankly, walking', 'Like a prize from a Cracker Jack box', 'Oily', 'Dry', 'Salty', 'Sweet']

punctuation = ['.', '!', '?', '~', '... NOT.', ', ~UwU~']

def main():
    
    plural = [True, False]
    food1 = pluralize(choice(food), choice(plural))        
    food2 = pluralize(choice(food), choice(plural))
    txt = "\n"
    txt = txt + 'A' + str(choice(ethnicity)) + ' dish: \n'
    txt = txt + '      ' + str(food1.capitalize()) + ' ' + str(choice(application)) + ' ' + str(choice(application_method)) + '\n'
    txt = txt + '            ' + str(food2) + ' for ' + str(num2words(choice(time))) + ' ' + str(choices(duration, weights=time_weights, k=1)[0]) + ".\n"
    txt = txt + '                  Served in a' + str(choice(restaurant)) + '.\n'
    txt = txt + '                        ' + str(choice(descriptor)) + str(choice(punctuation))
    tweeter(txt)
    exit(0)
    #print("\nPossible combinations: " + num2words(G.num_combs))
    #could set this to a bio? or something

    
t = Thread(target=main)    
t.start()   
#num_combs = ((len(food) * 2) * len(food) * 2 * len(application) * len(application_method) * len(restaurant) * len(punctuation) * len(ethnicity) * len(descriptor))
#G.set_combs(num_combs)
