import gather_keys_oauth2 as oauth2
import fitbit
import pandas as pd
import datetime

#Autho.py runs first
CLIENT_ID = "23B6T9"
CLIENT_SECRET='3fa9103ea574714a4926cf28a3be79c9'

server=Oauth2.OAuth2Server(CLIENT_ID, CLIENT_SECRET)
server.browser_authorize()
ACCESS_TOKEN=str(server.fitbit.client.session.token['access_token'])
REFRESH_TOKEN=str(server.fitbit.client.session.token['refresh_token'])
auth2_client=fitbit.Fitbit(CLIENT_ID,CLINT_SECRET,oauth2=True,access_token=ACCESS_TOKEN,refresh_token=REFRESH_TOKEN)

