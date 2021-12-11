import subprocess
import csv
class finalpreoutput:

    def __init__(self, name):
        self.name = name
        return

    def finalpreoutputprocess(self,filteredGenelist22,filteredPoslist22,filtereddepthlist2up2,filteredAGlist12,filteredReflist22,filteredAltlist22
        ,filteredAAlist212,filteredAAlist222,filteredAAPoslist122,filteredcodondepthlist22,filteredDP4list12,filteredAFlist12,filteredmutationlist12,
        filteredQDlist12,filteredSORlist12,filteredMQlist12,filteredMQRankSumlist12,filteredfilterscorelist12,filteredDescriptionlist12,filteredcandidateslist12,
        filteredreportablelist12,newlists1,AAdic):

        process = subprocess.Popen(
                ["samtools", "depth", "-a", self.name + "_SR.bam"], stdout=subprocess.PIPE
            )
        stdout, stderr = process.communicate()
        reader = csv.reader(
            stdout.decode("ascii").splitlines(), delimiter="\t", skipinitialspace=True
        )
        depthlist1 = []

        depthdic={}
        for row in reader:
            #print(row)
            if row[2] != "0":
                # print(row)
                depthlist1 += [row]
                depthdic[row[0],row[1]]=row[2]
                #print(row[1])
                #print(row[2])


        tempgene1=""
        tempgenepos1=""


        filteredGenelist23=filteredGenelist22
        filteredPoslist23=filteredPoslist22
        filtereddepthlist2up3=filtereddepthlist2up2
        filteredAGlist13=filteredAGlist12
        filteredReflist23=filteredReflist22
        filteredAltlist23=filteredAltlist22
        filteredAAlist213=filteredAAlist212
        filteredAAlist223=filteredAAlist222
        filteredAAPoslist123=filteredAAPoslist122
        filteredcodondepthlist23=filteredcodondepthlist22
        filteredDP4list13=filteredDP4list12
        filteredAFlist13=filteredAFlist12
        filteredmutationlist13=filteredmutationlist12
        filteredQDlist13=filteredQDlist12
        filteredSORlist13=filteredSORlist12
        filteredMQlist13=filteredMQlist12
        filteredMQRankSumlist13=filteredMQRankSumlist12
        filteredfilterscorelist13=filteredfilterscorelist12
        filteredDescriptionlist13=filteredDescriptionlist12
        filteredcandidateslist13=filteredcandidateslist12
        filteredreportablelist13=filteredreportablelist12

        #print(len(filteredDP4list12))
        #print(len(filteredAFlist12))


        for x in range(len(newlists1)):
            #print(x)
            if x%8==0:
                filteredGenelist23+=[newlists1[x]]
                tempgene1=newlists1[x]
            if x%8==1:
                filteredPoslist23+=[newlists1[x]]
                tempgenepos1=newlists1[x]
            if x%8==1:    
                filtereddepthlist2up3+=[depthdic[tempgene1,str(tempgenepos1)]]
            if x%8==1:
                filteredAGlist13+=["Freebayes"]
            if x%8==2:
                filteredReflist23+=[newlists1[x]]
            if x%8==3:
                filteredAltlist23+=[newlists1[x]]
            if x%8==5:
                filteredAAlist213+=[AAdic[newlists1[x]]]
            if x%8==6:
                filteredAAlist223+=[AAdic[newlists1[x]]]
            if x%8==4:
                filteredAAPoslist123+=[newlists1[x]]
            if x%8==1:
                filteredcodondepthlist23+=[int(depthdic[tempgene1,str(tempgenepos1-1)]+depthdic[tempgene1,str(tempgenepos1)]+depthdic[tempgene1,str(tempgenepos1+1)])/3]
            if x%8==1:
                filteredDP4list13+=["NA"]
            if x%8==7:
                #print([newlists1[x]])
                filteredAFlist13+=[newlists1[x]]
            if x%8==1:
                filteredmutationlist13+=["NA"]
            if x%8==1:    
                filteredQDlist13+=["NA"]
            if x%8==1:
                filteredSORlist13+=["NA"]
            if x%8==1:
                filteredMQlist13+=["NA"]
            if x%8==1:
                filteredMQRankSumlist13+=["NA"]
            if x%8==1:
                filteredfilterscorelist13+=["NA"]
            if x%8==1:
                filteredDescriptionlist13+=["NA,NA,NA,NA"]
            if x%8==1:
                filteredcandidateslist13+=["NA"]
            if x%8==1:
                filteredreportablelist13+=["NA"]
        return filteredGenelist23,filteredPoslist23,filtereddepthlist2up3,filteredAGlist13,filteredReflist23,filteredAltlist23,filteredAAlist213,filteredAAlist223,filteredAAPoslist123,filteredcodondepthlist23,filteredDP4list13,filteredAFlist13,filteredmutationlist13,filteredQDlist13,filteredSORlist13,filteredMQlist13,filteredMQRankSumlist13,filteredfilterscorelist13,filteredDescriptionlist13,filteredcandidateslist13,filteredreportablelist13