import unicodecsv
enrollment_filename= 'D:\Github\DAWithPython\pyScript\data\enrollments.csv'
dailyEngagement_filename= 'D:\Github\DAWithPython\pyScript\data\daily_engagement.csv'
projectsubmissions_filename= 'D:\Github\DAWithPython\pyScript\data\project_submissions.csv'
with open(enrollment_filename,'rb') as f:
    reader = unicodecsv.DictReader(f)
    enrollments=list(reader)
    print(enrollments[0])

with open(dailyEngagement_filename,'rb') as f:
    reader = unicodecsv.DictReader(f)
    dailyEngagement=list(reader)
    print(dailyEngagement[0])

with open(projectsubmissions_filename,'rb') as f:
    reader = unicodecsv.DictReader(f)
    projectsubmissions=list(reader)
    print(projectsubmissions[0])
    