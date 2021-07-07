import requests

api_key = "https://api.covid19api.com/summary"
json_data = requests.get(api_key).json()
total_cases = str(json_data['Global']['TotalConfirmed'])
total_deaths = str(json_data['Global']['TotalDeaths'])
countries = json_data['Countries']

print("Total Cases: " + total_cases + "\nTotal Deaths: " + total_deaths)

def shorten(s, subs):
    i = s.index(subs)
    return s[:i]

country = input("\nType a country's name to see its stats: ")

for i in countries:
  if i["Slug"] == country.lower():
    print("The total confirmed cases in %s is %s" % (country, i['TotalConfirmed']))
    print("The total deaths in %s is %s" % (country, i['TotalDeaths']))
    print("Date updated: %s" % shorten(i['Date'], 'T'))
