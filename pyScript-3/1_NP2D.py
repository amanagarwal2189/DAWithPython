import unicodecsv
enrollment_filename= 'D:\Github\DAWithPython\pyScript\data\enrollments.csv'
def readCsv(filename):
    with open(filename,'rb') as f:
        reader = unicodecsv.DictReader(f)
        return list(reader)
enrollments=readCsv(enrollment_filename)
