import requests

# Authorization Grant Flow
# Autho.py runs first and then access_json.py runs

access_token = ACCESS_TOKEN
refresh_token = REFRESH_TOKEN

# Gets data from Fitbit API using requests and stores it in response
header = {'Authorization': 'Bearer {}'.format(access_token)}
response = requests.get("https://api.fitbit.com/1/user/-/profile.json", headers=header).json()

# I just printed json, we could store the json into a variable that the app could use later.
print(response['user'])

for k, v in response['user'] .items():
   print(k)
   print(v)
   print("\n")




