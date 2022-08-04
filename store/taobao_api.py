import requests
url = "https://taobao-api.p.rapidapi.com/api"

querystring = {"api":"item_search","page_size":"40","q":"shoes"}

headers = {
	"X-RapidAPI-Key": "49a092b920msh71f18a68832b06fp18adfajsn2589793aedea",
	"X-RapidAPI-Host": "taobao-api.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response)