import time
import os
import glob

folder = '/Volumes/SSD_NVMe_256GB/emerson-2017-natgen/'

files = glob.glob(folder + "*.tsv")

for fname in files:

	filepath = fname

	outpath = 'parsed/' + fname.split("/")[-1]

	start = time.time()

	i=0
	f=open(filepath,'r')

	out_f= open(outpath,"w+")


	CMV_status = "unknown"

	for line in f.readlines():
		i+=1
		#print(i)
		l = line.split("\t")

		out_f.write(l[1]+ "," +l[10]+ "," +l[16] + "\n")
		#print(l[1],l[30],l[36])
		if i == 2:
			pos = "CMV +"
			neg = "CMV -"
			if pos in line:
				print("CMV positive")
				CMV_status = "positive"
			elif neg in line:
				print("CMV negative")
				CMV_status = "negative"
			else:
				print("problem")
	    #	break

	newname = outpath.split('.')[0] + "_" + CMV_status + ".csv"

	os.rename(outpath, newname)

	out_f.close()
	end = time.time()

	print("elapsed", end - start)