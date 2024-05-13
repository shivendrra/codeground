#para = input(str('enter a para'))      #for input
para = str("A paragraph is a group of sentences that convey an idea. Each sentence works together as part of a unit to create an overall thought or impression")
para_split = para.split('.' or '!' or '?')      #spliting the sentences

def split_sen():
    cmnWrds = []        #null list
    paraOne = para_split[0].split(' ')      #stored the first sentence
    paraTwo = para_split[1].split(' ')      #stored the second sentence
    for i in paraOne:   
        for j in paraTwo:   
            if i == j:      #common words checker
                cmnWrds.append(i)       #appending into the list
    print('Sen 1 has ', len(paraOne), 'words', '\n', 'Sen 2 has ', len(paraTwo), ' words')
    print('common words are', cmnWrds)

if(len(para_split) <= 2):       #checking the para length
    split_sen()
else:
    print("para is too long!")
