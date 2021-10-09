import json
import csv

column_identification = ['dateRep', 'cases', 'deaths', 'countriesAndTerritories']

with open('covid_cases.json') as covid_file:
    covid_data = json.loads(covid_file.read())

with open('parsed_covid', 'w') as file_parsed:

    data_file = csv.writer(file_parsed)

    data_file.writerow(column_identification)

    for info in covid_data["records"]:
        data_file.writerow([
            info["dateRep"],info["cases"],
            info["deaths"],info["countriesAndTerritories"]
        ])