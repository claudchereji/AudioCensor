import os
import sys



#usrinput = input("type input here: ")
userTxtFile = open('example.txt', 'r')

#crete an if statement that asks the user if they want to import a file or paste/type in the text. 
#add a line that says that multiple lines of text aren't supported, and they should save the large 
#text as a file then import it. 

swearwords = ['arse', 'arsehead', 'arsehole', 'ass', 'asshole', 'bastard', 'bitch', 'bloody', 'bollocks', 'brotherfucker', 'bugger', 'bullshit', 'child-fucker', 'Christ on a bike', 'Christ on a cracker', 'cock', 'cocksucker', 'crap', 'cunt', 'damn', 'damn it', 'dick', 'dickhead', 'dyke', 'fatherfucker', 'frigger', 'fuck', 'fucker', 'goddamn', 'godsdamn', 'hell', 'holy shit', "holy hell", 'horseshit', 'shit', 'Jesus Christ', 'Jesus fuck', 'Jesus H. Christ', 'Jesus Harold  Christ', 'Jesus Mary and Joseph', 'kike', 'motherfucker', 'nigga', 'nigra', 'piss', 'prick', 'pussy', 'shit', 'shit', 'ass', 'shite', 'sisterfucker', 'slut', 'son of a bitch', 'son of a whore', 'sweet Jesus', 'twat', 'wanker', "shit", "bullshit", "fuck", "asshole", "bullshit", "whore", "Fuck You", "Shit", "Piss off", "Dick head", "Asshole", "Son of a bitch", "Bastard", "Bitch", "Damn", "Dumb",	"Bimbo", "Piss",	"Jerk",	"Stupid",	"Wimp",	"Lame", "Idiot",	"Fool",	"Retard",	"Loser",	"Pain in the Neck", "Rubbish",	"Shag",	"Wanker", "Taking a Piss", "Twat", "Bollocks",	"Bugger",	"Choad",	"Crikey",	"Bloody Hell", "Bloody Oaf", "Root", "Get Stuffed", "Bugger Me", "Crazy", "Creepy", "Clown", "Weird"]
adjectives = ["Fuck You", "Shit", "Piss off", "Dick head", "Asshole", "Son of a bitch", "Bastard", "Bitch", "Damn", "Dumb",	"Bimbo", "Piss",	"Jerk",	"Stupid",	"Wimp",	"Lame", "Idiot",	"Fool",	"Retard",	"Loser",	"Pain in the Neck", "Rubbish",	"Shag",	"Wanker", "Taking a Piss", "Twat", "Bollocks",	"Bugger",	"Choad",	"Crikey",	"Bloody Hell", "Bloody Oaf", "Root", "Get Stuffed", "Bugger Me", "Crazy", "Creepy", "Clown", "Weird", 'adorable', 'adventurous', 'aggressive', 'agreeable', 'alert', 'alive', 'amused', 'angry', 'annoyed', 'annoying', 'anxious', 'arrogant', 'ashamed', 'attractive', 'average', 'awful', 'bad', 'beautiful', 'better', 'bewildered', 'black', 'bloody', 'blue', 'blue-eyed', 'blushing', 'bored', 'brainy', 'brave', 'breakable', 'bright', 'busy', 'calm', 'careful', 'cautious', 'charming', 'cheerful', 'clean', 'clear', 'clever', 'cloudy', 'clumsy', 'colorful', 'combative', 'comfortable', 'concerned', 'condemned', 'confused', 'cooperative', 'courageous', 'crazy', 'creepy', 'crowded', 'cruel', 'curious', 'cute', 'dangerous', 'dark', 'dead', 'defeated', 'defiant', 'delightful', 'depressed', 'determined', 'different', 'difficult', 'disgusted', 'distinct', 'disturbed', 'dizzy', 'doubtful', 'drab', 'dull', 'eager', 'easy', 'elated', 'elegant', 'embarrassed', 'enchanting', 'encouraging', 'energetic', 'enthusiastic', 'envious', 'evil', 'excited', 'expensive', 'exuberant', 'fair', 'faithful', 'famous', 'fancy', 'fantastic', 'fierce', 'filthy', 'fine', 'foolish', 'fragile', 'frail', 'frantic', 'friendly', 'frightened', 'funny', 'gentle', 'gifted', 'glamorous', 'gleaming', 'glorious', 'good', 'gorgeous', 'graceful', 'grieving', 'grotesque', 'grumpy', 'handsome', 'happy', 'healthy', 'helpful', 'helpless', 'hilarious', 'homeless', 'homely', 'horrible', 'hungry', 'hurt', 'ill', 'important', 'impossible', 'inexpensive', 'innocent', 'inquisitive', 'itchy', 'jealous', 'jittery', 'jolly', 'joyous', 'kind', 'lazy', 'light', 'lively', 'lonely', 'long', 'lovely', 'lucky', 'magnificent', 'misty', 'modern', 'motionless', 'muddy', 'mushy', 'mysterious', 'nasty', 'naughty', 'nervous', 'nice', 'nutty', 'obedient', 'obnoxious', 'odd', 'old-fashioned', 'open', 'outrageous', 'outstanding', 'panicky', 'perfect', 'plain', 'pleasant', 'poised', 'poor', 'powerful', 'precious', 'prickly', 'proud', 'putrid', 'puzzled', 'quaint', 'real', 'relieved', 'repulsive', 'rich', 'scary', 'selfish', 'shiny', 'shy', 'silly', 'sleepy', 'smiling', 'smoggy', 'sore', 'sparkling', 'splendid', 'spotless', 'stormy', 'strange', 'stupid', 'successful', 'super', 'talented', 'tame', 'tasty', 'tender', 'tense', 'terrible', 'thankful', 'thoughtful', 'thoughtless', 'tired', 'tough', 'troubled', 'ugliest', 'ugly', 'uninterested', 'unsightly', 'unusual', 'upset', 'uptight', 'vast', 'victorious', 'vivacious', 'wandering', 'weary', 'wicked', 'wide-eyed', 'wild', 'witty', 'worried', 'worrisome', 'wrong', 'zany', 'zealous', "shit", "bullshit", "fuck", "asshole", "bullshit", "whore", "whores", 'huge', 'large', 'foot', 'reticulated', 'great', 'indian', 'giant', 'sacred', 'african', 'big', 'burmese', 'enormous', 'royal', 'small', 'female', 'green', 'long', 'black', 'dead', 'live', 'regal', 'gigantic', 'reticulate', 'hungry', 'british', 'headed', 'mighty', 'monstrous', 'coiled', 'pure', 'standard', 'immense', 'terrible', 'golden', 'largest', 'angry', 'australian', 'asian', 'male', 'gorged', 'olive', 'brown', 'mightiest', 'sluggish', 'frosty', 'harmless', 'mythical', 'biggest', 'tame', 'massive', 'thick', 'motionless', 'grown', 'albino', 'asiatic', 'delphic', 'irish', 'deadly', 'legendary', 'numerical', 'wary', 'spotted', 'apollo', 'tailed', 'stuffed', 'empty', 'postprandial', 'poisonous', 'prostrate', 'longest', 'pound', 'sleek', 'overfed', 'invisible', 'fed', 'tremendous', 'unsated']


def tConv ():
    timeCodeM = (int(input("Enter the time code minute marker: ")))
    timeCodeS = (int(input("Enter the time code second marker: ")))
    condensedTime = (timeCodeM * 60) + (timeCodeS)
    timeSeconds = condensedTime
    timeMiliseconds = (condensedTime * 1000)
    
    print(timeSeconds)
    print(timeMiliseconds)


#once you create the function to import files uncomment the next 2 lines

lines = userTxtFile.readlines()
usrinput = '\t'.join([line.strip() for line in lines])
x = (usrinput.split())


#timeCodeM = (int(input("Enter the time code minute marker: ")))
#timeCodeS = (int(input("Enter the time code second marker: ")))
#condensedTime = (timeCodeM * 60) + (timeCodeS)
#timeSeconds = condensedTime
#timeMiliseconds = (condensedTime * 1000)

#print(timeSeconds)
#print(timeMiliseconds)

y = [ind for ind, val in enumerate(x) if val in swearwords]
print("you typed in a cuss word at index number: ", y)


time_code_q = input("Do you have a time code? y/n \n")

if time_code_q.lower() == 'y':
    tConv()
elif time_code_q.lower() == 'n':
    print('user typed no')
else:
    print('Type yes or no')


#code_to_run = ("ffmpeg -i (recording function goes here).mp3 -af "volume=enable='between(t, timeMiliseconds)':volume=0" (RECORDING FUNCTION GOES HERE AND GETS THE NEXT WORD APPENDED)Muted.mp3 && ffmpeg -i (APPENDED RECORDING FUNCTION GOES HERE).mp3 -i (CENSORED AUDIO FILE FUNCTION GOES HERE).m4a -filter_complex (CUSS WORD OCCURANCES GO IN THIS NEXT FUNCTION WITH SECONDS FUNCTION)"[0]adelay=timeSeconds|timeSeconds[s0];[1]adelay=[timeMiliseconds]|[timeMiliseconds][s1]; [s0][s1]amix=2" -preset ultrafast -async 1 output.mp3")

#print(code_to_run)
#loop this whole commented function for the number of occurances of swear words
