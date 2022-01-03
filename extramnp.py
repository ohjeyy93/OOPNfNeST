class extramnp:

    def __init__(self, filtered_path, unfiltered_path):
        self.filtered_path = filtered_path
        self.unfiltered_path = unfiltered_path
        return

    def extramnpprocess(self, bedname1, dicttrans2, testdic, dictrange):
        f3 = open(self.filtered_path, "r")
        #count=0
        totallist1=[]
        proteinlist1=[]
        tempaflist1=[]
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
            tempAF=""
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
                    #print(word)
                if count==7 and tempbases!="" and tempstate1=="activated":
                    count1=0
                    #print(word)
                    for item in word.split(","):
                        #print(item)
                        #print(float(item)>0)
                        if count1==0 and float(item)>0:
                            POS1=0
                            tempAF=item
                        if count1==1 and float(item)>0:
                            POS1=1
                            tempAF=item
                        count1+=1    
                    #print(tempmnp1.split(",")[POS1])
                #print(word)
                #if word.startswith(".p"):
                    #print(word)
                if word.startswith("p.") and tempbases!="" and tempstate1=="activated":
                    #print(word)
                    protein1=word
                count += 1
            #print(POS1)
            if POS1!="":
                #print(tempword,tempbases1,tempmnp1.split(",")[POS1],protein1)
                for x in range(len(tempbases1)):
                    #print(POS1)
                    #print(tempbase1)
                    #print(tempmnp1.split(",")[POS1])
                    #print(tempmnp1.split(",")[POS1][x])
                    #print(x)
                    #print(len(tempmnp1.split(",")[POS1][73]))
                    if x<len(tempmnp1.split(",")[POS1]):
                        if tempbases1[x]!=tempmnp1.split(",")[POS1][x]:
                            #print(list1)
                            list1+=[tempword,int(tempbase1)+x,tempbases1[x],tempmnp1.split(",")[POS1][x]]
            if list1!=[]:
                if list1 not in totallist1:
                    #print(protein1)
                    #print(list1)
                    totallist1+=[list1]
                    #print(proteinlist1)
                    #print([protein1])
                    proteinlist1+=[protein1]
                    tempaflist1+=[tempAF]
        #print(proteinlist1)
        #print(tempaflist1)
        #print(totallist1)
        #print(proteinlist1)
        truelist1=[]
        trueproteinlist1=[]
        truetempaflist1=[]
        count=0
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
                    #print(line)
                    if item[0] == line.split()[0] and item[1] == int(line.split()[1]):
                        #print(item)
                        truelist1+=item
                        #print(proteinlist1[count])
                        #print([proteinlist1[count]])
                        trueproteinlist1+=[proteinlist1[count]]
                        #print(tempaflist1[count])
                        truetempaflist1=[tempaflist1[count]]
            count+=1
        #print(truelist1)
        #print(truetempaflist1)
        #print(trueproteinlist1)
        truelist2=[]
        for x in range(0,len(truelist1),2):
            #print(x)
            truelist2+=[[truelist1[x],truelist1[x+1]]]

        truelist3=[]
        for x in range(0,len(truelist2),2):
            truelist3+=[truelist2[x]]

        #print(type(truelist3[0][0]),type(truelist3[0][1]))
        #print(truelist3)
        #print(truelist2)
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
        basechangedic={}
        for x in range(0,len(truelist2),2):
            #print(truelist2[x])
            #print(truelist2[x+1])print(', '.join(a))
            basechangedic[str(truelist2[x]).strip("[").strip("]")]=str(truelist2[x+1]).strip("[").strip("]")
        #for item in basechangedic:
        #    print(BASEAAPOSdicMNP[item])
        basechangedic2={}
        for item in basechangedic:
            basechangedic2[item.split(",")[0].strip("\"\'").strip("\'"),int(item.split(",")[1])]=basechangedic[item].strip("\"\'").strip("\'")
            #print(item.split(",")[0])
            #print(item.split(",")[1])
        #print(basechangedic2)
        #print(BASEAAPOSdicMNP)
        #for item in trueproteinlist1:
        #print(basechangedic2)
        newpos1=""
        prodict1={}
        testcount=0
        testcount2=0
        newpro1=""
        #print(trueproteinlist1)
        #print(trueproteinlist1)
        for word in trueproteinlist1:
            #print(word)
            newpos1=""
            for character in word:
                if character.isdigit():
                    newpos1+=character
            #print(newpos1)
            #print(word[2::].replace(newpos1,""))
            for character in word[2::].replace(newpos1,""):
                testcount+=1
                newpro1+=character
                if (testcount)%3==0 and testcount>0:
                    #print(newpro1)
                    testcount2+=1
                    if testcount>0:
                        prodict1[newpro1]=int(newpos1)+testcount2-1
                    if len(word[2::].replace(newpos1,""))/3/2==testcount2:
                        testcount2=0
                    newpro1=""
                #testcount+=1
        #print(prodict1)
        #print(finallist1)
        finallist1=[]
        #print(prodict1)
        #print(truetempaflist1)
        #print(prodict1)
        #print(BASEAAPOSdicMNP)
        for item in BASEAAPOSdicMNP:
            #print(item)
            #print(basechangedic2[item[0],int(item[1])].split(",")[0].strip("\'").strip())
            #print(basechangedic2[item[0],int(item[1])].split(",")[1].strip().strip("\'"))
            #print(BASEAAPOSdicMNP[item[0],int(item[1])])
            finallist1+=[item[0]]
            finallist1+=[item[1]]
            finallist1+=[basechangedic2[item[0],int(item[1])].split(",")[0].strip("\'").strip()]
            finallist1+=[basechangedic2[item[0],int(item[1])].split(",")[1].strip().strip("\'")]
            finallist1+=[BASEAAPOSdicMNP[item[0],int(item[1])]]
            #print(item2)
            for item2 in prodict1:
                #print(prodict1[item2])
                #print(BASEAAPOSdicMNP[item[0],int(item[1])])
                #print(BASEAAPOSdicMNP[item[0],int(item[1])])
                #print(prodict1[item2])
                if prodict1[item2]==BASEAAPOSdicMNP[item[0],int(item[1])]:
                    finallist1+=[item2]
            finallist1+=truetempaflist1
        print(finallist1)
        return finallist1
