import unicodecsv
enrollment_filename= 'D:\Github\DAWithPython\pyScript\data\enrollments.csv'
with open(enrollment_filename,'rb') as f:
    reader = unicodecsv.DictReader(f)
    enrollments=list(reader)
    print(enrollments[0])
    