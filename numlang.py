#number language

guide = {}
guide[' '] = 0
nums = 1




for char in range(ord('A'), ord('Z') + 1):
    
    guide[chr(char)] = nums
    nums += 1
for char in range(ord('a'), ord('z') + 1):
    guide[chr(char)] = nums
    nums += 1


revguide = {v: k for k, v in guide.items()}

#encoding print encoded word    
def encoding(inputstr):
    res = []
    for st in inputstr:
        if st in guide:
            res .append(str(guide.get(st)))
    print(' '.join(res))


#decoding print decoded word
def decoding(inputnum):
    ans = []
    for nu in inputnum:
        if nu in revguide:
            ans.append(revguide[nu])
    print(''.join(ans))



#Execution
def coding():
    options = input("Enter 'Encode' for Encoding or else 'Decode' for Decoding : ").lower()
    if options == 'encode':
        inputstr  = input("Enter a string : ")
        encoding(inputstr)
    elif options == 'decode' :
        inputnum = input("Enter a string of numbers : ").split()
        inputnum = [int(n) for n in inputnum]
        decoding(inputnum)
    else:
        print("Invalid Input")


# used to repeat program
recontinue = ""
while recontinue.lower() != "f":
    recont = input(f"If you want to start, press 'start'. To stop, press 'stop': ").lower()
    if recont == 'start':
        coding()
    elif recont == 'stop':
        recontinue = "f"
    else:
        print("Invalid input")
