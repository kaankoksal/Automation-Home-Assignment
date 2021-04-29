# AUTOMATION HOME ASSIGNMENT

This project scrapes www.imdb.com for all top movies, and returns the cast list for each movie in a csv file.
Then, the cast list is uploaded to Google Drive as Google Spreadsheet, which is then converted into a form. 
Finally, the form link is sent to the recipients in an email. 
Process can be automated by using schtasks for the scraping part and using Apps Script Triggers for the rest of the process.

## INSTALLATION

### Scraping Part

This project uses scrapy to scrape the imdb.com pages and the uses pandas dataframes to get the most frequent cast members. 
Therefore these libraries must be pre-installedbefore starting the process.

It is recommended to use a virtual environment with this project. 
If you do not have virtualenv installed already, it can be installed using pip as the other packages.

```
pip install virtualenv
```

After virtualenv is installed, use the below commands to create and activate the virtual environment.

```
virtualenv venv
```

To activate (given that you are in the project directory);

```
. ./venv/Scripts/activate
```

```
pip install scrapy
pip install pandas
```
Finally, Google client library must be installed
```
  pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
```
### Apps Script Part

This project uses Drive API. Therefore another requirement is to create a project in Google Cloud Platform 
on console.cloud.google.com and enabling the Drive API. Afterthe Drive API is enabled, 
you must obtain oAuth client ID for a **DESKTOP APPLICATION** and download the 
Client Secret file using the described steps on the page and save it in the project directory as **client_secret.json**.
The app will not work unless these steps are completed.

Finally, create an Apps Script project with the code written in **FormEmailScript.json**. 
This script will be used to generate the form based on the scraping results and send the form link to the recipients via email.

## USAGE

Considering that all the dependencies are installed and requirements are satisfied, 
run main.py in the project directory from the command line in order to manually scrape imdb.com , 
save results in a csv file and then upload it to Drive as Google Spreadhsheet

```
python main.py
```
To generate the form from the top 5  most frequent cast members, create a new Apps Script project using the code that can be found in **FormEmailScript.js** and run the automateForm function
```
function automateForm()
```

## AUTOMATION

schtasks can be utilized to automate the scraping. In order to scrape, get top 5 members and upload to drive on a weekly basis, on each Monday at 08:00 AM, insert the following command in Command Prompt
```
schtasks /create /tn ScrapeAutomation /tr c:\Users\...\automation-ha\main.py sc/ weekly /d MON /st 08:00
```

To automate the form generation and email sending, go into Triggers, and add a trigger with the below parametes:

function = automateForm,
deployment = Head,
event source = Time-Driven,
type = Week timer,
day = Monday,
time = 9am to 10 am,
