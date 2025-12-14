---
title: "Quiz 5"
notion_id: "5c2bb23c-be33-4486-bb09-7119af02d89c"
notion_url: "https://www.notion.so/Quiz-5-5c2bb23cbe334486bb097119af02d89c"
exported_at: "2025-12-13T23:11:00.133131+00:00"
---

# Quiz 5

## Question 1
Sie rufen im Webbrowser [**http://example.org**](http://example.org/) auf, während Sie die Pakete mit Wireshark verfolgen. Was würden Sie sehen?
❌ Sie sehen, dass es sich um eine HTTP-Anfrage an eine URL handelt, aber das HTTP-Verb (GET) und der Anfrageinhalt sind verschlüsselt.
✅ Sie können die IP- und TCP-Pakete sehen, wie auch die Anwendungsdaten innerhalb des TCP-Pakets.
❌ Sie können sehen, dass eine HTTP-GET-Anfrage gesendet wird, aber die Ziel-IP-Adresse ist verschlüsselt, da wir ein sicheres Transportprotokoll verwenden.
❌ Der gesamte Netzwerkverkehr wird verschlüsselt, d.h., alle Anwendungs-, TCP- und IP-Pakete werden verschlüsselt, so dass ein Angreifer lediglich die Ziel-IP-Adresse kennt.
❌ Keine der anderen Antworten ist korrekt.

<details>
<summary>Explanation</summary>

> 🧑‍🏫 **[Networking stack](/305c770201f94279bfd468d86c733ae6), [HTTP request methods](/f6bdc16ceadd474d895561e3c6762d42)**
When you visit [**http://example.org**](http://example.org/) in your web browser, you are making an HTTP request. HTTP is a protocol used for transmitting web pages over the internet. Here’s what happens and what you would see in Wireshark:
- HTTP is not encrypted. This means that the data being sent and received can be read by anyone who intercepts the traffic.
- When you visit a website using HTTP, the request and response data are sent in plain text.
❌ **Incorrect**, HTTP traffic is not encrypted. If it were HTTPS (HTTP Secure), then the data would be encrypted, but the question specifies HTTP.
✅ **Correct,** since HTTP is not encrypted, you can see the IP and TCP packets, as well as the actual data being transmitted (the application data) within the TCP packets. This includes the HTTP GET request and any other data being sent.
❌ **Incorrect,** the target IP address is not encrypted in HTTP traffic. Secure transport protocols like HTTPS would encrypt the data, but not the IP address.
❌ **Incorrect,** this describes HTTPS, not HTTP. In HTTP, none of the traffic is encrypted.
❌ **Incorrect,** one of the other answers is correct, specifically the one stating that you can see the IP and TCP packets and the application data within the TCP packets.
</details>
---
## Question 2
Sie möchten ein Experiment durchführen, bei dem Sie einen Webbrowser, z.B. Firefox, öffnen und auf [https://example.org](https://example.org/) gehen. Parallel dazu zeichnen Sie mit Wireshark die Pakete im Netzwerk auf. Welche der folgenden Aussagen sind richtig?
Wählen Sie *alle* richtigen Aussagen aus.
✅ Der Name ([example.org](http://example.org/)) wird vom DNS auf eine zugehörige IP-Adresse abgebildet. Dabei spielt es keine Rolle, ob Sie **http** oder **https** verwenden.
❌ Um die IP-Adresse von [example.org](http://example.org/) zu ermitteln, werden die Router entlang der Route zu [example.org](http://example.org/) abgefragt.
✅ Auf Wireshark können Sie den HTML-Inhalt der Antwort des Servers **nicht** sehen.
❌ Abhängig davon, ob Ihr Computer via Kabel (Ethernet) oder kabellos (WIFI) mit dem Internet verbunden ist, benötigen Sie zuerst eine DNS-Abfrage (oder eben nicht), um [https://example.org](https://example.org/) zu erreichen.

<details>
<summary>Explanation</summary>

> 🧑‍🏫 **[Networking stack](/305c770201f94279bfd468d86c733ae6), [DNS](/98fd60d45a0a4426a6f28d2665ba5a43#56e2d7cb60a34ae29ac8a805c79f51d8), [HTTP request methods](/f6bdc16ceadd474d895561e3c6762d42)**
✅ **Correct**, DNS (Domain Name System) is like the phonebook of the internet. It translates human-readable domain names (like [example.org](http://example.org/)) into IP addresses that computers use to identify each other on the network. This process is the same whether you are using HTTP or HTTPS. The protocol (HTTP or HTTPS) does not affect the DNS resolution process.
❌ **Incorrect**, DNS resolution does not involve querying routers along the route to the destination. Instead, it involves querying DNS servers. When you type a domain name into your browser, your computer contacts a DNS server (often provided by your ISP or a public DNS service like Google DNS) to resolve the domain name to an IP address. Routers are involved in routing the packets to the destination once the IP address is known, but they do not play a role in the DNS resolution process.
✅ **Correct**, HTTPS encrypts the data between your browser and the server, so tools like Wireshark cannot see the actual content of the data being transmitted. You can see the encrypted packets, but not the decrypted HTML content. If you were using HTTP (which is not encrypted), you would be able to see the HTML content in Wireshark.
❌ **Incorrect**, regardless of whether your computer is connected via Ethernet or WiFi, a DNS query is required to resolve the domain name to an IP address. The method of connection (wired or wireless) does not affect the necessity of a DNS query.
</details>
---
## Question 3
Gegeben ist der folgende Code, der Teile von Assignment 6 implementiert. Sie wollen alle gerade offenen Restaurants in einem gegebenen Radius finden.
```python
def find_restaurants(x, y, open_at, radius):
	url = '<https://api.yelp.com/v3/businesses/search>'
	restaurants = []
	params = {}
	params['latitude'] = x
	params['longitude'] = y
	params['open_at'] = open_at
	params['radius'] = radius
	params['categories'] = "restaurants"
	r = requests.get(url, params=params)
```

Bitte markieren Sie **alle** richtigen Aussagen.
❌ In Zeile 10 muss ein *PUT* request genutzt werden, um die Parameter zu setzen.
✅ Statt *open_at* sollte besser der Parameter *open_now* verwendet werden, um sicher zu jeder Zeit die aktuell geöffneten Restaurants zu finden.
❌ Es gibt kein Problem mit dem Code, er wird funktionieren.
✅ Die Anfrage wird zu einem Autorisierungsfehler (*authorization failure*) führen - Sie müssen den API-Schlüssel (*API key*) angeben!

<details>
<summary>Explanation</summary>

> 🧑‍🏫 **[API requests](/b431f30ba0674f04a6c836035b69ea8e), [HTTPS](/923d77685b5c46518f7726145cfce814), [TLS](/923d77685b5c46518f7726145cfce814)**
### Code Explanation
```python
def find_restaurants(x, y, open_at, radius):
    url = '<https://api.yelp.com/v3/businesses/search>'
    restaurants = []
    params = {}
    params['latitude'] = x
    params['longitude'] = y
    params['open_at'] = open_at
    params['radius'] = radius
    params['categories'] = "restaurants"
    r = requests.get(url, params=params)
```
1. **Function Definition**:
- `def find_restaurants(x, y, open_at, radius):` defines a function named `find_restaurants` that takes four parameters: `x` (latitude), `y` (longitude), `open_at` (time), and `radius` (search radius).
1. **URL and Parameters**:
- `url = '<https://api.yelp.com/v3/businesses/search'`> sets the URL for the Yelp API endpoint to search for businesses.
- `params = {}` initializes an empty dictionary to store the parameters for the API request.
- The next lines add key-value pairs to the `params` dictionary for latitude, longitude, open_at, radius, and categories.
1. **API Request**:
- `r = requests.get(url, params=params)` sends a GET request to the Yelp API with the specified parameters.
### Answer Explanations
❌ **Incorrect,** a PUT request is used to update resources on a server. In this case, we are retrieving data, so a GET request is appropriate.
✅ **Correct,** the `open_now` parameter is used to find businesses that are currently open at the time of the request. This is more straightforward than using `open_at`, which requires specifying a specific time.
❌ **Incorrect,** the code will not work as intended because it lacks an API key, which is required for authorization when making requests to the Yelp API.
✅ **Correct,** the Yelp API requires an API key for authorization. Without including the API key in the request headers, the request will fail with an authorization error.
### Corrected Code Example
Here is an example of how you might include the API key in the request:
```python
import requests

def find_restaurants(x, y, open_now, radius, api_key):
    url = '<https://api.yelp.com/v3/businesses/search>'
    headers = {
        'Authorization': f'Bearer {api_key}',
    }
    params = {
        'latitude': x,
        'longitude': y,
        'open_now': open_now,
        'radius': radius,
        'categories': "restaurants"
    }
    r = requests.get(url, headers=headers, params=params)
    return r.json()

# Example usage:
# api_key = 'your_api_key_here'
# print(find_restaurants(37.7749, -122.4194, True, 1000, api_key))
```
In this corrected code:
- `headers` is a dictionary that includes the API key for authorization.
- The `requests.get` function now includes the `headers` parameter to pass the API key along with the request.
</details>
---
## Question 4
Sie öffnen einen Browser auf Ihrem PC und rufen die Seite [https://www.unisg.ch](https://www.unisg.ch/) auf. Gehen Sie davon aus, dass Sie nur über Ihr Heimnetzwerk mit dem Internet verbunden sind.
Was ist die richtige Reihenfolge der ausgeführten Schritte?
✅ **Der Browser formuliert eine HTTP-GET-Anfrage, ermittelt die IP-Adresse des Servers über DNS, verpackt das HTTP in ein TCP-Segment (mit dem https-Standardport 443), verpackt dieses Paket in ein IP-Paket mit den richtigen Adressinformationen und schickt es auf das Trägermedium (natürlich ordnungsgemäss verpackt für dieses Trägermedium).**
❌ Der Browser formuliert eine HTTP-POST-Anfrage, erhält die IP-Adresse des Servers über UDP, verpackt das HTTP in ein DNS-Segment (am https-Standardport 80), verpackt dieses Paket in ein IP-Paket mit den richtigen Adressinformationen und schickt es auf das Trägermedium (natürlich ordnungsgemäss verpackt für dieses Trägermedium).
❌ Der Browser formuliert eine HTTP-POST-Anfrage, ermittelt die IP-Adresse des Servers über DNS, verpackt das HTTP in ein TCP-Segment (mit dem https-Standardport 443), verpackt dieses Paket in ein IP-Paket mit den richtigen Adressinformationen und schickt es auf das Trägermedium (natürlich ordnungsgemäss verpackt für dieses Trägermedium).
❌ Der Browser formuliert eine HTTP-GET-Anfrage, ermittelt die IP-Adresse des Servers über DNS, verpackt das HTTP in ein UDP-Segment (mit dem https-Standardport 440), verpackt dieses Paket in ein TCP-Segment mit den richtigen Adressinformationen und schickt es auf das Trägermedium (natürlich ordnungsgemäss verpackt für dieses Trägermedium).

<details>
<summary>Explanation</summary>

> 🧑‍🏫 **[Networking stack](/305c770201f94279bfd468d86c733ae6)**
Let's break down the correct answer and why the other options are incorrect.
### Correct Answer Explanation
**✅ Statement 1 **
1. ***…HTTP-GET-Anfrage…***
- When you open a webpage, the browser typically sends an HTTP GET request to retrieve the content of the page.
- Example: `GET / HTTP/1.1`
1. ***…ermittelt die IP-Adresse des Servers über DNS...***
- DNS (Domain Name System) translates the human-readable domain name (e.g., [www.unisg.ch](http://www.unisg.ch/)) into an IP address that computers can use to identify each other on the network.
- Example: `www.unisg.ch` might be translated to `192.0.2.1`.
1. ***…verpackt das HTTP in ein TCP-Segment…***
- HTTP requests are sent over TCP (Transmission Control Protocol), which ensures reliable delivery of data.
- The standard port for HTTPS (secure HTTP) is 443.
1. ***…verpackt dieses Paket in ein IP-Paket…***
- The TCP segment is then encapsulated in an IP packet, which includes the source and destination IP addresses.
1. ***…schickt es auf das Trägermedium…***
- Finally, the IP packet is sent over the physical network medium (e.g., Ethernet, Wi-Fi) to reach the destination server.
### Incorrect Answers Explanation
**❌ Statement 2**
- **HTTP-POST-Anfrage**: Incorrect because a POST request is typically used to send data to the server, not to retrieve a webpage.
- **UDP for DNS**: DNS queries can use UDP, but the rest of the statement is incorrect.
- **DNS-Segment**: There is no such thing as a DNS segment for HTTP data.
- **Port 80**: Port 80 is used for HTTP, not HTTPS.
**❌ Statement 3**
- **HTTP-POST-Anfrage**: Incorrect because a GET request is typically used to retrieve a webpage, not a POST request.
**❌ Statement 4**
- **UDP-Segment**: HTTP data is not sent over UDP; it is sent over TCP.
- **Port 440**: The standard port for HTTPS is 443, not 440.
- **TCP-Segment**: The statement is confusing because it mentions both UDP and TCP, which is incorrect for HTTP data transmission.
</details>
---
## Question 5
Geben ist der folgende Code, der Teile von Assignment 6 implementiert.
```python
def find_connection(origin, destination, departure_date, departure_time):
    url = '<http://transport.opendata.ch/v1/connections>'
    params = {}
    params['from'] = origin
    params['to'] = destination
    params['time'] = departure_time

    r = requests.get(url, params = params)
    first_conn- r.json()['connections'][0]
    x = first_conn['to']['coordinate']['x']
    y = first_conn['to']['coordinate']['y']
    departure = first_conn['from']['departure']
    arrival = first_conn['to']['arrival']
    transport_means = first_conn['products']
```
Bitte markieren Sie **alle** richtigen Aussagen.
✅ Die Zeilen, die x und y aus der Antwort abrufen, sind falsch. Es sollte first_conn['to']['station']['coordinate']['x'] bzw. first_conn['to']['station']['coordinate']['y'] lauten.
❌ Die Anfrage wird zu einem Autorisierungsfehler (*authorization failure*) führen - Sie müssen den API-Schlüssel (*API key*) angeben!
❌ Die Anfrage wird fehlschlagen, da wir POST und nicht GET verwenden müssen.
✅ **Der Code wird so nicht korrekt funktionieren.**
❌ [*opendata.ch*](http://opendata.ch/) kann nur über HTTPS erreicht werden, daher wird die Anfrage fehlschlagen.
✅ **Das Abreisedatum (*****departure date*****) fehlt in den Anfrageparametern.**

<details>
<summary>Explanation</summary>

> 🧑‍🏫 **[Transport Open Data API](https://transport.opendata.ch/docs.html), [requests library](/b431f30ba0674f04a6c836035b69ea8e)**
Let's break down the provided code and the answer options to understand why the correct answers are marked as they are.
### Code Explanation
1. **Function Definition:**
```python
def find_connection(origin, destination, departure_date, departure_time):
```
- This line defines a function named `find_connection` that takes four parameters: `origin`, `destination`, `departure_date`, and `departure_time`.
1. **URL and Parameters:**
```python
url = '<http://transport.opendata.ch/v1/connections>'
params = {}
params['from'] = origin
params['to'] = destination
params['time'] = departure_time
```
- `url` is the endpoint for the API.
- `params` is a dictionary that will hold the parameters for the API request.
- The parameters `from`, `to`, and `time` are set using the function's arguments.
1. **API Request:**
```python
r = requests.get(url, params=params)
```
- This line sends a GET request to the specified URL with the given parameters.
1. **Extracting Data:**
```python
first_conn = r.json()['connections'][0]
x = first_conn['to']['coordinate']['x']
y = first_conn['to']['coordinate']['y']
departure = first_conn['from']['departure']
arrival = first_conn['to']['arrival']
transport_means = first_conn['products']
```
- `r.json()` converts the response to a JSON object.
- `first_conn` extracts the first connection from the JSON response.
- The subsequent lines extract specific details from `first_conn`.
### Answer Explanations
✅ **Correct,** the lines that retrieve `x` and `y` coordinates are incorrect. They should be:
```python
x = first_conn['to']['station']['coordinate']['x']
y = first_conn['to']['station']['coordinate']['y']
```
- The correct path to the coordinates includes the `station` key.
❌ **Incorrect, **the request will not lead to an authorization failure because the API endpoint does not require an API key for this specific request.
❌ **Incorrect, **the request will not fail because of using GET instead of POST. The API documentation specifies that GET is the correct method for retrieving connections.
✅ **Correct, **the code will not work correctly as it stands. There are issues with the path to the coordinates and the missing departure date in the parameters.
❌ **Incorrect,** the endpoint `http://transport.opendata.ch/v1/connections` can be accessed over HTTP, not just HTTPS. Therefore, the request will not fail due to this reason.
✅ **Correct,** the departure date is missing in the request parameters. It should be included like this:
```python
params['date'] = departure_date
```
</details>
---

