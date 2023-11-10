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

                    apiUrl = f'https://capitalfield.primeairtime.com/api/topup/info/{int(number)}'

                    headers = {
                        'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiI2NDhiMDJmZGVmZmFjMzkxNjlkZTYwMDkiLCJpcCI6IjcxY2Y1NjUyMzczODAzYjNhN2M5OTQzOGRmYjlhNDZmIiwiZXhwIjoxNjk5Nzc2NTk5MDc0fQ.iMkH2s2dDouqPrTozqLF3MDBIb3x0PPNzSL7KVfZnlw'
        
                    }
                    response = requests.get(apiUrl, headers=headers)
                    if response.status_code == 200 or 201:
                        response = response.json()
                        network = response['opts']['operator']
                        with open("network_feedback.csv", "a") as file:

                            file.write(f"\n {name},{number},{amount},{department},{network}")

                    else:
                        print(response.status_code)

                else:
                    print(f"Row does not have two columns: {row}")
except FileNotFoundError:
    print(f"File '{csv_file}' not found.")
except Exception as e:
    print(f"An error occurred: {e}")

