# ExLibris-Alma-bulk-fine-waive

<b>Brief Description:</b> The script waives individual fines, on a list produced from alma analytics.

<b>Long description/background:</b></br>
This script was created for the purpose of waiving fines in bulk with more control than provided by the bulk fine waiving option in Alma. The list of fines was created using Alma analytics and filtered by date and amount there. The report will then be exported as a csv which will be read by the script as a dataframe. The columns of the dataframe are then added to arrays/lists. Each list/array is iterated over by a loop to create the link to post to the Alma API.  Error messages are added to the dataframe as a new column called 'Notes'. The updated dataframe is than saved as a new csv.

<b>Language:</b> Python, script available as both python and python notebook file.</br>
<b>API:</b> Alma, users, read/write.</br>
Originally written and executed with Anaconda/Jupyter.</br>

<b>Modules/Libraries used:</b>
<ul>
	<li>Requests (for API communication).</li>
	<li>Pandas (using data frames).</li>
	<li>Re (regular expressions).</li>
	<li>Datetime (current day/time, used to time).</li>
</ul>

<b>Includes:</b>
<ul>
	<li>Timing the script from start to finish.</li>
	<li>Importing csv as data frame.</li>
	<li>Converting data frame columns into arrays, stored as variables.</li>
	<li>Iterating over the arrays above using a for loop, values contained in the arrays used to build individual links for each fine to be sent to the API.</li>
	<li>POST links to API (update fines- waive them) and write response to variable.</li>
	<li>Selection statement, look for error notifier with regular expressions: If there is error: Look for error message in response using regular expressions and contain the message, add it to variable. If there is no error add success message to variable.</li>
	<li>Add either success or error message (contained in variable) to the notes column of the data frame.</li>
	<li>Write new data frame with updated notes column with error and success messages to csv.</li>
	<li>Display records processed.</li>
 </ul>
	
	
<b>Resources Used:</b></br>
Waiving fines with API dev network https://developers.exlibrisgroup.com/alma/apis/docs/users/UE9TVCAvYWxtYXdzL3YxL3VzZXJzL3t1c2VyX2lkfS9mZWVzL3tmZWVfaWR9/</br>
API console https://developers.exlibrisgroup.com/console/</br>
POST method https://www.w3schools.com/python/ref_requests_post.asp</br>
Pandas cheat sheet: http://datacamp-community-prod.s3.amazonaws.com/f04456d7-8e61-482f-9cc9-da6f7f25fc9b</br>
Regular Expressions Python Capture groups: https://stackoverflow.com/questions/48719537/capture-groups-with-regular-expression-python</br>
Find substring in string http://net-informations.com/python/basics/contains.htm#:~:text=Using%20Python's%20%22in%22%20operator,%2C%20otherwise%2C%20it%20returns%20false%20.</br>
Update Dataframes https://www.askpython.com/python-modules/pandas/update-the-value-of-a-row-dataframe?fbclid=IwAR3o7WAnpPYk6q7PmyMcpmpW8F9F4EVzV3GR-KoUAdmGPOUaIkELYoZOAhA</br>
