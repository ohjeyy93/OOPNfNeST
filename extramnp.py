class extramnp:

    def __init__(self, filtered_path):
        self.filtered_path = filtered_path
        return

    def extramnpprocess(self):
        f3 = open(self.filtered_path, "r")
        #count=0
        for line in f3:
            count=0
            tempword=""
            tempbase1=""
            tempbase2=""
            tempbases=""
            tempbases1=""
            tempstate1=""
            tempmnp1=""
            POS1=""
            protein1=""
            for word in line.split():
                if count==0:
                    if word=="PfCRT":
                        tempword=word
                        #print(word)
                if count==1 and tempword=="PfCRT":
                    if len(word)>5:
                        tempbases=word
                        tempbase1=word[0:3]
                        tempbase2=word[3:6]
                if count==2 and tempbases!="":
                    tempbases1=word
                    #print(len(tempbases1))
                    #print(int(tempbase2))
                    #print()
                    #print(int(tempbase2)-int(tempbase2))
                    if len(tempbases1)-1==int(tempbase2)-int(tempbase1):
                        tempstate1="activated"
                if count==3 and tempbases!="" and tempstate1=="activated":
                    tempmnp1=(word)
                if count==7 and tempbases!="" and tempstate1=="activated":
                    count1=0
                    for item in word.split(","):
                        #print(item)
                        #print(float(item)>0)
                        if count1==0 and float(item)>0:
                            POS1=0
                        if count1==1 and float(item)>0:
                            POS1=1
                        count1+=1    
                    #print(tempmnp1.split(",")[POS1])
                if count==31 and tempbases!="" and tempstate1=="activated":
                    protein1=word
                count += 1
            if POS1!="":
                print(tempword,tempbases1,tempmnp1.split(",")[POS1],protein1)
                for x in range(len(tempword)):
                    if tempword[x]!=tempbase1[x]
                        print(tempword[x],tempbase1[x],)