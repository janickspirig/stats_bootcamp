---
title: "I know what a Domain Name System (DNS) is and why it is important"
notion_id: "96cf322b-e247-4e52-82fb-cb60bd1d6995"
notion_url: "https://www.notion.so/I-know-what-a-Domain-Name-System-DNS-is-and-why-it-is-important-96cf322be2474e5282fbcb60bd1d6995"
exported_at: "2025-12-13T22:28:06.680866+00:00"
---

# I know what a Domain Name System (DNS) is and why it is important

### Defintion
The Domain Name System (DNS) is an integral part of how the internet works. It's a protocol within the set of standards for how computers exchange data on various networks, known as TCP/IP. The purpose of DNS is to translate human-friendly domain names like '[google.com](http://google.com/)' into IP addresses like '172.217.4.78', which computers use to identify each other on the network.
> 🤯 **Without DNS, you may have to type something like '172.217.4.78' to reach 'google.com'.**
---
### Why is the DNS important?
### 1. Internet Navigation
The DNS enables users to navigate the web without having to remember complex numerical IP addresses. Instead, they can use easily rememberable website names or domain names.
### 2. Management of Domain Names
DNS makes it possible to assign domain names to groups of Internet resources and update them in a central place. This is beneficial for end users as it allows a familiar naming scheme that is easier to remember than numeric IP addresses.
### 3. Load Distribution
DNS helps distribute user requests to the right servers. For instance, companies with global operations might have servers in multiple locations worldwide. DNS helps direct user traffic to the nearest server, thereby providing a better user experience by reducing latency.
---
### Working of DNS:
### Key Components:
- **DNS Resolver:** Your Computer’s internet settings enable it to request domain lookups from DNS servers.
- **Root Server:** A root server is a DNS server that contains IP addresses of the TLDs.
- **TLD Server:** These servers store the address information for second-level domains (e.g., 'google' in '[www.google.com](http://www.google.com/)').
- **Authoritative DNS Server:** These servers have the definitive information about the domains under them.
### Process:
1. **You type '**[**google.com**](http://google.com/)**' into your web browser:** The request goes to the DNS resolver configured in your computer's network settings.
1. **The DNS Resolver asks a Root Server:** The root server directs your DNS resolver to a TLD (Top-Level Domain) server.
1. **TLD server points towards the authoritative DNS Server:** The specific TLD server (in this case, '.com') tells the DNS Resolver that the information for "[google.com](http://google.com/)" is in a certain authoritative server.
1. **Getting the IP address:** The authoritative DNS server provides the IP address for '[google.com](http://google.com/)'.
---
💡 **Note:** The process might seems complex, but in real world, the communication happens in milliseconds.
---


