import pandas as pd

data ='students.csv'
percentage = []
def view():
    
    df = pd.read_csv(data)
    marks = df[['Economics','Maths','BST','Accounts']].sum(axis=1)
    for i in range(len(marks)):
        per=(marks[i] /400)*100
        percentage.append(per)

    df['Percentage'] = percentage
    print(df.to_string(index=False))   



   
  


def subject_wise():
    df = pd.read_csv(data)
    avg_accts = (df['Accounts'].mean()).__round__(2)
    avg_math = df['Maths'].mean()
    avg_eco = df['Economics'].mean()
    avg_bst = df['BST'].mean()
    print('SUBJECT WISE AVERAGE MARKS')
    print('-'*60)
    print(f'''
Maths       : {avg_math}
Accounts    : {avg_accts}
Economics   : {avg_eco}
Business    : {avg_bst}''')


def topper():
    df = pd.read_csv(data)

    df['Percentage'] = (
        df[['Economics','Maths','BST','Accounts']].sum(axis=1) / 400
    ) * 100
    top3 = df.sort_values(by='Percentage', ascending=False).head(3)
    print('TOP 3 PERFORMERS')
    print('-'*60)
    print(top3[['Name','Percentage']].to_string(index=False))

   
def pass_percentage():
    df = pd.read_csv(data)
    df['Percentage'] = (
        df[['Economics','Maths','BST','Accounts']].sum(axis=1) / 400
    ) * 100
    for i in range(len(df['Name'])):
        if df.iloc[i]['Percentage']<30:
            less = df.iloc[i]
            print(less[['Name','Percentage']].to_string())
            print('-'*40)
                
        
def export():
    df = pd.read_csv(data)
    df['Percentage'] = (
        df[['Economics','Maths','BST','Accounts']].sum(axis=1) / 400
    ) * 100
    df.to_csv('output.csv',index=False)







print('='*70)
print('STUDENT PERFORMANCE ANALYZER')
print('='*70)

print('''
1. View All Student Records
2. Subject-wise Average Marks
3. Top 3 Performers
4. Students Below Pass Percentage
5. Export Result Report
6. Exit''')


while True:
    user = input('Enter your choice: ')
    if user == '1' :
        view()
    elif user == '2':
        subject_wise()
    elif user == '3':
        topper()
    elif user == '4':
        pass_percentage()
    elif user == '5':
        export()
    elif user == '6':
         print('Thank you for using Student Performance Analyzer 👋')
         break    
    else:
        print('Invalid')
        continue
    