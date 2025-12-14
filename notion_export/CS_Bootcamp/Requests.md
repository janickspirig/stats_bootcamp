---
title: "Requests"
notion_id: "b431f30b-a067-4f04-a6c8-36035b69ea8e"
notion_url: "https://www.notion.so/Requests-b431f30ba0674f04a6c836035b69ea8e"
exported_at: "2025-12-13T22:57:44.077038+00:00"
---

# Requests

# Motivation
---
[Requests](https://requests.readthedocs.io/en/latest/) is a Python library that allows us to interact with other computer systems directly from inside our program code by sending [API requests](/d9dea9bec31b42b6aa208d00223b3fb5). 
This is great as it allows us to interact with the application layer only, without worrying about establishing a TCP connection or with the IP address of the target system is. The [Requests library](https://requests.readthedocs.io/en/latest/) is taking care of that. 
So whenever we want to send data to an external system or retrieve data from an external system over the Internet, we can use the functions from the Requests library.
---
# Functions
## [`.get()`](https://requests.readthedocs.io/en/latest/api/#requests.get)
---
**Syntax**
This method allows us to send a [HTTP GET request](/f6bdc16ceadd474d895561e3c6762d42#6b64ef335eb947678b9953ba8499f02d) to a server. Thus, we can use it whenever we want to retrieve data from another system.
`requests.get(<< url >>, params = << params >>, headers = << headers >>)`
**Input**
`<< url >>` : required
- String → the remote location from which we want to retrieve data
`<< params >>` : optional
- Dictionary → any parameters we want to send with our request
`<< headers >>` : optional
- Dictionary → any header fields we want to attach to our request
**Output**
[Response object](https://requests.readthedocs.io/en/latest/api/#requests.Response) → contains all data that was received from the remote server
---
**Send a request**
Let’s assume we want to retrieve all train and tram stations in Zurich form the [Swiss public Transport API](https://transport.opendata.ch/docs.html).
```python
import requests

url = 'http://transport.opendata.ch/v1/locations?query=Zuerich'

requests.get(url) 
<Response [200]> # return value
```
We can see that when we know the URL from where we want to retrieve the data, with the requests library it becomes very easy. We simply provide the URL as first parameter and get a response object back. 
---
Please note, that in this case the parameter `query=Zurich` was attached directly to the URL / inserted into the string. Systems that implement the HTTP protocol know that after the question mark `?` the parameters are submitted. 
If we are too lazy to write the entire URL, we can simply wrap all parameters into a dictionary and provide this dictionary as value for [`<< params >>`](/b431f30ba0674f04a6c836035b69ea8e#24b093f568384ee5859d5ea699e81d7c).
```python
import requests

params = {'query' : 'Zurich'}

url = 'http://transport.opendata.ch/v1/locations'

requests.get(url, params=params)
<Response [200]>
```
We can see know that we created a dictionary in which we included the request parameter `query`. Then, we simply submit this dictionary as value for [`<< params >>`](/b431f30ba0674f04a6c836035b69ea8e#24b093f568384ee5859d5ea699e81d7c). The request library takes care of attaching the part `?query=Zuerich` at the end of the URL.
---
## [`.json()`](https://requests.readthedocs.io/en/latest/api/#requests.Response.json)
---
**Syntax**
This method allows us to convert the content inside a [Response object](/b431f30ba0674f04a6c836035b69ea8e#7ed7ea04e56c45849631e30eb5f094b1), i.e., the data we got from the external system, to a regular Python dictionary. 
`<< response object >>.json()`
**Input**
None
**Output**
[Dictionary](/5b0832dbf9454eb1941b7632e68a9abb#a7ac954b45b441c6ba2cc4fbc81d26ad) containing the response payload.
---
**Convert a response payload to a dictionary**
Let’s assume we want to investigate the stations we received from our [Get request](/b431f30ba0674f04a6c836035b69ea8e#c1a960294f1f47708768304853d0f11e).
```python
import requests

params = {'query' : 'Zurich'}

url = 'http://transport.opendata.ch/v1/locations'

response = requests.get(url, params=params)

all_stations = response.json()

all_stations['stations'][0]

{
	'id': '8503000',
	'name': 'Zürich HB',
	'score': None,
	'coordinate':
		{
			'type': 'WGS84',
			'x': 47.377847,
			'y': 8.540502
		},
	'distance': None,
	'icon': 'train'
}
```
We can see that we simply call the `.json()` method on the Response object and we get all stations in Zurich that are registered and save them in `all_stations`.
We then [access](/5b0832dbf9454eb1941b7632e68a9abb#76a0afe2fbbe4d12a464eca65464f5d2) the first station in this [nested dictionary](/5b0832dbf9454eb1941b7632e68a9abb#ff1d8a7cca0c41ec88b2a7904913da20) and we get Zurich HB.
---
# General procedure
---
> 🔗 **[Jupyter Notebook with code](https://colab.research.google.com/drive/1vfwp9XOgP5-PIIYXEAolcJ0P_kYOesh9?usp=sharing)**
---
Let’s assume we want to query the distance in kilometer between Dufuorstrasse 1, St. Gallen and Bahnhofstrasse 10, Zurich by using the [Google Distance Matrix API](https://developers.google.com/maps/documentation/distance-matrix/overview).
## 1️⃣ Create request parameters
---
First, we need to create a dictionary containing all the request parameters that we have to send to the API. From the [API documentation](https://www.google.com/search?client=safari&rls=en&q=google%20distance%20matrix%20api&ie=UTF-8&oe=UTF-8) we can see that we need to provide the parameters `origins`, `destinations` and `key`.
As the API requires authorization (Google wants to make money with this service), we need to create an API Key and submit this key as value for the `key` parameter.
It is also very common to include the [API key in the request header](/b431f30ba0674f04a6c836035b69ea8e#07a54a475ce04ef2871e87ca53efed93). This depends on the practices of the remote system / API.
Thus, we need to create a new dictionary that contains three key-value pairs: `'origins'`, `'destinations'`, and `'key'`.
```python
params = {}

params['origins'] = '1+Dufourstrasse+St.Gallen'
params['destinations'] = '10+Bahnhofstrasse+Zuerich'
params['key'] = 'AIzaSyARhuiYTojo_HYBOYjREpU22I58cZFNDAk'
```
---
## 2️⃣ Create request headers
---
Similarly to request parameters, we can attach header fields to our HTTP request. One of the most common HTTP header fields is `Authorization`. If the remote system requires authentication (I don’t want others to be able to see my bank account), we often need to provide a value for the `Authorization` field.
There are multiple ways how authorization can be done and usually the API documentation of the remote system tells you what authorization method it supports. 
One of the most common one is the usage of an [API Key](https://en.wikipedia.org/wiki/API_key) which is a unique string containing a lot of characters. As the key only exists once, the remote system knows exactly who is querying data and can eventually charge something for this service.
If the API Key must be included as value for the `Authorization` field, we create another dictionary in which we include this header field as key-value pair.
```python
API_key = 'KEyvfzRKTEUosq8Nxnw0ZkCaae6IjUKkCb5vkOPe36VlWI'

headers = {}

headers['Authorization'] = 'Bearer ' + API_key
```
However, in our scenario the [Google Distance Matrix API](https://developers.google.com/maps/documentation/distance-matrix/overview) asks us to send the API key as a regular request parameter.
---
## 2️⃣ Send request
---
Now, after having created the `params` dictionary (and the headers dictionary if necessary), we can send our request. As we are retrieving data from the remote system, we send a [GET request](/f6bdc16ceadd474d895561e3c6762d42#6b64ef335eb947678b9953ba8499f02d).
```python
url = 'https://maps.googleapis.com/maps/api/distancematrix/json'

response = requests.get(url, params=params)
```
If the API key would have to be included in the header the request would look like this.
```python
url = 'https://maps.googleapis.com/maps/api/distancematrix/json'

response = requests.get(url, params=params, headers = headers)
```
---
## 3️⃣ Check response code
---
Before we can process further we must check if everything worked well. We can do so by checking the [HTTP Response Code](/f6bdc16ceadd474d895561e3c6762d42#6b75a24ce46f488882b239a07f12d879) that is stored in the `.response_code` attribute of the Response object. 
```python
response.response_code
200
```
We can see that the response code is 200 which means OK. Thus, our request was sent, processed and the response received successfully.
---
## 4️⃣ Extract data from response
---
As we are confident that everything worked well, we can now extract the distance value in kilometers from the response object. To do so, we must convert the Response content to a Dictionary by using the [`.json()`](/b431f30ba0674f04a6c836035b69ea8e#de76c444320d47eeb90a332fa6a6e1ae) method. 
```python
response_data = response.json() 

response_data {
	'destination_addresses': [
			'Bahnhofstrasse 10, 8001 Zürich, Switzerland'
		],
	 'origin_addresses':[
			'Dufourstrasse 1, 9008 St. Gallen, Switzerland'
		],
	 'rows': [
			{
				'elements': [
						{
								'distance': {
									'text': '86.8 km',
									'value': 86810
							},
								'duration': {
									'text': '1 hour 4 mins',
									'value': 3820
							},
						    'status': 'OK'
						}
				]
			}
		],
 'status': 'OK'
}
```
We can see that the response data structure is quite complex. The value we are interested in is 86.8 km. So we need to extract this value by navigating through this [nested dictionary](/5b0832dbf9454eb1941b7632e68a9abb#ff1d8a7cca0c41ec88b2a7904913da20). 
We see that the first nested dictionary is stored under the key `rows`. And that this dictionary contains a list (we can see that by the square brackets `[]`) with one element. Thus, as a first step we access this element in the list:
```python
response_data['rows'][0]

{
	'elements': [
		{
			'distance': {
				'text': '86.8 km',
				'value': 86810
			},
		   'duration': {
					'text': '1 hour 4 mins',
					'value': 3820
			},
		   'status': 'OK'
			}
	]
}
```
Now as a next step we need to access the value at `elements` which again is a list with one element, another dictionary. 
```python
response_data['rows'][0]['elements'][0]

{
	'distance': {
		'text': '86.8 km',
		'value': 86810
	},
	'duration': {
		'text': '1 hour 4 mins',
		'value': 3820
	},
	'status': 'OK'
}
```
Now as a last step we can access the dictionary stored under the `distance` key and within that dictionary under the `text` key we finally have the distance in kilometers.
```python
response_data['rows'][0]['elements'][0]['distance']['text']
'86.8 km'
```
---

