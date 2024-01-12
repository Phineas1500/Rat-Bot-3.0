import keep_alive
import json
import time
from twitter.account import Account
from twitter.search import Search
import random
import time
from datetime import datetime
import os

ct0 = os.environ['ct0']
auth_token = os.environ['auth_token']
keep_alive.keep_alive()

def load_ids(filename):
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_ids(filename, ids):
    with open(filename, 'w') as f:
        json.dump(ids, f)

#account = []
#search = []

# Rat Bot
account = Account(cookies={"ct0": ct0, "auth_token": auth_token})


search = Search(cookies={"ct0": ct0, "auth_token": auth_token})


old_ids = load_ids('tweet_ids4.txt')

toReply = [
    '(from:AltPhinny)', '(from:BadBoyHalo)', '(from:tommyinnit)',
    '(from:Ranboosaysstuff)', '(from:TubboLive)', '(from:JackManifoldTV)',
    '(from:quackity4k)', '(from:KarlJacobs_)',
    '(from:honkkarl)', '(from:GeorgeNotFound)', '(from:Valkyrae)',
    '(from:sapnap)', '(from:SaintsofGames)', '(from:GeorgeNootFound)',
    '(from:CptPuffy)', '(from:TubboTWO)', '(from:MrBeast)',
    '(from:Nihachu)', '(from:TinaKitten)', '(from:Antfrost)',
    '(from:FoolishGamers)', '(from:dantdm)',
    '(from:Corpse_Husband)', '(from:ranaltboo)', '(from:greg16676935420)',
    '(from:pokimanelol)', '(from:AustinOnTwitter)', '(from:LuciferDecides)', '(from:QuackityStudios)'
]
while True:
    for handle in toReply:
        res = search.run(
            limit=1,
            retries=1,
            queries=[
                {
                    'category': 'Latest',
                    'query': handle
                },
            ],
        )
        print(handle)
        first_tweet_rest_id = res[0][0]['content']['itemContent']['tweet_results']['result']['rest_id']
        handle_no_paren = handle[6:-1]  # Remove the '(from:' and ')' from the handle

        if old_ids.get(handle_no_paren) == first_tweet_rest_id:
            time.sleep(55)
            continue  # Skip this tweet

        first_tweet_full_text = res[0][0]['content']['itemContent']['tweet_results']['result']['legacy']['full_text']
        print(first_tweet_rest_id)
        print(first_tweet_full_text)

        tweetWords = first_tweet_full_text.lower()
        filterDetect = False
        filter = [
            "groom", "disgust", "piece of", "pathetic", "allegation",
            "don't understand", "manipulat", "ptsd", "this is fake",
            "this isn't true", "victim", "support", "pedo", "harass", "minor",
            "died", "passed away", "devastat", "heart broken", "for your loss",
            "much love", "take as long", "take all the time", "love ya",
            "sorry", "take care", "heartbreaking", "heart goes out",
            "hearts go out", "in fear", "war zone", "daily life",
            "anyone affected", "rest in peace", "rip", "chemo", "cancer",
            "racist", "❤️"
        ]
        for i in filter:
            if i in tweetWords:
                filterDetect = True
        if (filterDetect == False):
            x = random.randint(1, 518)
            if (x == 1):
                mediaLink = " https://twitter.com/AltPhinny/status/1382125508620660736/photo/1"
                tweetStatus = "Why are you looking at me?"
            elif (x == 2):
                mediaLink = " https://twitter.com/AltPhinny/status/1382125550295261186/photo/1"
                tweetStatus = "I'm uPfront"
            elif (x == 3):
                mediaLink = " https://twitter.com/AltPhinny/status/1382125596231225344/photo/1"
                tweetStatus = "WhERE ARE THE TURTLES!"
            elif (x == 4):
                mediaLink = " https://twitter.com/AltPhinny/status/1382125652510400515/photo/1"
                tweetStatus = "I'm listenIng"
            elif (x == 5):
                mediaLink = " https://twitter.com/AltPhinny/status/1382125710450552844/photo/1"
                tweetStatus = "Look there!!"
            elif (x == 6):
                mediaLink = " https://twitter.com/AltPhinny/status/1382125808974647297/photo/1"
                tweetStatus = "Hey there!"
            elif (x == 7):
                mediaLink = " https://twitter.com/AltPhinny/status/1382125900779638786/photo/1"
                tweetStatus = "What's the matter, " + handle_no_paren + "?"
            elif (x == 8):
                mediaLink = " https://twitter.com/AltPhinny/status/1382125950540918789/photo/1"
                tweetStatus = "Just chilliNg in Cedar Rapids"
            elif (x == 9):
                mediaLink = " https://twitter.com/AltPhinny/status/1402599234713554950/photo/1"
                tweetStatus = "I can't seEm to turn off the computer..."
            elif (x == 10):
                mediaLink = " https://twitter.com/AltPhinny/status/1382126054983229441/photo/1"
                tweetStatus = "GIMME"
            elif (x == 11):
                mediaLink = " https://twitter.com/AltPhinny/status/1382126080463634436/photo/1"
                tweetStatus = "Any left?"
            elif (x == 12):
                mediaLink = " https://twitter.com/AltPhinny/status/1382126119357415424/photo/1"
                tweetStatus = "I'm a professionAl"
            elif (x == 13):
                mediaLink = " https://twitter.com/AltPhinny/status/1382126161724071937/photo/1"
                tweetStatus = "Very comfy, I must say"
            elif (x == 14):
                mediaLink = " https://twitter.com/AltPhinny/status/1382126206691246082/photo/1"
                tweetStatus = "Let's have a staring conteSt"
            elif (x == 15):
                mediaLink = " https://twitter.com/AltPhinny/status/1382126252711108611/photo/1"
                tweetStatus = "Had a good nap"
            elif (x == 16):
                mediaLink = " https://twitter.com/AltPhinny/status/1382126297145556996/photo/1"
                tweetStatus = "What's your obsession wiTh cups?!"
            elif (x == 17):
                mediaLink = " https://twitter.com/AltPhinny/status/1382126331949907970/photo/1"
                tweetStatus = "It's hot in hEre!"
            elif (x == 18):
                mediaLink = " https://twitter.com/AltPhinny/status/1382126380834492416/photo/1"
                tweetStatus = "Why's there a paCifier in my mouth?! I'm a dog, not a baby!"
            elif (x == 19):
                mediaLink = " https://twitter.com/AltPhinny/status/1382126442713133062/photo/1"
                tweetStatus = "I love stuffed animals"
            elif (x == 20):
                mediaLink = " https://twitter.com/AltPhinny/status/1382126493871046666/photo/1"
                tweetStatus = "Whoa tHere!"
            elif (x == 21):
                mediaLink = " https://twitter.com/AltPhinny/status/1382126556357791748/photo/1"
                tweetStatus = "How do I turn this thing on!"
            elif (x == 22):
                mediaLink = " https://twitter.com/AltPhinny/status/1382126591912898566/photo/1"
                tweetStatus = "Huh?"
            elif (x == 23):
                mediaLink = " https://twitter.com/AltPhinny/status/1382126645021184004/photo/1"
                tweetStatus = "Still waiting in the Starbucks line..."
            elif (x == 24):
                mediaLink = " https://twitter.com/AltPhinny/status/1382126691221397505/photo/1"
                tweetStatus = "Ign.ore Bad, he's being annoying"
            elif (x == 25):
                mediaLink = " https://twitter.com/AltPhinny/status/1382126763128537095/photo/1"
                tweetStatus = "Sleeping is my one passion"
            elif (x == 26):
                mediaLink = " https://twitter.com/AltPhinny/status/1382126811698634754/photo/1"
                tweetStatus = "I'M STUCK IN THE DISHWASHER!! WHAT WAS BAD THINKING!?"
            elif (x == 27):
                mediaLink = " https://twitter.com/AltPhinny/status/1382126853046030336/photo/1"
                tweetStatus = "Oooo, I hear some tea!"
            elif (x == 28):
                mediaLink = " https://twitter.com/AltPhinny/status/1382126931265617922/photo/1"
                tweetStatus = "That is a lot to take in"
            elif (x == 29):
                mediaLink = " https://twitter.com/AltPhinny/status/1382127110215569420/photo/1"
                tweetStatus = "Am I awake or asleep?"
            elif (x == 30):
                mediaLink = " https://twitter.com/AltPhinny/status/1382127169502085128/photo/1"
                tweetStatus = "You moved your head, ha!"
            elif (x == 31):
                mediaLink = " https://twitter.com/AltPhinny/status/1382127230810226689/photo/1"
                tweetStatus = "I just wanna stay home! ;("
            elif (x == 32):
                mediaLink = " https://twitter.com/AltPhinny/status/1382127271717310467/photo/1"
                tweetStatus = "Ah, I'm finally safe"
            elif (x == 33):
                mediaLink = " https://twitter.com/AltPhinny/status/1382127351396438020/photo/1"
                tweetStatus = "Time for bed!"
            elif (x == 34):
                mediaLink = " https://twitter.com/AltPhinny/status/1382127388113387520/photo/1"
                tweetStatus = "Treats are my expertise!"
            elif (x == 35):
                mediaLink = " https://twitter.com/AltPhinny/status/1382127454500831236/photo/1"
                tweetStatus = "What's going through my brain?"
            elif (x == 36):
                mediaLink = " https://twitter.com/AltPhinny/status/1382127525518843904/photo/1"
                tweetStatus = "Time to snack!"
            elif (x == 37):
                mediaLink = " https://twitter.com/AltPhinny/status/1382127651343728642/photo/1"
                tweetStatus = "Do I see cheesy fries?!"
            elif (x == 38):
                mediaLink = " https://twitter.com/AltPhinny/status/1382127789252472836/photo/1"
                tweetStatus = "I DESERVE THE TREATS!"
            elif (x == 39):
                mediaLink = " https://twitter.com/AltPhinny/status/1382127858286538757/photo/1"
                tweetStatus = "I had a long day at work..."
            elif (x == 40):
                mediaLink = " https://twitter.com/AltPhinny/status/1382127907749904388/photo/1"
                tweetStatus = "Buy Bad's merCh so I can get more treats!"
            elif (x == 41):
                mediaLink = " https://twitter.com/AltPhinny/status/1382127967040630789/photo/1"
                tweetStatus = "I didn't see that!"
            elif (x == 42):
                mediaLink = " https://twitter.com/AltPhinny/status/1382128538711699457/photo/1"
                tweetStatus = "This mOvie's horrible, but I can't look away"
            elif (x == 43):
                mediaLink = " https://twitter.com/AltPhinny/status/1382128619431006209/photo/1"
                tweetStatus = "Why are you filMing me?!"
            elif (x == 44):
                mediaLink = " https://twitter.com/AltPhinny/status/1382128672287625222/photo/1"
                tweetStatus = "Did I hear the do/orbell?!"
            elif (x == 45):
                mediaLink = " https://twitter.com/AltPhinny/status/1382128727685992450/photo/1"
                tweetStatus = "Let me just lay down, " + handle_no_paren
            elif (x == 46):
                mediaLink = " https://twitter.com/AltPhinny/status/1382128838994432004/photo/1"
                tweetStatus = "I'm a tea connoisseur"
            elif (x == 47):
                mediaLink = " https://twitter.com/AltPhinny/status/1382129038253260806/photo/1"
                tweetStatus = "Seriously, what was Bad thinking when he posted this..."
            elif (x == 48):
                mediaLink = " https://twitter.com/AltPhinny/status/1382129232512434177/photo/1"
                tweetStatus = "I get my daily Vitamin C!"
            elif (x == 49):
                mediaLink = " https://twitter.com/AltPhinny/status/1382129333263863808/photo/1"
                tweetStatus = "This doesn't look right..."
            elif (x == 50):
                mediaLink = " https://twitter.com/AltPhinny/status/1382129377941540864/photo/1"
                tweetStatus = "Welcome to my house!"
            elif (x == 51):
                mediaLink = " https://twitter.com/AltPhinny/status/1382129492618002435/photo/1"
                tweetStatus = "I hope you brought something to the potluck"
            elif (x == 52):
                mediaLink = " https://twitter.com/AltPhinny/status/1382129584980828163/photo/1"
                tweetStatus = "I love my new mittens and earmuffs!"
            elif (x == 53):
                mediaLink = " https://twitter.com/AltPhinny/status/1382129794159108099/photo/1"
                tweetStatus = "Who enjoys eating their fur?! Bad loves playing cruel tricks >:("
            elif (x == 54):
                mediaLink = " https://twitter.com/AltPhinny/status/1382129919153610753/photo/1"
                tweetStatus = "Let me out!!"
            elif (x == 55):
                mediaLink = " https://twitter.com/AltPhinny/status/1382326298551447554/photo/1"
                tweetStatus = "Time for bed"
            elif (x == 56):
                mediaLink = " https://twitter.com/AltPhinny/status/1382326333687148546/photo/1"
                tweetStatus = "What's up?"
            elif (x == 57):
                mediaLink = " https://twitter.com/AltPhinny/status/1382326374090817538/photo/1"
                tweetStatus = "Ratception"
            elif (x == 58):
                mediaLink = " https://twitter.com/AltPhinny/status/1382326459415605249/photo/1"
                tweetStatus = "I'm a bag of fur!"
            elif (x == 59):
                mediaLink = " https://twitter.com/AltPhinny/status/1382326518416879616/photo/1"
                tweetStatus = "Atten-HUT!"
            elif (x == 60):
                mediaLink = " https://twitter.com/AltPhinny/status/1382326553690968067/photo/1"
                tweetStatus = "Let me tell you something...I like turtles."
            elif (x == 61):
                mediaLink = " https://twitter.com/AltPhinny/status/1382326637073678337/photo/1"
                tweetStatus = "I'm a Ratstronaut!"
            elif (x == 62):
                mediaLink = " https://twitter.com/AltPhinny/status/1382326741335695360/photo/1"
                tweetStatus = "Why's the camera in my face?"
            elif (x == 63):
                mediaLink = " https://twitter.com/AltPhinny/status/1382326809631592456/photo/1"
                tweetStatus = "I wish they made these in dog sizes"
            elif (x == 64):
                mediaLink = " https://twitter.com/AltPhinny/status/1382326914791145474/photo/1"
                tweetStatus = "Not too happy about that"
            elif (x == 65):
                mediaLink = " https://twitter.com/AltPhinny/status/1382326974950031364/photo/1"
                tweetStatus = "When will you go to bed?"
            elif (x == 66):
                mediaLink = " https://twitter.com/AltPhinny/status/1382327064267788289/photo/1"
                tweetStatus = "New blankies are so comfy"
            elif (x == 67):
                mediaLink = " https://twitter.com/AltPhinny/status/1382327429369303040/photo/1"
                tweetStatus = "Could you get the remote? I'm too wrapped up in the blanket."
            elif (x == 68):
                mediaLink = " https://twitter.com/AltPhinny/status/1382327498881531905/photo/1"
                tweetStatus = "Let's continue the walk, " + handle_no_paren + "!"
            elif (x == 69):
                mediaLink = " https://twitter.com/AltPhinny/status/1382327529424498692/photo/1"
                tweetStatus = "ARE SKEPPY AND BAD MEETING UP?!"
            elif (x == 70):
                mediaLink = " https://twitter.com/AltPhinny/status/1382327647133388800/photo/1"
                tweetStatus = "GIMME DAT FOOD!"
            elif (x == 71):
                mediaLink = " https://twitter.com/AltPhinny/status/1382327720118484997/photo/1"
                tweetStatus = "It's too dark!"
            elif (x == 72):
                mediaLink = " https://twitter.com/AltPhinny/status/1382327885491539969/photo/1"
                tweetStatus = "I HATE BATHS!"
            elif (x == 73):
                mediaLink = " https://twitter.com/AltPhinny/status/1382327938729840649/photo/1"
                tweetStatus = "Time to dry off"
            elif (x == 74):
                mediaLink = " https://twitter.com/AltPhinny/status/1382328008388837378/photo/1"
                tweetStatus = "I smell treats"
            elif (x == 75):
                mediaLink = " https://twitter.com/AltPhinny/status/1382328120699719688/photo/1"
                tweetStatus = "I wish dogs could eat chocolate (don't give your dog chocolate, it's toXic)"
            elif (x == 76):
                mediaLink = " https://twitter.com/AltPhinny/status/1382328169089355778/photo/1"
                tweetStatus = "Are there games on your phone?"
            elif (x == 77):
                mediaLink = " https://twitter.com/AltPhinny/status/1382328230343016450/photo/1"
                tweetStatus = "POg"
            elif (x == 78):
                mediaLink = " https://twitter.com/AltPhinny/status/1382329152787873797/photo/1"
                tweetStatus = "Just passed my driving test! Now I'm getting grOceries from Wal-Mart."
            elif (x == 79):
                mediaLink = " https://twitter.com/AltPhinny/status/1382329197981491202/photo/1"
                tweetStatus = "TREATS"
            elif (x == 80):
                mediaLink = " https://twitter.com/AltPhinny/status/1382329293619990534/photo/1"
                tweetStatus = "I will do anything for a snack"
            elif (x == 81):
                mediaLink = " https://twitter.com/AltPhinny/status/1382329378810515456/photo/1"
                tweetStatus = "Num num num num!"
            elif (x == 82):
                mediaLink = " https://twitter.com/AltPhinny/status/1382725047547260931/photo/1"
                tweetStatus = "Plop!"
            elif (x == 83):
                mediaLink = " https://twitter.com/AltPhinny/status/1382725164341809153/photo/1"
                tweetStatus = "I hate cages..."
            elif (x == 84):
                mediaLink = " https://twitter.com/AltPhinny/status/1382725471847264258/photo/1"
                tweetStatus = "Time to party!"
            elif (x == 85):
                mediaLink = " https://twitter.com/AltPhinny/status/1382725522174656514/photo/1"
                tweetStatus = "Tell me what you think is on my mind"
            elif (x == 86):
                mediaLink = " https://twitter.com/AltPhinny/status/1382725582132236288/photo/1"
                tweetStatus = "I have very big eyes"
            elif (x == 87):
                mediaLink = " https://twitter.com/AltPhinny/status/1382725812772814849/photo/1"
                tweetStatus = "I enjoy taking strolls in the park"
            elif (x == 88):
                mediaLink = " https://twitter.com/AltPhinny/status/1382726373664522240/photo/1"
                tweetStatus = "I've heard I'm a snorer"
            elif (x == 89):
                mediaLink = " https://twitter.com/AltPhinny/status/1382726429729824768/photo/1"
                tweetStatus = "I get treats when I stick my tongue out"
            elif (x == 90):
                mediaLink = " https://twitter.com/AltPhinny/status/1382726479159648260/photo/1"
                tweetStatus = "I didn't get any treats today ;("
            elif (x == 91):
                mediaLink = " https://twitter.com/AltPhinny/status/1382728594842136577/photo/1"
                tweetStatus = "Why is there a camera in my face?! I'm trying to sleep!"
            elif (x == 92):
                mediaLink = " https://twitter.com/AltPhinny/status/1382728667269373955/photo/1"
                tweetStatus = "Subscribe to BadBoyHalo so I can get toys other than paper plates"
            elif (x == 93):
                mediaLink = " https://twitter.com/AltPhinny/status/1382728738232795138/photo/1"
                tweetStatus = "GIMME!!"
            elif (x == 94):
                mediaLink = " https://twitter.com/AltPhinny/status/1382728797028499459/photo/1"
                tweetStatus = "uhhhhh, I'm not part of this"
            elif (x == 95):
                alsoNow = datetime.now()
                currentTime = alsoNow.strftime("%H:%M")
                mediaLink = " https://twitter.com/AltPhinny/status/1382728843648196612/photo/1"
                tweetStatus = "Why are you livestreaming at " + currentTime + " again (GMT/BST)?"
            elif (x == 96):
                mediaLink = " https://twitter.com/AltPhinny/status/1382728911558123521/photo/1"
                tweetStatus = "Chocolate, my forbidden pleasure..."
            elif (x == 97):
                mediaLink = " https://twitter.com/AltPhinny/status/1382736854684930048/photo/1"
                tweetStatus = "Kids these days..."
            elif (x == 98):
                mediaLink = " https://twitter.com/AltPhinny/status/1388327483427131395/photo/1"
                tweetStatus = "I have a PhD in looking cute"
            elif (x == 99):
                mediaLink = " https://twitter.com/AltPhinny/status/1382743183080194049/photo/1"
                tweetStatus = "I don't really understand Minecraft, to be honest"
            elif (x == 100):
                mediaLink = " https://twitter.com/AltPhinny/status/1382744016907812870/photo/1"
                tweetStatus = "Why does Bad keep teasing me?"
            elif (x == 101):
                mediaLink = " https://twitter.com/AltPhinny/status/1382744058913820674/photo/1"
                tweetStatus = "zzzzzz..."
            elif (x == 102):
                mediaLink = " https://twitter.com/AltPhinny/status/1382744111606865922/photo/1"
                tweetStatus = "I'm taller than TommyInnit, Dream, and Wilbur combined (after all your constant nagging, I have decided to add Ranboo to this statement as well. Thanks for nothing, you annoying humans)"
            elif (x == 103):
                mediaLink = " https://twitter.com/AltPhinny/status/1382766850518433793/photo/1"
                tweetStatus = "I'm an expert at looking cute"
            elif (x == 104):
                mediaLink = " https://twitter.com/AltPhinny/status/1382767133659136004/photo/1"
                tweetStatus = "Why am I so blurry?"
            elif (x == 105):
                mediaLink = " https://twitter.com/AltPhinny/status/1382767201946591234/photo/1"
                tweetStatus = "I'm intrigued"
            elif (x == 106):
                mediaLink = " https://twitter.com/AltPhinny/status/1382767285329408001/photo/1"
                tweetStatus = "My tongue looks like a snake"
            elif (x == 107):
                mediaLink = " https://twitter.com/AltPhinny/status/1382767371157397505/photo/1"
                tweetStatus = "You know, you're not a disappointment"
            elif (x == 108):
                mediaLink = " https://twitter.com/AltPhinny/status/1382823611682193413/photo/1"
                tweetStatus = "I NOW HATE WATER BOTTLES IN ADDITION TO THE NEIGHBOR'S CAT!"
            elif (x == 109):
                mediaLink = " https://twitter.com/AltPhinny/status/1383048535923421187/photo/1"
                tweetStatus = "I'm not crazy, YOU'RE crazy!!"
            elif (x == 110):
                mediaLink = " https://twitter.com/AltPhinny/status/1383048621000654848/photo/1"
                tweetStatus = "LET. ME. OUT."
            elif (x == 111):
                mediaLink = " https://twitter.com/AltPhinny/status/1383048738051084288/photo/1"
                tweetStatus = "I've always wondered what the white part of my eye is (it's a sclera)"
            elif (x == 112):
                mediaLink = " https://twitter.com/AltPhinny/status/1383048858465357834/photo/1"
                tweetStatus = "I wasn't able to get my Youtooz ;( (I got it!!)"
            elif (x == 113):
                mediaLink = " https://twitter.com/AltPhinny/status/1383048882872053769/photo/1"
                tweetStatus = "This excludes @Quackity for kicking me"
            elif (x == 114):
                mediaLink = " https://twitter.com/AltPhinny/status/1383049120345161736/photo/1"
                tweetStatus = "Bad likes taking pictures of when I'm crying >:("
            elif (x == 115):
                mediaLink = " https://twitter.com/AltPhinny/status/1383049630594764800/photo/1"
                tweetStatus = "I'm a cutie without putting in any eFfort"
            elif (x == 116):
                mediaLink = " https://twitter.com/AltPhinny/status/1383049731761434625/photo/1"
                tweetStatus = "ACHOO!!"
            elif (x == 117):
                mediaLink = " https://twitter.com/AltPhinny/status/1383049844231651329/photo/1"
                tweetStatus = "I sense some itching in the very near future..."
            elif (x == 118):
                mediaLink = " https://twitter.com/AltPhinny/status/1383050003149697027/photo/1"
                tweetStatus = "ARE YOU TEASING ME AGAIN BECAUSE I CAN'T EAT CHOCOLATE!?"
            elif (x == 119):
                mediaLink = " https://twitter.com/AltPhinny/status/1383050191473872896/photo/1"
                tweetStatus = "I've even a cutie upside-down"
            elif (x == 120):
                mediaLink = " https://twitter.com/AltPhinny/status/1383050341948743681/photo/1"
                tweetStatus = "I'm not liking hoW my neck feels"
            elif (x == 121):
                mediaLink = " https://twitter.com/AltPhinny/status/1383050482399199232/photo/1"
                tweetStatus = "This is humiliAting, Bad"
            elif (x == 122):
                mediaLink = " https://twitter.com/AltPhinny/status/1383050845416259586/photo/1"
                tweetStatus = "You're not posting pictures of me like this to Twitter!"
            elif (x == 123):
                mediaLink = " https://twitter.com/AltPhinny/status/1383051396510007298/photo/1"
                tweetStatus = "Fine, you got your photo-op, " + handle_no_paren + ". Now where are my treats?"
            elif (x == 124):
                mediaLink = " https://twitter.com/AltPhinny/status/1383051464550014989/photo/1"
                tweetStatus = "I'm feeling dizzy..."
            elif (x == 125):
                mediaLink = " https://twitter.com/AltPhinny/status/1383051935251566593/photo/1"
                tweetStatus = "I'm not sure what this image is supposed to be"
            elif (x == 126):
                mediaLink = " https://twitter.com/AltPhinny/status/1383052013018173440/photo/1"
                tweetStatus = "PantinG is supposed to make my temperature cool down"
            elif (x == 127):
                mediaLink = " https://twitter.com/AltPhinny/status/1383052544793010176/photo/1"
                tweetStatus = "I looK like a rose with seeds"
            elif (x == 128):
                mediaLink = " https://twitter.com/AltPhinny/status/1383052612602368005/photo/1"
                tweetStatus = "I'm currently playing hide and seek"
            elif (x == 129):
                mediaLink = " https://twitter.com/AltPhinny/status/1383052660979425280/photo/1"
                tweetStatus = "Did you know that my nickname is Rat because I look like one when my hair's cut?"
            elif (x == 130):
                mediaLink = " https://twitter.com/AltPhinny/status/1383052723269013505/photo/1"
                tweetStatus = "I'm very confused at the moment"
            elif (x == 131):
                mediaLink = " https://twitter.com/AltPhinny/status/1383052813018746888/photo/1"
                tweetStatus = "Get that camera out of my face!"
            elif (x == 132):
                mediaLink = " https://twitter.com/AltPhinny/status/1383053058708533250/photo/1"
                tweetStatus = "The other Rat and I love doing everything together"
            elif (x == 133):
                mediaLink = " https://twitter.com/AltPhinny/status/1383053116795465733/photo/1"
                tweetStatus = "Something we all have in common is the need to sleep"
            elif (x == 134):
                mediaLink = " https://twitter.com/AltPhinny/status/1383053230872084485/photo/1"
                tweetStatus = "I'M BEING USED AS A PILLOW!"
            elif (x == 135):
                mediaLink = " https://twitter.com/AltPhinny/status/1383053286048198662/photo/1"
                tweetStatus = "What in the world is going on!"
            elif (x == 136):
                mediaLink = " https://twitter.com/AltPhinny/status/1383053404445028355/photo/1"
                tweetStatus = "Ok, that is weird, and this is coming from someone who plays with paper plates"
            elif (x == 137):
                mediaLink = " https://twitter.com/AltPhinny/status/1383053556886994947/photo/1"
                tweetStatus = "I'm gonna pretend I'm sleeping until Bad takes his fingers off me"
            elif (x == 138):
                mediaLink = " https://twitter.com/AltPhinny/status/1383053633642770432/photo/1"
                tweetStatus = "Who in their right mind eats pickle chips?!"
            elif (x == 139):
                mediaLink = " https://twitter.com/AltPhinny/status/1383053722616487936/photo/1"
                tweetStatus = "Potato chips are just empty calories, and I'm not eating them"
            elif (x == 140):
                mediaLink = " https://twitter.com/AltPhinny/status/1383053791898009603/photo/1"
                tweetStatus = "You see? " + handle_no_paren + "'s hopeless..."
            elif (x == 141):
                mediaLink = " https://twitter.com/AltPhinny/status/1383053862349762567/photo/1"
                tweetStatus = "I accept any gifts you have for me, " + handle_no_paren
            elif (x == 142):
                mediaLink = " https://twitter.com/AltPhinny/status/1383054121486450689/photo/1"
                tweetStatus = "Why did Phineas even add this picture to the bot? There's nothing to it"
            elif (x == 143):
                mediaLink = " https://twitter.com/AltPhinny/status/1383054198640611330/photo/1"
                tweetStatus = "I'm not a fan of the camera"
            elif (x == 144):
                mediaLink = " https://twitter.com/AltPhinny/status/1383054365427122182/photo/1"
                tweetStatus = "I just want to sleep in peace"
            elif (x == 145):
                mediaLink = " https://twitter.com/AltPhinny/status/1383054437892100100/photo/1"
                tweetStatus = "I'm getting tired of writing captions"
            elif (x == 146):
                mediaLink = " https://twitter.com/AltPhinny/status/1383054587339411461/photo/1"
                tweetStatus = "That is not a mess I want to be a part of"
            elif (x == 147):
                mediaLink = " https://twitter.com/AltPhinny/status/1383054730201554951/photo/1"
                tweetStatus = "Just a blank stare, nothing else"
            elif (x == 148):
                mediaLink = " https://twitter.com/AltPhinny/status/1383055337587113986/photo/1"
                tweetStatus = "I've finally learned to look directly into the lense of the camera"
            elif (x == 149):
                mediaLink = " https://twitter.com/AltPhinny/status/1383055537399533570/photo/1"
                tweetStatus = "Why does Phineas keep gathering low-quality images!?"
            elif (x == 150):
                mediaLink = " https://twitter.com/AltPhinny/status/1383055729154789381/photo/1"
                tweetStatus = "I love my sweater!"
            elif (x == 151):
                mediaLink = " https://twitter.com/AltPhinny/status/1383055894016053249/photo/1"
                tweetStatus = "I don't want to eat my vegetables!"
            elif (x == 152):
                mediaLink = " https://twitter.com/AltPhinny/status/1383055963905724419/photo/1"
                tweetStatus = "Yo, what's up?"
            elif (x == 153):
                mediaLink = " https://twitter.com/AltPhinny/status/1383056021514502151/photo/1"
                tweetStatus = "Uhhhh, woof"
            elif (x == 154):
                mediaLink = " https://twitter.com/AltPhinny/status/1383056076908728331/photo/1"
                tweetStatus = "I'm just preparing for the snacks"
            elif (x == 155):
                mediaLink = " https://twitter.com/AltPhinny/status/1383056144327974914/photo/1"
                tweetStatus = "I'm cuter than the other Rat"
            elif (x == 156):
                mediaLink = " https://twitter.com/AltPhinny/status/1383056300322521089/photo/1"
                tweetStatus = "Tilting my head makes me cuter and gets me more snacks"
            elif (x == 157):
                mediaLink = " https://twitter.com/AltPhinny/status/1383056482980278280/photo/1"
                tweetStatus = "Who needs blankets when you've got a sweater?"
            elif (x == 158):
                mediaLink = " https://twitter.com/AltPhinny/status/1383056664937500672/photo/1"
                tweetStatus = "Yet another low-quality image, Phineas..."
            elif (x == 159):
                mediaLink = " https://twitter.com/AltPhinny/status/1383056748731371520/photo/1"
                tweetStatus = "I love filters!!"
            elif (x == 160):
                mediaLink = " https://twitter.com/AltPhinny/status/1383056841052131333/photo/1"
                tweetStatus = handle_no_paren + ", I know you have snacks, so hand them over peacefully"
            elif (x == 161):
                mediaLink = " https://twitter.com/AltPhinny/status/1383056944777289730/photo/1"
                tweetStatus = "I think I'm in need of a good scrub"
            elif (x == 162):
                mediaLink = " https://twitter.com/AltPhinny/status/1383057143109144576/photo/1"
                tweetStatus = "Is there something for me?!"
            elif (x == 163):
                mediaLink = " https://twitter.com/AltPhinny/status/1383057252660224001/photo/1"
                tweetStatus = "LANGUAGE!"
            elif (x == 164):
                mediaLink = " https://twitter.com/AltPhinny/status/1383057336613359617/photo/1"
                tweetStatus = "I'd look so cute in this!!"
            elif (x == 165):
                mediaLink = " https://twitter.com/AltPhinny/status/1383057404837904396/photo/1"
                tweetStatus = "Why does Bad keep embarrassing himself?"
            elif (x == 166):
                mediaLink = " https://twitter.com/AltPhinny/status/1383057465554702341/photo/1"
                tweetStatus = "WHAT ARE YOU DOING!? I haven't done my hair yet!!"
            elif (x == 167):
                mediaLink = " https://twitter.com/AltPhinny/status/1383057666138898433/photo/1"
                tweetStatus = "To be honest, I don't like potatoes"
            elif (x == 168):
                mediaLink = " https://twitter.com/AltPhinny/status/1383057756660318208/photo/1"
                tweetStatus = "I'm so cute that I'm gonna be on the Vogue cover next year"
            elif (x == 169):
                mediaLink = " https://twitter.com/AltPhinny/status/1383057991528812551/photo/1"
                tweetStatus = "Only a bar separates us"
            elif (x == 170):
                mediaLink = " https://twitter.com/AltPhinny/status/1383058165965668357/photo/1"
                tweetStatus = "You people are awesome!"
            elif (x == 171):
                mediaLink = " https://twitter.com/AltPhinny/status/1383058230994206723/photo/1"
                tweetStatus = "All I want for Christmas, is treats!!"
            elif (x == 172):
                mediaLink = " https://twitter.com/AltPhinny/status/1383058372199596033/photo/1"
                tweetStatus = "I'm not coming out until Bad gives me a muffin!"
            elif (x == 173):
                mediaLink = " https://twitter.com/AltPhinny/status/1383058558951043072/photo/1"
                tweetStatus = "I wasn't given any muffins :("
            elif (x == 174):
                mediaLink = " https://twitter.com/AltPhinny/status/1383091640391364608/photo/1"
                tweetStatus = "Why do I hear so much language in Bad's Jackbox game?"
            elif (x == 175):
                mediaLink = " https://twitter.com/AltPhinny/status/1383091747203452931/photo/1"
                tweetStatus = "I'm a birthday Rat!"
            elif (x == 176):
                mediaLink = " https://twitter.com/AltPhinny/status/1383091824470937601/photo/1"
                tweetStatus = "Why do we even have birthday parties?"
            elif (x == 177):
                mediaLink = " https://twitter.com/AltPhinny/status/1383091879462510597/photo/1"
                tweetStatus = "Bad's getting stalkerish, taking pictures while I'm sleeping"
            elif (x == 178):
                mediaLink = " https://twitter.com/AltPhinny/status/1383091942993563649/photo/1"
                tweetStatus = "That's how I look whenever Bad says Lucy"
            elif (x == 179):
                mediaLink = " https://twitter.com/AltPhinny/status/1383092028683264002/photo/1"
                tweetStatus = "Are there phones on your game?"
            elif (x == 180):
                mediaLink = " https://twitter.com/AltPhinny/status/1383092107510960129/photo/1"
                tweetStatus = "I can count the individual pixels in this picture"
            elif (x == 181):
                mediaLink = " https://twitter.com/AltPhinny/status/1383092189023109125/photo/1"
                tweetStatus = "When I'm sleeping, I only think about treats, language, muffins, and 14"
            elif (x == 182):
                mediaLink = " https://twitter.com/AltPhinny/status/1383092260984786945/photo/1"
                tweetStatus = "Do you play Club Penguin, " + handle_no_paren + "?"
            elif (x == 183):
                mediaLink = " https://twitter.com/AltPhinny/status/1383092347379007491/photo/1"
                tweetStatus = "Are you subscribed to BadBoyHalo and Skeppy? (and PhineasCPR, shhhhh)"
            elif (x == 184):
                mediaLink = " https://twitter.com/AltPhinny/status/1383092426563325969/photo/1"
                tweetStatus = "I am making this apology video because of what I did on camera to get treats"
            elif (x == 185):
                mediaLink = " https://twitter.com/AltPhinny/status/1383092538056261647/photo/1"
                tweetStatus = "I am very sad that you don't think I'm as cute as I know I am"
            elif (x == 186):
                mediaLink = " https://twitter.com/AltPhinny/status/1383092686131974153/photo/1"
                tweetStatus = "DRY ME!"
            elif (x == 187):
                mediaLink = " https://twitter.com/AltPhinny/status/1383092762904563713/photo/1"
                tweetStatus = "This is a random time to take a picture of me, Bad"
            elif (x == 188):
                mediaLink = " https://twitter.com/AltPhinny/status/1386845025745702917/photo/1"
                tweetStatus = "This is not my full height"
            elif (x == 189):
                mediaLink = " https://twitter.com/AltPhinny/status/1386845182302302216/photo/1"
                tweetStatus = "Num num num num num (I'm trying to imitate Stampy)"
            elif (x == 190):
                mediaLink = " https://twitter.com/AltPhinny/status/1386845748822777857/photo/1"
                tweetStatus = "Pouting gets me treats"
            elif (x == 191):
                mediaLink = " https://twitter.com/AltPhinny/status/1386845804397223943/photo/1"
                tweetStatus = "Bad thinks I'm a garden gnome for some reason..."
            elif (x == 192):
                mediaLink = " https://twitter.com/AltPhinny/status/1386846296422690819/photo/1"
                tweetStatus = "Time for bed"
            elif (x == 193):
                mediaLink = " https://twitter.com/AltPhinny/status/1386846407517212674/photo/1"
                tweetStatus = "I'm a supermodel"
            elif (x == 194):
                mediaLink = " https://twitter.com/AltPhinny/status/1386846476748328965/photo/1"
                tweetStatus = "I'm a bit worried about something..."
            elif (x == 195):
                mediaLink = " https://twitter.com/AltPhinny/status/1386846559300636672/photo/1"
                tweetStatus = "Bad's obsession with the camera is getting annoying"
            elif (x == 196):
                mediaLink = " https://twitter.com/AltPhinny/status/1386846631572684805/photo/1"
                tweetStatus = "Again, parties are overrated"
            elif (x == 197):
                mediaLink = " https://twitter.com/AltPhinny/status/1386846754767872009/photo/1"
                tweetStatus = "Peek-a-boo!"
            elif (x == 198):
                mediaLink = " https://twitter.com/AltPhinny/status/1386847122293678080/photo/1"
                tweetStatus = "There's someone behind me, " + handle_no_paren + "..."
            elif (x == 199):
                mediaLink = " https://twitter.com/AltPhinny/status/1386847215650476043/photo/1"
                tweetStatus = "Flip the camera!!"
            elif (x == 200):
                mediaLink = " https://twitter.com/AltPhinny/status/1386847337088180224/photo/1"
                tweetStatus = "Those eyes are eyes that want food"
            elif (x == 201):
                mediaLink = " https://twitter.com/AltPhinny/status/1386847492696854528/photo/1"
                tweetStatus = "Why am I so tall?!"
            elif (x == 202):
                mediaLink = " https://twitter.com/AltPhinny/status/1386847589526654976/photo/1"
                tweetStatus = "The look when you're pretending to listen but really aren't"
            elif (x == 203):
                mediaLink = " https://twitter.com/AltPhinny/status/1386847687128100876/photo/1"
                tweetStatus = "Ha, one of my eyes is covered!"
            elif (x == 204):
                mediaLink = " https://twitter.com/AltPhinny/status/1386847762810028040/photo/1"
                tweetStatus = "Oops, I left in a photo I wasn't meant to take!"
            elif (x == 205):
                mediaLink = " https://twitter.com/AltPhinny/status/1386847863259422720/photo/1"
                tweetStatus = "I'm a Bad Boy (even though I'm a girl)"
            elif (x == 206):
                mediaLink = " https://twitter.com/AltPhinny/status/1386847980087558147/photo/1"
                tweetStatus = "The question we all want answered is whether I will get the leftovers"
            elif (x == 207):
                mediaLink = " https://twitter.com/AltPhinny/status/1386848111235158017/photo/1"
                tweetStatus = "When's the Skeppy and Bad meet-up?! ;("
            elif (x == 208):
                mediaLink = " https://twitter.com/AltPhinny/status/1386848253975699456/photo/1"
                tweetStatus = "It's your birthday, happy birthday"
            elif (x == 209):
                mediaLink = " https://twitter.com/AltPhinny/status/1386848364621443076/photo/1"
                tweetStatus = "Sleepy time!"
            elif (x == 210):
                mediaLink = " https://twitter.com/AltPhinny/status/1386848637699899395/photo/1"
                tweetStatus = "What am I even looking at?"
            elif (x == 211):
                mediaLink = " https://twitter.com/AltPhinny/status/1388259988200644614/photo/1"
                tweetStatus = "The pollen keeps getting into my eyes!!"
            elif (x == 212):
                mediaLink = " https://twitter.com/AltPhinny/status/1388260026268147718/photo/1"
                tweetStatus = "La la la la, la la la la! " + handle_no_paren + "'s World!"
            elif (x == 213):
                mediaLink = " https://twitter.com/AltPhinny/status/1388260045998198786/photo/1"
                tweetStatus = "Mlem"
            elif (x == 214):
                mediaLink = " https://twitter.com/AltPhinny/status/1388262689126985729/photo/1"
                tweetStatus = "The blankie's too comfy"
            elif (x == 215):
                mediaLink = " https://twitter.com/AltPhinny/status/1388262838930743299/photo/1"
                tweetStatus = "Ready for my num-nums!"
            elif (x == 216):
                mediaLink = " https://twitter.com/AltPhinny/status/1388262911244742658/photo/1"
                tweetStatus = "Zzzzzzzz"
            elif (x == 217):
                mediaLink = " https://twitter.com/AltPhinny/status/1388263000562356225/photo/1"
                tweetStatus = "Please, " + handle_no_paren + ", I want some more"
            elif (x == 218):
                mediaLink = " https://twitter.com/AltPhinny/status/1388263105768079362/photo/1"
                tweetStatus = "Suffering from success"
            elif (x == 219):
                mediaLink = " https://twitter.com/AltPhinny/status/1388263180078551041/photo/1"
                tweetStatus = "Cozy!!"
            elif (x == 220):
                mediaLink = " https://twitter.com/AltPhinny/status/1388263262693863426/photo/1"
                tweetStatus = "When can I finally play with Rocco?"
            elif (x == 221):
                mediaLink = " https://twitter.com/AltPhinny/status/1388263336681353219/photo/1"
                tweetStatus = "Bad needs to cover up the sun..."
            elif (x == 222):
                mediaLink = " https://twitter.com/AltPhinny/status/1388263409070837760/photo/1"
                tweetStatus = "I do not like this cup, Sam-I-Am"
            elif (x == 223):
                mediaLink = " https://twitter.com/AltPhinny/status/1388263479807811586/photo/1"
                tweetStatus = "Am I asleep or awake?"
            elif (x == 224):
                mediaLink = " https://twitter.com/AltPhinny/status/1388263647533805573/photo/1"
                tweetStatus = "Very big and tall, I am"
            elif (x == 225):
                mediaLink = " https://twitter.com/AltPhinny/status/1388263868590329860/photo/1"
                tweetStatus = "I'm sad because Bad isn't letting me start my own vlogging channel"
            elif (x == 226):
                mediaLink = " https://twitter.com/AltPhinny/status/1388264063466184706/photo/1"
                tweetStatus = "Paper plates are the new Frisbee"
            elif (x == 227):
                mediaLink = " https://twitter.com/AltPhinny/status/1388264157674409989/photo/1"
                tweetStatus = "I really need a haircut"
            elif (x == 228):
                mediaLink = " https://twitter.com/AltPhinny/status/1388264229359206402/photo/1"
                tweetStatus = "Can you twist as much as I can?"
            elif (x == 229):
                mediaLink = " https://twitter.com/AltPhinny/status/1388264407487197189/photo/1"
                tweetStatus = "This is my Politician pose"
            elif (x == 230):
                mediaLink = " https://twitter.com/AltPhinny/status/1388264480652632071/photo/1"
                tweetStatus = "My fur is longer than the Eiffel Tower"
            elif (x == 231):
                mediaLink = " https://twitter.com/AltPhinny/status/1388264576920309762/photo/1"
                tweetStatus = "Why am I walking on dead grass?"
            elif (x == 232):
                mediaLink = " https://twitter.com/AltPhinny/status/1388264856919363584/photo/1"
                tweetStatus = "I'm looking for the AC"
            elif (x == 233):
                mediaLink = " https://twitter.com/AltPhinny/status/1388264998976344064/photo/1"
                tweetStatus = "I'm licking that plate clean!"
            elif (x == 234):
                mediaLink = " https://twitter.com/AltPhinny/status/1388265082774335495/photo/1"
                tweetStatus = "Shhhh, I'm sleeping"
            elif (x == 235):
                mediaLink = " https://twitter.com/AltPhinny/status/1388265170443677701/photo/1"
                tweetStatus = "Am I sitting on a shoe?!"
            elif (x == 236):
                mediaLink = " https://twitter.com/AltPhinny/status/1388265285120049159/photo/1"
                tweetStatus = "You are NOT taking me to the vet, " + handle_no_paren
            elif (x == 237):
                mediaLink = " https://twitter.com/AltPhinny/status/1388267671368654853/photo/1"
                tweetStatus = "Just got a shot from the vet. Get yours"
            elif (x == 238):
                mediaLink = " https://twitter.com/AltPhinny/status/1388267759860166657/photo/1"
                tweetStatus = "I'm just a pile of fur"
            elif (x == 239):
                mediaLink = " https://twitter.com/AltPhinny/status/1388267847433035777/photo/1"
                tweetStatus = "Cute"
            elif (x == 240):
                mediaLink = " https://twitter.com/AltPhinny/status/1388267924784308231/photo/1"
                tweetStatus = "I'm a snorer"
            elif (x == 241):
                mediaLink = " https://twitter.com/AltPhinny/status/1388268061724233740/photo/1"
                tweetStatus = "Time for some TV"
            elif (x == 242):
                mediaLink = " https://twitter.com/AltPhinny/status/1388268133987848195/photo/1"
                tweetStatus = "The floor is inviting me to sleep"
            elif (x == 243):
                mediaLink = " https://twitter.com/AltPhinny/status/1388268219027308547/photo/1"
                tweetStatus = "What's up?"
            elif (x == 244):
                mediaLink = " https://twitter.com/AltPhinny/status/1388268283372179456/photo/1"
                tweetStatus = "I hate these mid-moment shots"
            elif (x == 245):
                mediaLink = " https://twitter.com/AltPhinny/status/1388268377764945929/photo/1"
                tweetStatus = "The most seemingly-uncomfortable spots tend to be the most fun to sleep in"
            elif (x == 246):
                mediaLink = " https://twitter.com/AltPhinny/status/1388268455246372883/photo/1"
                tweetStatus = "Made ya look!"
            elif (x == 247):
                mediaLink = " https://twitter.com/AltPhinny/status/1388268546153754625/photo/1"
                tweetStatus = "Don't disturb me, " + handle_no_paren
            elif (x == 248):
                mediaLink = " https://twitter.com/AltPhinny/status/1388268597366169603/photo/1"
                tweetStatus = "You disturbed me"
            elif (x == 249):
                mediaLink = " https://twitter.com/AltPhinny/status/1388268778220408839/photo/1"
                tweetStatus = "Thank you for covering up the sun, " + handle_no_paren
            elif (x == 250):
                mediaLink = " https://twitter.com/AltPhinny/status/1388269081023889408/photo/1"
                tweetStatus = "Do you have games on your pager?"
            elif (x == 251):
                mediaLink = " https://twitter.com/AltPhinny/status/1388269196577067019/photo/1"
                tweetStatus = "I can take on KSI in a boxing match"
            elif (x == 252):
                mediaLink = " https://twitter.com/AltPhinny/status/1388269306480402435/photo/1"
                tweetStatus = "I live in the dishwasher now"
            elif (x == 253):
                mediaLink = " https://twitter.com/AltPhinny/status/1388269408301297664/photo/1"
                tweetStatus = "I look like a loaf of bread"
            elif (x == 254):
                mediaLink = " https://twitter.com/AltPhinny/status/1388269493647028224/photo/1"
                tweetStatus = "Nom nom"
            elif (x == 255):
                mediaLink = " https://twitter.com/AltPhinny/status/1388269563738050560/photo/1"
                tweetStatus = "Why do people think this pic is ugly?"
            elif (x == 256):
                mediaLink = " https://twitter.com/AltPhinny/status/1388269685301469185/photo/1"
                tweetStatus = "Floofy"
            elif (x == 257):
                mediaLink = " https://twitter.com/AltPhinny/status/1388269760346050562/photo/1"
                tweetStatus = "Huh?"
            elif (x == 258):
                mediaLink = " https://twitter.com/AltPhinny/status/1388269830067851264/photo/1"
                tweetStatus = "You called"
            elif (x == 259):
                mediaLink = " https://twitter.com/AltPhinny/status/1388269888771432449/photo/1"
                tweetStatus = "Did you know that 0! = 1?"
            elif (x == 260):
                mediaLink = " https://twitter.com/AltPhinny/status/1388269963169968129/photo/1"
                tweetStatus = "Tonight, I eat like a queen!"
            elif (x == 261):
                mediaLink = " https://twitter.com/AltPhinny/status/1388270052550524931/photo/1"
                tweetStatus = "Take my hand and hold on tight"
            elif (x == 262):
                mediaLink = " https://twitter.com/AltPhinny/status/1388270132410077184/photo/1"
                tweetStatus = "Say strawberry before I sneeze!!"
            elif (x == 263):
                mediaLink = " https://twitter.com/AltPhinny/status/1388270213045555206/photo/1"
                tweetStatus = "You didn't watch Stampy as a kid? Disappointing..."
            elif (x == 264):
                mediaLink = " https://twitter.com/AltPhinny/status/1388270322454040579/photo/1"
                tweetStatus = "Beware, " + handle_no_paren + "! I'm a dangerous doggo"
            elif (x == 265):
                mediaLink = " https://twitter.com/AltPhinny/status/1388270404716879872/photo/1"
                tweetStatus = "Phineas still hasn't finished the captions..."
            elif (x == 266):
                mediaLink = " https://twitter.com/AltPhinny/status/1388271169674129409/photo/1"
                tweetStatus = "Too blurry, NEXT"
            elif (x == 267):
                mediaLink = " https://twitter.com/AltPhinny/status/1388271556183351296/photo/1"
                tweetStatus = "I know treats when I sense them!"
            elif (x == 268):
                mediaLink = " https://twitter.com/AltPhinny/status/1388271664006406148/photo/1"
                tweetStatus = "My goal is to sleep in every part of the house"
            elif (x == 269):
                mediaLink = " https://twitter.com/AltPhinny/status/1388271773955801088/photo/1"
                tweetStatus = "CUT. MY. HAIR"
            elif (x == 270):
                mediaLink = " https://twitter.com/AltPhinny/status/1388271940582973442/photo/1"
                tweetStatus = "Just caught up on the latest Dream SMP lore..."
            elif (x == 271):
                mediaLink = " https://twitter.com/AltPhinny/status/1388272082765635585/photo/1"
                tweetStatus = "I cannot resist the pickle"
            elif (x == 272):
                mediaLink = " https://twitter.com/AltPhinny/status/1388272236608376832/photo/1"
                tweetStatus = "Why'd you wake me up in the middle of the night, " + handle_no_paren + "?!"
            elif (x == 273):
                mediaLink = " https://twitter.com/AltPhinny/status/1388272357907832836/photo/1"
                tweetStatus = "Gimme some of that, " + handle_no_paren + "!"
            elif (x == 274):
                mediaLink = " https://twitter.com/AltPhinny/status/1388272634266333187/photo/1"
                tweetStatus = "Let me rest in peace!"
            elif (x == 275):
                mediaLink = " https://twitter.com/AltPhinny/status/1388272822728994819/photo/1"
                tweetStatus = "I just remembered that I have another homework assignment due (bots incoming)"
            elif (x == 276):
                mediaLink = " https://twitter.com/AltPhinny/status/1388273031081074690/photo/1"
                tweetStatus = "Why do I stand up so often..."
            elif (x == 277):
                mediaLink = " https://twitter.com/AltPhinny/status/1388273178842124290/photo/1"
                tweetStatus = "People of Georgia!!"
            elif (x == 278):
                mediaLink = " https://twitter.com/AltPhinny/status/1388273299000594434/photo/1"
                tweetStatus = "I guess I'm pouting for some reason now..."
            elif (x == 279):
                mediaLink = " https://twitter.com/AltPhinny/status/1388273450255589376/photo/1"
                tweetStatus = "My hair is cut, and I am now sad"
            elif (x == 280):
                mediaLink = " https://twitter.com/AltPhinny/status/1388273893908140033/photo/1"
                tweetStatus = "Why put me through this humiliation, " + handle_no_paren + "?"
            elif (x == 281):
                mediaLink = " https://twitter.com/AltPhinny/status/1388324576841588739/photo/1"
                tweetStatus = "I am lit"
            elif (x == 282):
                mediaLink = " https://twitter.com/AltPhinny/status/1388324603609681921/photo/1"
                tweetStatus = "I look at right now and see glimpses of my past"
            elif (x == 283):
                mediaLink = " https://twitter.com/AltPhinny/status/1388324631971500034/photo/1"
                tweetStatus = "Unblock me, Dream!"
            elif (x == 284):
                mediaLink = " https://twitter.com/AltPhinny/status/1388324735646371840/photo/1"
                tweetStatus = "Will Thomas the Tank Engine Innit follow me?"
            elif (x == 285):
                mediaLink = " https://twitter.com/AltPhinny/status/1388324843205103625/photo/1"
                tweetStatus = "I will finally celebrate my birthday when " + handle_no_paren + " follows me"
            elif (x == 286):
                mediaLink = " https://twitter.com/AltPhinny/status/1388324922217353226/photo/1"
                tweetStatus = "This picture is weird..."
            elif (x == 287):
                mediaLink = " https://twitter.com/AltPhinny/status/1388325043990679555/photo/1"
                tweetStatus = "There is no such thing as Rat, only fur"
            elif (x == 288):
                mediaLink = " https://twitter.com/AltPhinny/status/1412076085144133632/photo/1"
                tweetStatus = "Amazing, " + handle_no_paren + "!"
            elif (x == 289):
                mediaLink = " https://twitter.com/AltPhinny/status/1412076445858402309/photo/1"
                tweetStatus = "Umm..."
            elif (x == 290):
                mediaLink = " https://twitter.com/AltPhinny/status/1412076495674224644/photo/1"
                tweetStatus = "Wake me up when it's all over"
            elif (x == 291):
                mediaLink = " https://twitter.com/AltPhinny/status/1412076538749722624/photo/1"
                tweetStatus = "Go away!!"
            elif (x == 292):
                mediaLink = " https://twitter.com/AltPhinny/status/1412076569556930568/photo/1"
                tweetStatus = "Quack!"
            elif (x == 293):
                mediaLink = " https://twitter.com/AltPhinny/status/1412076609046298628/photo/1"
                tweetStatus = "I am deeply hurt, " + handle_no_paren
            elif (x == 294):
                mediaLink = " https://twitter.com/AltPhinny/status/1412076646979547142/photo/1"
                tweetStatus = "Dogs don't eat PB&J!"
            elif (x == 295):
                mediaLink = " https://twitter.com/AltPhinny/status/1412076780014477315/photo/1"
                tweetStatus = "I'm now Ratè Bot!"
            elif (x == 296):
                mediaLink = " https://twitter.com/AltPhinny/status/1412077085712171010/photo/1"
                tweetStatus = "Bad got another Big Daddy mug..."
            elif (x == 297):
                mediaLink = " https://twitter.com/AltPhinny/status/1412077132453453831/photo/1"
                tweetStatus = "My tongue is longer than yours!"
            elif (x == 298):
                mediaLink = " https://twitter.com/AltPhinny/status/1412077154406486019/photo/1"
                tweetStatus = "The stick will DIE!"
            elif (x == 299):
                mediaLink = " https://twitter.com/AltPhinny/status/1412077200250224640/photo/1"
                tweetStatus = "I wear a mask with a smile for hours at a time..."
            elif (x == 300):
                mediaLink = " https://twitter.com/AltPhinny/status/1412077375681175558/photo/1"
                tweetStatus = "Bad can't tell us apart :("
            elif (x == 301):
                mediaLink = " https://twitter.com/AltPhinny/status/1412077410531614721/photo/1"
                tweetStatus = "Get. Him. Off. Me."
            elif (x == 302):
                mediaLink = " https://twitter.com/AltPhinny/status/1412077446585802752/photo/1"
                tweetStatus = "Boing!"
            elif (x == 303):
                mediaLink = " https://twitter.com/AltPhinny/status/1412077486091952133/photo/1"
                tweetStatus = "Am I a Rat or a muffin?"
            elif (x == 304):
                mediaLink = " https://twitter.com/AltPhinny/status/1412077516177784840/photo/1"
                tweetStatus = "MAKE THIS A THING!"
            elif (x == 305):
                mediaLink = " https://twitter.com/AltPhinny/status/1412077532191641601/photo/1"
                tweetStatus = "Motion blur makes everything better!"
            elif (x == 306):
                mediaLink = " https://twitter.com/AltPhinny/status/1412077562579275784/photo/1"
                tweetStatus = "I have bug eyes"
            elif (x == 307):
                mediaLink = " https://twitter.com/AltPhinny/status/1412077590043672583/photo/1"
                tweetStatus = "NOM!"
            elif (x == 308):
                mediaLink = " https://twitter.com/AltPhinny/status/1412077611782660099/photo/1"
                tweetStatus = "Uhh, time to move on, " + handle_no_paren
            elif (x == 309):
                mediaLink = " https://twitter.com/AltPhinny/status/1412077653272707072/photo/1"
                tweetStatus = "Why have we stopped, " + handle_no_paren + "?"
            elif (x == 310):
                mediaLink = " https://twitter.com/AltPhinny/status/1412077669630492673/photo/1"
                tweetStatus = "Post this to my Instagram!"
            elif (x == 311):
                mediaLink = " https://twitter.com/AltPhinny/status/1412077695488475138/photo/1"
                tweetStatus = "I am very 'boop'able"
            elif (x == 312):
                mediaLink = " https://twitter.com/AltPhinny/status/1412077722260627461/photo/1"
                tweetStatus = "Rat in blue"
            elif (x == 313):
                mediaLink = " https://twitter.com/AltPhinny/status/1412077748114399236/photo/1"
                tweetStatus = "Whoa there!"
            elif (x == 314):
                mediaLink = " https://twitter.com/AltPhinny/status/1412077777373831175/photo/1"
                tweetStatus = "Are you done there, " + handle_no_paren + "?"
            elif (x == 315):
                mediaLink = " https://twitter.com/AltPhinny/status/1412077803844034562/photo/1"
                tweetStatus = "Yum!"
            elif (x == 316):
                mediaLink = " https://twitter.com/AltPhinny/status/1412077846445625347/photo/1"
                tweetStatus = "I am pleading with " + handle_no_paren + " to give me treats"
            elif (x == 317):
                mediaLink = " https://twitter.com/AltPhinny/status/1412077870231568391/photo/1"
                tweetStatus = "*Licks*"
            elif (x == 318):
                mediaLink = " https://twitter.com/AltPhinny/status/1412077901130969099/photo/1"
                tweetStatus = "Upside-down Rat"
            elif (x == 319):
                mediaLink = " https://twitter.com/AltPhinny/status/1412077925965434882/photo/1"
                tweetStatus = "I don't see anything wrong with this"
            elif (x == 320):
                mediaLink = " https://twitter.com/AltPhinny/status/1412077950858633221/photo/1"
                tweetStatus = "What's your obsession with taking pictures of me with a blanket?"
            elif (x == 321):
                mediaLink = " https://twitter.com/AltPhinny/status/1412077973587566601/photo/1"
                tweetStatus = "This drama is AWESOME!"
            elif (x == 322):
                mediaLink = " https://twitter.com/AltPhinny/status/1412077996828237827/photo/1"
                tweetStatus = "Why are we at the McDonald's drive-thru?!"
            elif (x == 323):
                mediaLink = " https://twitter.com/AltPhinny/status/1412078025160671242/photo/1"
                tweetStatus = "Quakc"
            elif (x == 324):
                mediaLink = " https://twitter.com/AltPhinny/status/1412078052339765252/photo/1"
                tweetStatus = "GEROFF!"
            elif (x == 325):
                mediaLink = " https://twitter.com/AltPhinny/status/1412078076293533697/photo/1"
                tweetStatus = "EEEEEEE!!"
            elif (x == 326):
                mediaLink = " https://twitter.com/AltPhinny/status/1412078096900149255/photo/1"
                tweetStatus = "Let me out, " + handle_no_paren + " :("
            elif (x == 327):
                mediaLink = " https://twitter.com/AltPhinny/status/1412078123068411910/photo/1"
                tweetStatus = "The snack...is right there"
            elif (x == 328):
                mediaLink = " https://twitter.com/AltPhinny/status/1412088738105237507/photo/1"
                tweetStatus = "Just let me sleep, " + handle_no_paren
            elif (x == 329):
                mediaLink = " https://twitter.com/AltPhinny/status/1412088794287849477/photo/1"
                tweetStatus = "Do you like my Dream shirt, " + handle_no_paren + "?"
            elif (x == 330):
                mediaLink = " https://twitter.com/AltPhinny/status/1412088816186363904/photo/1"
                tweetStatus = "Esta caliente"
            elif (x == 331):
                mediaLink = " https://twitter.com/AltPhinny/status/1412088844858560514/photo/1"
                tweetStatus = "RAT PARTY!! (@ratparty_ please follow me)"
            elif (x == 332):
                mediaLink = " https://twitter.com/AltPhinny/status/1412088863040983041/photo/1"
                tweetStatus = "Blurry Rat"
            elif (x == 333):
                mediaLink = " https://twitter.com/AltPhinny/status/1412088920733622274/photo/1"
                tweetStatus = "Loopy Rat"
            elif (x == 334):
                mediaLink = " https://twitter.com/AltPhinny/status/1412088954044682245/photo/1"
                tweetStatus = "Okie"
            elif (x == 335):
                mediaLink = " https://twitter.com/AltPhinny/status/1412088979961389061/photo/1"
                tweetStatus = "Very tall hat!"
            elif (x == 336):
                mediaLink = " https://twitter.com/AltPhinny/status/1412089010743296000/photo/1"
                tweetStatus = "Why did @phineas1500 add this..."
            elif (x == 337):
                mediaLink = " https://twitter.com/AltPhinny/status/1412089043391848454/photo/1"
                tweetStatus = "I am shocked, " + handle_no_paren
            elif (x == 338):
                mediaLink = " https://twitter.com/AltPhinny/status/1412089070801543171/photo/1"
                tweetStatus = "I don't like potato"
            elif (x == 339):
                mediaLink = " https://twitter.com/AltPhinny/status/1412089104825827328/photo/1"
                tweetStatus = "ZZZZZ"
            elif (x == 340):
                mediaLink = " https://twitter.com/AltPhinny/status/1412089140032720903/photo/1"
                tweetStatus = "I think I've already added this pic to the bot..."
            elif (x == 341):
                mediaLink = " https://twitter.com/AltPhinny/status/1412089167543164931/photo/1"
                tweetStatus = "Bad and I with our friends!"
            elif (x == 342):
                mediaLink = " https://twitter.com/AltPhinny/status/1412089200636203017/photo/1"
                tweetStatus = "Leave me alone, " + handle_no_paren + "!"
            elif (x == 343):
                mediaLink = " https://twitter.com/AltPhinny/status/1412089224866799617/photo/1"
                tweetStatus = "Hewwo"
            elif (x == 344):
                mediaLink = " https://twitter.com/AltPhinny/status/1412089258836467717/photo/1"
                tweetStatus = "Orange"
            elif (x == 345):
                mediaLink = " https://twitter.com/AltPhinny/status/1412089273675878403/photo/1"
                tweetStatus = "Hard choice I have to make"
            elif (x == 346):
                mediaLink = " https://twitter.com/AltPhinny/status/1412089304650858501/photo/1"
                tweetStatus = "All I want to do is rest after a tiring day"
            elif (x == 347):
                mediaLink = " https://twitter.com/AltPhinny/status/1412089333616676865/photo/1"
                tweetStatus = "Night night!"
            elif (x == 348):
                mediaLink = " https://twitter.com/AltPhinny/status/1412089363509436417/photo/1"
                tweetStatus = "I am worried about " + handle_no_paren + "'s sleepwalking"
            elif (x == 349):
                mediaLink = " https://twitter.com/AltPhinny/status/1412089386699739138/photo/1"
                tweetStatus = "I yoinked " + handle_no_paren + "'s finger!"
            elif (x == 350):
                mediaLink = " https://twitter.com/AltPhinny/status/1412089412935168011/photo/1"
                tweetStatus = "Nose reveal"
            elif (x == 351):
                mediaLink = " https://twitter.com/AltPhinny/status/1412089441926144001/photo/1"
                tweetStatus = "Another repeat pic!"
            elif (x == 352):
                mediaLink = " https://twitter.com/AltPhinny/status/1412089486213799937/photo/1"
                tweetStatus = "Someone took a screenie of me on a stream. How rude!"
            elif (x == 353):
                mediaLink = " https://twitter.com/AltPhinny/status/1412089529654185989/photo/1"
                tweetStatus = "Baby Rat"
            elif (x == 354):
                mediaLink = " https://twitter.com/AltPhinny/status/1412089549707268097/photo/1"
                tweetStatus = "Grrrr"
            elif (x == 355):
                mediaLink = " https://twitter.com/AltPhinny/status/1412089581604950018/photo/1"
                tweetStatus = "You are wanted!"
            elif (x == 356):
                mediaLink = " https://twitter.com/AltPhinny/status/1412089606070284294/photo/1"
                tweetStatus = "ACHOOOOO!!!"
            elif (x == 357):
                mediaLink = " https://twitter.com/AltPhinny/status/1412089671732051972/photo/1"
                tweetStatus = "Another repeat pic I believe!"
            elif (x == 358):
                mediaLink = " https://twitter.com/AltPhinny/status/1412089705802440706/photo/1"
                tweetStatus = "GET OFF MINECRAFT, " + handle_no_paren + "!"
            elif (x == 359):
                mediaLink = " https://twitter.com/AltPhinny/status/1412090131364913157/photo/1"
                tweetStatus = "Who will nom?"
            elif (x == 360):
                mediaLink = " https://twitter.com/AltPhinny/status/1412090157419880450/photo/1"
                tweetStatus = "Floof"
            elif (x == 361):
                mediaLink = " https://twitter.com/AltPhinny/status/1412090348415881217/photo/1"
                tweetStatus = "Head tilts are a guaranteed cuteness boost"
            elif (x == 362):
                mediaLink = " https://twitter.com/AltPhinny/status/1412090367500038146/photo/1"
                tweetStatus = "This is like that jschatt pic"
            elif (x == 363):
                mediaLink = " https://twitter.com/AltPhinny/status/1412090476010819585/photo/1"
                tweetStatus = "*Yawns*"
            elif (x == 364):
                mediaLink = " https://twitter.com/AltPhinny/status/1412090510764908550/photo/1"
                tweetStatus = "Is this Rat or Gambit?"
            elif (x == 365):
                mediaLink = " https://twitter.com/AltPhinny/status/1412090538258538496/photo/1"
                tweetStatus = "One of you is doing something wrong, I just need to find out who it is"
            elif (x == 366):
                mediaLink = " https://twitter.com/AltPhinny/status/1412090562405179394/photo/1"
                tweetStatus = "The person who wakes me up will be cursed to eternal anguish"
            elif (x == 367):
                mediaLink = " https://twitter.com/AltPhinny/status/1412090595590430725/photo/1"
                tweetStatus = "I heard treats!"
            elif (x == 368):
                mediaLink = " https://twitter.com/AltPhinny/status/1412090614083198978/photo/1"
                tweetStatus = "As always, I'm a tall giant"
            elif (x == 369):
                mediaLink = " https://twitter.com/AltPhinny/status/1412090635130114048/photo/1"
                tweetStatus = "Don't worry, " + handle_no_paren + ", I'm just watching"
            elif (x == 370):
                mediaLink = " https://twitter.com/AltPhinny/status/1412090737345302528/photo/1"
                tweetStatus = "WHAT IN THE"
            elif (x == 371):
                mediaLink = " https://twitter.com/AltPhinny/status/1412090776989929475/photo/1"
                tweetStatus = "Baths are TERRIBLE, " + handle_no_paren
            elif (x == 372):
                mediaLink = " https://twitter.com/AltPhinny/status/1412090823102107650/photo/1"
                tweetStatus = "Cozy"
            elif (x == 373):
                mediaLink = " https://twitter.com/AltPhinny/status/1412090864638255114/photo/1"
                tweetStatus = "Good night moon"
            elif (x == 374):
                mediaLink = " https://twitter.com/AltPhinny/status/1412090899279106054/photo/1"
                tweetStatus = "Arr, me hearties, I do be Pirate Rat!"
            elif (x == 375):
                mediaLink = " https://twitter.com/AltPhinny/status/1412090941565984771/photo/1"
                tweetStatus = "Huh?"
            elif (x == 376):
                mediaLink = " https://twitter.com/AltPhinny/status/1412091011795410945/photo/1"
                tweetStatus = "Why am I turning my neck?"
            elif (x == 377):
                mediaLink = " https://twitter.com/AltPhinny/status/1412091145589596166/photo/1"
                tweetStatus = "I HAVE NO ARMS!!"
            elif (x == 378):
                mediaLink = " https://twitter.com/AltPhinny/status/1412091178443497472/photo/1"
                tweetStatus = "Sad for some reason"
            elif (x == 379):
                mediaLink = " https://twitter.com/AltPhinny/status/1412091200786604032/photo/1"
                tweetStatus = "For some reason this pic reminds me of something..."
            elif (x == 380):
                mediaLink = " https://twitter.com/AltPhinny/status/1412091271456473089/photo/1"
                tweetStatus = "TREATS?!"
            elif (x == 381):
                mediaLink = " https://twitter.com/AltPhinny/status/1412091313714089986/photo/1"
                tweetStatus = "That's odd"
            elif (x == 382):
                mediaLink = " https://twitter.com/AltPhinny/status/1412091348916834304/photo/1"
                tweetStatus = "Do I need a cut?"
            elif (x == 383):
                mediaLink = " https://twitter.com/AltPhinny/status/1412091395368751106/photo/1"
                tweetStatus = "Hi-lo!"
            elif (x == 384):
                mediaLink = "https://twitter.com/AltPhinny/status/1412091420672921610/photo/1 "
                tweetStatus = "You caption this pic!"
            elif (x == 385):
                mediaLink = " https://twitter.com/AltPhinny/status/1412091483809779719/photo/1"
                tweetStatus = "Fwiends!"
            elif (x == 386):
                mediaLink = " https://twitter.com/AltPhinny/status/1412091508325597190/photo/1"
                tweetStatus = "Why is Bad suddenly made out of vinyl?"
            elif (x == 387):
                mediaLink = " https://twitter.com/AltPhinny/status/1412091526981816320/photo/1"
                tweetStatus = "Ok"
            elif (x == 388):
                mediaLink = " https://twitter.com/AltPhinny/status/1412091560234258435/photo/1"
                tweetStatus = "Am I being punished?"
            elif (x == 389):
                mediaLink = " https://twitter.com/AltPhinny/status/1412091616110731269/photo/1"
                tweetStatus = "Quack nom"
            elif (x == 390):
                mediaLink = " https://twitter.com/AltPhinny/status/1412091685249634307/photo/1"
                tweetStatus = "GET THIS OFF ME!"
            elif (x == 391):
                mediaLink = " https://twitter.com/AltPhinny/status/1412091710360928257/photo/1"
                tweetStatus = "I'm resigned to the fact that I have to wear this for Bad's clout"
            elif (x == 392):
                mediaLink = " https://twitter.com/AltPhinny/status/1412091741650436100/photo/1"
                tweetStatus = "Can I even sleep with this duck on me?!"
            elif (x == 393):
                mediaLink = " https://twitter.com/AltPhinny/status/1412091772881276931/photo/1"
                tweetStatus = "Don't give me duck food"
            elif (x == 394):
                mediaLink = " https://twitter.com/AltPhinny/status/1412091807282958336/photo/1"
                tweetStatus = "They ask you how you are and you just have to say that you're fine when you're not really fine..."
            elif (x == 395):
                mediaLink = " https://twitter.com/AltPhinny/status/1412091886140116993/photo/1"
                tweetStatus = "Buy it so I can afford treats"
            elif (x == 396):
                mediaLink = " https://twitter.com/AltPhinny/status/1412091962509963264/photo/1"
                tweetStatus = "I see me!"
            elif (x == 397):
                mediaLink = " https://twitter.com/AltPhinny/status/1412092033301467153/photo/1"
                tweetStatus = "Camewa"
            elif (x == 398):
                mediaLink = " https://twitter.com/AltPhinny/status/1412092100552925184/photo/1"
                tweetStatus = "BOOP!"
            elif (x == 399):
                mediaLink = " https://twitter.com/AltPhinny/status/1412092167552647168/photo/1"
                tweetStatus = "Is this edible?"
            elif (x == 400):
                mediaLink = " https://twitter.com/AltPhinny/status/1412092316106493971/photo/1"
                tweetStatus = "What am I looking at?"
            elif (x == 401):
                mediaLink = " https://twitter.com/AltPhinny/status/1412092354614468610/photo/1"
                tweetStatus = "We're best friends!"
            elif (x == 402):
                mediaLink = " https://twitter.com/AltPhinny/status/1412092409354362888/photo/1"
                tweetStatus = "Phew, that was tiring"
            elif (x == 403):
                mediaLink = " https://twitter.com/AltPhinny/status/1412092471593553926/photo/1"
                tweetStatus = "Leave me be!"
            elif (x == 404):
                mediaLink = " https://twitter.com/AltPhinny/status/1412092488517656579/photo/1"
                tweetStatus = "This is your fault"
            elif (x == 405):
                mediaLink = " https://twitter.com/AltPhinny/status/1412092534881456129/photo/1"
                tweetStatus = "Plop!"
            elif (x == 406):
                mediaLink = " https://twitter.com/AltPhinny/status/1412092564371644418/photo/1"
                tweetStatus = "I love chocolate!!"
            elif (x == 407):
                mediaLink = " https://twitter.com/AltPhinny/status/1412092647792164867/photo/1"
                tweetStatus = "I love my stuffed animal!"
            elif (x == 408):
                mediaLink = " https://twitter.com/AltPhinny/status/1412092718608756743/photo/1"
                tweetStatus = "Idiot @phineas1500 is adding a lot of repeat pics..."
            elif (x == 409):
                mediaLink = " https://twitter.com/AltPhinny/status/1412092948104294401/photo/1"
                tweetStatus = "Not liking what I'm seeing"
            elif (x == 410):
                mediaLink = " https://twitter.com/AltPhinny/status/1412092974696173583/photo/1"
                tweetStatus = "EEEEE!!"
            elif (x == 411):
                mediaLink = " https://twitter.com/AltPhinny/status/1412093022842523649/photo/1"
                tweetStatus = "Wot"
            elif (x == 412):
                mediaLink = " https://twitter.com/AltPhinny/status/1412093051854524419/photo/1"
                tweetStatus = "Getting my Z's"
            elif (x == 413):
                mediaLink = " https://twitter.com/AltPhinny/status/1412093101020229633/photo/1"
                tweetStatus = "Sleepy Rat cam"
            elif (x == 414):
                mediaLink = " https://twitter.com/AltPhinny/status/1412093191541645318/photo/1"
                tweetStatus = "I still don't like my new stuffed animal"
            elif (x == 415):
                mediaLink = " https://twitter.com/AltPhinny/status/1412093237511217159/photo/1"
                tweetStatus = "Wot"
            elif (x == 416):
                mediaLink = " https://twitter.com/AltPhinny/status/1412093278833590275/photo/1"
                tweetStatus = "That's poggers!"
            elif (x == 417):
                mediaLink = " https://twitter.com/AltPhinny/status/1412093308520783875/photo/1"
                tweetStatus = "I need food"
            elif (x == 418):
                mediaLink = " https://twitter.com/AltPhinny/status/1412093339697127424/photo/1"
                tweetStatus = "I'm Justin Bieber!"
            elif (x == 419):
                mediaLink = " https://twitter.com/AltPhinny/status/1412093365798252556/photo/1"
                tweetStatus = "Bad will pay..."
            elif (x == 420):
                mediaLink = " https://twitter.com/AltPhinny/status/1412093411407110152/photo/1"
                tweetStatus = "It's a hard-knock life"
            elif (x == 421):
                mediaLink = " https://twitter.com/AltPhinny/status/1412093461281509381/photo/1"
                tweetStatus = "Blurry Rat is beautiful Rat"
            elif (x == 422):
                mediaLink = " https://twitter.com/AltPhinny/status/1412093539295633411/photo/1"
                tweetStatus = "I wonder what I'm eating..."
            elif (x == 423):
                mediaLink = " https://twitter.com/AltPhinny/status/1412093617192198144/photo/1"
                tweetStatus = "Why is the camera not focused on me?"
            elif (x == 424):
                mediaLink = " https://twitter.com/AltPhinny/status/1412093674352164866/photo/1"
                tweetStatus = "I don't touch blurry hands"
            elif (x == 425):
                mediaLink = " https://twitter.com/AltPhinny/status/1412093732699136005/photo/1"
                tweetStatus = "I can stand!!"
            elif (x == 426):
                mediaLink = " https://twitter.com/AltPhinny/status/1412093807676514316/photo/1"
                tweetStatus = "Yum-yum!"
            elif (x == 427):
                mediaLink = " https://twitter.com/AltPhinny/status/1412093857135841281/photo/1"
                tweetStatus = "Goodbye"
            elif (x == 428):
                mediaLink = " https://twitter.com/AltPhinny/status/1412093885623541760/photo/1"
                tweetStatus = "Comfy"
            elif (x == 429):
                mediaLink = " https://twitter.com/AltPhinny/status/1412093929110003715/photo/1"
                tweetStatus = "My YouTube profile pic!"
            elif (x == 430):
                mediaLink = " https://twitter.com/AltPhinny/status/1412093966703546376/photo/1"
                tweetStatus = "Get your muffin mix here!"
            elif (x == 431):
                mediaLink = " https://twitter.com/AltPhinny/status/1412094015219146756/photo/1"
                tweetStatus = "I want da Fanta!"
            elif (x == 432):
                mediaLink = " https://twitter.com/AltPhinny/status/1412094188502585345/photo/1"
                tweetStatus = "I'm in the Army!"
            elif (x == 433):
                mediaLink = " https://twitter.com/AltPhinny/status/1422209924688396301/photo/1"
                tweetStatus = "I want to eat this"
            elif (x == 434):
                mediaLink = " https://twitter.com/AltPhinny/status/1422210333658296322/photo/1"
                tweetStatus = "Poof!"
            elif (x == 435):
                mediaLink = " https://twitter.com/AltPhinny/status/1422210921989120002/photo/1"
                tweetStatus = "No camera allowed!"
            elif (x == 436):
                mediaLink = " https://twitter.com/AltPhinny/status/1422211396117348354/photo/1"
                tweetStatus = "Gimme my snacks"
            elif (x == 437):
                mediaLink = " https://twitter.com/AltPhinny/status/1422211427503378432/photo/1"
                tweetStatus = "Adidas!"
            elif (x == 438):
                mediaLink = " https://twitter.com/AltPhinny/status/1422211452862177284/photo/1"
                tweetStatus = "Please stop petting me"
            elif (x == 439):
                mediaLink = " https://twitter.com/AltPhinny/status/1422211514963042307/photo/1"
                tweetStatus = "Amazing!"
            elif (x == 440):
                mediaLink = " https://twitter.com/AltPhinny/status/1422211535921983497/photo/1"
                tweetStatus = ":p"
            elif (x == 441):
                mediaLink = " https://twitter.com/AltPhinny/status/1422211555471593473/photo/1"
                tweetStatus = "Z_Z"
            elif (x == 442):
                mediaLink = " https://twitter.com/AltPhinny/status/1422211581295964160/photo/1"
                tweetStatus = "I'm the queen of num-nums!"
            elif (x == 443):
                mediaLink = " https://twitter.com/AltPhinny/status/1422211603206971394/photo/1"
                tweetStatus = "Mr. @phineas1500 has found a lot of four-leaf clovers in his time"
            elif (x == 444):
                mediaLink = " https://twitter.com/AltPhinny/status/1422211667593728006/photo/1"
                tweetStatus = "Another repeat pic!"
            elif (x == 445):
                mediaLink = " https://twitter.com/AltPhinny/status/1422211690280665092/photo/1"
                tweetStatus = "NOM"
            elif (x == 446):
                mediaLink = " https://twitter.com/AltPhinny/status/1422211779980054529/photo/1"
                tweetStatus = "Grrr"
            elif (x == 447):
                mediaLink = " https://twitter.com/AltPhinny/status/1422211816596426756/photo/1"
                tweetStatus = "I'm in a vortex!"
            elif (x == 448):
                mediaLink = " https://twitter.com/AltPhinny/status/1422211836884180992/photo/1"
                tweetStatus = "Another Rat cam pic"
            elif (x == 449):
                mediaLink = " https://twitter.com/AltPhinny/status/1422211887450701826/photo/1"
                tweetStatus = "Boo-a-peek!"
            elif (x == 450):
                mediaLink = " https://twitter.com/AltPhinny/status/1422211967348051979/photo/1"
                tweetStatus = "Do I need a trim?"
            elif (x == 451):
                mediaLink = " https://twitter.com/AltPhinny/status/1422211988508266500/photo/1"
                tweetStatus = "Use this as your banner!"
            elif (x == 452):
                mediaLink = " https://twitter.com/AltPhinny/status/1422212078174154753/photo/1"
                tweetStatus = "Bebè Rat"
            elif (x == 453):
                mediaLink = " https://twitter.com/AltPhinny/status/1422212179957329921/photo/1"
                tweetStatus = "Gimme!"
            elif (x == 454):
                mediaLink = " https://twitter.com/AltPhinny/status/1422214048679186436/photo/1"
                tweetStatus = "Spot me in this!"
            elif (x == 455):
                mediaLink = " https://twitter.com/AltPhinny/status/1422215596289241093/photo/1"
                tweetStatus = "You're playing with me"
            elif (x == 456):
                mediaLink = " https://twitter.com/AltPhinny/status/1422215620314152961/photo/1"
                tweetStatus = "Fuzzy"
            elif (x == 457):
                mediaLink = " https://twitter.com/AltPhinny/status/1422215668301172736/photo/1"
                tweetStatus = "Rat burrito"
            elif (x == 458):
                mediaLink = " https://twitter.com/AltPhinny/status/1422217554567868424/photo/1"
                tweetStatus = "Skateboarder Rat"
            elif (x == 459):
                mediaLink = " https://twitter.com/AltPhinny/status/1422217600247926795/photo/1"
                tweetStatus = "Are we done? I'm not liking your additude"
            elif (x == 460):
                mediaLink = " https://twitter.com/AltPhinny/status/1422218104927662087/photo/1"
                tweetStatus = "Are you ready?"
            elif (x == 461):
                mediaLink = " https://twitter.com/AltPhinny/status/1422218131376852995/photo/1"
                tweetStatus = "I'm just watching the drama unfold"
            elif (x == 462):
                mediaLink = " https://twitter.com/AltPhinny/status/1422218210988986369/photo/1"
                tweetStatus = "ZOOM!"
            elif (x == 463):
                mediaLink = " https://twitter.com/AltPhinny/status/1422218254760779778/photo/1"
                tweetStatus = "Time to mope"
            elif (x == 464):
                mediaLink = " https://twitter.com/AltPhinny/status/1422218280987660291/photo/1"
                tweetStatus = "Do you have any issues with me?"
            elif (x == 465):
                mediaLink = " https://twitter.com/AltPhinny/status/1422218375749672961/photo/1"
                tweetStatus = "Profile picture Rat!"
            elif (x == 466):
                mediaLink = " https://twitter.com/AltPhinny/status/1422218453080018948/photo/1"
                tweetStatus = "Stop. Taking. Pictures. Of. Me. In. Bed."
            elif (x == 467):
                mediaLink = " https://twitter.com/AltPhinny/status/1422218615588278274/photo/1"
                tweetStatus = "Time for a walk?"
            elif (x == 468):
                mediaLink = " https://twitter.com/AltPhinny/status/1422218760686120960/photo/1"
                tweetStatus = "My eyes are my defining feature"
            elif (x == 469):
                mediaLink = " https://twitter.com/AltPhinny/status/1422218956564307968/photo/1"
                tweetStatus = "Is this pic even discernible?"
            elif (x == 470):
                mediaLink = " https://twitter.com/AltPhinny/status/1422219107295023104/photo/1"
                tweetStatus = "I like my red vest"
            elif (x == 471):
                mediaLink = " https://twitter.com/AltPhinny/status/1422219149879693315/photo/1"
                tweetStatus = "I recognize this pic..."
            elif (x == 472):
                mediaLink = " https://twitter.com/AltPhinny/status/1422219201905897474/photo/1"
                tweetStatus = "You know I have a face..."
            elif (x == 473):
                mediaLink = " https://twitter.com/AltPhinny/status/1422219224538288132/photo/1"
                tweetStatus = "Banner Rat!"
            elif (x == 474):
                mediaLink = " https://twitter.com/AltPhinny/status/1422219244842930178/photo/1"
                tweetStatus = "Back in my day..."
            elif (x == 475):
                mediaLink = " https://twitter.com/AltPhinny/status/1422219315110162433/photo/1"
                tweetStatus = "Confused Rat"
            elif (x == 476):
                mediaLink = " https://twitter.com/AltPhinny/status/1422219355555864580/photo/1"
                tweetStatus = "Almost done with the captions"
            elif (x == 477):
                mediaLink = " https://twitter.com/AltPhinny/status/1422219379123621888/photo/1"
                tweetStatus = "The first pic in the Rat album!"
            elif (x == 478):
                mediaLink = " https://twitter.com/AltPhinny/status/1422223220183388163/photo/1"
                tweetStatus = "Drip Rat"
            elif (x == 479):
                mediaLink = " https://twitter.com/AltPhinny/status/1422223253372907522/photo/1"
                tweetStatus = "This looks unusual, " + handle_no_paren + "..."
            elif (x == 480):
                mediaLink = " https://twitter.com/AltPhinny/status/1422291405268033539/photo/1"
                tweetStatus = "Gogy is a Rat Stan!"
            elif (x == 481):
                mediaLink = " https://twitter.com/AltPhinny/status/1422292106249375749/photo/1"
                tweetStatus = "It's a struggle being me"
            elif (x == 482):
                mediaLink = " https://twitter.com/AltPhinny/status/1422292843788480517/photo/1"
                tweetStatus = "This is fine"
            elif (x == 483):
                mediaLink = " https://twitter.com/AltPhinny/status/1604937164223029256/photo/1"
                tweetStatus = "RAWR"
            elif (x == 484):
                mediaLink = " https://twitter.com/AltPhinny/status/1604937377880875023/photo/1"
                tweetStatus = "I have flawless teeth"
            elif (x == 485):
                mediaLink = " https://twitter.com/AltPhinny/status/1604937589999411214/photo/1"
                tweetStatus = "BABY SHARK DODODODODODO"
            elif (x == 486):
                mediaLink = " https://twitter.com/AltPhinny/status/1604937876944609280/photo/1"
                tweetStatus = "Jingle Bells, Batman Smells"
            elif (x == 487):
                mediaLink = " https://twitter.com/AltPhinny/status/1604938123758436353/photo/1"
                tweetStatus = "Why does BBH look different..."
            elif (x == 488):
                mediaLink = " https://twitter.com/AltPhinny/status/1604938290905243648/photo/1"
                tweetStatus = "Could you brush the hair out of my eye?"
            elif (x == 489):
                mediaLink = " https://twitter.com/AltPhinny/status/1604938512654016518/photo/1"
                tweetStatus = "Yoga time!"
            elif (x == 490):
                mediaLink = " https://twitter.com/AltPhinny/status/1604938705105346560/photo/1"
                tweetStatus = "I'm hungy"
            elif (x == 491):
                mediaLink = " https://twitter.com/AltPhinny/status/1604938862446661632/photo/1"
                tweetStatus = "I'd like to apologize for my past actions"
            elif (x == 492):
                mediaLink = " https://twitter.com/AltPhinny/status/1604939377649799168/photo/1"
                tweetStatus = "I hate looking like a rat"
            elif (x == 493):
                mediaLink = " https://twitter.com/AltPhinny/status/1604939575809298432/photo/1"
                tweetStatus = "Hiya!"
            elif (x == 494):
                mediaLink = " https://twitter.com/AltPhinny/status/1604939747822018585/photo/1"
                tweetStatus = "Very snazzy"
            elif (x == 495):
                mediaLink = " https://twitter.com/AltPhinny/status/1604940019524837393/photo/1"
                tweetStatus = "I like scratchies"
            elif (x == 496):
                mediaLink = " https://twitter.com/AltPhinny/status/1604940190308507657/photo/1"
                tweetStatus = "We're indiscernible"
            elif (x == 497):
                mediaLink = " https://twitter.com/AltPhinny/status/1604940428993765383/photo/1"
                tweetStatus = "Clean as a feather"
            elif (x == 498):
                mediaLink = " https://twitter.com/AltPhinny/status/1604940637777694720/photo/1"
                tweetStatus = "New kids on the block"
            elif (x == 499):
                mediaLink = " https://twitter.com/AltPhinny/status/1604940935846060032/photo/1"
                tweetStatus = "I could be like this forever"
            elif (x == 500):
                mediaLink = " https://twitter.com/AltPhinny/status/1615209748328058881/photo/1"
                tweetStatus = "Keep your friends close, and your enemies closer..."
            elif (x == 501):
                mediaLink = " https://twitter.com/AltPhinny/status/1615209773774917635/photo/1"
                tweetStatus = "What is my purpose, but to suffer?!"
            elif (x == 502):
                mediaLink = " https://twitter.com/AltPhinny/status/1615209803302707200/photo/1"
                tweetStatus = "This is my final stand"
            elif (x == 503):
                mediaLink = " https://twitter.com/AltPhinny/status/1615209824572305409/photo/1"
                tweetStatus = "WHY ARE YOU HELPING HIM, BAD?!"
            elif (x == 504):
                mediaLink = " https://twitter.com/AltPhinny/status/1615209844729954305/photo/1"
                tweetStatus = "So I'm just baggage then"
            elif (x == 505):
                mediaLink = " https://twitter.com/AltPhinny/status/1623106228246261763/photo/1"
                tweetStatus = "Queen-sized bed for a queen"
            elif (x == 506):
                mediaLink = " https://twitter.com/AltPhinny/status/1623106262375272450/photo/1"
                tweetStatus = "Is something about to happen?"
            elif (x == 507):
                mediaLink = " https://twitter.com/AltPhinny/status/1623106290829479936/photo/1"
                tweetStatus = "Why is a random man holding me with his mouth wide-open while Bad is pointing with his fingers making a triangle shape?"
            elif (x == 508):
                mediaLink = " https://twitter.com/AltPhinny/status/1623106322328690689/photo/1"
                tweetStatus = "STOP SMILING LIKE THAT!!"
            elif (x == 509):
                mediaLink = " https://twitter.com/AltPhinny/status/1623106349855830018/photo/1"
                tweetStatus = "I sense treats nearby"
            elif (x == 510):
                mediaLink = " https://twitter.com/AltPhinny/status/1623106386186977280/photo/1"
                tweetStatus = "All right, what's the script so we can fool all the viewers at home?"
            elif (x == 511):
                mediaLink = " https://twitter.com/AltPhinny/status/1623106415739957253/photo/1"
                tweetStatus = "Stop smelling me, only dogs can do that"
            elif (x == 512):
                mediaLink = " https://twitter.com/AltPhinny/status/1623106459700535297/photo/1"
                tweetStatus = "Why is this man's shirt so baggy?"
            elif (x == 513):
                mediaLink = " https://twitter.com/AltPhinny/status/1623106491082219520/photo/1"
                tweetStatus = "I have a feeling I won't like what's about to happen next..."
            elif (x == 514):
                mediaLink = " https://twitter.com/AltPhinny/status/1624883361645748230/photo/1"
                tweetStatus = "ROCCO, AT LONG LAST!!"
            elif (x == 515):
                mediaLink = " https://twitter.com/AltPhinny/status/1624883393706983425/photo/1"
                tweetStatus = "AEOUNGH!"
            elif (x == 516):
                mediaLink = " https://twitter.com/AltPhinny/status/1624883430583418881/photo/1"
                tweetStatus = "I like the yellow North Face logo on your shirt"
            elif (x == 517):
                mediaLink = " https://twitter.com/AltPhinny/status/1624883459637354498/photo/1"
                tweetStatus = "Good day, stream"
            elif (x == 518):
                mediaLink = " https://twitter.com/AltPhinny/status/1624883482794024963/photo/1"
                tweetStatus = "Please stop glaring at me, Skeppy"
              
            try:
                account.reply(tweetStatus + mediaLink, tweet_id=first_tweet_rest_id)
            except:
                print("Can't reply to that tweet")

        # Update the list of old tweet IDs
        old_ids[handle_no_paren] = first_tweet_rest_id
        time.sleep(55)

    # Save the updated list of tweet IDs back to the file
    save_ids('tweet_ids4.txt', old_ids)
