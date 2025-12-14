---
title: "Quiz 6"
notion_id: "288f8ada-9a05-473a-8fa7-c7a306512db5"
notion_url: "https://www.notion.so/Quiz-6-288f8ada9a05473a8fa7c7a306512db5"
exported_at: "2025-12-13T23:21:09.425667+00:00"
---

# Quiz 6

## Question 1
Consider the following code that implements part of Assignment 6.
The returned list of restaurants should contain all restaurants in a given radius that are open at the moment.
Assume that "abcd" is a valid API key.
Your colleague asks you for feedback on this code.
What do you tell them?
```python
api_key = 'abcd'
url = '<https://api.yelp.com/v3/businesses/search>'

headers = {'Authorisation': 'Bearer ' + api_key}

restaurants = []

params = {}
params['latitude'] = x
params['longitude'] = y
params['opening_times'] = opening_times
params['radius'] = radius
params['open_now'] = false
params['categories'] = "restaurants"

r = requests.get(url, params=params)
```
❌ The code works perfectly.
❌ The variable *opening_times* in line 11 needs to be cast to a string. Otherwise an error will occurr.
❌ The headers-parameter in line 16 is missing, it must look like this:
`r = requests.get(url, params=params, headers)`
❌ You need to use a **PUT** request in line 16.
❌ The parameter *open_now* needs to be set to *true*.
`params['open_now'] = true`
✅ The headers-parameter in line 16 is missing, it must look like this:
`r = requests.get(url, params=params, headers=headers)`

<details>
<summary>Explanation</summary>

> 💡 **[HTTP methods](/f6bdc16ceadd474d895561e3c6762d42), [HTTP request fields](/305c770201f94279bfd468d86c733ae6#d4dd954760524dca8de4bdfe52cf821d)**
❌ **Incorrect**,** **the code does not work perfectly. There are missing headers in the request.
❌ **Incorrect**, the variable `opening_times` in line 11 doesn't need to be cast to a string as the [Yelp API](https://docs.developer.yelp.com/reference/v3_business_search) doesn't have a parameter for `opening_times` in the first place, so this line of code is unnecessary and incorrect.
❌ **Incorrect**, the headers-parameter is missing in the request, however we can not include the parameter like this as [positional arguments cannot follow keyword arguments](/288f8ada9a05473a8fa7c7a306512db5).
❌ **Incorrect**, we are fetching/requesting resources from the Yelp server, thus we must sue a GET request.
❌ **Incorrect**, open_now parameter expects a boolean to be passed and `false` is a boolean value. So there is no correction needed here.
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/cf83aa91-009e-4922-b7e6-d11c4db32690/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665F4TFRUH%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T232107Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIQCVQnyMh6UqenyjvBud1DknI88KpwST1IXJhKuNcFHxWgIgIwVrnQP2Dg5WcV37XmpZCjUx4JYbusC%2FOjnhozjvfZcq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDB9Exe0tfj5lAbovSCrcA%2FeqLYESWbA2XXuVG9FxFSZciATV5b%2Fu%2B5U8sWd3yN%2BiZX44IQ9NcMB17yxPaYEmLk0Gw6N0LkvR1KfWpJphV%2FA3orVpXEzNKo9Sj12RSj%2F6m08bWc0fx3z%2FmBroDzGhNdU1YFYImcyKSrb%2B%2B6wsDEdHDdNq%2BjJKSZyKwQ7gek0%2FmJJ0jap6T7lAZzXgFE01D4s%2FgbodgyPt5eNFrsjjSOd1OPt7Yc3pRUUSBmhxSrhom%2Bb%2BxLnYd7DYDx3igMdO1z%2FRfT7ADcHXLsqSv7Tvv0l8WkU5dRotKy2%2BYnwH29VlqHCoMup9NGabv%2BiLimUnjsnlN%2FiVvBuVj%2FbeVaP0ZpDJluzjZaPHGhuAQnwsWWy6GF7sEcwE2gTWv34nUVUgCzTKT85BWmnRGAtS1uWIiuTi98BbIP6vQcM%2BtQzoJLbQdpps7WD%2BZe1qUjA1AarUH%2FvIJjK%2BmwQAA8Nszhx%2BV0OvG7fBqXDHBhIpdFz5DxstoOh5DskZmjp114F5w63xSHDzeLdN6%2Fhn5Atfv9HaE5pImxzRol%2Bign3g9glr9KVLkTKmNzOZLeoBo189R88oxf3rkgjVGhhH%2Fff4bYJ3ukl6AqEyBSNC6qzmnnuQd%2BShKEN7LaT99tDM7Tx4MPHN98kGOqUBTPvOa8%2FQfDOik%2BLId9PBMY9vPI1NttIaCyDyavASXWSq6oh2LjRUqKdCDKdeLQECWXpc30vOcEoZ8GXEXpKh56j0GAAD%2FLFLZammYwVmM6cY%2ByN6LpWfGfCkT%2FxLYPG1GvopGGs19bbxQmRi5kcqh1arwRM4WIYtimnucMSUr0wLnf8J9OxozNnxMZtOszffUtcccMgXKhbaRi44DjZyoYTxNfn6&X-Amz-Signature=c9fe16af91b2f1bb4cae03934450e4f89a12412022fc5edd75104dffee73f16e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
✅ **Correct**, the header includes our API key, thus to have the Yelp server accept and process our request wer must include the headers in the request.
</details>
---
## Question 2
Consider the following code that implements parts of Assignment 6 and mark all correct statements.
```python
def find_top10_restaurants_for_trip(origin, destination, departure_date, departure_time, radius):
    limit = 10
    connection = find_connection(origin,
                                 destination,
                                 departure_date,
                                 departure_time)
    restaurants = find_restaurants(
        connection.destination_x,
        connection.destination_y,
        connection.get_unix_arrival_time(),
        radius
    )
    rests_sorted = sorted(restaurants, key=lambda tup: tup[1], reverse=False)
    return rests_sorted[:limit]
```
❌ In Assignment 6, this code leads to the issuing of two HTTP POST requests (to *transport.opendata.ch* and to *api.yelp.com*, respectively)
✅ In line 13, the parameter *reverse* needs to be set to true, otherwise the function will return the 10 worst rated restaurants instead of the 10 best ones.
❌ In Assignment 6, this code generally would not work because the return datatypes from *transport.opendata.ch* are not compatible with *api.yelp.com.*
✅ In Assignment 6, this code leads to the issuing of two HTTP GET requests (to *transport.opendata.ch* and to *api.yelp.com*, respectively)
❌ In line 3, *radius* needs to be added to the function *find_connection()* as an additional parameter after *departure_time*.

<details>
<summary>Explanation</summary>

> 💡 **[sorted function](/5b0832dbf9454eb1941b7632e68a9abb#7c022c5cc1a647d58ba1a7e82406c3e6), [access elements in nested lists (or tuples)](/5b0832dbf9454eb1941b7632e68a9abb#8526be0c72d1432c83067d8315535bd0)**
❌ **Incorrect**, in the context of this code, we don't see any HTTP POST requests being issued. The functions `find_connection` and `find_restaurants` might be issuing HTTP requests, but we cannot infer the type of request (GET or POST) from the given information.
✅ **Correct**, the `sorted` function in Python sorts in ascending order by default. If we want to sort in descending order (which we would for the top 10 rated restaurants), we need to set `reverse=True`.
❌ **Incorrect**, we cannot infer the compatibility of return datatypes from the given code. The functions `find_connection` and `find_restaurants` are expected to handle any necessary data type conversions.
✅ **Correct**, in both cases we request data from a server. First, we request the next connections and seocnd information about restaurants at the destination. Thus, two GET requests are issued.
❌ **Incorrect**, the `find_connection` function is expected to find a transport connection between `origin` and `destination` at a given `departure_date` and `departure_time`. The `radius` parameter doesn't seem to be relevant for finding a transport connection, it is used for finding restaurants around the destination.
</details>
---
## Question 3
Why is it relevant that packet-switching networks remain agnostic of the concrete medium that is used to transmit signals?
✅ **Economic Efficiency: **Being medium-agnostic allows packet-switching networks to use the most cost-effective transmission technologies available. This could mean opting for copper wires, fiber optics, or wireless technologies depending on the context, such as the required bandwidth, distance, and cost constraints.
❌ **Enhanced Security:** By being agnostic of the transmission medium, packet-switching networks are more secure because hackers cannot tailor their attacks to a specific type of medium. Security hence does not anymore depend on the network protocols that are used.
✅ **Flexibility:** Packet-switching networks that are agnostic of the transmission medium provide flexibility in network design and expansion. As technology evolves or the needs of the network change, different transmission media can be integrated without the need for major changes to the network infrastructure or protocols.
❌ **Increased Speed: **Packet-switching networks that remain agnostic of the transmission medium inherently process data packets faster, regardless of the physical medium used. This is because in this case the network can optimize for specific transmission media, thereby exploiting them best for achieving high transmission speeds.

<details>
<summary>Explanation</summary>

> 💡 **[**Circuit vs. packet switching**](https://www.youtube.com/watch?v=oUN-s6aFMTk)**
✅ **Correct**, being medium-agnostic allows packet-switching networks to use the most cost-effective transmission technologies available. This could mean opting for copper wires, fiber optics, or wireless technologies depending on the context, such as the required bandwidth, distance, and cost constraints.
❌ **Incorrect**, the security of a network does not directly depend on whether it is agnostic to the transmission medium or not. It's more about the security protocols in place, not the type of medium used.
✅ **Correct**, packet-switching networks that are agnostic of the transmission medium provide flexibility in network design and expansion. As technology evolves or the needs of the network change, different transmission media can be integrated without the need for major changes to the network infrastructure or protocols.
❌ **Incorrect**, the speed of data transmission is dependent on the physical medium used and not on whether the network is agnostic to the transmission medium. Different media have different data transmission speeds. For example, fiber optics can transmit data faster than copper wires. Being medium-agnostic does not inherently make a network faster.
</details>
---
## Question 4
Which additional key-value pair must be added to the request **params** in Line 8 in the given code example if you only want to receive ***direct*** connections?
Look at the documentation and select the correct statement: [https://transport.opendata.ch/docs.html](https://transport.opendata.ch/docs.html) 
```python
url = '<http://transport.opendata.ch/v1/connections>'

params = {}
params['from'] = origin
params['to'] = destination
params['date'] = departure_date
params['time'] = departure_time

r = requests.get(url, params=params)
```
❌ `params['true'] = 'direct'`
❌ `params['direct'] = '1'`
❌ `params['connection'] = 'direct'`
❌ *The API already considers only direct connections by default*
✅ *There is no possibility to request only direct connections*
❌ `params['direct'] = 'true'`
❌ `params['direct'] = 1`

<details>
<summary>Explanation</summary>

> 💡 **[**Opendata Transport API documentation**](https://transport.opendata.ch/docs.html)**
❌ **Incorrect**, there's no parameter named 'true' in the API documentation.
❌ **Incorrect**, this parameter does not exist.
❌ `params['connection'] = 'direct'` is incorrect because there's no parameter named 'connection' in the API documentation.
❌ **Incorrect**, by default, the API shows all connections, not just direct 
✅ **Correct**, the API documentation does not state that you can filter for direct connections.
❌ **Incorrect**, the API documentation specifies that the value for the 'direct' parameter should be '1' and not 'true'.
❌ **Incorrect**, because the API documentation specifies that the value for the 'direct' parameter should be a string ('1') and not an integer (1).
</details>
---
## Question 5
How does TCP solve the Two Generals' Problem?
❌ TCP solves the Two Generals' Problem by implementing packet sequencing and acknowledgment of each packet. Each general (sender or receiver) knows for sure that their messages have been received and understood because TCP guarantees delivery of every packet without fail. If a packet is lost, TCP retransmits it until it is confirmed to be received, ensuring both sides are always synchronized.
✅ TCP does not solve the Two Generals' Problem because this problem is fundamentally unsolvable over an unreliable communication system where messages can be lost. However, TCP addresses some of the practical aspects of this problem by using acknowledgments (ACKs), sequence numbers, and timeouts to ensure reliable communication through an unreliable network.
❌ TCP solves the Two Generals' Problem by using its three-way handshake mechanism. This handshake involves the sender initiating the connection (SYN), the receiver acknowledging this request (SYN-ACK), and the sender acknowledging the receiver's acknowledgment (ACK).
❌ TCP does not solve the Two Generals' Problem because it is primarily concerned with speed rather than reliability of message delivery, and thus does not implement acknowledgment or retransmission mechanisms to ensure messages have been received.

<details>
<summary>Explanation</summary>

> 💡 **[TCP](/305c770201f94279bfd468d86c733ae6#d9f0456867ee4c45ac9fc43d26c2f9a2), [**Two Generals’ Problem**](https://www.youtube.com/watch?v=s8Wbt0b8bwY)**
The Two Generals' Problem is a thought experiment in computer science which demonstrates that no amount of message passing alone can guarantee that all participants in a network will agree on some fact. It's a fundamental issue in distributed systems and relates to the difficulty of achieving consensus.
❌ **Incorrect**, while TCP does implement packet sequencing and acknowledgment, it doesn't solve the Two Generals' Problem. The Two Generals' Problem is a consensus problem that cannot be solved if there's a chance that messages can be lost or delayed - conditions that can occur even when using TCP.
✅ **Correct**, The Two Generals' Problem is fundamentally unsolvable in an unreliable communication system, which includes any real-world network. While TCP does use acknowledgments (ACKs), sequence numbers, and timeouts to ensure reliable communication, it cannot guarantee consensus, which is the crux of the Two Generals' Problem.
❌ **Incorrect**, while TCP does use a three-way handshake mechanism to establish a connection, this doesn't solve the Two Generals' Problem. The problem is not about establishing a connection, but about reaching consensus over an unreliable network, which the three-way handshake does not address.
❌ **Incorrect**, TCP is actually designed with reliability as a primary concern, not speed. It does implement acknowledgment and retransmission mechanisms to ensure messages have been received. However, as mentioned before, these mechanisms do not solve the Two Generals' Problem because it's a consensus problem that is unsolvable in an unreliable network.
</details>
---

