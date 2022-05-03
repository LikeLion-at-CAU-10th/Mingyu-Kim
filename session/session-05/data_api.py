import requests

def get_data(gu):
    
    url = 'http://openapi.seoul.go.kr:8088/6b4e4976576361643931486f494354/json/GetParkInfo/1/1000/'
    res = requests.get(url)
    res_json = res.json()
    data_row = res_json["GetParkInfo"]["row"]
    new_data = []

    for item in data_row:
        place = item["ADDR"]
        if gu in place:
            new_data.append(item)    

    return new_data

    
print(get_data("동작")[0])