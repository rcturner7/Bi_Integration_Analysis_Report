# Bi_Integration_Analysis_Report

# Repository Summary
This repository shows steps in Automation, BI, implementation, and engineering in analyzing data using 3rd party resources in creating reports and charts from data. 

# The Process of Analysis Creation
In this repository there are 2 scripts. 
 - UploadDataToMondoDB.py
   - Python script for automation
   - Uses Zendesk api for pulling the data of Customer Support tickets (I commented out this part in the script to provide the layout if Zendesk were to be used in real world, and just uploaded a fake customer support ticket csv file)
   - Uploads report to Mongodb Atlas
   - (The next process would be to use a resource like StitchData to connect the information from Mongodb to Google BigQuery)
   - (Due to this repository for testing and learning I skipped the part from connecting Mongodb to google bigquery using stictchdata and uploaded the data from csv to my google bigquery on the platform without using a script)
 - bigQuery.py
   - Python script for testing using bigQuery api to view data in python output
   - (Instead of writing within the script to send the data from BigQuery to the BI platform I used, which was Google Data Studio, I uploaded the report directly on the platform instead of using a python script)
  
# Customer Support Ticket report from Google Data Studio BI platform Results
<img width="911" alt="Report" src="https://github.com/rcturner7/Bi_Integration_Analysis_Report/assets/98337469/6f2b1128-03ec-4718-81d6-e6ab5479022d">






<img width="884" alt="Charts" src="https://github.com/rcturner7/Bi_Integration_Analysis_Report/assets/98337469/0a711ef7-ef03-416a-96b1-0d924254ba5e">



# Purpose of Repository
 - Learning and enhancing knowledge for myself or anyone wanting to grow their knowledge in real-world Data Analysis, and building the Software for implementation
 - Showing the process of Data from one platform Like Zendesk into a csv file
 - Scripting/Automation in uploading to a database like MongoDB
 - Connecting the database with BigQuery and using pipelines like StitchData
 - Connecting a BI platform to BigQuery to run reports and different types of Charts for a customer report team to get a better understanding of their customer support service, and may help to improve on handling support tickets
