import pandas as pd
grades_df = pd.DataFrame(
    data={'exam1': [43, 81, 78, 75, 89, 70, 91, 65, 98, 87],
          'exam2': [24, 63, 56, 56, 67, 51, 79, 46, 72, 60]},
    index=['Andre', 'Barry', 'Chris', 'Dan', 'Emilio', 
           'Fred', 'Greta', 'Humbert', 'Ivan', 'James']
)

def convert_grades(grades):
    if grades>90 and grades<100:
        grades = 'A'
    elif grades>80 and grades<89:
        grades = 'B'
    elif grades>70 and grades<79:
        grades = 'C'
    elif grades>60 and grades<69:
        grades = 'D'
    else:
        grades = 'F'
    return grades

#print(grades_df>80)
print(grades_df.applymap(convert_grades))