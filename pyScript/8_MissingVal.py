import unicodecsv
from datetime import datetime as dt

enrollment_filename= 'D:\Github\DAWithPython\pyScript\data\enrollments.csv'
dailyEngagement_filename= 'D:\Github\DAWithPython\pyScript\data\daily_engagement.csv'
projectsubmissions_filename= 'D:\Github\DAWithPython\pyScript\data\project_submissions.csv'

def readCsv(filename):
    with open(filename,'rb') as f:
        reader = unicodecsv.DictReader(f)
        return list(reader)

def parse_int(i):
    if i==None or i=='':
        return None
    else:
        return int(i)

def parse_date(date):
    if date==None or date=='':
        return None
    else:
        return dt.strptime(date, '%Y-%m-%d')

def parse_float(f):
    if f==None or f=='':
        return 0.0
    else:
        return float(f)

def getUniqueSet(di):
    uniqueSet=set()    
    for d in di:
        uniqueSet.add(d['account_key'])
    return uniqueSet

enrollments=readCsv(enrollment_filename)
dailyEngagements=readCsv(dailyEngagement_filename)
projectsubmissions=readCsv(projectsubmissions_filename)

for enrollment in enrollments:
    enrollment['days_to_cancel'] = parse_int(enrollment['days_to_cancel'])
    enrollment['is_canceled'] = enrollment['is_canceled']=='True'
    enrollment['join_date'] = parse_date(enrollment['join_date'])
    enrollment['is_udacity'] = enrollment['is_udacity']=='True'
    enrollment['cancel_date'] = parse_date(enrollment['cancel_date'])

for dailyEngagement in dailyEngagements:
    dailyEngagement['lessons_completed'] = parse_float(dailyEngagement['lessons_completed'])
    dailyEngagement['acct'] = parse_int(dailyEngagement['acct'])
    dailyEngagement['projects_completed'] = parse_float(dailyEngagement['projects_completed'])
    dailyEngagement['total_minutes_visited'] = parse_float(dailyEngagement['total_minutes_visited'])
    dailyEngagement['utc_date'] = parse_date(dailyEngagement['utc_date'])
    dailyEngagement['num_courses_visited'] = int(parse_float(dailyEngagement['num_courses_visited']))
    dailyEngagement['account_key'] = dailyEngagement['acct']
    del[dailyEngagement['acct']]

for projectsubmission in projectsubmissions:
    projectsubmission['completion_date'] = parse_date(projectsubmission['completion_date'])
    projectsubmission['creation_date'] = parse_date(projectsubmission['creation_date'])
    
print("enrollments : "+str(len(enrollments)))
print("dailyEngagements : "+str(len(dailyEngagements)))
print("projectsubmissions: "+str(len(projectsubmissions)))
#get unique data
##to get unique values in the dictionary
unique_enrolled_students = getUniqueSet(enrollments)
unique_daily_engagements = getUniqueSet(dailyEngagements)
unique_project_submissions = getUniqueSet(projectsubmissions)
print("unique_enrolled_students : "+str(len(unique_enrolled_students)))
print("unique_daily_engagements : "+str(len(unique_daily_engagements)))
print("unique_project_submissions: "+str(len(unique_project_submissions)))

#for enroll in unique_enrolled_students:
 #   if enroll not in unique_daily_engagements:
  #      
   #     print(enrollment for enrollment in enrollments if enrollment['account_key'] == enroll)
    #    break
count = 0
for enrollment in enrollments:
    student = enrollment['account_key']
    if (student not in unique_daily_engagements and enrollment['join_date'] != enrollment['cancel_date']):
        count=count + 1
print(count)        
          