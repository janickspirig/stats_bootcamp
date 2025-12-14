---
title: "Pandas"
notion_id: "1867045b-0583-43e1-a66b-677961515907"
notion_url: "https://www.notion.so/Pandas-1867045b058343e1a66b677961515907"
exported_at: "2025-12-13T22:26:39.045247+00:00"
---

# Pandas

# Motivation
---
If you are already familiar with [Numpy](/ccc5737dc7c64936bced118aca375cf9) you know that we can create 2-dimensional arrays that may look something like this:
```python
import numpy as np

my_array = np.arange(5, 95).reshape((9,10))

my_array
array([[ 5,  6,  7,  8,  9, 10, 11, 12, 13, 14],
       [15, 16, 17, 18, 19, 20, 21, 22, 23, 24],
       [25, 26, 27, 28, 29, 30, 31, 32, 33, 34],
       [35, 36, 37, 38, 39, 40, 41, 42, 43, 44],
       [45, 46, 47, 48, 49, 50, 51, 52, 53, 54],
       [55, 56, 57, 58, 59, 60, 61, 62, 63, 64],
       [65, 66, 67, 68, 69, 70, 71, 72, 73, 74],
       [75, 76, 77, 78, 79, 80, 81, 82, 83, 84],
       [85, 86, 87, 88, 89, 90, 91, 92, 93, 94]])
```
This Numpy array is basically nothing else than a simple table with 10 columns and 9 rows. So why not displaying the data in a more user-friendly and beautiful manner like this?
![Simple DataFrame with 9 rows and 10 columns](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/de8c59d1-37e8-4920-af3e-954b9e1b1bd9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666WZRUUT5%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T222447Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJFMEMCIFrfVfgKjHxq%2FoSa6kpV%2BS6bMfpYZlvVuILRO%2BqE2WEvAh9gJHwoOnxe6PbhgO1KlIye69%2FQkIdGHPFIdeXRzzuoKv8DCCcQABoMNjM3NDIzMTgzODA1IgwrK4xrYAi11Vch5Ecq3APhwEaFmdPlCJD5NvKEkkJBC%2FDyS%2F3DlD0TWI%2FvM7MYd8PUicHhxzGk8VqE8w7n2L9TYtNJahveHAtV04ag1FeQTdzIpi%2FY1GYu8CdJtakhQYrT0wU%2FUwugHDPsaQVGRz9igyh5hjZbSbMM%2FavqWPvYQZlzvV%2B57glykVuM43il0H%2FX87Zz75vEQqZrhThiEZSQQzR0vzA9YSME4DpgqOUI7Y2agJHtOYwgp4qLMOCrGFyg%2FPCVr1C3pVt47n0vlYSCc4cX%2BlxZGfUCV28YunstkSGDYcC0dHI3Ghv38ls27UeSFFvV7jDOkMP8FXMVGOzP9jRiP6MtKkH%2BTHVQCrayU3ufIIb3pV%2F%2Fx%2FtCYDk89VvisTUZzURGVoRFp5evElkPFOC%2FIfC0kozuhqsRf5fa7vzUADjQsp023urusCZjXiEYjg1AdmmHwHUEntfOmVz6Pu4behWsqFxdooJ6Wm%2FDkiFOe1TvQuD3t0db8hfTHqvUH%2F1J%2BIJdwtaI2BzzX4XPyLUjYtEFgxaTXQQh3K%2FP5PyJFIDyGQsJigMg46kq3pT8pnu5V9D6relDz5ektVdyD9fnHwlYYFOEk8Maru3bAS0p2d8aot1zCFiI5RImfyJxAdk5%2FKlFYH2pkzDpzffJBjqnAbjOBMaQHWdfAJobiRrVw9PLco3Ja1GXn6Up7lm%2BjTPrnkYH1oTX3uIH700mv8NExwjdXHae2HgO%2B9z7CQ72wy1kRqDUM75nl868Tkmos0D7FHKxT2zfVw0VuxG%2BQ4kFv5O1TbkSMM8CQo5LNiqFUtS0RofI%2FcoWRCk91PmUCQ6V%2BIxpTH%2FQ98rLoONEZWdoQ96TvHA6vRng4h9%2BDkQKhRuezsyILLw5&X-Amz-Signature=cf8fbc0588b8e9033d3efb2937eed76f235f518899491e59323ae0e70f08e467&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
This is exactly what the package **Pandas** allows us to do. Above you can see a very simple Pandas DataFrame. However, the package does not only enable us to create such nice-looking tables in Python but also a multitude of methods to wrangle around with data and manipulate data.
---
# Data Types
---
When using the Pandas library we deal with slightly different data types than in [regular Python](/1e485dd6e1754338bb05ff87ff4153ad). From the table below you see that we have all the datatypes available that we have in Python as well, they are just called marginally different.
| Pandas | Python |
| --- | --- |
| object | str |
| int64 | int |
| float64 | float |
| bool | bool |
| … | … |
It is important to mention that the table above is not exhaustive, but covers the most important ones. I don’t think that you need to remember the names exactly, it is just good to be aware of these differences so that you don’t get confused when working with Pandas. 
However, there are two very important data structures that exist in Pandas: DataFrame and Series. You will see many examples of these in the Functions documentation below.
Anyway, we quickly want to address the main difference between these two. 
---
**DataFrame**
Let’s assume we have a table like the following:
![Example DataFrame](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/a223167d-99ac-4364-8674-1158014b0574/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664EG43BMB%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T222447Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIQCnF2w4Rqmy6D0KNqrwTCGcXlfnrCFM8tX524G9Gcfj%2FgIgR1vS0xytpd9r%2FDMsFQoE%2FrNYpGCVC9%2FHja%2F7ezyiFLMq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDI9FaepN85jYqYOYiyrcA95CA5EkZmfpYsRp4lZFgXuJNYGVxgs9IdZWOdOUE0wDWi7%2BN9rjJE%2FOujoEs6WVqGno%2B57HGXCicTkh5yN8JC4dhwn3a4pdOKOns4c%2F5Qp1oFfuPSW34s9Sv2J8Dnrau4x9g%2BpRM%2FK%2F2Og7ffvk3Yb4%2FpK5LMWChg61%2FugQrU2MqPICJOyEQBOz8OdWmUMmZq%2Fa707%2BvjZRGLbnyUK77KhS6Ho0yllcCjzLr2Zq4uUmDb4bXlqjQtCcBAdFLBtfqY6to5jLRAMActCfv0bW%2F9RGHfT0GuaDEmiH6jDRvFFinDfITh7BBM4UWK%2Ft%2Fp7CLNxwEhFsQW2%2Bu6FOqEf64GwR%2Fq5ccZPiAl6yUKh8yw7YjYIxjp%2B3pzNcRQP1xV83XAf8xBt66Tz1uxF2MdKOyca0n%2F4Z4XYudEQyKjJ%2BOV45V8i%2B6hsf5lBHIwrArG0sNVorgLWXBa2D4y3Er4Nu%2FMh%2FlQYjOkHO70AYFNXT6pHjb4I7KGb2GhT9OrLAjwGe%2Bn%2FvuIiPcIIE2AKAdPVHsQ%2F%2BDodUVQL1whaHWZ97tGTrCd7qDN6qBfAxtzZpfXv3Fzn1sK4LqYEYzkfsfrmrKA3w0lWBxAVF%2BRMUjONKuWgOJEFdjXexm1kEqew9MOHN98kGOqUBSyuIHvxOQOpJkEw6w6S5ARDIqJ5f%2BOo45QrmOMjquYgAJxGMNGlXWODLhWAZX8WrdE0gVT96J93bV0Qp6OneIyqJjfoFdwg1M9gTDeLEKtqi54DpzCFtmzaCIx8Ck14N0d6IKBuKODanTh%2BXzmj4xccWEXORfq60p416pOHWfdBT7ippEQLcd2t7Hq9EO6m2UIh07YfWQWXJdhrv6uMUCgU%2F0ZTU&X-Amz-Signature=ad00e5293e524ad86103d38c1fdaa2c463c61d71d416eeea746d022296a73620&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
As soon as something looks similar to this table, we call it a **DataFrame. **
---
**Extracting single column or row**
If we extract a single column from a DataFrame we get a **Series**.
![Extracting a single column](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/e7650b7b-8ba9-4ae2-bb45-1fdcbdec6206/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662JAS3KDI%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T222450Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIFWd3tSEt2aeo8UCZ%2FKO0r36Yp6urqe%2FDcHhmdXMuh6NAiEA%2FZfneEpzb9Ens2Fy9cryk%2BT2P9ctD8%2Bm5fTQ2nWcfKwq%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDJIce8pYASQx%2BYRbUSrcA1%2BTpmOffctVDV0PzP2ckMZmA%2BktFfLDkPDZhhCdeUVBzBcero0lMWuDFPssKmrbAC0VZl5VmdAVdP%2Fyy7GLSXFlNSzhxJpI9qBU9QZFMiyBhxuxqric9aDi1twyxjMuiNvcW1saOiDtNd5FCKW2bkmXjUGcvdFliaBEfiXHOHYs3Ci%2BwxiWcz%2BQEOw9%2BJz9VTJwqsjMJpimuj992r7I%2Bcu1OHykC9ORN5Z9XrmdQXPUu6NfgMMOylPBps0zBCjAnID6vfZ9l6ToDlBLhXK8MCmH1tl8A6Yus41oo5ae1MCnsK6T1dgeH01wjGSnsIEDQECgCgOvMwbPaqve%2B5LLmA1LI6fN2S%2F%2FLPNd3Gdr6v273vIbLM5kkJ%2FnZtwBhAl6nL3mC5sIpKMV9vaAXVLGfz8CmxazFreOweIY2jOx02gISrufWRkU1rZ%2BDYWPDuWjtOM9VaeoCoPH48aPSj60tDGEeoqqMdORMdIp%2FYQdCpbvh5iKDtW68%2FWiTLT0cBBpzNoGmeAgrfEZAATLzPnMK%2FjxTtQl%2Bz85dUAhiC5zqocnsC30CeFzXmxjuSi8qy0m2CY79YIE%2B8rgJILcROR7uXpdz9iTm9T0IGiFSFvGqYacOXjAy7kI5n%2BBuVTVMOml98kGOqUBe5bee5x3VPyPfH89gv%2FyTzlqatGRsKaDlK6eWjXkLljGcVj1%2BasJG8yOuaQ3lWMtyb2wEVj3cKvgFnff72CBFBA3z6Ssbj5%2BlNxaWF5joNuI%2F1dtAePnFjKsIaBCRMrqAOcKnHWKe39A%2FT1y7Y9fB7wyXBmCIU8Afx%2B69CoMIVNC36IaNMiViP6ecZhff%2BEVl6FNILMCfRiBj1fUlIxB%2FWuafdFQ&X-Amz-Signature=db826e757e1f45266e95b46e0630ac8b95374e925a26da1bc167b94154c71bc7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

```python
Rank
1                       Jamie Vardy
2                        Danny Ings
3         Pierre-Emerick Aubameyang
4         Raheem Shaquille Sterling
5               Mohamed Salah Ghaly
6                        Sadio Mané
7                        Harry Kane
8     Raúl Alonso Jiménez Rodríguez
9                   Marcus Rashford
10                  Anthony Martial
Name: Player, dtype: object
```
Also, when we extract a single row from a DataFrame we get a **Series**.
![Extracting a single row](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/1fcd5fd2-ff89-4f7d-aa67-5c69c6c8077f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662KNA3B35%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T222452Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJGMEQCIF7TlA2al%2FnVKG3zZ1ZjjSV9NNNEu55MpmsZS8ECVc7TAiB8kgwS0DoYK0hu6bbFVo6SsJ0duyI2Q3SXpsP1LsWx8Cr%2FAwgmEAAaDDYzNzQyMzE4MzgwNSIMM4AyIzDGmG3ppCkTKtwDvht8%2FpugEC8Hwv81PEkPdoI4PefEB0fzcmcEx%2Fr20l5xpV5V5XLtzitGz75bKlQApuXsi37yhHRuyykR64GxtbfgIrOOj56vPtefwZk3GYgVn3FFbZ9XA7FgtmZ07rfdY73C1aCD74Lw0oOMUwLzTm5tNg0Z%2FcmbhNkfxbd6H7AHfQ5Hd3UJkUSOIFM7iSlspXn8SIftwxgod%2FMECm9VvGEn55kryqC4Xl3%2FdHL36VOT6QpfsAokum7f6dxGrAxAtuX%2BVNhgJgr0wymFoGpy3mmT97CvGhJ4jBRNJ1kOd%2Bp1OToQ8gB%2F8Gw60bldxYb5OSYmj0XT3Mhm%2BBXUpXTSVyYAxsqjQ%2Bf71VWnhwMbzwEsW6A0uAUdrJn%2FyTsM8a4tBO3ilCmVH4Ja3HGV%2FqrxycwcL5amIopRgEERPYCZRCLNJYNs6Zy%2B9HRhzDdFXEonsRpZR%2B3CLKoq7%2Be2YkF2efmZ6HKW6H5KL0Lydt8jrjKSRA6rVXIt9O1m%2B6Ijz7gM4IjUTkP8bx3A0tz%2BB0j%2FP9AfXnIqlHpkqy1Wm%2FpDxO22yeAxLPZkI%2FOz95I8T3ZLsdD%2FfQaDjHBriRdQ0U5vU%2FJDBUTqM32r45uWMIdwfKiID7yCRuOCj%2F9oO2Yw36X3yQY6pgGoCbJQ5Xzd3KWnK5SeALmHdRYQVVcE8%2FRRRJXac%2FKZHbSujytFshh8tOiogYt2v777MMzQrjo2Q6WXYWqaMWGdXWdrBiWSmD7XBGMsZBUfzBrTmMhh8E0iP3xhzcbvEjoOuM%2FaWU6W59xzKYr9yQIv6Ooy0ykjTwtUWvX7KqVBepBWqG1k8%2BstJoTGRpS4rCTfkwf02KU3ziLDOr%2Bg7nyoS1BqFgdZ&X-Amz-Signature=77ca758e3e5b37e6a0cd7e6ca232de2579350b45880135c90f194bacafbbfe1b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
```python
Player            Sadio Mané
Team               Liverpool
Games played              35
Games started             31
Minutes played          2753
Name: 6, dtype: object
```
---
**Extracting multiple columns or/and rows**
As soon as we extract multiple rows and/or columns from a DataFrame we get a **DataFrame **again.
![Extracting multiple rows](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/db277268-1e26-4fc0-baf8-b8c8daf05ddb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667JRKVN76%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T222453Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIBRCiiW0ClrEAvPlP1P5g%2FfSxSrRXhSjET8NKUZTYnxyAiEAmhyb8zf5uQCfULWArGWcFzI6ACBma9hk4haATUiwr70q%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDOrm1izUDx8LDtzbLSrcA2eiDIHl0CSJPZ6%2BWH%2BnHYY9Qo%2BMvVIcvOwJWAdVXAuRKrKAHXN8XhG4ov8M6x9nr5bChoKnKoS4uUdA1ViOaZN8DcyGtf44VWAFNiOzZonznPR53C6lQmDG3HI6NEiXtLGCzMJ4lg5DNGLk5fyBgwduhUngbi3JcsHppDDuuDi44t6af15S2ODokUbZ1vqFHvyQoQSXYlSLP1Kk97nmnwTGbSfyDxZtX%2BJmyd%2BCbSV6FKcy9XnnsdYvEGhY0oDpCEmmSm3ybM1GWWgk1ttevN3RZrzh4QZX9etO1TgbOrKVawQIWhojrk%2F3%2F2ZyXXuJvausGpOkcewyq3SHcxha5jYBoFCJc69idMLP6l6ibrN8Miqgo1FaB7CEf3xf8WwB4XdO0xmYKXLALS8g6K6iHBW17C5k38kjz9qed%2FB3VNNRkrUG0pM81YDSSPl4oOMsSQHvdCIoMP%2B621EaCJjmShVBvgj0LF4CqwVWmqa6q2gQxM6SyrjC91OWImLyB%2Bj7kz3fAzX9PbElpAcDYX57PXeU8RDsZkPsuuxP5KVVy0xpgl%2B2Lz9etES%2FvBh6dG0M%2B1e2bRcTaWZLL5vCEc76d4TfsPo2eVZZ9AT4O1GIDcMhnH%2B0ztexAs%2Bf9GK7MOfN98kGOqUBKp9Os1UmCJQpkAIaUZDPHxYlgWRtlhK0WG7FFDByRI9Znh0XW5aw%2BVthXFUXF5IpD6%2BfzMV1Lf63fct2rDBx3BbAYvwk9Deb10LEZ1rfEJDYy47J%2Fkc6kfmfSm8iVT0hvdCnhWMVePp%2FpVZhZw6Q7Y1Y9Yd%2FUm6K1tEfKmLSivJJBiNTo3gQNfDE%2BRxjNHQMMfm%2FzVVeXqgKx9AUwywDOCGOKrSC&X-Amz-Signature=912d8f4409be2175d9b22daa4fefda90556d45e8b0656a42352f3d88f1a261a2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
![Output when extracting multiple rows is a **DataFrame**](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/53af7edb-d0d0-4ea4-badb-fd3589227085/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S4XVMJ4M%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T222454Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIQDo3FmAL5MczZUFKgJK4ariqYvv7LxP1dXF1sEvQ754YgIgS8G7KhUBPajx%2B%2BRPxyiFG5MC4K68GLWedwUIi1Z3jHUq%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDNOb24he0i1sail6aSrcA2ugEvy3gC84tgociTtj1Wxon9csnfiBT%2Fg3hGvkiVXXEsmZ6BsWiHHrx0Aakl7xZTVYtLU9sr4s6QgY1vRuh%2FGqu516Ny5HOrRiUo9yEBEFGXpMzBclbBEs%2BUjWSUtAJ80eYRMIHxO%2BEyBGBFBr8K17mJJt5kVplkGQVwp5EcyHFxwc08xge11RqOrWPfjvzzsp41Nd89C6pk9ZreY%2BhyBD2nO27t7izDk69PxLDpSru1MC0d0ty5WU8NCtZkn%2By8GYEk3VvpVQw%2BqHF%2FZShPOirjC6DtlSyh9dPJ4%2FRv3DAKxHTlbVOyXjsiVZTE8TsNv1cN%2BFriLXMffCZXPFXB4%2F%2B%2F1fskZlE5i7fUEetCPhf5E2IZ1wwd1wabe%2Ftkq06UDjRKT%2BHFfjTg%2FAE1fwnqHPJuRQxCHJwKRNqTO8r6PWgua0iooZwp1Nk1AwbEa%2B%2BGsYB9WWPUArulCUorsKTHa%2BL27%2F%2BT2mHxUn2QLLRXFpL8um85p4MCMJQ%2BJiDkr8JpNieT20FG0MoZkQQo%2FSs53H2u1hSuMHDPP6KjCEwpuKvrcnPKs21Fw%2FhrDE33nv7D3LuuUJp0HfkxL1Ws5NrmKKNm9FY22%2F5f%2Bn4F%2B%2BUD3NOM0qmgETTqmqSDIoMMil98kGOqUByJp8FcO6SflJ7zlA6WdoRmA0IkvI0E8AC%2BG0onRlvG1eZYU2WcbKArSlmNTYM5pgBk8YqP8IUpSZ4Ae5MhuN4mmSsjbG3MuSHxNGXBBGdsHHYjGz5q8BEYgiizNuE%2BUTKsfWVoFaz6Kzpq9duov6mQVsU2UQfilm%2FCZtR3d6iDDedt6uiK12ofYP5hC%2BopkUJZmff6U6V%2Bgso4g%2Ft%2BN1iNB1bPYE&X-Amz-Signature=b984cea49d6c90f120357af8cb9f243ef27dde188f82a962aa9859aac01dc2dd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![Extracting multiple columns](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/88562ce7-4fca-4490-a353-3e11a90a77a1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663IEZA64S%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T222456Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJGMEQCIGLVYgtfi2eaFnEGc7UtecWo7vDHZ0Xq0IlOTayxdKjDAiBS%2FUBL%2BxGlmKGiPupKxMq6P6M7eCoBawnDtccU9XmBjSr%2FAwgnEAAaDDYzNzQyMzE4MzgwNSIMB6vP169ewf57wO6HKtwDnB7ieDCO8FlrA675GCvVl9sHvcyN%2BgHQPcK6HqYlT6tyEAtFncLClsm6rhn2OZq%2BbAs7kxpzT3plP8mkdITcp2uZu2DLxITRApjgl31ZO0FKaFDsuwH5coI9IJY6xAvPw3Lfp%2BtZjGSFALE1AeSguG0FdEDJdCH1SM7ZipqPYiTV4JQTNb7x5BNwhQRupxwLG5YamGvYwqLDCpxHCuVqLXFIzqV%2FzQASLc0sIdRrsmxiGxcPlB6vuBwx357wlIgqcXaibQZ70gTs4ht4qqNQ%2FMqb1sd9Vn5abgkCSTYJX2fY7DRscZpAwd7hoWyc8MiZ%2BTDxNZM5JJZLh8mtAtTSVQjFLqRZTT6om1%2BoI6TRpHIYmLoQCLGRjS5QGWSCix99x1MB0roKUiQgT8O18C0yM7F2TXP5jw2PvCzj7tzQf9%2FsnctFxY5YfvnobTnf0f0O2GQ4K%2BF0Vbr3edGdjy2q8bDHaW%2FbFj0X%2B0%2FPJfG93RzY8hJEOXAxf1KQpNJcn%2BBqtnuIvE9mS8epIvqUbA1Y0b7KPrEFVT8hk55H%2Fsx2z2A0ItFiZVGTA5Mi8OLSx61mkkohlM1qJYPf2WOHkaO56epktY5V0%2FGgOoCbQj8e0YYeGZAO1UuOhM4ePXwwjc73yQY6pgHkxRLcMOE2Vuw%2FQGb6%2FnPO0gWkSGwP9AN5bdLDERZJqzjEkQL%2BDkBMVnHE6kDax6m5fpxlypi%2B61RN1EYYN2zKRuyjWnmrQXjXXJaBMRD2c4ZLMCKI88pVnyT%2B2tFcqANfw0y9rTGc5EMnWyRcG1D36zk0CeqqNg3n6Kuz2kSdiilhi7kLPiXDqngnU8Dq36Nbbu%2BjwcxFD7kgN5bLR%2FfUNsv7toOk&X-Amz-Signature=5485c59e808ba104ab1a26624bd0234c2701e73cf7a19135475c4c2d9172d88f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)


![Output when extracting multiple columns is a **DataFrame**](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/ff1bc09b-155e-485d-847f-1d7a815793bb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665T3C274B%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T222457Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIHer%2BVPvD41CmbY5ZkVnQRILVRbq9r3Ij%2BND7w9SgLG6AiEAxvWfUQcp243jGngMrmwEcjhK%2FNjfEleTzNC9R6lOGNEq%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDGstLcNN8wWqXR%2B8EyrcA%2FQceL0I0xt6sDZDdldAENyamXPHOLLC19pNnQg4MaG4vNDd0mFED4%2BnEgIAcmE0FIbAa8N8PSy%2BBSooB5Z4ubGKQbQZmV9YNM1PctBOh23ThQlvC%2F7q0Wd2%2FUBatk3bCdHkVkxXlaHGQn%2BBQpaM8BvCQe4hzqdF7kpQmHzAxyGKRJoJW5KPAjKQCpHk5zzKRPxU%2BTWLpln1kBbfamvMso8dr9rhkTguvlNvzCjXpnUTWBSqcYiBivr%2Bo5Cifa8UCAJjYqweKp9pvyQh3c%2BOr5YONM8BTwtHRHPmN%2FG0dUGCVtV7NhmuZghsz%2FrgwLAU1RostK7hEdYvQ6M9bYojwZBQNT9EmZdUSlM3vFt9CAZvTpi%2BhzRDVwphT2Pjv7i%2FIKIjLVIEX%2Bqa3FYo1nG4xrICGsDQT0Oq4d4Mm%2Fz%2Fax5XsesC3nK%2BcGu3QiuhJ%2B49VVgm4GwBZyz1ZtQtTbRCNd%2FQl7flIn39FkZahqnFEoIap5F8TAf%2Fj1VjtosGQ%2FrEAe%2FOcFALrhw87EHTUboWCkcYROWCSb%2BB6vN7W5KPGcg3MOTcTeOhUVUnLWSMaBwUtxqrUIctRQ3WAjaKogamR0K%2BB07JkJSCxMeivb4o17a%2BxWv%2FqIrBv9PjuhtxMLim98kGOqUB8M16um9lMx%2BCXfh0RXhJXS9N8jEraiwP4t6YHg5ck2dRdtkHi7CDVHLhwVIc3ncX4rbAT2TvQ%2BPIi%2BZOpOtm0PmpsB6joxdPSl4ePEQtsTmUR7O2R6oQuaRaIx4QX1OR3vNFP%2B1l2PN4zf%2FG6nd7UKq25kaIjqw6NO0S4zhKfM3PM2DM5lVNIVnb%2B3qXAdMyXOoMAOUnoZ9CycLnMBVP8P5Jfaf3&X-Amz-Signature=36caf99ff021e5786d2bc57c1e080cad54172432225f8a45567fe71772c4baed&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
![Extracting multiple rows and columns](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/157b953e-6021-4b2c-b126-69f5f0f25e99/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662P7K3HFZ%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T222458Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIEDl4cBdYblCIarpVg0V456g1aeiCUgHLPakx6C9pmQKAiEAqVDyBPw88RmUjY967UMpay8KGrvWXFVsyJET01eU6o0q%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDIhAZSYmiT481IdMuyrcA6mGEqZKzt6oBakaFAMsHSxJyErd9XufxHDyVEMfs4ZlEt5jTeWnaXVOwoMJ0qm7Xf6VCXGxsI%2FZexMDs7qmlC7lwsbqCxcQqeXJks2e6bhsApRcs90eujjG%2BY5%2FpNds0ySKy5E8kTgNw6YFdkxp5IBuNtqVrKMpSkZwZ8RNFugiBOfQIQG9rsf%2BH96ptgjshxXqFeMSz3V64JExUPPT3iQ0i9wAzMjz%2BydTRnfEzn7L4Of8JC0Jo6ya%2Brq9dcDJ0NRso0TBReMUzl9yVCeWQoUpUuWTSHblyNyGRYpJBCs4q%2F6QcDamS2qLWuOqcUbjbaax8Nr7ESKBBZR%2BVb8IuK%2BdGM9FmdsKxKbbN9znpqYu69PB53hW6%2B3BrMYaKqEVf3L0C9km7lw%2BEpra8A96UAg7GmBmtLmeqo%2FdfzIlMymdUvFc7sU4g6sjiJkdcpNwJ18bMn6GTi%2B4gCUlFMqlYbbi0E29gmni3kiDwUCWtiQJVMgu98Mpi5oSpX%2FyQ6c%2FNMJ4w0Au0rJNGolMUpEySUnb%2F%2BCPMOLN3MLHCSfV%2F9kXSWSFWlVQgAt1wWXI0bZ%2BzUBD6JEvjMeesn1v2PmUQge69US0bppIrzumMvzeJaGUGLH8S8%2Bgmv8LAemuMLXO98kGOqUBHwo7aLGOJ81ycCAt9VxNB7BCWPIscpwFWrgGNLWlC8xayfyPDgYrQxYdDLBumv%2BQ0pRySwnJC00b3Ok5StJxWiJU%2B3tAs8JiwTzUhhkTobu6mx%2BfFvSSMNwOPn2F5Yq00BABI2shhD9kE1VIyxRTWHH84gBYG1xIWEhGF%2FNS3jZ8gAmhrFTJ5pta3IiPK61%2FQYc9QfMET%2BNc%2Buego9yR7y4ioiFb&X-Amz-Signature=cb9c74704ec251f3c2c69cf6c7e2adf10b40f0de94968e564b73e044547a48d3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
![Output when extracting multiple rows and columns is a **DataFrame**](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/dcbc1d74-aa73-4627-a883-76d56aaef98c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZZVAHZKM%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T222458Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIQCmukzCLyOuchNngF2TqEFST6jY%2FhPSUWwprl7ZaaLVbAIgYCH%2FmGIV0MhMV5k2kJBMl%2BnQj3V74ozNikj%2Fv4nMhN0q%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDAWMJp3wAsjvlGNmzSrcA9Mk4cg0ipWd%2F%2BOIpNMIPQQOZHCWg6DUevopz9K9xYckgW2I%2Br4%2Bsx7JUy5TSTuHv7nOpR%2FyQ4vEwa7RyT4o61W7oF2BcjHeoGVZTIUU0SPAB%2B%2FzW2WoBlZZswPssGGUluKp7TeR2VXUDVOYBboUe%2FbYzdt8bPjgosRKRBSdawgS2AOwzAJfwK7rrQwLMCLe3YwvDwDdI1FxHOup%2FMX3mvvaAlnmTpFMnkTBi%2BSIKU7H1QiI65aHycOfJfJlJ2dEY2XnRqXrC6jPjECMK3YyprFdX1v7bV09o6xJOg5VBnR2L6ukXl1ZV8%2BMewopnzP6ZxO3w6D%2BJZzCkOeS3zYQE8ReOFyOSkdBZCTKAxTdH48YioM6bXGrFtqzcao4Mquzbpu4jTmobXCtXVZrIDejRUClAsmp%2FIHcy8%2Fd0rj7WMby6zaOWugKibG%2BqZrzcGJA%2FPVBm4Lo4gKkLZl18nTq7rMJLM79hxUx4onvWxIzSVbApBOuknv6ig4%2BKP%2BLA%2FRW9i2%2BpZhefYEOsX2dWvJZ2NuaUWuefzvK%2FFzIm1Fwh8J5HAp7IHxPtZAIXw4bML30NBZXRdrZclq0ozNPp12pWnWl2pl8VjdT8AfdsR%2Fz6sfT%2Fi%2FXkDiOyncUzoyoMOSl98kGOqUBwnS2R%2FBEvOHRue6fA90GSCdgbYn1xMC2hxR6SM6LXtvVrZ5B%2Bk2dxbY9NMFdOANRKUXwnk3NX0BiaXp4o5HZdmodbC11bvoQH2FJrk8M6MQUshdTwX9Anwi3HwYX60CuwMSg9BM4i8RRanYIqUR%2FhjqSggspRnMNOsrrArkEKLiUECvjsGxxIDfXqalg6Qx9tGmR1FNF6UCotynKb8ZRPqxMdGur&X-Amz-Signature=0cf6fe4d75a033549db677a7a55fe3f17a5ef4e0885bddc22b71e70df6939454&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
---
# Functions
---
Below you find an overview of the most important Pandas functions that you should be familiar with and remember. All examples are based on the DataFrame `players_df` that contains football player data from the premier league season 2019/2020.
![players_df](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/88ad3bb4-c8e5-4d76-a3d9-ecf4028c834b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QJBC23E4%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T222500Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJIMEYCIQDdH2AROXcNm4HNIMub8wfGa3wo7JK5Y7LeYd%2F0%2BBNeVAIhAPrMIAwfsVrTkl6PeyxRRHAdNtadclv%2F9tIYkGkUs16LKv8DCCYQABoMNjM3NDIzMTgzODA1IgxK8bW3YXKMmPFtZjUq3APgYxm0HtIulrM3rfOvqi1uub606d%2BwBTUuvP%2Fg2pAMKMPFk68DUA7CGsN1ZWDVeQr9KYrSx2hb5bRA%2BNKasY9WJMbe23Xv5cMN35T%2B1zOwwvespk5ikwYqhFf2D%2FygN02RR0EYQRsqKXboPmo3H1%2F7BxL%2FQlMLh56wRM3PtOFCf2hAbVtsVxgT8begO2bCz7QhtP25IpivU6g7aodDFI6XjwkMboGfrS6OVeEW4haP9gw5gVXKpen0%2B4g00EHPK%2FrZUlnQIS%2Bh5FU46vmPyTUFgNGkJh%2FJ0htrPAzDGE03MB25drUiZL18sCaVa9ffXmlafDJ%2FNHcI%2BS852Odd%2F2aCfXKG44Op7ZSpiaNmypy25kU3L9Rl7lpCeBetgY2aZNR4HVQHx9qJSzdXGYr968Jc3katu2S4gwN36c80Q3FuohPIDWCuaPoKz0Vz3D1B3eFzuxcUsq76qfp074okLgYj5r7TftXmaP2Fn34qbf9RGNCBiZ%2FGa7PEtKPzn6AoZL3ErMAMewJhHLBE%2FicH4v%2BaR3LhRWKtPlxSBQkIhQY5%2BBwGJPZUvcbLnZ2pgxF2b0bCjDOGxDgidR%2F3tU5da4QfyqldhejXnOJSxOxQKe%2FaDgArjpntvciAva42UDCspvfJBjqkAR39jw3CJNGSzw2fkUD4sDgTuietGoqpW9HeUw47hmg5PO9sSU5DfPuIUx1mA%2FCnHqiQVBxHZVKlU4lcK19W5A9XcvGRiMNDlJBhg1UuCC%2Fuv%2FFFjHAnKUdS9ZnWOaDNmQja6nez1En%2Buc9HW6h4TPcgb2Kq2YqHCyjDyvXTecv1DmyEQ7%2FihbWqcxul81sY4e0cWMEmqEgyVcndUnHACniZEjG1&X-Amz-Signature=54091926865c3fdde6b26912112e0e5f6824c09de994f5e68fbbc943f4880d31&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
*`Priority functions`
## [`.DataFrame()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html)
---
**Syntax**
With this function we can create a new Pandas DataFrame. Loading the data into a DataFrame is always the first step before any other operations. 
The syntax is as follow:
`pd.DataFrame( << input data >>, << index column >>, << column names >>)`
The input data can be a numpy array, dictionary or another iterable. The first two formats are more common which is why we cover them in examples below.
---
**Creating DataFrame from numpy array**
Let’s assume we have the following numpy array `my_data_array` that contains data about exercise time and calories burned. 
```python
array([[420,  50],
       [380,  40],
       [390,  45],
       [610,  60],
       [700,  70]])
```
Each sub-list represents one observation from our experiment. The first value is the calories burned and the second value the duration of exercise.
To load this data now into a Pandas DataFrame we can execute the following command:
```python
import pandas as pd

df_experiment_array = pd.DataFrame(
	data=my_data_array,
	columns=['Calories', 'Duration']
)
```
![df_experiment_array](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/c2d3b467-0a74-4a15-8374-6aa18fcf8e55/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VKZ24O6G%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T222501Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJIMEYCIQDWSH%2BMLbG%2F%2B2s2I%2F2GaufL8%2BPN%2F5QSNDWjyGAAs%2B4GbgIhAN2Xv3r7dRBm2wafea0KJzCXdDFTnLm7LCNRRfZ1lko2Kv8DCCYQABoMNjM3NDIzMTgzODA1IgyyD8XRQ7MVIRa%2Ff5Aq3ANk8fFTillKFcsv4HUdsLbIKGpexpQU%2BAHy%2BJ5SE3lG7cd22zgdQtJASdBPPqjdvGuUJkNzI1aGBiHk23gsaaqHeFe2R6Kf6%2Fgj83SIll7IFLr5RmfDB9M8a77yDJZPLMUwaQrlUYDRJa6UDxnn8h9zr0I3QpTI0oNs%2BJC3CKG%2BOS9Dn5r36fRpgWe8p%2FTvtqjTk7N3%2BwgNVlqo51zozzWIHOCCZZSCxfGS1se8OMsKm06OYl3BUiymEKSfCB1UCUwjvYIooJ9YgFzO2%2FQQBNc5vaUxUP1K21owdm3z5tMPUowYxvn2HXORs3DEu9AHQK%2F1gVm%2BlqUtoolKajSn69MDSygx%2F7495BXg1dvMD6edo4Yi5cHmG538ei%2Bwzrp7M69TJ5A2gXW1O%2BFqQWEBEA%2F86g52dcy2tVw2y7uuId4mwiKuWamec4fNuPH1o7bOORWPnPR8NckmWbXqPt9eGoa1u%2BcepzEitdAEkDFCQ8oYQ8%2Fd7eUQgz9DmFvEH%2Fjz7AmPdE%2F%2BFzzYXHVQtGcJOiySh8sKUcofFs1v3g3FnmjrSsufKUNz9R4oBvTTfhI4%2FvuajwSa1eB%2BB8MqawvgkSwd9MUf4uGuOUYvbzAcpsQnIr7J1G4R8zUrydnu7TCYpvfJBjqkARI14Y4G%2B%2FcbfcvDeEk5pNx%2BUU%2F6JlNbJobfjaONqlyO6kiK3nL73PazxE3y0QWFs0ngyugaudsNuMZ7Y7rV02E0ffSAU51m24yCuHd1v3xKZenAe2XFlUrMZGOqLB8Q2juxlTPwhYCbTJW7VkAMSXDdTzF57F3SinaG0VF6I4vR8OfdJk8LnlTzqlRbMkdQ1JdbVmSynTHQj2dP9HQSGfhXhspv&X-Amz-Signature=e434f1c83717c04376391caa99a49efb0f872a03e933c79b7acbfce07ff6f09c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
From the code snippet we can see that we explicitly specified the `columns=` parameter. This was because Python normally expects the `index=` parameter at second position in this function. Because we did not provide a value for this parameter, a default index was assigned (0, 1, 2, 3, 4). 
---
**Creating DataFrame with custom index**
If we want to use specific values as index we can do so by specifying the `index=` parameter. Let’s assume we know the names of the participants in the experiments and we want to use these as index. We can simply wrap all the names into a list and pass this list as second parameter into the function.
```python
import pandas as pd

df_experiment_index = pd.DataFrame(
		data=my_data_array,
		index=['Caroline', 'Jack', 'Melanie', 'Frank', 'Herbert'],
		columns=['Calories', 'Duration']
)
```
![df_experiment_index](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/53a19e91-90aa-4e2d-9cd8-cb3d1fc18aee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VKZ24O6G%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T222501Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJIMEYCIQDWSH%2BMLbG%2F%2B2s2I%2F2GaufL8%2BPN%2F5QSNDWjyGAAs%2B4GbgIhAN2Xv3r7dRBm2wafea0KJzCXdDFTnLm7LCNRRfZ1lko2Kv8DCCYQABoMNjM3NDIzMTgzODA1IgyyD8XRQ7MVIRa%2Ff5Aq3ANk8fFTillKFcsv4HUdsLbIKGpexpQU%2BAHy%2BJ5SE3lG7cd22zgdQtJASdBPPqjdvGuUJkNzI1aGBiHk23gsaaqHeFe2R6Kf6%2Fgj83SIll7IFLr5RmfDB9M8a77yDJZPLMUwaQrlUYDRJa6UDxnn8h9zr0I3QpTI0oNs%2BJC3CKG%2BOS9Dn5r36fRpgWe8p%2FTvtqjTk7N3%2BwgNVlqo51zozzWIHOCCZZSCxfGS1se8OMsKm06OYl3BUiymEKSfCB1UCUwjvYIooJ9YgFzO2%2FQQBNc5vaUxUP1K21owdm3z5tMPUowYxvn2HXORs3DEu9AHQK%2F1gVm%2BlqUtoolKajSn69MDSygx%2F7495BXg1dvMD6edo4Yi5cHmG538ei%2Bwzrp7M69TJ5A2gXW1O%2BFqQWEBEA%2F86g52dcy2tVw2y7uuId4mwiKuWamec4fNuPH1o7bOORWPnPR8NckmWbXqPt9eGoa1u%2BcepzEitdAEkDFCQ8oYQ8%2Fd7eUQgz9DmFvEH%2Fjz7AmPdE%2F%2BFzzYXHVQtGcJOiySh8sKUcofFs1v3g3FnmjrSsufKUNz9R4oBvTTfhI4%2FvuajwSa1eB%2BB8MqawvgkSwd9MUf4uGuOUYvbzAcpsQnIr7J1G4R8zUrydnu7TCYpvfJBjqkARI14Y4G%2B%2FcbfcvDeEk5pNx%2BUU%2F6JlNbJobfjaONqlyO6kiK3nL73PazxE3y0QWFs0ngyugaudsNuMZ7Y7rV02E0ffSAU51m24yCuHd1v3xKZenAe2XFlUrMZGOqLB8Q2juxlTPwhYCbTJW7VkAMSXDdTzF57F3SinaG0VF6I4vR8OfdJk8LnlTzqlRbMkdQ1JdbVmSynTHQj2dP9HQSGfhXhspv&X-Amz-Signature=1143ea18e9ea0fe4130ba25e0e7948f84790ad8178cbd4ee7bfc2573fa56c29c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
*Disclaimer: Because we comply again now with the order of the parameters (index at second position, column names at third position) we don’t need to explicitly specify the parameters anymore, i.e., we can remove **`index=`**.*
---
**Creating DataFrame from dictionary**
We can also put the same data from the experiment into a dictionary first called my_data_dict.
```python
{
	'calories': [420, 380, 390, 200, 100],
	'duration': [50, 40, 45, 60, 70]
}
```
We can see that the structure between `my_data_array` and `my_data_dict` differs. In the array we inserted each observation one by one. In the dictionary however we have the values column-wise, meaning that the column name is the key and its associated value are all the values that should be inserted in this column.
As the column names are already in the dictionary (as keys) we can get rid off the `columns=` parameter and simply execute the following command:
```python
import pandas as pd

df_experiment_dict = pd.DataFrame(data)
```
![df_experiment_dict](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/c2d3b467-0a74-4a15-8374-6aa18fcf8e55/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VKZ24O6G%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T222501Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJIMEYCIQDWSH%2BMLbG%2F%2B2s2I%2F2GaufL8%2BPN%2F5QSNDWjyGAAs%2B4GbgIhAN2Xv3r7dRBm2wafea0KJzCXdDFTnLm7LCNRRfZ1lko2Kv8DCCYQABoMNjM3NDIzMTgzODA1IgyyD8XRQ7MVIRa%2Ff5Aq3ANk8fFTillKFcsv4HUdsLbIKGpexpQU%2BAHy%2BJ5SE3lG7cd22zgdQtJASdBPPqjdvGuUJkNzI1aGBiHk23gsaaqHeFe2R6Kf6%2Fgj83SIll7IFLr5RmfDB9M8a77yDJZPLMUwaQrlUYDRJa6UDxnn8h9zr0I3QpTI0oNs%2BJC3CKG%2BOS9Dn5r36fRpgWe8p%2FTvtqjTk7N3%2BwgNVlqo51zozzWIHOCCZZSCxfGS1se8OMsKm06OYl3BUiymEKSfCB1UCUwjvYIooJ9YgFzO2%2FQQBNc5vaUxUP1K21owdm3z5tMPUowYxvn2HXORs3DEu9AHQK%2F1gVm%2BlqUtoolKajSn69MDSygx%2F7495BXg1dvMD6edo4Yi5cHmG538ei%2Bwzrp7M69TJ5A2gXW1O%2BFqQWEBEA%2F86g52dcy2tVw2y7uuId4mwiKuWamec4fNuPH1o7bOORWPnPR8NckmWbXqPt9eGoa1u%2BcepzEitdAEkDFCQ8oYQ8%2Fd7eUQgz9DmFvEH%2Fjz7AmPdE%2F%2BFzzYXHVQtGcJOiySh8sKUcofFs1v3g3FnmjrSsufKUNz9R4oBvTTfhI4%2FvuajwSa1eB%2BB8MqawvgkSwd9MUf4uGuOUYvbzAcpsQnIr7J1G4R8zUrydnu7TCYpvfJBjqkARI14Y4G%2B%2FcbfcvDeEk5pNx%2BUU%2F6JlNbJobfjaONqlyO6kiK3nL73PazxE3y0QWFs0ngyugaudsNuMZ7Y7rV02E0ffSAU51m24yCuHd1v3xKZenAe2XFlUrMZGOqLB8Q2juxlTPwhYCbTJW7VkAMSXDdTzF57F3SinaG0VF6I4vR8OfdJk8LnlTzqlRbMkdQ1JdbVmSynTHQj2dP9HQSGfhXhspv&X-Amz-Signature=e434f1c83717c04376391caa99a49efb0f872a03e933c79b7acbfce07ff6f09c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
---
**Creating DataFrame from Pandas Series**
We can also create a DataFrame from multiple Pandas Series. Let’s assume we have created following two Pandas series: 
```python
import pandas as pd

series1 = pd.Series([1, 2, 3, 4], name='Numbers')
series2 = pd.Series(['one', 'two', 'three', 'four'], name='Words')
```
Next, let's see how we can create a DataFrame using multiple Series. Each series would form a column in the DataFrame.
```python
df_from_series = pd.DataFrame(
	pd.concat([series1, series2], axis=1)
)
```
In the above code we are concatenating the two series along the column columns (`axis=1`) to form the data for the DataFrame.
And the output will be a DataFrame where `series1` forms the 'Numbers' column and `series2` forms the 'Words' column:
![df_from_series](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/5f54bd84-3819-4a73-a684-e0962888e550/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VKZ24O6G%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T222501Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJIMEYCIQDWSH%2BMLbG%2F%2B2s2I%2F2GaufL8%2BPN%2F5QSNDWjyGAAs%2B4GbgIhAN2Xv3r7dRBm2wafea0KJzCXdDFTnLm7LCNRRfZ1lko2Kv8DCCYQABoMNjM3NDIzMTgzODA1IgyyD8XRQ7MVIRa%2Ff5Aq3ANk8fFTillKFcsv4HUdsLbIKGpexpQU%2BAHy%2BJ5SE3lG7cd22zgdQtJASdBPPqjdvGuUJkNzI1aGBiHk23gsaaqHeFe2R6Kf6%2Fgj83SIll7IFLr5RmfDB9M8a77yDJZPLMUwaQrlUYDRJa6UDxnn8h9zr0I3QpTI0oNs%2BJC3CKG%2BOS9Dn5r36fRpgWe8p%2FTvtqjTk7N3%2BwgNVlqo51zozzWIHOCCZZSCxfGS1se8OMsKm06OYl3BUiymEKSfCB1UCUwjvYIooJ9YgFzO2%2FQQBNc5vaUxUP1K21owdm3z5tMPUowYxvn2HXORs3DEu9AHQK%2F1gVm%2BlqUtoolKajSn69MDSygx%2F7495BXg1dvMD6edo4Yi5cHmG538ei%2Bwzrp7M69TJ5A2gXW1O%2BFqQWEBEA%2F86g52dcy2tVw2y7uuId4mwiKuWamec4fNuPH1o7bOORWPnPR8NckmWbXqPt9eGoa1u%2BcepzEitdAEkDFCQ8oYQ8%2Fd7eUQgz9DmFvEH%2Fjz7AmPdE%2F%2BFzzYXHVQtGcJOiySh8sKUcofFs1v3g3FnmjrSsufKUNz9R4oBvTTfhI4%2FvuajwSa1eB%2BB8MqawvgkSwd9MUf4uGuOUYvbzAcpsQnIr7J1G4R8zUrydnu7TCYpvfJBjqkARI14Y4G%2B%2FcbfcvDeEk5pNx%2BUU%2F6JlNbJobfjaONqlyO6kiK3nL73PazxE3y0QWFs0ngyugaudsNuMZ7Y7rV02E0ffSAU51m24yCuHd1v3xKZenAe2XFlUrMZGOqLB8Q2juxlTPwhYCbTJW7VkAMSXDdTzF57F3SinaG0VF6I4vR8OfdJk8LnlTzqlRbMkdQ1JdbVmSynTHQj2dP9HQSGfhXhspv&X-Amz-Signature=19faacc2657024aed1911144ff4453bfac09fb2ba0c45159ef981941ebda49cf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
---
## [`.read_csv()`](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html)
---
**Syntax**
Often we have data stored in external files such as .csv and must load it from the file into a DataFrame. This function allows us to do this:
`pd.read_csv( << filepath >> , delimiter= << delimiter >> , index_col= << column name >>, names = << custom column names >> , header = 0)`
Usually, we pass the `header=0` parameter only if we pass a value for the `names=` parameter, i.e., if we want to use customised column names.
---
**Reading data from a .csv file into a DataFrame**
Let’s assume we have a file called `player_stats.csv` that is stored in the same folder as our script.
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/00b58605-9e39-4338-9ad5-30ab0035c39e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YMY7XNHL%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T222502Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQDT15oBw1BLIuPSinfvciykq2sWdH66ByIIokq892Zz1AIhALZX5BB%2BuLU%2FymNR%2Fy5NAmwzWCjXqow2N16WW1gBr68UKv8DCCcQABoMNjM3NDIzMTgzODA1IgyeY1KMXAig2rpstu8q3AO5VffOl8SbxneQ6dW8FQW3jalnq%2FZcoZqRZ43XKpHerKGSBvbEqRWHjqjXrf3r6cxrliY8eOcOGv3Dlr968H%2FRkXYLz1DfgTJbr5hCDvwiFfBmWETyl5fN%2BwA%2BOWqIBQAGtaqBzomGwnYXjcVkVQ%2B1g8SguwRSjPmGe5vgVco%2BCAityq%2Bkh5ZsbA6LyaZCtgu6x4DNlaZqfoqkAHvwUwm%2FF6P8hHlI94PmZnWgsXAcWr0f2qiT%2Fm4ILVm6AcvqVIRC8acTkA3CGifSpr7EOnDwCxMZxnRUURrFteFSOsyZtE5BzpsXWTjUZr80Q1AATu0lFckCAeUipaNmGWPU4LrvFxZ%2FHOzCYQfWiebZxAmfiGgHZVOgXXVY5wBbeQcnZFm85GqmwzuwyWao%2BJJLSbKt4ddIZE3m37IQbmrVOzkmvYWRJ7YzAV25Hd1yvhct5oEx2MDIfCuKqTG29%2BUVZ8LvoAldbuWhLYil5HCgYaQ8N87h47HdqmQyPSvOD8zZg1wmoBCeYE%2FrhNil4H16WNSFPXK3gX%2FVVV2nd%2F2Nlw4vtCnkp5i6gDRCxrz8U%2FjseDjJmn41WT4P487h1Gh3xgdWQ9UUoFHoQ6wPdyS1gLJzQRc7tM%2F%2F4UwcZmiicDCgzvfJBjqkAWglt2lMZIEh8agX0AxqjvRG4HfoAgKUsXBaf1K5rT5BZPE0EmlZjnLjqIS2F4aHCWYWIN22FtK%2FCP%2FpI75I9soXmeANDDWo6CpXTbDtctFRj0qH9UyAIOw%2BvrGuc0v%2FbjDiIV%2BUb5C%2FC%2BskjK40CqD6fM3XZ1MhUG7r7owk4vEtlOqeTpWQOc0uO7l3SabDOkio2ogjg4BmoKhKK1a1dqM30yu1&X-Amz-Signature=09c86a5b886f4f8fb7efed0e313ac767267c8361d7490db6cdc2e4312737209a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
As you can see in the screenshot above, the file is in .csv format and the standard delimiter (`,`) is used. Thus, we can set `delimiter=','`. Also, we want to use the column `Rank` as index. Thus, we can set `index_col=0` as Rank is the first column or specify it explicitly with `index_col='Rank'`.
Finally, we can load the data into a DataFrame with the following command:
```python
players_df = pd.read_csv('player_stats.csv', delimiter=',', index_col='Rank')
```
![players_df](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/f9cbeba1-616f-40cf-839e-52bc9ce45d8e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YMY7XNHL%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T222502Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQDT15oBw1BLIuPSinfvciykq2sWdH66ByIIokq892Zz1AIhALZX5BB%2BuLU%2FymNR%2Fy5NAmwzWCjXqow2N16WW1gBr68UKv8DCCcQABoMNjM3NDIzMTgzODA1IgyeY1KMXAig2rpstu8q3AO5VffOl8SbxneQ6dW8FQW3jalnq%2FZcoZqRZ43XKpHerKGSBvbEqRWHjqjXrf3r6cxrliY8eOcOGv3Dlr968H%2FRkXYLz1DfgTJbr5hCDvwiFfBmWETyl5fN%2BwA%2BOWqIBQAGtaqBzomGwnYXjcVkVQ%2B1g8SguwRSjPmGe5vgVco%2BCAityq%2Bkh5ZsbA6LyaZCtgu6x4DNlaZqfoqkAHvwUwm%2FF6P8hHlI94PmZnWgsXAcWr0f2qiT%2Fm4ILVm6AcvqVIRC8acTkA3CGifSpr7EOnDwCxMZxnRUURrFteFSOsyZtE5BzpsXWTjUZr80Q1AATu0lFckCAeUipaNmGWPU4LrvFxZ%2FHOzCYQfWiebZxAmfiGgHZVOgXXVY5wBbeQcnZFm85GqmwzuwyWao%2BJJLSbKt4ddIZE3m37IQbmrVOzkmvYWRJ7YzAV25Hd1yvhct5oEx2MDIfCuKqTG29%2BUVZ8LvoAldbuWhLYil5HCgYaQ8N87h47HdqmQyPSvOD8zZg1wmoBCeYE%2FrhNil4H16WNSFPXK3gX%2FVVV2nd%2F2Nlw4vtCnkp5i6gDRCxrz8U%2FjseDjJmn41WT4P487h1Gh3xgdWQ9UUoFHoQ6wPdyS1gLJzQRc7tM%2F%2F4UwcZmiicDCgzvfJBjqkAWglt2lMZIEh8agX0AxqjvRG4HfoAgKUsXBaf1K5rT5BZPE0EmlZjnLjqIS2F4aHCWYWIN22FtK%2FCP%2FpI75I9soXmeANDDWo6CpXTbDtctFRj0qH9UyAIOw%2BvrGuc0v%2FbjDiIV%2BUb5C%2FC%2BskjK40CqD6fM3XZ1MhUG7r7owk4vEtlOqeTpWQOc0uO7l3SabDOkio2ogjg4BmoKhKK1a1dqM30yu1&X-Amz-Signature=0b716986e690bef505f12590b3dcf7d31fe6b86e2476c33a3683517e605ff7f3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
---
**Customising the column names**
If we want to customise the column names, we can pass an additional parameter `names=` into the function and assign it a list as value that contains all column names.
```python
column_names = ['Rank', 'Football player', 'Football team', 'Games', 'Games started', 'Minutes played', 'Goals scored', 'Assists provided', 'Shots made', 'Shots made on goal']
players_df = pd.read_csv('player_stats.csv', delimiter=',', index_col='Rank', names=column_names)
```
![players_df with odd first row](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/775e4236-68c7-4d20-86a5-f92c490d9fce/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YMY7XNHL%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T222502Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQDT15oBw1BLIuPSinfvciykq2sWdH66ByIIokq892Zz1AIhALZX5BB%2BuLU%2FymNR%2Fy5NAmwzWCjXqow2N16WW1gBr68UKv8DCCcQABoMNjM3NDIzMTgzODA1IgyeY1KMXAig2rpstu8q3AO5VffOl8SbxneQ6dW8FQW3jalnq%2FZcoZqRZ43XKpHerKGSBvbEqRWHjqjXrf3r6cxrliY8eOcOGv3Dlr968H%2FRkXYLz1DfgTJbr5hCDvwiFfBmWETyl5fN%2BwA%2BOWqIBQAGtaqBzomGwnYXjcVkVQ%2B1g8SguwRSjPmGe5vgVco%2BCAityq%2Bkh5ZsbA6LyaZCtgu6x4DNlaZqfoqkAHvwUwm%2FF6P8hHlI94PmZnWgsXAcWr0f2qiT%2Fm4ILVm6AcvqVIRC8acTkA3CGifSpr7EOnDwCxMZxnRUURrFteFSOsyZtE5BzpsXWTjUZr80Q1AATu0lFckCAeUipaNmGWPU4LrvFxZ%2FHOzCYQfWiebZxAmfiGgHZVOgXXVY5wBbeQcnZFm85GqmwzuwyWao%2BJJLSbKt4ddIZE3m37IQbmrVOzkmvYWRJ7YzAV25Hd1yvhct5oEx2MDIfCuKqTG29%2BUVZ8LvoAldbuWhLYil5HCgYaQ8N87h47HdqmQyPSvOD8zZg1wmoBCeYE%2FrhNil4H16WNSFPXK3gX%2FVVV2nd%2F2Nlw4vtCnkp5i6gDRCxrz8U%2FjseDjJmn41WT4P487h1Gh3xgdWQ9UUoFHoQ6wPdyS1gLJzQRc7tM%2F%2F4UwcZmiicDCgzvfJBjqkAWglt2lMZIEh8agX0AxqjvRG4HfoAgKUsXBaf1K5rT5BZPE0EmlZjnLjqIS2F4aHCWYWIN22FtK%2FCP%2FpI75I9soXmeANDDWo6CpXTbDtctFRj0qH9UyAIOw%2BvrGuc0v%2FbjDiIV%2BUb5C%2FC%2BskjK40CqD6fM3XZ1MhUG7r7owk4vEtlOqeTpWQOc0uO7l3SabDOkio2ogjg4BmoKhKK1a1dqM30yu1&X-Amz-Signature=0f0abca85cadb6fad4415a2b95ab5444cfe9dad56c6e508534efd0e816f2aaf3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
As you can see in the screenshot above, if we load the data like this then we have a very odd first row inserted into our DataFrame. This is because we are specifying our own column names so Pandas thinks that the first row in the file is just a regular row although in fact it is the original header row. 
For this reason we need to insert another parameter `header=0` which tells Pandas that the first row in the file is header and thus should be ignored / not included in the DataFrame.
```python
column_names = ['Rank', 'Football player', 'Football team', 'Games', 'Games started', 'Minutes played', 'Goals scored', 'Assists provided', 'Shots made', 'Shots made on goal']
players_df = pd.read_csv('player_stats.csv', delimiter=',', index_col='Rank', names=column_names, header=0)
```
![players_df with customised column names](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/763f8490-e513-40f0-b9da-8aa9e83e5c77/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YMY7XNHL%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T222502Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQDT15oBw1BLIuPSinfvciykq2sWdH66ByIIokq892Zz1AIhALZX5BB%2BuLU%2FymNR%2Fy5NAmwzWCjXqow2N16WW1gBr68UKv8DCCcQABoMNjM3NDIzMTgzODA1IgyeY1KMXAig2rpstu8q3AO5VffOl8SbxneQ6dW8FQW3jalnq%2FZcoZqRZ43XKpHerKGSBvbEqRWHjqjXrf3r6cxrliY8eOcOGv3Dlr968H%2FRkXYLz1DfgTJbr5hCDvwiFfBmWETyl5fN%2BwA%2BOWqIBQAGtaqBzomGwnYXjcVkVQ%2B1g8SguwRSjPmGe5vgVco%2BCAityq%2Bkh5ZsbA6LyaZCtgu6x4DNlaZqfoqkAHvwUwm%2FF6P8hHlI94PmZnWgsXAcWr0f2qiT%2Fm4ILVm6AcvqVIRC8acTkA3CGifSpr7EOnDwCxMZxnRUURrFteFSOsyZtE5BzpsXWTjUZr80Q1AATu0lFckCAeUipaNmGWPU4LrvFxZ%2FHOzCYQfWiebZxAmfiGgHZVOgXXVY5wBbeQcnZFm85GqmwzuwyWao%2BJJLSbKt4ddIZE3m37IQbmrVOzkmvYWRJ7YzAV25Hd1yvhct5oEx2MDIfCuKqTG29%2BUVZ8LvoAldbuWhLYil5HCgYaQ8N87h47HdqmQyPSvOD8zZg1wmoBCeYE%2FrhNil4H16WNSFPXK3gX%2FVVV2nd%2F2Nlw4vtCnkp5i6gDRCxrz8U%2FjseDjJmn41WT4P487h1Gh3xgdWQ9UUoFHoQ6wPdyS1gLJzQRc7tM%2F%2F4UwcZmiicDCgzvfJBjqkAWglt2lMZIEh8agX0AxqjvRG4HfoAgKUsXBaf1K5rT5BZPE0EmlZjnLjqIS2F4aHCWYWIN22FtK%2FCP%2FpI75I9soXmeANDDWo6CpXTbDtctFRj0qH9UyAIOw%2BvrGuc0v%2FbjDiIV%2BUb5C%2FC%2BskjK40CqD6fM3XZ1MhUG7r7owk4vEtlOqeTpWQOc0uO7l3SabDOkio2ogjg4BmoKhKK1a1dqM30yu1&X-Amz-Signature=d2196b2f05e71611a38ecf2fb46ebf3be06ae5ba6ccd213afa7d532a778374dd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
---
**Reading data from a .csv file with other delimiter**
The situation can occur in which we must import data from a .csv file that is not comma-separated but for example semicolon-separated: 
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/996f0cda-465e-450d-aed7-9c59ba403480/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YMY7XNHL%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T222502Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQDT15oBw1BLIuPSinfvciykq2sWdH66ByIIokq892Zz1AIhALZX5BB%2BuLU%2FymNR%2Fy5NAmwzWCjXqow2N16WW1gBr68UKv8DCCcQABoMNjM3NDIzMTgzODA1IgyeY1KMXAig2rpstu8q3AO5VffOl8SbxneQ6dW8FQW3jalnq%2FZcoZqRZ43XKpHerKGSBvbEqRWHjqjXrf3r6cxrliY8eOcOGv3Dlr968H%2FRkXYLz1DfgTJbr5hCDvwiFfBmWETyl5fN%2BwA%2BOWqIBQAGtaqBzomGwnYXjcVkVQ%2B1g8SguwRSjPmGe5vgVco%2BCAityq%2Bkh5ZsbA6LyaZCtgu6x4DNlaZqfoqkAHvwUwm%2FF6P8hHlI94PmZnWgsXAcWr0f2qiT%2Fm4ILVm6AcvqVIRC8acTkA3CGifSpr7EOnDwCxMZxnRUURrFteFSOsyZtE5BzpsXWTjUZr80Q1AATu0lFckCAeUipaNmGWPU4LrvFxZ%2FHOzCYQfWiebZxAmfiGgHZVOgXXVY5wBbeQcnZFm85GqmwzuwyWao%2BJJLSbKt4ddIZE3m37IQbmrVOzkmvYWRJ7YzAV25Hd1yvhct5oEx2MDIfCuKqTG29%2BUVZ8LvoAldbuWhLYil5HCgYaQ8N87h47HdqmQyPSvOD8zZg1wmoBCeYE%2FrhNil4H16WNSFPXK3gX%2FVVV2nd%2F2Nlw4vtCnkp5i6gDRCxrz8U%2FjseDjJmn41WT4P487h1Gh3xgdWQ9UUoFHoQ6wPdyS1gLJzQRc7tM%2F%2F4UwcZmiicDCgzvfJBjqkAWglt2lMZIEh8agX0AxqjvRG4HfoAgKUsXBaf1K5rT5BZPE0EmlZjnLjqIS2F4aHCWYWIN22FtK%2FCP%2FpI75I9soXmeANDDWo6CpXTbDtctFRj0qH9UyAIOw%2BvrGuc0v%2FbjDiIV%2BUb5C%2FC%2BskjK40CqD6fM3XZ1MhUG7r7owk4vEtlOqeTpWQOc0uO7l3SabDOkio2ogjg4BmoKhKK1a1dqM30yu1&X-Amz-Signature=53e993d2e44274b410f3580582414c898ee1573aaf102ebf8932853fb7a8912a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
In this case we can simply change the value of the `delimiter=` parameter to `';'` and Pandas knows how to deal with it:
```python
players_df = pd.read_csv('player_stats.csv', delimiter=';', index_col='Rank')
```
![players_df](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/f9cbeba1-616f-40cf-839e-52bc9ce45d8e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YMY7XNHL%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T222502Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQDT15oBw1BLIuPSinfvciykq2sWdH66ByIIokq892Zz1AIhALZX5BB%2BuLU%2FymNR%2Fy5NAmwzWCjXqow2N16WW1gBr68UKv8DCCcQABoMNjM3NDIzMTgzODA1IgyeY1KMXAig2rpstu8q3AO5VffOl8SbxneQ6dW8FQW3jalnq%2FZcoZqRZ43XKpHerKGSBvbEqRWHjqjXrf3r6cxrliY8eOcOGv3Dlr968H%2FRkXYLz1DfgTJbr5hCDvwiFfBmWETyl5fN%2BwA%2BOWqIBQAGtaqBzomGwnYXjcVkVQ%2B1g8SguwRSjPmGe5vgVco%2BCAityq%2Bkh5ZsbA6LyaZCtgu6x4DNlaZqfoqkAHvwUwm%2FF6P8hHlI94PmZnWgsXAcWr0f2qiT%2Fm4ILVm6AcvqVIRC8acTkA3CGifSpr7EOnDwCxMZxnRUURrFteFSOsyZtE5BzpsXWTjUZr80Q1AATu0lFckCAeUipaNmGWPU4LrvFxZ%2FHOzCYQfWiebZxAmfiGgHZVOgXXVY5wBbeQcnZFm85GqmwzuwyWao%2BJJLSbKt4ddIZE3m37IQbmrVOzkmvYWRJ7YzAV25Hd1yvhct5oEx2MDIfCuKqTG29%2BUVZ8LvoAldbuWhLYil5HCgYaQ8N87h47HdqmQyPSvOD8zZg1wmoBCeYE%2FrhNil4H16WNSFPXK3gX%2FVVV2nd%2F2Nlw4vtCnkp5i6gDRCxrz8U%2FjseDjJmn41WT4P487h1Gh3xgdWQ9UUoFHoQ6wPdyS1gLJzQRc7tM%2F%2F4UwcZmiicDCgzvfJBjqkAWglt2lMZIEh8agX0AxqjvRG4HfoAgKUsXBaf1K5rT5BZPE0EmlZjnLjqIS2F4aHCWYWIN22FtK%2FCP%2FpI75I9soXmeANDDWo6CpXTbDtctFRj0qH9UyAIOw%2BvrGuc0v%2FbjDiIV%2BUb5C%2FC%2BskjK40CqD6fM3XZ1MhUG7r7owk4vEtlOqeTpWQOc0uO7l3SabDOkio2ogjg4BmoKhKK1a1dqM30yu1&X-Amz-Signature=0b716986e690bef505f12590b3dcf7d31fe6b86e2476c33a3683517e605ff7f3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
---
## [`.head()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.head.html)
---
This function is very simple and allows us to display the top 5 rows of a DataFrame only. This can be very useful whenever we have a very large dataset and we want to gain a quick grasp of it.
```python
players_df.head()
```
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/117c3a28-5ad6-435a-8e63-3829f3f95c63/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46626E2BDIR%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T222504Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIBItfjvJSr6pfze38FIveSkYOCbTqPo5imlsIzDoat6bAiEAxAWLNBTgi%2BJ1Q9u3Ig60fW6BKGOkBYjSBr6BGjOlvEIq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDB%2BhzPbxmtXP22KTTircA4PEKhyOKCO%2FWRvFUHal59m28YAEI4yobWsEgwlSMq2YZIDDI52UNP%2BXLjGOr%2Buy42MRvFf0ViilR0l9pfPkZz7vVID6BD%2BJFMFYud9M%2BMgI1eLMzqVNgmCashBAj%2BnzsjPtjlBJ%2FMmPIt6zIH93kKPD%2BxUvc%2BPOhPykMvBSoCMf9v349ht%2FTNDSeVrgOmSuxg2OyXHQHMCf1qJdcCKEbvBtL3E8iVzuxOb5u7S9wzpkm5Y%2Bi7yzy7p9sZDPd6Mv6Fmb%2B%2FK%2B4NshZ8iBF2oRqLsZoSez9tAOEoX7fyvlpHSKCckPPqJhddHbPy6Af5i18SPIJlasDW6ver0HTJ5%2F09JmQeQ5hin%2FD9kuqX2K1CWrvLbqhHlsAKuC47SMSoABcmwo8iL81jKEFG8Xb8lx49lh4mDGn2jjcu%2BLO4rIqjgEIEpiAqyymOeGFvgZs6w2rqWda20OkUHLX8iUhY%2BwxmjwQOFy%2BIwid6YrpRzfi9VMARB0n7oowwwVhCuFoqRqkPoVpO5V22IFy19xLpdYEwdnG87001NflGr%2FMQpVkSYeizLpSZWzDByT4GPx23VBuC2WF97bbGjM4kV1LmzV%2BiO%2FvdA1dwhYk2qTKQj5L%2FDaW5%2FiQ%2FXbzwUIoNq9MOLN98kGOqUB6iI7JLSo4sh3vi7JnQ%2B7ZQJIzjiK%2Fm1FrPIQCnaYDcPZyM%2Fr16ZTfvOHshfgrAV%2FW9nX7IndvpPZukhpYZDE35VymMZdoSLY3nFcATMRRhQ9P91THsvy%2FARdjoQcoqx8mY2XphJUL5qnchjjbJ2iHKyrXqOQmDNqjbpRRTgRbX9AdMfWWMagmV4B%2FWFH7pV9rKyICzTObLuUti6OJb5RzoxDbuSw&X-Amz-Signature=24b6dd460b7c63a00d89831126cda5713df4443f00120962840f189d766dc1b0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
---
## [`.tail()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.tail.html)
---
Very similar to `.head()`, with the only difference that the last 5 rows are displayed only. 
```python
players_df.tail()
```
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/89c926bd-b290-49f7-96aa-2e74779d6f9d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SYVJO7F6%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T222505Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJGMEQCICgeVqiY6vVA5Y%2FuJMximrS7RJqyfCfRkqfDHdTtChHEAiAPptbHQmSa3Ck5H2sR7gLbvb90WueZZILXHZyUtG3L8ir%2FAwgnEAAaDDYzNzQyMzE4MzgwNSIMxim2WkExX9e70c%2FsKtwDLLKqgI69gRarkr6VwSrbZqpqaSeh55rEvd9j1aLhq9OchVUJwKLCkJzhrBwQv%2FHfi12pfS8dP8jEwJC5Kn%2Ble2hAoS9VAhSaKQua3FQ%2FlKP0Bd08JbrV49DJcR6fCTQRaU7jENJkU4YCTzivlQkzdWfkeg5Wwuj6Dha5uff1jeeSR64QXgrtDKYGf3%2FbtyWkW0wCgLYzdMBjCwIEDcBGJjQt6EPLE5V3O65yOQm%2FSns%2BUb2cu%2FYQ7VQKVTZPwDeL60RBLFeumJGFcHkNoOrzXQk4i7AVgAPw55dbh1hP%2FTtlQ%2Fd4CaGGIRSCDurWRvoepFotm32AaeGF1cnXKapyb4VU5lZS6vwwQz5NfiXcxP9njDCqdJ7EaiepLY3GGqTuFD41nSNqgiEDQKAbqr7XaRcgg9FaGjLmyXIIgDVefb7NcCH8yLCauVv5j9Hchmns%2B25XR%2FMgOs3NhNMs22lTHBOYFyA9OsyvkYF3DdnevFuyshTAHbEZIMbp4jEsgfkURECN5rdlu7P2%2FgaoFvOx4UPLc5z7K0Oe7LclYQG8%2BfAw7E4ajsV7eQIE7vguxRAyQ61mO7x8iov06mqKrLGC0SKht1QyfNHPY4tPcIv5FY5d0XqiU3HIvm%2F6JrMw8s73yQY6pgFt2NVMWGwWWy85Nyaq7%2B6OQLctm7WnSykgeNH9kRJB2bioFYV1436h5H5FBTVR1ow2gR5VQNePWzXlhjz33PpGl0yxTEtVsC3naWzew6LSo7dzfPSLPqlhIm0KC6quLEC1%2BetLYEjKInACtfizt7dpb9FL8ZO2zbjNFAgXO%2FLPwD5AVoiCuQn1U8KAwxV0t8Ka0%2Bz72sqRKZA3j%2Ft9if%2BEp8PKTo0M&X-Amz-Signature=84603e14617a18e6a40aa2a44c6e61cbb017896a34bd2d705af255660ca8b33d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
---
## [`.columns`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.columns.html)
---
**Syntax**
With this function we can extract the column labels of a DataFrame.
The syntax is the following:
`df.columns`
---
**Extract column labels from DataFrame**
Let’s assume we want to extract the column names from the following DataFrame.
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/3489a926-bdc6-41b8-86c1-de62699b188c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XLDPPUIZ%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T222505Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJGMEQCIHNai4fse0WcIz%2Fe2iyqhWaNzP9ewAddUDGu47Qb7HL0AiAauUvt6rGXIafLs3UjnzMsaw3X97Rts3TBD9VH8p92yir%2FAwgnEAAaDDYzNzQyMzE4MzgwNSIMDtoLSHRqLwtpzR3iKtwDT6b9PgQ6wiLM%2B8zn3DK0I8iROEAb7lxgVbuD%2FyffGu%2BAXpa%2FUpi0cooQngZj5yhFy2QikJLnuZ%2FOgjP6i6dYskmkFY6z1M9ZzCx%2BvA1bjD9jD%2BiiOO3JUba7RBGsVUbkcYNY7eqhZaoleOY1s5VDHjBLsQaFhnvfs83TEEyIgvQ01iihyheBLWQwXNv%2BICl9qZvrYKZFZgDx61CiqlVIUzji%2BK%2BVUfmzuux%2Bp7fTCiGvCi6gsgCKOqwaWKMUjGBHX8e2bzvzD6CPA6l%2F40bLqNfuFm3phIfbrHx4DtWocJCwJg%2FUJ4ZhsniaB3Yd3eGrlVfV%2FX4HURvNmFOOGT08cNXJI0Ry7uMdNYlKmwbtZyBEOZSwVy6RV9KtWUq9Nq9Q38Vkb91SG5Tw7ga1QwMWBa6FpD4%2F2ZmuJgPr50y1LO15DDw6i4nHVozQwUm3uRcHNvDfrGiGXuTgKrK9QCoAlgSgSqdEkGhrEuaVitlB%2B4f4TkxMnZyRpX63jqm2uz2Zw%2F8Vq%2F7A7XqrhGf28qeKSF0FR243U3syES3qiXuJyf%2B4ZaOrhrWHF%2B%2FRU4UVVPclsD%2FFxQTWARHPGuP0Nd6vrtWk4tg9GmMderAV5dhRIrpn8VKolcGAheibcjMw3833yQY6pgGBDkgMvz6zQ7RpILzt4GW8O3eA%2BBaMmBSJhBU5iQA1tKWVpYpoVN2OzgsDaVltbaFsi3WXfJFRQZKWDhhLvEbjXvkkCdxutDN%2F%2FqzyHEe%2FUDcYVJFIgyQNHg8Fa%2F6jcOgOTSwTMHEHWSr4IkuNVL%2BRyS30becwssrMuimtu3KN8ODI2JpEO%2Bs63jiy5GB7l55fsl538QIjFRtZySU449pyKfgpqM8B&X-Amz-Signature=8fadca5e1055987694dcb0779f894687a94e1b6fa34fa45ad1b8546a4e9f2013&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

```python
players_df.columns

Index([
		'Rank', 'Player', 'Team', 'Games played', 'Games started',
		'Minutes played', 'Goals', 'Assists', 'Shots', 'Shots on goal',
	],
  dtype='object'
)
```
As we can see the column labels are returned as [Index object](https://www.google.com/search?client=safari&rls=en&q=pandas%20index%20object&ie=UTF-8&oe=UTF-8). 
If we want to convert it to a list, we can do [type conversion](/5b0832dbf9454eb1941b7632e68a9abb#fe6cebbcc6914acba4d5674dcd118ddb) with the `list()` method.
```python
list(players_df.columns)

[
	'Rank','Player','Team','Games played','Games started',
	'Minutes played','Goals','Assists','Shots',
	'Shots on goal'
]
```
---
## [`.loc[]`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.loc.html) [`.iloc[]`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.iloc.html)
---
With `.loc[]` and `.iloc[]` we can access specific rows, columns and cells in a DataFrame.
### `.loc[]` → selection over index labels and column names
---
**Syntax**
The syntax of `.loc[]` is:
`df.loc[<< rows to select >> , << columns to select >>]`
If we only provide one parameter, then this parameter is treated as the rows to select.
---
**Access single row**
The command below goes through the index column in the DataFrame and checks where the String `'Dominic Calvert-Lewin'` is present and returns all column values for this player.
```python
players_df.loc['Dominic Calvert-Lewin']

######### OUTPUT #########
Team              Everton
Games played           36
Games started          30
Minutes played       2629
Goals                  13
Assists                 1
Shots                  70
Shots on goal          38
total_points           14
Name: Dominic Calvert-Lewin, dtype: object
```
---
**Access specific cell**
If we want to select only a specific column for this player, we can pass the column name to the selection. Now we receive the value for a single cell, i.e., the number of goals scored by this player.
```python
players_df.loc['Dominic Calvert-Lewin' , 'Goals']

######### OUTPUT #########
13
```
---
**Access multiple rows and columns**
We can also select multiple rows and columns by passing lists that contain all index labels and column labels that we wish to select.
```python
players_df.loc[['Dominic Calvert-Lewin', 'Harry Kane'] , ['Goals', 'Games played']]
```
As an output we receive a mini DataFrame that contains only these two players and the columns we have specified.
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/c7ccb92c-7800-435e-8704-64d239ffe161/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W5IGHHFH%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T222506Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJFMEMCHwXtfSmdLZuTNTb5i5u5uZGLdHJXtlC5oYVknzGfp8UCIH%2BYVIArshukzBkVstDwm12uu706QM9cVAFN37Z6hgHEKv8DCCcQABoMNjM3NDIzMTgzODA1Igxq7m%2FsLAWqBaiRv%2FIq3ANRt8XkF%2BaQjUOXsF7sAMjtBz3az%2BEGMEIzj9Av0KJxWXfu7Gnzxh1MCZXdizkxnsos%2FRgyb4tRb45cKYr9U89HLQ94FQv2CzG4%2BF7OMtAcNChzppxYS7hOXo%2FpzYz0CHuCN9OaLTYuclARTwYcmmBj8%2BqvAA0B2O9oKyLKafa3EoXU2EUUnPMfTa%2FVxD2Mb1UsA8rqgXKap8Xcy48iALBD7FdFBKZuk7WCPRcfuIsI22SkX3hk6ejDnPGobXMo0VB65X1xeRBtbQjj2AzIr9AZTRD47fRHirKL5mQ%2BBBx%2BGI%2FJs2CMbvx%2FfPfncYfncPLmUIMCqfspZGGIo00sy0vb%2BWsYnXQ0vknkfPEzX3NGscL7Pok0D1Bctb4dG3QaznXxib1%2Futx%2BpFv6a9oSFq7QCNaU3f%2FgZ7p9C6DnfpxVtKWlZ91o8sddkhSgbbZKeUjpzIitMJvBjonydl5bilfpND2v1bvt28JfGJTCf3%2FgGpnXoq4bDyOcm5h7IJ%2FcaYp67Ksig65Z0dF7DPQDFYL8IcUQ8VsPvrbhCAbeSKGHVbxS%2BpiM9psrdU0jEiu3y4HBF9zGeusYLrOfDFIYEKPZHoPlRuRWvJDAn6ulfSbj4nHQ7BKPOHwA%2FZvE%2BjDgzffJBjqnAcSWMVm5YZktJUFr96Pfvv0ICpK3WNa2yZV8bELpGzE8FQzCbu8bklhs6xiL1%2BxJGVDY%2BqFk6m1zKUIbtcVpZolEj7Z4PUXt3d2qByMICHorlPjtc1oXyzEsZILX5j6%2ByMk9C%2BI0UNrswSiImouEVCfSArBILzT5olddwPk6Uqq%2BPqg%2Fp%2F0JpAOWTLPBwnB9lD2r%2FxzFlVxeW8mXg3NdZLHQjbXonG6P&X-Amz-Signature=f44575f3fe07e01d6a18c87989ecc5aed66c4413f2ee3732e89a20774c8dd6b8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
---
**Access rows based on condition**
Another cool thing with `.loc[]` is that we can select rows based on a condition that returns True or False. For example, if we search for all players that scored exactly 10 goals, we can achieve this by the following command(s).
```python
players_df.loc[players_df['Goals'] == 10]
# OR
players_df[players_df['Goals'] == 10]
```
Python goes through the column `Goals` and checks for each value if it is equal to 10. If yes, it returns `True` if no, it returns `False`. In the end only the rows are displayed for which `True` has been returned.
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/ba1a88fc-24e1-4a54-896f-e55317031d16/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W5IGHHFH%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T222506Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJFMEMCHwXtfSmdLZuTNTb5i5u5uZGLdHJXtlC5oYVknzGfp8UCIH%2BYVIArshukzBkVstDwm12uu706QM9cVAFN37Z6hgHEKv8DCCcQABoMNjM3NDIzMTgzODA1Igxq7m%2FsLAWqBaiRv%2FIq3ANRt8XkF%2BaQjUOXsF7sAMjtBz3az%2BEGMEIzj9Av0KJxWXfu7Gnzxh1MCZXdizkxnsos%2FRgyb4tRb45cKYr9U89HLQ94FQv2CzG4%2BF7OMtAcNChzppxYS7hOXo%2FpzYz0CHuCN9OaLTYuclARTwYcmmBj8%2BqvAA0B2O9oKyLKafa3EoXU2EUUnPMfTa%2FVxD2Mb1UsA8rqgXKap8Xcy48iALBD7FdFBKZuk7WCPRcfuIsI22SkX3hk6ejDnPGobXMo0VB65X1xeRBtbQjj2AzIr9AZTRD47fRHirKL5mQ%2BBBx%2BGI%2FJs2CMbvx%2FfPfncYfncPLmUIMCqfspZGGIo00sy0vb%2BWsYnXQ0vknkfPEzX3NGscL7Pok0D1Bctb4dG3QaznXxib1%2Futx%2BpFv6a9oSFq7QCNaU3f%2FgZ7p9C6DnfpxVtKWlZ91o8sddkhSgbbZKeUjpzIitMJvBjonydl5bilfpND2v1bvt28JfGJTCf3%2FgGpnXoq4bDyOcm5h7IJ%2FcaYp67Ksig65Z0dF7DPQDFYL8IcUQ8VsPvrbhCAbeSKGHVbxS%2BpiM9psrdU0jEiu3y4HBF9zGeusYLrOfDFIYEKPZHoPlRuRWvJDAn6ulfSbj4nHQ7BKPOHwA%2FZvE%2BjDgzffJBjqnAcSWMVm5YZktJUFr96Pfvv0ICpK3WNa2yZV8bELpGzE8FQzCbu8bklhs6xiL1%2BxJGVDY%2BqFk6m1zKUIbtcVpZolEj7Z4PUXt3d2qByMICHorlPjtc1oXyzEsZILX5j6%2ByMk9C%2BI0UNrswSiImouEVCfSArBILzT5olddwPk6Uqq%2BPqg%2Fp%2F0JpAOWTLPBwnB9lD2r%2FxzFlVxeW8mXg3NdZLHQjbXonG6P&X-Amz-Signature=3def62fb3e639801cce1a88e10e5ab10514d4912b0e1242e6cdf96cc28dbdbcf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
We can also use more complicated conditions:
```python
players_df.loc[(players_df['Goals'] >= 10) & (players_df['Assists'] > 7)]
# OR
players_df[(players_df['Goals'] >= 10) & (players_df['Assists'] > 7)]
```
In this example we use two conditions and connect them with `AND (&)`, thus both conditions must evaluate to True for a player so that he is going to be displayed in the result set.
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/e36990b5-25ca-4f2b-b252-e4f64e702ab0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W5IGHHFH%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T222507Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJFMEMCHwXtfSmdLZuTNTb5i5u5uZGLdHJXtlC5oYVknzGfp8UCIH%2BYVIArshukzBkVstDwm12uu706QM9cVAFN37Z6hgHEKv8DCCcQABoMNjM3NDIzMTgzODA1Igxq7m%2FsLAWqBaiRv%2FIq3ANRt8XkF%2BaQjUOXsF7sAMjtBz3az%2BEGMEIzj9Av0KJxWXfu7Gnzxh1MCZXdizkxnsos%2FRgyb4tRb45cKYr9U89HLQ94FQv2CzG4%2BF7OMtAcNChzppxYS7hOXo%2FpzYz0CHuCN9OaLTYuclARTwYcmmBj8%2BqvAA0B2O9oKyLKafa3EoXU2EUUnPMfTa%2FVxD2Mb1UsA8rqgXKap8Xcy48iALBD7FdFBKZuk7WCPRcfuIsI22SkX3hk6ejDnPGobXMo0VB65X1xeRBtbQjj2AzIr9AZTRD47fRHirKL5mQ%2BBBx%2BGI%2FJs2CMbvx%2FfPfncYfncPLmUIMCqfspZGGIo00sy0vb%2BWsYnXQ0vknkfPEzX3NGscL7Pok0D1Bctb4dG3QaznXxib1%2Futx%2BpFv6a9oSFq7QCNaU3f%2FgZ7p9C6DnfpxVtKWlZ91o8sddkhSgbbZKeUjpzIitMJvBjonydl5bilfpND2v1bvt28JfGJTCf3%2FgGpnXoq4bDyOcm5h7IJ%2FcaYp67Ksig65Z0dF7DPQDFYL8IcUQ8VsPvrbhCAbeSKGHVbxS%2BpiM9psrdU0jEiu3y4HBF9zGeusYLrOfDFIYEKPZHoPlRuRWvJDAn6ulfSbj4nHQ7BKPOHwA%2FZvE%2BjDgzffJBjqnAcSWMVm5YZktJUFr96Pfvv0ICpK3WNa2yZV8bELpGzE8FQzCbu8bklhs6xiL1%2BxJGVDY%2BqFk6m1zKUIbtcVpZolEj7Z4PUXt3d2qByMICHorlPjtc1oXyzEsZILX5j6%2ByMk9C%2BI0UNrswSiImouEVCfSArBILzT5olddwPk6Uqq%2BPqg%2Fp%2F0JpAOWTLPBwnB9lD2r%2FxzFlVxeW8mXg3NdZLHQjbXonG6P&X-Amz-Signature=f0df793c1a67ab99e9778668c64df1307ddc42ca0796abec4f57953700206b9f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
Remember, even if the example above looks quite complicated, we have only passed a selection criteria for rows into `.loc[]`, as there is no comma `,` .
Thus, when we only want to have specific columns displayed in our result set, we can insert the comma `,` and pass a list to `.loc[]` with the column labels that should be displayed.
```python
players_df.loc[(players_df['Goals'] >= 10) & (players_df['Assists'] > 7), ['Goals', 'Assists']]
```
Now, this leads to only the columns `Goals` and `Assists` being displayed in the result set.
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/f6ca01be-39fd-475b-b4e4-94e0c80b5ec2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W5IGHHFH%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T222507Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJFMEMCHwXtfSmdLZuTNTb5i5u5uZGLdHJXtlC5oYVknzGfp8UCIH%2BYVIArshukzBkVstDwm12uu706QM9cVAFN37Z6hgHEKv8DCCcQABoMNjM3NDIzMTgzODA1Igxq7m%2FsLAWqBaiRv%2FIq3ANRt8XkF%2BaQjUOXsF7sAMjtBz3az%2BEGMEIzj9Av0KJxWXfu7Gnzxh1MCZXdizkxnsos%2FRgyb4tRb45cKYr9U89HLQ94FQv2CzG4%2BF7OMtAcNChzppxYS7hOXo%2FpzYz0CHuCN9OaLTYuclARTwYcmmBj8%2BqvAA0B2O9oKyLKafa3EoXU2EUUnPMfTa%2FVxD2Mb1UsA8rqgXKap8Xcy48iALBD7FdFBKZuk7WCPRcfuIsI22SkX3hk6ejDnPGobXMo0VB65X1xeRBtbQjj2AzIr9AZTRD47fRHirKL5mQ%2BBBx%2BGI%2FJs2CMbvx%2FfPfncYfncPLmUIMCqfspZGGIo00sy0vb%2BWsYnXQ0vknkfPEzX3NGscL7Pok0D1Bctb4dG3QaznXxib1%2Futx%2BpFv6a9oSFq7QCNaU3f%2FgZ7p9C6DnfpxVtKWlZ91o8sddkhSgbbZKeUjpzIitMJvBjonydl5bilfpND2v1bvt28JfGJTCf3%2FgGpnXoq4bDyOcm5h7IJ%2FcaYp67Ksig65Z0dF7DPQDFYL8IcUQ8VsPvrbhCAbeSKGHVbxS%2BpiM9psrdU0jEiu3y4HBF9zGeusYLrOfDFIYEKPZHoPlRuRWvJDAn6ulfSbj4nHQ7BKPOHwA%2FZvE%2BjDgzffJBjqnAcSWMVm5YZktJUFr96Pfvv0ICpK3WNa2yZV8bELpGzE8FQzCbu8bklhs6xiL1%2BxJGVDY%2BqFk6m1zKUIbtcVpZolEj7Z4PUXt3d2qByMICHorlPjtc1oXyzEsZILX5j6%2ByMk9C%2BI0UNrswSiImouEVCfSArBILzT5olddwPk6Uqq%2BPqg%2Fp%2F0JpAOWTLPBwnB9lD2r%2FxzFlVxeW8mXg3NdZLHQjbXonG6P&X-Amz-Signature=75e88959f3e763c43dec6077099ee856cf6ab0eb41a88f7dac3198a44e363a33&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
---
### `.iloc[]` → selection over index position and column position
---
**Syntax**
The  syntax of `.iloc[]` is:
`df.iloc[<< row indexes to select >> , << column indexes to select >>]`
If we only provide one parameter, then this parameter is again treated as the row indexes to select.
---
**Access single row**
The command below selects the third row in the DataFrame, which is at index position 2. 
> 💡 **When accessing an element over its index position, we always start counting at 0. So the first row/column in a DataFrame has index position 0.**
```python
players_df.iloc[2]

######### OUTPUT #########
Team              Arsenal
Games played           36
Games started          35
Minutes played       3138
Goals                  22
Assists                 3
Shots                  70
Shots on goal          42
total_points           25
Name: Pierre-Emerick Aubameyang, dtype: object
```
---
**Slicing on rows**
The power of `.iloc[]` is that we can apply it for slicing operations. Let’s say we want to select only the first 10 players, then we can do so by using `.iloc[:10]`.
```python
players_df.iloc[:10]
```
Here we have the same principle as when we do slicing with lists:
`[ << first index to be included >> : << first index to be excluded >> ]`
Thus, this command returns the players with index position 0 to 9, i.e., the first 10 players:
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/650b856f-f0af-4950-a1e4-ee0fca8ba573/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663ZVOMQA6%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T222507Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQCPQsIVwXTv9OUhSZOAqR2N1tx8gDu1qIufPei87v7mJwIhAPc9JsE72JQk%2BxU8Dvs8G7jP4uprCFF4wTRLlE2CPRPeKv8DCCcQABoMNjM3NDIzMTgzODA1IgySDFp8GtPpFC5yf40q3AO%2BKsyiTYN8FkL7ZQhM2fNGwcMuuVu8NizixIK4Ep1qWZpseZaK3EhwNxfj3JHPMKAHIO1TjeGWuPPHjBeEH9CwBiwlPJKK0XrlY%2BRRNLTdhKBzyHSJRKOSGWCcH80q23yviNA5f5m%2FkA%2BQFYQuJeI%2FHRXF9tQ5kkJlAgdmzx4utYWKZ7OdfqFJpBHbAylMxv57g5GpjtOl2WI08B1jni3Su3db%2BrcARCF14dY9cl8x73QHttK5Q8oRLO4HjrWi7LgAkXNgmrAlNibpATIeLkHcqFlr3UadPxcUcckenwVYuC4EQ3TBOOREOhdo%2BM8Otdve02pFeHkSphitRDE3eUGW3gsQNjtRcIwKSBJ%2FxSDh1W2gppeU4OXcIfoyCHsJHj0EAPefttrd3dVsOUT%2BllVPz7b8EydYMtqGnEgsnhy6rEqg3CRbv1Jx%2Bm67HlUpiBl2BlQ%2FtlQ0Jc8sFnuMSdWgN4Z5lVQV9uOpqK7agVCanzGZYCRUT93jdzh4LbiuPL9MORRd%2F9A3FUybJ3eeDrOxu7dIjpA47QV6VV61AuVccuCAQAJxcJEr602rr7SbG58eS%2B6VYeNVZ1daIxaaJdGTd83jwUgwN68QWqPf2omLHGDDGlIwEqJh8g9L6zCOzvfJBjqkAammyI7Ke5Ea32nCT%2BTf3aWEzsrfmkM4FeT4%2BnVMb%2BYi3C3d1xcvanpV7FRO67jne3loV6ADn6kaE31qBGThF5gc9UcfePDONO%2Fnta69sqZG9a2cTXKVXdLn6TKuYAKsN2BYIBIYrBNjlzb7N0JHoCb3xH2VMsNjtQWA0h5zDPgCZltcBDGe2ddbw5sEfHVoGd%2BE8LrwkqQP8CNwXubZCXjhlcjp&X-Amz-Signature=497b6ce6d44018a46c7d3d0cbb29ecc765d80907a6406f9c266c4e9ad0a6d35f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
---
**Slicing on rows and columns**
If we want to select not all columns but only the first three, we can insert the comma `,`.  For the columns the slicing command would be `[:3]` as this selects the columns with index `0` `1` `2` and thus the first three.
```python
players_df.iloc[:10, :3]
```
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/683390cb-2a6f-4cab-b0ba-2b9b3afc433f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663ZVOMQA6%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T222507Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQCPQsIVwXTv9OUhSZOAqR2N1tx8gDu1qIufPei87v7mJwIhAPc9JsE72JQk%2BxU8Dvs8G7jP4uprCFF4wTRLlE2CPRPeKv8DCCcQABoMNjM3NDIzMTgzODA1IgySDFp8GtPpFC5yf40q3AO%2BKsyiTYN8FkL7ZQhM2fNGwcMuuVu8NizixIK4Ep1qWZpseZaK3EhwNxfj3JHPMKAHIO1TjeGWuPPHjBeEH9CwBiwlPJKK0XrlY%2BRRNLTdhKBzyHSJRKOSGWCcH80q23yviNA5f5m%2FkA%2BQFYQuJeI%2FHRXF9tQ5kkJlAgdmzx4utYWKZ7OdfqFJpBHbAylMxv57g5GpjtOl2WI08B1jni3Su3db%2BrcARCF14dY9cl8x73QHttK5Q8oRLO4HjrWi7LgAkXNgmrAlNibpATIeLkHcqFlr3UadPxcUcckenwVYuC4EQ3TBOOREOhdo%2BM8Otdve02pFeHkSphitRDE3eUGW3gsQNjtRcIwKSBJ%2FxSDh1W2gppeU4OXcIfoyCHsJHj0EAPefttrd3dVsOUT%2BllVPz7b8EydYMtqGnEgsnhy6rEqg3CRbv1Jx%2Bm67HlUpiBl2BlQ%2FtlQ0Jc8sFnuMSdWgN4Z5lVQV9uOpqK7agVCanzGZYCRUT93jdzh4LbiuPL9MORRd%2F9A3FUybJ3eeDrOxu7dIjpA47QV6VV61AuVccuCAQAJxcJEr602rr7SbG58eS%2B6VYeNVZ1daIxaaJdGTd83jwUgwN68QWqPf2omLHGDDGlIwEqJh8g9L6zCOzvfJBjqkAammyI7Ke5Ea32nCT%2BTf3aWEzsrfmkM4FeT4%2BnVMb%2BYi3C3d1xcvanpV7FRO67jne3loV6ADn6kaE31qBGThF5gc9UcfePDONO%2Fnta69sqZG9a2cTXKVXdLn6TKuYAKsN2BYIBIYrBNjlzb7N0JHoCb3xH2VMsNjtQWA0h5zDPgCZltcBDGe2ddbw5sEfHVoGd%2BE8LrwkqQP8CNwXubZCXjhlcjp&X-Amz-Signature=8d54b96144072c17cebe1685818e14af381b86895b20be492e2ce3f4837e6823&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
We can also perform more complicated slicing operations with `.iloc[]`. let’s say we want to select the 94th until the 98th row and the 2nd  until the 4th column.
```python
players_df.iloc[93:98, 2:5]
```
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/37bffb74-4ae3-4b36-bec6-22ef1a31233c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663ZVOMQA6%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T222507Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQCPQsIVwXTv9OUhSZOAqR2N1tx8gDu1qIufPei87v7mJwIhAPc9JsE72JQk%2BxU8Dvs8G7jP4uprCFF4wTRLlE2CPRPeKv8DCCcQABoMNjM3NDIzMTgzODA1IgySDFp8GtPpFC5yf40q3AO%2BKsyiTYN8FkL7ZQhM2fNGwcMuuVu8NizixIK4Ep1qWZpseZaK3EhwNxfj3JHPMKAHIO1TjeGWuPPHjBeEH9CwBiwlPJKK0XrlY%2BRRNLTdhKBzyHSJRKOSGWCcH80q23yviNA5f5m%2FkA%2BQFYQuJeI%2FHRXF9tQ5kkJlAgdmzx4utYWKZ7OdfqFJpBHbAylMxv57g5GpjtOl2WI08B1jni3Su3db%2BrcARCF14dY9cl8x73QHttK5Q8oRLO4HjrWi7LgAkXNgmrAlNibpATIeLkHcqFlr3UadPxcUcckenwVYuC4EQ3TBOOREOhdo%2BM8Otdve02pFeHkSphitRDE3eUGW3gsQNjtRcIwKSBJ%2FxSDh1W2gppeU4OXcIfoyCHsJHj0EAPefttrd3dVsOUT%2BllVPz7b8EydYMtqGnEgsnhy6rEqg3CRbv1Jx%2Bm67HlUpiBl2BlQ%2FtlQ0Jc8sFnuMSdWgN4Z5lVQV9uOpqK7agVCanzGZYCRUT93jdzh4LbiuPL9MORRd%2F9A3FUybJ3eeDrOxu7dIjpA47QV6VV61AuVccuCAQAJxcJEr602rr7SbG58eS%2B6VYeNVZ1daIxaaJdGTd83jwUgwN68QWqPf2omLHGDDGlIwEqJh8g9L6zCOzvfJBjqkAammyI7Ke5Ea32nCT%2BTf3aWEzsrfmkM4FeT4%2BnVMb%2BYi3C3d1xcvanpV7FRO67jne3loV6ADn6kaE31qBGThF5gc9UcfePDONO%2Fnta69sqZG9a2cTXKVXdLn6TKuYAKsN2BYIBIYrBNjlzb7N0JHoCb3xH2VMsNjtQWA0h5zDPgCZltcBDGe2ddbw5sEfHVoGd%2BE8LrwkqQP8CNwXubZCXjhlcjp&X-Amz-Signature=6a4a867c457d92612004a4e8dcbfb02c0d1e370b596b1325a967a47a0970b24c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
---
---
## [`.at[]`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.at.html) [`.iat[]`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.iat.html)
---
Similar to `.loc[]` and `.iloc[]` we can access values in cells in a DataFrame using `.at[]` and `.iat[]`. Specially when we want to select only a single cell, these commands are much easier.
### `.at[]` → access single cell over index label and column name
---
**Syntax**
The syntax is as follow:
`df.at[ << index label >>, << column label >> ]`
As you can see the syntax is very similar to `.loc[]`. It’s just that we use `.at[]` mainly for accessing a single cell over labels. So with `.at[]` we are a bit less flexible, however, it is simpler to use.
---
**Access specific cell**
Let’s assume we want to access the team of Jamie Vardy. We can do so with the command below:
```python
players_df.at['Jamie Vardy', 'Team']
'Leicester City' # -> team of Jamie Vardy
```
---
### `.iat[]` → access single cell over index position and column position
---
**Syntax**
The syntax is as follow:
`df.iat[ << index position >>, << column position >> ]`
As you can see the syntax is very similar to `.iloc[]`. It’s just that we use `.iat[]` mainly for accessing a single cell over index positions. So with `.iat[]` we are a bit less flexible, however, it is simpler to use.
---
**Access specific cell**
Let’s assume we want to access team of the fifth player. We can do so with the command below:
```python
players_df.iat[4, 1]
'Liverpool' # -> team of Mohammed Salah (fifth player)
```
---
---
## [`.set_index()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.set_index.html)
---
**Syntax**
With this function we can change the index column of a DataFrame to any other column. The syntax is the following:
`df.set_index( << column name >>, inplace = True )`
---
**Change index column**
Let’s assume we have currently the column Rank set as the index.
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/3489a926-bdc6-41b8-86c1-de62699b188c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665S5JNWQY%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T222512Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJGMEQCIH3sOx8bWmbpHmHrZ%2FEePzo1eusQP69FItUzExWDEyU9AiBlcT4QMVKHFfeG22PrkjB54UpNGYufG81L9ex%2FoXlIpir%2FAwgnEAAaDDYzNzQyMzE4MzgwNSIMPuh8Nb1C%2FNr1etUxKtwD2p4LaOYr%2FZfsefAsBjCcTxlEBBXsg6K7%2FXaeEz9lEDnOf2gub7JVZkWnhj0Vg4FBt8jzgjx7tQekqjAgZnCxxr2kbq04jc%2BvApxs57rpb67Vli89%2B1fpnWTg8Ks0G95ISoIDVBbC65VmiLZhvCHxPhXz3kjQJBfKMW7%2Bk%2Fm4RH3uVkYtT4sP74MdTXFBv6mjT7vsSvRuMEFOTl67CXsFGe7QM6YZYoIX2bb8%2BXlWpC89yCKqwuRC0HjcRDXdQWTiLGjy4fgYLFflTqOYL3gWNs4lUUYXxEImAP4w3MWrh3lidoJEHnCLCZIyORcASX6IKsayWn0fRQxQPwTqzGW9kTQl%2ByL2BKT6EVTE%2F8UeRccUTSTxyldm3o2LPlTMQPmnwdYHKLhnPd%2BDBvXzutbMMzZ%2BwtoRJn73BjZOZ8wtz0KF5VjHmYsxxiRrl3A7Eni4DMdBu7PjP%2BFKl4PleqJqWke9SxT8Dnewm%2FHQY5y163VVoWcApqBg472NK7elewYteDGSlMEMRZA54XSklfn4KplUcfd1ENC6KoIDSoUZZ4l5rCG5l7a9LEPqr6lKMxesiwEfm2jbMoV6%2FmmIyCBHOzhVdjZJrWslW0WII7PxahKe%2Fo0h0%2BkGOMmfFfIw3833yQY6pgGPK9fzgpHq5MgXYICLZSktz01EvEEoqqh9FWrvLY854d3eu4XmMxLSImIGnhAgWeOj%2FJeBWhWDsRYEbphdvJ7RrMqV12FiYahKBGtdRZtWzfm4xDAzG7klxsym1h8%2FN%2F7AOeyn%2F%2F342hxLsG971pG9g4ZJTo5thzqGPrUv4UMWSPwpLR%2BOBVaNJJPLQ0CGKR2WOPGWzsOV%2BJGtD5iC%2Fek3N7IYw0pK&X-Amz-Signature=41fc7d1afe18056daf87a2361c8602b9393649b648ef5ca4cdda8c679c17be2f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
Because of that, we are not able to select a player (e.g. Danny Ings) by its name using `.loc[]`, as the player name is not present in the index column and we get a **KeyError**.
```python
players_df.loc['Danny Ings']

KeyError: 'Danny Ings' # -> the name 'Dany Ings' is not present in the index column
```
We can now change the index to the Player column. It is important that we set the parameter `inplace` to `True` as otherwise the DataFrame will not be updated.
```python
players_df.set_index('Player', inplace=True)

Team              Southampton
Games played               38
Games started              32
Minutes played           2812
Goals                      22
Assists                     2
Shots                      66
Shots on goal              38
Name: Danny Ings, dtype: object
```
We can see now in the updated DataFrame below that the Player column is now **bold** and thus is the new index column.
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/a9a40cea-8aa5-4715-9bc3-1621e47671dd/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665S5JNWQY%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T222512Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJGMEQCIH3sOx8bWmbpHmHrZ%2FEePzo1eusQP69FItUzExWDEyU9AiBlcT4QMVKHFfeG22PrkjB54UpNGYufG81L9ex%2FoXlIpir%2FAwgnEAAaDDYzNzQyMzE4MzgwNSIMPuh8Nb1C%2FNr1etUxKtwD2p4LaOYr%2FZfsefAsBjCcTxlEBBXsg6K7%2FXaeEz9lEDnOf2gub7JVZkWnhj0Vg4FBt8jzgjx7tQekqjAgZnCxxr2kbq04jc%2BvApxs57rpb67Vli89%2B1fpnWTg8Ks0G95ISoIDVBbC65VmiLZhvCHxPhXz3kjQJBfKMW7%2Bk%2Fm4RH3uVkYtT4sP74MdTXFBv6mjT7vsSvRuMEFOTl67CXsFGe7QM6YZYoIX2bb8%2BXlWpC89yCKqwuRC0HjcRDXdQWTiLGjy4fgYLFflTqOYL3gWNs4lUUYXxEImAP4w3MWrh3lidoJEHnCLCZIyORcASX6IKsayWn0fRQxQPwTqzGW9kTQl%2ByL2BKT6EVTE%2F8UeRccUTSTxyldm3o2LPlTMQPmnwdYHKLhnPd%2BDBvXzutbMMzZ%2BwtoRJn73BjZOZ8wtz0KF5VjHmYsxxiRrl3A7Eni4DMdBu7PjP%2BFKl4PleqJqWke9SxT8Dnewm%2FHQY5y163VVoWcApqBg472NK7elewYteDGSlMEMRZA54XSklfn4KplUcfd1ENC6KoIDSoUZZ4l5rCG5l7a9LEPqr6lKMxesiwEfm2jbMoV6%2FmmIyCBHOzhVdjZJrWslW0WII7PxahKe%2Fo0h0%2BkGOMmfFfIw3833yQY6pgGPK9fzgpHq5MgXYICLZSktz01EvEEoqqh9FWrvLY854d3eu4XmMxLSImIGnhAgWeOj%2FJeBWhWDsRYEbphdvJ7RrMqV12FiYahKBGtdRZtWzfm4xDAzG7klxsym1h8%2FN%2F7AOeyn%2F%2F342hxLsG971pG9g4ZJTo5thzqGPrUv4UMWSPwpLR%2BOBVaNJJPLQ0CGKR2WOPGWzsOV%2BJGtD5iC%2Fek3N7IYw0pK&X-Amz-Signature=ae57b1d5b3e34afbe03a7fd48bd5f90b1b882e7fb9d72bf6f06ac70abaaeac06&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
We can now select the player Danny Ings using `.loc[]` .
```python
players_df.loc['Danny Ings']

######### OUTPUT #########
Team              Southampton
Games played               38
Games started              32
Minutes played           2812
Goals                      22
Assists                     2
Shots                      66
Shots on goal              38
Name: Danny Ings, dtype: object
```
---
## [`.reset_index()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.reset_index.html)
---
**Syntax**
With this function we can reset the index column of a DataFrame so that the index is numeric again and the first row is at index 0.
`df.reset_index(inplace = True)`
---
**Reset index column**
Let’s assume in our DataFrame we have currently the column `Player` set as our index. 
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/88ad3bb4-c8e5-4d76-a3d9-ecf4028c834b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UCQLK72F%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T222516Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIAQ6ZxSgbB%2FjSr0HoqDGecf5chvkt%2FysdXX3%2BxaMKSgUAiEAn3eBcYqi5AgFU1LyxxPCLpdUkBu5rNXBZmDK12EGT60q%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDJfdXkd8e7pdY90h7CrcA6JtN81p5LmtPJtw7o73I3x3%2F3ntT8IzSvTQstkl1%2BsPBm6exaUU9AhfrDNmcTooGA3DqtOqBjGRvYEe4HrgyZfpwzmGme1t5aQ%2B%2B%2F4ZN6RvkWuJUzAUzrOry0IBKBUJFXHMkkEaKYd9%2B5CJjN2uazIOkoKCiDc9NoX2DGj7WbhQyvA7BQ6Jq1g%2BRSmUijMJtkfM0ebME4szeYDOaw0DF1KFvhu3%2BF%2BC05l0vuBCJ4U6rPv6K2KfWdG2c3OpGYb%2B4mhINSGQFXnpaeHPfaQs8ec7JdDtdJ5t9RZQQAVaz%2Bah8a0JcSXQnaYTVQp3mi6k%2B6NjmC0H0hNA7Xxm0lx6VAv%2FpWlaz2CW4fpAogr8PmLAm%2BgZI9JHEARNbnrHFQJj8ttdOFDSnIzL5ZJDNwCNAAshN2bKjgcUXWHGwbJta3Zsc3o99%2BBIdmII9dD5%2BEZ5%2FwFkegAHzt1uPI4M88zJyr0WBYyEOQUi7E4aYHNrXv0z0uAUhKZJzcTyvx1KHJL%2ByANCUZ0fOFnAOiXK71VB0x4kHhIZejsymGpp13OzndcBoPogva6MuQzNafQx%2FztiquYfBegiMXBXK8Uo1FeflzQLbCfYpLgM0v9CVgfSQZODberRA%2FPnpEYSRiR6MJ2m98kGOqUBZIGPKOFJ2RABTAi9A8z0Jp07W6yZ%2BJ%2FPAzIOKYf4jaAfwY7llAhh1AYrpQJ4IS48fdHM8fsna8Ep2Sz4fgwO1tr1mECLWpyCQxiwz2%2Fm6nNlB432xQepcekxqu2NFQO7Pkjym3gap3nUMrDXnXkfHQkPGm%2FGS41BNu1Xr0SKyepuXX2vX1oj8bGE2iEbUZgNgu%2F94EXps61Un2JaAh3yucSj1alV&X-Amz-Signature=3dee0ed33077add06f42e8549decad78ad11019e052ed6ad96f49bd6b0525d64&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
Now we can reset the index. Again, it is important to do `inplace=True` as otherwise the DataFrame is not updated properly.
```python
players_df.reset_index(inplace=True)
```
In the updated DataFrame below we now can see that the column `Player` is a *normal* column again and the default index has been re-inserted.
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/1c343a9f-1a8f-4da3-94f2-72dc953341ae/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UCQLK72F%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T222516Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIAQ6ZxSgbB%2FjSr0HoqDGecf5chvkt%2FysdXX3%2BxaMKSgUAiEAn3eBcYqi5AgFU1LyxxPCLpdUkBu5rNXBZmDK12EGT60q%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDJfdXkd8e7pdY90h7CrcA6JtN81p5LmtPJtw7o73I3x3%2F3ntT8IzSvTQstkl1%2BsPBm6exaUU9AhfrDNmcTooGA3DqtOqBjGRvYEe4HrgyZfpwzmGme1t5aQ%2B%2B%2F4ZN6RvkWuJUzAUzrOry0IBKBUJFXHMkkEaKYd9%2B5CJjN2uazIOkoKCiDc9NoX2DGj7WbhQyvA7BQ6Jq1g%2BRSmUijMJtkfM0ebME4szeYDOaw0DF1KFvhu3%2BF%2BC05l0vuBCJ4U6rPv6K2KfWdG2c3OpGYb%2B4mhINSGQFXnpaeHPfaQs8ec7JdDtdJ5t9RZQQAVaz%2Bah8a0JcSXQnaYTVQp3mi6k%2B6NjmC0H0hNA7Xxm0lx6VAv%2FpWlaz2CW4fpAogr8PmLAm%2BgZI9JHEARNbnrHFQJj8ttdOFDSnIzL5ZJDNwCNAAshN2bKjgcUXWHGwbJta3Zsc3o99%2BBIdmII9dD5%2BEZ5%2FwFkegAHzt1uPI4M88zJyr0WBYyEOQUi7E4aYHNrXv0z0uAUhKZJzcTyvx1KHJL%2ByANCUZ0fOFnAOiXK71VB0x4kHhIZejsymGpp13OzndcBoPogva6MuQzNafQx%2FztiquYfBegiMXBXK8Uo1FeflzQLbCfYpLgM0v9CVgfSQZODberRA%2FPnpEYSRiR6MJ2m98kGOqUBZIGPKOFJ2RABTAi9A8z0Jp07W6yZ%2BJ%2FPAzIOKYf4jaAfwY7llAhh1AYrpQJ4IS48fdHM8fsna8Ep2Sz4fgwO1tr1mECLWpyCQxiwz2%2Fm6nNlB432xQepcekxqu2NFQO7Pkjym3gap3nUMrDXnXkfHQkPGm%2FGS41BNu1Xr0SKyepuXX2vX1oj8bGE2iEbUZgNgu%2F94EXps61Un2JaAh3yucSj1alV&X-Amz-Signature=a566d95110c1641bd51fbd1242ae9dcb7161d70476a274de6f6bddaddbf5e63e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
---
## [`.isna()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.isna.html)
---
**Syntax**
With this function we can check if a row / column / cell contains a `NaN` value. If it contains a `NaN` value, the function will return `True` else `False`.
`df[<< some column >>].isna()`
---
**Check single column for ****`NaN`**** values**
Let’s assume we have a DataFrame that we suspect to contain `NaN` values in a Column named as `Unnamed: 10`.
We can run the command below to check that accordingly. 
```python
players_df['Unnamed: 10'].isna()

######### OUTPUT #########
0      True
1      True
2      True
3      True
4      True
       ... 
535    True
536    True
537    True
538    True
539    True
Name: Unnamed: 10, Length: 540, dtype: bool
```
From the output above we see that the function returns for each row True or False depending on if the specific row contains a `NaN` value in this column.
If we want to check if all rows contain a `NaN` value we can run the following command.
```python
players_df['Unnamed: 10'].isna().all()

True # -> All rows contain NaN value in column 'Unnamed: 10'
```
We see that the command returns True, thus our suspicion was correct.
---
## [`.drop()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.drop.html)
---
**Syntax**
With this function we can remove / drop a specific column from a DataFrame. 
`df.drop( << column label >>, axis = 1, inplace = True)`
Usually `axis = 0` means column-wise and `axis = 1` means row-wise. However, when Python executed the drop function it goes through the DataFrame row-wise and removes the specific column field for each row separately.
> 💡 **When we want to drop a column from a DataFrame we need to set `axis = 1` !**
---
**Drop single column**
Let’s assume we have an unnecessary column `Unnamed: 10` in the DataFrame that does not include any valuable data.
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/3500737e-2456-4b38-af6d-a0173189cae1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RSK62P2X%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T222518Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJGMEQCIBKMhNRwCy7vdHHOqh1Q%2BLuJlMkWpZzV2%2B1lVaUbom7aAiBnCd3n0etLaCGaEUK6ipNkfaqobUigGC2%2B6HVed1Zsdyr%2FAwgnEAAaDDYzNzQyMzE4MzgwNSIMZY2wf2nTaTlExVzIKtwDXn3rxTQnuXnmAunTHg3MqJkrL6kZ5awFzYB1cq%2BQUKecnLmYvDvaC5ruDlRKfMeuNRjai0rVL1kgZxlXfTvEMncoxJlgPfc%2FhUJYzMELDzYl6tL5pGAnxfBQmThWN1L8k50CB4Pm6TsLg9Vuadihxwx%2FkRc8XhRwKFjU4ZMRdfzviiXhom6gPYzbTBePn5sJiSh9An%2BWDcJEQc25lskNEon0nHJtSBSHyl10GxYzg2%2BEjTslCGf9FAvyBil3fJTxvgVOR60lJoOI5XDp8k8nbYlx98nIaScvpTb6kGrNWaEqt1j5%2FAi80AxffZJUcGelhGT%2B8rl92HjLavomUtlFjL0ted%2Fbu7TdHRoO1cCOOQIjJW7A6rpd2PHun4SQ7CF%2FkB1YrgHdmMf8oeIfeeIk35hHpVS%2F8LJZJHvZXldafQQOzTfKORv3QLcL2iDIWxQCvVNvKzp1PJZyMJlfd74JLMGm%2FjYccNiuDoq0FjXvaNQLdhRrZvVtgQ9wMOWOsdORMdWUWaIwX%2Bzihb99yTUU5glFDbiSvC2ufj1qUhb50W%2BJUSALfv86M%2BIAm8YKrvBDdtmQiX9luMoQjDX6oNWAGDMbMZtSQkWTCRv1zHIeR1wJooMB9703dZuJnRYw0873yQY6pgHpUPS%2F7BJbJ%2FdNxIJibdtcRrqM7qzQNp%2FuEn8gxijN97nNccVHBCl0dYu9wP8tpFxPNtXqKjGJiaynFyHfwnpxDr8fJ9XWGZvQwUsvOU8OILXb8LPcQcZRQqz8gbkP4hWHhT67OB571tY9Sy8%2FzW9sGIvLxHgKsL5mmlqg49zvZtILxD1bmZHYZOHuXISwgartfp8twwiqYWtSqOGGYqYNLwCvaehF&X-Amz-Signature=83e7eb9a8834fd096458016af18ae080d413417fbbae2b12293da8f5420e12e0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
We can now get rid of this column by executing the following command.
```python
players_df.drop('Unnamed: 10', axis=1, inplace=True)
```
And the column is removed:
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/6be99418-6837-48ed-ba88-5757a28c6f5e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RSK62P2X%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T222518Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJGMEQCIBKMhNRwCy7vdHHOqh1Q%2BLuJlMkWpZzV2%2B1lVaUbom7aAiBnCd3n0etLaCGaEUK6ipNkfaqobUigGC2%2B6HVed1Zsdyr%2FAwgnEAAaDDYzNzQyMzE4MzgwNSIMZY2wf2nTaTlExVzIKtwDXn3rxTQnuXnmAunTHg3MqJkrL6kZ5awFzYB1cq%2BQUKecnLmYvDvaC5ruDlRKfMeuNRjai0rVL1kgZxlXfTvEMncoxJlgPfc%2FhUJYzMELDzYl6tL5pGAnxfBQmThWN1L8k50CB4Pm6TsLg9Vuadihxwx%2FkRc8XhRwKFjU4ZMRdfzviiXhom6gPYzbTBePn5sJiSh9An%2BWDcJEQc25lskNEon0nHJtSBSHyl10GxYzg2%2BEjTslCGf9FAvyBil3fJTxvgVOR60lJoOI5XDp8k8nbYlx98nIaScvpTb6kGrNWaEqt1j5%2FAi80AxffZJUcGelhGT%2B8rl92HjLavomUtlFjL0ted%2Fbu7TdHRoO1cCOOQIjJW7A6rpd2PHun4SQ7CF%2FkB1YrgHdmMf8oeIfeeIk35hHpVS%2F8LJZJHvZXldafQQOzTfKORv3QLcL2iDIWxQCvVNvKzp1PJZyMJlfd74JLMGm%2FjYccNiuDoq0FjXvaNQLdhRrZvVtgQ9wMOWOsdORMdWUWaIwX%2Bzihb99yTUU5glFDbiSvC2ufj1qUhb50W%2BJUSALfv86M%2BIAm8YKrvBDdtmQiX9luMoQjDX6oNWAGDMbMZtSQkWTCRv1zHIeR1wJooMB9703dZuJnRYw0873yQY6pgHpUPS%2F7BJbJ%2FdNxIJibdtcRrqM7qzQNp%2FuEn8gxijN97nNccVHBCl0dYu9wP8tpFxPNtXqKjGJiaynFyHfwnpxDr8fJ9XWGZvQwUsvOU8OILXb8LPcQcZRQqz8gbkP4hWHhT67OB571tY9Sy8%2FzW9sGIvLxHgKsL5mmlqg49zvZtILxD1bmZHYZOHuXISwgartfp8twwiqYWtSqOGGYqYNLwCvaehF&X-Amz-Signature=265dc5d40441f738a2dc5f82c45885f2de2f09b9e2f4437d4dd867e36c774ed1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
---
## [`.dropna()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.dropna.html)
---
**Syntax**
With this function we can drop / remove column and rows from a DataFrame that contain a `NaN` value.
`df.dropna(axis = << 0 or 1 >>, how = << 'any' or 'all' >>, inplace=True)`
Check the table below to understand what the different parameter values do.
|  | `axis = 0` | `axis = 1` |
| --- | --- | --- |
| `how = 'any'` | Python removes all **rows** that contain **at least one** `NaN` value. | Python removes all **columns** that contain **at least one** `NaN` value. |
| `how = 'all'` | Python removes all **rows** that contain `NaN` values **only**. | Python removes all **columns** that contain `NaN` values **only**. |
---
**Remove rows with ****`NaN`**** value**
Let’s set the value in column `Team` to `NaN` of the first and third player.
```python
players_df.iloc[[0, 2], 2] = np.NaN
players_df.iloc[:3]
```
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/281439eb-3e8c-4578-887f-f90824b57da7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VSQZGRNB%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T222520Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIEP3dZRDdnM9Nl8rp4Ai7ChrzcXel2bKLx3hQMHDZP6LAiEA0obeNw4Q1Cexl0CLFl1gZYvO5dzeXXuOwBezAwmbtdYq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDIn07wMI2Ow28xVBUircA6oHYcEcLvKf1jUzXjZOeYqRJZ2lLFkhVCtdxN5J%2FFFgqLDR6I9lgS5hpkXdX3I6mEA0GUTugdby%2B0md2lPmOiV%2B0ViNEI2If0ebtJKWRRWZWxvrNPBCArd1jrygsfiP9L%2BUVuDURxdHNqme5MlkL7oRfLY9HgR2C7%2F8FkfaNcG3nsjUKUxz6Up475S1hJgZBitpo1GPGMB0dfhCiGaCCtMgqHkILhNEktwzOYyHdedwJF4ksVwwLzouPaaBTuN8r92q59EKkLYbfY6VeiFHT4zdd9U48c4Tj1y3iieqA4tMeuly1m4G%2B5gNS%2BPVp%2FeIBYVllBwMiMJifq4KCBsq5SrQxEEo5Pr%2FyCPPE6EXYcU%2F0R5RWNXWiNqq39ARqoaTMzpja0YEmmEEqXP1ViyJ23LoQ9wX%2Bj7xrsP2AXxibMnI7y3O%2F98d7M87TG3XR%2F4rDpSjQs5EiF7Q%2BopukWARVm%2B%2F41zQBtnMBhuFX5MnCvHOwNHuZ%2FcPZJZKkrm0L5fUfpnLU8cQhDwBsTTp4QU0qx%2BG68GTItJ7oQW13qhzCHsblc8DSpExjSjsTDzEmkqyh6gyIQdfaNP%2B5HQ2LtNOl9AVdTp0M38aUICvBXwsL8ZNoiTznYshSHtqLAVxMMjO98kGOqUBGc8u82vLZ9DV7UGY%2FHvYROZHX2m4K4cEgjvP7QFKGV6QmtDZ8oVKT3%2BmO4vPDBgQdH8Q0976mYXQgU63h6ywBj7iCPVVmHinYquiNylgxaGmub7BIixUC5ZcDrOIvjHHbTt6QwavZKtuRUyaTmyVHkXdgK2Su96wDnqu1xdLLc%2FicNyonD5vi%2FLOdMJ9xjpLNjEF1OEX8MkF2gPYCOItB9d0t6Mo&X-Amz-Signature=cf8fc4c64b6c10cf29629a5bfc5ced142d00c2ed774e403e01170b9e6f48103c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
We see that the values have been updated to `NaN`
Let’s remove the column `Team` using `.dropna()`
```python
players_df.dropna(axis=0, how='any', inplace=True)
players_df[:3]
```
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/5f6f5b09-95c7-4fd4-a7fe-ee8d8e53f780/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VSQZGRNB%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T222520Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIEP3dZRDdnM9Nl8rp4Ai7ChrzcXel2bKLx3hQMHDZP6LAiEA0obeNw4Q1Cexl0CLFl1gZYvO5dzeXXuOwBezAwmbtdYq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDIn07wMI2Ow28xVBUircA6oHYcEcLvKf1jUzXjZOeYqRJZ2lLFkhVCtdxN5J%2FFFgqLDR6I9lgS5hpkXdX3I6mEA0GUTugdby%2B0md2lPmOiV%2B0ViNEI2If0ebtJKWRRWZWxvrNPBCArd1jrygsfiP9L%2BUVuDURxdHNqme5MlkL7oRfLY9HgR2C7%2F8FkfaNcG3nsjUKUxz6Up475S1hJgZBitpo1GPGMB0dfhCiGaCCtMgqHkILhNEktwzOYyHdedwJF4ksVwwLzouPaaBTuN8r92q59EKkLYbfY6VeiFHT4zdd9U48c4Tj1y3iieqA4tMeuly1m4G%2B5gNS%2BPVp%2FeIBYVllBwMiMJifq4KCBsq5SrQxEEo5Pr%2FyCPPE6EXYcU%2F0R5RWNXWiNqq39ARqoaTMzpja0YEmmEEqXP1ViyJ23LoQ9wX%2Bj7xrsP2AXxibMnI7y3O%2F98d7M87TG3XR%2F4rDpSjQs5EiF7Q%2BopukWARVm%2B%2F41zQBtnMBhuFX5MnCvHOwNHuZ%2FcPZJZKkrm0L5fUfpnLU8cQhDwBsTTp4QU0qx%2BG68GTItJ7oQW13qhzCHsblc8DSpExjSjsTDzEmkqyh6gyIQdfaNP%2B5HQ2LtNOl9AVdTp0M38aUICvBXwsL8ZNoiTznYshSHtqLAVxMMjO98kGOqUBGc8u82vLZ9DV7UGY%2FHvYROZHX2m4K4cEgjvP7QFKGV6QmtDZ8oVKT3%2BmO4vPDBgQdH8Q0976mYXQgU63h6ywBj7iCPVVmHinYquiNylgxaGmub7BIixUC5ZcDrOIvjHHbTt6QwavZKtuRUyaTmyVHkXdgK2Su96wDnqu1xdLLc%2FicNyonD5vi%2FLOdMJ9xjpLNjEF1OEX8MkF2gPYCOItB9d0t6Mo&X-Amz-Signature=d1cac90aeea7cab1fd550e7663d8c79a968fbfb1eaaf500d50c8afbf5a371855&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
We see that the players Jamie Vardy and Pierre-Emerick Aubameyang have been removed as they contained at least one `NaN` value (in column `Team`).
---
**Remove columns with ****`NaN`**** value**
Now let’s set all values in column `Goals` to `NaN` values, except the first one.
```python
players_df.iloc[1:, 6] = np.NaN
players_df
```
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/ad5ad8d5-f3a1-4426-8c36-08628fbe3f75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VSQZGRNB%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T222520Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIEP3dZRDdnM9Nl8rp4Ai7ChrzcXel2bKLx3hQMHDZP6LAiEA0obeNw4Q1Cexl0CLFl1gZYvO5dzeXXuOwBezAwmbtdYq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDIn07wMI2Ow28xVBUircA6oHYcEcLvKf1jUzXjZOeYqRJZ2lLFkhVCtdxN5J%2FFFgqLDR6I9lgS5hpkXdX3I6mEA0GUTugdby%2B0md2lPmOiV%2B0ViNEI2If0ebtJKWRRWZWxvrNPBCArd1jrygsfiP9L%2BUVuDURxdHNqme5MlkL7oRfLY9HgR2C7%2F8FkfaNcG3nsjUKUxz6Up475S1hJgZBitpo1GPGMB0dfhCiGaCCtMgqHkILhNEktwzOYyHdedwJF4ksVwwLzouPaaBTuN8r92q59EKkLYbfY6VeiFHT4zdd9U48c4Tj1y3iieqA4tMeuly1m4G%2B5gNS%2BPVp%2FeIBYVllBwMiMJifq4KCBsq5SrQxEEo5Pr%2FyCPPE6EXYcU%2F0R5RWNXWiNqq39ARqoaTMzpja0YEmmEEqXP1ViyJ23LoQ9wX%2Bj7xrsP2AXxibMnI7y3O%2F98d7M87TG3XR%2F4rDpSjQs5EiF7Q%2BopukWARVm%2B%2F41zQBtnMBhuFX5MnCvHOwNHuZ%2FcPZJZKkrm0L5fUfpnLU8cQhDwBsTTp4QU0qx%2BG68GTItJ7oQW13qhzCHsblc8DSpExjSjsTDzEmkqyh6gyIQdfaNP%2B5HQ2LtNOl9AVdTp0M38aUICvBXwsL8ZNoiTznYshSHtqLAVxMMjO98kGOqUBGc8u82vLZ9DV7UGY%2FHvYROZHX2m4K4cEgjvP7QFKGV6QmtDZ8oVKT3%2BmO4vPDBgQdH8Q0976mYXQgU63h6ywBj7iCPVVmHinYquiNylgxaGmub7BIixUC5ZcDrOIvjHHbTt6QwavZKtuRUyaTmyVHkXdgK2Su96wDnqu1xdLLc%2FicNyonD5vi%2FLOdMJ9xjpLNjEF1OEX8MkF2gPYCOItB9d0t6Mo&X-Amz-Signature=d4a802da1764206d7a663e4a3a9581f6d3768023b7e4ddb6aef46e574f9396ac&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
We see that all values in column `Goals` are `NaN` except for the first player.
Let’s try to drop that column `Goals` using `.dropna()`
```python
players_df.dropna(axis=1, how='all', inplace=True)
players_df
```
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/ad5ad8d5-f3a1-4426-8c36-08628fbe3f75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VSQZGRNB%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T222520Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIEP3dZRDdnM9Nl8rp4Ai7ChrzcXel2bKLx3hQMHDZP6LAiEA0obeNw4Q1Cexl0CLFl1gZYvO5dzeXXuOwBezAwmbtdYq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDIn07wMI2Ow28xVBUircA6oHYcEcLvKf1jUzXjZOeYqRJZ2lLFkhVCtdxN5J%2FFFgqLDR6I9lgS5hpkXdX3I6mEA0GUTugdby%2B0md2lPmOiV%2B0ViNEI2If0ebtJKWRRWZWxvrNPBCArd1jrygsfiP9L%2BUVuDURxdHNqme5MlkL7oRfLY9HgR2C7%2F8FkfaNcG3nsjUKUxz6Up475S1hJgZBitpo1GPGMB0dfhCiGaCCtMgqHkILhNEktwzOYyHdedwJF4ksVwwLzouPaaBTuN8r92q59EKkLYbfY6VeiFHT4zdd9U48c4Tj1y3iieqA4tMeuly1m4G%2B5gNS%2BPVp%2FeIBYVllBwMiMJifq4KCBsq5SrQxEEo5Pr%2FyCPPE6EXYcU%2F0R5RWNXWiNqq39ARqoaTMzpja0YEmmEEqXP1ViyJ23LoQ9wX%2Bj7xrsP2AXxibMnI7y3O%2F98d7M87TG3XR%2F4rDpSjQs5EiF7Q%2BopukWARVm%2B%2F41zQBtnMBhuFX5MnCvHOwNHuZ%2FcPZJZKkrm0L5fUfpnLU8cQhDwBsTTp4QU0qx%2BG68GTItJ7oQW13qhzCHsblc8DSpExjSjsTDzEmkqyh6gyIQdfaNP%2B5HQ2LtNOl9AVdTp0M38aUICvBXwsL8ZNoiTznYshSHtqLAVxMMjO98kGOqUBGc8u82vLZ9DV7UGY%2FHvYROZHX2m4K4cEgjvP7QFKGV6QmtDZ8oVKT3%2BmO4vPDBgQdH8Q0976mYXQgU63h6ywBj7iCPVVmHinYquiNylgxaGmub7BIixUC5ZcDrOIvjHHbTt6QwavZKtuRUyaTmyVHkXdgK2Su96wDnqu1xdLLc%2FicNyonD5vi%2FLOdMJ9xjpLNjEF1OEX8MkF2gPYCOItB9d0t6Mo&X-Amz-Signature=d4a802da1764206d7a663e4a3a9581f6d3768023b7e4ddb6aef46e574f9396ac&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
We see that the column Goals was not removed. This is because we set `how` to `'all'`. Therefore, Python drops the column only if all values are `NaN`, which however is not the case as the first player has a normal value in column `Goals`.
Let’s set the value of the first player in column `Goals` to `NaN` as well.
```python
players_df.loc[0, 'Goals'] = np.NaN
players_df
```
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/5ca553a1-414f-4170-9177-39820cbd9529/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VSQZGRNB%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T222521Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIEP3dZRDdnM9Nl8rp4Ai7ChrzcXel2bKLx3hQMHDZP6LAiEA0obeNw4Q1Cexl0CLFl1gZYvO5dzeXXuOwBezAwmbtdYq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDIn07wMI2Ow28xVBUircA6oHYcEcLvKf1jUzXjZOeYqRJZ2lLFkhVCtdxN5J%2FFFgqLDR6I9lgS5hpkXdX3I6mEA0GUTugdby%2B0md2lPmOiV%2B0ViNEI2If0ebtJKWRRWZWxvrNPBCArd1jrygsfiP9L%2BUVuDURxdHNqme5MlkL7oRfLY9HgR2C7%2F8FkfaNcG3nsjUKUxz6Up475S1hJgZBitpo1GPGMB0dfhCiGaCCtMgqHkILhNEktwzOYyHdedwJF4ksVwwLzouPaaBTuN8r92q59EKkLYbfY6VeiFHT4zdd9U48c4Tj1y3iieqA4tMeuly1m4G%2B5gNS%2BPVp%2FeIBYVllBwMiMJifq4KCBsq5SrQxEEo5Pr%2FyCPPE6EXYcU%2F0R5RWNXWiNqq39ARqoaTMzpja0YEmmEEqXP1ViyJ23LoQ9wX%2Bj7xrsP2AXxibMnI7y3O%2F98d7M87TG3XR%2F4rDpSjQs5EiF7Q%2BopukWARVm%2B%2F41zQBtnMBhuFX5MnCvHOwNHuZ%2FcPZJZKkrm0L5fUfpnLU8cQhDwBsTTp4QU0qx%2BG68GTItJ7oQW13qhzCHsblc8DSpExjSjsTDzEmkqyh6gyIQdfaNP%2B5HQ2LtNOl9AVdTp0M38aUICvBXwsL8ZNoiTznYshSHtqLAVxMMjO98kGOqUBGc8u82vLZ9DV7UGY%2FHvYROZHX2m4K4cEgjvP7QFKGV6QmtDZ8oVKT3%2BmO4vPDBgQdH8Q0976mYXQgU63h6ywBj7iCPVVmHinYquiNylgxaGmub7BIixUC5ZcDrOIvjHHbTt6QwavZKtuRUyaTmyVHkXdgK2Su96wDnqu1xdLLc%2FicNyonD5vi%2FLOdMJ9xjpLNjEF1OEX8MkF2gPYCOItB9d0t6Mo&X-Amz-Signature=c0309f98d308f67579aa3568551d20df03c6f457490b83a391caa100f7992690&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
We see that the column `Goals` now contains `NaN` values only. So let’s try to run the `.dropna()` command from before again.
```python
players_df.dropna(axis=1, how='all', inplace=True)
players_df
```
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/e67efd46-7779-477d-95d2-b7ad6a53c9bf/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VSQZGRNB%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T222521Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIEP3dZRDdnM9Nl8rp4Ai7ChrzcXel2bKLx3hQMHDZP6LAiEA0obeNw4Q1Cexl0CLFl1gZYvO5dzeXXuOwBezAwmbtdYq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDIn07wMI2Ow28xVBUircA6oHYcEcLvKf1jUzXjZOeYqRJZ2lLFkhVCtdxN5J%2FFFgqLDR6I9lgS5hpkXdX3I6mEA0GUTugdby%2B0md2lPmOiV%2B0ViNEI2If0ebtJKWRRWZWxvrNPBCArd1jrygsfiP9L%2BUVuDURxdHNqme5MlkL7oRfLY9HgR2C7%2F8FkfaNcG3nsjUKUxz6Up475S1hJgZBitpo1GPGMB0dfhCiGaCCtMgqHkILhNEktwzOYyHdedwJF4ksVwwLzouPaaBTuN8r92q59EKkLYbfY6VeiFHT4zdd9U48c4Tj1y3iieqA4tMeuly1m4G%2B5gNS%2BPVp%2FeIBYVllBwMiMJifq4KCBsq5SrQxEEo5Pr%2FyCPPE6EXYcU%2F0R5RWNXWiNqq39ARqoaTMzpja0YEmmEEqXP1ViyJ23LoQ9wX%2Bj7xrsP2AXxibMnI7y3O%2F98d7M87TG3XR%2F4rDpSjQs5EiF7Q%2BopukWARVm%2B%2F41zQBtnMBhuFX5MnCvHOwNHuZ%2FcPZJZKkrm0L5fUfpnLU8cQhDwBsTTp4QU0qx%2BG68GTItJ7oQW13qhzCHsblc8DSpExjSjsTDzEmkqyh6gyIQdfaNP%2B5HQ2LtNOl9AVdTp0M38aUICvBXwsL8ZNoiTznYshSHtqLAVxMMjO98kGOqUBGc8u82vLZ9DV7UGY%2FHvYROZHX2m4K4cEgjvP7QFKGV6QmtDZ8oVKT3%2BmO4vPDBgQdH8Q0976mYXQgU63h6ywBj7iCPVVmHinYquiNylgxaGmub7BIixUC5ZcDrOIvjHHbTt6QwavZKtuRUyaTmyVHkXdgK2Su96wDnqu1xdLLc%2FicNyonD5vi%2FLOdMJ9xjpLNjEF1OEX8MkF2gPYCOItB9d0t6Mo&X-Amz-Signature=0e6f013e3c4cdd7c8173c78a02a1c923c54072518cb0cfa6b0bbafca8d441b3d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
We see now that the column `Goals` has been removed successfully.
---
## Insert new column
---
**Syntax**
When we want to insert a new column we can do it as follow.
`df[<< new column name >>] = << value of new column >>`
It is important to note that we must provide values for the new column for all existing rows in the DataFrame. But we don’t have to worry that much about this as often we calculate the values of the new column based on other columns in the DataFrame anyway. 
---
**Create new column**
Let’s assume we want a new column Total Points which should be the sum of the column Goals and Assists.
```python
players_df['Total points'] = players_df['Goals'] + players_df['Assists']
players_df
```
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/b3a38d78-543d-4e69-aabf-aba15f3000db/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QYNAQ2E2%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T222523Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQCLRTFHEegV%2FJVGxGjO1uCvkplENliJBlKYyaiQ2emJbwIhAJxIhWxwFGfwfrxZNciuYTj6yHyG1eZlmb7QKQopFLZnKv8DCCgQABoMNjM3NDIzMTgzODA1Igw8Xy%2BLODMXjBOOUtIq3AOsBwqary91DR6ZiNyMOmtckvBY3nkizXhF9YsspHjzyDeP5eEVDteH2gQmevRpOIa4S3YptnV0KAJbZPy%2BzuvGb8nAQr7vM3dSQijlTGd6vXqNw%2BiGyOAAsYHwhPpK%2BSjcH3Fndvli%2FFeJPzsAsFN7rXmbq%2BuusX8v1ANb0L5vBaX1te8Eio7QiFg7HZgvC5KQSkgSquw2i%2Fi3FU%2BrUS5SfnV4ukHjw1lnvkpQzi7dtWtD5X1JtqpP6XXjg4cDCE5aMCvGcS6hvkVbgC%2FS4ZxHyXdlbSNif6Y627o6ryFdGZ%2BBl2bF0YttLVwibfv2vX88N2RuCvYKeXFTl6MF2gajNUTCNu%2FvNz2HjYQonW4%2BYALn86YrMZ%2FKIKIv3AgpPh4PdSgrwsfW9yKIppdlPoDt%2FVyJ4fGUoJ3g8ZYfrRTXgZslFZvXt%2Br5EJfNZ3%2F3ZYd%2Bh2gFcyvoPur0w6CvRj4VJKESx6H0tRpEQfgyW2h4XWQFqxmKZcxhCTdXN54lXzjdEVIpa3edi%2FQjqPdILiy2V%2F%2BwPqia4zeL%2Fm6DsU%2BNTeWE54hLcoILHZfYqKgKdb9k%2Fb0iaxaefyU5%2BI13%2BuBgyJ%2Fqr4VvPQTrgbhIxoxDwOEE%2B5ZZbppm0cIVJTCaz%2FfJBjqkAcVHIgLP4legjcR7GdHvN%2FpqvCz2asaqAmLlYCV6th7k9G43AW0kOwfe3O6KYE%2FTFUNbmN06hlaBN%2FS8zC5KKlNqqfazx7Nh7mO3m87E8dqMd9K8yQVjzgXjNRWdg2NxIXXUMbfW2YfAhbLXuCSqzqkDPxBnCv8PpXBApV8vGl53rD%2Bo4J4dAy2Zl62HwoqaVJWmPCKy2dwvTDKcfSD1Ojw89B%2Fo&X-Amz-Signature=5d6dc0d804f2ab2733ef54bf8307fe1c4c39fe5f33cfd7ec2e7460aec0bb1c1a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
We see that a new column `Total points` was inserted which is calculated based on the values in column `Goals` and `Assists`.
---
## [`.apply()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.apply.html)
---
**Syntax**
With this function we can take the existing values in a column, compute something and update the values again.
`df[<< some column >>].apply(lambda x : << some function >>)`
As can be seen we have again a `lambda` function here. What Python does is it takes each value out of `<< some column >>` and throws it into the `lambda` function in which we define what computation we want to do with the value.
---
**Create new column based on values in other column**
Let’s assume we want to calculate how many days each player has played. We already have the column `Minutes played`. Thus, in a first step we simply create a new column `Days played` and set it to the same values as column `Minutes played`.
```python
players_df['days_played'] = players_df['Minutes played']
players_df
```
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/e6cb3aae-51fa-4146-bfe6-5962772911ac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665R7APL2S%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T222524Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCICK9tx8rbqpVEHHhRrr7N9aDxPfNyXde6nYVGZlx7KSxAiEAnrfwgeDX1Y2GzbFG7hJlW5nin9lW1Qf2CMLOsU3ZsWcq%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDITPmntmloDALULtVyrcA%2FeG4wz78gR3YsvIYsEP8uq0qcvC7s6qfr4W8NBPUQHlU8L7%2BCnpver9LcBQAbXDjwHcuXHMImgRMl%2FH4gIJf9lc7yzduUQeBRyXskeagqWOaSDOObzb6jz9jibUEeK5o%2FUh7MPwYSISvc%2FBxybngAC9V6aSKLteVR6yjTP3W0iAelA%2BAvxrXpQBPKXXsxEvzhqddWh2nCuAHh%2BzxEW5M8Vekv9RRuEL4QRxs6JskYGGCUNcJab0ziL6tZddrky2Z%2BAfVt0o3NLZJGjyAIVWiKwPiexXbjTlxrMhQN92560AEfXe%2BOInQwqcbEAGYBZ9JoUzGvaWdWrf9a3bHZE4jm5yXIxMYe60kWBDpnCogj6fh1kxuNlDUQr9hx83CtG0IoEu8c3h%2BPEEH3vjN2EXgSNch0FgiEVhXvCRDW%2Fzqx6M48e%2FgUTZK6nu6PKx8C5CTWRD4O0Nn%2F%2FLV4U8GTO8YldnJumosGm5pyz6OVemcydHbmH9BHMg3SDrHKWO4orjfHI5v7YmY6BeG2L0zaJDzDFW254wV8tDzbPbgC8V2Dtwf2UJJMnFpXMV8X1RCLbvkJ4qwEjLbaNQQhk%2B07WVtcEPLSyGhbPES%2F8A5sui5efstN3u%2FTrqIAIjY1z%2FMJim98kGOqUBvIu1npd0%2B%2FkSj5KF5bOkDYX87P88XOlo0lc4eItwFWkmqq17suw83ulf7U6%2BC84Cq5f4Ykjht6Scx%2BhFAq3zB2vB28Zy9qxaBgH%2Bz3DQ8n2g023391fE88rgJYs845Ke1nmMyc0VvuddxZ2hvlt18VBwhmMqPzy6wunx0Wm7rd7kF4nbYnujlR6l2AGsFR6PMj9Y%2BuGMIZh6x8EuzaGTzi4wcf8S&X-Amz-Signature=aaa82f2484ee802e55d8812ab6aec7c05d724bbd0e447fd837f0293b3b9a6454&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
We see that we have now a new column `days_played` which currently has the same values as `Minutes played`.
To convert the minutes in column `days_played` to days we can make use of the `.apply()` function.
```python
players_df['days_played'] = players_df['days_played'].apply(lambda x : x / 60 / 24)
players_df
```
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/02dda6da-5622-463a-9140-8612b4cea207/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665R7APL2S%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T222524Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCICK9tx8rbqpVEHHhRrr7N9aDxPfNyXde6nYVGZlx7KSxAiEAnrfwgeDX1Y2GzbFG7hJlW5nin9lW1Qf2CMLOsU3ZsWcq%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDITPmntmloDALULtVyrcA%2FeG4wz78gR3YsvIYsEP8uq0qcvC7s6qfr4W8NBPUQHlU8L7%2BCnpver9LcBQAbXDjwHcuXHMImgRMl%2FH4gIJf9lc7yzduUQeBRyXskeagqWOaSDOObzb6jz9jibUEeK5o%2FUh7MPwYSISvc%2FBxybngAC9V6aSKLteVR6yjTP3W0iAelA%2BAvxrXpQBPKXXsxEvzhqddWh2nCuAHh%2BzxEW5M8Vekv9RRuEL4QRxs6JskYGGCUNcJab0ziL6tZddrky2Z%2BAfVt0o3NLZJGjyAIVWiKwPiexXbjTlxrMhQN92560AEfXe%2BOInQwqcbEAGYBZ9JoUzGvaWdWrf9a3bHZE4jm5yXIxMYe60kWBDpnCogj6fh1kxuNlDUQr9hx83CtG0IoEu8c3h%2BPEEH3vjN2EXgSNch0FgiEVhXvCRDW%2Fzqx6M48e%2FgUTZK6nu6PKx8C5CTWRD4O0Nn%2F%2FLV4U8GTO8YldnJumosGm5pyz6OVemcydHbmH9BHMg3SDrHKWO4orjfHI5v7YmY6BeG2L0zaJDzDFW254wV8tDzbPbgC8V2Dtwf2UJJMnFpXMV8X1RCLbvkJ4qwEjLbaNQQhk%2B07WVtcEPLSyGhbPES%2F8A5sui5efstN3u%2FTrqIAIjY1z%2FMJim98kGOqUBvIu1npd0%2B%2FkSj5KF5bOkDYX87P88XOlo0lc4eItwFWkmqq17suw83ulf7U6%2BC84Cq5f4Ykjht6Scx%2BhFAq3zB2vB28Zy9qxaBgH%2Bz3DQ8n2g023391fE88rgJYs845Ke1nmMyc0VvuddxZ2hvlt18VBwhmMqPzy6wunx0Wm7rd7kF4nbYnujlR6l2AGsFR6PMj9Y%2BuGMIZh6x8EuzaGTzi4wcf8S&X-Amz-Signature=cd9a070cb2ae2a508f51abc55ce9ecc213401dae0a5d5e5effafbc52cf2f6210&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
We see now that we successfully converted the minutes in column `days_played` to days. Python went through the entire DataFrame took the minutes value, put it into the `lambda` function, where it was converted into days and updated the value.
It is important to note that with `.apply()` we must explicitly assign the new values to the column. That’s why we put `players_df['days_played']` in front. 
---
## [`.where()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.where.html)
---
**Syntax**
With this function we can apply an operation on rows that meet the specified condition, i.e., for which the condition evaluates to `True`. 
`np.where(<< condition to check >>, << val if True >>, << val if False >>)`
Python goes through each row in the DataFrame and checks the condition, if the check yields `True`, then the value passed as second parameter is applied, if the check yields `False` then the value passed as third parameter is applied. 
> 💡 **The `.where()` function comes from numpy, thus we must call it with `.np`!**
---
**Create new column based on condition**
Let’s assume we want to create a new column in our DataFrame `Points per Game`. This column should be calculated as `Total points` divided by `Games started`. However, we want to calculate the `Points per Game` only for those players who have started in more than 10 games, otherwise we just fill in the value `NaN`.
Thus our parameters are:
- Condition: Player started in more than 10 games
- If True: value = `Total points / Games started`
- If False: value = `NaN`
Let’s wrap the three bullet points into the `np.where()` function:
```python
players_df['Points per Game'] = np.where(players_df['Games started'] > 10, players_df['total_points'] / players_df['Games started'], np.nan)
players_df
```
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/64f23972-80aa-4d97-bf3a-54c0965029ac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TUHWYW4U%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T222527Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIB9Y2KF36Ug7%2FliDpzBLsaZfyC7IhMMRzBri4X%2F1GMgHAiEAvuueQaAG%2B8nnp5BviSNuTLJx3JTQ80IqpF8FykMg1hIq%2FwMIKBAAGgw2Mzc0MjMxODM4MDUiDDFiq%2Bos1xUcj4STAircAxMNOOOkPBIBQc50u%2FV7GTknCKem%2Bf5noslBUDBxBznL3liwEon4vp7aA3hnbKdoVN5Git3jzv3D5LTjwYedqPA7lS2hTNIsndodgMCtuB%2BdSuNwAuXIPtYBrIZXp0iWd9GqfZX1rCQN79LcZCyGURHFKonQzujLO4vieN2n8KAQZ%2BPVfddt%2BwPvE8QOv%2BoxT%2BOsLQcTeZ7eKgv%2B8D8DSyn%2FHNH3mdXNhUNwm4uOf7oCAccW72U3DL%2BKM0h6eN9l9CL0z2d5n%2FMvhVk%2B3Xq6phuOk6tDqdOqtW2CHHhfBJRJONEAV0jL52E4Of%2BL1rqz66mYb3IkmfCBoL74wF9UCCBdk05tXJQ%2FfnRt%2FdTAtyUnh5wOK6xFPQ0%2Byc%2FJmbOhPpmS30yGlGt1npbVTOLMoJK3CVDdoY2536my7k484uMpV5SSDFsn8G0uAznV%2FwXe77w9MIGPkzvvXZTa1qgz2AxHGK0eDBkCcAYW2XlZOCFqGSdE0knbn8MiA9IYYGB3SC5IL5JKx1JBwNEPZ0g0HHKmIylh2%2BRWwSN3fJz9cunR7EMnEOTv%2BbXUwPJUwt3o0n%2FbPvZkGsb%2Fi4mk3qwPsJ%2FyDutjZf49gZuk%2FgFVR1QWXLZsx1%2F%2B5myMUhvpMMDO98kGOqUBmjFqWxbwnOYbPh0xJHHP2uX16p1m2xan7IBAZwJiO%2BIo0RK4UvxsCKnE8IZVbX3klBO5ENAzz0ccaqdEuDBrdb7QoZvb7x0H%2FvCqMNCeSfupI45aBumGO0SwdTrABUd8t28w843yJAIuTpodme5T17AK3giiJ5cSJCp1Ohz9D%2B789iJsKTsiBxYW7OTZ7StG9ce7C3L8wYxwTZD392%2BI6PRnyfDf&X-Amz-Signature=ea06f32ec5ec006d032e7fad72d2b4aacdaeb74ed78ef4bad2664239e46f4259&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
We see that the values in `Points per Game` column were only calculated for those players who have started in at least 10 games. For the other players, the value in `Points per Game `column has been set to `NaN`.
---
## [`.set_option()`](https://pandas.pydata.org/pandas-docs/version/0.17.0/generated/pandas.set_option.html)
---
**Syntax**
This function allows us to define a multitude of global pandas options / settings.
`pd.set_option( << option parameter >>, << value >> )`
---
**Setting ****`display.precision`**** option**
When we look at the DataFrame `players_df` we see that in column `points_per_game` there are many digits after the point. This hinders readability and it is generally considered as unnecessary to display so many `digits` after the point. 
![Values in column `points_per_game` are displayed with many digits after the point](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/55a9009d-5f21-44bb-9902-54885088791f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664USOS3TZ%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T222528Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJGMEQCIG1XC1%2FQLXa%2FiWDu3oHy1V2KshRZZ8OPxDRo42LRPvjjAiBTZQIH1D7dO5v3t%2BwgmTKFN8Awx8YiydH15vwJiHTmzyr%2FAwgoEAAaDDYzNzQyMzE4MzgwNSIMisPvTuDj2JXz9KKUKtwDRhKIQ12uoOlPv2MlcYM8zkh5Y9CBRmIc3BzUB%2BgTk%2FOzMfOLytKtMY14R1VjggM9pKBQD6K9a94EwYpbS7igeW8ONqFVxdQF%2F7RygXY7yHBNpQBJoqFE%2FDLm3qr5WL3yt%2BXGVqkjHSlbhQ0bO7hIZiLVENtTkwkIDpXekrJ6j%2BmorrlA4zC4YCvShWS4bvCzwYt%2BIHFY%2Fnz0C0uJ2YrLvsKt1z6NaYE12CANLNkgYBdc99U9HrIRD7jrTsmedwTjwsWAk1TrA95O9RfmRas44NGoJfHtEoljByHavz3E415MG3%2FJ7fAbws59pHAd4MBQRuk9Jwsj5nKqfLj8SrLj1QdLO95gOH5iraESu280eiNQnQC3Pr7iIfxSjKPjpc4n%2F7HbI4eE6T9JKjaxQCdgTuF6baX5tqxJZDJ0sFyCj6v59D%2BPhnlsXdrNbm%2BptIhzKXnUAYTVBaWLI3eIMV1PPqj2zXPmQIpAOrSYMsljhRv6d%2BDRW9AldvC%2BeM1dQZz8fEXuu2LZdhshq9bjgTEMfs6nat0GvgNHjk9PCcFY1KrZcm%2Fu3MSCF1IhdPe9RFDbKHEyHRRGuCxotEwYh9ABSjCfyiM1fcYMTCkFfRjxK4gE%2F4Lj1opaSd2%2BDlIw1s73yQY6pgGwSVkZcIfab9RdSqJhWQAw675K0OIR7QZIkBsUPYs0%2BpgcrjtbuXnqSF4VY9f1ubHzWdO64FGUlgSQICYGlkPGd4yCFQFcMthCGSBdUN%2BwbBH68Rv4mR30pCEjgSx4ZWB2VaIR%2BEr8BHs%2FHLoX0GOKoKyl9r9sy5vhoN4vPcGt8mOzCv7SexunfU5M9WomMFh8UAfzdAZGMdK5uckfM4KZKDS1XQWY&X-Amz-Signature=c5bc17a99c6a2f31594927992aa25ddbde46c8907af3855934fbb4971e75e80b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
To mitigate this issue we can set the `global display.precision` option to value `2`.
```python
pd.set_option("display.precision", 2)
```
![Values in column `points_per_game` are now display with 2 digits after the point only](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/a0af3d06-c869-442f-b9aa-8db80bce1341/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664USOS3TZ%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T222528Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJGMEQCIG1XC1%2FQLXa%2FiWDu3oHy1V2KshRZZ8OPxDRo42LRPvjjAiBTZQIH1D7dO5v3t%2BwgmTKFN8Awx8YiydH15vwJiHTmzyr%2FAwgoEAAaDDYzNzQyMzE4MzgwNSIMisPvTuDj2JXz9KKUKtwDRhKIQ12uoOlPv2MlcYM8zkh5Y9CBRmIc3BzUB%2BgTk%2FOzMfOLytKtMY14R1VjggM9pKBQD6K9a94EwYpbS7igeW8ONqFVxdQF%2F7RygXY7yHBNpQBJoqFE%2FDLm3qr5WL3yt%2BXGVqkjHSlbhQ0bO7hIZiLVENtTkwkIDpXekrJ6j%2BmorrlA4zC4YCvShWS4bvCzwYt%2BIHFY%2Fnz0C0uJ2YrLvsKt1z6NaYE12CANLNkgYBdc99U9HrIRD7jrTsmedwTjwsWAk1TrA95O9RfmRas44NGoJfHtEoljByHavz3E415MG3%2FJ7fAbws59pHAd4MBQRuk9Jwsj5nKqfLj8SrLj1QdLO95gOH5iraESu280eiNQnQC3Pr7iIfxSjKPjpc4n%2F7HbI4eE6T9JKjaxQCdgTuF6baX5tqxJZDJ0sFyCj6v59D%2BPhnlsXdrNbm%2BptIhzKXnUAYTVBaWLI3eIMV1PPqj2zXPmQIpAOrSYMsljhRv6d%2BDRW9AldvC%2BeM1dQZz8fEXuu2LZdhshq9bjgTEMfs6nat0GvgNHjk9PCcFY1KrZcm%2Fu3MSCF1IhdPe9RFDbKHEyHRRGuCxotEwYh9ABSjCfyiM1fcYMTCkFfRjxK4gE%2F4Lj1opaSd2%2BDlIw1s73yQY6pgGwSVkZcIfab9RdSqJhWQAw675K0OIR7QZIkBsUPYs0%2BpgcrjtbuXnqSF4VY9f1ubHzWdO64FGUlgSQICYGlkPGd4yCFQFcMthCGSBdUN%2BwbBH68Rv4mR30pCEjgSx4ZWB2VaIR%2BEr8BHs%2FHLoX0GOKoKyl9r9sy5vhoN4vPcGt8mOzCv7SexunfU5M9WomMFh8UAfzdAZGMdK5uckfM4KZKDS1XQWY&X-Amz-Signature=b5dff81860c3b22f85fd1331a8ce2e118b144142ce1d933536bbce2a142938f3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
> 💡 **There are many more option parameters that we can customise as can be seen in the [official documentation](/1867045b058343e1a66b677961515907).**
---
## [`.astype()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.astype.html)
---
**Syntax**
With this function we can cast values in a DataFrame or Series into a specific data type. 
`df.astype( << new data type >> )`
---
**Modify data type of single column**
Let’s assume we create a simple DataFrame that contains strings in all three columns strings.
```python
import pandas as pd 

data = {
  "calories": ['420', '380', '390', '200', '100'],
  "duration": ['50', '40', '45', '60', '70'],
  "bmi" : ['21.2', '19.8', '23.4', '25.6', '26.1']
}

df = pd.DataFrame(data)
```
![df](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/bcfe397f-55ca-4491-9243-a6f63e35a4ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T46JXS3G%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T222529Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIEZHsoAQrLyqtdyD5NWxkZClvYedW23wA5e0N2EZdNpJAiEAx5D80iK%2FidYvloHEyyBvNLxKuybjw9qfdFvoW0g7mdcq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDHR%2FZ3111ZZ%2FFltiZyrcA8lQUHMZRacgrtgRE2LCw9hVpeoQV2UcWgm8VYYa%2FzzLFthLS8TJKSeAISCP2qwc30PT4GQEAqcmosMi08w8DwVPeHzWAbIyWfxgmgRfr2%2FIKFBhCGz6t0G7O%2FRmNvvT%2B3ogZghNpzrTk%2BTHa9DnB7lqKNCqNVcEUcHTBHOHocbTZ4N8WB7yhqzA%2F4UVqB0%2F9rwad7bROQ0pJ66aKCjbQEvep3jND33kQ1UD%2B%2FAbLqrWGgtjO0kK4OG6Y9wQuQHhLUooH3X7V%2FNU8wLK6lsEoQBOSUhSULyFr%2FdAWtP4Oy5B%2FavDjmjqB77ayZSjsokS9%2BGU0uZAd93%2B4xO9bT99JMyJgt%2B0o1zTkXuiYX0IZWu%2FSncT1G0OZSHLnFARgxWFy3ZWP8O8H9vjoFkChttsjRK4yzzMxlsFtun1vdFF8G3f4wYor1vdsqIOLsrPKkTBTZLJTi7yM7k2%2BBDR%2BkkKT6caPRXdaCR91ZnWV73FqvxufuXn%2FqgjmUasQ6GiitbwEBUwQAJ%2BRpPmqBQdfhobFvARvzGa6rkA7Pxb9YnERicr2sQ1p4JYK9VWWgtv0Fbje87ZOzLrjThnJi%2F3Ck8yTUo10stYauRWrYLBI2guHy30E9sDU2Gqr5wD5OfBMMLO98kGOqUBf%2F3I3Yz5mAhjdVH0obtE2KA%2B9kBcy%2BYaIt5macpwdZWPthZ65uQjqfKtmv5QKw0oV6cOSgf%2FPhbkHrp7WrvB0LtoQHAZrnqqfbMG8rqH4hqm6JpUNnMyK%2BAXGlRZk%2B3YDaCFeurI67ZpIAE%2BM98a5LD4zc%2FOHHFPtgqR7B8DOubcCR8H6uKWwy9qk6BR1JxPr3jV%2Fvr8%2F72z%2FGja62snCrQwBhMw&X-Amz-Signature=9a9dd3ff9d3f8a64988e8b79f18785e96659c6a6318438ec5610b3329dff3d2c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
Now if we look at column `bmi` we see that it contains float-like values, however, if we look at the code snippet we see that these values were inserted as strings. 
To convert the values in column `bmi` to data type `float` we can use the `.astype() `function.
```python
df['bmi'] = df['bmi'].astype(float)
```
We can check if the update was successful using the `.dtype` attribute.
```python
df['bmi'].dtype

dtype('float64')
```
---
**Modify data type for all columns in DataFrame**
Now we have already converted one column to the correct datatype, but what about the other columns, calories and duration? It seems that these columns contain integer-like values, however, when creating the DataFrame we passed the values as strings.
We can convert the values in multiple columns to different data types by passing a dictionary into the `.astype()` function. Thereby, the keys of the dictionaries represent the column names and the associated values the target / new data types.
```python
new_dtypes = {
    'calories' : int,
    'duration' : int,
    'bmi' : float
}

df = df.astype(new_dtypes)
```
Let’s check if the conversion worked.
```python
df['calories'].dtype
dtype('int64') # ok

df['duration'].dtype
dtype('int64') # ok

df['duration'].dtype
dtype('float64') # ok
```
---
## [`.get_dummies()`](https://pandas.pydata.org/docs/reference/api/pandas.get_dummies.html)
---
**Syntax**
This function allows us to create dummy variables from categorical data.
`pd.get_dummies( << categorical data >> )`
A dummy variable is a variable that can either take on value `1` or `0` and tells us if a specific observation belongs to a category (`1`) or not (`0`).
---
**Create dummy variables from simple array**
Let’s assume we have a simple numpy array that contains the school grades of six students.
```python
school_grades = np.array(['Good', 'Bad', 'Pass', 'Very good', 'Very good', 'Pass'])
```
Before we ask ourselves how to create dummy variables out of this array we must raise the question whether [this data is categorical or not](/8abd5dae91fc4e90b63453e6d4a80952)? We can clearly divide the data into different categories (Good, Bad, Pass etc.) thus this condition is fulfilled.
Now to create dummy variables we can simply use `.get_dummies()`.
```python
pd.get_dummies(school_grades)
```
![DataFrame containing dummy variables](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/4055b8ed-a655-4789-8cb6-7c93435f4317/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UQ522ZYB%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T222530Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJGMEQCIBDtF60qI0VzMg2X0n5quhEarMy0JCEPe2WL90SedpE%2BAiBwcIBFDQwJAuHGctWtWezv4vVNrn8bWX1f2KmLaEIcpir%2FAwgnEAAaDDYzNzQyMzE4MzgwNSIMAneDi7Zn7DbL2eG1KtwDfuR4Rbx9GgGbdjE3lS0JU2B9l%2BwumBh1TCRib61oA%2BHfHboKJMBx5Nlf9FfMtOvYBX5oilxgiacQKG%2FjBKuFmoAfC%2FzbEe6Y%2FsnXQhpWcB0o7Qmi%2FAC0hJ6BImtwL5UxEa8NZQA%2FwuMKDmlHdmcO3AW7A%2B5vjaWzz7w4DB3%2FwfhNkspNhYWX0BMXCX7LZn%2FtJqL8TpaYZHQLTj6GKdgq9mZRss2QTQcQbCRYtZklBswW1G91QQ3GViFn7GAJOB8YILUU1Q5HbUgqCd2Au1T%2Fecgo8zTBKdjrvkY9UEFmF4e6nyVoT%2FZYW1V4bZhvDlLpHGzJB4tndPAIsUXN8m49%2F8IsdntRdv7zufKQk2PkGBDYhbuqj6xZ%2F9%2BBbjd9qludjnotv7xkv4NckTFOkndaGF1w%2F5qp5fyFpEUEH%2FjSkOegpuCXEm4%2Bbk3zQZAuIr3vKPDmVg7kaBcABrrwfEDRTBam5jvg8gUDApTaF%2BfA%2BxJIZkPlEV0vCTR9mZwK5BMpmMn9L%2F4eth%2FO%2BS1Jg%2B3LBQ2F0BRs12VDZjT57gX2CE6RfRTpZVamF%2FnX%2BG7jXALzqTL0Ma0jVbSvtxEvTTeCnJmUu3v2z0ujkuse3rYKF3O3hB8eq9XM%2FO2sSlIwjc73yQY6pgE4cjpChkPvcHNfuU85DY6U1CbT3sn%2B4kFDndzfLMirLAGMdn2DI9TvIkSM5w%2B0ZFypCh%2BdOr3mpMqnWDnc8Oef1fBT2eQcsg0Df7uSyl%2FE%2BC2j91A2JWLGxt2BgwN6eVncBz3m%2F3HCPHhSMq2x0RSjhAygiHdKejyaBDOiLNeZv05tsa6GKz6VNUrAfiLh6tduuK0oMcvkwy0WcXFSnoK9Xb%2FTJoIK&X-Amz-Signature=f81381a19fc273bb640459e6bb3f548e2f8e189e81733b06fb5c46adca844199&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
If we have a look at the output DataFrame we see now that there are 6 rows in total (from index 0 to 5) which corresponds to the number of grades in `school_grades`. For each school grade we can read from the DataFrame to which category it belongs to.
- First grade → row 0 → `1` in column `Good` → corresponds to `school_grades[0]`
- Second grade → row 1 → `1` in column `Bad` → corresponds to `school_grades[1]`
- …
- Sixth grade → row 5 → `1` in column `Pass` → corresponds to `school_grades[5]`
---
**Create dummy variables from data in DataFrame**
We can also create a dummy variables DataFrame for the values in a column of a DataFrame. Let’s assume we want to create dummy variables for column `Team` in `players_df`.
```python
pd.get_dummies(players_df['Team']).head(10)
```
![DataFrame containing dummy variables for column `Team` of the first 10 players](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/49b381e1-2960-4843-a225-f757446bd0ef/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UQ522ZYB%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T222530Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJGMEQCIBDtF60qI0VzMg2X0n5quhEarMy0JCEPe2WL90SedpE%2BAiBwcIBFDQwJAuHGctWtWezv4vVNrn8bWX1f2KmLaEIcpir%2FAwgnEAAaDDYzNzQyMzE4MzgwNSIMAneDi7Zn7DbL2eG1KtwDfuR4Rbx9GgGbdjE3lS0JU2B9l%2BwumBh1TCRib61oA%2BHfHboKJMBx5Nlf9FfMtOvYBX5oilxgiacQKG%2FjBKuFmoAfC%2FzbEe6Y%2FsnXQhpWcB0o7Qmi%2FAC0hJ6BImtwL5UxEa8NZQA%2FwuMKDmlHdmcO3AW7A%2B5vjaWzz7w4DB3%2FwfhNkspNhYWX0BMXCX7LZn%2FtJqL8TpaYZHQLTj6GKdgq9mZRss2QTQcQbCRYtZklBswW1G91QQ3GViFn7GAJOB8YILUU1Q5HbUgqCd2Au1T%2Fecgo8zTBKdjrvkY9UEFmF4e6nyVoT%2FZYW1V4bZhvDlLpHGzJB4tndPAIsUXN8m49%2F8IsdntRdv7zufKQk2PkGBDYhbuqj6xZ%2F9%2BBbjd9qludjnotv7xkv4NckTFOkndaGF1w%2F5qp5fyFpEUEH%2FjSkOegpuCXEm4%2Bbk3zQZAuIr3vKPDmVg7kaBcABrrwfEDRTBam5jvg8gUDApTaF%2BfA%2BxJIZkPlEV0vCTR9mZwK5BMpmMn9L%2F4eth%2FO%2BS1Jg%2B3LBQ2F0BRs12VDZjT57gX2CE6RfRTpZVamF%2FnX%2BG7jXALzqTL0Ma0jVbSvtxEvTTeCnJmUu3v2z0ujkuse3rYKF3O3hB8eq9XM%2FO2sSlIwjc73yQY6pgE4cjpChkPvcHNfuU85DY6U1CbT3sn%2B4kFDndzfLMirLAGMdn2DI9TvIkSM5w%2B0ZFypCh%2BdOr3mpMqnWDnc8Oef1fBT2eQcsg0Df7uSyl%2FE%2BC2j91A2JWLGxt2BgwN6eVncBz3m%2F3HCPHhSMq2x0RSjhAygiHdKejyaBDOiLNeZv05tsa6GKz6VNUrAfiLh6tduuK0oMcvkwy0WcXFSnoK9Xb%2FTJoIK&X-Amz-Signature=9344222fac4fdba99d86705d9093f40c3ee46a60a06dfacd7ca3b7cc49c96471&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
From the output DataFrame we can see that it has the same structure as in the example before. The team to which a player belongs to has a `1` standing in the column. For example, we see that the fifth player belongs to Liverpool and the 9th player to Manchester United.
---
## [`.value_counts()`](https://pandas.pydata.org/docs/reference/api/pandas.Series.value_counts.html), [`.to_frame()`](https://pandas.pydata.org/docs/reference/api/pandas.Series.to_frame.html) & rename columns
---
**Syntax ****`.value_counts()`**
With this function we can count the number of appearances of each unique value in a column of a DataFrame.
`df.value_counts(<< come column name >>)`
---
**Count players per team**
Let’s assume we want to count the number of players per Team in our DataFrame. We can achieve this by using the `.value_counts()` function.
```python
players_df.value_counts('Team')

########### OUTPUT ###########
Team
Arsenal                     30
West Ham United             30
Manchester United           29
Bournemouth                 28
Burnley                     28
Watford                     28
Tottenham Hotspur           28
Liverpool                   28
Newcastle United            28
Norwich City                28
Southampton                 27
Chelsea                     27
Crystal Palace              27
Aston Villa                 27
Manchester City             25
Sheffield United            25
Everton                     25
Leicester City              24
Brighton and Hove Albion    24
Wolverhampton Wanderers     24
dtype: int64
```
We see that the function gives us back the information how many times each unique value (each team) appears in column `Team`.
---
**Format output**
If we want to put this back into a nicely looking DataFrame we can simply run `.to_frame()` and and `.reset_index()`.
```python
teams_players_df = players_df.value_counts('Team').to_frame().reset_index()
teams_players_df.iloc[:10]
```
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/f5eaf646-d1bf-463b-a48d-2f1ddda1b071/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665F3NUSEQ%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T222533Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJGMEQCIGtFvw9qn8b8bYhL82c9%2F4FaD9L9iv4kFCkE2Pd%2F3GK%2BAiAJXI9Dp8e74MFYlyemVWnaQDUtBz5wKpePOSVnlvIsqSr%2FAwgnEAAaDDYzNzQyMzE4MzgwNSIMTiaWmLz8W2rLqX4HKtwD%2FCjNlhO6bA4J2bNcbiKyw3uaKlNBrsOyfhz5tDpJiBSgeQ5H4x5k%2FyZ0scDdiRQSMhaTxop0guXLXsvC%2Fwh8YwzLInn2dPTdNHt32nnsiYD%2FP3f%2FqWMOS2hjCT%2FTHRDTtriQAp4ymJvJm2oJDScISab9vy2ZZ31A8f%2BrYpdVultJ5IoO84BtRRdVipzsbsTK%2BJ4w7VZG55dDcTlfPqf6A8e8a71%2BE1%2FDSDN0jmvIrBh7VYJ2Hg5NUUi2aHDe4eTz%2BpJSvHkSzhl1YCM0oj%2BoQf6G3NACZPSgi9uQ0dAW%2FlEFhMR8%2FowGAfj87xxsH9P8gX0KejxCtzW88ba%2FmiY1qIoCEXi%2B9LPTR25wtb3qDxm9lk4bLGfMD1QvTIsjJ1xRQ7G%2BqzPyyyQv0nLpAXOXULTKeimujnGY07v3cAaQOZN9tIEWu61%2FFAKoKV3wMVq5KcA1AbF2V4jxPShbctS%2FXjZ8K5qJqwGOLGeHlwW0hlxYHXrsAtmYb%2BsLaNRTe%2ByOo5H2yQTAayzwVTWH92%2F147LAQLGPlJrkVMT9B4Cs6pWon9EEySSwioEb1AF8jXgzHV5DMnN66B52t24tf8O91OmOlk6vZbliUUtFACVilS3hd4%2Bzayp4fACt2vMwjM73yQY6pgGQn8wbRy7WsYaJa1TDdUDLs1HkCXu7b017Z7SW6kvQ0ZJ4qzjhAOBt4RPzvjf8shqYGB6BnEYRcdOKSVu3rxq%2FqUe0pM8z0DdlsVtwWMfWadB59sn%2FR3tA%2BqNIUtgLKoGqIDA3kMiq%2FfgVeswJewFRHXxtwxz4gLijG3QoQncslEjR1rdIjTiny3QOx4ZJZ3l%2FpDr29vWx7UWRM%2Fdf%2BWr0u6NME5ep&X-Amz-Signature=42da8bec9fe668acb3d4729de99d0262ab93fa83158f8782bf4e56b9a03bddf3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
---
**Rename columns**
We can see that we have now all the information inside a DataFrame. However, the name of the second column looks quite ugly, so let’s rename it.
```python
teams_players_df.columns = ['Team', 'Players in team']
teams_players_df.iloc[:10]
```
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/8881d1f9-9c56-43d5-9f7e-a79ae7fb4c3c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665F3NUSEQ%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T222533Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJGMEQCIGtFvw9qn8b8bYhL82c9%2F4FaD9L9iv4kFCkE2Pd%2F3GK%2BAiAJXI9Dp8e74MFYlyemVWnaQDUtBz5wKpePOSVnlvIsqSr%2FAwgnEAAaDDYzNzQyMzE4MzgwNSIMTiaWmLz8W2rLqX4HKtwD%2FCjNlhO6bA4J2bNcbiKyw3uaKlNBrsOyfhz5tDpJiBSgeQ5H4x5k%2FyZ0scDdiRQSMhaTxop0guXLXsvC%2Fwh8YwzLInn2dPTdNHt32nnsiYD%2FP3f%2FqWMOS2hjCT%2FTHRDTtriQAp4ymJvJm2oJDScISab9vy2ZZ31A8f%2BrYpdVultJ5IoO84BtRRdVipzsbsTK%2BJ4w7VZG55dDcTlfPqf6A8e8a71%2BE1%2FDSDN0jmvIrBh7VYJ2Hg5NUUi2aHDe4eTz%2BpJSvHkSzhl1YCM0oj%2BoQf6G3NACZPSgi9uQ0dAW%2FlEFhMR8%2FowGAfj87xxsH9P8gX0KejxCtzW88ba%2FmiY1qIoCEXi%2B9LPTR25wtb3qDxm9lk4bLGfMD1QvTIsjJ1xRQ7G%2BqzPyyyQv0nLpAXOXULTKeimujnGY07v3cAaQOZN9tIEWu61%2FFAKoKV3wMVq5KcA1AbF2V4jxPShbctS%2FXjZ8K5qJqwGOLGeHlwW0hlxYHXrsAtmYb%2BsLaNRTe%2ByOo5H2yQTAayzwVTWH92%2F147LAQLGPlJrkVMT9B4Cs6pWon9EEySSwioEb1AF8jXgzHV5DMnN66B52t24tf8O91OmOlk6vZbliUUtFACVilS3hd4%2Bzayp4fACt2vMwjM73yQY6pgGQn8wbRy7WsYaJa1TDdUDLs1HkCXu7b017Z7SW6kvQ0ZJ4qzjhAOBt4RPzvjf8shqYGB6BnEYRcdOKSVu3rxq%2FqUe0pM8z0DdlsVtwWMfWadB59sn%2FR3tA%2BqNIUtgLKoGqIDA3kMiq%2FfgVeswJewFRHXxtwxz4gLijG3QoQncslEjR1rdIjTiny3QOx4ZJZ3l%2FpDr29vWx7UWRM%2Fdf%2BWr0u6NME5ep&X-Amz-Signature=b006532db52d40a044bcb1ca1b2035391a4bc36e76fb0dc948a4845f4a7ce69a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
We see that the column has been renamed successfully. With `.columns` we can access the column names of the DataFrame and by assigning a list of strings to the `.columns` attribute we can update the column names.
---
**Count Goals / Assists combinations**
Let’s assume we want to count how many times each combination between Goals and Assists occurred. To do so, we can simply provide a list with the two column names as parameter.
```python
players_df.value_counts(['Goals', 'Assists'])

Goals  Assists
0      0          228
       1           35
1      0           31
       1           29
2      0           16
                 ... 
8      6            1
       7            1
9      2            1
4      13           1
23     5            1
Length: 86, dtype: int64
```
We see now that there are 228 players that scored 0 goals and provided 0 assists.
If we want to include the 10 most frequent combinations we can simply extend the code with the `.head()` method.
```python
players_df.value_counts(['Goals', 'Assists']).head(10)

Goals  Assists
0      0          228
       1           35
1      0           31
       1           29
2      0           16
0      2           14
2      2           14
1      2           10
2      1           10
3      1            8
dtype: int64
```
And again, if we want to bring the output into a nice format, we can use `.to_frame()` and rename the columns.
```python
goals_assists_df = players_df.value_counts(['Goals', 'Assists']).to_frame()
goals_assists_df.columns = ['# of players']
```
![goals_assists_df](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/3d4c5199-1890-4496-8ce1-bd0754874750/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665F3NUSEQ%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T222533Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJGMEQCIGtFvw9qn8b8bYhL82c9%2F4FaD9L9iv4kFCkE2Pd%2F3GK%2BAiAJXI9Dp8e74MFYlyemVWnaQDUtBz5wKpePOSVnlvIsqSr%2FAwgnEAAaDDYzNzQyMzE4MzgwNSIMTiaWmLz8W2rLqX4HKtwD%2FCjNlhO6bA4J2bNcbiKyw3uaKlNBrsOyfhz5tDpJiBSgeQ5H4x5k%2FyZ0scDdiRQSMhaTxop0guXLXsvC%2Fwh8YwzLInn2dPTdNHt32nnsiYD%2FP3f%2FqWMOS2hjCT%2FTHRDTtriQAp4ymJvJm2oJDScISab9vy2ZZ31A8f%2BrYpdVultJ5IoO84BtRRdVipzsbsTK%2BJ4w7VZG55dDcTlfPqf6A8e8a71%2BE1%2FDSDN0jmvIrBh7VYJ2Hg5NUUi2aHDe4eTz%2BpJSvHkSzhl1YCM0oj%2BoQf6G3NACZPSgi9uQ0dAW%2FlEFhMR8%2FowGAfj87xxsH9P8gX0KejxCtzW88ba%2FmiY1qIoCEXi%2B9LPTR25wtb3qDxm9lk4bLGfMD1QvTIsjJ1xRQ7G%2BqzPyyyQv0nLpAXOXULTKeimujnGY07v3cAaQOZN9tIEWu61%2FFAKoKV3wMVq5KcA1AbF2V4jxPShbctS%2FXjZ8K5qJqwGOLGeHlwW0hlxYHXrsAtmYb%2BsLaNRTe%2ByOo5H2yQTAayzwVTWH92%2F147LAQLGPlJrkVMT9B4Cs6pWon9EEySSwioEb1AF8jXgzHV5DMnN66B52t24tf8O91OmOlk6vZbliUUtFACVilS3hd4%2Bzayp4fACt2vMwjM73yQY6pgGQn8wbRy7WsYaJa1TDdUDLs1HkCXu7b017Z7SW6kvQ0ZJ4qzjhAOBt4RPzvjf8shqYGB6BnEYRcdOKSVu3rxq%2FqUe0pM8z0DdlsVtwWMfWadB59sn%2FR3tA%2BqNIUtgLKoGqIDA3kMiq%2FfgVeswJewFRHXxtwxz4gLijG3QoQncslEjR1rdIjTiny3QOx4ZJZ3l%2FpDr29vWx7UWRM%2Fdf%2BWr0u6NME5ep&X-Amz-Signature=f75813bbe714b01a2013bf073863aa07a837196d5f508dd66113b3a50f8a3715&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
---
## [`.groupby()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.groupby.html), [`.get_group()`](https://pandas.pydata.org/docs/reference/api/pandas.core.groupby.GroupBy.get_group.html)
---
**Syntax ****`.groupby()`**
This function allows us to group a dataset based on the values of a specific column so that we can later analyse a certain group in more detail.
`df.groupby( << column name based on which grouping should be done >>)`
---
**Group players per team**
Let’s assume we want to analyse each team in greater detail. Thus, we want to group the different Teams together, which we can achieve by using `.groupby()`
```python
teams_grouped = players_df.groupby('Team', as_index=False)
```
We can now retrieve a specific group by using `.get_group()` . Let’s say we want to have a closer look at Arsenal.
```python
teams_grouped.get_group('Arsenal')
```
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/17ab1dcf-24fc-485d-b844-14c2bd68e3ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W3QX3WYU%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T222534Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQCaAvVwvsh8lCY%2FOKTqyh9GLBs9rlkgVrirRiIaywhDiwIhANaJa1IE87vb8G6YNIzyyTXcmlwiuohSo%2Bgyt4vgnRDSKv8DCCcQABoMNjM3NDIzMTgzODA1IgxQyU9wlZZA1VonHHQq3AMFL93UaGqQ3vOc6957Mr7wUAIpMXNlNs2qana%2B%2FntTRFwXZWA2fSINAhN10T3ma%2F%2BjhUrzA3R6IS14NumgSPXPTKIJz8ZoWGhV89xH%2BDha24LACc%2BJJr6SSs9nFtgq9QbhZq9NsTebKTJGmo%2BSd4dcwGUXfLOayJptXmURxmCXOQEH7NGF9yUWDFz%2FCt31W0tqj05Vu4BeYZA0u2lfMYRKePhjYt3a8hQbghz5Unkan3YQ5bruVWiujRnFEKDWLxmHYIlaOkW1wSrnAkjGw4wQYJk356vn0Jx1ylZVJfEGO82BMaGyjVH7%2F9rCVPc%2FIC6BbQky9bjk%2B4tT9rd6afBGO4DIzyQaIlzc6Ynq3i3r%2F5dFkmAKiE8LH2jmjUmEDuJH5RdRJX%2FUL6gVTjB9R3045I8hlVT%2FScmCSgug%2Bu6JqF4MPK628XXjrZ6765RlvyKmHu%2BrI0bBCi0y34DA8JRwmn8kupBpmvL3O2vJemlc9fTtMvcY%2FRxvzzS3ZbdL9j09XGmXDuG4vs5%2BQcMqHUTvAoozYQxVTl9IOwvmHX9xvNHyk0WocIN6qUDuiLJS9SkxeXF9N%2BqpkOi7hfT2F6a12SXL9OUl08KPBgYkxgSGOMp0z%2FUY1vNxzz4AvzDXzvfJBjqkAcVhmcnW9JJaDvXKKpdPiwxng1cRhTvtKVnpqZq9ZH46xLjE1us0VXH%2FZathk8LPSz%2B2ucJT%2BMCxGfMjWqW%2F2ZUW7q2cavjEetiQfS1o6xqOPYjHOBJnjWmrNzlmXQD98mKQ%2FemWiB4m0cyI%2BtxyFOlbrnsOjnTp9B%2BZBSm0D%2FZ0BLNOG0iPot8dpZiSrLtJ2GsNcMmRPAP1i2vK3npQWmxsQNly&X-Amz-Signature=9a6258aed5b486acd9fc6f58dd92c8127e650e2d3a9fdf7e949c8c8e30e7cc29&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
As we can see we get an overview about all the players that play for Arsenal.
---
## [`.agg()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.agg.html)
---
**Syntax**
With this function we can aggregate records together and thus get more insights into our data.
```python
df.agg(
	{
		'column1' : 'agg-mode',
		'column2' : 'agg-mode',
		'column3' : 'agg-mode'
	}
)
```
As we can see from the syntax above, we can pass a dictionary to the `.agg()` function as parameter, which contains the column names as keys and the aggregation mode as value. Because Python must know in the end how the values should be aggregated, e.g., should the values be summed up or multiplied together?
---
**Aggregate numerical data**
Let’s assume we want to re-use the DataFrame `teams_grouped`, which grouped the players of a team together. Now we can aggregate this grouped DataFrame to see which team scored the most `Goals`, `Assists` and achieved the highest `Total points`.
```python
agg_data = teams_grouped.agg(
	        {
	            'Goals': 'sum', # -> we want to see which team scored the most goals
	            'Assists': 'sum', # -> we want to see which team has most assists
	            'Total points' : 'sum', # -> we want to see which team has most total points
	        }
	   )
```
![agg_data](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/8b40cc7f-98b7-42de-bb85-b931a1290e6d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RW6RFBLX%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T222537Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQCx0ailllrEgLhCd4DluzD%2B122M%2FwOLZcDXMYEqEAufwQIhANCtv%2BxncEkK%2BRBXdu%2FyklFgbRFbelp0Tj8VGQU6fn8wKv8DCCcQABoMNjM3NDIzMTgzODA1IgynvQTLvn4FWjnFrWMq3AMoNY0NdMJ70dU0Aaq%2BbaRPsYnveiqQpY9Dcr4W%2BUggIW3te4sjbFydFbGiiTloa9NfvHUvUXbac5pgdk0RMKESmFAx2n5zK72kMbuVhWs55vyX9hlX6UuccM6Kk48NhppFZqQMRpIocWypN%2BsADl5W2BP93LVu0vqoDuqHt67mKipa6zu9iRnXrYdA0sAwSsJz845oSDMdgO96ZY19VTwR7GDgaVqySLEZkxJT7XkMRbpKJP09O%2FLpbd2kfMASzqTa7y4m%2BgBegOKGsE12Bw4JoByIMBRVkyBQrX5a7vqUMzq0GHiJXs71XtLZLewY53ca5XoJ%2Bhnla52jrYiUByjlZDSnhjqusGeE4YTnCTNizCOi6z8ejL51341Z83zsBvDJiucO5P2f7iE%2B%2BeMCKmLyfAFqUJmcP3oKeFIA1kMlryyu5c9BxD4HWfbfa%2F6u2MjdYWBmGnq6jOW4TkCjttYGNFl8j5h8SOQiVWq9kBVpOMihuU1%2F8As6BFLHWIsLLyIibi2FSy9mMVVzn7BTeq59Pgjhw%2B0bk93wJ62Q%2B1WsucQAkU9qq0fk7Ldsj1aLnh%2FBfOHyB6%2BNavs%2BCDAGsjjxIsBh8K4Y%2FKGBmNC7KQHYmU6kDWGosU6UEy2gHjD8zffJBjqkAb2%2FYwu559L54S9%2FUclmQdndH87hD3M4uBO9rMt%2BP9KeB2o0Gwdgv%2Fe5fMllI5E4Cz6gyQo5xk%2B4%2BcKQFx4AYrsUUMzYVU3NPmVQKQMaMLGjBeJp%2F4BPr6T9e6wKxe7FrBhlw4mOkj4vp72kbPRVLIsFrKaA5m%2FW0qoPWcqxUtA5Knr2k84cLrqbCWGhk9X8KgxBvy8drFfTOgBF%2BsKAMsEi0JvE&X-Amz-Signature=ee5e2a4322452292a074f63baca09c9c039bf1178cf82b5f47efd0b3a2e02309&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
We can see that we have now an overview about `Goals`, `Assists` and `Total points` per team.
---
But we still don’t know within a few seconds which team was the most productive one in terms of total points. So let’s sort the aggregated DataFrame based on column `Total points`. 
```python
agg_data.sort_values('Total points', ascending=False)
```
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/e035d01e-ef72-4e95-8a61-58b2b61d4aa7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RW6RFBLX%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T222537Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQCx0ailllrEgLhCd4DluzD%2B122M%2FwOLZcDXMYEqEAufwQIhANCtv%2BxncEkK%2BRBXdu%2FyklFgbRFbelp0Tj8VGQU6fn8wKv8DCCcQABoMNjM3NDIzMTgzODA1IgynvQTLvn4FWjnFrWMq3AMoNY0NdMJ70dU0Aaq%2BbaRPsYnveiqQpY9Dcr4W%2BUggIW3te4sjbFydFbGiiTloa9NfvHUvUXbac5pgdk0RMKESmFAx2n5zK72kMbuVhWs55vyX9hlX6UuccM6Kk48NhppFZqQMRpIocWypN%2BsADl5W2BP93LVu0vqoDuqHt67mKipa6zu9iRnXrYdA0sAwSsJz845oSDMdgO96ZY19VTwR7GDgaVqySLEZkxJT7XkMRbpKJP09O%2FLpbd2kfMASzqTa7y4m%2BgBegOKGsE12Bw4JoByIMBRVkyBQrX5a7vqUMzq0GHiJXs71XtLZLewY53ca5XoJ%2Bhnla52jrYiUByjlZDSnhjqusGeE4YTnCTNizCOi6z8ejL51341Z83zsBvDJiucO5P2f7iE%2B%2BeMCKmLyfAFqUJmcP3oKeFIA1kMlryyu5c9BxD4HWfbfa%2F6u2MjdYWBmGnq6jOW4TkCjttYGNFl8j5h8SOQiVWq9kBVpOMihuU1%2F8As6BFLHWIsLLyIibi2FSy9mMVVzn7BTeq59Pgjhw%2B0bk93wJ62Q%2B1WsucQAkU9qq0fk7Ldsj1aLnh%2FBfOHyB6%2BNavs%2BCDAGsjjxIsBh8K4Y%2FKGBmNC7KQHYmU6kDWGosU6UEy2gHjD8zffJBjqkAb2%2FYwu559L54S9%2FUclmQdndH87hD3M4uBO9rMt%2BP9KeB2o0Gwdgv%2Fe5fMllI5E4Cz6gyQo5xk%2B4%2BcKQFx4AYrsUUMzYVU3NPmVQKQMaMLGjBeJp%2F4BPr6T9e6wKxe7FrBhlw4mOkj4vp72kbPRVLIsFrKaA5m%2FW0qoPWcqxUtA5Knr2k84cLrqbCWGhk9X8KgxBvy8drFfTOgBF%2BsKAMsEi0JvE&X-Amz-Signature=ffd86803e33a7c1f90ee36025b52fae3e004672f12b4200a2f4c0da85cbc36ae&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
We see now that Manchester City was the most productive team with 169 points.
---
## [`.merge()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.merge.html)
---
**Syntax**
With this function we can merge two DataFrames together into a single one. If you are familiar with SQL, `.merge()` is Panda’s equivalent to SQL Joins.
`pd.merge(<< Left DataFrame >>, << Right DataFrame >>, << mode >>, << left key-column >>, << right key-column >>)`
For the `<< mode >>` parameter we have four different options / types of merge we can do:
`'inner'`
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/5408a8e0-787f-4825-a1d7-569d613696af/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664I7QZFKT%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T222539Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIQDA%2BTH%2FbQb0Hq1AWaj9UT0IgGtXxGt6YljybzHKhCa4JAIgHuQ6S5Ff1itEo45EhBwQ4uL6VyJDMCwEi0UUH9fHK8Uq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDKuNxMiubijIzS%2FkvyrcAz5cPMuEDJTE97Wo662g6PnkMVr5p1I47qPOarmYYF%2FGNPWjZtOtdd2eaMcRjXYJTgEfdC0%2FmxV1nC51ea8isfcrQf%2BLGJ8pE2WjI7QrIcqAS%2FI%2BgWhIdG0ZTIfr0XBLWuG7J3pBTkFwT4WN9av6uwEENUhGYz94eWH5SlORD6xZDrEHeQYvKAmr3HlTSdwbDlsUG6oUomYMMgGqp0kxTYxwxfXm26S7H8lPnlJOnwu2Ix4fVaAOmz10IHZ7E6nY9QYq4%2Fn5JkjOKjllGdgzS6FXwTdRWVm58Tx%2BcoK14fvoHsshx0PU%2BqHA2n85j4fbKnw3%2FHIrQVmudAyH8MfEo7TqQQywAhDU9duPbd7jGve0jIpzLhxhsp93p57EjlyVZesMKSAtUIoPYNXSQ10Ceo4BGjcutkqqNF4kCL5lYm5nsQ3KpCz6YiyuMXcJ5Bynseen9o4k43iCuvtNKQ7h5o0CeAj7G8N9jlOsf%2F%2FXzd4dsuIxFXd6WnS9MKSqUavV1BMVzPo8c05BlXQMe7ryMkiPQYlgi0ARBGuXi8mH5yTyNtqwU0ee2eS%2BoWrOJ3UlDPLiIt7dS8HpZvPNp7RdoAMEd3IF5l%2BnWnuiWyEBJeTVY7DAUh4KUegvE5kCMPjN98kGOqUBKKndQk%2BHeBcAAy%2FlkB1N%2BVR94qu%2FojWwfNeX28biMfCV9plbgu7XMAlJPHCX7scnyQW6C7GbmoaF6o%2BiF7gG2xiIunQ1RpqFLWTb6F9fN3ji2N%2Fn7A0mz%2BBqMK97ky%2Fsy57aQHptWS5iTrTOyJ7YiC97l3Ciw0yWjc3OFTR1BcbGXumvKIopD7kSYQE20LylIuSjbVTREXVfnyS%2Fs8kQ0MCryvV6&X-Amz-Signature=4bae0610bf8a261a9483eb62bf648e5f726c25a652e5c46aa6041716aced77a5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
`'left'`
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/09e2253a-b6d9-411d-836b-faa79515429b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UEGNE5YG%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T222539Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJGMEQCIDI8FV2zDrVubvQKcsx6MKA16FPvcVSTF5PtKUEuCpGkAiA3u%2B2N%2BfFi5B1ba4Vysigcdl4rj9ZAhINDv4cMn2Bofyr%2FAwgnEAAaDDYzNzQyMzE4MzgwNSIMjHQgZcbSEzDOmFJXKtwDgBn56YHJD7y0iCMxwiq99R7LSWxVY2EilszFiLLrmkzVIsR5x8yhxhOidxdqhYaM0D4zQ5YXhWH9iP8Krw%2BC6vXp2hpktyiN%2BUTEg6akHtyNqc%2FYma59fMw0ZV%2Bn0D77bLA0QlwcUJjyZsFELDqbIP6wbupbtb5BJXBhjhB9JqLJyc0nt6c%2F4YTZxFmtcAFCjryeUQyVlsl07An0HZNvbiAOnDn3HtMtB5X%2F%2BXcmcf%2F4zlvQ34YhaIaIPvEFg721zKinBSJxugAkLEZvGaKAL5m7r%2FCwEObNHWvjaQhehwIgnf9%2Ffec6W73oZ5yr5cHubwcNI2diLXpNaD0FQDTylrf7Wail1%2FZQmfl5lSTA5D72AFrHLqz3MUd7DTpHrT0IieRJ2u7wQ1YYyvY9rVsVKBaKh7EYNa3vTOHu3OlFQWK4CddYKk7Iiv%2FSaFNOjbtLCx3aasrCN17nWAP1h7J3Y3x2nLtWkQ9Lwbrsb4XWW50cCSGnrdbA4qzKlFop0Qd1Q%2FQBWrowoVexHdJmQcAUQjs4V%2FjS%2BAXzo31RD1mQq42NaGLKRRBCK2cWtgPl39AIhe2Tm%2BMi%2FceOaiv%2FPbW0uWek5sHdFIOoSdGXyZ7nyRGSFniohi82YNBhZn4w8c33yQY6pgGmQN33OAuAxZ2%2BnxFXa7wpbIysLSMi7wy1iT1rvgPG9zFRPG8vvN6A8amljTyBmTlnJRjypchSsXXAzHnnZVpXKZQHeyPfNh4c5vzTSetYdho%2Fy7ksPiGyQ5LHZGw69q5aeNll2oaS3L65wtduKHLClAUN6u9GI9O9ZtJciTBTtL8bXZc%2FNy7alFujVauRek4AzJdLexvpygL7%2Fue7zR6S3psLFTFb&X-Amz-Signature=7fe61dd6f20bc125088b6dac34e7f72a780c44204d64594889d122417cf08062&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
`'right'`
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/15e33ac0-53d8-4e72-867c-7d17c8d7a3e2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46623WCJI6H%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T222539Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJGMEQCIESqY83FfC4yq34dm4gJ1BrmtElUlO39oMQEsWA6wVgPAiBre3zAjP%2BILpy9qx%2Fdvm5ORZKuWrD6QL2z6K8tm3xlPCr%2FAwgmEAAaDDYzNzQyMzE4MzgwNSIMtHVyyK4UbnzBSbgrKtwDJPMzNV%2F3r8MvuLeuKrT7CbNuuj4CPwcmY5s1ciKUTvfZPnla29kxsRTLVZuBVwvltAuMrdrTTcFl10u%2Fvka5VUArBsrD6eZItMQvWNJg9pkO28OgSAYmsxf3ZW3GvM4Gl%2B3%2BlhQDglWan%2FLeKTkAxd5V2JcbFv%2F19Ek6N0LpaW2BYYd9nZLxUvde1TVHpS%2ByV%2BUJhnAtjGeVmiPNKycjVRAfwcI5sUwa1ssKKBAjVazZOnziGxPeGW548UXFnEafWctUzzweRARp%2BMymJ9JoYAMxcICTtoTA47TAfDEBA8%2FpED5SUqgl%2BqtcCEXijcSa86Snyv%2FaTv14KyA%2BT2Jyzg9vVcgSzJ3l0oocw4VYLGH5gb9IPPTNTedRBEXqt%2F79oOiYUN325de%2F1YiWptha12dSiVgVWo%2FUMe5%2B8gMU1sKBO5eWQw8ir2VQO%2BAqQR7mnqCKrLX8Hfuq8okQRkwga1takmhJgF8uiBE3xTRJycFQ1jKrTilJ5hhxdAa2yjeDNyTBQoHCi90AS%2B2yi%2FFL3WWaNI6nSY0SBsE8N1VteQDCV96h%2BkIdVJmrYeb0FW0hdfRYIgIkkFAvq3E70mAfSoVraVvMGvU2GIkBapzUK4fO7%2FGACOb%2BJ%2Fi5xc4w36b3yQY6pgF1xiIsMnnAODfx%2B1ycFoeGrTvwOVdf2ENyLzmEc18jQuGkF%2FstfPHWmPxYVyPyseXonT7eHTtOaRVF6uWCj37nJwBndtEjzxNBBp%2FiSqKuB3AXGB748QWCNKyS5yv7z%2BWnYNABQYvBNCM9o4wlsHfEBY5hGan5MLny0KeVJZLv2Peaz4lNbiFis4lJnCJkk1pJ6HkynLsbYRk8XMATJDO6vJeLthO2&X-Amz-Signature=5e0a1a27f9269876c7ede6870f13fb860b72dd13a1f845b13051ff0587178b24&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
`'outer'`
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/806d7472-621f-489c-b76f-7cfde93b8afc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X2AGKUBW%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T222540Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIDbF7jywalfACODmo%2FqMIltNNXI23EUY6jRuwMEtrEiWAiEAhFIBNjaZG9r6Y4p%2BgMhf9QFZnlakbg4DDIUfb1yC3F8q%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDAVex1MTK56zz2IobircA0j%2FpU15yuz1vdz%2BOrjrt57CiTkiPeX6yh0RGQ818wotgC5ps%2FgYsspQGf%2BMMyAnr5AqqYZ9Zk1jnrMlvmKclQiVHfyjKit7CGdF6GkvyGxUkK2COuzMTGyCn%2F%2FL4cIj8MNFP9AKJpt4Rp%2FxGhsBLhm3XBwSCSVVKr%2B2aZi7VM3OxoaM67gCYaH2SMGNxO2dX%2BomlucIHYItKuXy0KvHLeYJXN46%2FJZurxYxtz2%2BRL%2BeB4fU%2FBfGQBvGt1bt9bFnZO31zk4fuabaQPLj%2FJWPFwq0BpCxUfaruvIpC4yxv37Mp3%2BGAeB0%2FQf8sWKZliJu05RsbaZbGrTVSiAH7YANFyU8Urzgt2iH1N%2Fk4ATSSr7ZuhMI1jZCGTxzsX3uRFgWZZn9zCBtrpTUiMl42%2Br46C5kOqVr04oMcFwITYwLzWHBueh%2BLKgX3Of5YrNUZhOldsuNBpVEdhKKX6pw1ExZriDi30yeXLiPLQYvH5YzG%2Fwg0HQQC4%2Bf4V%2BW1lAL7dHoF3uvrMvq24g1py%2F36oklnYQZraHvZbGMgpH%2FEkixklYB3qWtk35HZD3PE2ssuZp0m7Y5qHDU43L%2BB3%2FxUAjCHS1e7m80AQdvoAIHKbaVEHIizUgSAT5TJ8CFbZPkMMDO98kGOqUB5l%2BK%2BxdE1vpH%2FE%2FlbEpbEkLLYzuRZ2DM54kHogmfZkzY7Rf0fEBVhspBkCTiUIXTUpzeQbi4dMu25tlRIvlZAGn610krRPizUDO65IQ4%2BFBJC7YPwz8Srue%2BgE6Ldaun8RUI5ExR7ANLvy6CoWg%2FOYExPb9fMi3MCFy5XhY9pRWihqeYThCy4FbbQYTltF3mIMHSfkTMuZkl6Dp1m7u3pLrXQjI4&X-Amz-Signature=bafb3cedc7658746fbd908de1139612cdcec38ea9c4a0fe468cff78fc95f5560&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
We will cover each of the four merge types in examples below.
---
**Simple merge**
Let’s assume we have two DataFrames:
`teams_players_df`
Tells us how many players each team has whose total points are higher than the median value.
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/717dc77f-d8a4-4bcc-8e02-f6ad22ea7515/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VEW5TWXK%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T222544Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQCykZuV5%2FNp2w02dYtp%2FVIOCEmkEllS5vWFKAcudxu%2FKAIhAMxQC4TKOTJH7E2bWfLbrjsUh%2BEMUCmXdG04B9JMLDz8Kv8DCCgQABoMNjM3NDIzMTgzODA1Igwx7U2eNivImjlg5ukq3ANNcoQ9dqLHImYeb01U7sMY4Ij7o1HUU56QJHYo3R9fk3SiB%2F%2FUBmmdQVprU15rSkh4s22u8wcx1GcgQqpo31DSq3LBMX8hRpOtFyCJsfOD%2BvwFl%2BCyxj%2F8Kul2cZGRTAZj4BIgBSL7c5rOfE4oqnmq9OrTJ6eD%2FaXu%2BXp2t1KvqpYAioLWVvc7uiffUZtiz86Qz85PGkZipQBojXjGmoyRvG%2FLYCi2xSeqgZGh9Q1o06WU1UQT9CE4c%2BK2tutBgnqYq4goKetM1XXwJDuKRp3nNH4x5ByR95F1yW8RefhPADJhc3IRw6Xd6QuUu3xYrc8Cx0%2FlyzgnBoAfnJfX9GBUPEFFD2J8SzZXDemAHkoB%2FmVWcb7%2B8Nc5AW4T%2F2kMdQdnzse7lo%2B6mqT%2FW%2Bwul23aJJO1AcVy1l8NBt%2BjY7KJ%2BeUskjuSh6oyohP392WB8DLKm1hhWlSEARiwFvikAM6ux35XV%2FzXbimkAsCTD28NzyMSVgxLPMzblnNpRMH1swRfGyIn86CY5WvC9FsUkv%2FNK4kSStHeivhrd3HsPvJdpsv2bYmDrUA9URObNzh0j4fyqAD5z59%2F9og55G6W6JpCMl3PxFJ4kFUrYoMYGps0t3jrzpHYcGrzwvnmJDC%2BzvfJBjqkAdj0IWW1MoTHkolLMhPciZQUzVba7eA4PtEKWMdofP16u973UACk3WBTgKVyPN4tBEIRRMnb5Qx8%2B41iPzeUFBnOdjBNG7lB%2FiEg%2FPvyOHJobkT5B8D1cKKeEz0behrCgx%2BkEI67TT9b9nOFrwidUkb1ZxY%2BOS88CZ1mFkrWZcN2jTqD9hdDonmFbC%2F%2FQAGHpDkdcYJ%2BQvpOIcvhUbDb9nTPK4ni&X-Amz-Signature=dea7bc5f4f94c0f41216cb5ee53d8a5691135e0d7fb52dc2f71e947d29dd9305&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
`teams_goals_df`
Tells us how many goals each team scored in total
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/8aeb3499-93e4-4e75-93bd-8cfbfb15ef89/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667VJJNGJ6%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T222551Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQCRbqSBEyCtzXzP%2BExgM5qIhvtCgTbAJ7J6x0rSSHmePAIhAI2xAZn4so95%2BxOe1GOwYEU1rb8s4Xa9IrxYh7yf2DKXKv8DCCcQABoMNjM3NDIzMTgzODA1IgwFiJP4WgyZDpm5lOAq3AM4%2BfDZUX5U7cpNH%2B8zYm8y4XHArtGs3spWDfO1OfRb9D9gj%2FiMXlsHCivyskfH2yf8k3E7R%2Fa5c2xX33bXsnnfN9lS5mZJjst%2F4XsA9kYNDdA6ebpV0g0U8aWJq26UJwvAooPHtZV60%2BwHcOpsvHRzlCJiGs%2Fjpd6ufaV7h6I5cGqKuuXlLxXoD29IYXfsvvYcTV1E%2BUKetDcLh5QlcRZ06rCB%2BKV9uifhMs6BXw4RPXzMlqO%2FzES6qWwKgJbZbc6vmOoQkFaAinBOLrGAXuRcGpYKCmi7ae98t9GmovUfeT8EID1zcxY5F%2BegKHN%2FP%2Bxyiog6Isb9HzWuXXc1RQ37bYMXfbfwjnMmU44agTkREWjzVeycvAyQd%2BMKX7%2Bgpk1CI%2B8j6KL8av3BDdq%2B9okDhU3MkBcxIUC2Hg8%2BHBf6wLlc3tmq%2BGbJo2d4moXCAj5U3oeYvdmaK7CnbLoWbr1NfPx0KLgwRcRXMjN3UmYiFFJmfKdzUwYfesBvRCszSvhOKtfbjSPyu8yo8eKLnVe1pBBcgVDysN1YRJGrZQC%2BWcxA5wUPp6hJLlo%2FfMDbHyssJgnNgpCZxn%2Bv%2FAQlqKaSBhGVyIFNpb2K7eEajExXc%2BN%2Fe3DjNd9lhfP%2FkjCDzvfJBjqkAZRzHZyUxWMpNfhut%2FaPxW4e5TUp%2FsApWOF7tAfyZbd%2FkDn1bpxRoKF4ztOb9BvZPdFLZzPVs3F6To067u3qbSw3r6XlseSFQ7iP7Kmyg2gKRnDn34EKnNkKNhtU7k4j9EMrtI2W4wqsL9%2FDYUfVmmWXqGav15oEslq42IR9C9AKxlS45oo7Hbeb5l2cW%2FZS7Uec24h6T6rOz%2ByzEiOvYGizDTO6&X-Amz-Signature=d3116cbd6e9f4bb71985d20685837fdf72becc05c9ff96e8ba97ec50fc6db4e0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
Now our goal is to merge these two DataFrames together into one single DataFrame. To do so, we must check if they have a something in common. We see that both DataFrames have a column `Team`, a so-called **key-column**. 
Thus, Python can use this key-column to connect the DataFrames together. Because if we want to get rid of the `teams_goals_df` DataFrame, Python must know where it should put the values in column `Total team goals` and Python does that by mapping the values in the key-columns.
We can now execute the merge command as follow:
```python
team_stats_df = pd.merge(teams_players_df, teams_goals_df, 'inner', left_index = True, right_index = True)
```
We got a new DataFrame called `team_stats_df`. As you can see the two DataFrames are now combined.
![team_stats_df](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/f966153d-f56f-4c61-a446-0ab9b688a507/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667SPW7UAC%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T222537Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIB9ZlUzC4v%2BqcuZZTRSFmmkC3yQkILI4y5Gb6za8g371AiEA2yLEY3N5%2FEAAn3hahBFj3crV5u0BD6uRIi9rJBD9WSwq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDBKRvFYFBLhVspqynircAyAj9Gy5LA5QNE%2FYPI9JiisD2HRFlkReHbp40eR1GJPJDX7EBWIiJaKWncPyRiqiwWYexx%2BvrPnVV10%2B1deVx4VtB9CD581NOvfzw63CJU3BQFCruA5PO%2Fk6U9%2B9kgK82hXjN5aZRQWTMi7SMvpFkFnAzDHlgH30H5MTFTTt66iO8AdQcLEuxQDhhCG5u5ORaSjWZ5NKGOuNbALQUMIpUTFQ1O84IBhQkVYRBMCykPqKPOXTG%2BpGMv%2BNcBsKiluTtm1VKzComVKyr3vQgYOiWHhXg%2F1e8nFtk6iq7%2FZkxqxp0xCb9hTNA5DCidqtisI3uguUKRNZSU8a96QlNcMj0V9bXY88wZpO8LjMOJie73WypTr6SLeolchCveqW%2FWnfOJR1pkDpeMCHMs8y29uFSaZmh1fRIQwUht%2B385M%2F27i0jdwlo7oCA9YsTXiuykdp%2B5VUA1JaTdTeMysn9ku%2BM8poruAwL1T21TDQ70EKZ1qG6TynM2e6iOF3zcK%2FXmoWDj3BoFmF1nEOEib1H1os0%2BiaED532iF6FuaLdwzi4V%2F9hP7C9V2myMifSP0GzVTZuTGDuI%2F%2B7GdGTzh%2F2XXndY8vk8olvCGBLwJGJ%2BLMKbVUgZM3U3mT2resJO%2FRMODN98kGOqUBtJLS70bnlniw%2B6jZia7GCEAuWC6xG83YCm3snbL8WcgWe14bTGWGOV60r3748lcHGUWXslS4JuACC3EH2NGfMGAxoutXQFduSQ2y42UR9A3df5lsQEGUWub7VuyTxbxH9f%2Bt9Kt2YtEBRHyjzWVPDixTJc2z2EMaynMzU5mFXXu9oL5o090XZ1oVOXxYVNJuVf7n4yKzd2zrWeoFl0jOwM5KCgtD&X-Amz-Signature=117377410ddbb917d00b24c6e0d5922f116765ba57d4ca3dbc7b9379e7cb65d7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
As each value in column `Team` is found in both DataFrames, `teams_players_df` and `teams_goals_df`, i.e., both DataFrames contain exactly the same football teams, it does not matter whether we do an `inner`, `outer`, `left` or `right` merge. 
More precisely, we can also do an `outer` merge and get the same result. 
```python
team_stats_df = pd.merge(teams_players_df, teams_goals_df, 'outer', left_on = 'Team', right_on = 'Team')
```
![team_stats_df](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/f966153d-f56f-4c61-a446-0ab9b688a507/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667SPW7UAC%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T222537Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIB9ZlUzC4v%2BqcuZZTRSFmmkC3yQkILI4y5Gb6za8g371AiEA2yLEY3N5%2FEAAn3hahBFj3crV5u0BD6uRIi9rJBD9WSwq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDBKRvFYFBLhVspqynircAyAj9Gy5LA5QNE%2FYPI9JiisD2HRFlkReHbp40eR1GJPJDX7EBWIiJaKWncPyRiqiwWYexx%2BvrPnVV10%2B1deVx4VtB9CD581NOvfzw63CJU3BQFCruA5PO%2Fk6U9%2B9kgK82hXjN5aZRQWTMi7SMvpFkFnAzDHlgH30H5MTFTTt66iO8AdQcLEuxQDhhCG5u5ORaSjWZ5NKGOuNbALQUMIpUTFQ1O84IBhQkVYRBMCykPqKPOXTG%2BpGMv%2BNcBsKiluTtm1VKzComVKyr3vQgYOiWHhXg%2F1e8nFtk6iq7%2FZkxqxp0xCb9hTNA5DCidqtisI3uguUKRNZSU8a96QlNcMj0V9bXY88wZpO8LjMOJie73WypTr6SLeolchCveqW%2FWnfOJR1pkDpeMCHMs8y29uFSaZmh1fRIQwUht%2B385M%2F27i0jdwlo7oCA9YsTXiuykdp%2B5VUA1JaTdTeMysn9ku%2BM8poruAwL1T21TDQ70EKZ1qG6TynM2e6iOF3zcK%2FXmoWDj3BoFmF1nEOEib1H1os0%2BiaED532iF6FuaLdwzi4V%2F9hP7C9V2myMifSP0GzVTZuTGDuI%2F%2B7GdGTzh%2F2XXndY8vk8olvCGBLwJGJ%2BLMKbVUgZM3U3mT2resJO%2FRMODN98kGOqUBtJLS70bnlniw%2B6jZia7GCEAuWC6xG83YCm3snbL8WcgWe14bTGWGOV60r3748lcHGUWXslS4JuACC3EH2NGfMGAxoutXQFduSQ2y42UR9A3df5lsQEGUWub7VuyTxbxH9f%2Bt9Kt2YtEBRHyjzWVPDixTJc2z2EMaynMzU5mFXXu9oL5o090XZ1oVOXxYVNJuVf7n4yKzd2zrWeoFl0jOwM5KCgtD&X-Amz-Signature=117377410ddbb917d00b24c6e0d5922f116765ba57d4ca3dbc7b9379e7cb65d7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
> 💡 **The output of `inner`, `outer`, `left` and `right` merge does only differ if there are some values in the key-column that are present in of the DataFrames but not in the other.**
---
**Simple merge over index-columns**
In the previous example we have specified the parameters `left_on` and `right_on` to tell Python which column to use as key-column in the two DataFrames.
Now if we want to use the index as the key-column we can do that as well.
Let’s set the column `Team` as index using the `.set_index()` method.
```python
teams_players_df.set_index('Team', inplace=True)
teams_goals_df.set_index('Team', inplace=True)
```
`teams_players_df`
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/fa07d056-415f-49e7-84b0-94cfa9734610/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667TMZMJD7%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T222552Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJGMEQCIFIaod3sqRgfSOjPaLMXVNPbnuW%2BBRgF5uv%2BEkOubEWGAiASTo5m64ZFLwX6%2FmTcCPguwnBIu3owytJUiufM5N0xNir%2FAwgnEAAaDDYzNzQyMzE4MzgwNSIMJV6S0acE5rB1pPs%2FKtwDQHmZ8nmximumo1nA9BFKVsDwqGI4ggFVBkTco95x5cVcBO9r20Vmf3FVVLYtyHvu4GBhpMt1LFsQvEsrAxd6MmmZwQ4tot40glQ4iTt%2FVz%2BVREwvhTLycYk2%2Fib2Hur%2BR63ZklL4uU%2Fg2EHniElSpAHC%2F22FQb7NO1R6Yz0cQLC4O%2FBE6ncz63KQjGWY4QYyAd6N27vqHOswt%2BafQqZhulodmwDnxJ%2BFS51kF%2BxG3%2Fzdp%2BKDb5F%2FLuTNprS0jt92mMy7Nq%2FsZn1ChbVD7wQ7wXeg%2BbnrdMyvAWMWjZkKNMvDDmxNpKZh9QqPq6BGTC%2BpKXDJczgghr3TGbL6ATKG9jY4dE3643Mdmmbp7oSVBY3OEK2HAswFjfUirBr7gdMwAVOXYlGmnZtOUreQPFvN4GnNw1rbl67oOnNNGFNMNtFx7rR%2FYFz8ONNlEN%2BAvCuLCJlA6RZ5j2CMeXvekaf6xa%2BtL5c8K8guWCghcivyEkbiVMsrji0i%2FqxoC3L%2BZH5vqg9n8K1v08synC0%2BbjVAg7fl8qYhbFwKqZjNnijUJL0nhGsKmM9TQBNmoZTkglfrqiGR2je49qjLXIpB8fSVR0%2B%2Bh%2BziGMcbyBiOXb5mf5d8SCgolG9eA%2BUloAkw8M33yQY6pgE9ZmI5NgUZET2vNIKv2QGkWheODc%2FB9nr4UJX957YYPP8AOAwl%2BfiA38%2FKnnYEOnQ6mdGrDDbZDuWKAQQW%2FU3tXpIwUKvU%2Bx%2F7dT9w%2FHb8yIwte4vb103m8fVYqiufb2HWo7evyQGt2oprtSjPxarKOGsktUjYPJprlqGjDqQNESlIHeRbLFypOgzGlsqQpXLQDCQF367q%2FMnN6ZHYwHXLEb0ANU7r&X-Amz-Signature=2fcfaa494bf259f5389a5c2d6080731ba7eaf60aef093e50cb94c0a24904b951&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

`teams_goals_df`
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/c92e9e38-25a7-447f-acc3-6d29a922c350/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664MM3MB5E%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T222556Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJGMEQCIACspZ5hMAqKav0HaijoKgtuYP1u33MlUUDtG1%2Fs753kAiAfMajfTEJUGgl%2BDeBsP9j91uB0ANAu0SKc0670Q%2Biu%2FSr%2FAwgnEAAaDDYzNzQyMzE4MzgwNSIMvrCZHrn%2Fjod09HSCKtwDKKrryQv%2F%2FLQ%2BYH7BELMU6ANDruecxJEwa8vkmzgGy%2BqpV6kpgAoH6BgOVoY9oWAtEZSpH0qscmgvtSnLVCxFT%2FRwNuYT%2FDwnzNODWnQ6kGnx%2FlhhR13ePMRi1qAPClKJQl3gnHwQ0WN7pkjrE2rFjGogXafceNu2750Fhsy2M6BPV4q9XI1qPm2O4XNeM2%2BcwHlwx73bnh%2FPBWl%2FwdJaK3gDmSZVnZl%2FCtC54tRGeXW9Yubd9joZbiETrmGa1YvESqp2ZXt6vk7zKZa4kSIAHl%2FuUYSzFka2NU1qI8a7NWRuYJtbh4Cb3C8aIXOjTlwis1wpiTqpHykCIR9SyC3zvas2X5J38e8xp7MfzijR9pgJiOVTVXSIzsemPgvr%2BXcHjxYfClryG4MwNY%2BeAy7I7euqpIAo%2BXIIl4jx8x2ZOxvnRF%2F31WPzA6Jm2QEI%2B%2FwAX%2FiYu6wX5E%2BzflnD9C3ayePKUNeBKI2eWCqXnNwIqVPkgxMbYli0DMjbkq4em%2Bz%2B7Nfv0ZlcmktYyGbK3qjGBjXLNtPXcaR00vleoKL7PZ0P1Hp8rvNLJpe8puDHCUXfNyiELX5SiucfYPtkQtelgsOAMD9OSMN6%2FzixFEN5l8wyHKhSAaYExczYFFQw1s73yQY6pgGSjjtSpz0rdz5qqoNlZ5mtcBEXQXs6VuJy31LgnHbWRdFE0OnQNaVeLqgrtCpFKC1bgeYLJK7Wi8QXuzf%2F97mV701tPqtJi%2Fu%2FEl4wuuc49ggd%2F2CmY1itNyW2IO3QKMKcQj5nFut3HedLtYXNulIcJruaYuNI4ZC4eREXyUDFaCG560%2FWTmBc5jR4gi%2F%2B%2FDxAS4eVH%2B%2BTeBRiYWu%2BDCQl6hKnY6Ne&X-Amz-Signature=f0e6ddad37e0ec3dc853baa184cb48acd4f304845b53878c60afe816f07f65e2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
Now if we want to merge the two DataFrames together we can simply specify the `left_index=` and `right_index=` parameters and tell Python that the indexes should be use as key-columns and we get the same output as before.
```python
team_stats_df = pd.merge(teams_players_df, teams_goals_df, 'inner', left_index = True, right_index = True)
```
![teams_stats_df](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/f966153d-f56f-4c61-a446-0ab9b688a507/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667SPW7UAC%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T222537Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIB9ZlUzC4v%2BqcuZZTRSFmmkC3yQkILI4y5Gb6za8g371AiEA2yLEY3N5%2FEAAn3hahBFj3crV5u0BD6uRIi9rJBD9WSwq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDBKRvFYFBLhVspqynircAyAj9Gy5LA5QNE%2FYPI9JiisD2HRFlkReHbp40eR1GJPJDX7EBWIiJaKWncPyRiqiwWYexx%2BvrPnVV10%2B1deVx4VtB9CD581NOvfzw63CJU3BQFCruA5PO%2Fk6U9%2B9kgK82hXjN5aZRQWTMi7SMvpFkFnAzDHlgH30H5MTFTTt66iO8AdQcLEuxQDhhCG5u5ORaSjWZ5NKGOuNbALQUMIpUTFQ1O84IBhQkVYRBMCykPqKPOXTG%2BpGMv%2BNcBsKiluTtm1VKzComVKyr3vQgYOiWHhXg%2F1e8nFtk6iq7%2FZkxqxp0xCb9hTNA5DCidqtisI3uguUKRNZSU8a96QlNcMj0V9bXY88wZpO8LjMOJie73WypTr6SLeolchCveqW%2FWnfOJR1pkDpeMCHMs8y29uFSaZmh1fRIQwUht%2B385M%2F27i0jdwlo7oCA9YsTXiuykdp%2B5VUA1JaTdTeMysn9ku%2BM8poruAwL1T21TDQ70EKZ1qG6TynM2e6iOF3zcK%2FXmoWDj3BoFmF1nEOEib1H1os0%2BiaED532iF6FuaLdwzi4V%2F9hP7C9V2myMifSP0GzVTZuTGDuI%2F%2B7GdGTzh%2F2XXndY8vk8olvCGBLwJGJ%2BLMKbVUgZM3U3mT2resJO%2FRMODN98kGOqUBtJLS70bnlniw%2B6jZia7GCEAuWC6xG83YCm3snbL8WcgWe14bTGWGOV60r3748lcHGUWXslS4JuACC3EH2NGfMGAxoutXQFduSQ2y42UR9A3df5lsQEGUWub7VuyTxbxH9f%2Bt9Kt2YtEBRHyjzWVPDixTJc2z2EMaynMzU5mFXXu9oL5o090XZ1oVOXxYVNJuVf7n4yKzd2zrWeoFl0jOwM5KCgtD&X-Amz-Signature=117377410ddbb917d00b24c6e0d5922f116765ba57d4ca3dbc7b9379e7cb65d7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
> 💡 **If the key-columns / matching values are in the index of one (or both) DataFrames we must specify the `left_index=` or/and `right_index=` parameters, otherwise we use the `left_on=` or/and `right_on=` parameters.**
---
**Modify DataFrames to create difference**
As we learnt already, the output of inner, outer, left and right merge does only differ if there is also a difference in the two DataFrames.
So let’s create this difference by dropping the teams Arsenal and Manchester City from the `teams_players_df` DataFrame:
```python
teams_players_new = teams_players_df[(teams_players_df.Team != 'Arsenal') & (teams_players_df.Team != 'Manchester City')]
```
And by dropping the teams Chelsea and Burnley from the `teams_goals_df` DataFrame.
```python
teams_goals_new = team_goals_df.drop(team_goals_df.loc[(team_goals_df.Team == 'Chelsea') | (team_goals_df.Team == 'Burnley')].index)
```
To avoid any confusion we saved the updated DataFrames in new variables with the `_new` extension.
`teams_players_new`
Arsenal and Manchester City are missing
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/c7d7e7df-3a32-451a-98bf-c558a0dd3f4e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WTTO6QVP%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T222557Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIHWW8knstrB4mzkvLRH0vRkKSdmcD8LyH66rLMK6E23iAiEA4MFbIVvGa0gOnYpNDb1QbDMRvTmKHNRrL062j3PN%2FIYq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDBaWRNXundRog7AttSrcAwZY%2B1Oy4wLOY3vmlJVqj7TvohNF2jRxd9bptJlVf3tfpMcDyXi011bZ0kEB%2BH0nCjsQOtBOZwx90yBiHqj4MvxrLLR%2FUj2uxK3IrH%2B9JPX86Lz4v4IpaE2nl8%2BBXgiA8M74eZZ2wufbB8YVQ0pQcg3ymkIkilzM7gOgcH0wIJmKKzhVQJy7Tf%2BY49r%2BE65R6eIDUcVzWwx83td%2BprivwWLKvo%2BLwISCyLVERv%2F10VNl7Hywatjz6lLOmBTLoLJz503w57g%2BtrSvnzce2jxVjRzfCGaP3CzEVg2bWAnutJS6mqAre8ITJCDmlZjmBIQuUKqv1ClLXRfcaU7MxoJTVgS6IZyynQNQfMHTC4I%2BtnbaVsLoOzHww8UnCECzFoeMy%2Be1B%2Fcjv9JBB7BNB0XZjrb5V5mLn%2BsE03lXnTZRKizt%2FhKNM4wiQ6ukHbce8X4%2FpFNjQ6EzJcZiFyfZvtyfiwdN3HR8U6E%2BvG%2FPCoia%2BjjOjnMQQnLdDfGns%2B%2Bfz0hFrMyFppI6Y%2Bcpn41dtJUy2I3B1iQzAiDSNG872zwhGjDlfAA8niwihB6p7jFgRRteyndE68412gT0ycN9b%2F8T76WMBQsHOZjgKzIR%2ByZWCkpKCNhlqtj5naPhKohpMITO98kGOqUB8UraZJjXTLnrJtP7qfKyZvX8QckocVxoppijkLpDgPci674ncLgnQoM58LtrNnvxZaelRNMg2rmv%2BLqi5N9kTtP8pGE4PnC7Pl%2FGMCmC%2FtoIqMzdyyix96%2F35o4VOWP%2BZwqPle5UdDlybCbJxzrdp0zUBxTHr0522gWV26F5ha5ZFk3HKJvjCjyYzh7o83gIIBAV%2FXINWM7iIHDLo1NBnrr14MBa&X-Amz-Signature=47b82791bf4182112d93d46ed650d663086eddbe32d87cc5e8c013a06b108a57&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
`teams_goals_new`
Chelsea and Burnley are missing
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/4a460f8b-2082-49cc-a749-a2543eec972c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663QZOX67C%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T222558Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQC4VjvEOlEXYW6qkVwjtpAF1tuP5qRQxdKfCO8bFOxrqgIhAImRE%2F5O2VG8rsPddXnJoDPjTI5Gn8ityE7YSN0vXYndKv8DCCcQABoMNjM3NDIzMTgzODA1Igzbdc5cBqu5ZYAfNGgq3AP01VfB2mdytrV9KNV1WhS%2Fo9SNdD5Ppta9VohF5sN2EzeTqEnGzXsN3ZiIHdGabfygIqp2KnupSw%2BWr8HU%2BSE%2BWy3AKykXX23XYmqEh42XeHdF7%2Fc%2BPk8DFVaYHEkQ5nAzN2wq4j9og7jGonHTZeL9LLBnEX1wI4yUPLj0%2BDuhCWvetd7VcQooHjZSBGVAzO5UYpTz4d0IjitzLE1RZ1X1PAq4%2BTNcMLFVbuhLsjBKyZ7totxSJ33VS4YwkyNw3BtwtIRCXUZkqlJUGtowkedBxqlbsBsm2eiQwqQe6b1O%2BpYIumr8WyODfqFNKVTHRJ4zkFHOXL3ARVT%2F3WeIOgvjV%2BkWQRYI3KdUohqNL6ik2O2YFcq7eDHaMXIPrZTSs4ZRG%2FlZEnLo1NeWIglprZTClkXlWaktP9VF3LfV9hCtc2K1OVUBH0PDDsterduNf6oRBMemqjxA4G05uVzICrElgaCsF1XUH85Lf%2FIMTo2RSsFUmftS3SiHoyQodhepOsJurBTLhgzIf7M7N09bL94ukPvo4oj3Blrs36RSeyQJmc%2BUWWh%2B63vielhy6SIluQHPS696kIzp1c0Gd0UJq%2F%2F48Sox6FzX1%2FBh7eaY2SbreGAJAoFZLjIbM9nR8DCIzvfJBjqkAYo1rxRRgnxhoYM3%2BHDxi7m6%2FiWuYjaftEe2hL5DrOshnKZLhiWrwHTsmaRaS4LZVRfNk9S5IDe04TcsYHreVs3HUK1D6MXXeExTgGYHMwXYaFda7FQIYSSJZNPrahuccz6iWrplGdkTLaD%2B%2BbSxYQVVDw8JG5mVHx%2Ft0SpHZV9VxBXkbHWbAYXcnxvG7rFJhLaOC7y84lbEcPY6qyxJxAwxYK8N&X-Amz-Signature=972a87623a88df45e26a6c1e8223cb7d3ba108b9b76d2450c28ff62c756cd680&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
---
**Inner merge**
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/5408a8e0-787f-4825-a1d7-569d613696af/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667SPW7UAC%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T222537Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIB9ZlUzC4v%2BqcuZZTRSFmmkC3yQkILI4y5Gb6za8g371AiEA2yLEY3N5%2FEAAn3hahBFj3crV5u0BD6uRIi9rJBD9WSwq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDBKRvFYFBLhVspqynircAyAj9Gy5LA5QNE%2FYPI9JiisD2HRFlkReHbp40eR1GJPJDX7EBWIiJaKWncPyRiqiwWYexx%2BvrPnVV10%2B1deVx4VtB9CD581NOvfzw63CJU3BQFCruA5PO%2Fk6U9%2B9kgK82hXjN5aZRQWTMi7SMvpFkFnAzDHlgH30H5MTFTTt66iO8AdQcLEuxQDhhCG5u5ORaSjWZ5NKGOuNbALQUMIpUTFQ1O84IBhQkVYRBMCykPqKPOXTG%2BpGMv%2BNcBsKiluTtm1VKzComVKyr3vQgYOiWHhXg%2F1e8nFtk6iq7%2FZkxqxp0xCb9hTNA5DCidqtisI3uguUKRNZSU8a96QlNcMj0V9bXY88wZpO8LjMOJie73WypTr6SLeolchCveqW%2FWnfOJR1pkDpeMCHMs8y29uFSaZmh1fRIQwUht%2B385M%2F27i0jdwlo7oCA9YsTXiuykdp%2B5VUA1JaTdTeMysn9ku%2BM8poruAwL1T21TDQ70EKZ1qG6TynM2e6iOF3zcK%2FXmoWDj3BoFmF1nEOEib1H1os0%2BiaED532iF6FuaLdwzi4V%2F9hP7C9V2myMifSP0GzVTZuTGDuI%2F%2B7GdGTzh%2F2XXndY8vk8olvCGBLwJGJ%2BLMKbVUgZM3U3mT2resJO%2FRMODN98kGOqUBtJLS70bnlniw%2B6jZia7GCEAuWC6xG83YCm3snbL8WcgWe14bTGWGOV60r3748lcHGUWXslS4JuACC3EH2NGfMGAxoutXQFduSQ2y42UR9A3df5lsQEGUWub7VuyTxbxH9f%2Bt9Kt2YtEBRHyjzWVPDixTJc2z2EMaynMzU5mFXXu9oL5o090XZ1oVOXxYVNJuVf7n4yKzd2zrWeoFl0jOwM5KCgtD&X-Amz-Signature=99629b910d0f82c1d75102914f971bc96d50f60ca457598ab8ea7a990952f439&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
As we now have some difference in our DataFrames we can analyse how the four different merging modes work and we start with the inner merge.
```python
inner_merge_df = pd.merge(teams_players_new, teams_goals_new, 'inner', left_on = 'Team', right_on = 'Team')
```
![inner_merge_df](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/79a226fa-2761-47e7-b051-752ec50a0f14/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667SPW7UAC%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T222537Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIB9ZlUzC4v%2BqcuZZTRSFmmkC3yQkILI4y5Gb6za8g371AiEA2yLEY3N5%2FEAAn3hahBFj3crV5u0BD6uRIi9rJBD9WSwq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDBKRvFYFBLhVspqynircAyAj9Gy5LA5QNE%2FYPI9JiisD2HRFlkReHbp40eR1GJPJDX7EBWIiJaKWncPyRiqiwWYexx%2BvrPnVV10%2B1deVx4VtB9CD581NOvfzw63CJU3BQFCruA5PO%2Fk6U9%2B9kgK82hXjN5aZRQWTMi7SMvpFkFnAzDHlgH30H5MTFTTt66iO8AdQcLEuxQDhhCG5u5ORaSjWZ5NKGOuNbALQUMIpUTFQ1O84IBhQkVYRBMCykPqKPOXTG%2BpGMv%2BNcBsKiluTtm1VKzComVKyr3vQgYOiWHhXg%2F1e8nFtk6iq7%2FZkxqxp0xCb9hTNA5DCidqtisI3uguUKRNZSU8a96QlNcMj0V9bXY88wZpO8LjMOJie73WypTr6SLeolchCveqW%2FWnfOJR1pkDpeMCHMs8y29uFSaZmh1fRIQwUht%2B385M%2F27i0jdwlo7oCA9YsTXiuykdp%2B5VUA1JaTdTeMysn9ku%2BM8poruAwL1T21TDQ70EKZ1qG6TynM2e6iOF3zcK%2FXmoWDj3BoFmF1nEOEib1H1os0%2BiaED532iF6FuaLdwzi4V%2F9hP7C9V2myMifSP0GzVTZuTGDuI%2F%2B7GdGTzh%2F2XXndY8vk8olvCGBLwJGJ%2BLMKbVUgZM3U3mT2resJO%2FRMODN98kGOqUBtJLS70bnlniw%2B6jZia7GCEAuWC6xG83YCm3snbL8WcgWe14bTGWGOV60r3748lcHGUWXslS4JuACC3EH2NGfMGAxoutXQFduSQ2y42UR9A3df5lsQEGUWub7VuyTxbxH9f%2Bt9Kt2YtEBRHyjzWVPDixTJc2z2EMaynMzU5mFXXu9oL5o090XZ1oVOXxYVNJuVf7n4yKzd2zrWeoFl0jOwM5KCgtD&X-Amz-Signature=b4f26294f703c50905eeeeaf1bd688c4baf4cbb75a90c1de08b512b225e0f354&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
We can now see that the `inner_merge_df` only has 16 rows but the source DataFrames, `teams_goals_new` and `teams_players_new` both have 20 rows.
Why is that? Well with the inner merge we only include those rows in the output that are present in both DataFrames. As we do the merge using column `Team` as key-column we must look at this column which leads us to the following observation:
The values Arsenal and Manchester are present in the key-column (`Team`) of the right DataFrame (`teams_goals_new`) but not in the left DataFrame (`teams_players_df`)
→ these two rows are not included in the output.
The values Chelsea and Burnley are present in the key-column (`Team`) of the left DataFrame (`teams_players_new`) but not in the right DataFrame (`teams_goals_new`)
→ these two rows are not included in the output.
> 💡 **Inner merge only includes overlapping values in the output. If a value is present in one but not the other DataFrame, its entire row is excluded.**
---
**Left merge**
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/09e2253a-b6d9-411d-836b-faa79515429b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667SPW7UAC%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T222538Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIB9ZlUzC4v%2BqcuZZTRSFmmkC3yQkILI4y5Gb6za8g371AiEA2yLEY3N5%2FEAAn3hahBFj3crV5u0BD6uRIi9rJBD9WSwq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDBKRvFYFBLhVspqynircAyAj9Gy5LA5QNE%2FYPI9JiisD2HRFlkReHbp40eR1GJPJDX7EBWIiJaKWncPyRiqiwWYexx%2BvrPnVV10%2B1deVx4VtB9CD581NOvfzw63CJU3BQFCruA5PO%2Fk6U9%2B9kgK82hXjN5aZRQWTMi7SMvpFkFnAzDHlgH30H5MTFTTt66iO8AdQcLEuxQDhhCG5u5ORaSjWZ5NKGOuNbALQUMIpUTFQ1O84IBhQkVYRBMCykPqKPOXTG%2BpGMv%2BNcBsKiluTtm1VKzComVKyr3vQgYOiWHhXg%2F1e8nFtk6iq7%2FZkxqxp0xCb9hTNA5DCidqtisI3uguUKRNZSU8a96QlNcMj0V9bXY88wZpO8LjMOJie73WypTr6SLeolchCveqW%2FWnfOJR1pkDpeMCHMs8y29uFSaZmh1fRIQwUht%2B385M%2F27i0jdwlo7oCA9YsTXiuykdp%2B5VUA1JaTdTeMysn9ku%2BM8poruAwL1T21TDQ70EKZ1qG6TynM2e6iOF3zcK%2FXmoWDj3BoFmF1nEOEib1H1os0%2BiaED532iF6FuaLdwzi4V%2F9hP7C9V2myMifSP0GzVTZuTGDuI%2F%2B7GdGTzh%2F2XXndY8vk8olvCGBLwJGJ%2BLMKbVUgZM3U3mT2resJO%2FRMODN98kGOqUBtJLS70bnlniw%2B6jZia7GCEAuWC6xG83YCm3snbL8WcgWe14bTGWGOV60r3748lcHGUWXslS4JuACC3EH2NGfMGAxoutXQFduSQ2y42UR9A3df5lsQEGUWub7VuyTxbxH9f%2Bt9Kt2YtEBRHyjzWVPDixTJc2z2EMaynMzU5mFXXu9oL5o090XZ1oVOXxYVNJuVf7n4yKzd2zrWeoFl0jOwM5KCgtD&X-Amz-Signature=7d5f7175481e0fd31b33e77341da5525ca7f23b55cfe320d8efd18f5f65cd7d8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
While the inner merge includes the overlapping rows only, the left merge includes all rows from the left DataFrame plus the values from the right DataFrame for the overlapping rows. 
```python
left_merge_df = pd.merge(teams_goals_new, teams_players_new, 'left', left_on = 'Team', right_on = 'Team')
```
![left_merge_df](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/fc5638ad-e2c6-491c-81ca-3d9dee8fa8a2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667SPW7UAC%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T222538Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIB9ZlUzC4v%2BqcuZZTRSFmmkC3yQkILI4y5Gb6za8g371AiEA2yLEY3N5%2FEAAn3hahBFj3crV5u0BD6uRIi9rJBD9WSwq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDBKRvFYFBLhVspqynircAyAj9Gy5LA5QNE%2FYPI9JiisD2HRFlkReHbp40eR1GJPJDX7EBWIiJaKWncPyRiqiwWYexx%2BvrPnVV10%2B1deVx4VtB9CD581NOvfzw63CJU3BQFCruA5PO%2Fk6U9%2B9kgK82hXjN5aZRQWTMi7SMvpFkFnAzDHlgH30H5MTFTTt66iO8AdQcLEuxQDhhCG5u5ORaSjWZ5NKGOuNbALQUMIpUTFQ1O84IBhQkVYRBMCykPqKPOXTG%2BpGMv%2BNcBsKiluTtm1VKzComVKyr3vQgYOiWHhXg%2F1e8nFtk6iq7%2FZkxqxp0xCb9hTNA5DCidqtisI3uguUKRNZSU8a96QlNcMj0V9bXY88wZpO8LjMOJie73WypTr6SLeolchCveqW%2FWnfOJR1pkDpeMCHMs8y29uFSaZmh1fRIQwUht%2B385M%2F27i0jdwlo7oCA9YsTXiuykdp%2B5VUA1JaTdTeMysn9ku%2BM8poruAwL1T21TDQ70EKZ1qG6TynM2e6iOF3zcK%2FXmoWDj3BoFmF1nEOEib1H1os0%2BiaED532iF6FuaLdwzi4V%2F9hP7C9V2myMifSP0GzVTZuTGDuI%2F%2B7GdGTzh%2F2XXndY8vk8olvCGBLwJGJ%2BLMKbVUgZM3U3mT2resJO%2FRMODN98kGOqUBtJLS70bnlniw%2B6jZia7GCEAuWC6xG83YCm3snbL8WcgWe14bTGWGOV60r3748lcHGUWXslS4JuACC3EH2NGfMGAxoutXQFduSQ2y42UR9A3df5lsQEGUWub7VuyTxbxH9f%2Bt9Kt2YtEBRHyjzWVPDixTJc2z2EMaynMzU5mFXXu9oL5o090XZ1oVOXxYVNJuVf7n4yKzd2zrWeoFl0jOwM5KCgtD&X-Amz-Signature=fa94304fb9921676bde6795e8b30b6d7c00519aeaa04c70b64c86ebadc5a72da&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
We can now see that the `left_merge_df` has 18 rows in total and two `NaN` values.
Why 18 rows? We know already that the teams Arsenal and Manchester City are in the right DataFrame (`teams_players_new`) but not in the left one (`teams_goals_new`). As we do a left merge all rows from the left DataFrame are included regardless if the team is in the right DataFrame too (or not). This is why the teams Arsenal and Manchester City are not included in the output but the teams Chelsea and Burnley are still there.
Why are there two `NaN` values? Well, the teams Chelsea and Burnley are not in the right DataFrame, thus we don’t have the information how many goals these two teams scored. Therefore, Python just fills this missing data cells with `NaN` values.
> 💡 **Left merge includes all rows from the left DataFrame plus all overlapping rows and where values are missing, `NaN` is inserted.**
---
**Right merge**
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/15e33ac0-53d8-4e72-867c-7d17c8d7a3e2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667SPW7UAC%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T222538Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIB9ZlUzC4v%2BqcuZZTRSFmmkC3yQkILI4y5Gb6za8g371AiEA2yLEY3N5%2FEAAn3hahBFj3crV5u0BD6uRIi9rJBD9WSwq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDBKRvFYFBLhVspqynircAyAj9Gy5LA5QNE%2FYPI9JiisD2HRFlkReHbp40eR1GJPJDX7EBWIiJaKWncPyRiqiwWYexx%2BvrPnVV10%2B1deVx4VtB9CD581NOvfzw63CJU3BQFCruA5PO%2Fk6U9%2B9kgK82hXjN5aZRQWTMi7SMvpFkFnAzDHlgH30H5MTFTTt66iO8AdQcLEuxQDhhCG5u5ORaSjWZ5NKGOuNbALQUMIpUTFQ1O84IBhQkVYRBMCykPqKPOXTG%2BpGMv%2BNcBsKiluTtm1VKzComVKyr3vQgYOiWHhXg%2F1e8nFtk6iq7%2FZkxqxp0xCb9hTNA5DCidqtisI3uguUKRNZSU8a96QlNcMj0V9bXY88wZpO8LjMOJie73WypTr6SLeolchCveqW%2FWnfOJR1pkDpeMCHMs8y29uFSaZmh1fRIQwUht%2B385M%2F27i0jdwlo7oCA9YsTXiuykdp%2B5VUA1JaTdTeMysn9ku%2BM8poruAwL1T21TDQ70EKZ1qG6TynM2e6iOF3zcK%2FXmoWDj3BoFmF1nEOEib1H1os0%2BiaED532iF6FuaLdwzi4V%2F9hP7C9V2myMifSP0GzVTZuTGDuI%2F%2B7GdGTzh%2F2XXndY8vk8olvCGBLwJGJ%2BLMKbVUgZM3U3mT2resJO%2FRMODN98kGOqUBtJLS70bnlniw%2B6jZia7GCEAuWC6xG83YCm3snbL8WcgWe14bTGWGOV60r3748lcHGUWXslS4JuACC3EH2NGfMGAxoutXQFduSQ2y42UR9A3df5lsQEGUWub7VuyTxbxH9f%2Bt9Kt2YtEBRHyjzWVPDixTJc2z2EMaynMzU5mFXXu9oL5o090XZ1oVOXxYVNJuVf7n4yKzd2zrWeoFl0jOwM5KCgtD&X-Amz-Signature=21df3bbb268e9a1b2ed3dda1182d42ad7550a2c789eac30aefbfca2e115c68a6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
The right merge is the pendant to the left merge. With the only difference that the right merge includes all rows from the right DataFrame plus the values from the left DataFrame for the overlapping rows.
```python
right_merge_df = pd.merge(teams_goals_new, teams_players_new, 'right', left_on = 'Team', right_on = 'Team')
```
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/039bd199-4137-4018-b9d7-2221c16121dd/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667SPW7UAC%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T222538Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIB9ZlUzC4v%2BqcuZZTRSFmmkC3yQkILI4y5Gb6za8g371AiEA2yLEY3N5%2FEAAn3hahBFj3crV5u0BD6uRIi9rJBD9WSwq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDBKRvFYFBLhVspqynircAyAj9Gy5LA5QNE%2FYPI9JiisD2HRFlkReHbp40eR1GJPJDX7EBWIiJaKWncPyRiqiwWYexx%2BvrPnVV10%2B1deVx4VtB9CD581NOvfzw63CJU3BQFCruA5PO%2Fk6U9%2B9kgK82hXjN5aZRQWTMi7SMvpFkFnAzDHlgH30H5MTFTTt66iO8AdQcLEuxQDhhCG5u5ORaSjWZ5NKGOuNbALQUMIpUTFQ1O84IBhQkVYRBMCykPqKPOXTG%2BpGMv%2BNcBsKiluTtm1VKzComVKyr3vQgYOiWHhXg%2F1e8nFtk6iq7%2FZkxqxp0xCb9hTNA5DCidqtisI3uguUKRNZSU8a96QlNcMj0V9bXY88wZpO8LjMOJie73WypTr6SLeolchCveqW%2FWnfOJR1pkDpeMCHMs8y29uFSaZmh1fRIQwUht%2B385M%2F27i0jdwlo7oCA9YsTXiuykdp%2B5VUA1JaTdTeMysn9ku%2BM8poruAwL1T21TDQ70EKZ1qG6TynM2e6iOF3zcK%2FXmoWDj3BoFmF1nEOEib1H1os0%2BiaED532iF6FuaLdwzi4V%2F9hP7C9V2myMifSP0GzVTZuTGDuI%2F%2B7GdGTzh%2F2XXndY8vk8olvCGBLwJGJ%2BLMKbVUgZM3U3mT2resJO%2FRMODN98kGOqUBtJLS70bnlniw%2B6jZia7GCEAuWC6xG83YCm3snbL8WcgWe14bTGWGOV60r3748lcHGUWXslS4JuACC3EH2NGfMGAxoutXQFduSQ2y42UR9A3df5lsQEGUWub7VuyTxbxH9f%2Bt9Kt2YtEBRHyjzWVPDixTJc2z2EMaynMzU5mFXXu9oL5o090XZ1oVOXxYVNJuVf7n4yKzd2zrWeoFl0jOwM5KCgtD&X-Amz-Signature=3dcb90180cce8a506057fd76eb5e3b039bd10e46432d043b6a92ea8c13f6ebaf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
Again you can see that there are 18 rows in total. This time the teams Chelsea and Burnley are left out as they are only present in the left DataFrame (`teams_goals_df`) but not in the right DataFrame (`teams_players_df`).
Also, for those teams that are in the right but not in the left DataFrame, Manchester City and Arsenal, `NaN` is inserted as we don’t have information available about the number of players they have.
> 💡 **Right merge includes all rows from the right DataFrame plus all overlapping rows and where values are missing, `NaN` is inserted.**
---
**Outer merge**
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/806d7472-621f-489c-b76f-7cfde93b8afc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667SPW7UAC%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T222538Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIB9ZlUzC4v%2BqcuZZTRSFmmkC3yQkILI4y5Gb6za8g371AiEA2yLEY3N5%2FEAAn3hahBFj3crV5u0BD6uRIi9rJBD9WSwq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDBKRvFYFBLhVspqynircAyAj9Gy5LA5QNE%2FYPI9JiisD2HRFlkReHbp40eR1GJPJDX7EBWIiJaKWncPyRiqiwWYexx%2BvrPnVV10%2B1deVx4VtB9CD581NOvfzw63CJU3BQFCruA5PO%2Fk6U9%2B9kgK82hXjN5aZRQWTMi7SMvpFkFnAzDHlgH30H5MTFTTt66iO8AdQcLEuxQDhhCG5u5ORaSjWZ5NKGOuNbALQUMIpUTFQ1O84IBhQkVYRBMCykPqKPOXTG%2BpGMv%2BNcBsKiluTtm1VKzComVKyr3vQgYOiWHhXg%2F1e8nFtk6iq7%2FZkxqxp0xCb9hTNA5DCidqtisI3uguUKRNZSU8a96QlNcMj0V9bXY88wZpO8LjMOJie73WypTr6SLeolchCveqW%2FWnfOJR1pkDpeMCHMs8y29uFSaZmh1fRIQwUht%2B385M%2F27i0jdwlo7oCA9YsTXiuykdp%2B5VUA1JaTdTeMysn9ku%2BM8poruAwL1T21TDQ70EKZ1qG6TynM2e6iOF3zcK%2FXmoWDj3BoFmF1nEOEib1H1os0%2BiaED532iF6FuaLdwzi4V%2F9hP7C9V2myMifSP0GzVTZuTGDuI%2F%2B7GdGTzh%2F2XXndY8vk8olvCGBLwJGJ%2BLMKbVUgZM3U3mT2resJO%2FRMODN98kGOqUBtJLS70bnlniw%2B6jZia7GCEAuWC6xG83YCm3snbL8WcgWe14bTGWGOV60r3748lcHGUWXslS4JuACC3EH2NGfMGAxoutXQFduSQ2y42UR9A3df5lsQEGUWub7VuyTxbxH9f%2Bt9Kt2YtEBRHyjzWVPDixTJc2z2EMaynMzU5mFXXu9oL5o090XZ1oVOXxYVNJuVf7n4yKzd2zrWeoFl0jOwM5KCgtD&X-Amz-Signature=494e656febab1ea3ab56d6282729a486afe3229d334cf1082a9e8932af4a9d90&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
The outer merge is the combination of the left and right merge. This means that the outer merge includes all rows from both DataFrames and thus no rows are left out in the output.
```python
outer_merge_df = pd.merge(teams_goals_new, teams_players_new, 'outer', left_on = 'Team', right_on = 'Team')
```
![outer_merge_df](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/2431d095-7483-492f-b1ec-5fe0a2250ea9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667SPW7UAC%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T222538Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIB9ZlUzC4v%2BqcuZZTRSFmmkC3yQkILI4y5Gb6za8g371AiEA2yLEY3N5%2FEAAn3hahBFj3crV5u0BD6uRIi9rJBD9WSwq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDBKRvFYFBLhVspqynircAyAj9Gy5LA5QNE%2FYPI9JiisD2HRFlkReHbp40eR1GJPJDX7EBWIiJaKWncPyRiqiwWYexx%2BvrPnVV10%2B1deVx4VtB9CD581NOvfzw63CJU3BQFCruA5PO%2Fk6U9%2B9kgK82hXjN5aZRQWTMi7SMvpFkFnAzDHlgH30H5MTFTTt66iO8AdQcLEuxQDhhCG5u5ORaSjWZ5NKGOuNbALQUMIpUTFQ1O84IBhQkVYRBMCykPqKPOXTG%2BpGMv%2BNcBsKiluTtm1VKzComVKyr3vQgYOiWHhXg%2F1e8nFtk6iq7%2FZkxqxp0xCb9hTNA5DCidqtisI3uguUKRNZSU8a96QlNcMj0V9bXY88wZpO8LjMOJie73WypTr6SLeolchCveqW%2FWnfOJR1pkDpeMCHMs8y29uFSaZmh1fRIQwUht%2B385M%2F27i0jdwlo7oCA9YsTXiuykdp%2B5VUA1JaTdTeMysn9ku%2BM8poruAwL1T21TDQ70EKZ1qG6TynM2e6iOF3zcK%2FXmoWDj3BoFmF1nEOEib1H1os0%2BiaED532iF6FuaLdwzi4V%2F9hP7C9V2myMifSP0GzVTZuTGDuI%2F%2B7GdGTzh%2F2XXndY8vk8olvCGBLwJGJ%2BLMKbVUgZM3U3mT2resJO%2FRMODN98kGOqUBtJLS70bnlniw%2B6jZia7GCEAuWC6xG83YCm3snbL8WcgWe14bTGWGOV60r3748lcHGUWXslS4JuACC3EH2NGfMGAxoutXQFduSQ2y42UR9A3df5lsQEGUWub7VuyTxbxH9f%2Bt9Kt2YtEBRHyjzWVPDixTJc2z2EMaynMzU5mFXXu9oL5o090XZ1oVOXxYVNJuVf7n4yKzd2zrWeoFl0jOwM5KCgtD&X-Amz-Signature=29fec6f070a3b5decc2c5e45cee35eec5edb4372c757843addc60fe90a2fb290&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
We can see that the total number of rows is 20. Thus, the four teams that are missing in one of the DataFrames, Manchester City, Arsenal, Burnley and Chelsea, are now included in the output.
Wherever data is missing, because a team is not present in either one of the DataFrames, `NaN` is inserted again. When looking at the `NaN` values we can clearly see that the outer merge is basically just a combination of the left and right merge.
> 💡 **Outer merge includes all rows from both DataFrames and where values are missing, `NaN` is inserted.**
---
## [**`.join()`**](/1a11208373ef44358aa1528a5dc7e807)
---
**.join() vs. merge()**
This function is very similar to [`.merge()`](/1867045b058343e1a66b677961515907#b51439170f884916a453b1c25e6b999f) with three main differences.
1. The `.join()` function uses the indices in the two DataFrames as key-columns to identify the rows that belong together. With the `.merge()` function we could specify any column in the two DataFrames as key-columns.
1. With the `.join()` function the columns and rows of one DataFrame are simply  appended to the other DataFrame but not actually merged. This means that all the data is simply joined into one DataFrame. But no merge is done for data that belong together.
1. When joining two DataFrames, we need to provide a suffix so that overlapping columns that exist in both DataFrames with the same name can be renamed. With `.merge()` Python merged overlapping columns together automatically and thus we did not have to provide these suffixes. 
**Syntax**
The syntax of the join method is the following:
`<< some df >>.join( << other df >> , how = << join method >> , lsuffix = 'some_string', rsuffix = 'some_string' )`
We can see that just as with merge we must specify the join-method (`'left'` `'right'` `'outer'` `'inner'`). If we don’t define this parameter, then `'left'` join is performed by default.
Also, we must specify a suffix for the overlapping columns. Because (as already mentioned) when both DataFrames have a column with the same name, Python needs instructions how to rename them so they can still be distinguished from each other.
---
**Inner join**
Let’s assume we have the same two DataFrames as we had in the `.merge()` examples above. We can perform a simple inner join as follow:
```python
teams_players_new.join(teams_goals_new, how='inner', lsuffix='_left', rsuffix='_right')
```
![Joined DataFrame `teams_players_new` & `teams_goals_new`](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/b538673d-13e4-4314-b241-aeba47efd6d8/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662622DKCH%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T222558Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIQDoEPhxIPC89rphPZxBfriCDeyoBDrZ4BqAulmTb82m5QIgex3B3Zw52EkLXdkO2AZy0mRl6e3PH6%2B4XWnR%2FE7tDZcq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDGmjcwKLPCQF%2BnPghSrcAzQJF0kGU4Bl45mGl1VJMEsADq8kbDiysQQCJ6gcIL7B5266Hf1gb%2FHS67sBoQxjv%2BRjjOiLeZDhVyjxEu6M6NKME7TPH%2BQLJoz20psbxgoYQV%2BB5%2FCHM77n5bpkevmJIP9gYhgOAJzyf1haSugtnGk%2BjP6jAFSoREEeslfdIjZeQX5Trf0g9fhiSS5QJoU4wPi3kFCZM5ZBykeqGQiTGXhtDkQxnlc5W%2BXnrd4EM855exU7%2BOQa4CqSV%2B8nlL4iI5skllho%2FSYjnYdBWLhNsreJxX9%2FBkI1%2BVxC5mRHHg1%2FfAmruMuW%2BZLT%2FdTd0cIVwFt8Nspj3gmYorzEqPX4Sz3MZXXPDaUE3EOGY8vUBc8Cw2AsjRR5jGnwe8yiHPVUeCohZ8UpVd%2B1nwpJ%2FvkqapqYyO2Ja%2Bt6rZWARhcOV7PoFIU1cglB01GoBGbQUx0Z0Lt145iRQHSa%2F3C26QVSlbAoiidfLHnDy3tMyTf%2Bw2dZXvl4jX9aFoim5X5%2BjdR%2FYpM8k0%2FKbZEH1h1bI5rsSX%2BK8XdcRJSrTuV0E0viiCqPB3PEnmcU5BH5b5r6yx5u%2F4qQyAiryP%2FCo34ydsmJZV4CnVMckeKKDGheS%2ByKv0UUxoMCdO0rEYHbygKYMN3O98kGOqUBxsCDHxhVk5gs9cwP%2Fk0mNA7qfhnC%2FVG9dVyGYLlgoKJ8eBPyp9nr6QbWILvtsTeTltLmcTc%2F2Jbd6S3r7hNg1doxM4L86tIjnMmnN%2B0UmCayc0g%2B%2Fqi0hxNhg%2FY7zU5%2BxLaIyh0sPYmRZOzk6rAH4MXq0%2BH8r%2BL7WmBxIzx7Mmv7zb%2Fq7skntDzU1oKg84AAqWTKL61YFyJeheNEXWK3%2FKH5phr1&X-Amz-Signature=5dcf01ff9df1806948828cc2fbb18f95f9e04b133f37a37d556d60d4774dcf94&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
In the output DataFrame we can observe two things.
Firstly, the data from the right DataFrame is just appended but not actually merged with the data from the left DataFrame. Therefore, we still have two columns with team names and some teams have two different index values. For example, Crystal Palace is in `Team_left` at index position 16 and in `Team_right` at index position 18. So, no new index ordering is created when doing a `.join()`.
Secondly, some index positions are missing, i.e., there are some gaps → 0, 2, 11 and 12 are missing. This is because the index positions 0 and 11 do not exist in the left DataFrame `teams_player_new` and the index positions 2 and 12 do not exist in the right DataFrame `teams_goals_new` (see pictures below). And since we do an `'inner'` join these rows are consequently excluded from the output.
![`teams_players_new` with missing index positions 0 and 11](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/ca5f11a7-7993-4b97-a4dc-f04a32c79b77/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RLTI7NM3%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T222601Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQD04NmRtr7%2FwaEKPSyuVLYZKPNXzsEJS6tbcZfxZmcITQIhAPfVfcqw4h7iDX67zC46o7FydoA9MctF4EiSlL%2BAN%2FSZKv8DCCcQABoMNjM3NDIzMTgzODA1IgwDcIckQI6jWg%2BdYCoq3AM1blfa0ScL7JbkHq0tkeQhARYRs25SZI9kGALEOqq1fgv7XBngoK7jEtpPA7rS7%2FeH3CCXvFwQ3fnewBVe94FO0rGlO%2FCRlsXsT2f4LK3iJ6rFXVHdLLGA3vB%2BmU2uPUF0KwBBnoz%2FPnBVJizJ64Fm1%2FwBwLE%2BLcnDkEjkI%2Fv59MOKzW2FNEZY68HZ3lzuJiwFYCz%2F2K2GMZKtYZUnOrlldYq4u%2FeHYVF04KadYgA9DbIfAskp4MevuHRgBUwVr0G%2BiH2vsbgqshVKulzBnAXuuGtoJ9LEEdGjveBJGwioS15XsREvAjQRhV%2FC0OA3e0Yx8vJdivKQIshdvKJwdER5N05LgqL%2FzwqN%2BvPK0uiH%2BSrqOJowXGvdcUnnppmeGgIl%2B2SCksb7L%2Bq23Ck4Oxy0YUF0KrwpKSZSEHeg%2ByTEgrhb2jHyVFXauSu9rvlp%2B0cY%2FjpCI2Tr9%2BgDN4uCTpSMa38BjfoTwNM65QAGnx4Eftex9MtpR7BhhK1qzxU%2BUMNZ3d%2FWTO1P%2B0%2FxOiJASXOxNhLQ5FAYECuGI6lapfWd%2FesgmmcStbm9yq3e3Gz8lt%2Fl5Yzqey%2BsXugpquj1AT0TO2yzVvNnLkdlhuvbJtNBUWbWLnI1bW%2BDoImBHjDfzffJBjqkASd3lBzZapBvTZxzHFPcmlnZbnmKJdvOd8xR6G1qmZ6%2B2vdHTY3DeYaYj3MblEugvdbTT73Rj0S8HrO4ZUqb5TLvujnvIwfrfWQSC2FvHxn2PYlIznMZw%2Frhh9ywFJesNDWbTPeeJL78WeltDcXm4rym30yRbRmYu49vwrMYZNTIihcNfxr09Y3dw13SbjyJmNRALfMF9O%2FUa6Ey2nyajpHSwDVS&X-Amz-Signature=0727d1641c969b2e86b423a29c96d6794df55855441a8a85638003af41fd697d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
![`teams_goals_new` with missing index positions 2 and 12](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/675a20f5-92cf-4684-b55d-caae3e9b9ef0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46642EFCOWK%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T222601Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIB2jdxL9pblhq35qGFWkMAzLIZtuP7tMIIr7BUU%2BQpdXAiEA%2Fb79oY6ilbxz3sXQJtZNge%2BOOxzkDk%2FPWSX62XaJIY4q%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDC6Gu%2BlByI3W9aWtYSrcAxPrFq6KcVuyTY5HKiKiNw%2Bcs7C4PYW29sWKNZMYK%2F6lP2OsQBx18BQSujWCaC2KBjy0B8rO3CeJS8hNLrFcSeY22v90PDrROxlUGvBPGr7e8HKm%2BGkiymwGnOcb31KRxNeenMnKjgBBM3z4yBA7jl9GGN44fezQkfJxsSAfGcbY5DByBCnIaei%2BASy%2F8qyf9f9N8441gV4%2FzUWKJQ8yynJNGXiuE9cJIoA9H0JQAC5yzj1gmPHyooC0G66nbazU77RLJ8SBcf2JV0%2FIwqSlsWqcu6VPTm9gBZTCAAvBFMxPtuCYlREoC2pOl%2FBDQv7tnIKaARYnjMgztUvEjfH8RHWFJ1YYveLQkSpcw3gqPh%2BE7IMEMmMtu7KYN2SxWdZSGMcbwjbN4ygsudMRmEOMOfJW4NutD0VTnjS53HFPLkOY6Wy0TOnLN1wPKHsTV%2FFZohW9Gn31Q0JQU0q5EnuoVzXGzfKdMhHyS1ZcYt2dJX9BBCFh8O4h%2FpqygOi6DR4zvnXk8FS51zILEKY%2BWmeJC0kXg3F9zS7TjWB4DeMl%2BUwqa0HT8xQb6QtgOouvZhh6kjkj9SJ%2F5U1eoFJcOeno%2FHVSeFrNlXey7IW%2B9aqFfuqhMmf2rK6YAEuP92oxMIzO98kGOqUBF7hQVBYnfVkOwSiUpZNtBt5N270qbGD6T8Y0maWQ1cAt%2Bl9aNiXf2rG7OFkl14hw5FFXcWtxyp25SRNDwHwZPUswy3r05Fk0qHVkf%2BwpRz0cDJfWR2naj%2FGkSOpyYNOJF2nAeAbgpbmeX1JWNTbThzk0TUddQr8m5DLGsf9MTF4W3P%2BX83IRU%2FPOdA1751RLzVGyOgu1XBqqq5jkPYvC8Xqgq3QF&X-Amz-Signature=ff642154078626f2cb1be5579585f885f350b1fdf180d715a5d175b6e5680333&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
---
**Left join**
As we already learned, the left-join is the default join method. Thus, when we want to do a left join we don’t have to specify the `how=` parameter.
```python
teams_players_new.join(teams_goals_new, lsuffix='_left', rsuffix='_right')
```
![Joined DataFrame `teams_players_new` & `teams_goals_new`](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/1059a0f9-71b6-4c0e-9ce9-154e1334b735/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662622DKCH%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T222558Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIQDoEPhxIPC89rphPZxBfriCDeyoBDrZ4BqAulmTb82m5QIgex3B3Zw52EkLXdkO2AZy0mRl6e3PH6%2B4XWnR%2FE7tDZcq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDGmjcwKLPCQF%2BnPghSrcAzQJF0kGU4Bl45mGl1VJMEsADq8kbDiysQQCJ6gcIL7B5266Hf1gb%2FHS67sBoQxjv%2BRjjOiLeZDhVyjxEu6M6NKME7TPH%2BQLJoz20psbxgoYQV%2BB5%2FCHM77n5bpkevmJIP9gYhgOAJzyf1haSugtnGk%2BjP6jAFSoREEeslfdIjZeQX5Trf0g9fhiSS5QJoU4wPi3kFCZM5ZBykeqGQiTGXhtDkQxnlc5W%2BXnrd4EM855exU7%2BOQa4CqSV%2B8nlL4iI5skllho%2FSYjnYdBWLhNsreJxX9%2FBkI1%2BVxC5mRHHg1%2FfAmruMuW%2BZLT%2FdTd0cIVwFt8Nspj3gmYorzEqPX4Sz3MZXXPDaUE3EOGY8vUBc8Cw2AsjRR5jGnwe8yiHPVUeCohZ8UpVd%2B1nwpJ%2FvkqapqYyO2Ja%2Bt6rZWARhcOV7PoFIU1cglB01GoBGbQUx0Z0Lt145iRQHSa%2F3C26QVSlbAoiidfLHnDy3tMyTf%2Bw2dZXvl4jX9aFoim5X5%2BjdR%2FYpM8k0%2FKbZEH1h1bI5rsSX%2BK8XdcRJSrTuV0E0viiCqPB3PEnmcU5BH5b5r6yx5u%2F4qQyAiryP%2FCo34ydsmJZV4CnVMckeKKDGheS%2ByKv0UUxoMCdO0rEYHbygKYMN3O98kGOqUBxsCDHxhVk5gs9cwP%2Fk0mNA7qfhnC%2FVG9dVyGYLlgoKJ8eBPyp9nr6QbWILvtsTeTltLmcTc%2F2Jbd6S3r7hNg1doxM4L86tIjnMmnN%2B0UmCayc0g%2B%2Fqi0hxNhg%2FY7zU5%2BxLaIyh0sPYmRZOzk6rAH4MXq0%2BH8r%2BL7WmBxIzx7Mmv7zb%2Fq7skntDzU1oKg84AAqWTKL61YFyJeheNEXWK3%2FKH5phr1&X-Amz-Signature=e70b5b1081cfb49646745d8c8307b39a75167896f1d5aaa20632b4bd262681fc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
In the output DataFrame we can observe that the indices 0 and 11 are still missing - why? These indices are present in the right DataFrame but not in the left one and thus no overlapping indices are found for these two rows. Since we are doing a left-join, these two rows are excluded from the output.
Also we see that for two rows there are some `NaN` values - why?
These rows, indices 2 and 12 are included in the left DataFrame but not in the right DataFrame. Since we are doing a left-join the rows are not excluded from the output, instead `NaN` is inserted in the cells where no data could be found in the right DataFrame for these two rows.
---
**Right join**
We can perform a right-join with the following command.
```python
teams_players_new.join(teams_goals_new, how='right', lsuffix='_left', rsuffix='_right')
```
![Joined DataFrame `teams_players_new` & `teams_goals_new`](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/033050c2-1732-452b-ac1e-177ed308e54d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662622DKCH%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T222559Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIQDoEPhxIPC89rphPZxBfriCDeyoBDrZ4BqAulmTb82m5QIgex3B3Zw52EkLXdkO2AZy0mRl6e3PH6%2B4XWnR%2FE7tDZcq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDGmjcwKLPCQF%2BnPghSrcAzQJF0kGU4Bl45mGl1VJMEsADq8kbDiysQQCJ6gcIL7B5266Hf1gb%2FHS67sBoQxjv%2BRjjOiLeZDhVyjxEu6M6NKME7TPH%2BQLJoz20psbxgoYQV%2BB5%2FCHM77n5bpkevmJIP9gYhgOAJzyf1haSugtnGk%2BjP6jAFSoREEeslfdIjZeQX5Trf0g9fhiSS5QJoU4wPi3kFCZM5ZBykeqGQiTGXhtDkQxnlc5W%2BXnrd4EM855exU7%2BOQa4CqSV%2B8nlL4iI5skllho%2FSYjnYdBWLhNsreJxX9%2FBkI1%2BVxC5mRHHg1%2FfAmruMuW%2BZLT%2FdTd0cIVwFt8Nspj3gmYorzEqPX4Sz3MZXXPDaUE3EOGY8vUBc8Cw2AsjRR5jGnwe8yiHPVUeCohZ8UpVd%2B1nwpJ%2FvkqapqYyO2Ja%2Bt6rZWARhcOV7PoFIU1cglB01GoBGbQUx0Z0Lt145iRQHSa%2F3C26QVSlbAoiidfLHnDy3tMyTf%2Bw2dZXvl4jX9aFoim5X5%2BjdR%2FYpM8k0%2FKbZEH1h1bI5rsSX%2BK8XdcRJSrTuV0E0viiCqPB3PEnmcU5BH5b5r6yx5u%2F4qQyAiryP%2FCo34ydsmJZV4CnVMckeKKDGheS%2ByKv0UUxoMCdO0rEYHbygKYMN3O98kGOqUBxsCDHxhVk5gs9cwP%2Fk0mNA7qfhnC%2FVG9dVyGYLlgoKJ8eBPyp9nr6QbWILvtsTeTltLmcTc%2F2Jbd6S3r7hNg1doxM4L86tIjnMmnN%2B0UmCayc0g%2B%2Fqi0hxNhg%2FY7zU5%2BxLaIyh0sPYmRZOzk6rAH4MXq0%2BH8r%2BL7WmBxIzx7Mmv7zb%2Fq7skntDzU1oKg84AAqWTKL61YFyJeheNEXWK3%2FKH5phr1&X-Amz-Signature=98baaf89cb9464433e201e08d7c30998fcafaee29b7bdd351e6419f63e86f2a0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
We can again observe that some indices are missing, 2 and 12 specifically. It’s the same concept as in the previous example: These indices are present in the left DataFrame but not in the right DataFrame and since we are doing a right-join these two rows are excluded.
And missing data cells are again filled with `NaN` values. This affects the rows that are present in the right DataFrame but not in the left DataFrame and are not excluded from the output as we are doing a right-join.
---
**Outer join**
We can perform an outer-join with the following command. 
```python
teams_players_new.join(teams_goals_new, how='outer', lsuffix='_left', rsuffix='_right')
```
![Joined DataFrame `teams_players_new` & `teams_goals_new`](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/a52156c7-c866-4fd1-ab19-6e21622433bb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662622DKCH%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T222558Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIQDoEPhxIPC89rphPZxBfriCDeyoBDrZ4BqAulmTb82m5QIgex3B3Zw52EkLXdkO2AZy0mRl6e3PH6%2B4XWnR%2FE7tDZcq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDGmjcwKLPCQF%2BnPghSrcAzQJF0kGU4Bl45mGl1VJMEsADq8kbDiysQQCJ6gcIL7B5266Hf1gb%2FHS67sBoQxjv%2BRjjOiLeZDhVyjxEu6M6NKME7TPH%2BQLJoz20psbxgoYQV%2BB5%2FCHM77n5bpkevmJIP9gYhgOAJzyf1haSugtnGk%2BjP6jAFSoREEeslfdIjZeQX5Trf0g9fhiSS5QJoU4wPi3kFCZM5ZBykeqGQiTGXhtDkQxnlc5W%2BXnrd4EM855exU7%2BOQa4CqSV%2B8nlL4iI5skllho%2FSYjnYdBWLhNsreJxX9%2FBkI1%2BVxC5mRHHg1%2FfAmruMuW%2BZLT%2FdTd0cIVwFt8Nspj3gmYorzEqPX4Sz3MZXXPDaUE3EOGY8vUBc8Cw2AsjRR5jGnwe8yiHPVUeCohZ8UpVd%2B1nwpJ%2FvkqapqYyO2Ja%2Bt6rZWARhcOV7PoFIU1cglB01GoBGbQUx0Z0Lt145iRQHSa%2F3C26QVSlbAoiidfLHnDy3tMyTf%2Bw2dZXvl4jX9aFoim5X5%2BjdR%2FYpM8k0%2FKbZEH1h1bI5rsSX%2BK8XdcRJSrTuV0E0viiCqPB3PEnmcU5BH5b5r6yx5u%2F4qQyAiryP%2FCo34ydsmJZV4CnVMckeKKDGheS%2ByKv0UUxoMCdO0rEYHbygKYMN3O98kGOqUBxsCDHxhVk5gs9cwP%2Fk0mNA7qfhnC%2FVG9dVyGYLlgoKJ8eBPyp9nr6QbWILvtsTeTltLmcTc%2F2Jbd6S3r7hNg1doxM4L86tIjnMmnN%2B0UmCayc0g%2B%2Fqi0hxNhg%2FY7zU5%2BxLaIyh0sPYmRZOzk6rAH4MXq0%2BH8r%2BL7WmBxIzx7Mmv7zb%2Fq7skntDzU1oKg84AAqWTKL61YFyJeheNEXWK3%2FKH5phr1&X-Amz-Signature=a9427134058c4d749640122eccdee488b848eef11550fae81a89272861c08c87&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
We can observe that no indices are missing, from 0 to 19, all are there. This is because we did an outer join in which we take combine all rows from both DataFrames, regardless if there are overlapping or missing rows. 
Wherever data is missing, the usual `NaN` values are inserted. We can see now that the outer-join is just a combination of the left- and right-join.
---
## [`.count()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.count.html)
---
**Syntax**
With this function we can count the number of non-`NaN` values for each column or row in a DataFrame. So if we are interested in how many cells do actually contain valid data, we can use this function. The syntax is pretty simple:
`df.count( << axis >> )`
The `<< axis >>` parameter works as follow: 
- `axis = 0` → counts non-`NaN` values per column
- `axis = 1` → counts non-`NaN` per row
---
**Count non-****`NaN`**** values per column**
Let’s assume we have the following DataFrame `outer_merge_df`:
![outer_merge_df](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/2431d095-7483-492f-b1ec-5fe0a2250ea9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WV34OUJT%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T222602Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIQDMByBbngjfCcT%2BbP3JqhJFsH7DP5Z55oHopT7zey42hwIgYGvj1tJUu5Pb1xPjDosH8UE472ikCbRcEwxOMdwwPGoq%2FwMIKBAAGgw2Mzc0MjMxODM4MDUiDCpWFScxsR3N8DhMjyrcA4YfQbPhBIThpVOcyt6EVXQSEYrBtboFnLR2UDHkMIN%2FF9udCbWhlBOx%2FF0Ap88z5itPPW73TgGgzvS0uyDVWj47yuB124nD2xMLUd7inHpjfdmWJWQLZxlGiQmxn%2BKL8jXn%2BXa2cC28ximYJd7Wfoi1Eb%2BuqXosT%2FVrybHY%2BmBd3vBt%2FU8Zr69o7F8jOeGULWtYylyCcMivXYXEJakcCs1pZiB9TFqOYGdJhjySj2U4Blswi4znIv54JHB4ws%2Ft4jcNrceZ%2BO39jQ8qhHribAC2HHRG1QgFU%2FJ9F3tOx%2BL6Jho9%2B7fu%2FIZKilJC6GeRZ%2FRAeOE7TVC%2FBmb%2B2gP5It9KANhka23W%2FiWYpi1mWZBFRD0C%2F0%2BPzTXG18cCOe%2BIorqmWd5lcshTa%2FyWbOdZZOOqS5aDhFAfNp6s0mZTsFvRm4qbC8L57TN%2F3gBBpTAIFoA%2BqEp18JLkYOe%2FtIVYsOBzv6aeyt%2Fh5tr556vTcApvfHXhQ7G%2B3KssuwNdhtnJs%2BzqMqFvnNhVoC%2Fa7AxzrrCiouSbseLj3twlFimPMypjLbIOzgX54%2FIyhSZMSrEV9bRmfI9KAg3JwjvMaw%2BqhZHBnEfGT1hAvjTsUSLcSN98g4UVY8SWwDJY6qOPMJrP98kGOqUBKj62O6Vjqg3UJem7jogtObpoYj3PG4wpgeDq6zP8J5xWB6lsIJESR0DJ7RvKxMjf4TlO1OUzvqbqxsyevu2b5geqMo3r46Xcu%2BVo6K07LlK3aBHV7ggAE0Z2OZNv5rzZ0y1LljVf94uD2EajFim%2FpPoplOarF5L297i4mc1RLwCjCF%2BHetp3lhKXVMzgjT4QGt1qbCE%2FaeeT0vAqIBAOFUL1bvV9&X-Amz-Signature=1b592d4d31a4ae0684d240f602712eac7775f0b12a0acf11a5fea44a25d09883&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
If we want to count now the non-NaN values for each of the three columns we can execute the following command:
```python
outer_merge_df.count(axis=0)

Team                 20
Total team goals     18
Number of players    18
dtype: int64
```
We can see that for each column we see now how many non-`NaN` values there are.
In the first column Team there is valid data only → 20 non-`NaN` values
In the second and third column there is two times the value `NaN`  → 18 non-`NaN` values
---
**Count non-****`NaN`**** values per row**
To count the non-NaN values per rows we simply must change the axis parameter:
```python
outer_merge_df.count(axis=1)

0     2
1     3
2     3
3     3
4     2
5     3
6     3
7     3
8     3
9     3
10    3
11    3
12    3
13    3
14    3
15    3
16    3
17    3
18    2
19    2
dtype: int64
```
From the output we can see that nearly all rows have three non-`NaN` values and thus no `NaN` value (there are three columns in total). Row 0, 4, 18 and 19 however, have only two non-`NaN` values as all of them have one `NaN` value.

---
## [`.copy()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.copy.html)
---
**Syntax**
With this function we can create a copy of an existing DataFrame or Series.
`df.copy()`
---
**Copying a DataFrame**
Let’s assume we have the following DataFrame `df`:
![df](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/e2a194f9-0d78-4736-836b-59261da98028/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664UV7AMQX%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T222603Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQCR2Kgb10r55KZeKIE0dXIn0ZM9A90k0K347Dc2zqA7bQIhAOgV8mmzfOnHh3D3ICLyaswBhMbVgDMK43BYnsssBaFSKv8DCCcQABoMNjM3NDIzMTgzODA1Igwe2rndaMcpussl1nYq3ANmtAljUjN17jlkk7ptmXL%2FvdygA6%2BeyLDxbN01jSXQUGnZLarJeOme0oL%2Bt3x90RqWFwKPdvEIcFGbmQ%2FFkbJv68yAx36ZflVUFw5Oy4uQ%2Bjyi%2FDbpriUGECf8pMQKjqUtSdTGlaiFfosVfXVOv5PWRptI%2BbBGJAPnLgyd%2F29zs47KVp9XWab2TsNbZEP7Ue%2BxPoqWm%2FsMYB8ScghYHvnAe%2BVuw1EeBvJYFEyFBCRF3uISDTmg1ym5GyM1s1HocxISYv5nwyhI1r5fRGa6KKynT%2F1sfaCG77PgGCeF8G2q4uDFrM7Z3sEDI9RNzMsXqrBz93P2zCyBI9v9rFRmw8IztOJCfEXHP8Su587x8ra1RdHdkB5NGFDsBBOSIMXYS7PYPAhg6sQZ3Xt4CKFKnEh7H9WrxpdFEjpdc2BPBcXLaFRr9KoFJKHnmVdAeGgl5KzD3iFNMa0HIYf3u1XY03Osu%2FDBBm5aIjRsA3RYvCRKoTKNUXDP0UVwzZ%2B25vEMfDyfQciJ8FIdiXUTO0My1RYZQ%2Fh6SldSVZnlLPR8Z9R%2BfQyft%2BlbE6%2BPoa45NJKlJLR5jKfM2gibw%2B7ePDaQ5BXNJYE7qnNlUsbxUq43YJAt%2Fh7WkCR%2BrYEdqZ8doTDlzffJBjqkASVEDpRb3SlMI6kaXRtOaJ3KbWJWkZS8XpSOurlSX5XE3GR8m4wPJQ%2BoJSFtRq4R9GlbjgEz0Be4VznxNZAxgVQSQ%2F8OhAjnU458NComrxHjPYPvi9MAuq4Zv14P8w2vQpvM%2Bp7Hbcqkdsyge%2Fe7ZHTtqYi5RlymSX1KSQqPc99m%2F%2F81p%2FWbTygmGOIwgV1RBw5%2B7h3fjbC2oOlrXgrm%2FYJIb0DW&X-Amz-Signature=6d0bea641f55e73fd06f770de6f8425054125202ef6aabf1c908553f21c9db9e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
If we now want to create a second version of this DataFrame and store it in a new variable `df_2`, we can simply create a copy of `df`.
```python
df_2 = df.copy()

df_2
```
![df_2](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/25b4b04b-4667-48fd-8a2d-1d13102917f8/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664UV7AMQX%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T222603Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQCR2Kgb10r55KZeKIE0dXIn0ZM9A90k0K347Dc2zqA7bQIhAOgV8mmzfOnHh3D3ICLyaswBhMbVgDMK43BYnsssBaFSKv8DCCcQABoMNjM3NDIzMTgzODA1Igwe2rndaMcpussl1nYq3ANmtAljUjN17jlkk7ptmXL%2FvdygA6%2BeyLDxbN01jSXQUGnZLarJeOme0oL%2Bt3x90RqWFwKPdvEIcFGbmQ%2FFkbJv68yAx36ZflVUFw5Oy4uQ%2Bjyi%2FDbpriUGECf8pMQKjqUtSdTGlaiFfosVfXVOv5PWRptI%2BbBGJAPnLgyd%2F29zs47KVp9XWab2TsNbZEP7Ue%2BxPoqWm%2FsMYB8ScghYHvnAe%2BVuw1EeBvJYFEyFBCRF3uISDTmg1ym5GyM1s1HocxISYv5nwyhI1r5fRGa6KKynT%2F1sfaCG77PgGCeF8G2q4uDFrM7Z3sEDI9RNzMsXqrBz93P2zCyBI9v9rFRmw8IztOJCfEXHP8Su587x8ra1RdHdkB5NGFDsBBOSIMXYS7PYPAhg6sQZ3Xt4CKFKnEh7H9WrxpdFEjpdc2BPBcXLaFRr9KoFJKHnmVdAeGgl5KzD3iFNMa0HIYf3u1XY03Osu%2FDBBm5aIjRsA3RYvCRKoTKNUXDP0UVwzZ%2B25vEMfDyfQciJ8FIdiXUTO0My1RYZQ%2Fh6SldSVZnlLPR8Z9R%2BfQyft%2BlbE6%2BPoa45NJKlJLR5jKfM2gibw%2B7ePDaQ5BXNJYE7qnNlUsbxUq43YJAt%2Fh7WkCR%2BrYEdqZ8doTDlzffJBjqkASVEDpRb3SlMI6kaXRtOaJ3KbWJWkZS8XpSOurlSX5XE3GR8m4wPJQ%2BoJSFtRq4R9GlbjgEz0Be4VznxNZAxgVQSQ%2F8OhAjnU458NComrxHjPYPvi9MAuq4Zv14P8w2vQpvM%2Bp7Hbcqkdsyge%2Fe7ZHTtqYi5RlymSX1KSQqPc99m%2F%2F81p%2FWbTygmGOIwgV1RBw5%2B7h3fjbC2oOlrXgrm%2FYJIb0DW&X-Amz-Signature=bbf8e190759f282ef9f62040ed6cf9566346bf94b4c7743cccea02ad65944272&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
---
**`.copy()`**** vs. ****`=`**
If we had used the assignment operator (`=`) instead of `.copy()`, a new DataFrame would not have been created. In this case, the variable `df_2` would simply be pointing to the same DataFrame as the variable df.
Let’s assume we try to copy the DataFrame `df` this time like this:
```python
df_2 = df
```
And now we drop one row from `d2`, which *we think* *shouldn’t* affect the DataFrame stored in `df_2`.
```python
df.drop(6, axis=0, inplace=True)

df
```
![df](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/cedfaef2-c0a6-48ee-b82e-0aba216bca06/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664UV7AMQX%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T222603Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQCR2Kgb10r55KZeKIE0dXIn0ZM9A90k0K347Dc2zqA7bQIhAOgV8mmzfOnHh3D3ICLyaswBhMbVgDMK43BYnsssBaFSKv8DCCcQABoMNjM3NDIzMTgzODA1Igwe2rndaMcpussl1nYq3ANmtAljUjN17jlkk7ptmXL%2FvdygA6%2BeyLDxbN01jSXQUGnZLarJeOme0oL%2Bt3x90RqWFwKPdvEIcFGbmQ%2FFkbJv68yAx36ZflVUFw5Oy4uQ%2Bjyi%2FDbpriUGECf8pMQKjqUtSdTGlaiFfosVfXVOv5PWRptI%2BbBGJAPnLgyd%2F29zs47KVp9XWab2TsNbZEP7Ue%2BxPoqWm%2FsMYB8ScghYHvnAe%2BVuw1EeBvJYFEyFBCRF3uISDTmg1ym5GyM1s1HocxISYv5nwyhI1r5fRGa6KKynT%2F1sfaCG77PgGCeF8G2q4uDFrM7Z3sEDI9RNzMsXqrBz93P2zCyBI9v9rFRmw8IztOJCfEXHP8Su587x8ra1RdHdkB5NGFDsBBOSIMXYS7PYPAhg6sQZ3Xt4CKFKnEh7H9WrxpdFEjpdc2BPBcXLaFRr9KoFJKHnmVdAeGgl5KzD3iFNMa0HIYf3u1XY03Osu%2FDBBm5aIjRsA3RYvCRKoTKNUXDP0UVwzZ%2B25vEMfDyfQciJ8FIdiXUTO0My1RYZQ%2Fh6SldSVZnlLPR8Z9R%2BfQyft%2BlbE6%2BPoa45NJKlJLR5jKfM2gibw%2B7ePDaQ5BXNJYE7qnNlUsbxUq43YJAt%2Fh7WkCR%2BrYEdqZ8doTDlzffJBjqkASVEDpRb3SlMI6kaXRtOaJ3KbWJWkZS8XpSOurlSX5XE3GR8m4wPJQ%2BoJSFtRq4R9GlbjgEz0Be4VznxNZAxgVQSQ%2F8OhAjnU458NComrxHjPYPvi9MAuq4Zv14P8w2vQpvM%2Bp7Hbcqkdsyge%2Fe7ZHTtqYi5RlymSX1KSQqPc99m%2F%2F81p%2FWbTygmGOIwgV1RBw5%2B7h3fjbC2oOlrXgrm%2FYJIb0DW&X-Amz-Signature=72666944fdea8a7f73e3c5f96cf694574d5d6b50a25073272cfc4a40709482dc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
However, when we output now `df_2` we can see that row 6 was dropped fom this DataFrame as well. This is because no copy was created in the frist place, thus variables `df` and `df_2` are pointing to the same DataFrame.
![df_2](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/cedfaef2-c0a6-48ee-b82e-0aba216bca06/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664UV7AMQX%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T222603Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQCR2Kgb10r55KZeKIE0dXIn0ZM9A90k0K347Dc2zqA7bQIhAOgV8mmzfOnHh3D3ICLyaswBhMbVgDMK43BYnsssBaFSKv8DCCcQABoMNjM3NDIzMTgzODA1Igwe2rndaMcpussl1nYq3ANmtAljUjN17jlkk7ptmXL%2FvdygA6%2BeyLDxbN01jSXQUGnZLarJeOme0oL%2Bt3x90RqWFwKPdvEIcFGbmQ%2FFkbJv68yAx36ZflVUFw5Oy4uQ%2Bjyi%2FDbpriUGECf8pMQKjqUtSdTGlaiFfosVfXVOv5PWRptI%2BbBGJAPnLgyd%2F29zs47KVp9XWab2TsNbZEP7Ue%2BxPoqWm%2FsMYB8ScghYHvnAe%2BVuw1EeBvJYFEyFBCRF3uISDTmg1ym5GyM1s1HocxISYv5nwyhI1r5fRGa6KKynT%2F1sfaCG77PgGCeF8G2q4uDFrM7Z3sEDI9RNzMsXqrBz93P2zCyBI9v9rFRmw8IztOJCfEXHP8Su587x8ra1RdHdkB5NGFDsBBOSIMXYS7PYPAhg6sQZ3Xt4CKFKnEh7H9WrxpdFEjpdc2BPBcXLaFRr9KoFJKHnmVdAeGgl5KzD3iFNMa0HIYf3u1XY03Osu%2FDBBm5aIjRsA3RYvCRKoTKNUXDP0UVwzZ%2B25vEMfDyfQciJ8FIdiXUTO0My1RYZQ%2Fh6SldSVZnlLPR8Z9R%2BfQyft%2BlbE6%2BPoa45NJKlJLR5jKfM2gibw%2B7ePDaQ5BXNJYE7qnNlUsbxUq43YJAt%2Fh7WkCR%2BrYEdqZ8doTDlzffJBjqkASVEDpRb3SlMI6kaXRtOaJ3KbWJWkZS8XpSOurlSX5XE3GR8m4wPJQ%2BoJSFtRq4R9GlbjgEz0Be4VznxNZAxgVQSQ%2F8OhAjnU458NComrxHjPYPvi9MAuq4Zv14P8w2vQpvM%2Bp7Hbcqkdsyge%2Fe7ZHTtqYi5RlymSX1KSQqPc99m%2F%2F81p%2FWbTygmGOIwgV1RBw5%2B7h3fjbC2oOlrXgrm%2FYJIb0DW&X-Amz-Signature=72666944fdea8a7f73e3c5f96cf694574d5d6b50a25073272cfc4a40709482dc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
---
## [`.rename()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.rename.html)
---
**Syntax**
This function allows us to rename single column names in a DataFrame. Thy syntax is as follow:
`df.rename( << mapping dictionary >> , axis = <<axis>> , inplace = True)`
In the mapping dictionary we must map the old column names with the new ones. Because somehow Python must know what should be replaced with what.
Specifically, the structure of the `<< mapping dictionary >>` must be as follow:
```python
{
	old_label_1 : new_label_1,
	old_label_2 : new_label_2,
	old_label_3 : new_label_3,
	...,
	old_label_n : new_label_n
}
```
If we want to rename columns we must set axis = 1.
If we want to rename the index labels we must set axis = 0.
---
**Rename single columns**
Let’s assume we have our original DataFrame `players_df` and we want to rename the three last columns:
- total_points → Total points
- points_per_game → Points per game
- days_played → Days played
![players_df with old column labels](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/21964fa8-a672-418d-8f2d-f80e59e55bf3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662MTC77VA%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T222604Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIE2UqQWsvhDwa3zfxer8m8KM1ev6FomMb31SyG5HtBmbAiEA06gIZbKHRz9ky0dxHDyO%2FSK1rQwI6JoeMGbDeaT1PlAq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDHpP0BFDUbSoEXT4VCrcAzVk7kcX3OHv%2F6mmSkJaEIdX%2Fbq7YaysBDk5Q%2FG9zK1xcztGJ5sKaDayC31LOV%2BU6tDvuYurekFMe8FYxMIREPuld%2Bsc3lWcTcooLd6%2F%2B5YMDKWw2xuMdyqUibDwfNVvHXftLAfminRIl5yss4dDXXBvjmNm%2FXAs255fJDLMk9moqK68Mmtxq5Nn80y2AzC2jj3jrQTgx7nAuQC01EUKCoGPkiBe6zao6%2BbnvkSLqYSPXSajdLP9ew6dIcVAo%2B4iyYWisJSCbGaKy4EI7ocS2R2zxAfES%2BBVxAS7ATDImg754MQenDEz4EPU8Ein2N616Od3mO6aoz3Jlg2Q7XNoe7VjGk7Y%2BH6gUPU9lkSdbHCaxskxEKZ657wGW9FJz7maXf2TCs5PbU6HNyUYYIple6nJPbSEMx%2FjevHpn00Ja3JyabMZuyPO9Ux12%2FZ3i3%2FUh7jxHEC4l8sgyYthg4WTWgsHctW6RZPllvNs4dxxM1J2pQrjdqmAEUUFiaJYttg8hml%2FGQhE4J%2F7AGD%2BtuRwsPC%2BpEGsmHSWWJCWIE9RkylGpprSgcrY%2FNR08qr028Na%2FyFsZKKsyw%2BhPvY%2BEunTByd3Al2kQX2LGL7cpnRMJaj06%2F%2BCm2oLk1Rn0KxXMIXO98kGOqUBSwXSRegkh4z0Blzx5mvFnFLPjz8hJVVfFEZOukPR8idWsssFk5J%2B%2BwiRcDaub3siUk8ss%2F5AoyaCtyRHKtKUUzgQkXUwTic9yEgrSL5AAKmZAgl94h0%2FCWWAjkwGBtw0zPjkwg5CwNGkXRYtLRhI9cqLib%2FJC%2BXkhX%2FiAAH2f0d1xZMYLsVJJMIAVyy64XfK9sD0qqdXLwK%2FlgLRKp3%2B2P7E%2BN2N&X-Amz-Signature=26c7d95a1d96a8380276d119f53868af624b1f93570d580f9a9f87e3d235ceed&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
We can achieve that by running the following command:
```python
mapping_dict = {
		'total_points' : 'Total points',
		'points_per_game' : 'Points per game',
		'days_played' : 'Days played'
}

players_df.rename(mapping_dict, axis=1, inplace=True)
```
![playes_df with new column labels](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/c2cf77df-7b1d-4b9f-8a5c-aeeaaf7ae0bb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662MTC77VA%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T222604Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIE2UqQWsvhDwa3zfxer8m8KM1ev6FomMb31SyG5HtBmbAiEA06gIZbKHRz9ky0dxHDyO%2FSK1rQwI6JoeMGbDeaT1PlAq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDHpP0BFDUbSoEXT4VCrcAzVk7kcX3OHv%2F6mmSkJaEIdX%2Fbq7YaysBDk5Q%2FG9zK1xcztGJ5sKaDayC31LOV%2BU6tDvuYurekFMe8FYxMIREPuld%2Bsc3lWcTcooLd6%2F%2B5YMDKWw2xuMdyqUibDwfNVvHXftLAfminRIl5yss4dDXXBvjmNm%2FXAs255fJDLMk9moqK68Mmtxq5Nn80y2AzC2jj3jrQTgx7nAuQC01EUKCoGPkiBe6zao6%2BbnvkSLqYSPXSajdLP9ew6dIcVAo%2B4iyYWisJSCbGaKy4EI7ocS2R2zxAfES%2BBVxAS7ATDImg754MQenDEz4EPU8Ein2N616Od3mO6aoz3Jlg2Q7XNoe7VjGk7Y%2BH6gUPU9lkSdbHCaxskxEKZ657wGW9FJz7maXf2TCs5PbU6HNyUYYIple6nJPbSEMx%2FjevHpn00Ja3JyabMZuyPO9Ux12%2FZ3i3%2FUh7jxHEC4l8sgyYthg4WTWgsHctW6RZPllvNs4dxxM1J2pQrjdqmAEUUFiaJYttg8hml%2FGQhE4J%2F7AGD%2BtuRwsPC%2BpEGsmHSWWJCWIE9RkylGpprSgcrY%2FNR08qr028Na%2FyFsZKKsyw%2BhPvY%2BEunTByd3Al2kQX2LGL7cpnRMJaj06%2F%2BCm2oLk1Rn0KxXMIXO98kGOqUBSwXSRegkh4z0Blzx5mvFnFLPjz8hJVVfFEZOukPR8idWsssFk5J%2B%2BwiRcDaub3siUk8ss%2F5AoyaCtyRHKtKUUzgQkXUwTic9yEgrSL5AAKmZAgl94h0%2FCWWAjkwGBtw0zPjkwg5CwNGkXRYtLRhI9cqLib%2FJC%2BXkhX%2FiAAH2f0d1xZMYLsVJJMIAVyy64XfK9sD0qqdXLwK%2FlgLRKp3%2B2P7E%2BN2N&X-Amz-Signature=0682b04a897481507c6b1205181517ff2be70d33a020739e67dfab889a37b482&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
Another alternative is when renaming columns is to set the `columns=` parameter. Then we can get rid of the `axis=` parameter.
```python
mapping_dict = {
		'total_points' : 'Total points',
		'points_per_game' : 'Points per game',
		'days_played' : 'Days played'
}

players_df.rename(columns=mapping_dict, inplace=True)
```
---
**Rename single index labels**
Let’s assume we want to rename the index labels, i.e., the Rank, of the first, third and fifth player:
- 1 → Player One
- 3 → Player Three
- 5 → Player Five
![players_df with old index labels](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/25ecc7fb-79c8-400a-b6f6-a5555e6f1257/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662MTC77VA%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T222604Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIE2UqQWsvhDwa3zfxer8m8KM1ev6FomMb31SyG5HtBmbAiEA06gIZbKHRz9ky0dxHDyO%2FSK1rQwI6JoeMGbDeaT1PlAq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDHpP0BFDUbSoEXT4VCrcAzVk7kcX3OHv%2F6mmSkJaEIdX%2Fbq7YaysBDk5Q%2FG9zK1xcztGJ5sKaDayC31LOV%2BU6tDvuYurekFMe8FYxMIREPuld%2Bsc3lWcTcooLd6%2F%2B5YMDKWw2xuMdyqUibDwfNVvHXftLAfminRIl5yss4dDXXBvjmNm%2FXAs255fJDLMk9moqK68Mmtxq5Nn80y2AzC2jj3jrQTgx7nAuQC01EUKCoGPkiBe6zao6%2BbnvkSLqYSPXSajdLP9ew6dIcVAo%2B4iyYWisJSCbGaKy4EI7ocS2R2zxAfES%2BBVxAS7ATDImg754MQenDEz4EPU8Ein2N616Od3mO6aoz3Jlg2Q7XNoe7VjGk7Y%2BH6gUPU9lkSdbHCaxskxEKZ657wGW9FJz7maXf2TCs5PbU6HNyUYYIple6nJPbSEMx%2FjevHpn00Ja3JyabMZuyPO9Ux12%2FZ3i3%2FUh7jxHEC4l8sgyYthg4WTWgsHctW6RZPllvNs4dxxM1J2pQrjdqmAEUUFiaJYttg8hml%2FGQhE4J%2F7AGD%2BtuRwsPC%2BpEGsmHSWWJCWIE9RkylGpprSgcrY%2FNR08qr028Na%2FyFsZKKsyw%2BhPvY%2BEunTByd3Al2kQX2LGL7cpnRMJaj06%2F%2BCm2oLk1Rn0KxXMIXO98kGOqUBSwXSRegkh4z0Blzx5mvFnFLPjz8hJVVfFEZOukPR8idWsssFk5J%2B%2BwiRcDaub3siUk8ss%2F5AoyaCtyRHKtKUUzgQkXUwTic9yEgrSL5AAKmZAgl94h0%2FCWWAjkwGBtw0zPjkwg5CwNGkXRYtLRhI9cqLib%2FJC%2BXkhX%2FiAAH2f0d1xZMYLsVJJMIAVyy64XfK9sD0qqdXLwK%2FlgLRKp3%2B2P7E%2BN2N&X-Amz-Signature=f61cbe03131dc71b33aab5cbd76256c8f24a352e9ac9d7a47b7e6afe382db7c8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
We can achieve that by running the following command:
```python
mapping_dict = {
		1 : 'Player One',
		3 : 'Player Three',
		5 : 'Player Five'
}

players_df.rename(mapper=mapping_dict, axis=0, inplace=True)
```
![players_df with new index labels](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/7717e680-7d76-46c6-8103-047a0ed4deb6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662MTC77VA%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T222604Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIE2UqQWsvhDwa3zfxer8m8KM1ev6FomMb31SyG5HtBmbAiEA06gIZbKHRz9ky0dxHDyO%2FSK1rQwI6JoeMGbDeaT1PlAq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDHpP0BFDUbSoEXT4VCrcAzVk7kcX3OHv%2F6mmSkJaEIdX%2Fbq7YaysBDk5Q%2FG9zK1xcztGJ5sKaDayC31LOV%2BU6tDvuYurekFMe8FYxMIREPuld%2Bsc3lWcTcooLd6%2F%2B5YMDKWw2xuMdyqUibDwfNVvHXftLAfminRIl5yss4dDXXBvjmNm%2FXAs255fJDLMk9moqK68Mmtxq5Nn80y2AzC2jj3jrQTgx7nAuQC01EUKCoGPkiBe6zao6%2BbnvkSLqYSPXSajdLP9ew6dIcVAo%2B4iyYWisJSCbGaKy4EI7ocS2R2zxAfES%2BBVxAS7ATDImg754MQenDEz4EPU8Ein2N616Od3mO6aoz3Jlg2Q7XNoe7VjGk7Y%2BH6gUPU9lkSdbHCaxskxEKZ657wGW9FJz7maXf2TCs5PbU6HNyUYYIple6nJPbSEMx%2FjevHpn00Ja3JyabMZuyPO9Ux12%2FZ3i3%2FUh7jxHEC4l8sgyYthg4WTWgsHctW6RZPllvNs4dxxM1J2pQrjdqmAEUUFiaJYttg8hml%2FGQhE4J%2F7AGD%2BtuRwsPC%2BpEGsmHSWWJCWIE9RkylGpprSgcrY%2FNR08qr028Na%2FyFsZKKsyw%2BhPvY%2BEunTByd3Al2kQX2LGL7cpnRMJaj06%2F%2BCm2oLk1Rn0KxXMIXO98kGOqUBSwXSRegkh4z0Blzx5mvFnFLPjz8hJVVfFEZOukPR8idWsssFk5J%2B%2BwiRcDaub3siUk8ss%2F5AoyaCtyRHKtKUUzgQkXUwTic9yEgrSL5AAKmZAgl94h0%2FCWWAjkwGBtw0zPjkwg5CwNGkXRYtLRhI9cqLib%2FJC%2BXkhX%2FiAAH2f0d1xZMYLsVJJMIAVyy64XfK9sD0qqdXLwK%2FlgLRKp3%2B2P7E%2BN2N&X-Amz-Signature=3f78184249a022705080dcf7c7147d1bc6d9589063f25165efa366d2ba473310&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
---
**Difference between ****`.rename()`**** and ****`.index`**** and ****`.columns`**
You may recall that we already covered renaming column names over the .columns attribute. And this is in fact also a valid alternative to `.rename()` function.
However, the important difference is that when renaming column or index labels using `.columns` / `.index` we must provide values for all columns / rows and not only for those we want to rename. 
If we try to change the column names as we did before over the `.columns` attribute, we receive an error:
```python
players_df.columns = ['Total points', 'Points per game', 'Days played']

ValueError: Length mismatch: Expected axis has 12 elements, new values have 3 elements
```
With this `ValueError`, Python tells us that there are 12 columns in the DataFrame and that we provided only three values in the list, so Python does not know what to do with the other nine columns. 
And this is the power of `.rename()` as it allows us to rename specific columns and index labels, which is very powerful, especially when we have DataFrames with hundreds of columns and thousand of rows. Then it would be very cumbersome to type down again all other 99 column names that we don’t even want to change.
---
## [`.sum()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sum.html)
---
**Syntax**
This method allows us to calculate the sum for all columns / rows in a DataFrame or for a single column / row.
`df.sum( << axis >> )`
To calculate the sum per row we must use `axis = 1`
To calculate the sum per column we must use `axis = 0`
**OR**
`df[ << some column or row >> ].sum()`
---
**Calculate sum for all rows / columns**
To calculate the sum for each row in the DataFrame we can use the following command.
```python
players_df.sum(axis=1)

Rank
1      3245
2      3010
3      3346
4      2850
5      3134
       ... 
536       0
537       0
538     142
539       0
540       0
Length: 540, dtype: int64
```
And for columns we just have to change `axis=` to `0`.
```python
players_df.sum(axis=0)

Player            Jamie VardyDanny IngsPierre-Emerick Aubameyang...
Team              Leicester CitySouthamptonArsenalManchester Cit...
Games played                                                  10252
Games started                                                  8149
Minutes played                                               730975
Goals                                                           986
Assists                                                         689
Shots                                                          6659
Shots on goal                                                  3191
dtype: object
```
We can see that Pandas also tries to calculate a sum for those columns that contain text data such as Player or Team. If we want to prevent this from happening, we can simply set `numeric_only=` to `True`.
```python
players_df.sum(axis=0, numeric_only=True)

Games played       10252
Games started       8149
Minutes played    730975
Goals                986
Assists              689
Shots               6659
Shots on goal       3191
dtype: int64
```
---
**Calculate sum for specific column / row**
If we want to calculate the sum only for a specific row or column, we can simply select this row or column first and then call the `sum()` function.
```python
players_df['Goals'].sum()

986
```
If we want to calculate a sum for a single row that contains text data as well (such as the player name), the this will fail. 
```python
players_df.iloc[4].sum()

TypeError: can only concatenate str (not "numpy.int64") to str
```
This error is thrown because Pandas is not able to count strings with numbers together. But then why was it possible before when we calculated the sum for all rows? Because for a `DataFrame` this is possible, i.e., Pandas is able to skip text values, but when applying the `.sum()` function on a `Series` (which is returned as we have selected a single row) then Pandas fails.
So we must exclude the columns with text data first in the selector and then we can also calculate the sum for a single row.
```python
players_df.iloc[4, 2:].sum()

3134
```
---
## [`.max()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.max.html)
---
**Syntax**
With this function we can find out the highest value in a specific column in a DataFrame.
`df[ << some column >> ].max()`
---
**Find highest numerical value**
Let’s assume we are interested in the highest number of goals a player scored.
```python
players_df['Goals'].max()

23
```
And how can we find out the name of the player with the most goals? We can use `.loc[]` again as we can put in a boolean condition into the selector.
```python
players_df.loc[players_df['Goals'] == players_df['Goals'].max(), 'Player']

79    Jamie Vardy
Name: Player, dtype: object
```
---
**Find highest alphabetic value**
We can also use `.max()` to find the word in a column that comes last in the alphabet. Let’s assume we want to find the team name that comes last in the alphabet.
```python
players_df['Team'].max()

'Wolverhampton Wanderers'
```
---
## [`.idxmax()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.idxmax.html)
---
**Syntax**
This function allows us to get the index label or the column name of the highest numerical value in the column or in the row. The syntax is as follow:
`df.idxmax( << axis >> ) `
The difference between the values for `<< axis >>` parameter is the following:
| `axis=0` | `axis=1` |
| --- | --- |
| For each column, the index label of the row with the highest value is returned | For each row, the column name with the highest value is returned |
---
**Get index labels for highest value in columns**
Let’s assume we have again the DataFrame `outer_merge_df` with the column `Player` set as the index column.
![outer_merge_df](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/c09b5108-a06d-464d-9777-48fd059e0031/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XMYQ3PCA%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T222607Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIB6liCZN4BfLIKHK4Vq1fuqDN4mxMzoTVDFxsxJkulRHAiEA%2FTYo8vhjO5Qjvtbm8JaF5BfQqHxPQZeUeRFymZJA4asq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDLjwZnsej7bq6rYrzCrcAzI5Xh%2BnBXCvAUMrm%2FLMlgwk8GYvd7dGZOo3BB0Erq68XzB%2FkynxyV6FjEwOTtBIAPvYXGhUJ0RYLUheaxDo7RPMl9pbk4d49dbJcSvzpY62robhp9setxdLc2FZh5jMVg3OQE6jgDoVWvLDzhefTyLcNvTvvxXYVgC7CBzkTlJh7FctrZyK%2BBBv75SZLWvH047CH%2F8ALbN7NfCf2kuXuoZyHp8nEheJ95Rz7SJu743XUitUM4TUMdZibqzJHLwmp45A0x%2Fp13LLIBsQFzN2FsJS9brwo4OUB5jjrCcGNM11YPFdeuOxPvAUSbPbccQzup%2FsIcEY%2FstCLhZYjHAiq8T6652%2F0zQjVBYlOYR4Yqh4TXm%2F%2BXkGc0uXObiiDx5qL8giKGnLPf%2BQfomDai2hxXmNxw6kD584hjCt0898VPmapbUfKXkihiuS1ODNl0yxJqCnp33x5ygui5VQdRfjD%2FwhBA4D4ivAMX%2Flc7KfC9C16tV7lH5nJDTPU4fcdxaUnejdBEJsRsD%2FosQs8UHbOyJVC7Q8Tni7w4JMWhA%2BBtpI6fQnA3vpwHe%2FaT5iFADRViY4StVE%2FqTVoYGcoJqoTLmeIDZ4Kmr0FDQQyL8JoZHvohK9aNqmD2%2B37QioMMXO98kGOqUBOh1gKy2q8aAnOaL9ydQyRGf1glt8Ic%2BIFbYPKYCvbVNVN0b9%2FDXcS%2Fg7Khry9dJAuo42M6GlM56GQqACLOPnNNfhG4ZhbQxdARxGv545HsZ%2BtD9W%2FZ%2BX2Sf4zkOIQjcZ9kKrjsiWoBMvRE7jsbs%2BmSOB%2Fvt%2Ffcuc40EP%2B2X0ZSfJr4mmXGM57JjJdotR9facb7WcIzrNoxRV30IwQn5K%2F1SNNnqm&X-Amz-Signature=083d1bae28a66d5d7e352a1e2581094087a4c65f52560d6627e43d914a534277&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
To find out the team with the highest team goals and the highest number of players, we can run the following command:
```python
outer_merge_df.idxmax(axis=0)

Total team goals      Manchester City
Number of players    Newcastle United
dtype: object
```
We can see that Manchester City is the team with the highest goals and Newcastle United the team with the highest number of players.
---
**Get index label of highest value in single column**
We can also use `.idxmax()` on a single column. Thus, to find out the name of the team that scored the highest goals only, we can run the following command:
```python
outer_merge_df['Total team goals'].idxmax()

'Manchester City'
```
This is especially useful when we have a large dataset that is not sorted and we want to quickly find out the index label that corresponds to a maximum value in a column.
---
**Get column name for highest value in each row**
To find out for each team whether their number of goals scored or number of players is higher we can run the following command:
```python
outer_merge_df.idxmax(axis=1)

### OUTPUT ###
Team
Manchester City              Total team goals
Liverpool                    Total team goals
Manchester United            Total team goals
Leicester City               Total team goals
Arsenal                      Total team goals
Tottenham Hotspur            Total team goals
Southampton                  Total team goals
West Ham United              Total team goals
Wolverhampton Wanderers      Total team goals
Everton                      Total team goals
Aston Villa                  Total team goals
Bournemouth                  Total team goals
Newcastle United             Total team goals
Sheffield United             Total team goals
Watford                      Total team goals
Brighton and Hove Albion     Total team goals
Crystal Palace               Total team goals
Norwich City                 Total team goals
Chelsea                     Number of players
Burnley                     Number of players
dtype: object
```
We see that almost all the teams have a higher value in column `Total team goals`, except Chelsea and Burnley: It seems that these teams have more players than goals scored. However, this is not necessarily true, because they both have a `NaN` value in column `Total team goals`. So we don’t know…
---
> 💡 **When running `.idxmax()` with `axis=0` we get the same number of return values as there are columns. When we use `axis=1` we get the same number of return values as there are rows.**
---
## [**`.min()`**](/a75dc11df0cf41a99774029877a76063)
---
**Syntax**
With this function we can find out the lowest value in a specific column in a DataFrame.
`df[ << some column >> ].min()`
---
**Find lowest numerical value**
Let’s assume we are interested in the lowest number of days a player played football.
```python
players_df['days_played'].min()

0.08472222222222221
```
And how can we find out the name of the player with the lowest number of days played? We can use `.loc[]` again as we can put in a boolean condition into the selector.
```python
players_df.loc[players_df['days_played'] == players_df['days_played'].min(), 'Player']

24    Curtis Jones
Name: Player, dtype: object
```
---
**Find lowest alphabetic value**
We can also use `.min()` to find the word in a column that comes first in the alphabet. Let’s assume we want to find the team name that comes first in the alphabet.
```python
players_df['Team'].min()

'Arsenal'
```
---
## [`.idxmin()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.idxmin.html)
---
**Syntax**
This function allows us to get the index label or the column name of the lowest numerical value in the column or in the row. The syntax is as follow:
`df.idxmin( << axis >> ) `
The difference between the values for `<< axis >>` parameter is the following:
| `axis=0` | `axis=1` |
| --- | --- |
| For each column, the index label of the row with the lowest value is returned | For each row, the column name with the lowest value is returned |
---
**Get index labels for lowest value in columns**
Let’s assume we have again the DataFrame `outer_merge_df` with the column `Player` set as the index column.
![outer_merge_df](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/c09b5108-a06d-464d-9777-48fd059e0031/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666N4FIADZ%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T222610Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJGMEQCICKfhMgTyJR4rtiGWURz3TYaV7Gs%2FO%2F4i5CemlniJzLOAiBsQH8o%2BT4nT44AmP3VXF3ptZGIcveCB7BkpPYU3PbYayr%2FAwgnEAAaDDYzNzQyMzE4MzgwNSIMZdpfXix3mLQp9ZGNKtwDVwoLwKidOqvJXqVn7XbjNp7zipum9EYR3nje95ecI2ciXBx7UpgeQ2DWZRXSf6uEicDt7roAvDPaTz6x8nT0g7lkwk2dosOG4koH6VvU5FUwemnegmb9NHOmxU8m89p2Um7Vme1AVCHzBFVxGqwH0rpneha10kLfaULMtwLkDqIpxRFjz7ZFtd9kB9mF9i%2B9DD%2F9029RlOfrEqwXFrxkFIVFdjelL1sNmlF1MSeQjRxVbVzMzWxD6SYVTZX%2Bma2jtIvtk6CglGWFw0blJRNuCTPuzIRE6Rl1k4E%2FTxYYTVCHX%2BKDanKnowwLkp90bGrSqBjray38KS7aZGnEE8KzL%2F00V7wEHUHB5%2BBj4vmBDLqVlwJxyNQS8yNCaI%2Fav1dQRqPUqkePRfF4fWuGfkSPIFH6GbN%2FAuj3kbZP28%2BLrOI3tly57%2FcCbMV0CDHJka%2Fc8doIMg5je8b1fk6H5j8RygdHKqhhICQoSHJWmuXlTMlk6c5XsZlF4ALsrty4bFNhF%2BnrZLkuxoyMWimEnN56cAQVaVm%2F9FaV%2BX2zNS%2FvXvbzxOs5xRsgSxt9zImQ8EsqQx%2FQq32vSjbj7znoESFsbX%2B0I%2BK9j22oO5ujdp%2F4PnlPaEZ6wO8YkOdXE2Iwtc73yQY6pgG0e0Dk6qellL0S4BBKPG2LK%2BfYEOxjKxq6SoTRPkBKTValVM%2FylJi22aChciSUYak8TTrj%2FFDRLuedSBHKz%2BfJlxLZ4z2WDrrqHTqHxEgJX%2B26%2FHZXmlG7hkzISIuO2BygpylIAR4vMwfNPdqnPlrbsOQun%2FEUC5T8jsRx1GVJaAj5JDgk9cVOB0hqcvFDgifAy6LCby2%2BMzLkhuAnVYRAkq%2FrdEtU&X-Amz-Signature=eef7161d3a1df36758e2e635ac07dd6b4f3ba0cb2dc0c53db6b9846ca2789c25&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
To find out the team with the lowest team goals and the lowest number of players, we can run the following command:
```python
outer_merge_df.idxmin(axis=0)

Total team goals      Norwich City
Number of players    Norwich United
dtype: object
```
We can see that Norwich City is the team with the lowest goals and also lowest number of players.
---
**Get index label of lowest value in single column**
We can also use `.idxmin()` on a single column. Thus, to find out the name of the team that scored the lowest goals only, we can run the following command:
```python
outer_merge_df['Total team goals'].idxmin()

'Norwich City'
```
This is especially useful when we have a large dataset that is not sorted and we want to quickly find out the index label that corresponds to a maximum value in a column.
---
**Get column name for lowest value in each row**
To find out for each team whether their number of goals scored or number of players is lower we can run the following command:
```python
outer_merge_df.idxmin(axis=1)

### OUTPUT ###
Team
Manchester City              Total team goals
Liverpool                   Number of players
Manchester United           Number of players
Leicester City              Number of players
Arsenal                      Total team goals
Tottenham Hotspur           Number of players
Southampton                 Number of players
West Ham United             Number of players
Wolverhampton Wanderers     Number of players
Everton                     Number of players
Aston Villa                 Number of players
Bournemouth                 Number of players
Newcastle United            Number of players
Sheffield United            Number of players
Watford                     Number of players
Brighton and Hove Albion    Number of players
Crystal Palace              Number of players
Norwich City                Number of players
Chelsea                     Number of players
Burnley                     Number of players
dtype: object
```
We see that almost all the teams have a lower value in column `Number of players`, except Manchester City and Arsenal: It seems that these teams have less players than goals scored. However, this is not necessarily true, because they both have a `NaN` value in column `Number of players`. So we don’t know…
---
> 💡 **When running `.idxmin()` with `axis=0` we get the same number of return values as there are columns. When we use `axis=1` we get the same number of return values as there are rows.**
---
## [`.mean()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.mean.html)
---
**Syntax**
This function calculates the mean value for a specific column or the entire DataFrame.
`df[ << some column >> ].mean()` → single column
`df.mean()` → entire DataFrame
---
**Calculate mean value of single column**
Let’s assume we want to calculate in how many games a player has played on average.
```python
players_df['Games played'].mean()

18.985185185185184
```
---
**Calculate mean value for all columns**
Let’s assume we want to calculate the average for all columns in the DataFrame that contain numeric data.
```python
players_df.mean()

Games played        18.985185
Games started       15.090741
Minutes played    1353.657407
Goals                1.825926
Assists              1.275926
Shots               12.331481
Shots on goal        5.909259
dtype: float64
```
---
## [`.describe()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.describe.html)
**Syntax**
With this function we can retrieve the descriptive statistics for a single column or the entire DataFrame.
`df[ << some column >> ].describe()` → single column
`df.describe()` → entire DataFrame
The output includes:
- [`count`](/1a11208373ef44358aa1528a5dc7e807) → number of values
- [`mean`](/1a11208373ef44358aa1528a5dc7e807) → average value
- [`std`](https://www.nedarc.org/statisticalhelp/basicStatistics/standardDeviation.html) → standard deviation
- [`min`](/1a11208373ef44358aa1528a5dc7e807) → lowest value
- [`max`](/1a11208373ef44358aa1528a5dc7e807) → highest value
- [`25%`](https://www.mathsisfun.com/data/percentiles.html) → lower quartile
- [`50%`](/1a11208373ef44358aa1528a5dc7e807) → middle quartile / median
- [`75%`](https://www.mathsisfun.com/data/percentiles.html) → upper quartile
---
**Descriptive statistics for single column**
Let’s assume we want to retrieve the descriptive statistics for the column `Shots`. 
```python
players_df['Goals'].describe()

count    540.000000
mean      12.331481
std       16.651935
min        0.000000
25%        0.000000
50%        6.000000
75%       17.000000
max       95.000000
Name: Shots, dtype: float64
```
---
**Descriptive statistics for entire DataFrame**
Let’s assume we want to retrieve the descriptive statistics for all columns in the DataFrame that contain numeric data.
```python
players_df.describe()
```
![DataFrame is returned with the stats measures in the index and all columns with numeric data in `players_df` as columns](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/d744d39a-d451-4172-b2c3-42c4dea5c4c6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VJHYC2QN%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T222612Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQDhptPH28n0uD%2BtL5J1AnSDbcZgWzmoX9oMvfyOaffrCgIhAIyUAJSFUF3FLgJkZKZCkwXpk3p0JNvb6nWvCiF0EztYKv8DCCcQABoMNjM3NDIzMTgzODA1IgzTNa08mbRUuhaVbXEq3ANnNVQRonvvqoHhqtoeEQJsl%2BlKmXAtVdeyJQ4sFdWA6VZlOmyr%2B1Y5AxAuZk%2F%2BEXssencSFhC%2FzVlvmwFwTkBElHeVCVEjyANviCaN4vWtymgzfP89c25ylMDAhrrLpzpMTk5aOl4o6rI7H8EdpjeIjVPeN43jLa3FpOUqmbWW1%2FI%2BSr714mL6cYVphQev99bw8QbbAPeecXQ2yU%2Bz23o7LP2ifuj%2FUD000daDcLXqZn29K36E9Fy76E1EHn808fO0PpurcQE%2BM2XqkY0wrHZVu%2BD7Hx%2BsWoVF4%2BD2jOxAWSYCfZi%2FLpvUY3naDbZ8pNzGrxHcdW1gEu4FeOGfRtBTe6Te6bga6YgPjvGsBK4oWssH8HyuoG9UYBz2iUXcbK4OqbvbE1Vg7pIA7P0ZiJFF%2BzCUdzLBCXmv8Ako7YhAhDYzw67T%2BImInYfSqKp6%2B5Ipa1h34sk2qIMbaw3Q62evXiyBN32J0ZB%2BIaIaOmJaYtZ2IaJ%2FiFgNxp0jVZwc2cOCIof6h4p3EJzVM3svz%2FhzGsV4GAHymJuVKMulIEtUGOV%2B%2BYsCgvkUWyqaG%2F4l3bGB0ZemTE3jaEnz60JcrOBtCtL0Ju9w81caGfPwADiL2juR0apIdQs4LOSYrzDvzffJBjqkASO9J9q035s3O4X6G3cvqEkQlnkUgtmmJ%2FjEFNCu3508xe9GQbQr6byEuoOd9M89IEpY4jlVs56vRDIaZlf5aenkgSNU2X%2F4Ci69ttkRaNOjNt6i8PTn3Nbx0r17osgnHFbY%2BQNmnb%2Bnai9rTIhQuAYTj1QTa%2FXxdhi53lRoPmhBPeZhrUy8d1j5vxpgxYPoixFv7XvSHYBb%2F2ARr8sqmKNFClM2&X-Amz-Signature=c1ad8153c79cdf74156a10d4530e5c162c730df6409a2ac545c38f61fbc37569&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
---
## [`.cut()`](https://pandas.pydata.org/docs/reference/api/pandas.cut.html)
---
**Syntax**
This function allows us to segment values into different bins. Specially when we want to create a Histogram with let’s say 10 bars then this function is helpful as it allows us to put the values in 10 equally-sized bins. 
`pd.cut( << data >> , << number of bins >> , retbins = True )`
If we don’t set the `retbins=` parameter to `True`, then the single bins are not returned. Only to which bin each value belongs to. If wet `retbins=True`, both things are returned.
---
**Put series into bins**
Let’s assume we want to create a histogram for the column `total_points` in `players_df` with those players who have scored more than 1 point (312 players).
In our histogram there should be 20 bars in the end, thus we cut the data into 20 bins. 
```python
bins = pd.cut(players_df['total_points'], 10)
```
We can check now the output, i.e., the content in bins, which is a Tuple that contains two elements.
```python
bins[1]

array([ 0.968,  2.6  ,  4.2  ,  5.8  ,  7.4  ,  9.   , 10.6  , 12.2  ,
       13.8  , 15.4  , 17.   , 18.6  , 20.2  , 21.8  , 23.4  , 25.   ,
       26.6  , 28.2  , 29.8  , 31.4  , 33.   ])
```
We see that the second element in the array is a numpy array containing the border values of the 20 bins. These border values are interpretable as follow:
| # bin | bin | Values included |
| --- | --- | --- |
| 1st | `(0.968, 2.6]` | `0.968 < val ≤ 2.6` |
| 2nd | `(2.6, 4.2]` | `2.6 < val ≤ 4.2` |
| 3rd | `(4.2, 5.8]` | `4.2 < val ≤ 5.8` |
| … | … | … |
| 18th | `(28.2, 29.8]` | `28.2 < val ≤ 29.8` |
| 19th | `(29.8, 31.4]` | `29.8 < val ≤ 31.4` |
| 20th | `(31.4, 33.0]` | `31.4 < val ≤ 33.0` |
```python
bins[0]

Rank
1      (26.6, 28.2]
2      (23.4, 25.0]
3      (23.4, 25.0]
4      (20.2, 21.8]
5      (28.2, 29.8]
           ...     
451    (0.968, 2.6]
454    (0.968, 2.6]
471    (0.968, 2.6]
472    (0.968, 2.6]
501    (0.968, 2.6]
Name: total_points, Length: 312, dtype: category
```
We can see that the first element in `bins` is a Series that contains for each player the according bin he falls into, based on the total points he has achieved.
For example, we can check into which bin the 18th player falls into as follow:
```python
bins[0][18]

Interval(13.8, 15.4, closed='right')
```
We see that the 18th player has achieved between 13.8 and 15.4 points.
---
**Excursus: Create Histogram using custom bins**
Now, although this is rather a [Matplotlib](/a75dc11df0cf41a99774029877a76063) topic, we quickly want to see how this works. We can use the `.plot()` function of `Matplotlib.pyplot` package to create a histogram. 
```python
import matplotlib.pyplot as plt

plt.hist(players_df['total_points'], bins[1])
```
As we can see we first pass the values of which we want to visualise the frequency and then as second parameter the bin values. The function `.plot()` then puts the values into the respective bins automatically and we get the following chart:
![Simple histogram that shows that the majority of players has achieved close to zero points](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/f2df9952-028a-4b16-acf5-4e33b3acb75c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662SMQJQOQ%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T222613Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJGMEQCIGWUw%2BRyGF%2FCQznyvgL7XYKS39cCCBHh9wPqbTG7WNebAiBe5SaLzKOmsqmZK8k4xgT0Xrus%2FnOLv84PQxfS%2BmeZLir%2FAwgnEAAaDDYzNzQyMzE4MzgwNSIMCbWP%2F9Eu5hX0rs%2FIKtwD00dSLtme%2F464cL3f6ab%2FeUuvNrrUwLVr9OQD8MdMQY1mSkpdJyR8FAMTKd8ImWIIIpgoQ7rolJXdPp2GZdTwMmCGVUsSq3ZuAPv9MYFXzep%2Bv7t%2FESFriAWNTtwgu5uQV8VwcEFspY%2FUAlFY%2BUg1hjFBgktm2y484Hz0%2FzwSmBIaHTwq%2BCpubL%2BAuQ7WgEcKSiU9HKqhTqqrBZJ9TZtBVye0NWzE%2FXleLkj5aUEoV3aXAxC2zK%2FzU4Maq0UyLD4lM2riwNnYtcID6Zv8uOZ06LzsaAX15%2FIjlFLr%2Brw3fORkmGbF2rch8B5hvxr3oiS04S8BUV8Ic4cMiI5bY4xRBeTHuZHC08sDvdOWJ4EYXlpOwrvnf8CMQcFDNddGnM0hdCkVcQOvnQ708CbMbLaVHCtW8BhxFWo%2BMgakXVcNcr9wiIhEbZJ5SBslaYThYwz9f0H4G9vGHiQwbutt3oYzbIgONQ69BZtxYLUHqNy5jfoloZXrT%2FL1Hy7HgsStXWHPuTLEeWLroZgSlviplQp9uQjN%2FY3LEnS9VnpAQjzCXh0%2BmeP2Us%2BjEdXrCNzKGCXLBKH3%2BcaUqYI%2FyhqJeOAMJ3e9%2B51it7SGW%2F8BsHv81e9pAxyKfrLD0ePs%2B4ow4833yQY6pgEiTsWcUFKlDBowUd14C90L6%2BwI2kW9qWKARGKjazbJ%2BBYyLY7knZSHzqSpZ6P8JBi%2BYpXJkuKNfWCoHMmey1ZhXvNwQdQC7O936eCaE5MbgjHTxLF%2BPxZelcRKP7f7zom9NlJ6VM7gkkzNXPPWJiAJCwXr%2BqYoqcZn23RDRQewjppBMc0R8cbQH1oB5a5ldDuZPZQ9a83GOZSmYXOHWWJp%2BHGtN12U&X-Amz-Signature=a32f1fcd16e12028d5eb342453bb409cd6077b8d5640653587450143d2624f8b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
---
## [`.unique()`](https://pandas.pydata.org/docs/reference/api/pandas.unique.html)
---
**Syntax**
This function allows us to retrieve all unique values in either a row or a column. 
`pd.unique( << some row or column >>)`
---
**Retrieve unique values in column**
We have seen before that the player with the most goals, Jamie Vardy, scored 23 goals. Now as there are much more players in the DataFrame `players_df` than 23 we want to get the unique values from column `Goals` only. We can achieve this with the following command:
```python
pd.unique(players_df['Goals'])
 
array([ 0,  1,  4,  6,  5,  2,  3, 10,  8, 17,  7, 23, 11,  9, 20, 19, 13,
       16, 14, 18, 15, 22])
```
Now we see that the function returns a numpy array. How can we now check if each number of goals, from 0 to 23, was scored at least once? We can simply extend our method with the `.size` attribute (equivalent to `len()` when using lists). 
```python
pd.unique(players_df['Goals']).size

22
```
We see that the there are only 22 unique values in the array. Thus not each number of goals from 0 to 23 was scored at least once. Which number of goals was not scored? Let’s sort the array to find out. 
```python
sorted(pd.unique(players_df['Goals']))

[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 18, 19, 20, 22, 23]
```
We see now that the number 12 and 21 are missing in the array above. Thus, there is no player who scored 12 or 21 goals.
---
**Retrieve unique values in row**
To get the unique values for a single row, we can use the same function. We just have to extract the row first from the DataFrame using `.loc[]` or `.iloc[]`. Let’s say we want to check how many unique values there are for the sixth player in the DataFrame. We can achieve that by running the following command:
```python
pd.unique(players_df.iloc[5]) 

array(['Scott McTominay', 'Manchester United', 27, 20, 1770, 4, 1, 17, 10,
       5, 0.25, 1.2291666666666667], dtype=object)

pd.unique(players_df.iloc[5]).size
12
```
We see that the player Scott McTominay has 12 unique values. Does the player have any duplicate values? Let’s find out by checking the total number of columns in the DataFrame using the `.columns` attribute. 
```python
len(players_df.columns)

12
```
We see that there are 12 columns in the DataFrame. Thus, the player does not have any duplicate values.
---
## [`.sort_index()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sort_index.html)
---
**Syntax**
This function allows us to sort a DataFrame based on its index column.
`df.sort_index(inplace=True)`
---
**Sort DataFrame according to its index**
Let’s assume that for some reason the DataFrame got messed up and thus the rows are jumbled, i.e., no longer sorted according to the index:
![Unsorted players_df](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/ddbf4cb0-bf1f-491d-b50a-cda8910a5fee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664Z7VZYMZ%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T222619Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQCWSUzcBYhjF%2B5Uv3YcaYtv%2BW1x9IcqSLqNLFVTTmsWogIhALg3o6uiETmoKd4i6j%2BwBNjeT%2F1SpKdaMqvnukAxHt1BKv8DCCcQABoMNjM3NDIzMTgzODA1IgxWMzVSYlq3bIkdTF4q3ANi5wIWNWNZcx877feFS%2Bm%2FkFX%2FW67FYaHofHvaJPve4jHvSUAFjr7cP%2Bzrhrehv%2BC%2F6uVJc3wVzvuWnFxCS91xz2gNsTyxrVG0pZuMa7d%2BJn4HhrDj2hxYqA0joyg3C8QURzNCcZt1ssJ9ckqk3sfbHGyQu0rASTbFK3XRRpw%2B6B2WSe3vLiR2zFj6c3HtRp5UeGxwzesMBkpWqTnV4pnykdjbhNXYydG6AznGmYRCFgieyXdwaqPO3fMRofQvfUF9ghU57fRlD9EBBMivRxmyS4O9G2XpCcYCy5AoLllxwukTNV9EaWhc%2Bb7%2FUFmf25T%2BaHPcJERS1z0l6Tp4N5CQUZURtwia88Q%2FgmigS%2BvClqYatCqWRTPXBhzwIAK972AM6gUYASBKzMUmXECCURzDEwkXyqbDhU6TddesMs3DLIwiTRjDj%2F%2FR8LYXJrvHT8QXBe%2FJOu8HE2saUNktyKINl%2B1Hp5txm87fD72CfmF9gaL7uYcP02aRdSfZBl1r1QAyloIL4qfDXt9POvQ6RfsCGMdfOXgHlca8gGQkF2RGQBZiQ5DtkHbwk3SDW2vU8XAbTWW1UPtfTy43ra%2F9cYYQJJ49yO19TMPnfiysNzPZLA11XncXOofAg0ZJvTDXzvfJBjqkASqcwLjwW6e%2FrHtrlrPNBOetd67bRVNPXuKc37vl656ag%2FGgWLrMecEd2VV4ZrqOoV8qc4GORPtdsfybfdUIKw6cSYIFJBWnEg4SDm5%2BsvQCl7lyCc8zgLD71UDsi0NQRo9US3W37587741QM2TzrFspjKx7p40dqBBvuBu44Ao09ZJw%2F7kzKXExuoi6XGcqPMBuw9Vi75Ki9NdcZ6HUCo1kioq2&X-Amz-Signature=fea1c4d620d7427168396286e96be06a1998bf57eed7dc34e82b140efbc5862f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
We can now restore the correct order by sorting the DataFrame again:
```python
players_df.sort_index(inplace=True)
```
![Sorted players_df](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/efdd00d4-abfb-4ddb-887e-e03a6a2e2064/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664Z7VZYMZ%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T222619Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQCWSUzcBYhjF%2B5Uv3YcaYtv%2BW1x9IcqSLqNLFVTTmsWogIhALg3o6uiETmoKd4i6j%2BwBNjeT%2F1SpKdaMqvnukAxHt1BKv8DCCcQABoMNjM3NDIzMTgzODA1IgxWMzVSYlq3bIkdTF4q3ANi5wIWNWNZcx877feFS%2Bm%2FkFX%2FW67FYaHofHvaJPve4jHvSUAFjr7cP%2Bzrhrehv%2BC%2F6uVJc3wVzvuWnFxCS91xz2gNsTyxrVG0pZuMa7d%2BJn4HhrDj2hxYqA0joyg3C8QURzNCcZt1ssJ9ckqk3sfbHGyQu0rASTbFK3XRRpw%2B6B2WSe3vLiR2zFj6c3HtRp5UeGxwzesMBkpWqTnV4pnykdjbhNXYydG6AznGmYRCFgieyXdwaqPO3fMRofQvfUF9ghU57fRlD9EBBMivRxmyS4O9G2XpCcYCy5AoLllxwukTNV9EaWhc%2Bb7%2FUFmf25T%2BaHPcJERS1z0l6Tp4N5CQUZURtwia88Q%2FgmigS%2BvClqYatCqWRTPXBhzwIAK972AM6gUYASBKzMUmXECCURzDEwkXyqbDhU6TddesMs3DLIwiTRjDj%2F%2FR8LYXJrvHT8QXBe%2FJOu8HE2saUNktyKINl%2B1Hp5txm87fD72CfmF9gaL7uYcP02aRdSfZBl1r1QAyloIL4qfDXt9POvQ6RfsCGMdfOXgHlca8gGQkF2RGQBZiQ5DtkHbwk3SDW2vU8XAbTWW1UPtfTy43ra%2F9cYYQJJ49yO19TMPnfiysNzPZLA11XncXOofAg0ZJvTDXzvfJBjqkASqcwLjwW6e%2FrHtrlrPNBOetd67bRVNPXuKc37vl656ag%2FGgWLrMecEd2VV4ZrqOoV8qc4GORPtdsfybfdUIKw6cSYIFJBWnEg4SDm5%2BsvQCl7lyCc8zgLD71UDsi0NQRo9US3W37587741QM2TzrFspjKx7p40dqBBvuBu44Ao09ZJw%2F7kzKXExuoi6XGcqPMBuw9Vi75Ki9NdcZ6HUCo1kioq2&X-Amz-Signature=68d45f162bd6c8e4edff8371e42b646ccd4a9272a157525f641e6827c12d6191&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
---
## [`.sort_values()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sort_values.html)
---
**Syntax**
This function allows us to sort a DataFrame based on the values in any column. 
`df.sort_values( by = [ << column(s) to sort >> ], ascending = << False or True >>, inplace = True )`
---
**Sort DataFrame based on single column**
Let’s assume we want to sort the DataFrame players_df based on column Assists in descending order. Thus, the player with the most assists should be on top.
```python
players_df.sort_values(by=['Assists'], ascending=False, inplace=True)
```
![`players_df` sorted based on column `Assists` in descending order](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/b453e607-898f-4093-80d9-39f634fd6f61/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SPDDO5SP%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T222620Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIBeq5IdA1ZwQYozGMqztswnnYW%2FBXbV8Dq4S9c0WhADaAiEAizmaHvFQ%2FmqQ3YjnpP1IA4EOWrX77r%2FCkijyCPSRPesq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDE2R%2BXyBC37ABeYGuircA%2Ba%2BGHL9RmUhYHUWMHpzsgHkkAeUbFbcB0BXQoMRAz%2B7lcfyFPenulNPt7Kic0HeDIFexcKViuA0muaDiQJRCmK5%2BZydbOvkqj6ththZQeotzHX%2B5EKt6za%2Fp9kpUukm9z4HRadxRsk1o69Gh%2B7b5JrlAegjGuZ%2BwCUoF%2F2qLjWwL%2FBY0sPGwOPR5fivM7CeCRyII328RzLxBKT6WT1KY58TR1yni5nA09KRlo62FHTt0SPdqFCJIPed1LQ4RClso7IzRJWCrLdxVsWsnSLbFAvac3tnok%2BU0x6QYNgrR5xl8JuXy9cHGWAi9m6JctoCv%2Bv%2BWPLkPYIx1F6gl%2Bpqx2BnB6goXp2X6W2wdcsKB2gPtb88k%2BaIh2ZP4yj09KHUpA1JdIQXuc%2B406SJ1Z5e9GfURQ1VSwqdIx5qlEnZkzvRRqR%2BIrCD83K0A8PIcKRhgbKpQ6foSXMOor5Z4Be2LAo10WhFU5rlPRIfD%2BvkjZUZTcYLmqvdo7LeiE7V6NM3Dlpdc0z0UuMzvfumUfSUbwijTyEaDlSSEUQxAJaTv5r7sz%2B8Sb16%2FNx8ZhEHmVqO26sPjtRkHkqcVNJOdnHIflxoRGHX6l%2F9%2F%2BymXZq%2Fru%2F2r8Sxcii2Znz5wRLSMPDN98kGOqUBHJvqRBM5PunCPjENcrJx9AE1frlEzQoU1tz9tZICQ0zOuSJUSB6AyHqL0oHdo%2Bml3qnx8pwuZHX%2BUkiOitk1v6IpKfbXJOYagG%2FVyWN3LAcjPmqiRQQlhRqAeybZyNyppZCFOhgeREcqFvBxwI0nfUThfUCxVRYMS%2BOQ%2FdVK3W2gNnUyR%2BQbNsV5BTmnJA5plshQiL3UvaBKYiGfFsc8gW5dz2wJ&X-Amz-Signature=5dbc4b5ee826f27d6f54fd46e2789980819db735f4db602d60152daca0023ef8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
In the code snippet we can see that we explicitly specified the `ascending=` parameter. This is necessary as per default `ascending=` is set to `True`, so if we want to sort in descending order, we need to set this parameter to `False`.
---
**Sort DataFrame based on multiple columns**
Let’s extend the previous example and sort the DataFrame first based on column Assists and then based on column Goals.
```python
players_df.sort_values(by=['Assists', 'Goals'], ascending=False, inplace=True)

players_df.head(10)
```
![`players_df` sorted based on column `Assists` and `Goals` in descending order](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/857b7752-594c-4f3f-ab41-99f60bea6a56/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SPDDO5SP%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T222620Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIBeq5IdA1ZwQYozGMqztswnnYW%2FBXbV8Dq4S9c0WhADaAiEAizmaHvFQ%2FmqQ3YjnpP1IA4EOWrX77r%2FCkijyCPSRPesq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDE2R%2BXyBC37ABeYGuircA%2Ba%2BGHL9RmUhYHUWMHpzsgHkkAeUbFbcB0BXQoMRAz%2B7lcfyFPenulNPt7Kic0HeDIFexcKViuA0muaDiQJRCmK5%2BZydbOvkqj6ththZQeotzHX%2B5EKt6za%2Fp9kpUukm9z4HRadxRsk1o69Gh%2B7b5JrlAegjGuZ%2BwCUoF%2F2qLjWwL%2FBY0sPGwOPR5fivM7CeCRyII328RzLxBKT6WT1KY58TR1yni5nA09KRlo62FHTt0SPdqFCJIPed1LQ4RClso7IzRJWCrLdxVsWsnSLbFAvac3tnok%2BU0x6QYNgrR5xl8JuXy9cHGWAi9m6JctoCv%2Bv%2BWPLkPYIx1F6gl%2Bpqx2BnB6goXp2X6W2wdcsKB2gPtb88k%2BaIh2ZP4yj09KHUpA1JdIQXuc%2B406SJ1Z5e9GfURQ1VSwqdIx5qlEnZkzvRRqR%2BIrCD83K0A8PIcKRhgbKpQ6foSXMOor5Z4Be2LAo10WhFU5rlPRIfD%2BvkjZUZTcYLmqvdo7LeiE7V6NM3Dlpdc0z0UuMzvfumUfSUbwijTyEaDlSSEUQxAJaTv5r7sz%2B8Sb16%2FNx8ZhEHmVqO26sPjtRkHkqcVNJOdnHIflxoRGHX6l%2F9%2F%2BymXZq%2Fru%2F2r8Sxcii2Znz5wRLSMPDN98kGOqUBHJvqRBM5PunCPjENcrJx9AE1frlEzQoU1tz9tZICQ0zOuSJUSB6AyHqL0oHdo%2Bml3qnx8pwuZHX%2BUkiOitk1v6IpKfbXJOYagG%2FVyWN3LAcjPmqiRQQlhRqAeybZyNyppZCFOhgeREcqFvBxwI0nfUThfUCxVRYMS%2BOQ%2FdVK3W2gNnUyR%2BQbNsV5BTmnJA5plshQiL3UvaBKYiGfFsc8gW5dz2wJ&X-Amz-Signature=7b8d6cf54568103082e184444f08c41bf4ff92041896698e3e9309b6f5eef383&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
We looking at the top 10 rows in the DataFrame we can see that the sorting worked. Three players have 10 assists, but one player has more goals than the other two, thus the player Mohamed Sala Ghaly is displayed correctly before the other two players with 10 assists. 
We can also see in the code snippet that we can simply extended the list that we pass as `by=` parameter value with another column name.
---
**Sort DataFrame based on column containing text**
Let’s assume we have the following DataFrame `players_df_new`.
![players_df_new](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/59998ff6-4439-4f6e-8d92-b267731f85cf/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SPDDO5SP%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T222620Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIBeq5IdA1ZwQYozGMqztswnnYW%2FBXbV8Dq4S9c0WhADaAiEAizmaHvFQ%2FmqQ3YjnpP1IA4EOWrX77r%2FCkijyCPSRPesq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDE2R%2BXyBC37ABeYGuircA%2Ba%2BGHL9RmUhYHUWMHpzsgHkkAeUbFbcB0BXQoMRAz%2B7lcfyFPenulNPt7Kic0HeDIFexcKViuA0muaDiQJRCmK5%2BZydbOvkqj6ththZQeotzHX%2B5EKt6za%2Fp9kpUukm9z4HRadxRsk1o69Gh%2B7b5JrlAegjGuZ%2BwCUoF%2F2qLjWwL%2FBY0sPGwOPR5fivM7CeCRyII328RzLxBKT6WT1KY58TR1yni5nA09KRlo62FHTt0SPdqFCJIPed1LQ4RClso7IzRJWCrLdxVsWsnSLbFAvac3tnok%2BU0x6QYNgrR5xl8JuXy9cHGWAi9m6JctoCv%2Bv%2BWPLkPYIx1F6gl%2Bpqx2BnB6goXp2X6W2wdcsKB2gPtb88k%2BaIh2ZP4yj09KHUpA1JdIQXuc%2B406SJ1Z5e9GfURQ1VSwqdIx5qlEnZkzvRRqR%2BIrCD83K0A8PIcKRhgbKpQ6foSXMOor5Z4Be2LAo10WhFU5rlPRIfD%2BvkjZUZTcYLmqvdo7LeiE7V6NM3Dlpdc0z0UuMzvfumUfSUbwijTyEaDlSSEUQxAJaTv5r7sz%2B8Sb16%2FNx8ZhEHmVqO26sPjtRkHkqcVNJOdnHIflxoRGHX6l%2F9%2F%2BymXZq%2Fru%2F2r8Sxcii2Znz5wRLSMPDN98kGOqUBHJvqRBM5PunCPjENcrJx9AE1frlEzQoU1tz9tZICQ0zOuSJUSB6AyHqL0oHdo%2Bml3qnx8pwuZHX%2BUkiOitk1v6IpKfbXJOYagG%2FVyWN3LAcjPmqiRQQlhRqAeybZyNyppZCFOhgeREcqFvBxwI0nfUThfUCxVRYMS%2BOQ%2FdVK3W2gNnUyR%2BQbNsV5BTmnJA5plshQiL3UvaBKYiGfFsc8gW5dz2wJ&X-Amz-Signature=50c55479277f48666a22b83fb3592206ec0a8d3d46b5db2b30b5f151ea35e01f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
As we can see the column `Player` includes the player names. Sometimes the name of the player is written in lower letters.
Let’s sort the DataFrame based on the column `Player`.
```python
players_df_new.sort_values('Player', inplace=True)
```
![players_df_new sorted incorrectly](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/c0c0379f-1513-4eba-a177-4213fdaf1436/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SPDDO5SP%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T222620Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIBeq5IdA1ZwQYozGMqztswnnYW%2FBXbV8Dq4S9c0WhADaAiEAizmaHvFQ%2FmqQ3YjnpP1IA4EOWrX77r%2FCkijyCPSRPesq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDE2R%2BXyBC37ABeYGuircA%2Ba%2BGHL9RmUhYHUWMHpzsgHkkAeUbFbcB0BXQoMRAz%2B7lcfyFPenulNPt7Kic0HeDIFexcKViuA0muaDiQJRCmK5%2BZydbOvkqj6ththZQeotzHX%2B5EKt6za%2Fp9kpUukm9z4HRadxRsk1o69Gh%2B7b5JrlAegjGuZ%2BwCUoF%2F2qLjWwL%2FBY0sPGwOPR5fivM7CeCRyII328RzLxBKT6WT1KY58TR1yni5nA09KRlo62FHTt0SPdqFCJIPed1LQ4RClso7IzRJWCrLdxVsWsnSLbFAvac3tnok%2BU0x6QYNgrR5xl8JuXy9cHGWAi9m6JctoCv%2Bv%2BWPLkPYIx1F6gl%2Bpqx2BnB6goXp2X6W2wdcsKB2gPtb88k%2BaIh2ZP4yj09KHUpA1JdIQXuc%2B406SJ1Z5e9GfURQ1VSwqdIx5qlEnZkzvRRqR%2BIrCD83K0A8PIcKRhgbKpQ6foSXMOor5Z4Be2LAo10WhFU5rlPRIfD%2BvkjZUZTcYLmqvdo7LeiE7V6NM3Dlpdc0z0UuMzvfumUfSUbwijTyEaDlSSEUQxAJaTv5r7sz%2B8Sb16%2FNx8ZhEHmVqO26sPjtRkHkqcVNJOdnHIflxoRGHX6l%2F9%2F%2BymXZq%2Fru%2F2r8Sxcii2Znz5wRLSMPDN98kGOqUBHJvqRBM5PunCPjENcrJx9AE1frlEzQoU1tz9tZICQ0zOuSJUSB6AyHqL0oHdo%2Bml3qnx8pwuZHX%2BUkiOitk1v6IpKfbXJOYagG%2FVyWN3LAcjPmqiRQQlhRqAeybZyNyppZCFOhgeREcqFvBxwI0nfUThfUCxVRYMS%2BOQ%2FdVK3W2gNnUyR%2BQbNsV5BTmnJA5plshQiL3UvaBKYiGfFsc8gW5dz2wJ&X-Amz-Signature=f944f244ae04df93ba3e6a6dfa7598f219cdea06a430b5d32fb294d1c9b144fc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
We can see now that the player Sadio Mané is displayed before the player harry kane although the letter S comes after letter H in the alphabet. This is because the `.sort_values()` method is case-sensitive and goes from A, B, … Z first and only then starts with a, b, … z, i.e., with the lower letters.
For this reason we must provide a `key=` parameter and a `lambda` function as value which transforms all the values in column Player to lower letters before the actual sorting is done. 
```python
players_df_new.sort_values('Player', key=lambda x:x.lower(), inplace=True)
```
![players_df_new sorted correctly](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/2831e596-6fd1-47ec-93e3-e19fea8667ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SPDDO5SP%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T222620Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIBeq5IdA1ZwQYozGMqztswnnYW%2FBXbV8Dq4S9c0WhADaAiEAizmaHvFQ%2FmqQ3YjnpP1IA4EOWrX77r%2FCkijyCPSRPesq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDE2R%2BXyBC37ABeYGuircA%2Ba%2BGHL9RmUhYHUWMHpzsgHkkAeUbFbcB0BXQoMRAz%2B7lcfyFPenulNPt7Kic0HeDIFexcKViuA0muaDiQJRCmK5%2BZydbOvkqj6ththZQeotzHX%2B5EKt6za%2Fp9kpUukm9z4HRadxRsk1o69Gh%2B7b5JrlAegjGuZ%2BwCUoF%2F2qLjWwL%2FBY0sPGwOPR5fivM7CeCRyII328RzLxBKT6WT1KY58TR1yni5nA09KRlo62FHTt0SPdqFCJIPed1LQ4RClso7IzRJWCrLdxVsWsnSLbFAvac3tnok%2BU0x6QYNgrR5xl8JuXy9cHGWAi9m6JctoCv%2Bv%2BWPLkPYIx1F6gl%2Bpqx2BnB6goXp2X6W2wdcsKB2gPtb88k%2BaIh2ZP4yj09KHUpA1JdIQXuc%2B406SJ1Z5e9GfURQ1VSwqdIx5qlEnZkzvRRqR%2BIrCD83K0A8PIcKRhgbKpQ6foSXMOor5Z4Be2LAo10WhFU5rlPRIfD%2BvkjZUZTcYLmqvdo7LeiE7V6NM3Dlpdc0z0UuMzvfumUfSUbwijTyEaDlSSEUQxAJaTv5r7sz%2B8Sb16%2FNx8ZhEHmVqO26sPjtRkHkqcVNJOdnHIflxoRGHX6l%2F9%2F%2BymXZq%2Fru%2F2r8Sxcii2Znz5wRLSMPDN98kGOqUBHJvqRBM5PunCPjENcrJx9AE1frlEzQoU1tz9tZICQ0zOuSJUSB6AyHqL0oHdo%2Bml3qnx8pwuZHX%2BUkiOitk1v6IpKfbXJOYagG%2FVyWN3LAcjPmqiRQQlhRqAeybZyNyppZCFOhgeREcqFvBxwI0nfUThfUCxVRYMS%2BOQ%2FdVK3W2gNnUyR%2BQbNsV5BTmnJA5plshQiL3UvaBKYiGfFsc8gW5dz2wJ&X-Amz-Signature=2f9cb5d425c4187f9a29f3a82df1baea1380fe6d79ee4055020ed4c2faba0086&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
---
## [`.T`](https://pandas.pydata.org/pandas-docs/version/0.25.0/reference/api/pandas.DataFrame.T.html)
---
**Syntax**
This attribute allows us to transpose a DataFrame.
`df.T`
Transpose simply exchanges rows with column. This means that each index label becomes a column and each column stands now in the index of the DataFrame.
![[Simple example](https://www.w3resource.com/pandas/dataframe/dataframe-transpose.php) of how transpose work](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/8a8c29ad-29e1-4d93-8b7f-d11607362931/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662VGMPQ7R%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T222623Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIATqjj5QbPMfl7fRKeClbNVlci%2FzTo0Zy2U8gAyLPW6bAiEA%2BueES0iRw6%2BniZRK%2BqQblEg0w85%2F4M6vmj1mwzmI0gUq%2FwMIKBAAGgw2Mzc0MjMxODM4MDUiDJD0p08OHLagUVzbeyrcAxtF11WDpP5qNs%2FbzDm%2BGXpBBHz5UilXcseKS9knJd%2FTJCzOi9%2F7%2FxNt7FVLko4Iuk0WJWcCbc49BmjKinOPse%2BqT7H4BgEVQoN2d36jk1R2vw1qe98i76aI%2FPoA16q3LKrG7ma2RyaOGZ67yTvXoECCSopIyefP9g1lL1xVJpYGsvGUjien0LC3LOuLc1d4dll0Nlg2e0BDnYwWfxHiAWmCS5N9xFM83hFDvGBiNvfKResoCmccw7MRvA3MLAkwoPY%2BlQ5Z5jBImJFxXR%2BotbkguVDNFdMScDc8zzfRhz%2B3I1lMRYMSJ8%2FjjFBiBS4ierFpM1R7LUGaGljaL3q6peaxrgMf%2BC7ME6FA1nCubX0OdalLLMO8%2BJnBMXXMverAyT9OXs0cYYAOCPdow%2FHb6QzXAt0Lc%2BCq0Ga2AK4fs6f0yxHbFrskCLljn%2FLsY2URz7nob5NDTd7BU%2FRJGht%2B62wtJKDN3c3Vt1wrS15ZOf3%2FQIBw1jj6d4e2FoRenasWk4oaBPR6hafGrZOPt2DJ6zMJ3Exesaoovu3uuEW991ndLxRxuurYjGw%2FRBWP8azmNL3EgZT2YR9zFN0qjIF2hHwlmmdrTQtNDEtVLIuAkXqvaPrn00hJOm4EvG0UMMXO98kGOqUBkvJlp05NVNuGVhbw4cXgAEOZ5g79ZXCUuelgdOP73oKn%2BWGSZHVlJjF9TLDL%2FdcyTdKIRk0vZnBNYzrXYGlmPggelmthCCT%2FcTGPa30mRmvqmZYI7GLQ8aJIcvpOnE5MOvZTuMmrwSPLW1rWSTI%2FePoeiW41dGclwIZYvEm3Qo4aYljsd2k5dKRAZ6To58Of%2FDlrceoBnbpVXcrD%2B%2FhEYsBC6Mjl&X-Amz-Signature=f4edbf81f9fdf0f11604e1b77451b1aa1b6a7c27bb63959b0693290f38176c4c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
---
**Transposing a DataFrame**
Let’s transpose the DataFrame `outer_merge_df`.
```python
palyers_df.T
```
![Transposed DataFrame `players_df`](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/89702bec-4246-4790-9f9c-f88c8d756671/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662VGMPQ7R%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T222623Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIATqjj5QbPMfl7fRKeClbNVlci%2FzTo0Zy2U8gAyLPW6bAiEA%2BueES0iRw6%2BniZRK%2BqQblEg0w85%2F4M6vmj1mwzmI0gUq%2FwMIKBAAGgw2Mzc0MjMxODM4MDUiDJD0p08OHLagUVzbeyrcAxtF11WDpP5qNs%2FbzDm%2BGXpBBHz5UilXcseKS9knJd%2FTJCzOi9%2F7%2FxNt7FVLko4Iuk0WJWcCbc49BmjKinOPse%2BqT7H4BgEVQoN2d36jk1R2vw1qe98i76aI%2FPoA16q3LKrG7ma2RyaOGZ67yTvXoECCSopIyefP9g1lL1xVJpYGsvGUjien0LC3LOuLc1d4dll0Nlg2e0BDnYwWfxHiAWmCS5N9xFM83hFDvGBiNvfKResoCmccw7MRvA3MLAkwoPY%2BlQ5Z5jBImJFxXR%2BotbkguVDNFdMScDc8zzfRhz%2B3I1lMRYMSJ8%2FjjFBiBS4ierFpM1R7LUGaGljaL3q6peaxrgMf%2BC7ME6FA1nCubX0OdalLLMO8%2BJnBMXXMverAyT9OXs0cYYAOCPdow%2FHb6QzXAt0Lc%2BCq0Ga2AK4fs6f0yxHbFrskCLljn%2FLsY2URz7nob5NDTd7BU%2FRJGht%2B62wtJKDN3c3Vt1wrS15ZOf3%2FQIBw1jj6d4e2FoRenasWk4oaBPR6hafGrZOPt2DJ6zMJ3Exesaoovu3uuEW991ndLxRxuurYjGw%2FRBWP8azmNL3EgZT2YR9zFN0qjIF2hHwlmmdrTQtNDEtVLIuAkXqvaPrn00hJOm4EvG0UMMXO98kGOqUBkvJlp05NVNuGVhbw4cXgAEOZ5g79ZXCUuelgdOP73oKn%2BWGSZHVlJjF9TLDL%2FdcyTdKIRk0vZnBNYzrXYGlmPggelmthCCT%2FcTGPa30mRmvqmZYI7GLQ8aJIcvpOnE5MOvZTuMmrwSPLW1rWSTI%2FePoeiW41dGclwIZYvEm3Qo4aYljsd2k5dKRAZ6To58Of%2FDlrceoBnbpVXcrD%2B%2FhEYsBC6Mjl&X-Amz-Signature=5bf2df776d70efd2e4263981d7b62d6b3019fc7b6513e6d40f826de41c688989&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
We see that the DataFrame has now only 9 rows but 540 columns. This is because there are 540 players in the dataset and as we transposed the DataFrame all these players became now columns.
---
## [**`.pivot()`**](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.pivot.html)
---
**Syntax**
This function allows us to re-organise and summarise the data in a DataFrame and thus view it from a different perspective.
`df.pivot( << index >> , << column >> , << values >> )`
The parameters of the .pivot() function are very intuitive, we basically just need to tell Pandas what values should be put where in the pivoted DataFrame.
![Structure of pivoted DataFrame](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/ce3fbd7a-7ed0-4aca-813b-7b876b8a9341/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VLYLYHQ7%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T222626Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQDKryZxFiXy4DzNlnsq0XFIoXULyNS%2B2Mgy1AVicJN7jQIhANgoV2xXY1lY4%2B3b5k5zoateZAxu95tzsOLzUOj7hDfeKv8DCCgQABoMNjM3NDIzMTgzODA1Igw%2FQrqrWKDxXhmGpQAq3ANwTtfLJoyQq1Zk368XeFFpNgk%2BdCLdwJyBYtGgwaJlfKpYlZ%2BO5Aykmq0ZVxhRyZeIbyMpgjauZ2QFv0LlOk9E16MsoXY7ocKDi5e%2F1kYlJQeYTGO2xCDNvWM7qxxiVpHls1dNPJDHbtnDKPqGDH1ZpHlYVHQLxwpn6fvIzrgNnuv%2B3HBahb4xZmaRS5t%2BSBK6vaNxxz9g4RHnO6h6J2H9yPtn2lGC3A5uzppQmJwPOzUPPvtgLgt5Bomw43vFw9XlGmM0k%2BXrgG9xyr8JA53XQaZtXixI90tlRpf2wBDCMuRjvV8UUkWiz0UkqWGKRx30O78Mc4MC4Lyauhw%2BCa2PsdCdEgLs6ANbZk8s5kNl01tr4ibsQW1jlArZxGF0nuL3yTYi0fw7JqYvg7ZBvsSBWOVd%2FAVJdBiAMwkLM%2F4aeTs7SY84V%2BU7KBExSEIqFVT8EQWnMg10SDR1jDY5nvIfk7agX9VshWSP0Pw2uimjcj2Ik7RWSwaM3fbS4s4m28315vX9hrMc9VXnKW0u91xeo%2F2Ls6UAK26X79UZabf2wxftLRmhhJzftAFyv%2BGmGhNAWZ0n2XtINi90WO0U6ki1F%2BHwallMGYTu%2BG1SFadprFZMk3q8KJotl%2FSBITCOzvfJBjqkAT6aUwQggFocCl0zm2mxkq6xWLM38KdeCOBVMtgx1jHyeAQDxM7IbLSdL42VHN3Okd8%2BaOpjEgfuufqaRgL9rxDTEEJPuwG40J891nEhYjEYobKH92vorCk6%2B5JVk7e0heWizIk3cVc008p945WPSCZNBUxmcPPg%2FpcRbA%2BoYemLcx6VjWtWFRyPIp4dRxhzZaSHGwTYU7eEtmlD3dIYBbU3GwO2&X-Amz-Signature=c4e8c1b0439ab470a0e1f9dd1a5775b2c65bfca416b4661206e69d83727dbb8c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
---
**Create simple pivot table**
Assume that we sliced the 10 players with most goals from `players_df`, which gives us the following DataFrame `players_df_top10`.
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/3662a662-2783-4f3c-b27d-bafa37d5e277/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VLYLYHQ7%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T222626Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQDKryZxFiXy4DzNlnsq0XFIoXULyNS%2B2Mgy1AVicJN7jQIhANgoV2xXY1lY4%2B3b5k5zoateZAxu95tzsOLzUOj7hDfeKv8DCCgQABoMNjM3NDIzMTgzODA1Igw%2FQrqrWKDxXhmGpQAq3ANwTtfLJoyQq1Zk368XeFFpNgk%2BdCLdwJyBYtGgwaJlfKpYlZ%2BO5Aykmq0ZVxhRyZeIbyMpgjauZ2QFv0LlOk9E16MsoXY7ocKDi5e%2F1kYlJQeYTGO2xCDNvWM7qxxiVpHls1dNPJDHbtnDKPqGDH1ZpHlYVHQLxwpn6fvIzrgNnuv%2B3HBahb4xZmaRS5t%2BSBK6vaNxxz9g4RHnO6h6J2H9yPtn2lGC3A5uzppQmJwPOzUPPvtgLgt5Bomw43vFw9XlGmM0k%2BXrgG9xyr8JA53XQaZtXixI90tlRpf2wBDCMuRjvV8UUkWiz0UkqWGKRx30O78Mc4MC4Lyauhw%2BCa2PsdCdEgLs6ANbZk8s5kNl01tr4ibsQW1jlArZxGF0nuL3yTYi0fw7JqYvg7ZBvsSBWOVd%2FAVJdBiAMwkLM%2F4aeTs7SY84V%2BU7KBExSEIqFVT8EQWnMg10SDR1jDY5nvIfk7agX9VshWSP0Pw2uimjcj2Ik7RWSwaM3fbS4s4m28315vX9hrMc9VXnKW0u91xeo%2F2Ls6UAK26X79UZabf2wxftLRmhhJzftAFyv%2BGmGhNAWZ0n2XtINi90WO0U6ki1F%2BHwallMGYTu%2BG1SFadprFZMk3q8KJotl%2FSBITCOzvfJBjqkAT6aUwQggFocCl0zm2mxkq6xWLM38KdeCOBVMtgx1jHyeAQDxM7IbLSdL42VHN3Okd8%2BaOpjEgfuufqaRgL9rxDTEEJPuwG40J891nEhYjEYobKH92vorCk6%2B5JVk7e0heWizIk3cVc008p945WPSCZNBUxmcPPg%2FpcRbA%2BoYemLcx6VjWtWFRyPIp4dRxhzZaSHGwTYU7eEtmlD3dIYBbU3GwO2&X-Amz-Signature=1972e9292cc808156081aecfef4a028c30f0f022b7fe774a029ea72800bb5146&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
Now we want to analyse the Goals and Assists of these players in more detail. We can thus create a pivot table to summarise the data in these columns more efficiently. Specifically, we define that the player name should stand in the Index, the number of goals as columns and the number of assists should be the actual values in the table. We can execute the following command. 
```python
players_df_top10.pivot('Player', 'Goals', 'Assists')
```
![Pivoted DataFrame with NaN values](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/59679060-a9fd-444c-b16c-d3fec05c116b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VLYLYHQ7%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T222626Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQDKryZxFiXy4DzNlnsq0XFIoXULyNS%2B2Mgy1AVicJN7jQIhANgoV2xXY1lY4%2B3b5k5zoateZAxu95tzsOLzUOj7hDfeKv8DCCgQABoMNjM3NDIzMTgzODA1Igw%2FQrqrWKDxXhmGpQAq3ANwTtfLJoyQq1Zk368XeFFpNgk%2BdCLdwJyBYtGgwaJlfKpYlZ%2BO5Aykmq0ZVxhRyZeIbyMpgjauZ2QFv0LlOk9E16MsoXY7ocKDi5e%2F1kYlJQeYTGO2xCDNvWM7qxxiVpHls1dNPJDHbtnDKPqGDH1ZpHlYVHQLxwpn6fvIzrgNnuv%2B3HBahb4xZmaRS5t%2BSBK6vaNxxz9g4RHnO6h6J2H9yPtn2lGC3A5uzppQmJwPOzUPPvtgLgt5Bomw43vFw9XlGmM0k%2BXrgG9xyr8JA53XQaZtXixI90tlRpf2wBDCMuRjvV8UUkWiz0UkqWGKRx30O78Mc4MC4Lyauhw%2BCa2PsdCdEgLs6ANbZk8s5kNl01tr4ibsQW1jlArZxGF0nuL3yTYi0fw7JqYvg7ZBvsSBWOVd%2FAVJdBiAMwkLM%2F4aeTs7SY84V%2BU7KBExSEIqFVT8EQWnMg10SDR1jDY5nvIfk7agX9VshWSP0Pw2uimjcj2Ik7RWSwaM3fbS4s4m28315vX9hrMc9VXnKW0u91xeo%2F2Ls6UAK26X79UZabf2wxftLRmhhJzftAFyv%2BGmGhNAWZ0n2XtINi90WO0U6ki1F%2BHwallMGYTu%2BG1SFadprFZMk3q8KJotl%2FSBITCOzvfJBjqkAT6aUwQggFocCl0zm2mxkq6xWLM38KdeCOBVMtgx1jHyeAQDxM7IbLSdL42VHN3Okd8%2BaOpjEgfuufqaRgL9rxDTEEJPuwG40J891nEhYjEYobKH92vorCk6%2B5JVk7e0heWizIk3cVc008p945WPSCZNBUxmcPPg%2FpcRbA%2BoYemLcx6VjWtWFRyPIp4dRxhzZaSHGwTYU7eEtmlD3dIYBbU3GwO2&X-Amz-Signature=e1207b75d5febf5769bb184413dbd01fe3be9bf911dc4ce2888d8bd98711d098&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
From the output we can read now easily for each player how many goals and assists they have achieved, only if there would’t be these disturbing `NaN` values. We can get rid of those using the [`fillna()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.fillna.html) function.
```python
players_df_top10.pivot('Player', 'Goals', 'Assists').fillna('')
```
![Pivoted DataFrame without NaN values](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/2d52b792-ba61-4b0d-8ed5-5d7498041672/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VLYLYHQ7%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T222626Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQDKryZxFiXy4DzNlnsq0XFIoXULyNS%2B2Mgy1AVicJN7jQIhANgoV2xXY1lY4%2B3b5k5zoateZAxu95tzsOLzUOj7hDfeKv8DCCgQABoMNjM3NDIzMTgzODA1Igw%2FQrqrWKDxXhmGpQAq3ANwTtfLJoyQq1Zk368XeFFpNgk%2BdCLdwJyBYtGgwaJlfKpYlZ%2BO5Aykmq0ZVxhRyZeIbyMpgjauZ2QFv0LlOk9E16MsoXY7ocKDi5e%2F1kYlJQeYTGO2xCDNvWM7qxxiVpHls1dNPJDHbtnDKPqGDH1ZpHlYVHQLxwpn6fvIzrgNnuv%2B3HBahb4xZmaRS5t%2BSBK6vaNxxz9g4RHnO6h6J2H9yPtn2lGC3A5uzppQmJwPOzUPPvtgLgt5Bomw43vFw9XlGmM0k%2BXrgG9xyr8JA53XQaZtXixI90tlRpf2wBDCMuRjvV8UUkWiz0UkqWGKRx30O78Mc4MC4Lyauhw%2BCa2PsdCdEgLs6ANbZk8s5kNl01tr4ibsQW1jlArZxGF0nuL3yTYi0fw7JqYvg7ZBvsSBWOVd%2FAVJdBiAMwkLM%2F4aeTs7SY84V%2BU7KBExSEIqFVT8EQWnMg10SDR1jDY5nvIfk7agX9VshWSP0Pw2uimjcj2Ik7RWSwaM3fbS4s4m28315vX9hrMc9VXnKW0u91xeo%2F2Ls6UAK26X79UZabf2wxftLRmhhJzftAFyv%2BGmGhNAWZ0n2XtINi90WO0U6ki1F%2BHwallMGYTu%2BG1SFadprFZMk3q8KJotl%2FSBITCOzvfJBjqkAT6aUwQggFocCl0zm2mxkq6xWLM38KdeCOBVMtgx1jHyeAQDxM7IbLSdL42VHN3Okd8%2BaOpjEgfuufqaRgL9rxDTEEJPuwG40J891nEhYjEYobKH92vorCk6%2B5JVk7e0heWizIk3cVc008p945WPSCZNBUxmcPPg%2FpcRbA%2BoYemLcx6VjWtWFRyPIp4dRxhzZaSHGwTYU7eEtmlD3dIYBbU3GwO2&X-Amz-Signature=b5bb87a3a522cd7ab08229c8f0015d8c71496d5ed6ea48793b4df0f72f706868&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
As we see from the output it is now much easier to read the data. We just must keep in mind that the values inside the DataFrame represent the number of assists.
> 💡 **When doing a pivot of a DataFrame, the actual data is not modified. Instead, we only change the perspective from which we look at the data by selecting the relevant columns and leaving the ones that are irrelevant out.**
---
**Pivoting with duplicate values**
One very common mistake or problem with pivoting are duplicate values. Let’s assume we want to change our pivot slightly so that the values (assists) are in the index and the player names represent the values. 
```python
players_df_top10.pivot('Assists', 'Goals', 'Player').fillna('')

ValueError: Index contains duplicate entries, cannot reshape
```
We see that Python throws an error the there are duplicate values in the index column. This means that multiple players have scored the same number of assists. Thus Python tries to write the names of these players into a single cell, which however is not possible as we can only write one value in a cell. Concretely, the players that cause this problem are Danny Ings and Harry Kane (both with 2 assists) as well as Anthony Martial and Raul Rodriguez (both with 6 assists).
![Four players have the same umber of assists which causes problem when trying to create a pivot with Assists in the index](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/ad30fa93-727a-4e0f-9a2d-32466cefc3a3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VLYLYHQ7%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T222626Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQDKryZxFiXy4DzNlnsq0XFIoXULyNS%2B2Mgy1AVicJN7jQIhANgoV2xXY1lY4%2B3b5k5zoateZAxu95tzsOLzUOj7hDfeKv8DCCgQABoMNjM3NDIzMTgzODA1Igw%2FQrqrWKDxXhmGpQAq3ANwTtfLJoyQq1Zk368XeFFpNgk%2BdCLdwJyBYtGgwaJlfKpYlZ%2BO5Aykmq0ZVxhRyZeIbyMpgjauZ2QFv0LlOk9E16MsoXY7ocKDi5e%2F1kYlJQeYTGO2xCDNvWM7qxxiVpHls1dNPJDHbtnDKPqGDH1ZpHlYVHQLxwpn6fvIzrgNnuv%2B3HBahb4xZmaRS5t%2BSBK6vaNxxz9g4RHnO6h6J2H9yPtn2lGC3A5uzppQmJwPOzUPPvtgLgt5Bomw43vFw9XlGmM0k%2BXrgG9xyr8JA53XQaZtXixI90tlRpf2wBDCMuRjvV8UUkWiz0UkqWGKRx30O78Mc4MC4Lyauhw%2BCa2PsdCdEgLs6ANbZk8s5kNl01tr4ibsQW1jlArZxGF0nuL3yTYi0fw7JqYvg7ZBvsSBWOVd%2FAVJdBiAMwkLM%2F4aeTs7SY84V%2BU7KBExSEIqFVT8EQWnMg10SDR1jDY5nvIfk7agX9VshWSP0Pw2uimjcj2Ik7RWSwaM3fbS4s4m28315vX9hrMc9VXnKW0u91xeo%2F2Ls6UAK26X79UZabf2wxftLRmhhJzftAFyv%2BGmGhNAWZ0n2XtINi90WO0U6ki1F%2BHwallMGYTu%2BG1SFadprFZMk3q8KJotl%2FSBITCOzvfJBjqkAT6aUwQggFocCl0zm2mxkq6xWLM38KdeCOBVMtgx1jHyeAQDxM7IbLSdL42VHN3Okd8%2BaOpjEgfuufqaRgL9rxDTEEJPuwG40J891nEhYjEYobKH92vorCk6%2B5JVk7e0heWizIk3cVc008p945WPSCZNBUxmcPPg%2FpcRbA%2BoYemLcx6VjWtWFRyPIp4dRxhzZaSHGwTYU7eEtmlD3dIYBbU3GwO2&X-Amz-Signature=2b13b319ca0d942ffb28ab146903a9d860d085e0802bc94dfe11cc03774d64f7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
> 💡 **When creating a pivot, we must make sure that the columns we use as Index and Columns do not contain duplicate values.**
---
## [`.melt()`](https://pandas.pydata.org/docs/reference/api/pandas.melt.html)
---
**Syntax**
This function allows us to re-shape a DataFrame from long-format into wide-format. So far we always had the variable names as the column labels and each row in the DataFrame represented an observation. Now, when we melt a DataFrame, we put the variable names and their associated values into the DataFrame as well and thus we make it wider and shorter.
`pd.melt( << df >> , << identifier variables >> , << value variables >> )`
The identifier variables are the ones we want to keep as column labels whereas the value variables are the ones we want to put into the DataFrame.
---
**Melting with single variables**
Let’s assume we want to select from `players_df` the column `Player` and `Games played`. Thereby, the column label `'Games played'` as well as the associated values should appear inside the DataFrame now. 
```python
pd.melt(players_df, id_vars=['Player'], value_vars=['Games played'])
```
![Melted DataFrame with Player as identifier variable and Games played as value variable.](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/376279f1-3a8f-4131-b498-cada89cf6c52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XOBB65IL%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T222632Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJGMEQCIHaUCIL%2Bd3mXM64C2AffWCIViXauqvlW0tv%2BISAqnFOCAiBUFhHRZjDh56JKdhCbF2MXAnu7NXmeelnVmejz5HoIyCr%2FAwgnEAAaDDYzNzQyMzE4MzgwNSIMzLT%2FmEHx6ObfwXKyKtwD4nc1oi9KF2P9j7CQUESUGlB2Iy%2FMFALnR8iG9TmF4akHy5mIDxPJ5ziKipxtpNQHoOdqcS23%2BX%2Bz%2BQkDEjkGYgmuZE%2BFnJBIxkWb2XNyJZ1pMjPaI105X4uYF1rEM3devKpjn1FT7S36uUH1dC14SULlXMjgdCgI8N8vI42USpyeVXgcpZVpMm%2F1j8OW8xIBqxHEoMubonoGtqptf%2Bgp8BpUdMfgA8db40I2NfE%2FZJdHsTFqzbxXsZ2kc4mJnK424mJHNl5JFAXdXrHaesPbOemZoI98uYzLCRBtG6ZgkaxjuCxJQYSbsy%2FnjvKNLxQCEuoFzYlMxlWAvpvQ0KuwycdJbcxJ2HBLrOLoCp0MEnFYYAyc2VCXjNmwqqON8amFCbePsWq9XRh9OB80kv4U3mcdH5D5kluwJYmeyIH0q5R71U7zJA0%2F9tDsy5NTgVl0oeC4oy3M%2Bqteghxb2Z47k1cB2i9XwgN0NjYwpnF0gkiZA00uPevq8svaZtZP9CaxTF%2BL5SHYjPMO9RcueuyuvCgH7FTOPjIejDsPskF2BrvIlhRVxiO7KhkAw4UTFaR8Hn%2B1I5YLkWfS%2BAySbDWo5HEvHhKZEoLLj84lxFDEmJm4nLTf87c9mMZzh6ww4833yQY6pgG%2FyCY0p%2F5aIH3mD4%2F%2BxWoQNZbxTqqccQtm%2BhIXbEeR3A0crDoydy%2BcXGhsywkgMdKmv3KQgC3PAw12KFgo5bcsAkfe%2FlhSjTtU%2BaDx3%2FhG8YElwNdP1hmzxhxznxtMKtVNl2HJW5uqDR4EPVFfp1f7kM3EhA5Y6zp9GggKsbThgjTikhoOb6kb580QifW7Q64Lbb0IN64xAUnyF4Z%2BQJeDhk%2FQ6JAC&X-Amz-Signature=8a3ca657a2a33da81692d16693cba2a89110fc698e8380360ba265a75c17b948&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
We can see that the column label `'Games played'` is now also a value of the DataFrame, thus we now read the DataFrame from left to right, i.e., in wide-orientation and no longer from top to bottom as the column labels, except from the identifier variable `Player` have not a lot of meaning anymore.
---
**Melting with multiple variables**
We can also pass multiple labels as identifiers and value variables to the melt() function
```python
pd.melt(players_df, id_vars=['Player', 'Team'], value_vars=['Games played', 'Goals', 'Assists'])
```
![Melted DataFrame that contains multiple identifier and value variables](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/2d3d4d02-c126-4579-a159-9c1aaee826b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XOBB65IL%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T222632Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJGMEQCIHaUCIL%2Bd3mXM64C2AffWCIViXauqvlW0tv%2BISAqnFOCAiBUFhHRZjDh56JKdhCbF2MXAnu7NXmeelnVmejz5HoIyCr%2FAwgnEAAaDDYzNzQyMzE4MzgwNSIMzLT%2FmEHx6ObfwXKyKtwD4nc1oi9KF2P9j7CQUESUGlB2Iy%2FMFALnR8iG9TmF4akHy5mIDxPJ5ziKipxtpNQHoOdqcS23%2BX%2Bz%2BQkDEjkGYgmuZE%2BFnJBIxkWb2XNyJZ1pMjPaI105X4uYF1rEM3devKpjn1FT7S36uUH1dC14SULlXMjgdCgI8N8vI42USpyeVXgcpZVpMm%2F1j8OW8xIBqxHEoMubonoGtqptf%2Bgp8BpUdMfgA8db40I2NfE%2FZJdHsTFqzbxXsZ2kc4mJnK424mJHNl5JFAXdXrHaesPbOemZoI98uYzLCRBtG6ZgkaxjuCxJQYSbsy%2FnjvKNLxQCEuoFzYlMxlWAvpvQ0KuwycdJbcxJ2HBLrOLoCp0MEnFYYAyc2VCXjNmwqqON8amFCbePsWq9XRh9OB80kv4U3mcdH5D5kluwJYmeyIH0q5R71U7zJA0%2F9tDsy5NTgVl0oeC4oy3M%2Bqteghxb2Z47k1cB2i9XwgN0NjYwpnF0gkiZA00uPevq8svaZtZP9CaxTF%2BL5SHYjPMO9RcueuyuvCgH7FTOPjIejDsPskF2BrvIlhRVxiO7KhkAw4UTFaR8Hn%2B1I5YLkWfS%2BAySbDWo5HEvHhKZEoLLj84lxFDEmJm4nLTf87c9mMZzh6ww4833yQY6pgG%2FyCY0p%2F5aIH3mD4%2F%2BxWoQNZbxTqqccQtm%2BhIXbEeR3A0crDoydy%2BcXGhsywkgMdKmv3KQgC3PAw12KFgo5bcsAkfe%2FlhSjTtU%2BaDx3%2FhG8YElwNdP1hmzxhxznxtMKtVNl2HJW5uqDR4EPVFfp1f7kM3EhA5Y6zp9GggKsbThgjTikhoOb6kb580QifW7Q64Lbb0IN64xAUnyF4Z%2BQJeDhk%2FQ6JAC&X-Amz-Signature=6e9bd6229ac4d8e577822ce8900e9cedb3bedd2101e39484d18abfdd31e6a9b3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
We can see now that the output DataFrame contains a lot more records (1620) than the one before (540). This is because we have now three value variables and thus three times as much as records as before when we had only one value variables. 
To understand what is happening in detail it helps to look at one player only and compare the melted DataFrame with the normal one.
![melted DataFrame](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/e810c7eb-a76f-4663-bf34-e5c7d9be01a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZAWJBAVP%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T222633Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJGMEQCIGe6bHTwNH5rsHLosHjQNTo94iaPgq2aZFLb8XX4mG2LAiBGtXU60cqdIqDASX37SjiTeo7LRHI8y4r0Nvb637lGmyr%2FAwgnEAAaDDYzNzQyMzE4MzgwNSIM0SVVxD%2FY8ChOS6SXKtwDJ%2F4yeqocLXbhRq9MaEnXFT9V1apccTi5L7zk829Zn8P0TzCcup7OCmzCZm%2BKII4nbS9aiLplBzJReTdI0zf396CJoiXvTbpR%2BFWSEkIuf1OoNTktqb8ERTZ50evxS1ZS8eLi1uw9%2BVk4BmH1qeFML1Us9e%2FoPoefb2i12aru3RGZX2RbsXMvZkyauUZ8s%2B70FeOn80QCryoflzLagS9ZjgrN%2ByRA0xDxEF1R4yKHxk%2FlQWylnNPimEmoZqtYFcpkc%2BAoqiLSSddVDtW7IYuRiiqpSDI%2BC8WEdq5phodDt5yNnuZOscWVx3qhxhz3qw7R%2F89ryFolmOLXcLbt%2FC74SIsG9hS4px8JfDwrqlqYX5QGx%2BviYQLlCwuSph5qy7ipaWCLugrIJqsMbzvxWIyAJWrubFm%2FaVuF4cADEq%2F9Z25y1%2FUn8cNCwtog%2Bc1kcbkG64IymWVVGTxn%2FUqc%2Fnybu79DbGDnUlLgf9jsa1Go%2BgevEYvFUQuWLhg1q7%2BAoHIfAFsa%2FPPOl38cLEiZcH3gHouqJ3VXjHlhCeXoGX5lThdCE%2B67lOjOIAFg5cQMe4bNSa5p4gOoqPpNtDBRSC%2FUz%2FGEkpjxFGpscBzw2vvuLWekswSOZZz7OfEEWskwoc73yQY6pgHoNgey8oA6rUqdSIc1%2BgnKq9b5C%2BB1wNYLZqkX9%2BsiE9xDyOpYKR4IHh9b2u2nXxiC%2BVj2TS9f1rt%2Blvfa6W1gmePTDFSWFukzKFEiSIwXfq0hbldfuGPnvvBOiWdQfiQdeD5TVggHQgIAuQllb%2B5ik6BI6p5FpToehNRuxmZSyNXkEd7onTOzlkBihGve83QHUXKrDJjeodnHqYvBXW2%2Bxsu1Ae88&X-Amz-Signature=f22c0d5a09fc4b27ce0d2dde0e13984ebacf31931809ffda7ecd547642f6b165&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
![regular DataFrame](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/5782aa33-0a88-4833-9ec1-3545e2cb104c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46625UDBNWF%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T222635Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQCrNRaGsBehb%2B9h2RKMIt5IhYx0fXAQWC6sVQboRgWRxgIhAKruoqZlH8JTmVduMOVE31%2BDYp%2FI%2F6G7ZNOTEDMSd05%2BKv8DCCcQABoMNjM3NDIzMTgzODA1IgxQROAAVe1CzgtLK1sq3AMIMhtvZlLzHMINLcRYaXwBigxA2o4QB0lhnDqca%2F%2Fx0vUAaqRJZWkWcVk1kkLyZebnFdympto3z9hF7TojxNhAuLHfH1n6etnyB9I4GRzwih0JS1jEC2QfPTCZyWlNPzKrYTGex%2B48sBoISRBx7lkETPHBQs0JBiaee9BUd2BFPLBubYFyifr1HulVlhFVXpKM06JvLskyJYlkkvjNBhf00YhFeQ%2BRP1dDnwEce5JTZk%2FJgYbNd5VLJOtvjxksNhOUt015tBPPIJ88RQg%2BjyFAwx%2FycVfUgEBrG9R%2Fw6EugOU6cr%2B9PDx5cEmRBGCVNheXDC9eFH1T5%2BXwygG5V1wnVDSfdqoytOHaafRUAUjfT6Z6Wc9OqPmiJWKn92LNjcshX8oJz55LwTe54vMkIonFeQF41Dvvlo9u1yg%2FZPrm%2FdOzjsRSHXffxZVlkZjPTfoUzZ8JU8GfSyYGP2%2BL7oiqFi2BUlgzEqyloUoz6G%2B5wF7vp3T79jHxkMUacSbCZqnlfR0fLY%2FYpgkLCLTbgwv926qFQK%2FQRl1loJhLIkMnUpWN8MA8kSqT2BZgpierrKGzvcUtlOem4CbodxFfMIEsjaAEwrspovGumuGWKDIB1OI36v5UHrW%2F75NXcDDnzffJBjqkATzR%2B%2BoJ6sj5cfX390Q9aTAq31u25hEOp6zWNutrGYCtyp45vPl07GK1SNK015DdpW8pox4d2RrLpOmwJSR5HZtb0M5CKFlcZxXSzsQEiU2gxR2KRpX01fmOeS2IU9UbwUVQ5TdZyTqW6Qz0vTDDcjJamaMPiLjDf0DwcDPaenA4N0Ch9QXaWvywb5Rb5R7eCVBmVaMhx9EIt9BC%2BV0Gbgy3cWoU&X-Amz-Signature=26b93086a10b83146a74f0ae54269ec592d7de640800a9bbe54b4aff14646eae&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

We can observe that the melted DataFrame has more entries than the regular one. Specifically, it has as many entries (three) as there are value variables included. So this is just a different way how we can organise our data.
> 💡 **With each additional value variable, a new row is inserted into the DataFrame for all observations. Thus, the more value variables included, the longer / bigger the DataFrame becomes.**
---
## [`.Timestamp()`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.html) & [`.to_datetime()`](https://pandas.pydata.org/docs/reference/api/pandas.to_datetime.html)
---
**Syntax**
These functions allow us to convert dates and times into the Timestamp format. This is the equivalent to the Datetime object we have in Python. 
`pd.Timestamp( << datetime-like >> )`
`pd.to_datetime( << datetime-like >> ) `

> 💡 **`<< datetime-like >>` can be many things, such as a String, seconds passed since the Unix epoch etc. The important thing here is that the value passed into the function can be interpreted as a date and/or time so that it can be converted to a timestamp.**
> 💡 **Both functions are extremely similar and can be used interchangeably. Both  take some datetime-like input and convert it into a pandas Timestamp.**
---
**Creating timestamp from string**
Let’s assume we have a string and we want to create a Timestamp object out of it.
```python
date_string = '2019-04-06T12:30:35'

my_date = pd.Timestamp(date_string)

my_date
Timestamp('2019-04-06 12:30:35')
```
We can achieve the same thing by using the `.to_datetime()` function.
```python
date_string = '2019-04-06T12:30:35'

my_date = pd.to_datetime(date_string)

my_date
Timestamp('2019-04-06 12:30:35')
```
---
**Accessing Timestamp properties**
The cool thing with Timestamp we can easily access and modify the specific properties of this date / time.
```python
my_date.year
2019

my_date.month
4

my_date.day
6

my_date.hour
12

my_date.minute
30

my_date.second
35

# modify
my_date.day = 8

my_date.day
8
```
---
**Insert new column into DateFrame with timestamp value**
Let’s assume we want to create a new Timestamp object of the current date & time and save it in the `players_df` in a new column called `last_updated`
```python
current_date_time = pd.Timestamp.now()

players_df['last_updated'] = current_date_time
```
![DataFrame `players_df` with new column `last_updated`](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/8a1db142-80f5-44af-8755-ffad5c54575a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666P22XZLX%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T222635Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCICW1wGkokoxPp%2F0C0OThpQ2PRD86Yy6%2F2jpiHGN26IfzAiEA%2BFkc%2FDdzwnB1MUTV%2FqEKrGwQsHJuettzyPg0pK%2BEuNsq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDHE8QIUNTUWVaj4qKircA3udQt1zJfiiMX6hbW7EH7XL0Y64Rbvp%2BE76eBnB7JuTu5KCOi3QtexSpp64xprR9FOo5Kihp6ghi4f8fd2841OfQ3KpqdbiHNLg4xPgY3%2F0LB0VwGeV4UvQp59VKDhCOBY5HDDgWNWuhbJ7zxDgaA81O1T7cTl6mAzGXBuePl%2FyfSU7pkXR2lJ9LWehQBvwWe6p5haKzZz9Lj1PyLa8%2F1lxhQYMHyeqr8%2B0GN5%2FuN%2Fn8ebUIdMKjNBUQntkimLF5el8Ovf%2F5MJ4JOXbPeJbGFnpkM06k7pJvxyX1KX9f28GIQNwcvx9Bcgoy8J5fLuARZ9njW6eaQ7BDqawIKxIiVbXnukF%2FEh8bcMHHPkVu6kpSSEY2ninQZ5VXib9UOns9JUys0UcY9dD9r0szcjYUHNwivegV2Q7XEZdtNSC7i8uuOg22ZbDt%2FYZF77gQ7GCZhpcp1rcBI6Z4yziIuy2rjqOBDS30kalkLGx%2FDpESkbcI%2Bxbu%2FfMIXJmAsaEYKsDnZhqBuyD%2FvSEW9cior%2BBWGO3Whvhh8%2B%2FPgmCQhdc4z2silNjgi4kRxay2NSgXpzG1QIiDZRwPKIWPzfHdOIDOHd86bzCC2juJnaJ6WyjEveqNtDAqMv%2BId9HbNjSMPzN98kGOqUBpJFvMIathT%2Bl9OczHFpB6qITsL0gw5DPw1comndYCM6nO9LzTUDSD8cHLHX%2FD6ZKfvEYrjYJyQSl8rUswfbg47LT56fK78i58%2Bd7acB7kb9ue%2Bkv1yNXRE6t%2FdoPgFXiL9C69xZabMoCyrkR7LhkHi6XE%2Bo0X13%2F8N5Lluwipr%2FvNC0P4IIiMW7IVjz9PNGGafOyHojH3lICwCpA51pxtWxYm2%2FL&X-Amz-Signature=bd9684cfa917a3fa9ca04f30ab02e9be31817c82e1c2314a224d2f1f05856b64&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
What is the benefit of inserting a Timestamp object instead of a simple string into the column `last_updated`?
Firstly, whoever is going to interact with this DataFrame will come across the Timestamp and thus knows that it is intended that date / time information is stored in this column. 
Secondly, Timestamp enable us to do calculations as well, such as calculating the difference between two dates or how much time has passed since the player was last updated etc. etc.
Therefore it is advisable that whenever we deal with date / time information that we convert it into the proper data type.
---
## [**`.Timedelta()`**](/1a11208373ef44358aa1528a5dc7e807)
---
**Syntax**
This function allows us to create a time difference in any kind of unit (days, hours, seconds etc.). 
`pd.Timedelta( << value >> , << unit >>)`
The possibilities for the `<< unit >>` parameter are quite extensive such as:
- Days: `'days'` or `'day'`
- Hours: `'hours'`, `'hour'`, `'hr'` or `'h'`
- Minutes: `'minutes'`, `'minute'`, `'min'` or `'m'`
- Seconds: `'seconds'`, `'second'` or `'sec'`
---
**Create simple Timedelta object**
Let’s assume we want to create a Timedelta object of 5 minutes.
```python
my_delta = pd.Timedelta(5, 'minutes')

my_delta
Timedelta('0 days 00:05:00')
```
---
**Comparison between time difference and timedelta**
Let’s assume we want to check if the time passed since the data in `players_df` has been last updated is bigger than the Timedelta `my_delta`, i.e., if the data has been updated more than five minutes ago.
```python
time_passed = pd.Timestamp.now() - players_df['last_updated']

time_passed > my_delta

Rank
1      True
2      True
3      True
4      True
5      True
       ... 
451    True
454    True
471    True
472    True
501    True
Name: last_updated, Length: 312, dtype: bool
```
As can be inferred from the output, most players have been updated more than 5 minutes ago. But let’s use the [`any()`](https://www.w3schools.com/python/ref_func_any.asp) function to gain 100% confidence. 
```python
time_passed = pd.Timestamp.now() - players_df['last_updated']

any(time_passed > my_delta)
True
```
---
## [**`.Period()`**](/1867045b058343e1a66b677961515907)
---
**Syntax**
This function allows us to create and store a time specific time period such as a month, quarter or year.
`pd.Period( << time-period-like string >> )`
---
**Define simple time period**
Let’s assume we want to create the fourth quarter of 2005 as a time Period.
```python
my_period = pd.Period('4Q2005')
```
We can now access a multitude of properties of the time Period object `my_period`.
```python
my_period.year
2005

my_period.month
12

my_period.day
31

my_period.day_of_year
365
```
---

