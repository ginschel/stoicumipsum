import random, sys, subprocess, platform
try:
    import pyperclip
except:
    print("You need to install pyperclip to run this program")
    subprocess.check_call([sys.executable, "-m", "pip3", "install", "pyperclip"])
    import pyperclip

#config

#Minimal length of stoicum ipsum text
min_txt_lngth = 600
inputfile = "meditationes"



#booleans
linenumbererror = False
generalerror = False
def giveipsum(linenumber):
    #to make the line number the same as its position in the list
    linenumber-=1
    #error handling
    if linenumber < 0:
        linenumbererror = True
        raise Exception("Please use a line number over 0")
    elif linenumber >= numberoflines:
        linenumber = numberoflines-1
    with open(inputfile, "r") as f:
        lines = f.readlines()
        return lines[linenumber]

txt = ""

#counts line number
with open(inputfile, "r") as f:
    numberoflines = sum(1 for lines in f)
#checks if a line number was given
try:
    option = sys.argv[1]
    i = 1
    temp = []
    queue = []
    #merge
    if option == "-m" or option == "-l" or option == "-r":
        try:
            while not (sys.argv[-i] == "-m" or sys.argv[-i] == "-l" or sys.argv[-i] == "-r"):
                temp.append(int(sys.argv[-i])); i+=1
            for x in range(len(temp), 0, -1): queue.append(temp[x-1]); 
            
            if option == "-m":
                for line in queue:
                    txt += giveipsum(line)
                        #enlarge to or more than the minimum length
            elif option == "-l":
                if len(queue) == 1:
                    x = 0
                    while len(txt) <= min_txt_lngth:
                     txt += giveipsum(queue[0]+x); x+=1
                     #in case you want a random line to have a minimum size
                elif len(queue) == 0:
                    x = 0
                    linenumber = random.randint(0, numberoflines)
                    while len(txt) <= min_txt_lngth:
                     txt += giveipsum(linenumber+x); x+=1;                  
                else:
                    raise Exception("You used one argument too much with the -l command")
               #range/merge of many ranges
            elif option == "-r":
                if len(queue) % 2 == 0:
                    x = len(queue)
                    y = 0
                    while x//2!=0:
                        x/=2; 
                        if queue[y] < queue[y+1]: 
                            for z in range(queue[y], queue[y+1]+1, 1):     txt += giveipsum(z); 
                            
                        elif queue[y] > queue[y+1]:
                            for z in range(queue[y], queue[y-1]-1, -1):     txt += giveipsum(z); 
                        
                        else: txt += giveipsum(queue[y]); 
                        y+=2


                else:
                    raise Exception("You specified a range with an odd number")


        except:
            if linenumbererror: 
                print("Please use a line number over 0")
            else:
                print("There was an error, you used the syntax of the command in the wrong way")


    #standard/ only one line will be displayed
    else:
        #check if passed argument is a digit 

        if not sys.argv[1].isdigit():
            print("There was an error, you used the syntax of the command in the wrong way")
            generalerror = True
        if not generalerror == True:     
            linenumber = int(sys.argv[1])
            txt += giveipsum(linenumber)

except:
    linenumber = random.randint(0, numberoflines)
    txt += giveipsum(linenumber)
   
#output
if not generalerror == True:
    print(txt)
    pyperclip.copy(txt)



