import csv
fp=open('sample.csv',"w+")
f=csv.writer(fp)
f.writerow(["Name","Place","Age"])
f.writerows([("k","toronto",22),("B","VanCouver",45),("c","yemen",34)])
fp.close()
fg=open("sample.csv","r")
g=csv.reader(fg)
for i in g:
	print(i)