import random

print("This is Build 2 of the dumpster fire(c) AI\nsay something to the funny AI")

greeting = ["hell\no", "sup", "hi", "greetigs"]
keywords = ["doom", "math", "among", "bot", "hello"]
responses = ["yes", "i hate math", "AMOg uS!?!?", "We have detected automated abuse of Google coming from your Internet Service Provider. This page checks to see if it's really a human sending the requests and not a robot coming through your ISP's network. IP address: 151.188.137.226 Time: 2023-01-03T19:08:42Z", random.choice(greeting)]
randomwords = ["yes", "no", "idk", "sorry, i dont undersand", "I need to learn more", "sure man", "im not a bot"]

train = False # doesnt work yet

while True:
    userinput = input()
    userinput = userinput.lower()
   
    keyFound = False
    
    for index in range (len(keywords)):
        if (keywords[index] in userinput):
            if(train == False):
                print("AI: " + responses[index])
                keyFound = True

    if (keyFound == False and train == True): # training algorithm
        keywords.append(userinput)
        newRes = input("AI: What am I supposed to say to something like this?")
        responses.append(newRes)
        train = False
        
    if (keyFound == False and train == False):
        print("AI: " + random.choice(randomwords))
        randomwords.append(userinput)

   
