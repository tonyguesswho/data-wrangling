import requests
import csv
import datetime


class OpenDataApi:
    BASE_URL = "http://api.eia.gov/series/"
    API_KEY = "fde4249dee64ae4932a3ed8d52fb5126"

    def __init__(self, series_id):
        self.params = {"series_id":series_id, "api_key":self.API_KEY}
        self.data = None

    @property
    def get(self):
        try:
            response = requests.get(self.BASE_URL, params=self.params).json()
            self.data = response["series"][0]["data"]
        except Exception as e:
            raise Exception(e)

    def format(self, type):
        final_data = []
        for data in self.data:
            if type == "monthly":
                details =[datetime.datetime.strptime(data[0],"%Y%m").strftime('%d-%b-%Y') ,data[1]]
            elif type == "daily":
                 details =[datetime.datetime.strptime(data[0],"%Y%m%d").strftime('%d-%b-%Y') ,data[1]]
            final_data.append(details)
        self.data= final_data

        
    def get_prices_in_csv(self, type):
        self.get
        self.format(type)
        with open(f'data/{type}_prices.csv','w') as f:
            writer = csv.writer(f)
            writer.writerow(['Date', 'Price'])
            writer.writerows(self.data)




def main():
    OpenDataApi("NG.RNGWHHD.D").get_prices_in_csv("daily")
    OpenDataApi("NG.RNGWHHD.M").get_prices_in_csv("monthly")  

if __name__ ==  '__main__':
  main()