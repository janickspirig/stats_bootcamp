---
title: "Computing basics"
notion_id: "b0c2d90a-6de5-45b7-8f7b-2586514e9a20"
notion_url: "https://www.notion.so/Computing-basics-b0c2d90a6de545b78f7b2586514e9a20"
exported_at: "2025-12-13T22:55:02.753338+00:00"
---

# Computing basics

---
**Decimal to binary**
What is 452 in binary?

<details>
<summary>Solution</summary>

`1 1100 0100`
| Calculation | Resulting binary digit | Aggregated binary digits |
| --- | --- | --- |
| `452 / 2 = 226` | `0` | `0` |
| `226 / 2 = 113` | `0` | `00` |
| `113 - 1 = 112 / 2` | `1` | `100` |
| `56 / 2 = 28` | `0` | `0100` |
| `28 / 2 = 14` | `0` | `0 0100` |
| `14 / 2 = 7` | `0` | `00 0100` |
| `7 - 1 = 6 / 2 = 3` | `1` | `100 0100` |
| `3 - 1 = 2 / 2 = 1` | `1` | `1100 0100` |
| `1 - 1 = 0` | `1` | `1 1100 0100` |
</details>
---
**Binary to decimal**
What is `1101 0011` in decimal? 

<details>
<summary>Solution</summary>

211
We go through the binary number from right to left:
`1` → `1 * 2^0 = `**`1`**
`1` → `1 * 2^1 = `**`2`**
`0` → `0 * 2^2 = `**`0`**
`0` → `0 * 2^3 = `**`0`**
`1` → `1 * 2^4 = `**`16`**
`0` → `0 * 2^5 = `**`0`**
`1` → `1 * 2^6 = `**`64`**
`1` → `1 * 2^7 = `**`128`**
Now we sum up all the numbers:
1 + 2 + 0 + 0 + 16 + 0 + 64 + 128 = <u>**211**</u>
</details>
---
**Logic gates**
Assign the images below to their logic gate and create their truth table.
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/35462356-6d1c-4967-ae72-fbd005674a21/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665CFRTC7P%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T225446Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIBONqwoMjDFYeoa8AAw9ehkPeQIBqYtwkk3VDQSZGx5xAiEA0lFg%2FJw5KOEDPgJXCbHYq%2FMcwfanUWijGJEPpmQbVHsq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDDZtEzHPtXGJBGw5byrcA7eJQaRiByWhk9R%2BwllIiOhT5YTmmKnXsxjQ1j%2FVtUz2AnkkjiRYSQFh1a%2F0KWV9%2Fv5v5Sf%2BAGIekgqlqsrt%2FAE6to5MaE1LZ92W5R6sKjkf2YzL%2BZ5a%2BrVf9YCdXcVbPYOdlj7x6wUd3tVpjMTm3hQrpHNC2xO%2F7oaH5O%2BF6gPzHr98GC67OdJMxa3J4wI1G6KDiqiMaFYVIDNvvWF0OIgyavPKA%2FfZTgixVD%2BXGJiNJpY3Dr4GXsqw%2FUxwjX5HF4rFEc6rK5anvUsOQcxj9Y3Uhc%2B7bxH%2BgK10HqLXPU%2BliMQyUaSZXuXz%2FjOxgSW3mo6OdSmMO5gd8RYa0RjcCXt5rTe1AU1BVWNNSWbHbpUwJpQfUQ96AlSU%2F2rKHGV%2Fl2pS%2FzhVfSYtKFpvTRhwHyzJZhFBpMZcfCMdpPeumaFhiLM0x5X3S5qVWXxk2sPpQ6icBQNBh0Vr0pTBFrhwRuANZ4vjIrienR7jQD4VBS6QoN3lLWH5PaeV9Qktd6i4PR4s%2FNIAAHx3nootd2t%2FVei4laaI5125TaaHLbGlmVD0HL3RmRg%2FadBT0PefDhcLeJeixLPeQ4YPUF%2BoUCvbXYOcZUzEQaM8P7KtGkiLGIrnb%2FuPTWPNK1AirojKMMbO98kGOqUB8z8g6xDdXHeL6gTNLBmEOoLstqrewvi2vK4spZTGn5nWlMWjB55WO69fYVgYw4sOAh%2B3BBYcJguGgkZK21F3Rj0xejnqgWIli9BIjvgPe7aKtrB3UtYlyvWkSuZ%2FcIdfhviSbKpW%2FTl02z7wc2Kk1kIxvE0PVtlyJOK5g5zFpVQw9426FFKTjMtXhP7BIOqdDNAHdfxH9ICZVfPTRH9WnjFU%2FmWv&X-Amz-Signature=9c94ab1274ee904964e603ebe18797a144e07c12c683b11f1f81854695c0465e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/86d2f17d-981c-4b80-92cc-e38b737660b2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665CFRTC7P%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T225446Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIBONqwoMjDFYeoa8AAw9ehkPeQIBqYtwkk3VDQSZGx5xAiEA0lFg%2FJw5KOEDPgJXCbHYq%2FMcwfanUWijGJEPpmQbVHsq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDDZtEzHPtXGJBGw5byrcA7eJQaRiByWhk9R%2BwllIiOhT5YTmmKnXsxjQ1j%2FVtUz2AnkkjiRYSQFh1a%2F0KWV9%2Fv5v5Sf%2BAGIekgqlqsrt%2FAE6to5MaE1LZ92W5R6sKjkf2YzL%2BZ5a%2BrVf9YCdXcVbPYOdlj7x6wUd3tVpjMTm3hQrpHNC2xO%2F7oaH5O%2BF6gPzHr98GC67OdJMxa3J4wI1G6KDiqiMaFYVIDNvvWF0OIgyavPKA%2FfZTgixVD%2BXGJiNJpY3Dr4GXsqw%2FUxwjX5HF4rFEc6rK5anvUsOQcxj9Y3Uhc%2B7bxH%2BgK10HqLXPU%2BliMQyUaSZXuXz%2FjOxgSW3mo6OdSmMO5gd8RYa0RjcCXt5rTe1AU1BVWNNSWbHbpUwJpQfUQ96AlSU%2F2rKHGV%2Fl2pS%2FzhVfSYtKFpvTRhwHyzJZhFBpMZcfCMdpPeumaFhiLM0x5X3S5qVWXxk2sPpQ6icBQNBh0Vr0pTBFrhwRuANZ4vjIrienR7jQD4VBS6QoN3lLWH5PaeV9Qktd6i4PR4s%2FNIAAHx3nootd2t%2FVei4laaI5125TaaHLbGlmVD0HL3RmRg%2FadBT0PefDhcLeJeixLPeQ4YPUF%2BoUCvbXYOcZUzEQaM8P7KtGkiLGIrnb%2FuPTWPNK1AirojKMMbO98kGOqUB8z8g6xDdXHeL6gTNLBmEOoLstqrewvi2vK4spZTGn5nWlMWjB55WO69fYVgYw4sOAh%2B3BBYcJguGgkZK21F3Rj0xejnqgWIli9BIjvgPe7aKtrB3UtYlyvWkSuZ%2FcIdfhviSbKpW%2FTl02z7wc2Kk1kIxvE0PVtlyJOK5g5zFpVQw9426FFKTjMtXhP7BIOqdDNAHdfxH9ICZVfPTRH9WnjFU%2FmWv&X-Amz-Signature=1bc4c086c2e54e776874d7b4aa8860ecbc7a6a5be294618ff678ca6ab640c3ec&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/5f7ffde3-100f-4167-aa32-0cd81d32311c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665CFRTC7P%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T225446Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIBONqwoMjDFYeoa8AAw9ehkPeQIBqYtwkk3VDQSZGx5xAiEA0lFg%2FJw5KOEDPgJXCbHYq%2FMcwfanUWijGJEPpmQbVHsq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDDZtEzHPtXGJBGw5byrcA7eJQaRiByWhk9R%2BwllIiOhT5YTmmKnXsxjQ1j%2FVtUz2AnkkjiRYSQFh1a%2F0KWV9%2Fv5v5Sf%2BAGIekgqlqsrt%2FAE6to5MaE1LZ92W5R6sKjkf2YzL%2BZ5a%2BrVf9YCdXcVbPYOdlj7x6wUd3tVpjMTm3hQrpHNC2xO%2F7oaH5O%2BF6gPzHr98GC67OdJMxa3J4wI1G6KDiqiMaFYVIDNvvWF0OIgyavPKA%2FfZTgixVD%2BXGJiNJpY3Dr4GXsqw%2FUxwjX5HF4rFEc6rK5anvUsOQcxj9Y3Uhc%2B7bxH%2BgK10HqLXPU%2BliMQyUaSZXuXz%2FjOxgSW3mo6OdSmMO5gd8RYa0RjcCXt5rTe1AU1BVWNNSWbHbpUwJpQfUQ96AlSU%2F2rKHGV%2Fl2pS%2FzhVfSYtKFpvTRhwHyzJZhFBpMZcfCMdpPeumaFhiLM0x5X3S5qVWXxk2sPpQ6icBQNBh0Vr0pTBFrhwRuANZ4vjIrienR7jQD4VBS6QoN3lLWH5PaeV9Qktd6i4PR4s%2FNIAAHx3nootd2t%2FVei4laaI5125TaaHLbGlmVD0HL3RmRg%2FadBT0PefDhcLeJeixLPeQ4YPUF%2BoUCvbXYOcZUzEQaM8P7KtGkiLGIrnb%2FuPTWPNK1AirojKMMbO98kGOqUB8z8g6xDdXHeL6gTNLBmEOoLstqrewvi2vK4spZTGn5nWlMWjB55WO69fYVgYw4sOAh%2B3BBYcJguGgkZK21F3Rj0xejnqgWIli9BIjvgPe7aKtrB3UtYlyvWkSuZ%2FcIdfhviSbKpW%2FTl02z7wc2Kk1kIxvE0PVtlyJOK5g5zFpVQw9426FFKTjMtXhP7BIOqdDNAHdfxH9ICZVfPTRH9WnjFU%2FmWv&X-Amz-Signature=e939d9b10e48e0b8603093e7f0a900151c66c31b2e16a5c9c787de17a0246a4b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/d7a05b3c-4771-4673-8ac5-89221fdfc57d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665CFRTC7P%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T225446Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIBONqwoMjDFYeoa8AAw9ehkPeQIBqYtwkk3VDQSZGx5xAiEA0lFg%2FJw5KOEDPgJXCbHYq%2FMcwfanUWijGJEPpmQbVHsq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDDZtEzHPtXGJBGw5byrcA7eJQaRiByWhk9R%2BwllIiOhT5YTmmKnXsxjQ1j%2FVtUz2AnkkjiRYSQFh1a%2F0KWV9%2Fv5v5Sf%2BAGIekgqlqsrt%2FAE6to5MaE1LZ92W5R6sKjkf2YzL%2BZ5a%2BrVf9YCdXcVbPYOdlj7x6wUd3tVpjMTm3hQrpHNC2xO%2F7oaH5O%2BF6gPzHr98GC67OdJMxa3J4wI1G6KDiqiMaFYVIDNvvWF0OIgyavPKA%2FfZTgixVD%2BXGJiNJpY3Dr4GXsqw%2FUxwjX5HF4rFEc6rK5anvUsOQcxj9Y3Uhc%2B7bxH%2BgK10HqLXPU%2BliMQyUaSZXuXz%2FjOxgSW3mo6OdSmMO5gd8RYa0RjcCXt5rTe1AU1BVWNNSWbHbpUwJpQfUQ96AlSU%2F2rKHGV%2Fl2pS%2FzhVfSYtKFpvTRhwHyzJZhFBpMZcfCMdpPeumaFhiLM0x5X3S5qVWXxk2sPpQ6icBQNBh0Vr0pTBFrhwRuANZ4vjIrienR7jQD4VBS6QoN3lLWH5PaeV9Qktd6i4PR4s%2FNIAAHx3nootd2t%2FVei4laaI5125TaaHLbGlmVD0HL3RmRg%2FadBT0PefDhcLeJeixLPeQ4YPUF%2BoUCvbXYOcZUzEQaM8P7KtGkiLGIrnb%2FuPTWPNK1AirojKMMbO98kGOqUB8z8g6xDdXHeL6gTNLBmEOoLstqrewvi2vK4spZTGn5nWlMWjB55WO69fYVgYw4sOAh%2B3BBYcJguGgkZK21F3Rj0xejnqgWIli9BIjvgPe7aKtrB3UtYlyvWkSuZ%2FcIdfhviSbKpW%2FTl02z7wc2Kk1kIxvE0PVtlyJOK5g5zFpVQw9426FFKTjMtXhP7BIOqdDNAHdfxH9ICZVfPTRH9WnjFU%2FmWv&X-Amz-Signature=d678fba5eb6e695129593857053fc181bbaff82d243109b361fa005a24dd3b8c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/efdb3faf-eea5-41cd-87d1-6255fbf8cee1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665CFRTC7P%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T225446Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIBONqwoMjDFYeoa8AAw9ehkPeQIBqYtwkk3VDQSZGx5xAiEA0lFg%2FJw5KOEDPgJXCbHYq%2FMcwfanUWijGJEPpmQbVHsq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDDZtEzHPtXGJBGw5byrcA7eJQaRiByWhk9R%2BwllIiOhT5YTmmKnXsxjQ1j%2FVtUz2AnkkjiRYSQFh1a%2F0KWV9%2Fv5v5Sf%2BAGIekgqlqsrt%2FAE6to5MaE1LZ92W5R6sKjkf2YzL%2BZ5a%2BrVf9YCdXcVbPYOdlj7x6wUd3tVpjMTm3hQrpHNC2xO%2F7oaH5O%2BF6gPzHr98GC67OdJMxa3J4wI1G6KDiqiMaFYVIDNvvWF0OIgyavPKA%2FfZTgixVD%2BXGJiNJpY3Dr4GXsqw%2FUxwjX5HF4rFEc6rK5anvUsOQcxj9Y3Uhc%2B7bxH%2BgK10HqLXPU%2BliMQyUaSZXuXz%2FjOxgSW3mo6OdSmMO5gd8RYa0RjcCXt5rTe1AU1BVWNNSWbHbpUwJpQfUQ96AlSU%2F2rKHGV%2Fl2pS%2FzhVfSYtKFpvTRhwHyzJZhFBpMZcfCMdpPeumaFhiLM0x5X3S5qVWXxk2sPpQ6icBQNBh0Vr0pTBFrhwRuANZ4vjIrienR7jQD4VBS6QoN3lLWH5PaeV9Qktd6i4PR4s%2FNIAAHx3nootd2t%2FVei4laaI5125TaaHLbGlmVD0HL3RmRg%2FadBT0PefDhcLeJeixLPeQ4YPUF%2BoUCvbXYOcZUzEQaM8P7KtGkiLGIrnb%2FuPTWPNK1AirojKMMbO98kGOqUB8z8g6xDdXHeL6gTNLBmEOoLstqrewvi2vK4spZTGn5nWlMWjB55WO69fYVgYw4sOAh%2B3BBYcJguGgkZK21F3Rj0xejnqgWIli9BIjvgPe7aKtrB3UtYlyvWkSuZ%2FcIdfhviSbKpW%2FTl02z7wc2Kk1kIxvE0PVtlyJOK5g5zFpVQw9426FFKTjMtXhP7BIOqdDNAHdfxH9ICZVfPTRH9WnjFU%2FmWv&X-Amz-Signature=194f790422da46afea9ec30f0f5940626825d472a146ddf0e70b7cab979a682a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

<details>
<summary>Solution</summary>

![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/35462356-6d1c-4967-ae72-fbd005674a21/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662YVCFYNY%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T225449Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQCBvj2hXHcDxiu6qdD0YkHiQh8qIta3i7ud4IPJrx4JFgIhAMneg6in1I7sOw13v9Gv7a6Cg7%2ByMoMM931QhxsV339aKv8DCCcQABoMNjM3NDIzMTgzODA1IgwZ3ln9FoVw%2BEMG%2FIwq3ANUsr4s7lO6SE%2BahZj3KAQrISxRO7hpdYd7OmUEnhE1Ah%2FuMOIfduM6HdE1Xe58xt7Uc3Z%2FIQS%2BtPYJMQepEQpfz3HAt7loKTsUWnHZO4m%2B9ksKuTM0m%2BfhaQQC8ZpNGKb%2FpLdMhVpTd4y4bcNyE4p2fUTWflFCUQ2M8hRJrn3VKQBl0rlCIZKtkC5AJg3SQ9ENwmn7SRhiEFeJeEgNVqtSRa7aKgiMhAYCAZ16aScGKxQHTtb7ZXJX1AGrJcAeEeiDUxE7zPRiPu4bPAafkEuW4sxVhY8HtKk7Ytjn4xLpDz5dhd3bNRDWElZarSmuZpDDsS%2FzMM5ACp7l4bbHVecrSLDjw2DcQ9S6d18lo8RvtCrZxfIOhf7Tn4i3ahbytSoMkgkf5qvGURpCp1vmD2lIoevbqM%2ByDTyR%2BcIjCCzeftYs%2BY0vr0DXS7rW0geCScTKtEgfQBQQXIoJZ1UEScYGBRh8BGn1gam%2FErRdyqJjZB6hQlYShIdcLkzHa8BUUJ2sk8eUrEsjw1wKyiPB%2FIa%2F3Rgjvg7WA65HGFfYHV2KQbGSBaT%2B5qWdi6Z3e9H2IqRSyC6VkFXG7mTbAX9qbQdLm%2BQ5cTyFeSK08RYEujQgls4k%2FiL4U8Wq41X6RjCCzvfJBjqkAeufe%2FBa266NqicTkAaJ1ZWvY5%2BdSDLIxmtWa9AIcZPIUbq0CXDgRq2iEWZ9AMwyR8E4HrqQEwynv31bEF1R5036R%2FaPyhEhX1EW%2B6yRZDq7%2BZMkD5%2BgbmmyjKyWWZgHSMjCy5PAXJl2io38PrY%2FFOpTEZ%2F9jwxGMF5hRiyNkPnRZJNg347R%2F8UI9H2AvaGCdErOCo3SejLeH0xcrwa8Q9IAE13G&X-Amz-Signature=10fdd52c3b543a2a86d5b6652de26131ced14aadb793cdc9d5de6ae7b0d5a293&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
- Gate: NAND
- Truth table:
| Input 1 | Input 2 | Result |
| --- | --- | --- |
| False (0) | False (0) | True (1) |
| False (0) | True (1) | True (1) |
| True (1) | False (0) | True (1) |
| True (1) | True (1) | False (0) |
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/86d2f17d-981c-4b80-92cc-e38b737660b2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662YVCFYNY%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T225449Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQCBvj2hXHcDxiu6qdD0YkHiQh8qIta3i7ud4IPJrx4JFgIhAMneg6in1I7sOw13v9Gv7a6Cg7%2ByMoMM931QhxsV339aKv8DCCcQABoMNjM3NDIzMTgzODA1IgwZ3ln9FoVw%2BEMG%2FIwq3ANUsr4s7lO6SE%2BahZj3KAQrISxRO7hpdYd7OmUEnhE1Ah%2FuMOIfduM6HdE1Xe58xt7Uc3Z%2FIQS%2BtPYJMQepEQpfz3HAt7loKTsUWnHZO4m%2B9ksKuTM0m%2BfhaQQC8ZpNGKb%2FpLdMhVpTd4y4bcNyE4p2fUTWflFCUQ2M8hRJrn3VKQBl0rlCIZKtkC5AJg3SQ9ENwmn7SRhiEFeJeEgNVqtSRa7aKgiMhAYCAZ16aScGKxQHTtb7ZXJX1AGrJcAeEeiDUxE7zPRiPu4bPAafkEuW4sxVhY8HtKk7Ytjn4xLpDz5dhd3bNRDWElZarSmuZpDDsS%2FzMM5ACp7l4bbHVecrSLDjw2DcQ9S6d18lo8RvtCrZxfIOhf7Tn4i3ahbytSoMkgkf5qvGURpCp1vmD2lIoevbqM%2ByDTyR%2BcIjCCzeftYs%2BY0vr0DXS7rW0geCScTKtEgfQBQQXIoJZ1UEScYGBRh8BGn1gam%2FErRdyqJjZB6hQlYShIdcLkzHa8BUUJ2sk8eUrEsjw1wKyiPB%2FIa%2F3Rgjvg7WA65HGFfYHV2KQbGSBaT%2B5qWdi6Z3e9H2IqRSyC6VkFXG7mTbAX9qbQdLm%2BQ5cTyFeSK08RYEujQgls4k%2FiL4U8Wq41X6RjCCzvfJBjqkAeufe%2FBa266NqicTkAaJ1ZWvY5%2BdSDLIxmtWa9AIcZPIUbq0CXDgRq2iEWZ9AMwyR8E4HrqQEwynv31bEF1R5036R%2FaPyhEhX1EW%2B6yRZDq7%2BZMkD5%2BgbmmyjKyWWZgHSMjCy5PAXJl2io38PrY%2FFOpTEZ%2F9jwxGMF5hRiyNkPnRZJNg347R%2F8UI9H2AvaGCdErOCo3SejLeH0xcrwa8Q9IAE13G&X-Amz-Signature=8ed28af633d1ad0dbd44eaf4a0cc00ea5a70171ac57ea71b6200ba62a8f2e2ab&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
- Gate: OR
- Truth table:
| Input 1 | Input 2 | Result |
| --- | --- | --- |
| False (0) | False (0) | False (0) |
| False (0) | True (1) | True (1) |
| True (1) | False (0) | True (1) |
| True (1) | True (1) | True (1) |
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/5f7ffde3-100f-4167-aa32-0cd81d32311c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662YVCFYNY%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T225449Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQCBvj2hXHcDxiu6qdD0YkHiQh8qIta3i7ud4IPJrx4JFgIhAMneg6in1I7sOw13v9Gv7a6Cg7%2ByMoMM931QhxsV339aKv8DCCcQABoMNjM3NDIzMTgzODA1IgwZ3ln9FoVw%2BEMG%2FIwq3ANUsr4s7lO6SE%2BahZj3KAQrISxRO7hpdYd7OmUEnhE1Ah%2FuMOIfduM6HdE1Xe58xt7Uc3Z%2FIQS%2BtPYJMQepEQpfz3HAt7loKTsUWnHZO4m%2B9ksKuTM0m%2BfhaQQC8ZpNGKb%2FpLdMhVpTd4y4bcNyE4p2fUTWflFCUQ2M8hRJrn3VKQBl0rlCIZKtkC5AJg3SQ9ENwmn7SRhiEFeJeEgNVqtSRa7aKgiMhAYCAZ16aScGKxQHTtb7ZXJX1AGrJcAeEeiDUxE7zPRiPu4bPAafkEuW4sxVhY8HtKk7Ytjn4xLpDz5dhd3bNRDWElZarSmuZpDDsS%2FzMM5ACp7l4bbHVecrSLDjw2DcQ9S6d18lo8RvtCrZxfIOhf7Tn4i3ahbytSoMkgkf5qvGURpCp1vmD2lIoevbqM%2ByDTyR%2BcIjCCzeftYs%2BY0vr0DXS7rW0geCScTKtEgfQBQQXIoJZ1UEScYGBRh8BGn1gam%2FErRdyqJjZB6hQlYShIdcLkzHa8BUUJ2sk8eUrEsjw1wKyiPB%2FIa%2F3Rgjvg7WA65HGFfYHV2KQbGSBaT%2B5qWdi6Z3e9H2IqRSyC6VkFXG7mTbAX9qbQdLm%2BQ5cTyFeSK08RYEujQgls4k%2FiL4U8Wq41X6RjCCzvfJBjqkAeufe%2FBa266NqicTkAaJ1ZWvY5%2BdSDLIxmtWa9AIcZPIUbq0CXDgRq2iEWZ9AMwyR8E4HrqQEwynv31bEF1R5036R%2FaPyhEhX1EW%2B6yRZDq7%2BZMkD5%2BgbmmyjKyWWZgHSMjCy5PAXJl2io38PrY%2FFOpTEZ%2F9jwxGMF5hRiyNkPnRZJNg347R%2F8UI9H2AvaGCdErOCo3SejLeH0xcrwa8Q9IAE13G&X-Amz-Signature=5af919749aeb2064656a31f4350888f2503f7c1f34ebcac1ee507ea7f8d8766d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
- Gate: AND
- Truth table:
| Input 1 | Input 2 | Result |
| --- | --- | --- |
| False (0) | False (0) | False (0) |
| False (0) | True (1) | False (0) |
| True (1) | False (0) | False (0) |
| True (1) | True (1) | True (1) |
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/d7a05b3c-4771-4673-8ac5-89221fdfc57d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662YVCFYNY%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T225449Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQCBvj2hXHcDxiu6qdD0YkHiQh8qIta3i7ud4IPJrx4JFgIhAMneg6in1I7sOw13v9Gv7a6Cg7%2ByMoMM931QhxsV339aKv8DCCcQABoMNjM3NDIzMTgzODA1IgwZ3ln9FoVw%2BEMG%2FIwq3ANUsr4s7lO6SE%2BahZj3KAQrISxRO7hpdYd7OmUEnhE1Ah%2FuMOIfduM6HdE1Xe58xt7Uc3Z%2FIQS%2BtPYJMQepEQpfz3HAt7loKTsUWnHZO4m%2B9ksKuTM0m%2BfhaQQC8ZpNGKb%2FpLdMhVpTd4y4bcNyE4p2fUTWflFCUQ2M8hRJrn3VKQBl0rlCIZKtkC5AJg3SQ9ENwmn7SRhiEFeJeEgNVqtSRa7aKgiMhAYCAZ16aScGKxQHTtb7ZXJX1AGrJcAeEeiDUxE7zPRiPu4bPAafkEuW4sxVhY8HtKk7Ytjn4xLpDz5dhd3bNRDWElZarSmuZpDDsS%2FzMM5ACp7l4bbHVecrSLDjw2DcQ9S6d18lo8RvtCrZxfIOhf7Tn4i3ahbytSoMkgkf5qvGURpCp1vmD2lIoevbqM%2ByDTyR%2BcIjCCzeftYs%2BY0vr0DXS7rW0geCScTKtEgfQBQQXIoJZ1UEScYGBRh8BGn1gam%2FErRdyqJjZB6hQlYShIdcLkzHa8BUUJ2sk8eUrEsjw1wKyiPB%2FIa%2F3Rgjvg7WA65HGFfYHV2KQbGSBaT%2B5qWdi6Z3e9H2IqRSyC6VkFXG7mTbAX9qbQdLm%2BQ5cTyFeSK08RYEujQgls4k%2FiL4U8Wq41X6RjCCzvfJBjqkAeufe%2FBa266NqicTkAaJ1ZWvY5%2BdSDLIxmtWa9AIcZPIUbq0CXDgRq2iEWZ9AMwyR8E4HrqQEwynv31bEF1R5036R%2FaPyhEhX1EW%2B6yRZDq7%2BZMkD5%2BgbmmyjKyWWZgHSMjCy5PAXJl2io38PrY%2FFOpTEZ%2F9jwxGMF5hRiyNkPnRZJNg347R%2F8UI9H2AvaGCdErOCo3SejLeH0xcrwa8Q9IAE13G&X-Amz-Signature=dcd0421caaa03d00e136a6303cb53890fe877d41aa0d603abff8552aee71a9e2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
- Gate: NOR
- Truth table:
| Input 1 | Input 2 | Result |
| --- | --- | --- |
| False (0) | False (0) | True (1) |
| False (0) | True (1) | False (0) |
| True (1) | False (0) | False (0) |
| True (1) | True (1) | False (0) |
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/efdb3faf-eea5-41cd-87d1-6255fbf8cee1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662YVCFYNY%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T225449Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQCBvj2hXHcDxiu6qdD0YkHiQh8qIta3i7ud4IPJrx4JFgIhAMneg6in1I7sOw13v9Gv7a6Cg7%2ByMoMM931QhxsV339aKv8DCCcQABoMNjM3NDIzMTgzODA1IgwZ3ln9FoVw%2BEMG%2FIwq3ANUsr4s7lO6SE%2BahZj3KAQrISxRO7hpdYd7OmUEnhE1Ah%2FuMOIfduM6HdE1Xe58xt7Uc3Z%2FIQS%2BtPYJMQepEQpfz3HAt7loKTsUWnHZO4m%2B9ksKuTM0m%2BfhaQQC8ZpNGKb%2FpLdMhVpTd4y4bcNyE4p2fUTWflFCUQ2M8hRJrn3VKQBl0rlCIZKtkC5AJg3SQ9ENwmn7SRhiEFeJeEgNVqtSRa7aKgiMhAYCAZ16aScGKxQHTtb7ZXJX1AGrJcAeEeiDUxE7zPRiPu4bPAafkEuW4sxVhY8HtKk7Ytjn4xLpDz5dhd3bNRDWElZarSmuZpDDsS%2FzMM5ACp7l4bbHVecrSLDjw2DcQ9S6d18lo8RvtCrZxfIOhf7Tn4i3ahbytSoMkgkf5qvGURpCp1vmD2lIoevbqM%2ByDTyR%2BcIjCCzeftYs%2BY0vr0DXS7rW0geCScTKtEgfQBQQXIoJZ1UEScYGBRh8BGn1gam%2FErRdyqJjZB6hQlYShIdcLkzHa8BUUJ2sk8eUrEsjw1wKyiPB%2FIa%2F3Rgjvg7WA65HGFfYHV2KQbGSBaT%2B5qWdi6Z3e9H2IqRSyC6VkFXG7mTbAX9qbQdLm%2BQ5cTyFeSK08RYEujQgls4k%2FiL4U8Wq41X6RjCCzvfJBjqkAeufe%2FBa266NqicTkAaJ1ZWvY5%2BdSDLIxmtWa9AIcZPIUbq0CXDgRq2iEWZ9AMwyR8E4HrqQEwynv31bEF1R5036R%2FaPyhEhX1EW%2B6yRZDq7%2BZMkD5%2BgbmmyjKyWWZgHSMjCy5PAXJl2io38PrY%2FFOpTEZ%2F9jwxGMF5hRiyNkPnRZJNg347R%2F8UI9H2AvaGCdErOCo3SejLeH0xcrwa8Q9IAE13G&X-Amz-Signature=5836a007674b1dce9637fabeebcfcaabbcb2bc328fae5525d0bcaef08ef393b8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
- Gate: XOR
- Truth table:
| Input 1 | Input 2 | Result |
| --- | --- | --- |
| False (0) | False (0) | False (0) |
| False (0) | True (1) | True (1) |
| True (1) | False (0) | True (1) |
| True (1) | True (1) | False (0) |
</details>
---
**Logic gates**
Which logic gate is represented here?
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/d9e5aec0-bc51-48d2-94f2-21491e487e6b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665CFRTC7P%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T225446Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIBONqwoMjDFYeoa8AAw9ehkPeQIBqYtwkk3VDQSZGx5xAiEA0lFg%2FJw5KOEDPgJXCbHYq%2FMcwfanUWijGJEPpmQbVHsq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDDZtEzHPtXGJBGw5byrcA7eJQaRiByWhk9R%2BwllIiOhT5YTmmKnXsxjQ1j%2FVtUz2AnkkjiRYSQFh1a%2F0KWV9%2Fv5v5Sf%2BAGIekgqlqsrt%2FAE6to5MaE1LZ92W5R6sKjkf2YzL%2BZ5a%2BrVf9YCdXcVbPYOdlj7x6wUd3tVpjMTm3hQrpHNC2xO%2F7oaH5O%2BF6gPzHr98GC67OdJMxa3J4wI1G6KDiqiMaFYVIDNvvWF0OIgyavPKA%2FfZTgixVD%2BXGJiNJpY3Dr4GXsqw%2FUxwjX5HF4rFEc6rK5anvUsOQcxj9Y3Uhc%2B7bxH%2BgK10HqLXPU%2BliMQyUaSZXuXz%2FjOxgSW3mo6OdSmMO5gd8RYa0RjcCXt5rTe1AU1BVWNNSWbHbpUwJpQfUQ96AlSU%2F2rKHGV%2Fl2pS%2FzhVfSYtKFpvTRhwHyzJZhFBpMZcfCMdpPeumaFhiLM0x5X3S5qVWXxk2sPpQ6icBQNBh0Vr0pTBFrhwRuANZ4vjIrienR7jQD4VBS6QoN3lLWH5PaeV9Qktd6i4PR4s%2FNIAAHx3nootd2t%2FVei4laaI5125TaaHLbGlmVD0HL3RmRg%2FadBT0PefDhcLeJeixLPeQ4YPUF%2BoUCvbXYOcZUzEQaM8P7KtGkiLGIrnb%2FuPTWPNK1AirojKMMbO98kGOqUB8z8g6xDdXHeL6gTNLBmEOoLstqrewvi2vK4spZTGn5nWlMWjB55WO69fYVgYw4sOAh%2B3BBYcJguGgkZK21F3Rj0xejnqgWIli9BIjvgPe7aKtrB3UtYlyvWkSuZ%2FcIdfhviSbKpW%2FTl02z7wc2Kk1kIxvE0PVtlyJOK5g5zFpVQw9426FFKTjMtXhP7BIOqdDNAHdfxH9ICZVfPTRH9WnjFU%2FmWv&X-Amz-Signature=d4b472ad7699bb1afbcf42716eea2c13989bbb364b10aa7041fe25465ef3a504&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
- [ ] Q = A AND B
- [ ] Q = A OR B
- [ ] Q = A XOR B
- [ ] Q = A NAND B
- [ ] Q = A NOR B

<details>
<summary>Solution</summary>

Q = A **XOR** B
| A | B | Output |
| --- | --- | --- |
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |
</details>
---
**Logic gates**
Create and fill out a Truth-table for the logic gate combination below. Your table should have three columns: A, B and Z.
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/c219addd-4634-4ed7-97e9-9d9433e6027d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665CFRTC7P%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T225446Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIBONqwoMjDFYeoa8AAw9ehkPeQIBqYtwkk3VDQSZGx5xAiEA0lFg%2FJw5KOEDPgJXCbHYq%2FMcwfanUWijGJEPpmQbVHsq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDDZtEzHPtXGJBGw5byrcA7eJQaRiByWhk9R%2BwllIiOhT5YTmmKnXsxjQ1j%2FVtUz2AnkkjiRYSQFh1a%2F0KWV9%2Fv5v5Sf%2BAGIekgqlqsrt%2FAE6to5MaE1LZ92W5R6sKjkf2YzL%2BZ5a%2BrVf9YCdXcVbPYOdlj7x6wUd3tVpjMTm3hQrpHNC2xO%2F7oaH5O%2BF6gPzHr98GC67OdJMxa3J4wI1G6KDiqiMaFYVIDNvvWF0OIgyavPKA%2FfZTgixVD%2BXGJiNJpY3Dr4GXsqw%2FUxwjX5HF4rFEc6rK5anvUsOQcxj9Y3Uhc%2B7bxH%2BgK10HqLXPU%2BliMQyUaSZXuXz%2FjOxgSW3mo6OdSmMO5gd8RYa0RjcCXt5rTe1AU1BVWNNSWbHbpUwJpQfUQ96AlSU%2F2rKHGV%2Fl2pS%2FzhVfSYtKFpvTRhwHyzJZhFBpMZcfCMdpPeumaFhiLM0x5X3S5qVWXxk2sPpQ6icBQNBh0Vr0pTBFrhwRuANZ4vjIrienR7jQD4VBS6QoN3lLWH5PaeV9Qktd6i4PR4s%2FNIAAHx3nootd2t%2FVei4laaI5125TaaHLbGlmVD0HL3RmRg%2FadBT0PefDhcLeJeixLPeQ4YPUF%2BoUCvbXYOcZUzEQaM8P7KtGkiLGIrnb%2FuPTWPNK1AirojKMMbO98kGOqUB8z8g6xDdXHeL6gTNLBmEOoLstqrewvi2vK4spZTGn5nWlMWjB55WO69fYVgYw4sOAh%2B3BBYcJguGgkZK21F3Rj0xejnqgWIli9BIjvgPe7aKtrB3UtYlyvWkSuZ%2FcIdfhviSbKpW%2FTl02z7wc2Kk1kIxvE0PVtlyJOK5g5zFpVQw9426FFKTjMtXhP7BIOqdDNAHdfxH9ICZVfPTRH9WnjFU%2FmWv&X-Amz-Signature=d99f8417d09d495525f6e6c2cd8bc4b8e99c53e899cbe45bf082b351ee0b3db5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

<details>
<summary>Solution</summary>

| A | B | Z |
| --- | --- | --- |
| 0 | 0 | 0 |
| 0 | 1 | 0 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |
</details>
---
**Logic gates**
If we put 0 as A and 1 as B into the Full Adder, what will S and C-out be?

<details>
<summary>Solution</summary>

`S = 1`, `C-out = 0`
1 + 0 = 1 → no carry
</details>
---
**Logic gates**
The Half-adder has a Carry-Out but no Carry-In. True or False?

<details>
<summary>Solution</summary>

True
</details>
---
**Binary addition**
What is `01010101` + `10110101`?

<details>
<summary>Solution</summary>

`100001010`
Write numbers above each other and sum them up
</details>
---
|  |
|  |
|  |
|  |
|  |
**CPU**
What is stored in Register 0 and Register 1 after executing the following program:
`0011011 0001100 1110 0101 1001`

| Command | Explanation |
| --- | --- |
| 00xyyyy | Load number yyyy into R[x] |
| 11xy | Multiply R[x] with R[y] and store result in R[y] |
| 10xy | Add R[x] and R[y] and store result in R[y]  |
| 01xy | Subtract R[y] from R[x] and store result in R[x] |

<details>
<summary>Solution</summary>

| R[0] | R[1] |
| --- | --- |
| 12 | 11 |
| 132 | **132** |
| **121** |  |
</details>
---
**CPU**
What is stored in Register 0 and Register 1 after executing the following program:
`0001101 0010010 0101 1101 1010`

| Command | Explanation |
| --- | --- |
| 00xyyyy | Load number yyyy into R[x] |
| 11**x**y | Multiply R[x] with R[y] and store result in R[y] |
| 10xy | Add R[x] and R[y] and store result in R[y]  |
| 01xy | Subtract R[y] from R[x] and store result in R[x] |

<details>
<summary>Solution</summary>

| R[0] | R[1] |
| --- | --- |
| 13 | 2 |
| 11 | **22** |
| **33** |  |
</details>
---
**CPU**
In which part of the CPU is the the Full-Adder located?
- [ ] Control Unit
- [ ] Registers
- [ ] Arithmetic Logic Unit (ALU)
- [ ] Memory Unit

<details>
<summary>Solution</summary>

Arithmetic Logic Unit (ALU)
All mathematical operations / computation is done in ALU
</details>
---
