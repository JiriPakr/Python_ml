
# ChatGPT genered code

import requests
import json

# Set the match ID that you want to retrieve information about
def getMatchID(match_id):

    # Make a GET request to the OpenDota API to retrieve match data
    response = requests.get(f"https://api.opendota.com/api/matches/{match_id}")

    # Parse the JSON response
    match_data = json.loads(response.text)
    return match_data
    # Print the match data
    #print(match_data)

def getPublicMatches():
    response = requests.get(f"https://api.opendota.com/api/publicMatches")
    match_data = json.loads(response.text)
    return match_data