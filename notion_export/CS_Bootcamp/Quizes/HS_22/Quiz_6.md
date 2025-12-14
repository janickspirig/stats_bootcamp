---
title: "Quiz 6"
notion_id: "67bc96d9-82f7-4e2a-8c16-6a61cc10d328"
notion_url: "https://www.notion.so/Quiz-6-67bc96d982f74e2a8c166a61cc10d328"
exported_at: "2025-12-13T23:16:11.808507+00:00"
---

# Quiz 6

## Question 1
Which additional key-value pair must be added to the request params in Line 8 in the given code example if you only want to receive the first 10 connections?
Look at the he documentation and select the correct statement: 
[https://transport.opendata.ch/docs.html](https://transport.opendata.ch/docs.html)
```python
url = 'http://transport.opendata.ch/v1/connections'

params = {}
params['from'] = origin
params['to'] = destination
params['date'] = departure_date
params['time'] = departure_time

r = requests.get(url, params=params)
```
❌ `params['limit'] = 10`
❌ `params['10'] = 'limit'`
❌ `params['page'] = '10'`
❌* The API already considers only the first 10 connections by default. *
❌* There is no possibility to request the first 10 connections. *
❌ `params['page'] = 10`
✅ `params['limit'] = 10`

<details>
<summary>Explanation</summary>

In the API documentation, we see that the number of connections to be displayed in the result can be specified over the `limit` parameter:
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/c6e17cac-20fa-47d5-8e77-41b1b793095d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XZZOTLZF%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T231609Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQDaymlBWwDPaYRw28gG6wyffaq%2FAZbokDyvKvXRahs2mwIhAI%2Fzbr5ApeHN2eNhp8Q%2F6ct9NcCA0qEppVaNlRje3JXUKv8DCCcQABoMNjM3NDIzMTgzODA1Igx%2BPXTtYL4gohtUoHwq3AO8lJUxkVm7usURlAVV9VQC5TJdj6TR51tGGZx%2BwQpBRRQOwyQDlNmjTbJyRbpscVqkmkBK8YWwaxFRVSt65%2FDHNdauKRWaJUbSr6aYOlOJnSNxZcQ%2Fci1Nx%2FB1FkQeGt2%2BF%2F2S4Qvl516XIqb9tRm3kxiJZF0B765%2FIxOeTW%2FXLnivcj6KoaJaJTH63HH1AWaZtKtJY%2BOAMZNQMT7uWlKqVCNkszS%2Fg3ZGJrY83HFNBGR7I0WIOmXp0MJn5r7Z1vsr%2Fgl8pQzPuHhZtkaYRebSedfvViLAfgp4SKjKDGl2LCFjkuXrSz17nq8IMp6iO6ebqD5XiK1i6wgSdWKAnUHpXC5gyJNAr2LvQ6kY%2Fh7PTPdrv2gLztou4Uereq8hAnvPNGUXb75a1JtuqVqZqW7byCTzeiffhjUedd6wSf6m5JdockG6fWmNfq8nNKsXySN3kG03%2FCn8NshzcejtqaedLlVkJ5YdtDCV8M4WtquU%2FXy52ml7AncjvJKaFxLwYmZ28NLi0DOSGf2zKeDWBgT8M%2B16s7U%2BEjRXf60wW2qRaSLmwmmb5kVf5G964JqWiH%2F%2BomIJKKxxDEub7gTObMub%2F8wA6h5O6tNfJuxOsO1hAZHozpxmP3P9%2FbcGcDCwzvfJBjqkAcX6OwigDqjBQhpq5ie72UlEPyN08R%2BHi08Z%2FsrdiVcNf7XQFfKu5FCnPJwwWPt%2FoIJFBi6bzLj9b7ivjtc3MMan2xwaftEUlLrZtMe5Q5iJSSGMg2gIg%2BjimfhCBY6GsoROymkuKhu7bTnTJpQqiG1fpkJmEErJNJbNQh%2BbReBzKOmsryWMUyEFr4eusPqxqAicwvfhLyClcuVtr5EE0FkZJLBP&X-Amz-Signature=5c23672b6b01d954dd91cebf7755a2b3a3f85db0c3a172e1ff9121c0930c7093&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
</details>
---
## Question 2
If you launch two different Web browsers (e.g. Chrome and Firefox) on two different computers and open [https://unisg.ch](https://unisg.ch/) in both at the same time, which of the following applies?
❌ In any case, both browsers will use the same local port to access the remote server.
✅ In any case, both browsers will use the same remote IP to access the remote server.
✅ In any case, both browsers will use the same remote port to access the remote server.
❌ In any case, both browsers will use the same local IP to access the remote server.

<details>
<summary>Explanation</summary>

❌ **Incorrect**. The two browsers are running on different computers. The local port for https connections can be different for the two computers. 
✅ **Correct**. Both browsers are accessing server of the university over the URL [unisg.ch](http://unisg.ch/). Thus, both browsers are pointing to the same remote server, which is assigned exactly one IP address. 
✅ **Correct**. Both browsers are using the https protocol. Thus, the unisg server receives the requests over the same port (usually 443). If one browser would do an http request and the other one https, then the remote ports would differ (http → 8080, https → 443).
❌ **Incorrect**. The two browsers are running on different computer. IP addresses are device specific and unique. Thus, they differ between the two computers.
</details>
---
## Question 3
Consider the following code that implements parts of Assignment 6 and mark all correct statements.
```python
def find_top10_restaurants_for_trip(origin, destination, departure_date, departure_time, radius):
    limit = 10
    connection = find_connection(origin, destination, departure_date, departure_time)
    restaurants = find_restaurants(
			c.destination_x,
			c.destination_y,
			c.get_unix_arrival_time()
		)
    rests_sorted = sorted(restaurants, key=lambda tup: tup[1], reverse=True)
    
    return rests_sorted[:limit]
```
✅ After line 7, *radius* needs to be added to the function *find_restaurants()* as an additional parameter after *connection.get_unix_arrival_time()*.
❌ In line 3, *radius* needs to be added to the function *find_connection()* as an additional parameter after departure_time.
❌ In Assignment 6, this code generally would not work because the datatypes from [*transport.opendata.ch*](http://transport.opendata.ch/) are not compatible with [*api.yelp.com*](http://api.yelp.com/).
❌ In Assignment 6, this code leads to the issuing of two HTTP POST requests (to [*transport.opendata.ch*](http://transport.opendata.ch/) and [*api.yelp.com*](http://api.yelp.com/) respectively).

<details>
<summary>Explanation</summary>

✅ **Correct**. In the assignment we see that the method find_resturants() requires the parameter radius. 
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/6cbc72ed-5f0b-43c1-8dc2-80432c9425f7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TP2DDKDN%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T231610Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQDH3QwQLDkvP94I8rvxAyQe8ikZM3vBHtjvkIhPmXnLnAIhAOnA21QnporhdOLjbrBmBKigeaI68%2BhZdeLE700aP5QHKv8DCCcQABoMNjM3NDIzMTgzODA1IgxudAfeRd8C8J5RhcYq3AMRveJdtx2%2BhfUPx2aCq82KLMlLwzMUCPZMUGYlDssSTQnkHYrqu93TeiNRWq09%2BAB7%2Bq%2F9eKg9RYHkmamXdfY0QjJbDoDueEp3fWSJgO3JhgeiXI55Qf09RdsRS3RQtlr05XiaCNKsN33VtsnMjC0z6lUlMLXo4MNqnhVfNpDWyOFqvXSqbHOS3LB04ZqxmgZlCzpWeu3Nk26POH5pq4qK0MKT%2FSUWJ5w7CMlAShIIPUA%2F4dG50rdijI3pDreOUZVl5Tu1b0gVBRGTm4qq2GB%2BaDNDvwDWFDG6%2BkOSP3j%2BlUTj9X4Wz8nUtoDZZMSC%2F%2Ffq5Dy5kU%2FhlAFL5yE4WtQ6mcmpqGhIKsAHUi%2BwMuS%2FHItZcOPS%2FIA0UCQDNAFUyDWE0BxHTSGkd0RdRNYMx2NzrHg4jRCGFXLi36CF168E5WbZZxkx2tVGE6HzW2ibNZFJClj5xdh%2BuNMbJb%2B0UAn%2B8co1v%2BD2pfxOl3m2hdXkn73aOZxPVHptCdQMxtKb0NP71Y1hD83pt%2Bb51jOy%2BSLs6Nh3WqZBCGYQN5rkTkSbU5OemTIHxlURZw5CYjqDlrWe7kLsNV57VSud3rxalJKwDDIUsA3eTt22myxf46OkTxImzhHAh15cKQy2NjDlzffJBjqkAbnSIJv6GoMoT5vhW0ND8k8lp7AyNFdol1rJ%2BClCJJ5PlzMYw6A2TUTdiOjdheNrWAzVI74XtwuGInL9LtO30W2QSvgFcE%2FoqQMfX85q1eDQerlYJcz43sk7fOziTmbvhUOuXIHKDup9R%2FxJelwNmg8gIwYbM1Z9YD1AiBT3JEkcLfDnmwAaVTr6CiehTLz%2F%2B91gtRwf2qlV9v3Lg071jdIt5L%2Bk&X-Amz-Signature=9f64f879fb4cd04533996b19e5fd6825873b2b1605cc183d7677fd429ae60e79&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
This is because the [Yelp API tells us](https://docs.developer.yelp.com/reference/v3_business_search) that this parameter  must be provided to look for businesses around a specific location. 
❌ **Incorrect**. Radius has nothing to do with public transport connections. 🙂
❌ **Incorrect**. The datatypes are compatible. Both API expect and return JSON objects. And we already learned [how to work with JSON objects](/5b0832dbf9454eb1941b7632e68a9abb#2248b4b3bfb444e89a15bbeb58513b6e) in Python.
This is exactly the power of JSON. We don’t know whether the Yelp API and Open Transport API are implemented with he same technologies. However, because they both adhere to JSON standard, we can use the output data from Open Transport API as input data for our request at the Yelp API.
❌ **Incorrect**. As we are retrieving data from both API’s we are issuing GET requests. We would use POST requests if we would want to create a new resource on one or both of the servers. For example a new train connection or a new restaurant that recently has opened.

</details>
---
## Question 4
Consider the following code that implements part of Assignment 6. Assume that “abcd” is a valid API key. 
Your colleague asks you for feedback on this code.
What do you tell them?
```python
api_key = 'abcd'
url= 'https://api.elp.com/v3/businesses/search'

headers = {'Authorisation': 'Bearer ' + api_key}

restaurants = {}

params = {}
params['latitude'] = x
params['longitude'] = y
params['opening_times'] = opening_times
params['radius'] = radius
params['categories'] = "restaurants"

r = requests.post(params=params, url, headers=headers)
```
❌ You need to use a PUT request in line 15.
✅ You need to use a GET request in line 15.
❌ The variable radius in line 12 needs to be cast to float. Otherwise an error will occur.
❌ The code works perfectly.
✅ The parameters in line 15 are in the wrong order, they need to be orders like this: 
`r = requests.get(url, params=params, headers=headers)`
❌ The parameters in line 15 are in the wrong order, they need to be ordered like this:
`r = requests.get(params=params, headers=headers, url)`

<details>
<summary>Explanation</summary>

❌ **Incorrect**. We are retrieving data from the server. Thus, we need to use GET request.
✅ **Correct**. We are retrieving (getting) data from the server.
❌ **Incorrect**. Because statement 5 is correct, which means there is an error in the code.
✅ **Correct**. According to the [requests library documentation](https://requests.readthedocs.io/en/latest/api/#requests.get), the url must be the first parameter.
❌ **Incorrect**. The url must be submitted as the first parameter.
</details>
---
## Question 5
When working on Assignment 6, which packets did you see in Wireshark when interacting with [https://unisg.ch](https://unisg.ch/) ?
✅ TCP packets with TLS-encrypted content.
❌ UDP packets with TLS-encrypted content.
❌ TCP packets and HTTP packets.
❌ HTTP packets with TLS-encrypted content.

<details>
<summary>Explanation</summary>

✅ **Correct**. Because we are using **HTTPS** on the **application** layer, **TLS** is used on the **transport** layer to establish an encrypted and secure connection between the client and the unisg server.
❌ **Incorrect**. UDP connections are not encrypted with TLS. TLS is used to make TCP connections secure. → [Difference between UDP and TCP](/305c770201f94279bfd468d86c733ae6#0dea562007ff4bcb8e4f0fd74d244a86).
❌ **Incorrect**. As we are using the secure **HTTP****S** in the url, we cannot see any **HTTP** packets.
❌ **Incorrect**. TLS is used in combination with HTTPS. Both protocols enable encryption. HTTPS on the application level and TLS on the transport level.

</details>
---

