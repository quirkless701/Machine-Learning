import pandas as pd
from io import StringIO
import numpy as np
import re
from datetime import datetime


#Pandas Dataframe Exercises
#    • Make a Pandas DataFrame with two-dimensional list | Python
temp = pd.DataFrame({'Temperature' : ['10 C' , '20 C' , '30C'] ,
             'Wind' : ['no wind' , ' little wind' , 'fast wind'] ,
              } , index=['morning' , 'evening' , 'Night' ])

print(temp)
#    • Python | Creating DataFrame from dict of narray/lists
data = {'Temperature' : ['10 C' , '20 C' , '30C'] ,
             'Wind' : ['no wind' , ' little wind' , 'fast wind'] }
 
df = pd.DataFrame(data)
print(df )
#    • Creating Pandas dataframe using list of lists

Age = [['Rishabh', 10], ['On', 15], ['Deez', 20]]
df = pd.DataFrame(Age, columns = ['Name', 'Age'])
print(df )
#    • Creating a Pandas dataframe using list of tuples
data = [('Brad', 18, 37),
        ('Tiffany', 15, 56),
        ('Kelly', 17, 48),
        ('Veronica', 18, 57),
        ('Chirs', 17, 35) ]
df = pd.DataFrame(data, columns =['Name', 'Age', 'Weight'])
print(df)
#    • Create a Pandas DataFrame from List of Dicts
data = [{'Bruh': 'dataframe', 'bruh': 'using', 'bRuh': 'list'},
        {'Bruh':10, 'bruh': 20, 'bRuh': 30}]
 
df = pd.DataFrame.from_records(data,index=['1', '2'])
print(df)
#    • Python | Convert list of nested dictionary into Pandas dataframe
list = [
        {
        "Student": [{"Exam": 90, "Grade": "a"},
                    {"Exam": 99, "Grade": "b"},
                    {"Exam": 97, "Grade": "c"},
                   ],
        "Name": "Rishabh Vyas"
        },
        {
        "Student": [{"Exam": 89, "Grade": "a"},
                    {"Exam": 80, "Grade": "b"}
                   ],
        "Name": "Anil modi"
        }
       ]
  
print(list)
#    • Creating a dataframe from Pandas series
name = ['crow', 'eli', 'nier', 'rem']
score = [223, 41, 414, 578]
series = pd.Series(name)
article_series = pd.Series(score)
frame = { 'name': series, 'score': article_series }
result = pd.DataFrame(frame)
print(result)
#    • Construct a DataFrame in Pandas using string data
StringData = StringIO("""Date;Event;Cost
    10/2/2011;Music;10000
    11/2/2011;Poetry;12000
    12/2/2011;Theatre;5000
    13/2/2011;Comedy;8000
    """)

data = pd.read_csv(StringData, sep =";")

print(df)

#    • Replace values in Pandas dataframe using regex
df = pd.DataFrame({'City':['New York', 'Parague', 'New Delhi', 'Venice', 'new Orleans'],
                    'Event':['Music', 'Poetry', 'Theatre', 'Comedy', 'Tech_Summit'],
                    'Cost':[10000, 5000, 15000, 2000, 12000]})

index_ = [pd.Period('02-2018'), pd.Period('04-2018'),
          pd.Period('06-2018'), pd.Period('10-2018'), pd.Period('12-2018')]
df.index = index_
  
print(df)
df_updated = df.replace(to_replace ='[nN]ew', value = 'New_', regex = True)
  
print(df_updated)
#    • Reindexing in Pandas DataFrame
column = ['a', 'b', 'c', 'd', 'e']
index = ['A', 'B', 'C', 'D', 'E']
  
df1 = pd.DataFrame(np.random.rand(5, 5),
        columns = column, index = index)
 
new_index =['U', 'A', 'B', 'C', 'Z']
 
print(df1.reindex(new_index))
#    • Mapping external values to dataframe values in Pandas
initial_data = {'First_name': ['Ram', 'Mohan', 'Tina', 'Jeetu', 'Meera'], 
        'Last_name': ['Kumar', 'Sharma', 'Ali', 'Gandhi', 'Kumari'], 
        'Age': [42, 52, 36, 21, 23], 
        'City': ['Mumbai', 'Noida', 'Pune', 'Delhi', 'Bihar']}
  
df = pd.DataFrame(initial_data, columns = ['First_name', 'Last_name',
                                                      'Age', 'City'])
  
new_data = { "Ram":"B.Com",
             "Mohan":"IAS",
             "Tina":"LLB",
             "Jeetu":"B.Tech",
             "Meera":"MBBS" }
  
df["Qualification"] = df["First_name"].map(new_data)
  
print(df)
#    • Python | Change column names and row indexes in Pandas DataFrame
df=pd.DataFrame({"Name":['Tom','Nick','John','Peter'],
                 "Age":[15,26,17,28]})
  
print(df)
df.columns =['Col_1', 'Col_2']
  
df.index = ['Row_1', 'Row_2', 'Row_3', 'Row_4']
  
print(df)
#Pandas Dataframe Row Exercises
#    • How to iterate over rows in Pandas Dataframe
data = {'Name': ['Ankit', 'Amit',
                 'Aishwarya', 'Priyanka'],
        'Age': [21, 19, 20, 18],
        'Stream': ['Math', 'Commerce',
                   'Arts', 'Biology'],
        'Percentage': [88, 92, 95, 70]}
  
df = pd.DataFrame(data, columns=['Name', 'Age',
                                 'Stream', 
                                 'Percentage'])
  
print("Given Dataframe :\n", df)
  
print("\nIterating over rows using loc function :\n")
  
for i in range(len(df)):
    print(df.loc[i, "Name"], df.loc[i, "Age"])
#    • Different ways to iterate over rows in Pandas Dataframe
#    • Selecting rows in pandas DataFrame based on conditions
record = {
  'Name': ['Ankit', 'Amit', 'Aishwarya', 'Priyanka', 'Priya', 'Shaurya' ],
  'Age': [21, 19, 20, 18, 17, 21],
  'Stream': ['Math', 'Commerce', 'Science', 'Math', 'Math', 'Science'],
  'Percentage': [88, 92, 95, 70, 65, 78]}
  
dataframe = pd.DataFrame(record, columns = ['Name', 'Age', 'Stream', 'Percentage'])
  
print("Given Dataframe :\n", dataframe) 
  
options = ['Math', 'Science']
rslt_df = dataframe.loc[(dataframe['Age'] == 21) &
              dataframe['Stream'].isin(options)]
  
print('\nResult dataframe :\n', rslt_df)
#    • Select any row from a Dataframe using iloc[] and iat[] in Pandas
df = pd.DataFrame({'Date':['10/2/2011', '11/2/2011', '12/2/2011', '13/2/11'],
                    'Event':['Music', 'Poetry', 'Theatre', 'Comedy'],
                    'Cost':[10000, 5000, 15000, 2000]})
   
Row_list =[]
   
for i in range((df.shape[0])):
    cur_row =[]
    for j in range(df.shape[1]):
           
        cur_row.append(df.iat[i, j])
           
    Row_list.append(cur_row)
print(Row_list[:3])
#    • Limited rows selection with given column in Pandas | Python
data = {'Name':['Jai', 'Princi', 'Gaurav', 'Anuj'], 
        'Age':[27, 24, 22, 32], 
        'Address':['Delhi', 'Kanpur', 'Allahabad', 'Kannauj'], 
        'Qualification':['Msc', 'MA', 'MCA', 'Phd']} 
    
df = pd.DataFrame(data) 
    
print(df.loc[1:3, ['Name', 'Qualification']])
#    • Drop rows from the dataframe based on certain condition applied on a column

#    • Insert row at given position in Pandas Dataframe
df = pd.DataFrame({'Date':['10/2/2011', '12/2/2011', '13/2/2011', '14/2/2011'],
                    'Event':['Music', 'Poetry', 'Theatre', 'Comedy'],
                    'Cost':[10000, 5000, 15000, 2000]})
 
# Let's visualize the dataframe
print(df)
def Insert_row(row_number, df, row_value):
    # Starting value of upper half
    start_upper = 0
  
    # End value of upper half
    end_upper = row_number
  
    # Start value of lower half
    start_lower = row_number
  
    # End value of lower half
    end_lower = df.shape[0]
  
    # Create a list of upper_half index
    upper_half = [*range(start_upper, end_upper, 1)]
  
    # Create a list of lower_half index
    lower_half = [*range(start_lower, end_lower, 1)]
  
    # Increment the value of lower half by 1
    lower_half = [x.__add__(1) for x in lower_half]
  
    # Combine the two lists
    index_ = upper_half + lower_half
  
    # Update the index of the dataframe
    df.index = index_
  
    # Insert a row at the end
    df.loc[row_number] = row_value
   
    # Sort the index labels
    df = df.sort_index()
  
    # return the dataframe
    return df
  
# Let's create a row which we want to insert
row_number = 2
row_value = ['11/2/2011', 'Wrestling', 12000]
 
if row_number > df.index.max()+1:
    print("Invalid row_number")
else:
     
    # Let's call the function and insert the row
    # at the second position
    df = Insert_row(row_number, df, row_value)
  
    # Print the updated dataframe
    print(df)
#    • Create a list from rows in Pandas dataframe
df = pd.DataFrame({'Date':['10/2/2011', '11/2/2011', '12/2/2011', '13/2/11'],
                    'Event':['Music', 'Poetry', 'Theatre', 'Comedy'],
                    'Cost':[10000, 5000, 15000, 2000]})
Row_list =[]
for index, rows in df.iterrows():
    my_list =[rows.Date, rows.Event, rows.Cost]
    Row_list.append(my_list)

print(Row_list)  
print(df)
#    • Ranking Rows of Pandas DataFrame
movies = {'Name': ['The Godfather', 'Bird Box', 'Fight Club'],
         'Year': ['1972', '2018', '1999'],
         'Rating': ['9.2', '6.8', '8.8']}
  
df = pd.DataFrame(movies)
print(df)
df['Rating_Rank'] = df['Rating'].rank(ascending = 1)
  
df = df.set_index('Rating_Rank')
print(df)
#    • Sorting rows in pandas DataFrame
data = {'name': ['Simon', 'Marsh', 'Gaurav', 'Alex', 'Selena'], 
        'Maths': [8, 5, 6, 9, 7], 
        'Science': [7, 9, 5, 4, 7],
        'English': [7, 4, 7, 6, 8]}
  
df = pd.DataFrame(data)
  
a = df.sort_values(by ='Science', ascending = 0)
print("Sorting rows by Science:\n \n", a)
#    • Select row with maximum and minimum value in Pandas dataframe
dict1 = {'Driver': ['Hamilton', 'Vettel', 'Raikkonen',
                    'Verstappen', 'Bottas', 'Ricciardo',
                    'Hulkenberg', 'Perez', 'Magnussen',
                    'Sainz', 'Alonso', 'Ocon', 'Leclerc',
                    'Grosjean', 'Gasly', 'Vandoorne',
                    'Ericsson', 'Stroll', 'Hartley', 'Sirotkin'],
 
         'Points': [408, 320, 251, 249, 247, 170, 69, 62, 56,
                    53, 50, 49, 39, 37, 29, 12, 9, 6, 4, 1],
 
         'Age': [33, 31, 39, 21, 29, 29, 31, 28, 26, 24, 37,
                 22, 21, 32, 22, 26, 28, 20, 29, 23]}
 
df = pd.DataFrame(dict1)
print(df.head(10))
#    • Get all rows in a Pandas DataFrame containing given substring
df = pd.DataFrame({'Name': ['Eem', 'Peter', 'James', 'Jack', 'Lisa'],
                   'Team': ['Boston', 'Boston', 'Boston', 'Chele', 'Barse'],
                   'Position': ['PG', 'PG', 'UG', 'PG', 'UG'],
                   'Number': [3, 4, 7, 11, 5],
                   'Age': [33, 25, 34, 35, 28],
                   'Height': ['6-2', '6-4', '5-9', '6-1', '5-8'],
                   'Weight': [89, 79, 113, 78, 84],
                   'College': ['MIT', 'MIT', 'MIT', 'Stanford', 'Stanford'],
                   'Salary': [99999, 99994, 89999, 78889, 87779]},
                   index =['ind1', 'ind2', 'ind3', 'ind4', 'ind5'])
print(df, "\n")
  
print("Check PG values in Position column:\n")
df1 = df['Position'].str.contains("PG")
print(df1)

#    • How to randomly select rows from Pandas DataFrame
data = {'Name':['Jai', 'Princi', 'Gaurav', 'Anuj', 'Geeku'],
        'Age':[27, 24, 22, 32, 15],
        'Address':['Delhi', 'Kanpur', 'Allahabad', 'Kannauj', 'Noida'],
        'Qualification':['Msc', 'MA', 'MCA', 'Phd', '10th']}
 
df = pd.DataFrame(data)
shit = df.sample()
print(shit)
#Pandas Daraftame Columns Exercises
#    • Create a pandas column using for loop

#    • How to rename columns in Pandas DataFrame
rankings = {'test': ['India', 'South Africa', 'England',
                            'New Zealand', 'Australia'],
            'odi': ['England', 'India', 'New Zealand',
                            'South Africa', 'Pakistan'],
            't20': ['Pakistan', 'India', 'Australia',
                            'England', 'New Zealand']}
  
rankings_pd = pd.DataFrame(rankings)
  
print(rankings_pd)
  
rankings_pd.rename(columns = {'test':'TEST'}, inplace = True)
  
# After renaming the columns
print("\nAfter modifying first column:\n", rankings_pd.columns)
#    • Get unique values from a column in Pandas DataFrame
data = {
    'A':['A1', 'A2', 'A3', 'A4', 'A5'], 
    'B':['B1', 'B2', 'B3', 'B4', 'B4'], 
    'C':['C1', 'C2', 'C3', 'C3', 'C3'], 
    'D':['D1', 'D2', 'D2', 'D2', 'D2'], 
    'E':['E1', 'E1', 'E1', 'E1', 'E1'] }
  
df = pd.DataFrame(data)
  
sed = df.B.unique()
print(sed)
#    • Conditional operation on Pandas DataFrame columns
df = pd.DataFrame({'Date':['10/2/2011', '11/2/2011', '12/2/2011', '13/2/2011'],
                   'Product':['Umbrella', 'Mattress', 'Badminton', 'Shuttle'],
                   'Last Price':[1200, 1500, 1600, 352],
                   'Updated Price':[1250, 1450, 1550, 400],
                   'Discount':[10, 10, 10, 10]})
 
print(df)
if 'Updated Price' in df.columns:
    df['Final cost'] = df['Updated Price'] - (df['Updated Price']*0.1)
 
else :
    df['Final cost'] = df['Last Price'] - (df['Last Price']*0.1)
 
print(df)
#    • Return the Index label if some condition is satisfied over a column in Pandas Dataframe

#    • Formatting integer column of Dataframe in Pandas
data = {'Month' : ['January', 'February', 'March', 'April'],
     'Expense': [ 21525220.653, 31125840.875, 23135428.768, 56245263.942]}
  
dataframe = pd.DataFrame(data, columns = ['Month', 'Expense'])
  
print("Given Dataframe :\n", dataframe)
  
pd.options.display.float_format = '{:.2f}'.format
  
print('\nResult :\n', dataframe)
#    • Create a new column in Pandas DataFrame based on the existing columns
df = pd.DataFrame({'Date':['10/2/2011', '11/2/2011', '12/2/2011', '13/2/2011'],
                    'Event':['Music', 'Poetry', 'Theatre', 'Comedy'],
                    'Cost':[10000, 5000, 15000, 2000]})
 
print(df)
df['Discounted_Price'] = df.apply(lambda row: row.Cost -
                                  (row.Cost * 0.1), axis = 1)
 
print(df)
df['Discounted_Price'] = df.apply(lambda row: row.Cost -
                                  (row.Cost * 0.1), axis = 1)
 
print(df)
#    • Python | Creating a Pandas dataframe column based on a given condition
df = pd.DataFrame({'Date' : ['11/8/2011', '11/9/2011', '11/10/2011',
                                        '11/11/2011', '11/12/2011'],
                'Event' : ['Music', 'Poetry', 'Music', 'Comedy', 'Poetry']})
 
print(df)
df['Price'] = [1500 if x =='Music' else 800 for x in df['Event']]
 
print(df)
#   • Split a String into columns using regex in pandas DataFrame
movie_data = ["Name: The_Godfather Year: 1972 Rating: 9.2",
            "Name: Bird_Box Year: 2018 Rating: 6.8",
            "Name: Fight_Club Year: 1999 Rating: 8.8"]
  
movies = {"Name":[], "Year":[], "Rating":[]}
  
for item in movie_data:
      
    name_field = re.search("Name: .*",item)
      
    if name_field is not None:
        name = re.search('\w*\s\w*',name_field.group())
    else:
        name = None
    movies["Name"].append(name.group())
      
    year_field = re.search("Year: .*",item)
    if year_field is not None:
        year = re.search('\s\d\d\d\d',year_field.group())
    else:
        year = None
    movies["Year"].append(year.group().strip())
      
    rating_field = re.search("Rating: .*",item)
    if rating_field is not None: 
        rating = re.search('\s\d.\d',rating_field.group())
    else: 
        rating - None
    movies["Rating"].append(rating.group().strip())
  
df = pd.DataFrame(movies)
print(df)
#   • Getting frequency counts of a columns in Pandas DataFrame
df = pd.DataFrame({'A': ['foo', 'bar', 'g2g', 'g2g', 'g2g',
                         'bar', 'bar', 'foo', 'bar'],
                  'B': ['a', 'b', 'a', 'b', 'b', 'b', 'a', 'a', 'b'] })
  
count = df['A'].value_counts()
print(count)
#   • Split a text column into two columns in Pandas DataFrame
df = pd.DataFrame({'Name': ['John Larter', 'Robert Junior', 'Jonny Depp'],
                   'Age':[32, 34, 36]})
   
print("Given Dataframe is :\n",df)
   
print("\nSplitting 'Name' column into two different columns :\n",
                                  df.Name.str.split(expand=True))

#   • Difference of two columns in Pandas dataframe
df1 = { 'Name':['George','Andrea','micheal',
                'maggie','Ravi','Xien','Jalpa'],
        'score1':[62,47,55,74,32,77,86],
        'score2':[45,78,44,89,66,49,72]}
  
df1 = pd.DataFrame(df1,columns= ['Name','score1','score2'])
  
print("Given Dataframe :\n", df1)
  
# getting Difference
df1['Score_diff'] = df1['score1'] - df1['score2']
print("\nDifference of score1 and score2 :\n", df1)
#   • How to drop one or multiple columns in Pandas Dataframe
data = {
    'A': ['A1', 'A2', 'A3', 'A4', 'A5'],
    'B': ['B1', 'B2', 'B3', 'B4', 'B5'],
    'C': ['C1', 'C2', 'C3', 'C4', 'C5'],
    'D': ['D1', 'D2', 'D3', 'D4', 'D5'],
    'E': ['E1', 'E2', 'E3', 'E4', 'E5']}
  
# Convert the dictionary into DataFrame
df = pd.DataFrame(data)
  
print(df)
#   • How to lowercase column names in Pandas dataframe
df = pd.DataFrame({'A': ['John', 'bODAY', 'MinA', 'Peter', 'nicky'],
                  'B': ['masters', 'graduate', 'graduate',
                                   'Masters', 'Graduate'],
                  'C': [27, 23, 21, 23, 24]})
   
print(df)
df = pd.DataFrame({'A': ['John', 'bODAY', 'MinA', 'Peter', 'nicky'],
                  'B': ['masters', 'graduate', 'graduate', 
                                   'Masters', 'Graduate'],
                  'C': [27, 23, 21, 23, 24]})
   
df['A'] = df['A'].str.lower()
  
print(df)
#   • Capitalize first letter of a column in Pandas dataframe
df = pd.DataFrame({'A': ['john', 'bODAY', 'minA', 'Peter', 'nicky'],
                  'B': ['masters', 'graduate', 'graduate',
                                   'Masters', 'Graduate'],
                  'C': [27, 23, 21, 23, 24]})
   
print(df)
df = pd.DataFrame({'A': ['john', 'bODAY', 'minA', 'Peter', 'nicky'],
                  'B': ['masters', 'graduate', 'graduate',
                                   'Masters', 'Graduate'],
                  'C': [27, 23, 21, 23, 24]})
   
df['A'] = df['A'].str.capitalize()
  
print(df)
#Pandas Datetime Exercises
#    • Pandas | Basic of Time Series Manipulation
range_date = pd.date_range(start ='1/1/2019', end ='1/08/2019',
                                                   freq ='Min')
print(range_date)
#   • Using Timedelta and Period to create DateTime based indexes in Pandas
ts = pd.Timestamp('02-06-2018')
  
print(ts)
df = pd.DataFrame({'City':['Lisbon', 'Parague', 'Macao', 'Venice'],
                    'Event':['Music', 'Poetry', 'Theatre', 'Comedy'],
                    'Cost':[10000, 5000, 15000, 2000]})
  
  
index_ = [pd.Timestamp('01-06-2018'), pd.Timestamp('04-06-2018'),
          pd.Timestamp('07-06-2018'), pd.Timestamp('10-06-2018')]
  
df.index = index_
  
print(df)
#    • Convert the column type from string to datetime format in Pandas dataframe
df = pd.DataFrame({'Date':['11/8/2011', '04/23/2008', '10/2/2019'],
                'Event':['Music', 'Poetry', 'Theatre'],
                'Cost':[10000, 5000, 15000]})
 
print(df)
 
df.info()
df['Date']= pd.to_datetime(df['Date'])
 
df.info()
df = pd.DataFrame({'Date':['11/8/2011', '04/23/2008', '10/2/2019'],
                'Event':['Music', 'Poetry', 'Theatre'],
                'Cost':[10000, 5000, 15000]})
 
print(df)
 
df.info()
    