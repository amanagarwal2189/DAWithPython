import unicodecsv
from datetime import datetime as dt

enrollment_filename= 'D:\Github\DAWithPython\pyScript\data\enrollments.csv'
dailyEngagement_filename= 'D:\Github\DAWithPython\pyScript\data\daily_engagement.csv'
projectsubmissions_filename= 'D:\Github\DAWithPython\pyScript\data\project_submissions.csv'

#read file
def readCsv(filename):
    with open(filename,'rb') as f:
        reader = unicodecsv.DictReader(f)
        return list(reader)

enrollments=readCsv(enrollment_filename)
dailyEngagements=readCsv(dailyEngagement_filename)
projectsubmissions=readCsv(projectsubmissions_filename)

#format data
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

for enrollment in enrollments:
    enrollment['days_to_cancel'] = parse_int(enrollment['days_to_cancel'])
    enrollment['is_canceled'] = enrollment['is_canceled']=='True'
    enrollment['join_date'] = parse_date(enrollment['join_date'])
    enrollment['is_udacity'] = enrollment['is_udacity']=='True'
    enrollment['cancel_date'] = parse_date(enrollment['cancel_date'])

for dailyEngagement in dailyEngagements:
    dailyEngagement['lessons_completed'] = parse_float(dailyEngagement['lessons_completed'])
    dailyEngagement['projects_completed'] = parse_float(dailyEngagement['projects_completed'])
    dailyEngagement['total_minutes_visited'] = parse_float(dailyEngagement['total_minutes_visited'])
    dailyEngagement['utc_date'] = parse_date(dailyEngagement['utc_date'])
    dailyEngagement['num_courses_visited'] = int(parse_float(dailyEngagement['num_courses_visited']))
    dailyEngagement['account_key'] = dailyEngagement['acct']
    dailyEngagement['has_Visited'] = 1 if dailyEngagement['total_minutes_visited']>0 else 0
    del[dailyEngagement['acct']]

for projectsubmission in projectsubmissions:
    projectsubmission['completion_date'] = parse_date(projectsubmission['completion_date'])
    projectsubmission['creation_date'] = parse_date(projectsubmission['creation_date'])
    
#get unique data
##to get unique values in the dictionary
unique_enrolled_students = getUniqueSet(enrollments)
unique_daily_engagements = getUniqueSet(dailyEngagements)
unique_project_submissions = getUniqueSet(projectsubmissions)
        
#to remove ud accounts data from all the lists
ud_Acct=set()
for enrollment in enrollments:
    if enrollment['is_udacity']:
        ud_Acct.add(enrollment['account_key'])

def removeUdAcct(di):
    nonud=[]    
    for d in di:
        if d['account_key'] not in ud_Acct:
           nonud.append(d)
    return nonud

nonud_enroll=removeUdAcct(enrollments)
nonud_engagement=removeUdAcct(dailyEngagements)
nonud_projSubmission=removeUdAcct(projectsubmissions)        

#to get the dictionary of students who havent cancelled or have cancelled atleast 8 days after joining
#approach 1: when first occurance or any occurance is taken into account..
#paid_students=dict()
#for stud in nonud_enroll:
#    if stud['days_to_cancel']==None or stud['days_to_cancel']>7:
#        paid_students[stud['account_key']]=stud['join_date']
#approach 2: only make an entry about the most recent enrollment
paid_students=dict()
for stud in nonud_enroll:
    if not stud['is_canceled'] or stud['days_to_cancel']>7:
        account_key=stud['account_key']
        date = stud['join_date']
        if stud['account_key'] not in paid_students or date>paid_students[account_key]:
            paid_students[account_key]=date

#get paid students
def remove_cancelled_reg(data):
    paid_data=[]
    for d in data:
        if d['account_key'] in paid_students:
            paid_data.append(d)
    return paid_data

def within_one_week(join_date, engagement_date):
    time_delta = engagement_date - join_date
    return time_delta.days < 7 and time_delta.days >=0

paid_enrollments = remove_cancelled_reg(nonud_enroll)
paid_engagement = remove_cancelled_reg(nonud_engagement)
paid_projSubmission = remove_cancelled_reg(nonud_projSubmission)

#this contains the students who have paid for lectures in the first week of joining!
paid_engagement_in_first_week = []
for engagement_record in paid_engagement:
    account_key = engagement_record['account_key']
    join_date = paid_students[account_key]
    engagement_record_date = engagement_record['utc_date']
    if within_one_week(join_date, engagement_record_date):
        paid_engagement_in_first_week.append(engagement_record)

#get unique accountkeys and store each account key's engagement record in list
#the dictionary will be {(account_key1:[engagement1, engagement2....]),...}
from collections import defaultdict
dict_account_engagements = defaultdict(list)
for paid_engagement_rcrd in paid_engagement_in_first_week:
    dict_account_engagements[paid_engagement_rcrd['account_key']].append(paid_engagement_rcrd) 

#dict_acct_min stores the students (accountkey:total mins of video watched)
dict_acct_min = {}
for account_key, engagement_records in dict_account_engagements.items():
    total_min=0
    for record in engagement_records:
        total_min += record['total_minutes_visited']
    dict_acct_min[account_key] = total_min

#list of all the total mins.. Just the values
total_min = list(dict_acct_min.values())
    
import numpy as np
#print(np.mean(total_min))
#print(np.max(total_min))

#find surprising data points. the max in the llist was 10568.1 which is more than the number of minutes in a week
#in a week there are 10080 mins. Hence we will come out with the records/account keys which have minutes more than that

invalid_acc={key:value for key,value in dict_acct_min.items() if value>10080}
#print(invalid_acc)

##########THIS IS NEW HERE###################
def givestats(dictionary, s):
    theList= list(dictionary.values())
    print("the stats for " + s+ " are:")
    print("Mean", np.mean(theList))
    print("Min",np.min(theList))
    print("Max",np.max(theList))
    print("Std Dev",np.std(theList))

def sumGroupData(data, field_name):
    dict_acct_key = {}
    for account_key, engagement_records in data.items():
        total_field=0
        for record in engagement_records:
            total_field += record[field_name]
        dict_acct_key[account_key] = total_field
    return dict_acct_key

givestats(sumGroupData(dict_account_engagements,'lessons_completed'), "Lessons")
##########Also Line 57###################
givestats(sumGroupData(dict_account_engagements,'has_Visited'), "Visits")

##########THIS IS NEW HERE.###################

subway_project_lesson_keys = ['746169184', '3176718735']
pass_subway_project = set()
for submission in paid_projSubmission:
    lesson_key = submission['lesson_key']
    grade = submission['assigned_rating']
    if((lesson_key in subway_project_lesson_keys) and (grade == 'PASSED' or grade == 'DISTINCTION')):
        pass_subway_project.add(submission['account_key'])

passing_engagement = []
non_passing_engagement = []
for engagement_record in paid_engagement_in_first_week:
    if engagement_record['account_key'] in pass_subway_project:
        passing_engagement.append(engagement_record)
    else:
        non_passing_engagement.append(engagement_record)

print(len(passing_engagement))
print(len(non_passing_engagement))