import csv
import requests
import random
import datetime

# Specify the path to your CSV file
csv_file = 'numbers.csv'

try:
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        
        for row in reader:
            if row:  # Check if the row is not empty
                if len(row) >= 2:  # Ensure there are at least two values in the row
                    name, department, number, amount = row[0], row[1], row[2], row[3]

                    apiUrl = f'https://capitalfield.primeairtime.com/api/topup/exec/{number}'

                    headers = {
                        'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiI2NDhiMDJmZGVmZmFjMzkxNjlkZTYwMDkiLCJpcCI6IjExYjg1YzUyMDM3Y2MxNDBjMTY2MGJmMzBhMTg2NjMzIiwiZXhwIjoxNjk5NzIwNjA0ODgyfQ.BGLcyVzwQdh2QXnw6Dxn6LJKfHBYMk5VlPXv8-u2uS0'
        
                    }
                    ref = random.randint(1000, 9999)
                    

                    data = {
                        'product_id': 'MFIN-5-OR',
                        'denomination': f'{amount}',
                        'send_sms': False,
                        'sms_text': '',
                        'customer_reference': f'myref202311{ref}'
                        }
                    
                    response = requests.post(apiUrl, json=data, headers=headers)
                    if response.status_code == 200 or 201: 
                        feedback = 'successful'
                        

                        with open("feedback.csv", "a") as file:

                            file.write(f"\n {name},{number},{amount},{department},{datetime.datetime.now()},credited successfully")

                    else:
                        print(response.status_code)

                else:
                    print(f"Row does not have two columns: {row}")
except FileNotFoundError:
    print(f"File '{csv_file}' not found.")
except Exception as e:
    print(f"An error occurred: {e}")
