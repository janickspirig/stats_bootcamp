---
title: "Quiz 6"
notion_id: "1cd9dd4b-2d28-4795-9da6-fa4b4cae7284"
notion_url: "https://www.notion.so/Quiz-6-1cd9dd4b2d2847959da6fa4b4cae7284"
exported_at: "2025-12-14T01:01:22.501481+00:00"
---

# Quiz 6

## Question 1
In Assignment 6 war Ihr letztes Ziel, die 10 besten Restaurants zu finden. Würde der folgende Code dieses Ziel erreichen?
```python
def find_top10_restaurants_for_trip(origin, destination, departure_date, departure_time,
radius):
	limit=10
	c = find_connection(origin, destination, departure_date, departure_time)
	rests = find_restaurants(c.destination_x, c.destination_y, c.get_unix_arrival_time(), radius)
	return rests [:limit]
```
❌ Ja, das ist perfekt. Sie erhalten die 10 besten Restaurants, weil wir die Liste auf 10 begrenzt haben.
❌ Sie müssen dies zusätzlich tun: `rests sorted = sorted(rests, key=lambda tup: tup[1])` und dann `return rests_sorted[:limit]`
❌ Es gibt keine Möglichkeit, nur die ersten 10 Verbindungen anzufordern.
❌ Sie müssen dies zusätzlich tun: `rests_sorted = sorted(rests, key=lambda tup: tup[2], reverse=True)` und dann `return rests_sorted[:limit]`
❌ Die API berücksichtigt bereits standardmäßig nur die Top-10-Restaurants.
✅ Sie müssen dies zusätzlich tun: `rests_sorted = sorted(rests, key=lambda tup: tup[1], reverse=True)` und dann `return rests_sorted[:limit]`

<details>
<summary>Explanation</summary>

> 💡 **[sorted function](/5b0832dbf9454eb1941b7632e68a9abb#7c022c5cc1a647d58ba1a7e82406c3e6), [access elements in nested lists (or tuples)](/5b0832dbf9454eb1941b7632e68a9abb#8526be0c72d1432c83067d8315535bd0)**
❌ **Incorrect**. The code will return the **10 closest** **restaurants** but not necessarily the 10 best ones (based on rating).
❌ **Incorrect**. The `sorted()` function sorts by default in **ascending** order. Thus the restaurant with the **lowest rating** would appear on top in this case.
❌ **Incorrect**. This was implemented in the assignment, to get the next **x** connections.
❌ **Incorrect**. The API returns **all restaurants that are within the provided radius** of the x and y coordinate location. Therefore it can be that the API returns less or more than 10.
✅ **Correct**. The rating of the restaurant is at **index position 1** of each element in `rests`. Thus, the rating can be accessed by using `tup[1]`. Now as we pass the `reverse=True` parameter to the **sorted** function and the restaurants are sorted in **descending** **order** so the **highest-rated** one is appearing **on top**.
</details>
---
## Question 2
Sie möchten ein Experiment durchführen, beidem Sie einen Webbrowser, z.B. Firefox, öffnen und auf [http://example.org](http://example.org/) gehen. Parallel dazu zeichnen Sie mit Wireshark die Pakete im Netzwerk auf. Welche der folgenden Aussagen sind richtig?
❌ Um die IP-Adresse von [example.org](http://example.org/) zu ermitteln, können Sie ipconfig (oder ifconfig) verwenden.
✅ Der Name ([example.org](http://example.org/)) wird vom DNS auf eine zugehörige IP-Adresse abgebildet. Sie können auch den Befehl nslookup verwenden, um die IP-Adresse von [example.org](http://vonexample.org/) zu finden.
✅ Auf Wireshark sehen Sie eine HTTP-GET-Anfrage, gefolgt von der Antwort des Servers mit HTML-Inhalt.
❌ Die IP-Adresse von [example.org](http://example.org/) wird von der IP-Schicht gefunden, welche die Router im Internet abfragt.

<details>
<summary>Explanation</summary>

> 💡 **[networking stack](/305c770201f94279bfd468d86c733ae6), [DNS](/98fd60d45a0a4426a6f28d2665ba5a43#56e2d7cb60a34ae29ac8a805c79f51d8), [HTTP request methods](/f6bdc16ceadd474d895561e3c6762d42)**
❌ **Incorrect**. `ipconfig` command can be used to **configure the Internet Protocol layer** on your local computer and has nothing to do with domain names. For example, with `ipconfig /release` you can get rid off your IP address and with `ipconfig /renew` you can get a new one. Just **don’t** do `ipconfig /release` during a zoom call, otherwise your counterpart will have some questions. 🙂
✅ **Correct**. The DNS server is responsible for **mapping domain names to IP-addresses** and we can use the `nslookup << domain name >>` command to query the IP address of a domain by using the terminal.
![Using nslookup to query the IP-address of [unisg.ch](http://unisg.ch/) webpage](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/c30fd7e9-9c93-41fd-957c-3637c155530b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667I25T2LZ%2F20251214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251214T010121Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJGMEQCIBkmyRl5DFSIuKxyAfQRFFrR6xiQswxq028N9YntsYIyAiBIY%2F5KfdJeyol0dO1RukVG%2FuRgzAXXdHCgvqb0SfPatSr%2FAwgqEAAaDDYzNzQyMzE4MzgwNSIMD9wi%2FWjKkBXrtoj9KtwDkoFAArEgRwgiXLRC7jjMoOtr5MsSS2qEKl4OeEXzx1b9ACUGbb0O3%2FmD6R1f6xHT%2FG9jTok9myWjFH8iUyXrD%2BbtXDNoHHrrPK%2B8O%2FBo0UJpK%2BzFaH8xGgDdgcJIY2NW6oydPzgIpYSIKsWoyCHK53vWUHC7uzysntZVg%2Bv8kHXn8vxmNPPrZ%2FTxdcPiwydFg5BO60O%2FskPpdYOzaFLmT81MsBbfDvg0KHSXHT14KXHx26P0hmfyQVzntL%2Bif%2FYKTrOIwkktqNuJwc3Xi5s1nvFpkG64JHjTDymzKc%2BjWCLCwLstO2Us%2BD0gHGPYroDIc0juI86KEhgxlW97mKmexbvGKgV%2B7Yk4sTGum5%2BSz1ZNCBJfBLLv8x1Be3lCtIGZPzZVzFkoTe8AVHKr%2FhmXFUJZT3HORYN1%2FlQ1ZgOqTUPQxawqF38X61Jz4vm5sDlVU5vpxsxX7pEZIYhkp7fWOOLQHMdIbRUX9Z247n8GgWUivpHQPy37F%2BDK%2Bj03Rbh7mw4MW9DTyaO5fhXrUEf0Oh7nAdR3GCAd1OMALHUVAnw2P7BwPhT0SRALrZLtRqUAQwfX9S3XC%2FmcHW9%2BxzhEm%2FuV4wcKlvH%2BELv%2Bf02HuGmEwDzq5apykVs%2BI8AwkJb4yQY6pgERWprf4eTGQbZ5SfG93SUSgrU%2FH0nxrkiCEurg2EjFbDtrXnvYNiLZtxfS%2FucV0luV7hBWHq863JGKZnCBBc8U89SVsNpzOua00hvKe6viRWSy2a0%2B4VpYfUrLJbcGz4O9qM3ILefKlJ2t5%2FhzuxDhh9VjSfMxltTBt12ondCIbhn%2B2RT65V6Qxyi2MMWWMwqB900kATbmjv9Q72iqD9X%2BZODI7StZ&X-Amz-Signature=5e3ba552e965df5cd5c1154bb901ddbceb90bd2c728b61aaf0cc8a5a87c70801&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
✅ **Correct**. When calling [http://example.org](http://example.org/) the **http protocol** is used. As we are requesting a resource from the example.org server (the webpage) our browser is sending an HTTP **GET **request.
❌ **Incorrect**. The address is found using the **DNS protocol** and the DNS protocol is part of the **application** layer.
</details>
---
## Question 3
Gegeben ist der folgende Code, der Teile von Assignment 6 implementiert.
```python
def find_restaurants (x, y, open_at, radius):
	url = 'https: //api.yelp.com/v3/businesses/search'
	restaurants = []
	params= {}
	params['latitude'] = x
	params['longitude'] = y
	params['openat'] = open_at
	params['radius'] = radius
	params['categories'] = "restaurants"
	r = requests.get(url, params=params, headers=headers)
```
Bitte markieren Sie **alle** richtigen Aussagen.
✅ Die Anfrage wird zu einem Autorisierungsfehler (*authorization failure*) führen - Sie müssen den API-Schlüssel (*API key*) angeben!
❌ Die Anfrage wird fehlschlagen, weil der Parameter *'city'* fehlt.
❌ Es gibt kein Problem mit dem Code, er wird funktionieren.
✅ Auf Wireshark würden Sie ein TLS-Paket sehen.

<details>
<summary>Explanation</summary>

> 💡 **[API requests](/b431f30ba0674f04a6c836035b69ea8e), [HTTPS](/923d77685b5c46518f7726145cfce814), [TLS](/923d77685b5c46518f7726145cfce814)**
✅ **Correct**. From the [API documentation](https://docs.developer.yelp.com/reference/v3_business_search) we can see that we must authenticate ourselves by providing an API key.
❌ **Incorrect**. From the [API documentation](https://docs.developer.yelp.com/reference/v3_business_search) we can see that there is actually no parameter city. We must provide **latitude** and **longitude **instead:
![Required parameters latitude and longitude](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/fe685723-7f02-4a13-bc3e-b92ec8212ba7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664XBU7ZTW%2F20251214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251214T010121Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJHMEUCIQCqmQqiep4%2F0yUSUvVgxiFpu%2F1%2BsAxpzbjY%2B2%2FCsBBR1QIgUrDpl29w78LZeUxTSPHpH5%2FrQFpR3PM%2BeskshSDwUYgq%2FwMIKhAAGgw2Mzc0MjMxODM4MDUiDPeLNffPTT4SVK7A8ircA40Fx%2B16G5QiMgQ%2FdYfVkV3NXKDKvPTpIGoxwKBwP%2B64nJ3ZbPRhH9Xm96piSTNNZ5BaQAFc5h3bruk4H2KSs323uKyrdxHhMfbyTeK8QsjPTAMqeRt%2FwBmMUosWPwj7OMaWozTZ%2FZgylwutZNhj14NwaTGPTm4i%2FbYBji6LQcQn%2F%2FjLo04YdNVODlTX2VJDhaEW99L90lZJy4ptEsvObcfkRJVao8LpkJWY5%2BkPEPS8CcAgWzE2YmRZY630pQrErRJCbh0pjvm3r7bK9ypBBVAN%2F1pyrAxOGKvL%2BXrU2X%2FiAkck5lyVrmfpP8GCjvox3Xb7gExie54LZSjpdcpC7hKJvO%2FQ701DVTmfGlRYPBnoyH3ncpxG%2Fxlta5mLuJ2O4BVC0cw86liFU77b41SabeZ%2FAOpQfSEJTOismfWHODI0ydQf4hOdQeUDAMmCwEhmgArlsMKMd9gz0fhG%2FGgpdTdTrSdetzOOD2cIG2L0qeBxGpQJJy3z3zopZYjQcIXmy5oUAxV5x78x14gR2%2FJybzBWeS%2FfJtDsFYjZDtC7p3PAElvpaMe7%2FqXy84DyqiFfBRACLqmU6Si5t8FfMFvGhZnhtK1kx0kA4RTCMBzIcziVl0Lois%2BAfaPI5urKMIOX%2BMkGOqUBHSHiXsU8Smk5hbHxKHnCS0xmwNfObc%2BL4FvuVX%2Bt8naPXLlJ4T%2Fo05hjW0yDlp6blP4nM4wszywlRVx8IT7aLcvWbUsmqJSII49WPF4K7ls4v86OF1ps4T9g4Is8C0%2B36IyDP%2FWDbRD2rE4RWgq3rckHIZtRj0ae85CpObO2l1Q%2FBlxTbswA9MSRgJBEfyTlNdWFMBNpyrC4CvP3JciJ4917X3sT&X-Amz-Signature=fc16842e7e815719faf61d58d5132a840128a8993bccd9c765725d69fcc7bb65&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
❌ **Incorrect**. The API key is missing (see answer 1). 
✅ **Correct**. from the url we can see that the **https** protocol is used (`https://`) and the https protocol uses **TLS** to establish a secure connection on the **transport** layer.
</details>
---
## Question 4
Sie rufen im Webbrowser [https://example.org](https://example.org/) auf, während Sie die Pakete mit Wireshark verfolgen. Was würden Sie sehen?
❌ Der gesamte Netzwerkverkehr wird verschlüsselt, d.h., alle Anwendungs-, TCP- und IP-Pakete werden verschlüsselt, so dass ein Angreifer nicht einmal die Ziel-IP-Adresse kennt.
❌ Sie können sehen, dass eine HTTP-GET-Anfrage gesendet wird, aber die Ziel-IP-Adresse ist verschlüsselt, da wir ein sicheres Transportprotokoll verwenden.
✅ Sie können die IP- undTCP-Pakete sehen, aber die Anwendungsdaten innerhalb des TCP-Pakets sind TLS-verschlüsselt (Sie werden also nicht einmal wissen, ob es sich um HTTP handelt).
❌ Sie sehen, dass es sich um eine HTTP-Anfrage an eine URL handelt, aber das HTTP-Verb (GET) und der Anfrageinhalt sind verschlüsselt.

<details>
<summary>Explanation</summary>

> 💡 **[what ](/923d77685b5c46518f7726145cfce814#f0ce6a93e602411b84715ccf86bad894)[*actually*](/923d77685b5c46518f7726145cfce814#f0ce6a93e602411b84715ccf86bad894)[ is encrypted on each layer](/923d77685b5c46518f7726145cfce814#f0ce6a93e602411b84715ccf86bad894)**
❌ **Incorrect**. If we would encrypt everything we **couldn’t send our request over the internet** to [example.org](http://example.org/). Because the other entities in the network **could not see** to where the request / packet should be routed to. So even if https is used, not everything is encrypted and made invisible to others.
❌ **Incorrect**. The remote **IP address is visible**, even though the request is encrypted and secured. This is necessary so that the request can be routed to the right destination over the internet.
✅ **Correct**. The HTTP request is only relevant on the **application layer**, i.e., for our web browser and the [example.org](http://example.org/) server. However, the network **must not see** the HTTP request in order to know to where the request / packet should be routed to.
❌ **Incorrect**. As the previous answer (type of request (HTTP) not visible) is correct, this statement can’t be correct as well.
</details>
---
## Question 5
Gegeben ist der folgende Code, der Teile von Assignment 6 implementiert.
```python
def find_connection(origin, destination, departure_date, departure_time): 2
	url = 'http://transport.opendata.ch/v1/connections'
	params = {}
	params['from'] = origin
	params['to'] = destination
	params['time'] = departuretime
	r = requests.post(url, params = params) first_conn= r.json()['connections'][0]
	
	× = first_conn['to']['coordinate']['x']
	y = first_conn['to']['coordinate']['y']
	departure = first_conn['from']['departure']
	arrival = first_conn['to']['arrival']
	transport_means = first_conn['products']
```
Bitte markieren Sie **alle** richtigen Aussagen.
❌ Der Code ist in Ordnung. Er wird funktionieren.
❌ Die Anfrage wird zu einem Autorisierungsfehler (*authorization failure*) führen- Sie müssen den API-Schlüssel(*API key*) angeben!
✅ Das Abreisedatum (*departure date*) fehlt in den Anfrageparametern.
✅ Die Zeilen, die x und y aus der Antwort abrufen, sind falsch. Es sollte `first_conn['to'][station]['coordinate']['x']` bzw. `first_conn['to'][station]['coordinate']['y']` lauten.
✅ Die Anfrage wird fehlschlagen, da wir GET und nicht POST verwenden müssen.
❌ [opendata.ch](http://opendata.ch/) kann nur über HTTPS erreicht werden, daher wird die Anfrage fehlschlagen.

<details>
<summary>Explanation</summary>

> 💡 **[extracting data from API response](/b431f30ba0674f04a6c836035b69ea8e#10b666e3faee4c088aeeb9b30ee93a28)**
❌ **Incorrect**. Because statements 3, 4 and 5 are correct.
❌ **Incorrect**. Open data does not require an API key, otherwise it wouldn’t make sense to call themselves **open** data 🙂
✅ **Correct**. If we provide a value for the `time` parameter we must also provide a value for the `date` parameter.
✅ Correct. The example output in the [API documentation](https://transport.opendata.ch/docs.html#connections) shows that all information about the station is stored inside a sub-dictionary `station`:
![Example output from the /connections API](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/87eed5b4-a6db-4a5d-a62f-1bbe7c6cd8f2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XFA5HJSL%2F20251214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251214T010122Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJHMEUCIQCYDmBDDzwWcI8POVyy3U8xdqOJlzO3BznRQmlXLPRPRQIgCA1J8Az0NNI9irz2dhaPwM8tuHI%2F01ZF4jcUSrr%2B3zEq%2FwMIKhAAGgw2Mzc0MjMxODM4MDUiDDR1N0REXK%2B2MKsSCCrcAw5IJGuplotnVM9gHBQ6z2rpDWlUeI5ojHERfcrGdYycqbrBqVUTE74hT%2BrrugGMIQ6j3cpGheuvPbFnLqcZ0qDF%2B4S%2F0rls3DsZhZ40WFz9L0D519InSmWfoo%2FHXLcQmnz7r%2FZLUm%2B0s3zwVACeVssDiQAGL3gQpzq2Mev2WXBlpFK7mVkJILmEzazn6hpHpd8nOOAZGKsROVxmy2RoQrkliLOes5shV%2Fm8P1KqfAcOBYPL5aVNsxh9YOsJzynXmRVs6Log81WGZ5dFBGKltQKBXElA6SadG0yE%2FcgSpBl4nOE5Go1eUqKnRjadj2DcfkgZuttOlkyim9p93WdYrsyAKTc1X7Pk%2Fa97ae5d9Lh28uFYIcvXcU5t%2BUq3C1AJy3lwvm1VjqQMvT3u6qgkBEIp3AiC4h0Eil%2FwiGxyVukAeclgj7yN3vyuMQCK5UApWwoGOsMcMVePodq%2F5rWUPLu9mEf6OVLSOwpJY6Rs9EvyaOx2IuT0VIV91KCHSAr1jUOjgLm%2F7NTdxOQL8abSoSVn4u%2FTn5r%2Btl7Wq1U2TDupY4UvT2lRza1HHvx9yirXPMKVVGvuzwN%2FqP76jQzMH4hwLGQ%2FmDfIjFGNd22RAufF7Hn4CVCAtljPi1XiMI%2BX%2BMkGOqUBHaS%2BiT7Nnr924%2F5EJgkMNqnqVxDqAdfSy5K4FBTcBUinvWYIVhieTSvEdOJliuCsZKiXERC%2BOXMXATfZe4UFGdUaGqXDMBeoBiGzoyiuxTooJ9YVzdPn8UHTfEL5DE64AERxJSh4htOu4AmBqWoXhNAodpp1Wo9dFRqmm8JC7CKUH0WwCUwfeLlfONzbZ5zcTQ6TSvpQzlGg3QeVStVLv1YbHpaZ&X-Amz-Signature=3ec8867fcd40c782a7b7f0ce077b7520d0d4b2ceedaca10173053c1725c769fb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
❌ **Incorrect**. In the [API documentation](https://transport.opendata.ch/docs.html#connections)  we can see that the http protocol can be used:
![Example request URL to the /connections API](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/2e088418-bd12-4539-a730-3e04a06915e0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XFA5HJSL%2F20251214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251214T010122Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJHMEUCIQCYDmBDDzwWcI8POVyy3U8xdqOJlzO3BznRQmlXLPRPRQIgCA1J8Az0NNI9irz2dhaPwM8tuHI%2F01ZF4jcUSrr%2B3zEq%2FwMIKhAAGgw2Mzc0MjMxODM4MDUiDDR1N0REXK%2B2MKsSCCrcAw5IJGuplotnVM9gHBQ6z2rpDWlUeI5ojHERfcrGdYycqbrBqVUTE74hT%2BrrugGMIQ6j3cpGheuvPbFnLqcZ0qDF%2B4S%2F0rls3DsZhZ40WFz9L0D519InSmWfoo%2FHXLcQmnz7r%2FZLUm%2B0s3zwVACeVssDiQAGL3gQpzq2Mev2WXBlpFK7mVkJILmEzazn6hpHpd8nOOAZGKsROVxmy2RoQrkliLOes5shV%2Fm8P1KqfAcOBYPL5aVNsxh9YOsJzynXmRVs6Log81WGZ5dFBGKltQKBXElA6SadG0yE%2FcgSpBl4nOE5Go1eUqKnRjadj2DcfkgZuttOlkyim9p93WdYrsyAKTc1X7Pk%2Fa97ae5d9Lh28uFYIcvXcU5t%2BUq3C1AJy3lwvm1VjqQMvT3u6qgkBEIp3AiC4h0Eil%2FwiGxyVukAeclgj7yN3vyuMQCK5UApWwoGOsMcMVePodq%2F5rWUPLu9mEf6OVLSOwpJY6Rs9EvyaOx2IuT0VIV91KCHSAr1jUOjgLm%2F7NTdxOQL8abSoSVn4u%2FTn5r%2Btl7Wq1U2TDupY4UvT2lRza1HHvx9yirXPMKVVGvuzwN%2FqP76jQzMH4hwLGQ%2FmDfIjFGNd22RAufF7Hn4CVCAtljPi1XiMI%2BX%2BMkGOqUBHaS%2BiT7Nnr924%2F5EJgkMNqnqVxDqAdfSy5K4FBTcBUinvWYIVhieTSvEdOJliuCsZKiXERC%2BOXMXATfZe4UFGdUaGqXDMBeoBiGzoyiuxTooJ9YVzdPn8UHTfEL5DE64AERxJSh4htOu4AmBqWoXhNAodpp1Wo9dFRqmm8JC7CKUH0WwCUwfeLlfONzbZ5zcTQ6TSvpQzlGg3QeVStVLv1YbHpaZ&X-Amz-Signature=b4a924051cafb1df7e3bb2e8655674d0cf045523ca1bb47f44bf4dd4312b9ee7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
</details>
---

