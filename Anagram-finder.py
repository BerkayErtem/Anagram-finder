from collections import Counter
def inputs():
    count1=Counter()
    count2=Counter()


    #inputs here
    sen1=input('First Sentence: ')
    sen2=input('Second Sentence: ')

    #lower the sentences and remove the spaces
    sen1=sen1.lower()
    sen2=sen2.lower()
    sen1=sen1.replace(" ","")
    sen2=sen2.replace(" ","")

    letter1=list(sen1)
    letter2=list(sen2)

    for word in letter1:
        count1[word]+=1
    print(count1)

    for word in letter2:
        count2[word]+=1
    print(count2)
    print('-----------------')

    if count1==count2:
        print('They are anagram')
        

    elif len(count1-count2)!=0:
        
        print('These letters should be deleted from the FIRST sentence as many as it shows on the right side')
        print(count1-count2)
        inputs()
    elif len(count2-count1)!=0:

        print('These letters should be deleted from the SECOND sentence as many as it shows on the right side')
        print(count2-count1)
        inputs()

inputs()
