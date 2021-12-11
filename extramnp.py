class extramnp:

    def __init__(self, filtered_path, unfiltered_path):
        self.filtered_path = filtered_path
        self.unfiltered_path = unfiltered_path
        return

    def extramnpprocess(self, bedname1, dicttrans2, testdic, dictrange):
        f3 = open(self.filtered_path, "r")
        #count=0
        totallist1=[]
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
            list1=[]
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
                if count==32 and tempbases!="" and tempstate1=="activated":
                    protein1=word
                count += 1
            if POS1!="":
                #print(tempword,tempbases1,tempmnp1.split(",")[POS1],protein1)
                for x in range(len(tempbases1)):
                    if tempbases1[x]!=tempmnp1.split(",")[POS1][x]:
                        list1+=[tempword,int(tempbase1)+x,tempbases1[x],tempmnp1.split(",")[POS1][x]]
            if list1!=[]:
                if list1 not in totallist1:
                    print(protein1)
                    print(list1)
                    totallist1+=[list1]
        truelist1=[]
        for item in totallist1:
            #print(item)
            f2 = open(self.unfiltered_path, "r")
            for line in f2:
                if len(line.split())>1:
                   #print(line)
                    #print(item[0])
                    #print(line.split()[0])
                    #print(item[1])
                    #print(line.split()[1])
                    if item[0] == line.split()[0] and item[1] == int(line.split()[1]):
                        truelist1=item
        truelist2=[]
        for x in range(0,len(truelist1),2):
            #print(x)
            truelist2+=[[truelist1[x],truelist1[x+1]]]

        truelist3=[]
        for x in range(0,len(truelist2),2):
            truelist3+=[truelist2[x]]

        #print(type(truelist3[0][0]),type(truelist3[0][1]))
        #print(truelist3)
        BASEAAPOSdicMNP = {}
        for x in range(len(bedname1)):
            tempfa2 = ""
            temptestfa2 = ""
            tempAAPOS = ""
            count = 0
            AAcount = 0
            for y in range(len(dictrange[bedname1[x]][0])):
                # print(dictrange[bedname1[x][0]])
                if len(dictrange[bedname1[x]][0]) == 1:
                    for z in range(
                        dictrange[bedname1[x]][0][y] - 1, dictrange[bedname1[x]][1][y] - 1
                    ):
                        # print(z)
                        if count % 3 == 1:
                            AAcount += 1
                        count += 1
                        #print(type(bedname1[x]),type(z))
                        #print(bedname1[x], str(z))
                        if [bedname1[x], z] in truelist3:
                            #print("True")
                            BASEAAPOSdicMNP[bedname1[x], z] = AAcount

                if len(dictrange[bedname1[x]][0]) > 1:
                    for z in range(
                        dictrange[bedname1[x]][0][y] - 1, dictrange[bedname1[x]][1][y]
                    ):
                        # print(z)
                        if count % 3 == 1:
                            # print(count)
                            AAcount += 1
                        count += 1
                        #print(bedname1[x], str(z))
                        if [bedname1[x], z] in truelist3:
                            #print("True")
                            BASEAAPOSdicMNP[bedname1[x], z] = AAcount
        print(truelist2)
        print(BASEAAPOSdicMNP)
        print(protein1)