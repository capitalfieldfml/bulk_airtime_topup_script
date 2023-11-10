#!/usr/bin/env python
import cgi
import requests
import random

form = cgi.FieldStorage()

# You can access form data like this:
title = form.getvalue('title')
first_name = form.getvalue('firstName')
middle_name = form.getvalue('middleName')
last_name = form.getvalue('lastName')
gender = form.getvalue('gender')
dob = form.getvalue('dateOfBirth')
address = form.getvalue('address')
nationality = form.getvalue('nationality')
phone_number = form.getvalue('phoneNumber')
email = form.getvalue('email')
stateOfOrigin = form.getvalue('stateOfOrigin')
lga = form.getvalue('lga')
address = form.getvalue('address')
nationality = form.getvalue('nationality')
profilePicture = form.getvalue('profilePicture')
marital_status = form.getvalue('maritalStatus')
bvn = form.getvalue('bvn')



# GENERATE 6 DIGITS RANDOM NUMBER AS OTP
def generate_random_number():
    return str(random.randint(100000, 999999))

# BVN VALIDATION PROCESS

apiUrl = '/identitypass/verification/bvn_validation'

headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer your_access_token',
    'app-id': '',
    'x-api-key': ''
}

# Define the data to send in the request (in this example, sending JSON data)
data = {
    'bvn': f'{bvn}',
    
}

# Send the POST request
response = requests.post(apiUrl, json=data, headers=headers)

# Check the response status code
if response.status_code == 200: 
    bvn_validation_response = response.json()

    if bvn_validation_response.data.last_name == last_name :
        bvn_validation_status = "BVN validated successfully"
        otp = generate_random_number()
        


else:
    print('Error: BVN validation failed', response.status_code)