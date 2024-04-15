import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response = requests.get(self.url)
        return response.content

    def load_json(self):
        list_of_data = []
        #request is a list/array of JSON or objects/dictionaries
        list_of_requested_data= json.loads(self.get_response_body())

        for data in list_of_requested_data:
            list_of_data.append(data)

        return list_of_data
