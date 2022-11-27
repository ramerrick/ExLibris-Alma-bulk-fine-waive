#!/usr/bin/env python
# coding: utf-8
#Author Rachel Merrick. 
#This script was created for the purpose of waiving fines in bulk with more control than provided by the bulk fine waiving
#option in Alma. The list of fines are created using Alma analytics and filtered by date and amount there.
#The report will then be exported as a csv which will be read by the script as a dataframe.
#The columns of the dataframe are then added to arrays/lists. Each list/array is iterated over by a loop to create the link
#to post to the Alma API. The response from the APIs are then saved into a text file in XML.
#Error messages are added to the dataframe as a new column called 'Notes'. The updated dataframe is than saved as a new csv.
#Originally written and executed with Anaconda/Jupyter:
#Some libraries may need to be installed before running the script in other environments.

#Import datetime module.
from datetime import datetime
#Assign variable for start time, used to time how long script takes.
start_time = datetime.now()

#Import required libraries/modules.
import requests as req #Used to to access Alma API.
import pandas as pd #Used to import csv as dataframe. May need to be installed if used oustide of Anaconda/Jupyter
import re #Allows use of regular expresions which have been used to extract error messages.

#Set variables.
key = '' #Alma production API key- enter your key between ''
error = '<errorsExist>true</errorsExist>' #Test to indicate when an error is pressent.
error_message = '<errorMessage>(.+)</errorMessage>' #Extracting the error message from API response.

#Import csv file. Can also use pd.read_excel to use .xlsx files.
df = pd.read_csv('fines.csv')

#Extracting reuired columns (Columns which contain variable operators in the API link) from the dataset.
#Placing the contents into arrays/lists which are defined as variables.
#UserId, Fine ID and amount  are variables in this script. Operation (waive), Reason (other) 
#and comment (RM_testing_bulk_waive_API) are static and have been defined in the url for all fines waived by this script.
users_list = df.iloc[:,0].values
fineID_list = df.iloc[:,1].values
amount_list = df.iloc[:,2].values

#Loop iterating over the number of rows in the User ID column. all columns should have the same number of rows.
for i in range(len(users_list)):
    #Setting the variable for the usersID, FineID and amount to be used in buidling the url.
    #All variables are converted to string so that the URL can be concatenated.
    user = str(users_list[i])
    fineID = str(fineID_list[i])
    amount = str(amount_list[i])
    #Building URL with variables above and API key.
    url = 'https://api-ap.hosted.exlibrisgroup.com/almaws/v1/users/' + user  + '/fees/' + fineID +'?user_id_type=all_unique&op=waive&amount=' +amount+ '&reason=OTHER&comment=API_bulk_waive&apikey=' +key
    #Post URL to Alma. reponse will be contained in the variable.
    response = req.post(url)
    
    
    #Selection statement if there is an error add error message to notes column of data frame, else No errors detected.
    if error in response.text:
        note = re.search(error_message, response.text)
        df.at[i, 'Notes'] = note.group(1)
        
    else:
        note = 'No errors detected'
        df.at[i, 'Notes'] = note
        
#Print message of how many records were processed and to wait for csv to be written to.
print(str(i + 1) + " records processed, please wait for responses to be saved to csv...")

#Write file to csv
df.to_csv('responses.csv')

#print file save completeion messages.
print("File saved, please check responses.csv for error messages.")
#set variable for end time
end_time = datetime.now()
#Display time taken (end time - star time)
print('Time taken: {}'.format(end_time - start_time))


#add if falls down
#df.to_csv('responses.csv')







