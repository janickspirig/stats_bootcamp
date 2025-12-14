---
title: "Distributed Systems & Networks"
notion_id: "a8ef211d-76e2-485c-bffc-98356b0b47c4"
notion_url: "https://www.notion.so/Distributed-Systems-Networks-a8ef211d76e2485cbffc98356b0b47c4"
exported_at: "2025-12-13T22:55:58.235678+00:00"
---

# Distributed Systems & Networks

---
**APIs**
When I want to call an API out of my program code, it is important that I program in the same language as the server is implemented. True or False?

<details>
<summary>Solution</summary>

False
We can send the data to the server in JSON format and the server can also send the response data back in JSON format. Almost all programming languages know how to deal with data in JSON as it is a standardised format. Thus, I can program in Python and the server could be implemented in C#.
</details>
---
**APIs**
The API key which allows authentication and authorisation must be placed in the body of an HTTP request. True or False?

<details>
<summary>Solution</summary>

False
The API key must be placed in the header of the HTTP request.
</details>
---
**APIs**
Web APIs allow a digital entity such as a notebook or a roboter to access a remote server’s resources.

<details>
<summary>Solution</summary>

True
Humans look up the quickest route from A to B over Web browser. My business website does it in the source code by sending a request to the Google API.
</details>
---
**Application layer**
What are the three main things that happen on the Application layer?

<details>
<summary>Solution</summary>

Translation (text into binary)
Compression (Reduction of binary data)
Encryption / Decryption (entered e-banking password is encrypted)
</details>
---
**Transport layer**
Explain why sequence numbers are important.

<details>
<summary>Solution</summary>

A reques coming from the Application layer is split into different TCP segments that are sent to the remote server. Because of packet switching it can occurr that the segment that was sent as third arrives the remote server as the first one. The sequence number allows the remote server to put together the TCP segmetns in the right order again.
</details>
---
**Network layer**
Which of the following things are part of an IP packet?
- [ ] 1) Source MAC address
- [ ] 2) Host MAC address
- [ ] 3) TCP segment
- [ ] 4) HTTP request

<details>
<summary>Solution</summary>

3, 4
TCP segment is in the Payload of the IP packet
HTTP request is in the payload of the TCP segment
MAC address are only added on Data Link layer
</details>
---
**Network layer**
On the Network layer we have multiple different protocols that are used. True or False?

<details>
<summary>Solution</summary>

False
Narrow-waist of networking stack → only IP protocol on Network level
</details>
---
**Network layer**
If my device is not connect to the internet it does not have an IP address. True or False?

<details>
<summary>Solution</summary>

True
</details>
---
**Ports**
I send an HTTP request from Chrome and Safari, which of the following statements are True?
- [ ] 1) The source port number in both requests is the same.
- [ ] 2) The source port number in both requests is different.
- [ ] 3) The remote port number in both requests is the same
- [ ] 4) The remote port number in both requests is different.

<details>
<summary>Solution</summary>

2, 3
Source port tells my own computer from which application the request is coming from to wire the response back to the right place. The remote server does not care if request was sent by Chrome or Safari, it just cares about the source computer which sent the request.
</details>
---
**TCP vs. UDP**
UDP is less reliable as we don’t know if our request that we sent out over UDP was successfully received by the host. True or False?

<details>
<summary>Solution</summary>

True
</details>
---
**UCP**
When we stream a video from Netflix, the User Diagram Protcol (UDP) is used. True or False?

<details>
<summary>Solution</summary>

False
Video streaming uses a bunch of [other protocols](https://www.haivision.com/blog/all/video-encoding-basics-live-video-streaming-protocols/) such as RTMP, RTP or SRT.
</details>
---
**DNS**
When sending a DNS request, the TCP protocol is commonly used. True or False?

<details>
<summary>Solution</summary>

False, DNS goes normally over UDP.
</details>
---
**Data Link layer**
I can manually reset the MAC address of my notebook. True or False?

<details>
<summary>Solution</summary>

False
MAC addreses are burned into a device → permanent physical addressing
</details>
---
**Symmetric encryption**
Choose all correct answers from below:
- [ ] 1) In symmetric encryption, no public keys exist.
- [ ] 2) In symmetric encryption, messages are decrypted with one’s private key.
- [ ] 3) In symmetric encryption, a message is encrypted and decrypted with the same key.
- [ ] 4) In symmetric encryption, both counterparts use only one key.
- [ ] 5) Symmetric encryption can generally be considered as safe and is therefore widely adopted.

<details>
<summary>Solution</summary>

1, 3, 4
</details>
---
**Asymmetric encryption**
Choose all correct answers from below:
- [ ] 1) In asymmetric encryption, public keys are not shared.
- [ ] 2) In asymmetric encryption, private keys are not shared.
- [ ] 3) In asymmetric encryption, the message is encrypted with the public key of the counterpart.
- [ ] 4) In asymmetric encryption, the message is encrypted with the private key of the counterpart.
- [ ] 5) In asymmetric encryption, the private and public key depend mathematically on each other.
- [ ] 6) in asymmetric encryption, a message can only be decrypted with one’s public key.
- [ ] 7) in asymmetric encryption, a message can only be decrypted with one’s private key.

<details>
<summary>Solution</summary>

2, 3, 5, 7
</details>
---
**Diffie-Hellman key exchange**
Choose all correct answers from below:
- [ ] 1) In Diffie-Hellman, messages are decrypted with one’s private key.
- [ ] 2) In Diffie-Hellmann, both counterparts use the same key to encrypt end decrypt messages.
- [ ] 3) Diffie-Hellmann brings together the power of symmetric and asymmetric encryption. 
- [ ] 4) In Diffie-Hellmann, the hacker is not able to decrypt the message as he does not possess one of the public keys.

<details>
<summary>Solution</summary>

2, 3
</details>
---
**HTTP methods**
When I want to change my e-banking password, what kind of request is most likely sent to the e-banking server? 
- [ ] 1) PUT
- [ ] 2) POST
- [ ] 3) GET
- [ ] 4) DELETE

<details>
<summary>Solution</summary>

PUT
My e-banking user exists already. Thus, we modify an existing resource (my e-banking user) on the server, which we can achieve by sending a PUT request.
</details>
---
**HTTP methods**
When I create a new Notion account, what kind of request is most likely sent to the Notion server?
- [ ] 1) PUT
- [ ] 2) POST
- [ ] 3) GET
- [ ] 4) DELETE

<details>
<summary>Solution</summary>

POST
We want to create a new resource on the server (my new Notion account) which we can achieve by sending a POST request to the server.
</details>
---
**HTTP Response codes**
Explain for the response codes below what they mean. 
200 | 201 | 400 | 401 | 404 | 501 | 503

<details>
<summary>Solution</summary>

200 → OK
201 → Created
400 → Bad request
401 → Unauthorised
404 → Not found
501 → Internal server error
503 → Service unavailable
</details>
---
**HTTPS**
When sending an HTTPS request, which of the following things are encrypted?
- [ ] 1) Payload
- [ ] 2) Host IP address
- [ ] 3) HTTP method
- [ ] 4) Host port number
- [ ] 5) Source port number
- [ ] 6) Amount of data transferred

<details>
<summary>Solution</summary>

1, 3
If we would encrypt the other things it would be difficult to send the request to the right destination.
</details>
---
**HTTPS / TLS**
When sending my e-banking login to the bank’s sever, HTTPS makes sure that my password, i.e., the data is encrypted and secured whereas TLS makes sure that the connection to the server is reliable and secure.

<details>
<summary>Solution</summary>

True
HTTPS is responsible for encryption on application level while TLS is encryption on transport / connection level. They play together to ensure that the e-banking login gets transmitted securely to the bank’s server.
</details>
---
**TLS handshake**
We cannot use both at the same time, TLS/SSL and HTTPS. True or False?

<details>
<summary>Solution</summary>

False
We use HTTPS on application level and TLS/SSL on transport level. 
First we establish a reliable connection with the remote server by performing a TLS/SSL handshake. Then we exchange data with the remote server securely over HTTPS.
</details>
---
**TLS handshake**
Explain what the role of the Certificate Authority (CA) is during the TLS/SSL handshake.

<details>
<summary>Solution</summary>

The CS checks if the remote server actually is the person / party which it pretends to be. Because the server could send to us any kind of certificate, also a fake one, so before we send our e-banking password to this server we must check with the CA that this actually is the UBS e-banking server.
</details>
---

