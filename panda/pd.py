import pandas as pd
pd

df = pd.read_csv('telco_churn.csv')  #this is how you create a dataframe from csv
tempdict = {'col1': [1,2,3], 'col2': [4,5,6], 'col3': [7,8,9]}  #this is how you create a temporary dictionary
dictdf = pd.DataFrame.from_dict(tempdict)   ##this is how you create a dataframe from a dictionary


#Teaching Read
print(df.head(10)) #df=csv head=first, without a number it give you the first 5 starting from 0
print(dictdf.head()) #dict=dictionary head=first

print(df.tail()) #tail=end without a number it give you the last 5

print(df.columns) #this allows you to see all the collumns we have avalible 
print(df.dtypes) #dtypes allows you to see all the data types, dont forget the 's' at the end 
print(df.describe()) #this help you calculate summary statistics
print(df.describe(include='object')) ##this help you calculate summary statistics of something specific, in this case objects

#REMEMBER THESE ARE CASE SENESTIVE
print(df.State) #how to grab a single collumn, this is case specific  
print(df['International plan']) #how to grab a single collumn with a space in the name, notice ther eis no '.' , but instead "['']"
print(df[['State', 'International plan']])  #to grab 2+ collums alone, you need "[['']]" so similar to the space name, but double bracetts instead of 1
print(df.Churn.unique()) #kind of obvious, this is to grab unique values from your collumn

#FILTERING ROWS
print(df[df['International plan']=='No']['International plan']) #in order to see specifically what you are looking for you need the collumn name, 
#otherwise it will load the results with ALL the collumns. If this is a small database that is fine buy in this case just be specific on VSCode

print(df[(df['International plan'] == 'No') & (df['Churn'] == False)][['International plan', 'Churn']])
#Ok so if you want 2+ specific rows with 1+ conditions
#remember to put both rows at the complete end

print(df[df['International plan']=='No'][['International plan', 'State', 'Churn']])
#this is an example of 2+ rows specific, they're all following the 1 condition in the begining
# but the state and churn have different values in their rows unlike the example above

#this next function will allow you to grab data by row with a number
print(df.iloc[8]) #This pulled all the info from row 9
#(this file started with row 1 being all the titles of the collumn, and panda always starts from 0 so it is 2 numbers off )

print(df.iloc[8, 2]) #this allows you to pull out the specific row and collumn you want

print(df.iloc[22:33])   #this allows you to select a group a row starting from x to y [x:y]

state = df.copy() #copy the collumn you want to set an  index on
state.set_index('State', inplace=True)  #this sets the index for whichever collumn you chose
print(state.head())

print(state.loc['OH'])  #this allows specify which rows you want, in this case it's OH


print(df.isnull().sum())  #this helps us spot the missiing values in our rows(or called null{s})
print(df.dropna(inplace=True)) #this dropped all the rows that were missing values
print(df.isnull().sum())


#Updating
print(df.drop('Area code', axis=1)) #dropped a collumn

df['New Collumn'] = df['Total night minutes'] + df['Total intl minutes'] #this is how you create a new collumn
print(df['New Collumn'])    #proof of the new collumn
df['New Collumn'] = 100    #updating an entire collumn
print(df['New Collumn'])

df.iloc[0,-1] = 10      #this is how you can update a single value
# if you add ':y" it will update just like line 42
print(df['New Collumn'])

df['Churn binary'] = df['Churn'].apply(lambda x: 1 if x==True else 0)   #this is how we work with apply, but i only know how to apply binary code
print(df[['Churn binary', 'Churn']])


#Delet/Output
df.to_csv('output_test_csv')
df.to_json()
df.to_html()


#to delete the wholw thing just del df