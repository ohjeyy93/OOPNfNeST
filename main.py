#1Generate POS/ALT/GENE/REF

#2SAMTOOLS Depth figure out

#3 DepthVal

#4 Genelist2/CurrentPOS2/GENE2/REF2/ALT2

#5 AF/MQ/QD/MQRankSUM/SOR

#6 filter number filter score

#7 dicttrans1

#8 dicttrans2

#9 coverage

#10 filterlists

#11 filteredlists2

#12 

import argparse
import pandas as pd
import subprocess
import csv
import itertools
from GPRA import GPRA
from depthlist import depthlist
from codondepth import codondepthlist



#def main(unfiltered_path,filtered_path,bamfile_path,bedfile_path,candidates_path,voi_path,fasta_path):
def main(arguments):
    #print(arguments)
    #print(arguments)
    #arguements=parse_args(arguements)
    
    #########import arguments#################
    unfiltered_path = arguments.unfiltered_path
    filtered_path = arguments.filtered_path
    #print(filtered_path)
    name = arguments.name
    bamfile_path = arguments.bamfile_path
    bedfile_path = arguments.bedfile_path
    candidates_path = arguments.candidates_path
    voi_path = arguments.voi_path
    fasta_path = arguments.fasta_path
    #########################################

    ######First class (Get Gene, Ref, POS, Alt lists)############
    grpa=GPRA(filtered_path)
    Genelist1,POSlist1,Reflist1,Altlist1=grpa.GPRAPROCESS()
    #print(Genelist1,Reflist1,POSlist1,Altlist1)


    #####Second class (Get depths) ##########################
    depthpro=depthlist(name)
    depthlist1up,depthpair1,depthlist1=depthpro.depthprocess(Genelist1, POSlist1)
    #print(depthlist1up,depthpair1)
    #########################################
    #print(depthlist1up,depthpair1)

    #print(depthlist1)
    #####Third class (Codondepthlist) ############
    codondepth1=codondepthlist()
    #print(codondepth1)
    #print(depthlist1)
    codondepthlist1=codondepth1.codondepprocess(Genelist1, POSlist1, depthpair1, depthlist1)
    #print(codondepthlist1)
    #codondepprocess(Genelist1, POSlist1, depthpair1, depthlist1)

    ######Fourth 



    return(0)

def parse_arguments():
    parser = argparse.ArgumentParser(description="name")
    parser.add_argument(
        "-v1", dest="unfiltered_path", type=str, help="name of unfilterd merged vcf file"
    )
    parser.add_argument(
        "-v2", dest="filtered_path", type=str, help="name of filtered merged vcf file"
    )
    parser.add_argument("-b1", dest="bamfile_path", type=str, help="name of bam file")
    parser.add_argument("-b2", dest="bedfile_path", type=str, help="name of bed file")
    parser.add_argument("-e1", dest="candidates_path", type=str, help="name of candidates")
    parser.add_argument("-e2", dest="voi_path", type=str, help="name of variants of interest")
    parser.add_argument("-f1", dest="fasta_path", type=str, help="name of fasta file")
    parser.add_argument("-o1", dest="name", type=str, help="name of output")
    args = parser.parse_args()
    #print(args)
    return args



if __name__ == '__main__':
    arguments = parse_arguments()
    #main(args.unfiltered_path,args.filtered_path,args.bamfile_path,args.bedfile_path,args.candidates_path,args.voi_path,args.fasta_path)
    #print(arguments)
    main(arguments)