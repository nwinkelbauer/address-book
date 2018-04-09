# Address Book Application
Searchable contact list application. Built using python.

## CLI Python Script
Included is a python script to run the app functionality inside the command line using the command:
`python lookup-contact-cli.py --search="SEARCH" --file="FILE"`. 
- SEARCH is a string used to filter results
- FILE is a path used to collect contact data from; defualts to `assets/example.txt`.

## Web App
To initialize the web application:
- Open the folder inside the command line
- Run the command `make build` in the command line
- Run the command `make run` in the command line
- Navigate your web browser to `0.0.0.0:5000` 

Use the search input field to live filter the contact list. The clear button will clear all input from the search bar. 