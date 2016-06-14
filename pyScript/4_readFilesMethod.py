import unicodecsv
enrollment_filename= 'D:\Github\DAWithPython\pyScript\data\enrollments.csv'
dailyEngagement_filename= 'D:\Github\DAWithPython\pyScript\data\daily_engagement.csv'
projectsubmissions_filename= 'D:\Github\DAWithPython\pyScript\data\project_submissions.csv'

def readCsv(filename):
    with open(filename,'rb') as f:
        reader = unicodecsv.DictReader(f)
        return list(reader)

enrollments=readCsv(enrollment_filename)
print(enrollments[0])
dailyEngagement=readCsv(dailyEngagement_filename)
print(dailyEngagement[0])
projectsubmissions=readCsv(projectsubmissions_filename)
print(projectsubmissions[0])