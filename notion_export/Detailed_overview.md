---
title: "Detailed overview"
notion_id: "3784667b-a797-4f05-aaee-bb0acac5fb3a"
notion_url: "https://www.notion.so/Detailed-overview-3784667ba7974f05aaeebb0acac5fb3a"
exported_at: "2025-12-14T01:06:36.386545+00:00"
---

# Detailed overview

---
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/eab6158a-1be0-494c-b474-8e2318fc3919/Screenshot_2022-06-24_at_12.58.02.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UTMHJ2EA%2F20251214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251214T010632Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJIMEYCIQDdbxEQZ02Em2%2FkjauKUNCal2Ay9wAvQLn%2B47CDSXZxkgIhAMrUBlgvr0LsmTNHrrhYAPQZteTk715oWruUygicSXxiKv8DCCoQABoMNjM3NDIzMTgzODA1IgxEySgXTiuvgOkapHIq3AOmnlegI%2BpHaHh1NFck6M47KIB6v8ugMN80wIoLOKApS42O7hLF7SgixT54yWWDWDRiAy49mWRPJ%2BpUqouuy9xGrt1wCWA8iL6aH4bdYzombVIw%2B3fDTEYsC3kIaoftgO1VORqQMvIgmpEo0%2BWRI2nNUjR8vHMaQARHJ21DHpsGYbfDVvzsK5rlclbYd%2FqtaN%2BfNm50bZ%2F9cdUefPfNVXGkxXojcTFyWuG6Cge%2Fl4JYnYDjfaSKNm1UPcMd%2Bg%2BqEyreHhkJf4HbrjE36eNWbTyYhRJh9z47EA4ETO7d%2FouM7O7o9rbWc4HysTS37fAQK0wcRJu6BJrhuwgU4mZhArVBd7E6qkSZvUgSAO9s1He0jRMJX0ltXTE5ojTjcMsMOk2%2BHcDJo0wi3wCl5n6MgUELpMetPHPDdaEUUWI2Q4LvmU7%2FsgaAp52qvljLAF6Bf%2B6oIBpUiqnqUFuD6Io4Oez4k1iWB52%2Fu6EzR2xz3xWsy4EwRZbKhVYg%2F5cHVswOh8p1P20PbqGRgTVN%2B145yK2L1Y%2Bg1%2F9NfumdAhZVdi8JnuXY6IcLfR500Gy%2BPjhfQ81b1f%2BJUb9RS1ZIraFh7YchGP0JxhEYS7%2F2zzlZWZSkwDY%2BvPEeuL6x%2F0GzFDCFlvjJBjqkASv0aNyYqeiEL6RlIPLZxr5tWYT01Irx1V6uh%2Fo51b3jQ4%2BbL49f9AoH4lXzh%2FlbN2hnS6qxTvWSFTkbd1%2B4MIQnJKCcwDRBMh6TShH1z3S0L6TuQQ9Egb3aKoXyE%2BqRzbDwzxQ9jlQ4LyiMxkm1a5BtTfqtQiMHD0B4JCebWknPKKZHB21g6iKF5XFkBCO0NqjN3BiHidvuQOzl8CyJbKwlO3Jv&X-Amz-Signature=727cb08f3dc70e0665eb97ccc545592d5d2dc1ecd8c340fc52bbb05630d8f4d6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
<details>
<summary>Explanation</summary>

**Introduction**
The networking stack, also known as the network protocol stack, is essentially a set of rules or protocols that govern the way information (like a message on Facebook) moves from one computer system to another over the internet.
**Motivation**
Imagine you want to say "Hi!" to a friend on Facebook. You click on send. But what happens afterward? How does your message reach your friend who uses an Apple device, while you're on Windows?
In the virtual world, we need a system that allows humans to communicate through computers - where computers become intermediaries that deliver messages. That's where the networking stack comes in. The networking stack ensures connectivity among different hardware, operating systems, and software. It achieves this through **standardization** and **separation of concerns**.
**Standardization** is important to set up a unified and common process which all systems can follow to ensure effective communication and data exchange. Suppose that the standardization is like the "language" that all computers use to "communicate" with each other.
**Separation of concerns** refers to the idea that each part of a system should take care of a specific function and should not be concerned with the tasks of any other part of the system. Each layer in the networking stack has its own purpose and only needs to focus on that.
</details>
---
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/36153664-118f-4073-803f-a81ad72fe01a/Screenshot_2022-06-24_at_12.58.19.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UTMHJ2EA%2F20251214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251214T010632Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJIMEYCIQDdbxEQZ02Em2%2FkjauKUNCal2Ay9wAvQLn%2B47CDSXZxkgIhAMrUBlgvr0LsmTNHrrhYAPQZteTk715oWruUygicSXxiKv8DCCoQABoMNjM3NDIzMTgzODA1IgxEySgXTiuvgOkapHIq3AOmnlegI%2BpHaHh1NFck6M47KIB6v8ugMN80wIoLOKApS42O7hLF7SgixT54yWWDWDRiAy49mWRPJ%2BpUqouuy9xGrt1wCWA8iL6aH4bdYzombVIw%2B3fDTEYsC3kIaoftgO1VORqQMvIgmpEo0%2BWRI2nNUjR8vHMaQARHJ21DHpsGYbfDVvzsK5rlclbYd%2FqtaN%2BfNm50bZ%2F9cdUefPfNVXGkxXojcTFyWuG6Cge%2Fl4JYnYDjfaSKNm1UPcMd%2Bg%2BqEyreHhkJf4HbrjE36eNWbTyYhRJh9z47EA4ETO7d%2FouM7O7o9rbWc4HysTS37fAQK0wcRJu6BJrhuwgU4mZhArVBd7E6qkSZvUgSAO9s1He0jRMJX0ltXTE5ojTjcMsMOk2%2BHcDJo0wi3wCl5n6MgUELpMetPHPDdaEUUWI2Q4LvmU7%2FsgaAp52qvljLAF6Bf%2B6oIBpUiqnqUFuD6Io4Oez4k1iWB52%2Fu6EzR2xz3xWsy4EwRZbKhVYg%2F5cHVswOh8p1P20PbqGRgTVN%2B145yK2L1Y%2Bg1%2F9NfumdAhZVdi8JnuXY6IcLfR500Gy%2BPjhfQ81b1f%2BJUb9RS1ZIraFh7YchGP0JxhEYS7%2F2zzlZWZSkwDY%2BvPEeuL6x%2F0GzFDCFlvjJBjqkASv0aNyYqeiEL6RlIPLZxr5tWYT01Irx1V6uh%2Fo51b3jQ4%2BbL49f9AoH4lXzh%2FlbN2hnS6qxTvWSFTkbd1%2B4MIQnJKCcwDRBMh6TShH1z3S0L6TuQQ9Egb3aKoXyE%2BqRzbDwzxQ9jlQ4LyiMxkm1a5BtTfqtQiMHD0B4JCebWknPKKZHB21g6iKF5XFkBCO0NqjN3BiHidvuQOzl8CyJbKwlO3Jv&X-Amz-Signature=1deeb1aa8fbde6c79ca864ae3a0f959280c85e0cdeae292dab3fe1fba46df461&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
<details>
<summary>Explanation</summary>

The networking stack, commonly referred to as the internet protocol suite, is a set of communication protocols used for the internet and similar networks. This concept can be visualized as a stack of layers, where each layer provides services to the layers above it and uses the services of the layers below it. Let's break down the different layers.
**Application Layer**
This is the topmost layer in the networking stack, designed to interact directly with the user's applications, such as email (SMTP), file transfer (FTP), and web surfing (HTTP). Here, the 'Data' is in a format understandable by these applications.
**Transport Layer**
This layer is responsible for providing end-to-end or host-to-host communication services for applications. It can handle flow control, reliability, and multiplexing. Transport Layer 'Segments' data into smaller units for easier transmission.
**Network Layer**
This layer is about delivering packets from the source computer to the destination computer. It's responsible for routing packets, which is the process of selecting a path through the network to send these 'Packets'.
**Data Link Layer**
This layer is responsible for transferring data between network nodes on the same network segment. In the Data-link layer, data packets are encoded into 'Frames' for transmission.
**Physical Layer**
The Physical Layer transmits raw bit stream over the physical medium - like cables or radio waves. It's responsible for turning 'Frames' into raw 'Bits' and vice sends the 'Bits' over the network hardware.
*Note:*
A message from the application layer on the sender-side travels down the stack to the physical layer, gets transmitted over the network medium, and then travels up the stack on the receiver-side to be processed by the proper application.
Here is a simple illustration:
Sender-side:
```plain text
Application Layer: "Hello"
    ↓ (into segments)
Transport Layer: "He","ll","o"
    ↓ (into packets)
Network Layer: Packet 1, Packet 2, Packet 3
    ↓ (into frames)
Data Link Layer: Frame 1, Frame 2, Frame 3
    ↓ (into bits)
Physical Layer: 10010101, 11010101, 11101011
```
After being sent over the network, the bits are processed in reverse order on the receiver-side.
This layered approach provides a way to divide the complex process of communicating over a network into more manageable parts, each with its own specialized job.
</details>
---
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/30340e7e-d053-4447-a5b4-1021abf03d13/Screenshot_2022-06-24_at_12.58.30.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UTMHJ2EA%2F20251214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251214T010632Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJIMEYCIQDdbxEQZ02Em2%2FkjauKUNCal2Ay9wAvQLn%2B47CDSXZxkgIhAMrUBlgvr0LsmTNHrrhYAPQZteTk715oWruUygicSXxiKv8DCCoQABoMNjM3NDIzMTgzODA1IgxEySgXTiuvgOkapHIq3AOmnlegI%2BpHaHh1NFck6M47KIB6v8ugMN80wIoLOKApS42O7hLF7SgixT54yWWDWDRiAy49mWRPJ%2BpUqouuy9xGrt1wCWA8iL6aH4bdYzombVIw%2B3fDTEYsC3kIaoftgO1VORqQMvIgmpEo0%2BWRI2nNUjR8vHMaQARHJ21DHpsGYbfDVvzsK5rlclbYd%2FqtaN%2BfNm50bZ%2F9cdUefPfNVXGkxXojcTFyWuG6Cge%2Fl4JYnYDjfaSKNm1UPcMd%2Bg%2BqEyreHhkJf4HbrjE36eNWbTyYhRJh9z47EA4ETO7d%2FouM7O7o9rbWc4HysTS37fAQK0wcRJu6BJrhuwgU4mZhArVBd7E6qkSZvUgSAO9s1He0jRMJX0ltXTE5ojTjcMsMOk2%2BHcDJo0wi3wCl5n6MgUELpMetPHPDdaEUUWI2Q4LvmU7%2FsgaAp52qvljLAF6Bf%2B6oIBpUiqnqUFuD6Io4Oez4k1iWB52%2Fu6EzR2xz3xWsy4EwRZbKhVYg%2F5cHVswOh8p1P20PbqGRgTVN%2B145yK2L1Y%2Bg1%2F9NfumdAhZVdi8JnuXY6IcLfR500Gy%2BPjhfQ81b1f%2BJUb9RS1ZIraFh7YchGP0JxhEYS7%2F2zzlZWZSkwDY%2BvPEeuL6x%2F0GzFDCFlvjJBjqkASv0aNyYqeiEL6RlIPLZxr5tWYT01Irx1V6uh%2Fo51b3jQ4%2BbL49f9AoH4lXzh%2FlbN2hnS6qxTvWSFTkbd1%2B4MIQnJKCcwDRBMh6TShH1z3S0L6TuQQ9Egb3aKoXyE%2BqRzbDwzxQ9jlQ4LyiMxkm1a5BtTfqtQiMHD0B4JCebWknPKKZHB21g6iKF5XFkBCO0NqjN3BiHidvuQOzl8CyJbKwlO3Jv&X-Amz-Signature=343efe9daa1bb5c0993bfb4965a03701ebd8fd78f0ac3b877bade6ee883e7bfa&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
<details>
<summary>Explanation</summary>

When you send a message on Facebook, here's what happens:
1. You type your message and click send. This is the **Application Layer** at work.
1. The message is translated into a format that can be sent over the internet. This is the **Application Layer** at work.
1. A 'conversation' is set up between your device and your friend's device. This is the **Application Layer** at work.
1. The message is broken down into smaller pieces, or 'packets', and each packet is given a label with the destination address. This is the **Transport Layer** at work.
1. The best path for each packet to take is determined. This is the **Network Layer** at work.
1. The packets are sent from your device to your friend's device. This is the **Data Link Layer** at work.
1. The physical connection between your device and your friend's device is used to transmit the packets. This is the **Physical Layer** at work.
So, the networking stack allows you to send a message on Facebook as if you were talking to your friend in person, with your computers acting as the 'middle-men' to deliver the message.
</details>
---
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/56270223-b816-45d8-a313-124e94b91df2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UTMHJ2EA%2F20251214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251214T010632Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJIMEYCIQDdbxEQZ02Em2%2FkjauKUNCal2Ay9wAvQLn%2B47CDSXZxkgIhAMrUBlgvr0LsmTNHrrhYAPQZteTk715oWruUygicSXxiKv8DCCoQABoMNjM3NDIzMTgzODA1IgxEySgXTiuvgOkapHIq3AOmnlegI%2BpHaHh1NFck6M47KIB6v8ugMN80wIoLOKApS42O7hLF7SgixT54yWWDWDRiAy49mWRPJ%2BpUqouuy9xGrt1wCWA8iL6aH4bdYzombVIw%2B3fDTEYsC3kIaoftgO1VORqQMvIgmpEo0%2BWRI2nNUjR8vHMaQARHJ21DHpsGYbfDVvzsK5rlclbYd%2FqtaN%2BfNm50bZ%2F9cdUefPfNVXGkxXojcTFyWuG6Cge%2Fl4JYnYDjfaSKNm1UPcMd%2Bg%2BqEyreHhkJf4HbrjE36eNWbTyYhRJh9z47EA4ETO7d%2FouM7O7o9rbWc4HysTS37fAQK0wcRJu6BJrhuwgU4mZhArVBd7E6qkSZvUgSAO9s1He0jRMJX0ltXTE5ojTjcMsMOk2%2BHcDJo0wi3wCl5n6MgUELpMetPHPDdaEUUWI2Q4LvmU7%2FsgaAp52qvljLAF6Bf%2B6oIBpUiqnqUFuD6Io4Oez4k1iWB52%2Fu6EzR2xz3xWsy4EwRZbKhVYg%2F5cHVswOh8p1P20PbqGRgTVN%2B145yK2L1Y%2Bg1%2F9NfumdAhZVdi8JnuXY6IcLfR500Gy%2BPjhfQ81b1f%2BJUb9RS1ZIraFh7YchGP0JxhEYS7%2F2zzlZWZSkwDY%2BvPEeuL6x%2F0GzFDCFlvjJBjqkASv0aNyYqeiEL6RlIPLZxr5tWYT01Irx1V6uh%2Fo51b3jQ4%2BbL49f9AoH4lXzh%2FlbN2hnS6qxTvWSFTkbd1%2B4MIQnJKCcwDRBMh6TShH1z3S0L6TuQQ9Egb3aKoXyE%2BqRzbDwzxQ9jlQ4LyiMxkm1a5BtTfqtQiMHD0B4JCebWknPKKZHB21g6iKF5XFkBCO0NqjN3BiHidvuQOzl8CyJbKwlO3Jv&X-Amz-Signature=c1285db4e45bfd82f6777ffe3e4015e014847d8345afaaba50282a34c0185bb3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
<details>
<summary>Explanation</summary>

The **Application layer** is the topmost layer in the networking stack where network applications like web browsers, email clients or file transfer tools work.
- These applications use **protocols** like HTTP for web browsing, SMTP/IMAP for sending emails, and FTP for transferring files. A protocol is simply a set of rules that define how data is formatted and processed in a communication system.
- This layer is also in charge of **session management**, which can be thought of as a system in which even if you are using several applications at the same time, your computer can distinguish where the data from each application goes or comes from.
- Messages composed of usual **characters and numbers are converted into binary data** (0s and 1s) so that computers can process them. For example, the HTTP request `GET /postbox HTTP/1.1` might be turned into those binary digits.
- **Compression** takes place in order to reduce the size of binary data, which is especially important for services like Netflix that deal with large amounts of data.
- For security reasons, the data must often be **encrypted** (made unreadable) during transmission, then decrypted (made readable again) by only the intended recipient. This ensures nobody else can read sensitive information if they intercept the data.
*Example*: imagine you're ordering pizza using your phone. The phone (or the app in it) represents the application layer. The language you use to order the pizza (Italian, English, etc.) corresponds to the protocol. And the pizza delivery (session) initiated by your order is managed completely, regardless of whether you're also navigating through maps or browsing the web on your phone.
</details>
---
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/c448eec4-4faa-4eda-aec9-8fae356d46f5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UTMHJ2EA%2F20251214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251214T010632Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJIMEYCIQDdbxEQZ02Em2%2FkjauKUNCal2Ay9wAvQLn%2B47CDSXZxkgIhAMrUBlgvr0LsmTNHrrhYAPQZteTk715oWruUygicSXxiKv8DCCoQABoMNjM3NDIzMTgzODA1IgxEySgXTiuvgOkapHIq3AOmnlegI%2BpHaHh1NFck6M47KIB6v8ugMN80wIoLOKApS42O7hLF7SgixT54yWWDWDRiAy49mWRPJ%2BpUqouuy9xGrt1wCWA8iL6aH4bdYzombVIw%2B3fDTEYsC3kIaoftgO1VORqQMvIgmpEo0%2BWRI2nNUjR8vHMaQARHJ21DHpsGYbfDVvzsK5rlclbYd%2FqtaN%2BfNm50bZ%2F9cdUefPfNVXGkxXojcTFyWuG6Cge%2Fl4JYnYDjfaSKNm1UPcMd%2Bg%2BqEyreHhkJf4HbrjE36eNWbTyYhRJh9z47EA4ETO7d%2FouM7O7o9rbWc4HysTS37fAQK0wcRJu6BJrhuwgU4mZhArVBd7E6qkSZvUgSAO9s1He0jRMJX0ltXTE5ojTjcMsMOk2%2BHcDJo0wi3wCl5n6MgUELpMetPHPDdaEUUWI2Q4LvmU7%2FsgaAp52qvljLAF6Bf%2B6oIBpUiqnqUFuD6Io4Oez4k1iWB52%2Fu6EzR2xz3xWsy4EwRZbKhVYg%2F5cHVswOh8p1P20PbqGRgTVN%2B145yK2L1Y%2Bg1%2F9NfumdAhZVdi8JnuXY6IcLfR500Gy%2BPjhfQ81b1f%2BJUb9RS1ZIraFh7YchGP0JxhEYS7%2F2zzlZWZSkwDY%2BvPEeuL6x%2F0GzFDCFlvjJBjqkASv0aNyYqeiEL6RlIPLZxr5tWYT01Irx1V6uh%2Fo51b3jQ4%2BbL49f9AoH4lXzh%2FlbN2hnS6qxTvWSFTkbd1%2B4MIQnJKCcwDRBMh6TShH1z3S0L6TuQQ9Egb3aKoXyE%2BqRzbDwzxQ9jlQ4LyiMxkm1a5BtTfqtQiMHD0B4JCebWknPKKZHB21g6iKF5XFkBCO0NqjN3BiHidvuQOzl8CyJbKwlO3Jv&X-Amz-Signature=292a5061029b68ce1590ccef6c4f34a1df13cf55635cda34f83d4e5a3f8d084b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
---
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/e4ee47d4-55e2-47f2-b3d0-adb9c0811cf4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UTMHJ2EA%2F20251214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251214T010632Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJIMEYCIQDdbxEQZ02Em2%2FkjauKUNCal2Ay9wAvQLn%2B47CDSXZxkgIhAMrUBlgvr0LsmTNHrrhYAPQZteTk715oWruUygicSXxiKv8DCCoQABoMNjM3NDIzMTgzODA1IgxEySgXTiuvgOkapHIq3AOmnlegI%2BpHaHh1NFck6M47KIB6v8ugMN80wIoLOKApS42O7hLF7SgixT54yWWDWDRiAy49mWRPJ%2BpUqouuy9xGrt1wCWA8iL6aH4bdYzombVIw%2B3fDTEYsC3kIaoftgO1VORqQMvIgmpEo0%2BWRI2nNUjR8vHMaQARHJ21DHpsGYbfDVvzsK5rlclbYd%2FqtaN%2BfNm50bZ%2F9cdUefPfNVXGkxXojcTFyWuG6Cge%2Fl4JYnYDjfaSKNm1UPcMd%2Bg%2BqEyreHhkJf4HbrjE36eNWbTyYhRJh9z47EA4ETO7d%2FouM7O7o9rbWc4HysTS37fAQK0wcRJu6BJrhuwgU4mZhArVBd7E6qkSZvUgSAO9s1He0jRMJX0ltXTE5ojTjcMsMOk2%2BHcDJo0wi3wCl5n6MgUELpMetPHPDdaEUUWI2Q4LvmU7%2FsgaAp52qvljLAF6Bf%2B6oIBpUiqnqUFuD6Io4Oez4k1iWB52%2Fu6EzR2xz3xWsy4EwRZbKhVYg%2F5cHVswOh8p1P20PbqGRgTVN%2B145yK2L1Y%2Bg1%2F9NfumdAhZVdi8JnuXY6IcLfR500Gy%2BPjhfQ81b1f%2BJUb9RS1ZIraFh7YchGP0JxhEYS7%2F2zzlZWZSkwDY%2BvPEeuL6x%2F0GzFDCFlvjJBjqkASv0aNyYqeiEL6RlIPLZxr5tWYT01Irx1V6uh%2Fo51b3jQ4%2BbL49f9AoH4lXzh%2FlbN2hnS6qxTvWSFTkbd1%2B4MIQnJKCcwDRBMh6TShH1z3S0L6TuQQ9Egb3aKoXyE%2BqRzbDwzxQ9jlQ4LyiMxkm1a5BtTfqtQiMHD0B4JCebWknPKKZHB21g6iKF5XFkBCO0NqjN3BiHidvuQOzl8CyJbKwlO3Jv&X-Amz-Signature=9a7bfa64899cd72fd6c88559479e39cafc77f815e387b3b3e88c562a4828281d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
<details>
<summary>Explanation</summary>

The **Transport layer** ensures the reliable arrival of messages and provides error-checking mechanisms. It regulates the size, sequencing and ultimately the delivery of data between systems and hosts.
- **Port Number**: It's like a door in a system through which the protocols communicate; certain services are attached to certain port numbers. Some examples are DNS which uses port number 53, and HTTPS using port number 443.
- **Segmentation**: Think of this as chopping up a long letter into several postcards. Each postcard (segment) holds a part of the whole message, making it easier to send across a network.
- **Flow Control**: This ensures the sender is not overwhelming the receiver with too much data at once. It's like having a conversation where you pause to let the other person understand and respond.
- **Error Control**: To guarantee the data is correctly delivered from sender to receiver, an Acknowledgement (ACK) is sent back to the sender by the receiver to confirm it got the data. If the sender does not receive an ACK, it understands that an error occurred and will send the data again.
- **TCP and UDP**: They are types of transport layer protocols. TCP is connection-oriented (like a phone call, it establishes a connection, ensures data is received, then ends the connection). UDP on the other hand is connectionless (like mailing a letter, you send the letter but don't know if it was received).
- **Source Port and Destination Port**: Source port is the port used by the sending computer, and the destination port is used by the receiving computer. This is like sending physical mail where you have a sender's address and receiver's address.
- **TCP Segment**: A TCP segment is a block of data which is transported over a TCP connection. Each segment is assigned a unique sequence number, this is to ensure the correct order of the segments when the data is reconstructed at the destination.
Below is an example of a TCP segment:
```plain text
Structure of a TCP segment

Segments:               Head            Source Port     Dest. Port     Data
1                        ABC              12345             443        Hello
2                        DEF              12346             443        World
```
In this case, we are sending the message "Hello World" from our system (with source ports 12345 and 12346) to a server (destination port 443 denoting HTTPS). "ABC" and "DEF" are headers and "Hello" and "World" are the data being sent. The Head contains information such as the sequence number, acknowledgement number, flags etc. that are used for controlling the transmission.
</details>
---
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/08a56604-fb38-4411-a69d-4e76dc201f6d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UTMHJ2EA%2F20251214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251214T010632Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJIMEYCIQDdbxEQZ02Em2%2FkjauKUNCal2Ay9wAvQLn%2B47CDSXZxkgIhAMrUBlgvr0LsmTNHrrhYAPQZteTk715oWruUygicSXxiKv8DCCoQABoMNjM3NDIzMTgzODA1IgxEySgXTiuvgOkapHIq3AOmnlegI%2BpHaHh1NFck6M47KIB6v8ugMN80wIoLOKApS42O7hLF7SgixT54yWWDWDRiAy49mWRPJ%2BpUqouuy9xGrt1wCWA8iL6aH4bdYzombVIw%2B3fDTEYsC3kIaoftgO1VORqQMvIgmpEo0%2BWRI2nNUjR8vHMaQARHJ21DHpsGYbfDVvzsK5rlclbYd%2FqtaN%2BfNm50bZ%2F9cdUefPfNVXGkxXojcTFyWuG6Cge%2Fl4JYnYDjfaSKNm1UPcMd%2Bg%2BqEyreHhkJf4HbrjE36eNWbTyYhRJh9z47EA4ETO7d%2FouM7O7o9rbWc4HysTS37fAQK0wcRJu6BJrhuwgU4mZhArVBd7E6qkSZvUgSAO9s1He0jRMJX0ltXTE5ojTjcMsMOk2%2BHcDJo0wi3wCl5n6MgUELpMetPHPDdaEUUWI2Q4LvmU7%2FsgaAp52qvljLAF6Bf%2B6oIBpUiqnqUFuD6Io4Oez4k1iWB52%2Fu6EzR2xz3xWsy4EwRZbKhVYg%2F5cHVswOh8p1P20PbqGRgTVN%2B145yK2L1Y%2Bg1%2F9NfumdAhZVdi8JnuXY6IcLfR500Gy%2BPjhfQ81b1f%2BJUb9RS1ZIraFh7YchGP0JxhEYS7%2F2zzlZWZSkwDY%2BvPEeuL6x%2F0GzFDCFlvjJBjqkASv0aNyYqeiEL6RlIPLZxr5tWYT01Irx1V6uh%2Fo51b3jQ4%2BbL49f9AoH4lXzh%2FlbN2hnS6qxTvWSFTkbd1%2B4MIQnJKCcwDRBMh6TShH1z3S0L6TuQQ9Egb3aKoXyE%2BqRzbDwzxQ9jlQ4LyiMxkm1a5BtTfqtQiMHD0B4JCebWknPKKZHB21g6iKF5XFkBCO0NqjN3BiHidvuQOzl8CyJbKwlO3Jv&X-Amz-Signature=5b881dbe37f46dc6896899d8aa83d76421557ef1375fc341f8182c9c6f6e9aaa&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
<details>
<summary>Explanation</summary>

The **Network layer** is where packets are moved from the source to the destination. It is important to understand the terms used at this layer:
- **Logical addressing**: This assigns the sender and receiver an IP address, which can change, to form an IP packet. It's like giving each device on a network its own post office box number.
- **Routing**: This involves moving data packets from the source to the destination and directing them to the correct client within a network, based on their IP address. It's similar to how a postal worker delivers mail to the right address.
- **Path determination**: Path determination means picking the most efficient route for data delivery. It's like using a GPS to select the fastest route when driving.
- **Narrow-waist of the networking stack**: At the Network layer, there is only the IP protocol - a standard set of rules for sending and receiving data through the internet. It's like how all letters in a country need to be sent using the country's standard postal system.
The Transport layer provides *segments* to the Network layer. These segments are transformed into IP packets at the Network layer.
</details>
---
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/03695b43-83b2-477a-b836-7c617d9e7c83/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UTMHJ2EA%2F20251214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251214T010632Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJIMEYCIQDdbxEQZ02Em2%2FkjauKUNCal2Ay9wAvQLn%2B47CDSXZxkgIhAMrUBlgvr0LsmTNHrrhYAPQZteTk715oWruUygicSXxiKv8DCCoQABoMNjM3NDIzMTgzODA1IgxEySgXTiuvgOkapHIq3AOmnlegI%2BpHaHh1NFck6M47KIB6v8ugMN80wIoLOKApS42O7hLF7SgixT54yWWDWDRiAy49mWRPJ%2BpUqouuy9xGrt1wCWA8iL6aH4bdYzombVIw%2B3fDTEYsC3kIaoftgO1VORqQMvIgmpEo0%2BWRI2nNUjR8vHMaQARHJ21DHpsGYbfDVvzsK5rlclbYd%2FqtaN%2BfNm50bZ%2F9cdUefPfNVXGkxXojcTFyWuG6Cge%2Fl4JYnYDjfaSKNm1UPcMd%2Bg%2BqEyreHhkJf4HbrjE36eNWbTyYhRJh9z47EA4ETO7d%2FouM7O7o9rbWc4HysTS37fAQK0wcRJu6BJrhuwgU4mZhArVBd7E6qkSZvUgSAO9s1He0jRMJX0ltXTE5ojTjcMsMOk2%2BHcDJo0wi3wCl5n6MgUELpMetPHPDdaEUUWI2Q4LvmU7%2FsgaAp52qvljLAF6Bf%2B6oIBpUiqnqUFuD6Io4Oez4k1iWB52%2Fu6EzR2xz3xWsy4EwRZbKhVYg%2F5cHVswOh8p1P20PbqGRgTVN%2B145yK2L1Y%2Bg1%2F9NfumdAhZVdi8JnuXY6IcLfR500Gy%2BPjhfQ81b1f%2BJUb9RS1ZIraFh7YchGP0JxhEYS7%2F2zzlZWZSkwDY%2BvPEeuL6x%2F0GzFDCFlvjJBjqkASv0aNyYqeiEL6RlIPLZxr5tWYT01Irx1V6uh%2Fo51b3jQ4%2BbL49f9AoH4lXzh%2FlbN2hnS6qxTvWSFTkbd1%2B4MIQnJKCcwDRBMh6TShH1z3S0L6TuQQ9Egb3aKoXyE%2BqRzbDwzxQ9jlQ4LyiMxkm1a5BtTfqtQiMHD0B4JCebWknPKKZHB21g6iKF5XFkBCO0NqjN3BiHidvuQOzl8CyJbKwlO3Jv&X-Amz-Signature=068e74d98e54f150b9c0a81611f810fc8b4ba47fa603e3ff478cae4314735ff3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
<details>
<summary>Explanation</summary>

The term 'narrow-waist' refers to the standardized use of the IP protocol at the Network layer. With many options for protocols both above (at Transport and Application layers) and below (at link and physical layers), the consistent use of IP at the Network layer simplifies the process and allows for easier communication and growth of the Internet.
The IP protocol has two versions:
- **IPv4** like `192.168.1.1`, is the most commonly used version.
- **IPv6** like `fe80::d4a8:6435:d2d8:d9f3b11`, provides a higher capability for device support and compatibility, particularly with mobile networks. It was developed because the number of devices connected to the Internet quickly outpaced the number of unique addresses possible with IPv4.
</details>
---
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/c0e6a302-42a3-4062-bc54-1ae4cbf81a83/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UTMHJ2EA%2F20251214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251214T010632Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJIMEYCIQDdbxEQZ02Em2%2FkjauKUNCal2Ay9wAvQLn%2B47CDSXZxkgIhAMrUBlgvr0LsmTNHrrhYAPQZteTk715oWruUygicSXxiKv8DCCoQABoMNjM3NDIzMTgzODA1IgxEySgXTiuvgOkapHIq3AOmnlegI%2BpHaHh1NFck6M47KIB6v8ugMN80wIoLOKApS42O7hLF7SgixT54yWWDWDRiAy49mWRPJ%2BpUqouuy9xGrt1wCWA8iL6aH4bdYzombVIw%2B3fDTEYsC3kIaoftgO1VORqQMvIgmpEo0%2BWRI2nNUjR8vHMaQARHJ21DHpsGYbfDVvzsK5rlclbYd%2FqtaN%2BfNm50bZ%2F9cdUefPfNVXGkxXojcTFyWuG6Cge%2Fl4JYnYDjfaSKNm1UPcMd%2Bg%2BqEyreHhkJf4HbrjE36eNWbTyYhRJh9z47EA4ETO7d%2FouM7O7o9rbWc4HysTS37fAQK0wcRJu6BJrhuwgU4mZhArVBd7E6qkSZvUgSAO9s1He0jRMJX0ltXTE5ojTjcMsMOk2%2BHcDJo0wi3wCl5n6MgUELpMetPHPDdaEUUWI2Q4LvmU7%2FsgaAp52qvljLAF6Bf%2B6oIBpUiqnqUFuD6Io4Oez4k1iWB52%2Fu6EzR2xz3xWsy4EwRZbKhVYg%2F5cHVswOh8p1P20PbqGRgTVN%2B145yK2L1Y%2Bg1%2F9NfumdAhZVdi8JnuXY6IcLfR500Gy%2BPjhfQ81b1f%2BJUb9RS1ZIraFh7YchGP0JxhEYS7%2F2zzlZWZSkwDY%2BvPEeuL6x%2F0GzFDCFlvjJBjqkASv0aNyYqeiEL6RlIPLZxr5tWYT01Irx1V6uh%2Fo51b3jQ4%2BbL49f9AoH4lXzh%2FlbN2hnS6qxTvWSFTkbd1%2B4MIQnJKCcwDRBMh6TShH1z3S0L6TuQQ9Egb3aKoXyE%2BqRzbDwzxQ9jlQ4LyiMxkm1a5BtTfqtQiMHD0B4JCebWknPKKZHB21g6iKF5XFkBCO0NqjN3BiHidvuQOzl8CyJbKwlO3Jv&X-Amz-Signature=454b1a23e42d71ff8c50201297984da4185e12f7ea49230243300240ec79d6d1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
<details>
<summary>Explanation</summary>

The **Data Link Layer **handles the physical transmission of data over the network. It's a kind of 'courier' service in the system. The Data Link layer takes IP (Internet Protocol) packets from the Network layer and prepares them for the delivery across the network. It turns these packets into Frames.
- **Physical Addressing**: It uses MAC (Media Access Control) addresses to identify the sender and receiver. MAC addresses are unique identifiers assigned to network interfaces.
- **ARP (Address Resolution Protocol)**: If the MAC address of the receiver is not known, the Data Link layer uses ARP to find it. ARP maps an IP address to its corresponding MAC address.
- **Coordination of Communication**: The Data Link layer ensures that two devices do not send data at the same time to avoid collision. For example, if you and your brother are using the same network, you both can't send a frame at the same time.
- **Forming Frames**: The Data Link layer takes the IP packets from the Network layer and encapsulates them into a frame for transmission.
Here's a simple analogy: Think of the Data Link layer as a post office. The MAC address is like the home address, the ARP is like the post office's system for finding addresses, and the frame is like the envelope that the letter (data) is put into.
</details>
---
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/5084c73b-fa1b-4fa9-bb85-3a7b5da3be6e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UTMHJ2EA%2F20251214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251214T010632Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJIMEYCIQDdbxEQZ02Em2%2FkjauKUNCal2Ay9wAvQLn%2B47CDSXZxkgIhAMrUBlgvr0LsmTNHrrhYAPQZteTk715oWruUygicSXxiKv8DCCoQABoMNjM3NDIzMTgzODA1IgxEySgXTiuvgOkapHIq3AOmnlegI%2BpHaHh1NFck6M47KIB6v8ugMN80wIoLOKApS42O7hLF7SgixT54yWWDWDRiAy49mWRPJ%2BpUqouuy9xGrt1wCWA8iL6aH4bdYzombVIw%2B3fDTEYsC3kIaoftgO1VORqQMvIgmpEo0%2BWRI2nNUjR8vHMaQARHJ21DHpsGYbfDVvzsK5rlclbYd%2FqtaN%2BfNm50bZ%2F9cdUefPfNVXGkxXojcTFyWuG6Cge%2Fl4JYnYDjfaSKNm1UPcMd%2Bg%2BqEyreHhkJf4HbrjE36eNWbTyYhRJh9z47EA4ETO7d%2FouM7O7o9rbWc4HysTS37fAQK0wcRJu6BJrhuwgU4mZhArVBd7E6qkSZvUgSAO9s1He0jRMJX0ltXTE5ojTjcMsMOk2%2BHcDJo0wi3wCl5n6MgUELpMetPHPDdaEUUWI2Q4LvmU7%2FsgaAp52qvljLAF6Bf%2B6oIBpUiqnqUFuD6Io4Oez4k1iWB52%2Fu6EzR2xz3xWsy4EwRZbKhVYg%2F5cHVswOh8p1P20PbqGRgTVN%2B145yK2L1Y%2Bg1%2F9NfumdAhZVdi8JnuXY6IcLfR500Gy%2BPjhfQ81b1f%2BJUb9RS1ZIraFh7YchGP0JxhEYS7%2F2zzlZWZSkwDY%2BvPEeuL6x%2F0GzFDCFlvjJBjqkASv0aNyYqeiEL6RlIPLZxr5tWYT01Irx1V6uh%2Fo51b3jQ4%2BbL49f9AoH4lXzh%2FlbN2hnS6qxTvWSFTkbd1%2B4MIQnJKCcwDRBMh6TShH1z3S0L6TuQQ9Egb3aKoXyE%2BqRzbDwzxQ9jlQ4LyiMxkm1a5BtTfqtQiMHD0B4JCebWknPKKZHB21g6iKF5XFkBCO0NqjN3BiHidvuQOzl8CyJbKwlO3Jv&X-Amz-Signature=1d5f6b84cf765cba7a6948c6a36c44143bfb8bea10b8cbf8d9ab66b184add8a2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
<details>
<summary>Explanation</summary>

The **Physical Layer** is the lowest layer of the stack. It's responsible for transmitting raw bit stream over the physical medium like cables or wireless.
</details>
---
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/7c3c354d-826c-48ce-b159-4ddbcd0d9114/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UTMHJ2EA%2F20251214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251214T010632Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJIMEYCIQDdbxEQZ02Em2%2FkjauKUNCal2Ay9wAvQLn%2B47CDSXZxkgIhAMrUBlgvr0LsmTNHrrhYAPQZteTk715oWruUygicSXxiKv8DCCoQABoMNjM3NDIzMTgzODA1IgxEySgXTiuvgOkapHIq3AOmnlegI%2BpHaHh1NFck6M47KIB6v8ugMN80wIoLOKApS42O7hLF7SgixT54yWWDWDRiAy49mWRPJ%2BpUqouuy9xGrt1wCWA8iL6aH4bdYzombVIw%2B3fDTEYsC3kIaoftgO1VORqQMvIgmpEo0%2BWRI2nNUjR8vHMaQARHJ21DHpsGYbfDVvzsK5rlclbYd%2FqtaN%2BfNm50bZ%2F9cdUefPfNVXGkxXojcTFyWuG6Cge%2Fl4JYnYDjfaSKNm1UPcMd%2Bg%2BqEyreHhkJf4HbrjE36eNWbTyYhRJh9z47EA4ETO7d%2FouM7O7o9rbWc4HysTS37fAQK0wcRJu6BJrhuwgU4mZhArVBd7E6qkSZvUgSAO9s1He0jRMJX0ltXTE5ojTjcMsMOk2%2BHcDJo0wi3wCl5n6MgUELpMetPHPDdaEUUWI2Q4LvmU7%2FsgaAp52qvljLAF6Bf%2B6oIBpUiqnqUFuD6Io4Oez4k1iWB52%2Fu6EzR2xz3xWsy4EwRZbKhVYg%2F5cHVswOh8p1P20PbqGRgTVN%2B145yK2L1Y%2Bg1%2F9NfumdAhZVdi8JnuXY6IcLfR500Gy%2BPjhfQ81b1f%2BJUb9RS1ZIraFh7YchGP0JxhEYS7%2F2zzlZWZSkwDY%2BvPEeuL6x%2F0GzFDCFlvjJBjqkASv0aNyYqeiEL6RlIPLZxr5tWYT01Irx1V6uh%2Fo51b3jQ4%2BbL49f9AoH4lXzh%2FlbN2hnS6qxTvWSFTkbd1%2B4MIQnJKCcwDRBMh6TShH1z3S0L6TuQQ9Egb3aKoXyE%2BqRzbDwzxQ9jlQ4LyiMxkm1a5BtTfqtQiMHD0B4JCebWknPKKZHB21g6iKF5XFkBCO0NqjN3BiHidvuQOzl8CyJbKwlO3Jv&X-Amz-Signature=737b9d95bdccae069184f13026e07d03444113ea7dabd2847e8cdc752a392fe4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
<details>
<summary>Explanation</summary>

To recap again, the ntworking stack is divided into different layers, each responsible for a specific task. 
1. **Application Layer**: This is where network applications (like your web browser or email client) and their protocols reside. For example, HTTP (Hypertext Transfer Protocol) is an application layer protocol used on the web. The line `GET /postbox HTTP/1.1` is an HTTP request to retrieve the resource located at `/postbox`.
1. **Transport Layer**: This layer is responsible for end-to-end communication over the network. It uses protocols like TCP (Transmission Control Protocol) to ensure data is sent and received correctly. The `TCP Segment` section in the slide shows details of a TCP packet, including the sequence number and source/destination ports.
1. **Network Layer**: This layer is responsible for routing data across networks. It uses protocols like IP (Internet Protocol) to route packets to their destination. The `IP Packet` section shows the source and destination IP addresses for a packet.
1. **Data Link Layer**: This layer is responsible for transferring data between network nodes. It uses protocols like Ethernet to communicate with devices on the same network. The `Frame` section shows the source and destination MAC addresses, which are unique identifiers for network devices.
1. **Physical Layer**: This layer is responsible for the actual transmission of data over the physical medium (like Ethernet cables or Wi-Fi signals). The binary numbers at the end represent the raw data being sent over the network.
Here's a simple analogy: Imagine sending a letter. You write the letter (Application), put it in an envelope (Transport), address the envelope (Network), give it to the post office (Data Link), and it's physically delivered (Physical). The receiving end opens the letter in reverse order.
</details>
---
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/53e3fd5c-da04-4f47-a794-61aeeb808f12/Screenshot_2022-06-24_at_12.59.38.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UTMHJ2EA%2F20251214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251214T010632Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJIMEYCIQDdbxEQZ02Em2%2FkjauKUNCal2Ay9wAvQLn%2B47CDSXZxkgIhAMrUBlgvr0LsmTNHrrhYAPQZteTk715oWruUygicSXxiKv8DCCoQABoMNjM3NDIzMTgzODA1IgxEySgXTiuvgOkapHIq3AOmnlegI%2BpHaHh1NFck6M47KIB6v8ugMN80wIoLOKApS42O7hLF7SgixT54yWWDWDRiAy49mWRPJ%2BpUqouuy9xGrt1wCWA8iL6aH4bdYzombVIw%2B3fDTEYsC3kIaoftgO1VORqQMvIgmpEo0%2BWRI2nNUjR8vHMaQARHJ21DHpsGYbfDVvzsK5rlclbYd%2FqtaN%2BfNm50bZ%2F9cdUefPfNVXGkxXojcTFyWuG6Cge%2Fl4JYnYDjfaSKNm1UPcMd%2Bg%2BqEyreHhkJf4HbrjE36eNWbTyYhRJh9z47EA4ETO7d%2FouM7O7o9rbWc4HysTS37fAQK0wcRJu6BJrhuwgU4mZhArVBd7E6qkSZvUgSAO9s1He0jRMJX0ltXTE5ojTjcMsMOk2%2BHcDJo0wi3wCl5n6MgUELpMetPHPDdaEUUWI2Q4LvmU7%2FsgaAp52qvljLAF6Bf%2B6oIBpUiqnqUFuD6Io4Oez4k1iWB52%2Fu6EzR2xz3xWsy4EwRZbKhVYg%2F5cHVswOh8p1P20PbqGRgTVN%2B145yK2L1Y%2Bg1%2F9NfumdAhZVdi8JnuXY6IcLfR500Gy%2BPjhfQ81b1f%2BJUb9RS1ZIraFh7YchGP0JxhEYS7%2F2zzlZWZSkwDY%2BvPEeuL6x%2F0GzFDCFlvjJBjqkASv0aNyYqeiEL6RlIPLZxr5tWYT01Irx1V6uh%2Fo51b3jQ4%2BbL49f9AoH4lXzh%2FlbN2hnS6qxTvWSFTkbd1%2B4MIQnJKCcwDRBMh6TShH1z3S0L6TuQQ9Egb3aKoXyE%2BqRzbDwzxQ9jlQ4LyiMxkm1a5BtTfqtQiMHD0B4JCebWknPKKZHB21g6iKF5XFkBCO0NqjN3BiHidvuQOzl8CyJbKwlO3Jv&X-Amz-Signature=2d3ab77e8e04f2c3a09682ae5b2fd2d105410ba4cc58cac4e97d1582f14a56a9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
<details>
<summary>Explanation</summary>

```python
# A simplified code example of how this might look in Python:

# Application Layer
message = "Hi!"

# Transport Layer
segments = [message[i:i+2] for i in range(0, len(message), 2)]

# Network Layer
source_ip = "192.168.1.1"
destination_ip = "192.168.1.2"
packets = [(source_ip, destination_ip, segment) for segment in segments]

# Data Link Layer
source_mac = "00:0a:95:9d:68:16"
destination_mac = "00:0a:95:9d:68:17"
frames = [(source_mac, destination_mac, packet) for packet in packets]

# Physical Layer
signals = [bin(int.from_bytes(frame[2][2].encode(), 'big')) for frame in frames]
```
</details>
---
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/d8b53f67-1da2-4f3b-85f1-5cfda740476d/Screenshot_2022-06-24_at_12.59.44.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UTMHJ2EA%2F20251214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251214T010632Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJIMEYCIQDdbxEQZ02Em2%2FkjauKUNCal2Ay9wAvQLn%2B47CDSXZxkgIhAMrUBlgvr0LsmTNHrrhYAPQZteTk715oWruUygicSXxiKv8DCCoQABoMNjM3NDIzMTgzODA1IgxEySgXTiuvgOkapHIq3AOmnlegI%2BpHaHh1NFck6M47KIB6v8ugMN80wIoLOKApS42O7hLF7SgixT54yWWDWDRiAy49mWRPJ%2BpUqouuy9xGrt1wCWA8iL6aH4bdYzombVIw%2B3fDTEYsC3kIaoftgO1VORqQMvIgmpEo0%2BWRI2nNUjR8vHMaQARHJ21DHpsGYbfDVvzsK5rlclbYd%2FqtaN%2BfNm50bZ%2F9cdUefPfNVXGkxXojcTFyWuG6Cge%2Fl4JYnYDjfaSKNm1UPcMd%2Bg%2BqEyreHhkJf4HbrjE36eNWbTyYhRJh9z47EA4ETO7d%2FouM7O7o9rbWc4HysTS37fAQK0wcRJu6BJrhuwgU4mZhArVBd7E6qkSZvUgSAO9s1He0jRMJX0ltXTE5ojTjcMsMOk2%2BHcDJo0wi3wCl5n6MgUELpMetPHPDdaEUUWI2Q4LvmU7%2FsgaAp52qvljLAF6Bf%2B6oIBpUiqnqUFuD6Io4Oez4k1iWB52%2Fu6EzR2xz3xWsy4EwRZbKhVYg%2F5cHVswOh8p1P20PbqGRgTVN%2B145yK2L1Y%2Bg1%2F9NfumdAhZVdi8JnuXY6IcLfR500Gy%2BPjhfQ81b1f%2BJUb9RS1ZIraFh7YchGP0JxhEYS7%2F2zzlZWZSkwDY%2BvPEeuL6x%2F0GzFDCFlvjJBjqkASv0aNyYqeiEL6RlIPLZxr5tWYT01Irx1V6uh%2Fo51b3jQ4%2BbL49f9AoH4lXzh%2FlbN2hnS6qxTvWSFTkbd1%2B4MIQnJKCcwDRBMh6TShH1z3S0L6TuQQ9Egb3aKoXyE%2BqRzbDwzxQ9jlQ4LyiMxkm1a5BtTfqtQiMHD0B4JCebWknPKKZHB21g6iKF5XFkBCO0NqjN3BiHidvuQOzl8CyJbKwlO3Jv&X-Amz-Signature=a45ceeba2364364cfc0d085d130b3baf05c89234855a9929c688322ec8291b72&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
---
