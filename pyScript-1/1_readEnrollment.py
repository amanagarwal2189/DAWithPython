import unicodecsv

enrollments = []

f=open('D:\Github\DAWithPython\pyScript\data\enrollments.csv','rb')
reader = unicodecsv.DictReader(f)

for r in reader:
    enrollments.append(r)

f.close()
print(enrollments[0])
    