# Reading the table (Terminal and non-Terminal symbols are spaerated by space in parsing table)
table=[i.strip().split('\t') for i in open('grammar.txt','r').readlines()]
stack=['$']
startSymbol=table[1][0]
stack.append(startSymbol)
userInput=[i for i in open('input.txt','r').readlines()][0] # each token must be spaerated by space in input
inputBuffer = (userInput+' $').split(' ')
readingString=0
while stack[-1]!='$':
    if stack[-1]!=inputBuffer[readingString]:
        replaceProduction=''
        column=table[0].index(inputBuffer[readingString])
        row=[i for i,j in enumerate(table) if stack[-1]==j[0]]
        replaceProduction=table[row[0]][column]
        print("\n---------------------")
        print('Stack: ',stack[::-1])
        print('Input Buffer: ',inputBuffer[readingString:])
        print('Productin Which Should be Push in Stack: ',replaceProduction)
        if replaceProduction=="' '":
            break
        elif replaceProduction=='epsilon':
            stack.pop()
        else:
            stack.pop()
            for i in replaceProduction.split(' ')[::-1]:
                stack.append(i)
    else:
        print('--------------')
        print('Stack: ',stack[::-1])
        print('Input Buffer: ',inputBuffer[readingString:])
        print('Stack Top or InputBuffer First Element is Match So POP Stack and Move Reading String forward')
        stack.pop()
        readingString+=1
if stack[-1]=='$' and inputBuffer[readingString]:
    print('\n "',userInput,'" is Accepted String')
else:
    print('\n "',userInput,'" is Not Accepted String')