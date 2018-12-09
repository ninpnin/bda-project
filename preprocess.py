import os
import csv
import numpy as np
import pandas as pd
import scipy.stats as stats


all_subj = []
phen_stat = []
all_uniq_tcr =[]

pres_num =[]
pres_stat_post= []

path = 'G:\\bioData\\train\\'
for filename in os.listdir(path):
    with open(path + filename) as tsvfile:

        reader = csv.DictReader(tsvfile, dialect='excel-tab')

        stat_info = 0
        uniq_tcr =set()
        for row in reader:
            uniq_tcr.add(row['amino_acid']+'|'+ row['v_gene']+'|' + row['j_gene'])
            str= row['sample_tags']
            if "CMV -" in str:
                stat_info = 0
            else:
                stat_info = 1

        phen_stat.append(stat_info)
        all_subj.append(uniq_tcr)

        all_uniq_tcr = set().union(all_uniq_tcr, uniq_tcr)


pvalues =[]
tcr_table=dict()
w = csv.writer(open("pvalues.csv", "w"))
for tcr in all_uniq_tcr:
    tcr_status =[]
    pres_num = 0
    pres_pos =0
    pres_neg=0
    absent_pos=0
    absent_neg=0
    cmv_post =[]
    cmv_neg = []
    for i, subj in enumerate(all_subj):
        tc_st =tcr in subj
        ph_st = phen_stat[i]
        if (tcr in subj)==True and phen_stat[i] == 1:
            pres_pos +=1
        elif (tcr in subj)== True and phen_stat[i] == 0:
            pres_neg +=1
        elif (tcr in subj)==False and phen_stat[i] == 1:
            absent_pos +=1
        elif (tcr in subj) == False and phen_stat[i] == 0:
            absent_neg +=1

    cmv_post =[pres_pos,absent_pos]
    cmv_neg =[pres_neg,absent_neg]
    tcr_status =[cmv_post,cmv_neg]

    oddsratio, pvalue = stats.fisher_exact(tcr_status)
    #tcr_table[tcr] = [tcr_status, pvalue]
    w.writerow([tcr, tcr_status, pvalue])

