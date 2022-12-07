import urllib.request as ulib
import json

class JokeBE(object):

    def __init__(self):
        #Creating dictionaries for required language and joke types in url
        self.language_dict = {0: 'lang=de', 1: '', 2: 'lang=fr'}
        self.type_dict = {0: 'type=single', 1: '', 2: 'type=twopart'}
        self.jokeText = ""

        #Standard-url if language is english and no certain joke type is required

        self.url = 'https://v2.jokeapi.dev/joke/Any'

        self.joke_language = 1
        self.joke_type = 1

        self.url_txt = ulib.urlopen(self.url).read()

        #loading the dictionary from url

        self.joke_dict = json.loads(self.url_txt)

    #This method uses the urllib module and json to first open the set url
    #and then load a dictionary from the webpage witch which the single joke elements
    #can be accessed.
    def setJokeText(self):
        self.url_txt = ulib.urlopen(self.url).read()
        self.joke_dict = json.loads(self.url_txt)
        
        #Since the first implementation there was a change on the website so that some joke types in 
        #french do not always constitute a valid request and throw a KeyError, which is excepted below.
        try:
            if self.joke_dict["type"] == "twopart":
                self.jokeText = self.joke_dict["setup"] + "\n\n" + self.joke_dict["delivery"]
            else:
                self.jokeText = self.joke_dict["joke"]
        
        except (KeyError):
            print("Diese Kombination wurde neuerdings auf der Website deaktiviert. Programm ist 1A ok!\ndie vorherigen Einstellungen werden beibehalten.")

    def setURl(self):

        #If only one setting deviates from the standard, the url needs to have an extra option added with the '?'
        #this is achieved by assigning the standard settings to one, so they can be interpreted as a boolean "True".
        #Not the cleanest way in terms of programming etiquette, but the most direct I could think of.
        if self.joke_language ^ self.joke_type:
            self.url = 'https://v2.jokeapi.dev/joke/Any' + '?' + self.language_dict[self.joke_language] + self.type_dict[self.joke_type]

        #If neither option is set to standard both extra options need to be added to the url.

        elif self.joke_language != 1 and self.joke_type != 1:
            self.url = 'https://v2.jokeapi.dev/joke/Any' + '?' + self.language_dict[self.joke_language] + '&' + self.type_dict[self.joke_type]

        #else the standard url can be used.

        else:
            self.url ='https://v2.jokeapi.dev/joke/Any'

