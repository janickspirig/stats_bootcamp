---
title: "Pandas"
notion_id: "1867045b-0583-43e1-a66b-677961515907"
notion_url: "https://www.notion.so/Pandas-1867045b058343e1a66b677961515907"
exported_at: "2025-12-13T22:09:59.611973+00:00"
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
![Simple DataFrame with 9 rows and 10 columns](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/de8c59d1-37e8-4920-af3e-954b9e1b1bd9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QUAFPSCA%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T220831Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIGYaPWr%2FX2aKCNS2lXUGtKp2EaAWcGixC733rY1QDtzmAiEA0h%2B%2BhYIlpBN7rHHiXowORh2V2H%2BPjXpAB%2Fv%2F42B3yroq%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDCdZHB691rJJ1WZuwSrcAx21DBER1Q85tMsnt9%2F7MTWq0k3d1RWhjpoUZEiLE7YfB1%2BtkhitfVr%2BMyc5TltTMQrotSv74GC6uYPvSFUDLWfcTVkocxjg4Wc3Akoyn55DolA1ALlQkhfEIKCZlTWLdWSWdlj3PqG12HH4GGLIuqAlAF69k6PgXgaz%2FDfC%2FMlt9DThRR6osU%2FtE1Rl8190VEoUjq4%2BOWY%2Fpf%2B3NVKRXXd3FbvTcTr44j8lqbgJE6hrLuthZT20SzNrL1n698yyg%2BcbY1ufBfTLGHwzwtgE6tfDhu9G0OYUMMkCkvFiGBI707L%2BbFFPWqbgInMzs6UQC6JBgNR%2FRj43SyUI9mzVfHUIsHDo5nYvUSP4%2B8RinEG6X2%2FiCqKfkuGKxADTXAz4AEVNa8DFevO4v5eCZL5MHhxUpnd6g8vqmo8swEAfMRPF1pLRuWjCEudbtr5KsJ4wA1qQVfvSjw4FcLsLooToyDNrEDBqGhzPfYuwatdrA3T6YZo0Ynb%2B73bdGJMGHExjgNNF9XKIkgEAW5FCK2ElCAmvXJKWvVXAvJ0mPO4ce4JHEEmn3wHkxRZcZ%2Bwnrf3FbuhaQugXpa9EoZMaz%2Bcy7P0vjE2ypDkRJpljjDu7OeZPv3GsxlrTbdADbjmlMPCl98kGOqUBPifPfK8btq9UwgOL%2FZNn91gCeZ5Dj32DjHoPcanrsVIteBNfGC5XAGQSoqVlnRbA1L%2BeBjcx%2F77difKEjSNiok%2B%2FY%2Bl7j2pcgU%2BPXtp3FJYONsOqwkkVL9bayZvpINIFLySfLuwadHxXhTHfAXO2O06P00feJnSR1DKWwjwUzFmVSgdyxQ%2BjVhd69XSQGY6E5vqynSkFHg6XKZ7KFL2r4ooCxWTJ&X-Amz-Signature=21f74834ab1273c9d7b97ac75d83d56d32f2ddad099374b34986de1194a5aaec&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
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
![Example DataFrame](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/a223167d-99ac-4364-8674-1158014b0574/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ULF7VMSY%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T220831Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIGWp%2BVCw6P6B00KE0RQDRV4cKWY35UpNOuYSorhAV4A0AiEAgJl2tIB5XQZjTXo%2B75ORTKIvOaWUVp%2B7%2F8TxE1N8se4q%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDMkaqpoCaXaWQ1UcoyrcAzGoNOAhAX1AfBFeDFeJvtB%2F7jc0OLZqwS0NOqYcIfX9Rhye9XaIgIcWKMKe%2BAcRgXMKfyTT7%2BBTIXhNESRhFwpOV%2BK6%2FWK6HHkImm6btngowqz%2B9FtNijvTK0RjCOSvPIpGXvbVmYY25SZGFHaUyMaMahHxAdCl97JOMSwWAFko2XuWhlgVTenP4jdNLXtP9Kale2Tqx6RKXPQ5dkEmSqstDw9PvOzqnYPy25L%2B6p%2FaRkwGVFerMs%2BW1wFimRP7bimcTGj1G4DDlMRyTvmqJJnXuZb2UddAxpS94EZ3Fb8hcmVEYwYRGl7YftBMAu6Lb9JI4h334FQmbn5TdTRGlWtGQAw%2F0przNW5l7bDhdLWhNqfd16E2adR7JHYascOWPAhSVZkcWSSGuGosWEzJcuFanCO42rfcPcPzBtWBxpts8hYRt2CC1xacDmV6RG9kpleBj6DSlVxr2XG47RyyKQFMArJhnam%2FrbgtdVQifyoLS4dNGL5R5Ntxuuj3Pj3Ri7dObJSiLl%2BtBIczuvNxVpe7gqBYivcOdmKTELtdu8dPedYFVNT0t3ORkuzXdZvRTQg0GR0kYcHTQD%2Fa6bVEioHldCwKhj8EG7PCAH7TACGLZ79RY%2BQeuGRQHbM%2FMP2l98kGOqUBR0hpgCwp%2FPj2EhIoHN9054YzrBE6eMtBs4%2FTShlHvBVk4yrDr22X1diX%2BrhoSd8TqhtNK5UB3iS5dMuPFTT7lCQHxdWq7bDKt4av4LAxlaJzufCBRU2FQZOhwZ47LGJU4rTHTdTLMqANK8jOeam4qX82iR5IDtxeey5lko0zm%2BwHcyroLW4MAsXTWJzD6RA1lERoDPWjrAfILGoAc2TJqaXx6DwZ&X-Amz-Signature=a9a1fb138af00e3d634f9788c1d35eea2d5dbd579cc42360d9985a07a99a5dbe&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
As soon as something looks similar to this table, we call it a **DataFrame. **
---
**Extracting single column or row**
If we extract a single column from a DataFrame we get a **Series**.
![Extracting a single column](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/e7650b7b-8ba9-4ae2-bb45-1fdcbdec6206/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XSQM5JIZ%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T220835Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIQDw%2FuJ7f%2Fbg7wT37vnF14kknXjAiChsCut9%2B9QD059BgwIgN7VWpg1hnEFXLngNCfwBBy3f3e%2BdMoUGsPdmWmy14V8q%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDPY7wciensK5kB2dBircAyYT4pMr4MrFFpPHc8QVp5nEMPn3LhzdYd%2Bu52RhI4P0eEnf6HS%2Fc%2B1IpahhyO8wypFGv88zznlMoyxAKsQ6bgcd1nUTIjahXCPfWcxqerP6RwG0PpTxdY5H8MCx34Tvb%2FCjAtOSfv%2BsHIfox43sMVbrQA8xMylsBYD955LDHTrXoH3yeflIUjdq3mUXjGt0VgmrtbGHVOg14ZUqxS9GXzI6R%2FVHEDZkrmfgFzzc%2BKQyzbwH3SIPizyI3zJooUfcT%2BF6kmmfCOkeCAy4aifjSJvmlJnxdRSRJYHmFwIZ4%2B8%2BnV0b40VIlvF451xPnKPy43l9W%2BI1cGTQTBDioMMdWyPBiLpVTIwKPXfPoUkAy61CULyuaLm2TYyMm38s%2B7UXlXwHbkhrop%2BFAjmbMudqWNi0AWH3OJAcRc20a0LFoaLVgn26oZgJ4LcW%2BSOXhccibJQ4iScD9gPOU%2F%2Bd5BQJM9nVbL6sBmx53vGpzNvI9O0mR4FBCD5i36zH3SG8Gn%2Fy3kV9b1rvgC3QZFh1spJ2%2BAPi4gGNlzpAAWRlpfKpErVD7K8orlxkDl49bCrew%2FIdJv3CMzaR7yjiYNLB%2BctX0TBujCaBRPs%2Fza1%2BLIxQizUK5Y6QPwWCOnQcnAi0MMul98kGOqUBItoNNGC%2BIHATvRBLTepSJo1jr3YwwZdgkLYhdDCpQ9fgcBh%2FLeDW4iNCWWN%2FVxRX99XcnxkrC%2BMpFyaaCUmWTbJnVLgmk5dCSefyISqo8MEXo9lSEivp8IS2tPCEsn9nrfXBW7ckxllR7x2cDMGT%2FgkuxO3MH2x%2BxzQ7ZhkRTa0VV9F1I9CCBbTWuad%2F5xvbsinZLfqwpo3EXJ2aLfWfPLKHFCkx&X-Amz-Signature=675926e95943940cc1d0014b1bf4ebb41d104a6420a28283282ef0dd58bedc83&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
![Extracting a single row](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/1fcd5fd2-ff89-4f7d-aa67-5c69c6c8077f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664KA3YRPL%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T220837Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIQCA%2FgKO94wlB8VlXXN9bnQkkolBuYzSVW3u%2BXI123q7%2BwIgFOvA7W%2BAznja3hHC4fCEpg2id0wUMsq87P%2BhSCYDrXMq%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDAWKpzepiua702l8tircA98LWcaZwdJfTl%2BH6vz7jr1E%2Fbkec0mxkMh%2FevvGnwoprrU7zFEzXQGFmBjFrIhg8%2BfnKP5Ezr6s75N9QFkbdj4CZtKxPXK8Z3ziHY7Q62d53MHcFxohynx9KxGiZhi%2F14jHpI1brHS6MnPlipZHABbkheqIMx6JR9rebxA2vKoCvL6mVoidegxXLGvvmk8CAdb6BKAs%2Fiu%2FfDUJoTEB9sw8js2VaLFVOdhUCSRBsqGPvpCHPqIIhhtqjSOl0m3h6EkI6ewSCBDbFSXLzsWmJPsRlSHB5eaSpofgDt07UTtSxyq4D2r4aW08jLt%2BmK%2F0HHrSqgy8KjvOEGuaBIruKdwMY1ZsrqQDVLoN923q0mEY%2Bz7eEIQ7oKPVlBHkIEJrwkmHEVIlSZx%2FRkx6pBwzh1362OM5VWoEll4dJdA7Zxmy9f67DM%2BIcNI3y6xBi%2FjUYydlTuF6ycczQVs9vxWT1Jc1zLJdQRTuWd4aVPKfsWqzIn%2BXLd5vTefoddEVgUaXrx3lXDl3RirH5fvw3nV4YFlFAqPK8UdD8hOTFROw2KuiBXcdsFT0oBUSWYP8FnfUcme8wU7eTuNMbw7Cd70noFEK%2B0EYGh810b9vwt9TfUD%2BDgsXAC3oAN1%2BjLS4MMSl98kGOqUB3psS9wehIJhtYqiYDx%2FU0pzo3B81CAJ%2FtB6yAaqgLbfhCEQmngtsSL3MZzJAaLoidLf0fNn4v9kzOr7JMF3AyK32PVxSwxssqYb38slsQSrD0ZPdWiOA0xON2i8BrmEJq2dfynyn0wW2cTYKd1jHJfDhDsq%2FfCs2CZ7rx%2Be6DHI6B8Tk84jDBIc8BNeijufx7rIX1irjahZh6kPsU%2FRYQNdExbsu&X-Amz-Signature=ff4c8ad1c6663f2da3084217c727177e0b02388be08013af224852894b902933&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
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
![Extracting multiple rows](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/db277268-1e26-4fc0-baf8-b8c8daf05ddb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VAXPQ4HY%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T220838Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJIMEYCIQD1AyUZoTvUWHBV5asBL%2BsXo%2F281ZVsxJzAMx0O543lcAIhAJBUz2AeBX4lXjcYaOAwgjO8QI8Z7SaQ%2B9qOvSv5D3JAKv8DCCYQABoMNjM3NDIzMTgzODA1IgxUsFidRKP6pMW1Wr8q3AOzyqnG9UWBqIhHjJQ6T4dudtEYmavrOSGoKhgCruKJ%2BXTdNR196YyacSxz7sORc3G38BdOO%2FgdclG%2B3dgy8N6zES%2BhHeEnceqpI7aJgOv%2FVBK9M1VYn9Lq%2BJ4qJzl%2FJVFwFCCFwbA1RGLK8PuNsFLAgQJTh7iUxgk5HMovMElkgah0Csm%2FMOwsEOZKSFV2GE%2F594ENUBfwR4EcHJyzMU%2Fo7ybNL4KOuC8T8%2FG%2Bv7OJuLcIzpvPrlHW11k7LdO5yCDLkevGuK8Bghj6%2BIyyB09bGi9oy8KTN1TYA8sGG3aMlnKnIhc9npAzUP6rr9PETTvhDzEXx6j5UXhJ7%2F%2F9DIRBzhm2GtldiEOXFQSrulFqRhjLsYzrc6moqr3rvlgDyJyvlzzQc01lEhN0ZH2U4AQWaIHqKaQvlVnmVngUb1WiOJ4UeKtQImnKQpZY5tOr9L%2F2CoMHimA3LmQxJwF3Bq%2BpV%2B1nXE%2FX1SiUSEXcE0ZxL73EluBDOicUgoI6VTIYKxoTDukZKtlOSvyg%2F3cGrfshgjU%2F%2F0htBKmT0fLFwqtCZ99mY%2FlpblLhAoW%2BX45ycCgL8heXXNbAFZejaArtwvwc5xQpDCKr0nzZEicS%2FyAAASOeq%2B41YExzql%2F29zDfpffJBjqkATGMqxz0tTKjrshIz9maAMgxROa%2B2tNDpOijR%2BQOnZD6SqlTz0fPQKWDQUXt%2FzrUnynRdZoecyL5BnL%2FBIpCQmvFSA800EdISr6XBQNibrM%2B8BxGsuZzxhTzeTlFll%2FOfoAj009EktOez2N3NagHsuMP4iY7gMHFR%2B6bSbMaXb%2BfOtxw2W2Uss5iIS7m4PCwaogT3kiDaWmW2IEKZcblnLLNN%2F4O&X-Amz-Signature=8a4feb036674a0c4c922b102672da0f8783e9dc5715e4f00a07abcd530ac689c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
![Output when extracting multiple rows is a **DataFrame**](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/53af7edb-d0d0-4ea4-badb-fd3589227085/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QSGEXLKL%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T220838Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJGMEQCIBH%2F8FW5hj73SyF3sF7azszRMf5m2dniiMZ98SYd8LRfAiBR9LCiPA22Ty5ytL%2FCmECgN1cPw1NxGv4IEkCYZWKMQir%2FAwgmEAAaDDYzNzQyMzE4MzgwNSIMas6cRRKD5qDmLu1kKtwDLTpzsLqI9o%2Fyu376XkQEx8hMV6PaX7k%2FzhTH39p4p1o1uO%2BTH071fSy%2FbF03jlC2fRFWUuPU%2BzqS1mxwkbk8JtSflBgdakwX6WPt9dmoJYFgkYcnWAwbk7isnpwNYLW1CXZnFBll98DpmJBliTIKD5SU9wXQrxZjXXnsmyED2EBErR4w9b13R9kYolJIbgsbTB3P38L30mrbWunPTvwor%2Bb7162Y3YXhJabdxsTT3eJTn4%2F%2F%2FswWbuECaa1YqAOU5k%2FYp7WPSBIqUGI5iyxVxC2pJWhcmpVozS91MqFuWZhs7qbf%2F1C%2FoUqPOAWfv8toJLguNtZA4YPuG0XXpWd5iBQtBsvuGQFG8p62fyl998ZXT%2FWEK6ylyo%2B6Ja6KZ53Tw8ej7%2FpLWfyj9qwTpiI9IszgYrYFSWjeLrOlySXWOqUgmf%2BjP3k95pMsHU4GScZ5BRUaHwszifh6T7GAM6NyJqR8CV%2FpbhX7jznEnpYNrIx%2B8aXxVtp9lUOrTlKHV1cIfnlpZrKCSAVqrX3HCqrYTIkTo4HRzSbW3%2B2stOlWe0Q14t9LpB2u6ZntquRdgGnrRMrL8vmMMfm8DlkpQQHajgYxRvshfRpBudyQ%2FTdA%2FSlCXEZhMaUe1q8IAYEw36X3yQY6pgHYbWLBSS%2FHwtKZjul286wtulau6nHGuiHORnpKCSArOOBb6SC6%2F5YjajVQHc4IcBwMuKTcrGvhqWQ6dMuE7%2BL4KqhZRALbByiXR7xd9TXXiOjTfLYZUHiOZpsvWRe1oC6CBcdhnFW1OnViwhglm5SdASdzI2MHFU2Vqz7w1F2c7xhUGySUb6X5VsbnvhMtbRf2Ig9nzELP2i1iuhVuZmSrkdQ5zeVI&X-Amz-Signature=3b04e7e6db07e699ddfef2c2461222155d5f7be9ad52cadad57e54d41f211470&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![Extracting multiple columns](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/88562ce7-4fca-4490-a353-3e11a90a77a1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XJANAIWJ%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T220839Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIEJwVP4eGIbetJvlFpaK3Jdyn1w%2BmFGP6hTYTSlBHf6lAiEA3kS9GP0D3BP60vMGk7jNOh13YCoTw%2FUhFDZK%2BonEWeYq%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDFv7WhttybCiZLCvkCrcAyq73geYFdOM5lXH1%2F0fSoEp7NF%2BeV2B9gT3E5UZkq%2BfZDzHnNAJROaP9l7cwwmvgPtOHsNi2R5zcHd68f3jU62lKsIBLgIM%2BCpeQSL5vkrZ6NHG24MWq6fjoW9KAXZsKQFPqb4BbjxWtBT1vj2yPWauc575m3XR4Il%2Bjtva8POxVbj6mX28%2B9UHAdksjfpGn2HIkcA3Qi9R2nxPLcaI0hr0pXiN2i9pQgfFk6wyCWcn5qpzblbWdKSCAqEFREG%2FZXXWXI2QnKVJDI%2FcYO8p%2F5w7wrvw60AmE4a7ZU6D1%2BVJSETB48pidGpSlOnjducmVZ7m2VxCWxt6KPS106COWOIqtpyaGTQlYKBYWbfAijpAYA5b75EX%2FMm6bMHCRoIugqUCQ2d%2Fy5G5cJOAGGkHcdgwdLdWVD9aN1TDa5meY4gXd0%2FpjBmwR6T7a32bXUTNq%2Fkd3CEaQ%2BnOMXPcdrx%2BAWbMY3AzP3H87Q3FAHI2%2Fg11D6ckecxBYH%2BkS0J55%2B1El1%2FvPIdwzT2ZATpHmq7EKUMvWnUf3QWVkEWzr06AWGWE97aVDvehyBEco63nP%2BeQLpwFsOOlIVkYttyGqXXdLi2qHUtn8LTVxcJouXnEf0Ye4T7J47G1gR761KACMImm98kGOqUBDLhpYDMwYs55Vjzfh6t4uA7QjPTcAaHVi2Bu7NH1liRd46fjWlN9Pzuw5Q5UN903LJ%2BIxQmQhB9L1fGXQykyB3y3UmdIA0Wfgs9jiWU9W%2Bvp4Gj512Wu73%2FCSPAsxPrTFnNbmbhUv0YMZ7%2Fqrfk%2F9Vu%2FlpX5nXpyB0yG0CbAlKBHQQmxsCCjDrWTud0ekBPye0hqoFAdZhwejBQbCZi84iZxiQyF&X-Amz-Signature=54bcc1beb61b5d0aa1a85a276ca27f7b43b07904290a39f4c25295b8f931827a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)


![Output when extracting multiple columns is a **DataFrame**](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/ff1bc09b-155e-485d-847f-1d7a815793bb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662KZO4A6R%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T220839Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIQC9Qu3loFlNEiu5Ty97ESzQ1EB2zweJbUU3VbJUYKXzCgIgakVTi%2FIoyHPWJWStj0vWoxCBXid4d3IhvB3nfms6oT4q%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDNRx9SDykOjFDsKLeCrcA9leTLsbCXt2fSpooliNZnJchp%2BV8q5bnuiMOeymQjkP%2FyOYe1PNteDd3Da0X5OyOq8oMLTpoRaYQGoy0gdVZLJxSjsu2hoYWaDJ%2BqVhUc5CHCgUzNKNcoANho7BWKxvygJsZ8R%2FTn2ihQPZGWwW0JXu0a30pW80fWYvfmYDFa3gar4F65Z8BzSHA7ntOeSJ13hYBIAseUOFzCQSI73TEBfGv2ZyK6lpRfLj0Uafr86TlTKDuL8HnZwDvUnt6K7dbFi7pWHXVhZrk%2Fml6xpqDKxnY1tLShG0PariKFW63IY7wP4uoRQ%2Boih8HcGtncej1CqzpxcEBoBpbx%2FdmP0ukknsIgXBJKcIUU2dZxG0roqA1cDZBKw0eT4PN8B9pZv9v4LvAN%2Fg%2F%2FYl67vBdZbx5Gv4SsI%2FMcrsbGiSL%2FIqG2T0N92OU2oqVwLEJiaJZ1iMnY6t0hVD6h60Qy73DovVpv43Kvy0Znaivbm23CyswhqsYBQ6JeNyvi8seKEU1KOAhEYx0BT5307KbDG28iWl5zfz%2FXtPTUU2UvojQwV2BtmH7NnLAZPWMHuCKXEXsTQ8jrJEz69EdinLfRldSFqlS%2B3q8hrCeltjn5hvasq65bQElngC0W%2FSvSO9vEg1MMil98kGOqUBfT4CujSpEd13JANufknUtFERJQmn4pZjOot8EuiP6YoHFAGAezDYd1s8JzE90CubZffehkQp8CfzuzE4Eq53IPjMDxVL6wc7fQABCxc9IT2ISvUez26Ogx%2FPnilDK7W7cxcRJg9O5ElCqZDqS%2BND6GWJBP8NRIjZpA6Ysf6PsUZKCLmiof%2BNoaRrxp%2Bs6Pl955jW%2BT59dHO3HmQIxESGDfTl9gos&X-Amz-Signature=80f564f238480513a72890492544efe98268b1e18e3dd39bce2f81e2fed6a927&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
![Extracting multiple rows and columns](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/157b953e-6021-4b2c-b126-69f5f0f25e99/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XKCPWEFA%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T220840Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJGMEQCIEe8tGyWDdbjpC3GSjUi4yTxSZ47yRI5KbiRR5huqbmNAiA9JBp5Az1Uji2Cx8im0HKnP6pXMq1pi9jqLr4kfx6m1yr%2FAwgmEAAaDDYzNzQyMzE4MzgwNSIMS3tppIrFT0ex%2BLHbKtwD%2Fp2ZAl3W%2BgMsABwkijCoAZVBvp69eNAUNfCPaxlpR49hAj%2FRoZPlPxuhMIDh7XFqhJkxqunzj26m77Msilrz6HYC63%2B2OFg4nLFDKNnJqPwQpqW6niq7tlEsIuTLa6ZyEMEWvTu5A%2FwjPsnbAuh3ZxjvaEF6%2BchaVghDQuuWJxbLTEBKhLRmino7txtfAoX9eFGhw6IQnP%2BHxeJ4QNm%2Fb9WkEk88ToJwtTlNTmWDxMxJya%2BH%2FYB2Z4TwgyIoeOSkNfvRkRGIIHCuYbUSDkTUNnu7pA%2Fp%2FP8PFtgVaxxsXg0LZiZQuYPGOWRBekDNjFP2ZWH%2FZaqAT3sjAU8g2tokhZRzEdjDkLFkt7OpoIVNbpDZnyqChlIc7Dsg3rG%2FCk4Vu6n73km5xPTJME724nF%2FUSkrQx678OxZUoFbxT%2FjvbYJzNdTTVjyGVLhDu6JHQkuDAikn7jLVnUBbtnmGGrNmv8u6BNw3q3rjiVzkWRxDxfTL3qQMBmUqDORz9Q0JeDK%2FOzFluaYMonwfHsS7hTfLFPrRpBzFbeXfaioVMeuSxrpiGVi8w%2BOnwD4JEA5zLYoMPv2sQsJW7b3lH0WbKDVLwTFsieEJDhpvYrOsbG02AFBJ7MRrcDlmt9qQRAw5KX3yQY6pgGqCyLua95Q5YIiUEkSCabXX9uAqH5qRkVYdHW%2F27LZcMxau3afEOecSS3l18zX4EDs70lUZs6S2wLjt%2BgByHgUnv9p%2FIvObxo79NhYTURzbUvsAuzOxW3P2P1hJEGuo804T0rmmrghASxtXrWbdlMC82PdSB%2Fxv%2BXgbzgsUbZW7t8mXA9m6MxfJos3iaw%2BM8kNGb2Zfn7OzvULM1CAIHJ5uYNaeKNj&X-Amz-Signature=84d4e817b151d31c822d4ce1e5715b0ff1a9a8c120ceea699e1e10ece03671ca&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
![Output when extracting multiple rows and columns is a **DataFrame**](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/dcbc1d74-aa73-4627-a883-76d56aaef98c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZPOM3BI4%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T220841Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJGMEQCIGwLnXrDsig7bIcw%2BFtfvdC4q%2Bn9q7idjNUe2A7bOvfgAiB6HcGHCaK%2BY%2BmoAenXiZo%2Bi4RRioXCvl9aQlXXoj%2BpCSr%2FAwgmEAAaDDYzNzQyMzE4MzgwNSIMiIY1%2FMk0BL3zt2sbKtwDh43RhI9b%2BYVW6X4JnTSZzt7831p%2FUAjK3t9Ih1UDHHtxoo8aLWrR9oML3OUU5i7aR9KWQRs5d%2FfM62AvyqdcI4NsolEOyHwcW2Dyn1kdfRdH3gPXilndNKT52165dqvE68%2FFHV6%2Bg0TNTXjidSjsgCpQOTt4NvdSziu4%2BaH40WUu63iBYzu6kEKxepKK7Vo4xYjI6%2BLaXAPjjNkODxu6Moini45bbjXrXdQ%2BCIwk%2BEMndoE1LDFfGg2tur0Vad3ml7KgxAZAnA6legQ91V%2FtbKuKb5JbEYwQ8qf%2FUeHvV%2BK5qa4ewkVeYZPbswhoBtvei4WYbO5quUJ1Lx%2BEJiWcNhwZ1S0KlVnvnhKZQSG26qCdmIPLZQSHX1gh%2BwlTVprCjy8UcLPvI1RftV1QQ%2BwwXtEWweGuOmchOtGsaT9tJdhHAVYAsJS9j%2FBUHW1vfpaB9tjHgo0Vh9F0O7ArmrfDcZeuF9Ll3IBzQfSiZnBgrixbDyIjFqb3GYK6w5Q16UXfG5zJ2R8JJ1iowhyuFMbPf2A3rFI4TXQqGLDXhuKkVoycO1kZTONDeCubVfnbw5KXtMAam97ugtX%2FRPvFYixNCinYzCgt6xjUWd8N4CZR6SNAFPeUTFtYR0%2F5AzQwvKb3yQY6pgHZUcEJ6nps4OjJCTwNP53uNdjKe%2FOCqqbA7H8BQFJaKm6tFYO5tyAQVcnlrVFRXhO432PYpsKgOrY26Z%2BSzNFlA%2BBS0E1087WISmF7pM0qwfhZdchpfeheU7WXx0al09%2BLYu1LFLRpECjD7I9NH4VoPL6UTiSK%2B%2Fh9zMDLTYJDvHil5Pn6l5l6Cl2YU0hIIv5KBFmro1jakR7m6dfys%2FWrDiGMnFsz&X-Amz-Signature=19b1637e73899a896565424ed808f2e20f72981e68d6323bb79f136bdec9e33b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
---
# Functions
---
Below you find an overview of the most important Pandas functions that you should be familiar with and remember. All examples are based on the DataFrame `players_df` that contains football player data from the premier league season 2019/2020.
![players_df](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/88ad3bb4-c8e5-4d76-a3d9-ecf4028c834b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T3JWNFUH%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T220841Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJGMEQCIG2J4V4%2BBxLT3g7A7e7yV%2BwnZEe7Eu0emz6%2F9nZKvLJdAiAhmr4Sp5dCIx334FenwQygDqWjKGTzhe%2FLmsHfqgJtNSr%2FAwgmEAAaDDYzNzQyMzE4MzgwNSIMG4fvvTPcY30nN1i9KtwDVAXow3nBtGCR1%2BBVTanAUDIkJrQWIQOEQ%2FT48%2FGu0qgsscMu5HqnxcW%2BUprnrTJQsni%2B5Zoz2HjH65c6I2mJemdAbOOkrFLT99SPfpZdZHbpw7asZtm%2BpDXAtTcMgVFcy3pzmOLKffB%2FZvXScGw5tigLQVi8eZ0LF6gDOsGclt8SNQ4yePj%2BM95dmvZU82SgXkRROc%2BdVbXR8gviC3mRLsGNpUs5rrVaVXVQHwA6ubXNnNWes0EC3s%2BnQ3IajVVQimQYfxwLJcx8%2FhDa17hlV%2BRBHdV9NUFKkCm0MEyqycVOb2d1ey0BIPK%2FGq89nVNR9fMT7Ic4bx5eezmjdYEzIH1BW4BSZj2y%2Fq3k8O9I6ibj78TwrcsyWepPAUR2bVz%2F%2B3JLWkui6bIpgrKc7A587yUbP9f7XH8HUWNPWwM4nSCOCCetqpewcl97iMiJ7gVgut2FlslxJOULTFyuQ1pnY8FVdUcqHR36KIG8uUSh4oIQAZzucOH9UVSN2rpLrWjaG6G0Oj%2BlsY49qbYp7vzwAW0tqjIUdP2NDy0N5Wpmt9YCuVwhY9wUOOgG7SdFKK%2FuYGJuxDGo7OZjsaaYTebJoMdmHhA0w6d8OnhIpD3USXVUUgJlDbySnT4cdAsw76X3yQY6pgEclNX5nlUgFqCn2OBwbLnnTdGG1Wk%2F6wYsXupx9IXc%2B35eK8EoIUn3ARCq6kR%2BSUGk9cBEd8awFnN%2F93Km95UvHscn8mcJNTCJkZDOGze3iFQXT95zqwUwHl7WtzHeK9erPT9PFgNUH9gOPaG0meRtq1OC%2Bx%2BO9fJ82a9uTfTihnsu2zxwBVUVTZ3VIZnK4hlqQpI657M2PLuXk0bcK3JupGixZJMu&X-Amz-Signature=9dba72cd25a14d2a47f5f571a66fe52f88dfa5adf6cd487157d485a1c592ff6d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
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
![df_experiment_array](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/c2d3b467-0a74-4a15-8374-6aa18fcf8e55/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UP6O67HP%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T220842Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJGMEQCIEVlyOs4MAW32jfHahEIq6XJTd248y9wcDSv3yaylc0XAiBaj1Ug6AXU8cXhiu%2FEDbrJjMMrkEswAwcMfY159kQR5ir%2FAwgmEAAaDDYzNzQyMzE4MzgwNSIMYqkz2tNO3pOSJjYrKtwDwuMIepT4jpi9NQBUhL9%2Fo8%2FcrQsIeh%2FY0HGT4SNKwfRIJbK3dQPOCAjM6IVDTdxDCQrB2XNZPlhIrP85c2Arc84lJxE5KvdVGrLZWMzZCyTS2IJOoB3JdKL6sbZCfrwrsF0nUYsMABQgJ2Ke1lOn40lmFo%2BtxJa3%2BLpe6lLtS%2Bf7CwpKnk58mv%2BHaT5V%2By20aALxeq2ZX6cnrjmaJaP2CNNO6byHOiC%2BhdmzWDC2MCV4nsuoUk3uz4jJoq3MR4fdnj9Xe8gPO%2FvBBtZdU5lokOvRFUJW01EAh2x3jguyLuGYxlm5MdVr0enzA5RolIoSLnPQyB7351neAD0vq5sa2mEloNYV4DmUQPD4%2BxpsTJxG%2Fu7IusytO76J4udVvMFLCuSpGohUQR%2F02M5XoSVZGXPnA7su6A%2BUt19oxZuQg2RAsvl8FuvlK5Ps0FGLpV82PC%2BNUt3jq7BWc5mvYndI88uTwu0XI3rTA7LzAyZDXT52RZF3vMmn3ZZtuXlQTMwmYx5TRbf%2Bzs3PC61PD%2BLB1a8gR%2BHxdTfsRnggthsPb6uKGjnmmBCFaikfdbaN%2FCC0XNVkKp%2F693WPd6gAXoA9UhBL7P7MaQ9D7jv%2BEx7335XyQXV45S7P1NIUj%2Bsw%2FKX3yQY6pgGiYNB0L215SNFXosnc2C2Rr9JA%2Fiymu4QKuV3nzbmqp4ngTFrqzCX7Ab59487gm6KJwTpVrXVgXFEuHbKnkLOT1sMHdSIEeJYNgOp9NQUA9zb6wQ6YjrQOlrx0Mypb887btqjv9pdXh7geNF6VA2WOhjSltNf4pFY1fGJ1X%2B88V3E7NADAjMk9kVCIkDhBUWFWr8y98gWdpzcxlMJffQ7mq4OJNtmc&X-Amz-Signature=31b3f49a56460f80057b21b32ec131b120efacf41106fe69395b172b89ffa1d5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
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
![df_experiment_index](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/53a19e91-90aa-4e2d-9cd8-cb3d1fc18aee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UP6O67HP%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T220842Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJGMEQCIEVlyOs4MAW32jfHahEIq6XJTd248y9wcDSv3yaylc0XAiBaj1Ug6AXU8cXhiu%2FEDbrJjMMrkEswAwcMfY159kQR5ir%2FAwgmEAAaDDYzNzQyMzE4MzgwNSIMYqkz2tNO3pOSJjYrKtwDwuMIepT4jpi9NQBUhL9%2Fo8%2FcrQsIeh%2FY0HGT4SNKwfRIJbK3dQPOCAjM6IVDTdxDCQrB2XNZPlhIrP85c2Arc84lJxE5KvdVGrLZWMzZCyTS2IJOoB3JdKL6sbZCfrwrsF0nUYsMABQgJ2Ke1lOn40lmFo%2BtxJa3%2BLpe6lLtS%2Bf7CwpKnk58mv%2BHaT5V%2By20aALxeq2ZX6cnrjmaJaP2CNNO6byHOiC%2BhdmzWDC2MCV4nsuoUk3uz4jJoq3MR4fdnj9Xe8gPO%2FvBBtZdU5lokOvRFUJW01EAh2x3jguyLuGYxlm5MdVr0enzA5RolIoSLnPQyB7351neAD0vq5sa2mEloNYV4DmUQPD4%2BxpsTJxG%2Fu7IusytO76J4udVvMFLCuSpGohUQR%2F02M5XoSVZGXPnA7su6A%2BUt19oxZuQg2RAsvl8FuvlK5Ps0FGLpV82PC%2BNUt3jq7BWc5mvYndI88uTwu0XI3rTA7LzAyZDXT52RZF3vMmn3ZZtuXlQTMwmYx5TRbf%2Bzs3PC61PD%2BLB1a8gR%2BHxdTfsRnggthsPb6uKGjnmmBCFaikfdbaN%2FCC0XNVkKp%2F693WPd6gAXoA9UhBL7P7MaQ9D7jv%2BEx7335XyQXV45S7P1NIUj%2Bsw%2FKX3yQY6pgGiYNB0L215SNFXosnc2C2Rr9JA%2Fiymu4QKuV3nzbmqp4ngTFrqzCX7Ab59487gm6KJwTpVrXVgXFEuHbKnkLOT1sMHdSIEeJYNgOp9NQUA9zb6wQ6YjrQOlrx0Mypb887btqjv9pdXh7geNF6VA2WOhjSltNf4pFY1fGJ1X%2B88V3E7NADAjMk9kVCIkDhBUWFWr8y98gWdpzcxlMJffQ7mq4OJNtmc&X-Amz-Signature=712575c8c505bf7eb010d740596026d628cbaff26a802a8338f0be5934963bf7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
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
![df_experiment_dict](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/c2d3b467-0a74-4a15-8374-6aa18fcf8e55/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UP6O67HP%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T220842Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJGMEQCIEVlyOs4MAW32jfHahEIq6XJTd248y9wcDSv3yaylc0XAiBaj1Ug6AXU8cXhiu%2FEDbrJjMMrkEswAwcMfY159kQR5ir%2FAwgmEAAaDDYzNzQyMzE4MzgwNSIMYqkz2tNO3pOSJjYrKtwDwuMIepT4jpi9NQBUhL9%2Fo8%2FcrQsIeh%2FY0HGT4SNKwfRIJbK3dQPOCAjM6IVDTdxDCQrB2XNZPlhIrP85c2Arc84lJxE5KvdVGrLZWMzZCyTS2IJOoB3JdKL6sbZCfrwrsF0nUYsMABQgJ2Ke1lOn40lmFo%2BtxJa3%2BLpe6lLtS%2Bf7CwpKnk58mv%2BHaT5V%2By20aALxeq2ZX6cnrjmaJaP2CNNO6byHOiC%2BhdmzWDC2MCV4nsuoUk3uz4jJoq3MR4fdnj9Xe8gPO%2FvBBtZdU5lokOvRFUJW01EAh2x3jguyLuGYxlm5MdVr0enzA5RolIoSLnPQyB7351neAD0vq5sa2mEloNYV4DmUQPD4%2BxpsTJxG%2Fu7IusytO76J4udVvMFLCuSpGohUQR%2F02M5XoSVZGXPnA7su6A%2BUt19oxZuQg2RAsvl8FuvlK5Ps0FGLpV82PC%2BNUt3jq7BWc5mvYndI88uTwu0XI3rTA7LzAyZDXT52RZF3vMmn3ZZtuXlQTMwmYx5TRbf%2Bzs3PC61PD%2BLB1a8gR%2BHxdTfsRnggthsPb6uKGjnmmBCFaikfdbaN%2FCC0XNVkKp%2F693WPd6gAXoA9UhBL7P7MaQ9D7jv%2BEx7335XyQXV45S7P1NIUj%2Bsw%2FKX3yQY6pgGiYNB0L215SNFXosnc2C2Rr9JA%2Fiymu4QKuV3nzbmqp4ngTFrqzCX7Ab59487gm6KJwTpVrXVgXFEuHbKnkLOT1sMHdSIEeJYNgOp9NQUA9zb6wQ6YjrQOlrx0Mypb887btqjv9pdXh7geNF6VA2WOhjSltNf4pFY1fGJ1X%2B88V3E7NADAjMk9kVCIkDhBUWFWr8y98gWdpzcxlMJffQ7mq4OJNtmc&X-Amz-Signature=31b3f49a56460f80057b21b32ec131b120efacf41106fe69395b172b89ffa1d5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
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
![df_from_series](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/5f54bd84-3819-4a73-a684-e0962888e550/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UP6O67HP%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T220842Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJGMEQCIEVlyOs4MAW32jfHahEIq6XJTd248y9wcDSv3yaylc0XAiBaj1Ug6AXU8cXhiu%2FEDbrJjMMrkEswAwcMfY159kQR5ir%2FAwgmEAAaDDYzNzQyMzE4MzgwNSIMYqkz2tNO3pOSJjYrKtwDwuMIepT4jpi9NQBUhL9%2Fo8%2FcrQsIeh%2FY0HGT4SNKwfRIJbK3dQPOCAjM6IVDTdxDCQrB2XNZPlhIrP85c2Arc84lJxE5KvdVGrLZWMzZCyTS2IJOoB3JdKL6sbZCfrwrsF0nUYsMABQgJ2Ke1lOn40lmFo%2BtxJa3%2BLpe6lLtS%2Bf7CwpKnk58mv%2BHaT5V%2By20aALxeq2ZX6cnrjmaJaP2CNNO6byHOiC%2BhdmzWDC2MCV4nsuoUk3uz4jJoq3MR4fdnj9Xe8gPO%2FvBBtZdU5lokOvRFUJW01EAh2x3jguyLuGYxlm5MdVr0enzA5RolIoSLnPQyB7351neAD0vq5sa2mEloNYV4DmUQPD4%2BxpsTJxG%2Fu7IusytO76J4udVvMFLCuSpGohUQR%2F02M5XoSVZGXPnA7su6A%2BUt19oxZuQg2RAsvl8FuvlK5Ps0FGLpV82PC%2BNUt3jq7BWc5mvYndI88uTwu0XI3rTA7LzAyZDXT52RZF3vMmn3ZZtuXlQTMwmYx5TRbf%2Bzs3PC61PD%2BLB1a8gR%2BHxdTfsRnggthsPb6uKGjnmmBCFaikfdbaN%2FCC0XNVkKp%2F693WPd6gAXoA9UhBL7P7MaQ9D7jv%2BEx7335XyQXV45S7P1NIUj%2Bsw%2FKX3yQY6pgGiYNB0L215SNFXosnc2C2Rr9JA%2Fiymu4QKuV3nzbmqp4ngTFrqzCX7Ab59487gm6KJwTpVrXVgXFEuHbKnkLOT1sMHdSIEeJYNgOp9NQUA9zb6wQ6YjrQOlrx0Mypb887btqjv9pdXh7geNF6VA2WOhjSltNf4pFY1fGJ1X%2B88V3E7NADAjMk9kVCIkDhBUWFWr8y98gWdpzcxlMJffQ7mq4OJNtmc&X-Amz-Signature=3a701bb09677b0268b5b6bf92e8dbc314c52268decc0facf0db12a7a4a7b4a27&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
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
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/00b58605-9e39-4338-9ad5-30ab0035c39e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466772MZZN3%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T220844Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIQDkrekz2MPtNy861yrLSWRQuTO7WIUQVfsCtB4ZJ9g7RAIgdai%2F02LMF5X8RmarLAQ7v1YITfzn3hB7Syl0DAf9DGQq%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDJ04dpQzONWv4R0BSyrcA2UQQMwIShiKF2P%2B%2BwxWj1B%2F7826asDNE08vsP3LYzrFMZ9hVQzsxRVmP38tBoMtz7tGgkayx4xmhpz4x5Zn9FBEdKn%2BtnHeUhtYmOyWb1PWxd90BFM5w8Lf%2BfIKDVYJK2vchUcOtfoh06cdihtrs6sy%2Fu%2FxXdW%2BL0o523ykzPthK%2FAnqgy6iCNyTOx3fWu77rvZrj6ITbm2S5bB7uIpAIT30R8khSE7b6aFpqxgJvHZkiXe26fxdQfdh86RXanqr5nwOJtXmkrqW%2BAu9330kVvOCtCOrR0gUGe1qopAjwBQK9a3fXH4CpPnjty8SGyMp7EXtgLwpfZ0V2Vh0yFOVarAqnDVjNYl18M0aXzeLIghIp0gyGG1EHVxSJa77ar8bAj0RVS4TdBdCkSIFlnZWOGTNgQvYZvGB%2BAKx5GCBUCao%2FTGFDA6CSJBupGtUTEkpHQzE%2FiNGyukj5GEJZp8HJlIOLNxMQcUvzM%2BQTT7rFabUKwDTUjOLcQW6w7xTlBW4fyHApUlZ2UqEY%2BHqoMWTcGWfeWz0yTveFE75SzlCkn1G1boA5mU8AX%2FslZ22LWx5cz0DbmqOq5HsiSAWzdICDhbpG3paDxpw04cHupN7SXVcb6WVQHOkSJ27WfrMNyl98kGOqUBfK4GKu7nNW8znEiT3eHhffmQcrYrsE7OARdV03UXPzVTEI2IoRE3Vrtm7ioPEHXRXpNzj3o2vtrGAioGIxwC%2FWd5l2YzmraYq1c4st7iEs5yaZwTxwUsFU1b9ztOJRm1ruLPX%2FeSWb7hzPmtwA5%2Bh0rLGpHgJuLNa5zycvz4TtWMYQCmxKrqxuILtQuGLPcy1i8dPzif5SgMDQvwNHHjQSINc3ge&X-Amz-Signature=ba1c1e065000bf6a0b9f7401412d9e7496953b29fe3bb10562b4a260001c016c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
As you can see in the screenshot above, the file is in .csv format and the standard delimiter (`,`) is used. Thus, we can set `delimiter=','`. Also, we want to use the column `Rank` as index. Thus, we can set `index_col=0` as Rank is the first column or specify it explicitly with `index_col='Rank'`.
Finally, we can load the data into a DataFrame with the following command:
```python
players_df = pd.read_csv('player_stats.csv', delimiter=',', index_col='Rank')
```
![players_df](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/f9cbeba1-616f-40cf-839e-52bc9ce45d8e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466772MZZN3%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T220844Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIQDkrekz2MPtNy861yrLSWRQuTO7WIUQVfsCtB4ZJ9g7RAIgdai%2F02LMF5X8RmarLAQ7v1YITfzn3hB7Syl0DAf9DGQq%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDJ04dpQzONWv4R0BSyrcA2UQQMwIShiKF2P%2B%2BwxWj1B%2F7826asDNE08vsP3LYzrFMZ9hVQzsxRVmP38tBoMtz7tGgkayx4xmhpz4x5Zn9FBEdKn%2BtnHeUhtYmOyWb1PWxd90BFM5w8Lf%2BfIKDVYJK2vchUcOtfoh06cdihtrs6sy%2Fu%2FxXdW%2BL0o523ykzPthK%2FAnqgy6iCNyTOx3fWu77rvZrj6ITbm2S5bB7uIpAIT30R8khSE7b6aFpqxgJvHZkiXe26fxdQfdh86RXanqr5nwOJtXmkrqW%2BAu9330kVvOCtCOrR0gUGe1qopAjwBQK9a3fXH4CpPnjty8SGyMp7EXtgLwpfZ0V2Vh0yFOVarAqnDVjNYl18M0aXzeLIghIp0gyGG1EHVxSJa77ar8bAj0RVS4TdBdCkSIFlnZWOGTNgQvYZvGB%2BAKx5GCBUCao%2FTGFDA6CSJBupGtUTEkpHQzE%2FiNGyukj5GEJZp8HJlIOLNxMQcUvzM%2BQTT7rFabUKwDTUjOLcQW6w7xTlBW4fyHApUlZ2UqEY%2BHqoMWTcGWfeWz0yTveFE75SzlCkn1G1boA5mU8AX%2FslZ22LWx5cz0DbmqOq5HsiSAWzdICDhbpG3paDxpw04cHupN7SXVcb6WVQHOkSJ27WfrMNyl98kGOqUBfK4GKu7nNW8znEiT3eHhffmQcrYrsE7OARdV03UXPzVTEI2IoRE3Vrtm7ioPEHXRXpNzj3o2vtrGAioGIxwC%2FWd5l2YzmraYq1c4st7iEs5yaZwTxwUsFU1b9ztOJRm1ruLPX%2FeSWb7hzPmtwA5%2Bh0rLGpHgJuLNa5zycvz4TtWMYQCmxKrqxuILtQuGLPcy1i8dPzif5SgMDQvwNHHjQSINc3ge&X-Amz-Signature=73543d3591e3168a99847283b7f62feb103a806171f927f2886d49d64df20deb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
---
**Customising the column names**
If we want to customise the column names, we can pass an additional parameter `names=` into the function and assign it a list as value that contains all column names.
```python
column_names = ['Rank', 'Football player', 'Football team', 'Games', 'Games started', 'Minutes played', 'Goals scored', 'Assists provided', 'Shots made', 'Shots made on goal']
players_df = pd.read_csv('player_stats.csv', delimiter=',', index_col='Rank', names=column_names)
```
![players_df with odd first row](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/775e4236-68c7-4d20-86a5-f92c490d9fce/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466772MZZN3%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T220844Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIQDkrekz2MPtNy861yrLSWRQuTO7WIUQVfsCtB4ZJ9g7RAIgdai%2F02LMF5X8RmarLAQ7v1YITfzn3hB7Syl0DAf9DGQq%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDJ04dpQzONWv4R0BSyrcA2UQQMwIShiKF2P%2B%2BwxWj1B%2F7826asDNE08vsP3LYzrFMZ9hVQzsxRVmP38tBoMtz7tGgkayx4xmhpz4x5Zn9FBEdKn%2BtnHeUhtYmOyWb1PWxd90BFM5w8Lf%2BfIKDVYJK2vchUcOtfoh06cdihtrs6sy%2Fu%2FxXdW%2BL0o523ykzPthK%2FAnqgy6iCNyTOx3fWu77rvZrj6ITbm2S5bB7uIpAIT30R8khSE7b6aFpqxgJvHZkiXe26fxdQfdh86RXanqr5nwOJtXmkrqW%2BAu9330kVvOCtCOrR0gUGe1qopAjwBQK9a3fXH4CpPnjty8SGyMp7EXtgLwpfZ0V2Vh0yFOVarAqnDVjNYl18M0aXzeLIghIp0gyGG1EHVxSJa77ar8bAj0RVS4TdBdCkSIFlnZWOGTNgQvYZvGB%2BAKx5GCBUCao%2FTGFDA6CSJBupGtUTEkpHQzE%2FiNGyukj5GEJZp8HJlIOLNxMQcUvzM%2BQTT7rFabUKwDTUjOLcQW6w7xTlBW4fyHApUlZ2UqEY%2BHqoMWTcGWfeWz0yTveFE75SzlCkn1G1boA5mU8AX%2FslZ22LWx5cz0DbmqOq5HsiSAWzdICDhbpG3paDxpw04cHupN7SXVcb6WVQHOkSJ27WfrMNyl98kGOqUBfK4GKu7nNW8znEiT3eHhffmQcrYrsE7OARdV03UXPzVTEI2IoRE3Vrtm7ioPEHXRXpNzj3o2vtrGAioGIxwC%2FWd5l2YzmraYq1c4st7iEs5yaZwTxwUsFU1b9ztOJRm1ruLPX%2FeSWb7hzPmtwA5%2Bh0rLGpHgJuLNa5zycvz4TtWMYQCmxKrqxuILtQuGLPcy1i8dPzif5SgMDQvwNHHjQSINc3ge&X-Amz-Signature=d3136aa7773448a32516397e7ac6c4bd8176899c2d51652abe22a78544421ed2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
As you can see in the screenshot above, if we load the data like this then we have a very odd first row inserted into our DataFrame. This is because we are specifying our own column names so Pandas thinks that the first row in the file is just a regular row although in fact it is the original header row. 
For this reason we need to insert another parameter `header=0` which tells Pandas that the first row in the file is header and thus should be ignored / not included in the DataFrame.
```python
column_names = ['Rank', 'Football player', 'Football team', 'Games', 'Games started', 'Minutes played', 'Goals scored', 'Assists provided', 'Shots made', 'Shots made on goal']
players_df = pd.read_csv('player_stats.csv', delimiter=',', index_col='Rank', names=column_names, header=0)
```
![players_df with customised column names](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/763f8490-e513-40f0-b9da-8aa9e83e5c77/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466772MZZN3%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T220844Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIQDkrekz2MPtNy861yrLSWRQuTO7WIUQVfsCtB4ZJ9g7RAIgdai%2F02LMF5X8RmarLAQ7v1YITfzn3hB7Syl0DAf9DGQq%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDJ04dpQzONWv4R0BSyrcA2UQQMwIShiKF2P%2B%2BwxWj1B%2F7826asDNE08vsP3LYzrFMZ9hVQzsxRVmP38tBoMtz7tGgkayx4xmhpz4x5Zn9FBEdKn%2BtnHeUhtYmOyWb1PWxd90BFM5w8Lf%2BfIKDVYJK2vchUcOtfoh06cdihtrs6sy%2Fu%2FxXdW%2BL0o523ykzPthK%2FAnqgy6iCNyTOx3fWu77rvZrj6ITbm2S5bB7uIpAIT30R8khSE7b6aFpqxgJvHZkiXe26fxdQfdh86RXanqr5nwOJtXmkrqW%2BAu9330kVvOCtCOrR0gUGe1qopAjwBQK9a3fXH4CpPnjty8SGyMp7EXtgLwpfZ0V2Vh0yFOVarAqnDVjNYl18M0aXzeLIghIp0gyGG1EHVxSJa77ar8bAj0RVS4TdBdCkSIFlnZWOGTNgQvYZvGB%2BAKx5GCBUCao%2FTGFDA6CSJBupGtUTEkpHQzE%2FiNGyukj5GEJZp8HJlIOLNxMQcUvzM%2BQTT7rFabUKwDTUjOLcQW6w7xTlBW4fyHApUlZ2UqEY%2BHqoMWTcGWfeWz0yTveFE75SzlCkn1G1boA5mU8AX%2FslZ22LWx5cz0DbmqOq5HsiSAWzdICDhbpG3paDxpw04cHupN7SXVcb6WVQHOkSJ27WfrMNyl98kGOqUBfK4GKu7nNW8znEiT3eHhffmQcrYrsE7OARdV03UXPzVTEI2IoRE3Vrtm7ioPEHXRXpNzj3o2vtrGAioGIxwC%2FWd5l2YzmraYq1c4st7iEs5yaZwTxwUsFU1b9ztOJRm1ruLPX%2FeSWb7hzPmtwA5%2Bh0rLGpHgJuLNa5zycvz4TtWMYQCmxKrqxuILtQuGLPcy1i8dPzif5SgMDQvwNHHjQSINc3ge&X-Amz-Signature=e74e82ba809ec606251e258d340bd7401392a0ae270b4d100f84a31e82751aeb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
---
**Reading data from a .csv file with other delimiter**
The situation can occur in which we must import data from a .csv file that is not comma-separated but for example semicolon-separated: 
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/996f0cda-465e-450d-aed7-9c59ba403480/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466772MZZN3%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T220844Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIQDkrekz2MPtNy861yrLSWRQuTO7WIUQVfsCtB4ZJ9g7RAIgdai%2F02LMF5X8RmarLAQ7v1YITfzn3hB7Syl0DAf9DGQq%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDJ04dpQzONWv4R0BSyrcA2UQQMwIShiKF2P%2B%2BwxWj1B%2F7826asDNE08vsP3LYzrFMZ9hVQzsxRVmP38tBoMtz7tGgkayx4xmhpz4x5Zn9FBEdKn%2BtnHeUhtYmOyWb1PWxd90BFM5w8Lf%2BfIKDVYJK2vchUcOtfoh06cdihtrs6sy%2Fu%2FxXdW%2BL0o523ykzPthK%2FAnqgy6iCNyTOx3fWu77rvZrj6ITbm2S5bB7uIpAIT30R8khSE7b6aFpqxgJvHZkiXe26fxdQfdh86RXanqr5nwOJtXmkrqW%2BAu9330kVvOCtCOrR0gUGe1qopAjwBQK9a3fXH4CpPnjty8SGyMp7EXtgLwpfZ0V2Vh0yFOVarAqnDVjNYl18M0aXzeLIghIp0gyGG1EHVxSJa77ar8bAj0RVS4TdBdCkSIFlnZWOGTNgQvYZvGB%2BAKx5GCBUCao%2FTGFDA6CSJBupGtUTEkpHQzE%2FiNGyukj5GEJZp8HJlIOLNxMQcUvzM%2BQTT7rFabUKwDTUjOLcQW6w7xTlBW4fyHApUlZ2UqEY%2BHqoMWTcGWfeWz0yTveFE75SzlCkn1G1boA5mU8AX%2FslZ22LWx5cz0DbmqOq5HsiSAWzdICDhbpG3paDxpw04cHupN7SXVcb6WVQHOkSJ27WfrMNyl98kGOqUBfK4GKu7nNW8znEiT3eHhffmQcrYrsE7OARdV03UXPzVTEI2IoRE3Vrtm7ioPEHXRXpNzj3o2vtrGAioGIxwC%2FWd5l2YzmraYq1c4st7iEs5yaZwTxwUsFU1b9ztOJRm1ruLPX%2FeSWb7hzPmtwA5%2Bh0rLGpHgJuLNa5zycvz4TtWMYQCmxKrqxuILtQuGLPcy1i8dPzif5SgMDQvwNHHjQSINc3ge&X-Amz-Signature=19ffb0979463fa1719887a6306906f53527e2a2c326c3d4f24ba988580c911a4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
In this case we can simply change the value of the `delimiter=` parameter to `';'` and Pandas knows how to deal with it:
```python
players_df = pd.read_csv('player_stats.csv', delimiter=';', index_col='Rank')
```
![players_df](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/f9cbeba1-616f-40cf-839e-52bc9ce45d8e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466772MZZN3%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T220844Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIQDkrekz2MPtNy861yrLSWRQuTO7WIUQVfsCtB4ZJ9g7RAIgdai%2F02LMF5X8RmarLAQ7v1YITfzn3hB7Syl0DAf9DGQq%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDJ04dpQzONWv4R0BSyrcA2UQQMwIShiKF2P%2B%2BwxWj1B%2F7826asDNE08vsP3LYzrFMZ9hVQzsxRVmP38tBoMtz7tGgkayx4xmhpz4x5Zn9FBEdKn%2BtnHeUhtYmOyWb1PWxd90BFM5w8Lf%2BfIKDVYJK2vchUcOtfoh06cdihtrs6sy%2Fu%2FxXdW%2BL0o523ykzPthK%2FAnqgy6iCNyTOx3fWu77rvZrj6ITbm2S5bB7uIpAIT30R8khSE7b6aFpqxgJvHZkiXe26fxdQfdh86RXanqr5nwOJtXmkrqW%2BAu9330kVvOCtCOrR0gUGe1qopAjwBQK9a3fXH4CpPnjty8SGyMp7EXtgLwpfZ0V2Vh0yFOVarAqnDVjNYl18M0aXzeLIghIp0gyGG1EHVxSJa77ar8bAj0RVS4TdBdCkSIFlnZWOGTNgQvYZvGB%2BAKx5GCBUCao%2FTGFDA6CSJBupGtUTEkpHQzE%2FiNGyukj5GEJZp8HJlIOLNxMQcUvzM%2BQTT7rFabUKwDTUjOLcQW6w7xTlBW4fyHApUlZ2UqEY%2BHqoMWTcGWfeWz0yTveFE75SzlCkn1G1boA5mU8AX%2FslZ22LWx5cz0DbmqOq5HsiSAWzdICDhbpG3paDxpw04cHupN7SXVcb6WVQHOkSJ27WfrMNyl98kGOqUBfK4GKu7nNW8znEiT3eHhffmQcrYrsE7OARdV03UXPzVTEI2IoRE3Vrtm7ioPEHXRXpNzj3o2vtrGAioGIxwC%2FWd5l2YzmraYq1c4st7iEs5yaZwTxwUsFU1b9ztOJRm1ruLPX%2FeSWb7hzPmtwA5%2Bh0rLGpHgJuLNa5zycvz4TtWMYQCmxKrqxuILtQuGLPcy1i8dPzif5SgMDQvwNHHjQSINc3ge&X-Amz-Signature=73543d3591e3168a99847283b7f62feb103a806171f927f2886d49d64df20deb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
---
## [`.head()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.head.html)
---
This function is very simple and allows us to display the top 5 rows of a DataFrame only. This can be very useful whenever we have a very large dataset and we want to gain a quick grasp of it.
```python
players_df.head()
```
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/117c3a28-5ad6-435a-8e63-3829f3f95c63/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664MAMHMTH%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T220845Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIQCbwH%2B8ig9HOr453BjQKMuLLeK%2Fo9XeuqBdhS0I7eDWKwIgYylddV7DXRO%2Bt%2BLRXsoCl6jbX8vr0sfPO2nnAfGtfOEq%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDGEhI3E5r6lIJ1So2ircAywMUvwSFc%2BLti111rp85FuJhe%2B9ZYgjPFoqomxad3r1j2Yby4aHFEPQtiEtmSJioQHk37tU4bKR936OIkS%2B81JHsYvLTZ8Mt3qzBKdNmINYHuPHq3fX2bwWWDYl8LIN0VOct5yBZR3HyijVqTtyHm0h%2FCnYCqyLp12KQ2U16wdZ6zVVC0UPI3bOttNiHdv%2BNC2zLeCW7IFPA4EFojKGH69Xj91nwYys0Ty5o8oo5gWh%2FSi7etfSx7BaAQ5i10y14tBWjV9yrLpGFOIKOoa5S1m1Sh3vj7d5vKcwmHp7M8nDVaNi7NkiykqvQtUSSOlyudhk%2BIWcF7s8lHzRV7rDBIn2j1wNdzW2ilB2OrpCV87RW%2B1IONiB%2BHgofYNnwW%2FbqAw%2FtGk%2FW4yPeZJAvhr%2BIWdnZfBPEmzd7T4nRAU6NK4kHqz8Ho6r%2BEfQoUvIgxlidKQDQ0cxlICbVwWV8zKI4e%2FrwGts3Q3%2FbgZP3%2BOvlsl8v5%2FbBYBacc82Rfs%2Bp%2FCIxPh4wTSGnj956e2m9Yyl5WFq3GqJ2RHM6dPvDoUtwKt1wlinbJWpS96Prb0yw1aWzVtncCCPb0%2BiZzidh19vDA%2FGJRoGoo3S2yNlp%2B28JLm6I7cbiHzer%2FVLTX6DMOSl98kGOqUBgJ0O2VTLaBEd%2BUPys%2B4DnIdsKQrJ5gOGPKWIxKPzm2R2BB5%2BPtzmqfHRrYeOoJ9jR0b1S3o%2FgLloRHIA7%2FJTMLFVaDKyL%2BVLQmP%2FYBeBwFVXxcHGF4VjA0GZ1LReaH0ue2eLdkKmGyj63McohxxOvnKW6jwiRM9VYdjm7eWiHID8KoNF%2FLSzcoh2SHELTJWB3bm41L1FfkmLQUjT8nCsMjOZY5Rt&X-Amz-Signature=0861668fdc5eb73d3e0cfe199f160bbb918722650d54217733dee9c958e5cc56&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
---
## [`.tail()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.tail.html)
---
Very similar to `.head()`, with the only difference that the last 5 rows are displayed only. 
```python
players_df.tail()
```
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/89c926bd-b290-49f7-96aa-2e74779d6f9d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V6ZOWFDQ%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T220845Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJIMEYCIQChWly6VQkcGVO63TGWUXrYHhRZjggWw4gdiPMNd3TE0QIhAKbYw6NPIhOprBsBLYeki2T8BOsIIRydSxxjLfrE6%2B5OKv8DCCYQABoMNjM3NDIzMTgzODA1IgxKldl9WkVtJkIh7Zgq3AMFDmzXEaGEOGUrG9uYLQRZ0FcJWEzOcl%2B%2F2A04SCPxrimP9u19ZyxBaNuXsLDK%2FmK1C2x8sQBGbRJiP%2Bwn6755Ln6%2FphyZxlAk4JKhDxXV36OZNcMJcnR7WFCR%2FOv0A2d%2BsjtomR%2BQLYDmtMuuAl%2FK3F650zXFmEyt6wx6s3kAgt1IfZsw36I3HkQL6J%2FmKTrvkF52Gztx5Oi%2BECVXZd8616IimE238g1jQPOwVXosGLC0vsleWNXPaWTm8ZhRU%2BojKevOqVMdRyC1udAxQzVDrnXoxuCxq5dlaMqHBRiUxTIngZqd5hmBYTbLrBEh5Hbh53hiXW4XuYygtCpvKb7sjcb2piKrq1Csi4c%2BGvRtA3FTNDIPapD8%2F7n1K%2B4OEwYKIQIdbF6fKoATTrt52g3BK1BrnhqwmWrgYTI%2FyHWiP%2BVXGszkhWjfwRQoVNHGWAl64tKtK%2BfSoOdzT5eHWEj1naKQKZ8cU%2FsXrVyPIumyu5s%2FIZN3R%2BvFQ7iaDbNcd6NjdVuFwx4pPHEtoW%2F81xk1Ow8YraPlch%2FhA0tssQoqlnD%2FTKc9O7qLkpL242FVYpO5NuelzDyipkaMec1ddOUaYtxV95TFfot41MAAQnzeQX4gUlLj25b7dVz%2BFzDfpffJBjqkAfWl8QZe1QVtoAoFpFwdcfNAPKTizNcKF7YKsKoNPl%2FuJnpHaV1mbfptIUFVn5%2Bd6YV%2F5wC0fEXMhqjNh15KN2SG9PBG9K4EHRUiKOcfNxnZOsvQ3fdpQ9l%2BiJ9YBBqn5ASokCVlm1zw0qbF1EPd3jKlnlQEGtdi05DZjlgXQiswA36cVrYwDFX3rbBm1qi%2B6CvkBu%2Fyx35BuruaUFSSAuZGHVRz&X-Amz-Signature=549e2c4b2789aa231f21ff9c7d2d901c5ab6206fd293d62e1e2f12565a9666d1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
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
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/3489a926-bdc6-41b8-86c1-de62699b188c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667UGSQZB3%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T220846Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJGMEQCIHvOXI6amepJeKUOq%2F3%2FRWjhOOsHGt4gexJk5SjP8heyAiB12QnIElBwVgslk39%2FnxQBNOgtTvc9qQ3wlmPDI9gc9ir%2FAwgmEAAaDDYzNzQyMzE4MzgwNSIMFvaeCtSzYly6Iep8KtwDz%2ByVje2YF0O0psFB6qezBm%2BQw36bCABz6SmZnizyO98dsQLTl0p2uuYm%2Fs40XtxBo0h6uVEyUeyHK3yjJQVF6IQS2J7MTRiPtYa191pxF0cZFW2tzRoGK%2BAOIt4yZcnqsfgLOn%2FCP9tGZ2zS%2FzOceMyrpjKsG9F%2FkWDaX5nUTzCtAvK32bT2ZR3M9IChXLeLoYoC%2FRKMUJF5iWEJdcZbkwBEWwsrwlAq%2FpNeTevb19j63RAtz%2FEq881874kW7ysgwKaD6d491k8gwEApvWLWuNHjdqW9x%2FYnH%2BTaLz74L4UHa29CsdV5A3rlGwy%2FQe5N%2FGQJFWFmoe9HOvRFHbOccNZD%2BWL5frAf%2F723ZZJGdLLUfOPx4hQkgMy0Jp80VGKgWXitfW5OCkpsD5y1ciC5UwXBolRFQrLjrdETlB2EzRqN3y6H3GT%2BJaCYCMMrJFHLD7ReCiywiCzzzt8M1BNCtCuUhHrrkq%2F1Bqu18ErNq0pT3WCNl9lpLbFo626hZcr%2FMaqMenMqq8Sw9SPu%2BMhwvFyn0F3GbBa378Bj%2F3Z5d2nR1tQFDLAQrjDOdrMSFb5V%2FT8ZpWYKkyj%2Fkm66jNUEX8EcxN3hjhNpFAKxF6hdAudLQFyMTNtEsYtYdoww06X3yQY6pgFQmhbTPoYtEltE1oNAMXofY8yhEfyMHR%2B1wqvNiEaBCJYkcnvn0CE6NYFs7UFIwcJUqBR3h71cVQQuU7odcFNp1%2BRew7TlquJQp1xkIod%2BHjYs7UJmXteXeWm5T9BlXQUF7JfsouZtyBnDNfE77spDsaAFY3IN5g8CBpghI%2BOl5oyBN18V4lLyrbN3nrQxoEyU%2BemJDmLnjdDjZCF%2FCv4nmyZkmn9r&X-Amz-Signature=6b8776a54cca3f74f15ece47a58488a4876ebaccc0145a9da47344c8a58aed88&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/c7ccb92c-7800-435e-8704-64d239ffe161/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46656SZVPB4%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T220849Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJGMEQCIA5bhBcnEdDtVmO6SYiGymEOEIS%2FBungZ6s9lvuAL2ZpAiBmxVQGHz1rmpzmZ2G5gYgnaEv4EnYd8hOJ2IP%2FTzobQir%2FAwgmEAAaDDYzNzQyMzE4MzgwNSIMN%2BAjjkbXKaUFwvKgKtwDsC%2Bt0QXsF%2FSTvlrznJJXL1bf1EJuVTIP%2FiO4eUKrYwsOIYLdPCDnyFWmcHwYiyKN6VmP24vu%2B7Z740d4uLQnM1Ejht3f%2Fu0PS44r%2FwnCjXH4vepTi5hNPLGnXUZ4Uh%2FE1hnG8Y9UW2owrYW1rZY8QdTWCgEk6tZrus7Ay9WWiviFS127YQW0QGriOBuJQVEGdfMTWwP1MwwLvkcKDmEqBntZAUf49s3rI%2FCERtlFRwI0bdPz4kt9SnxcaykbZigxeBxhvQrgMoFvcqp9SDKOezGv9yOl16%2Fykfvjhh1G%2Fprj3dy938AH2BphfKutT%2BdH9vJtzRQk3yHgW0YjrOWiLvJBaQScJbryCbICaSftBS9viotsbvWG01NlzWZf2vG0D%2BsKvVKgzrkL71o%2FeeCrp5iivhC%2BS5j9wgAle0luAJNrOJWGsW0tPIUGFGWZPNuoGoI2gZ3b8F%2BQuUOXQcltl588u10LRh2aiydPphr1KtFuD17Pr0G%2FZWa%2F7HJB3hj8Rb3zaKkCY4B3d0YuWnL9lbcgWed7XERImDIZ%2BInuqVNSczp%2B7hlP6I7fTWEUl9sVA3HtjFbhqIkqAenbj051TU%2FzlxuXkRb4MxPBFVs551DmvR3CwLMaJMI%2FsXkwsKb3yQY6pgFNZLaghlhwLEbBZUoZgsbLUflR17%2B33tIRBWLXhWnLJgQeOCLQN%2Fw%2Fdlx7J%2BI0xsKrn%2BpNa0fXJ64lnqPok9MWrfzCLcMFQQV8Cn5%2FMNseMyvARyhFrBAUkZawegI2jq%2FL4Y%2FCKg9nDLbU059W6pcQqhywoMssvz%2B1G6re52EEcOlfW9dR3WOmC2n6AfKjPF5vneWa%2FT%2Fycidt7rPyJ4KZf3vZczIb&X-Amz-Signature=accb8932ddd207c0451f7072c43722d1e60d3770fe94598b22ddd6848fff3fc1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
---
**Access rows based on condition**
Another cool thing with `.loc[]` is that we can select rows based on a condition that returns True or False. For example, if we search for all players that scored exactly 10 goals, we can achieve this by the following command(s).
```python
players_df.loc[players_df['Goals'] == 10]
# OR
players_df[players_df['Goals'] == 10]
```
Python goes through the column `Goals` and checks for each value if it is equal to 10. If yes, it returns `True` if no, it returns `False`. In the end only the rows are displayed for which `True` has been returned.
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/ba1a88fc-24e1-4a54-896f-e55317031d16/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46656SZVPB4%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T220849Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJGMEQCIA5bhBcnEdDtVmO6SYiGymEOEIS%2FBungZ6s9lvuAL2ZpAiBmxVQGHz1rmpzmZ2G5gYgnaEv4EnYd8hOJ2IP%2FTzobQir%2FAwgmEAAaDDYzNzQyMzE4MzgwNSIMN%2BAjjkbXKaUFwvKgKtwDsC%2Bt0QXsF%2FSTvlrznJJXL1bf1EJuVTIP%2FiO4eUKrYwsOIYLdPCDnyFWmcHwYiyKN6VmP24vu%2B7Z740d4uLQnM1Ejht3f%2Fu0PS44r%2FwnCjXH4vepTi5hNPLGnXUZ4Uh%2FE1hnG8Y9UW2owrYW1rZY8QdTWCgEk6tZrus7Ay9WWiviFS127YQW0QGriOBuJQVEGdfMTWwP1MwwLvkcKDmEqBntZAUf49s3rI%2FCERtlFRwI0bdPz4kt9SnxcaykbZigxeBxhvQrgMoFvcqp9SDKOezGv9yOl16%2Fykfvjhh1G%2Fprj3dy938AH2BphfKutT%2BdH9vJtzRQk3yHgW0YjrOWiLvJBaQScJbryCbICaSftBS9viotsbvWG01NlzWZf2vG0D%2BsKvVKgzrkL71o%2FeeCrp5iivhC%2BS5j9wgAle0luAJNrOJWGsW0tPIUGFGWZPNuoGoI2gZ3b8F%2BQuUOXQcltl588u10LRh2aiydPphr1KtFuD17Pr0G%2FZWa%2F7HJB3hj8Rb3zaKkCY4B3d0YuWnL9lbcgWed7XERImDIZ%2BInuqVNSczp%2B7hlP6I7fTWEUl9sVA3HtjFbhqIkqAenbj051TU%2FzlxuXkRb4MxPBFVs551DmvR3CwLMaJMI%2FsXkwsKb3yQY6pgFNZLaghlhwLEbBZUoZgsbLUflR17%2B33tIRBWLXhWnLJgQeOCLQN%2Fw%2Fdlx7J%2BI0xsKrn%2BpNa0fXJ64lnqPok9MWrfzCLcMFQQV8Cn5%2FMNseMyvARyhFrBAUkZawegI2jq%2FL4Y%2FCKg9nDLbU059W6pcQqhywoMssvz%2B1G6re52EEcOlfW9dR3WOmC2n6AfKjPF5vneWa%2FT%2Fycidt7rPyJ4KZf3vZczIb&X-Amz-Signature=a3bb16e9510c3688c5fb06751804aedb3d651be25676622e2695663569013ad4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
We can also use more complicated conditions:
```python
players_df.loc[(players_df['Goals'] >= 10) & (players_df['Assists'] > 7)]
# OR
players_df[(players_df['Goals'] >= 10) & (players_df['Assists'] > 7)]
```
In this example we use two conditions and connect them with `AND (&)`, thus both conditions must evaluate to True for a player so that he is going to be displayed in the result set.
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/e36990b5-25ca-4f2b-b252-e4f64e702ab0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46656SZVPB4%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T220849Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJGMEQCIA5bhBcnEdDtVmO6SYiGymEOEIS%2FBungZ6s9lvuAL2ZpAiBmxVQGHz1rmpzmZ2G5gYgnaEv4EnYd8hOJ2IP%2FTzobQir%2FAwgmEAAaDDYzNzQyMzE4MzgwNSIMN%2BAjjkbXKaUFwvKgKtwDsC%2Bt0QXsF%2FSTvlrznJJXL1bf1EJuVTIP%2FiO4eUKrYwsOIYLdPCDnyFWmcHwYiyKN6VmP24vu%2B7Z740d4uLQnM1Ejht3f%2Fu0PS44r%2FwnCjXH4vepTi5hNPLGnXUZ4Uh%2FE1hnG8Y9UW2owrYW1rZY8QdTWCgEk6tZrus7Ay9WWiviFS127YQW0QGriOBuJQVEGdfMTWwP1MwwLvkcKDmEqBntZAUf49s3rI%2FCERtlFRwI0bdPz4kt9SnxcaykbZigxeBxhvQrgMoFvcqp9SDKOezGv9yOl16%2Fykfvjhh1G%2Fprj3dy938AH2BphfKutT%2BdH9vJtzRQk3yHgW0YjrOWiLvJBaQScJbryCbICaSftBS9viotsbvWG01NlzWZf2vG0D%2BsKvVKgzrkL71o%2FeeCrp5iivhC%2BS5j9wgAle0luAJNrOJWGsW0tPIUGFGWZPNuoGoI2gZ3b8F%2BQuUOXQcltl588u10LRh2aiydPphr1KtFuD17Pr0G%2FZWa%2F7HJB3hj8Rb3zaKkCY4B3d0YuWnL9lbcgWed7XERImDIZ%2BInuqVNSczp%2B7hlP6I7fTWEUl9sVA3HtjFbhqIkqAenbj051TU%2FzlxuXkRb4MxPBFVs551DmvR3CwLMaJMI%2FsXkwsKb3yQY6pgFNZLaghlhwLEbBZUoZgsbLUflR17%2B33tIRBWLXhWnLJgQeOCLQN%2Fw%2Fdlx7J%2BI0xsKrn%2BpNa0fXJ64lnqPok9MWrfzCLcMFQQV8Cn5%2FMNseMyvARyhFrBAUkZawegI2jq%2FL4Y%2FCKg9nDLbU059W6pcQqhywoMssvz%2B1G6re52EEcOlfW9dR3WOmC2n6AfKjPF5vneWa%2FT%2Fycidt7rPyJ4KZf3vZczIb&X-Amz-Signature=641011662d78326559ea3db3f20c6cd1e375bed674b4e6242fb3ed82716dce49&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
Remember, even if the example above looks quite complicated, we have only passed a selection criteria for rows into `.loc[]`, as there is no comma `,` .
Thus, when we only want to have specific columns displayed in our result set, we can insert the comma `,` and pass a list to `.loc[]` with the column labels that should be displayed.
```python
players_df.loc[(players_df['Goals'] >= 10) & (players_df['Assists'] > 7), ['Goals', 'Assists']]
```
Now, this leads to only the columns `Goals` and `Assists` being displayed in the result set.
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/f6ca01be-39fd-475b-b4e4-94e0c80b5ec2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46656SZVPB4%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T220849Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJGMEQCIA5bhBcnEdDtVmO6SYiGymEOEIS%2FBungZ6s9lvuAL2ZpAiBmxVQGHz1rmpzmZ2G5gYgnaEv4EnYd8hOJ2IP%2FTzobQir%2FAwgmEAAaDDYzNzQyMzE4MzgwNSIMN%2BAjjkbXKaUFwvKgKtwDsC%2Bt0QXsF%2FSTvlrznJJXL1bf1EJuVTIP%2FiO4eUKrYwsOIYLdPCDnyFWmcHwYiyKN6VmP24vu%2B7Z740d4uLQnM1Ejht3f%2Fu0PS44r%2FwnCjXH4vepTi5hNPLGnXUZ4Uh%2FE1hnG8Y9UW2owrYW1rZY8QdTWCgEk6tZrus7Ay9WWiviFS127YQW0QGriOBuJQVEGdfMTWwP1MwwLvkcKDmEqBntZAUf49s3rI%2FCERtlFRwI0bdPz4kt9SnxcaykbZigxeBxhvQrgMoFvcqp9SDKOezGv9yOl16%2Fykfvjhh1G%2Fprj3dy938AH2BphfKutT%2BdH9vJtzRQk3yHgW0YjrOWiLvJBaQScJbryCbICaSftBS9viotsbvWG01NlzWZf2vG0D%2BsKvVKgzrkL71o%2FeeCrp5iivhC%2BS5j9wgAle0luAJNrOJWGsW0tPIUGFGWZPNuoGoI2gZ3b8F%2BQuUOXQcltl588u10LRh2aiydPphr1KtFuD17Pr0G%2FZWa%2F7HJB3hj8Rb3zaKkCY4B3d0YuWnL9lbcgWed7XERImDIZ%2BInuqVNSczp%2B7hlP6I7fTWEUl9sVA3HtjFbhqIkqAenbj051TU%2FzlxuXkRb4MxPBFVs551DmvR3CwLMaJMI%2FsXkwsKb3yQY6pgFNZLaghlhwLEbBZUoZgsbLUflR17%2B33tIRBWLXhWnLJgQeOCLQN%2Fw%2Fdlx7J%2BI0xsKrn%2BpNa0fXJ64lnqPok9MWrfzCLcMFQQV8Cn5%2FMNseMyvARyhFrBAUkZawegI2jq%2FL4Y%2FCKg9nDLbU059W6pcQqhywoMssvz%2B1G6re52EEcOlfW9dR3WOmC2n6AfKjPF5vneWa%2FT%2Fycidt7rPyJ4KZf3vZczIb&X-Amz-Signature=a3bd2a09b964c2e906c12b0ff25ad7e6e3f43d508c8c194fcda1a7b938c47d4c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
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
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/650b856f-f0af-4950-a1e4-ee0fca8ba573/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZZVAHZKM%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T220849Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIQCmukzCLyOuchNngF2TqEFST6jY%2FhPSUWwprl7ZaaLVbAIgYCH%2FmGIV0MhMV5k2kJBMl%2BnQj3V74ozNikj%2Fv4nMhN0q%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDAWMJp3wAsjvlGNmzSrcA9Mk4cg0ipWd%2F%2BOIpNMIPQQOZHCWg6DUevopz9K9xYckgW2I%2Br4%2Bsx7JUy5TSTuHv7nOpR%2FyQ4vEwa7RyT4o61W7oF2BcjHeoGVZTIUU0SPAB%2B%2FzW2WoBlZZswPssGGUluKp7TeR2VXUDVOYBboUe%2FbYzdt8bPjgosRKRBSdawgS2AOwzAJfwK7rrQwLMCLe3YwvDwDdI1FxHOup%2FMX3mvvaAlnmTpFMnkTBi%2BSIKU7H1QiI65aHycOfJfJlJ2dEY2XnRqXrC6jPjECMK3YyprFdX1v7bV09o6xJOg5VBnR2L6ukXl1ZV8%2BMewopnzP6ZxO3w6D%2BJZzCkOeS3zYQE8ReOFyOSkdBZCTKAxTdH48YioM6bXGrFtqzcao4Mquzbpu4jTmobXCtXVZrIDejRUClAsmp%2FIHcy8%2Fd0rj7WMby6zaOWugKibG%2BqZrzcGJA%2FPVBm4Lo4gKkLZl18nTq7rMJLM79hxUx4onvWxIzSVbApBOuknv6ig4%2BKP%2BLA%2FRW9i2%2BpZhefYEOsX2dWvJZ2NuaUWuefzvK%2FFzIm1Fwh8J5HAp7IHxPtZAIXw4bML30NBZXRdrZclq0ozNPp12pWnWl2pl8VjdT8AfdsR%2Fz6sfT%2Fi%2FXkDiOyncUzoyoMOSl98kGOqUBwnS2R%2FBEvOHRue6fA90GSCdgbYn1xMC2hxR6SM6LXtvVrZ5B%2Bk2dxbY9NMFdOANRKUXwnk3NX0BiaXp4o5HZdmodbC11bvoQH2FJrk8M6MQUshdTwX9Anwi3HwYX60CuwMSg9BM4i8RRanYIqUR%2FhjqSggspRnMNOsrrArkEKLiUECvjsGxxIDfXqalg6Qx9tGmR1FNF6UCotynKb8ZRPqxMdGur&X-Amz-Signature=4b6ea5501b6d48ebd9deeadb177120fc208ab4ac4cc93746252ddf0722af543e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
---
**Slicing on rows and columns**
If we want to select not all columns but only the first three, we can insert the comma `,`.  For the columns the slicing command would be `[:3]` as this selects the columns with index `0` `1` `2` and thus the first three.
```python
players_df.iloc[:10, :3]
```
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/683390cb-2a6f-4cab-b0ba-2b9b3afc433f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZZVAHZKM%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T220849Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIQCmukzCLyOuchNngF2TqEFST6jY%2FhPSUWwprl7ZaaLVbAIgYCH%2FmGIV0MhMV5k2kJBMl%2BnQj3V74ozNikj%2Fv4nMhN0q%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDAWMJp3wAsjvlGNmzSrcA9Mk4cg0ipWd%2F%2BOIpNMIPQQOZHCWg6DUevopz9K9xYckgW2I%2Br4%2Bsx7JUy5TSTuHv7nOpR%2FyQ4vEwa7RyT4o61W7oF2BcjHeoGVZTIUU0SPAB%2B%2FzW2WoBlZZswPssGGUluKp7TeR2VXUDVOYBboUe%2FbYzdt8bPjgosRKRBSdawgS2AOwzAJfwK7rrQwLMCLe3YwvDwDdI1FxHOup%2FMX3mvvaAlnmTpFMnkTBi%2BSIKU7H1QiI65aHycOfJfJlJ2dEY2XnRqXrC6jPjECMK3YyprFdX1v7bV09o6xJOg5VBnR2L6ukXl1ZV8%2BMewopnzP6ZxO3w6D%2BJZzCkOeS3zYQE8ReOFyOSkdBZCTKAxTdH48YioM6bXGrFtqzcao4Mquzbpu4jTmobXCtXVZrIDejRUClAsmp%2FIHcy8%2Fd0rj7WMby6zaOWugKibG%2BqZrzcGJA%2FPVBm4Lo4gKkLZl18nTq7rMJLM79hxUx4onvWxIzSVbApBOuknv6ig4%2BKP%2BLA%2FRW9i2%2BpZhefYEOsX2dWvJZ2NuaUWuefzvK%2FFzIm1Fwh8J5HAp7IHxPtZAIXw4bML30NBZXRdrZclq0ozNPp12pWnWl2pl8VjdT8AfdsR%2Fz6sfT%2Fi%2FXkDiOyncUzoyoMOSl98kGOqUBwnS2R%2FBEvOHRue6fA90GSCdgbYn1xMC2hxR6SM6LXtvVrZ5B%2Bk2dxbY9NMFdOANRKUXwnk3NX0BiaXp4o5HZdmodbC11bvoQH2FJrk8M6MQUshdTwX9Anwi3HwYX60CuwMSg9BM4i8RRanYIqUR%2FhjqSggspRnMNOsrrArkEKLiUECvjsGxxIDfXqalg6Qx9tGmR1FNF6UCotynKb8ZRPqxMdGur&X-Amz-Signature=397854585bd5db916cc92e32fd896f613235c13cb5c3cb008d90e60ede1451d1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
We can also perform more complicated slicing operations with `.iloc[]`. let’s say we want to select the 94th until the 98th row and the 2nd  until the 4th column.
```python
players_df.iloc[93:98, 2:5]
```
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/37bffb74-4ae3-4b36-bec6-22ef1a31233c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZZVAHZKM%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T220849Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIQCmukzCLyOuchNngF2TqEFST6jY%2FhPSUWwprl7ZaaLVbAIgYCH%2FmGIV0MhMV5k2kJBMl%2BnQj3V74ozNikj%2Fv4nMhN0q%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDAWMJp3wAsjvlGNmzSrcA9Mk4cg0ipWd%2F%2BOIpNMIPQQOZHCWg6DUevopz9K9xYckgW2I%2Br4%2Bsx7JUy5TSTuHv7nOpR%2FyQ4vEwa7RyT4o61W7oF2BcjHeoGVZTIUU0SPAB%2B%2FzW2WoBlZZswPssGGUluKp7TeR2VXUDVOYBboUe%2FbYzdt8bPjgosRKRBSdawgS2AOwzAJfwK7rrQwLMCLe3YwvDwDdI1FxHOup%2FMX3mvvaAlnmTpFMnkTBi%2BSIKU7H1QiI65aHycOfJfJlJ2dEY2XnRqXrC6jPjECMK3YyprFdX1v7bV09o6xJOg5VBnR2L6ukXl1ZV8%2BMewopnzP6ZxO3w6D%2BJZzCkOeS3zYQE8ReOFyOSkdBZCTKAxTdH48YioM6bXGrFtqzcao4Mquzbpu4jTmobXCtXVZrIDejRUClAsmp%2FIHcy8%2Fd0rj7WMby6zaOWugKibG%2BqZrzcGJA%2FPVBm4Lo4gKkLZl18nTq7rMJLM79hxUx4onvWxIzSVbApBOuknv6ig4%2BKP%2BLA%2FRW9i2%2BpZhefYEOsX2dWvJZ2NuaUWuefzvK%2FFzIm1Fwh8J5HAp7IHxPtZAIXw4bML30NBZXRdrZclq0ozNPp12pWnWl2pl8VjdT8AfdsR%2Fz6sfT%2Fi%2FXkDiOyncUzoyoMOSl98kGOqUBwnS2R%2FBEvOHRue6fA90GSCdgbYn1xMC2hxR6SM6LXtvVrZ5B%2Bk2dxbY9NMFdOANRKUXwnk3NX0BiaXp4o5HZdmodbC11bvoQH2FJrk8M6MQUshdTwX9Anwi3HwYX60CuwMSg9BM4i8RRanYIqUR%2FhjqSggspRnMNOsrrArkEKLiUECvjsGxxIDfXqalg6Qx9tGmR1FNF6UCotynKb8ZRPqxMdGur&X-Amz-Signature=1015ffcf83622fa86d4475ef56583e83c469064f24aa256eb648132e63197880&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
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
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/3489a926-bdc6-41b8-86c1-de62699b188c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663NLJSHYS%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T220856Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIDkPCrEJOdf2ONZvqoAGM5PSl9XfJAD0kYdztHjNKVKeAiEAttCaq4hQtYMEipbrjZcRseHuNsBqcWmviamzGT6Bz7sq%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDNAcG5QM7QUjwMi%2BWSrcA1Sx%2F%2ByvSm92UhabVctcp8wZtlwzW4MUi6dftVTmRPR%2FkZ4JiIL8gPYId2Kro%2Bd%2B0vqWijBMDNh%2B3mOFTRSTvICEXQt7USBA%2F8m8ajhqzLUSMH9UuE5YP1RPK3SjG6%2F08dlydixqB6DaEy0FsDjweZF1AQu6BqrLEj1GErrCRbZvL7Q0PHHhMr1xnHe6inCkSWoFM6gnLYM8geDZBBB2TLGTXlznsOnSaGLaZnl66AZytSkki8O1OX8sG%2FeDY5HcCij0bNgNVF419S8Np3fjDZu2dku%2B0WeDzwdYBnL7oHcEbrHuqHK5beNoM%2BP6WWDbj264gCJ7th%2FKn0dlC5OummrmA19ToWXvihLgOSJIS63YjKx8iG5wl2jbdWQMshUlO%2B2ZzOaC5SkWSpHzW%2BjuYb6RSHCgeJlhcPXpE3PXw83O8CcKm%2BkPlvmr1Dmqrj%2BDDVIizaRyZVe78sKkokBQzNe1YXukG85cp6pTuRXc0hsTeGO2E3WxuVjuBkvnxFm8cCJOcXTR4xlmHEiae5jg%2FuIyPi9yxkln0Y9BCt1Dq%2BvF4R2fNVVtZMMj2EKC0kPluS26PXv%2Bt%2FN29Gel3TU2BUBO%2BiKV%2B2zrp1rzVhRw%2Fe31sQSsK22IsurrZs9sMJ2m98kGOqUBGEX7IzQMAQmO5nNA0Hpp0HyYT2d3piyz84UwgNbCKmJoCEcc8He3kVz1LohKPIq1WzNFPu%2FnEg3p9K%2BGexK3O9mgv2BDjkv9SihKK%2BmJSL9saPAjpRGrhEZw0T9CCAhmwnYnSCsgyDtgCkMZiH9q4ISovw8qEVDf65odttBtEYIbvMfjDfoOhN1QcUFmJhtiGXKs3wVCLXJ0EE3t%2BXaMV1h6onEm&X-Amz-Signature=82a9f6465fa7884d7fd0a911163e12e291ae8321089171b1d287d344678f603d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
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
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/a9a40cea-8aa5-4715-9bc3-1621e47671dd/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663NLJSHYS%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T220856Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIDkPCrEJOdf2ONZvqoAGM5PSl9XfJAD0kYdztHjNKVKeAiEAttCaq4hQtYMEipbrjZcRseHuNsBqcWmviamzGT6Bz7sq%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDNAcG5QM7QUjwMi%2BWSrcA1Sx%2F%2ByvSm92UhabVctcp8wZtlwzW4MUi6dftVTmRPR%2FkZ4JiIL8gPYId2Kro%2Bd%2B0vqWijBMDNh%2B3mOFTRSTvICEXQt7USBA%2F8m8ajhqzLUSMH9UuE5YP1RPK3SjG6%2F08dlydixqB6DaEy0FsDjweZF1AQu6BqrLEj1GErrCRbZvL7Q0PHHhMr1xnHe6inCkSWoFM6gnLYM8geDZBBB2TLGTXlznsOnSaGLaZnl66AZytSkki8O1OX8sG%2FeDY5HcCij0bNgNVF419S8Np3fjDZu2dku%2B0WeDzwdYBnL7oHcEbrHuqHK5beNoM%2BP6WWDbj264gCJ7th%2FKn0dlC5OummrmA19ToWXvihLgOSJIS63YjKx8iG5wl2jbdWQMshUlO%2B2ZzOaC5SkWSpHzW%2BjuYb6RSHCgeJlhcPXpE3PXw83O8CcKm%2BkPlvmr1Dmqrj%2BDDVIizaRyZVe78sKkokBQzNe1YXukG85cp6pTuRXc0hsTeGO2E3WxuVjuBkvnxFm8cCJOcXTR4xlmHEiae5jg%2FuIyPi9yxkln0Y9BCt1Dq%2BvF4R2fNVVtZMMj2EKC0kPluS26PXv%2Bt%2FN29Gel3TU2BUBO%2BiKV%2B2zrp1rzVhRw%2Fe31sQSsK22IsurrZs9sMJ2m98kGOqUBGEX7IzQMAQmO5nNA0Hpp0HyYT2d3piyz84UwgNbCKmJoCEcc8He3kVz1LohKPIq1WzNFPu%2FnEg3p9K%2BGexK3O9mgv2BDjkv9SihKK%2BmJSL9saPAjpRGrhEZw0T9CCAhmwnYnSCsgyDtgCkMZiH9q4ISovw8qEVDf65odttBtEYIbvMfjDfoOhN1QcUFmJhtiGXKs3wVCLXJ0EE3t%2BXaMV1h6onEm&X-Amz-Signature=488759fec9af944bdf4274f7cd8bc31ea69893945535a3df06448d95835f12eb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
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
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/88ad3bb4-c8e5-4d76-a3d9-ecf4028c834b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YUY2J76K%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T220857Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJIMEYCIQDYBIlKM4E%2FB7Gq4l59PEErGhZmNrDdh2ByklgwGLJbgQIhAPcyRYYlwQCiXIm7h8daqH8bjthXjfeyv3m%2BCSgisj1TKv8DCCYQABoMNjM3NDIzMTgzODA1Igw36JPs5ERo8ci4uBYq3AOHRFh8DPZZol3DoBruPLg4buqUDwQatwHCzxvuRDu%2F64MDIawleysjKhRxFKqYM%2FHf8CnJOHBGX50ONqTZfu7EpDQMnWhTqKr8P95RwFVvinhLt3SVQAvXhpNE4nhJowfZu1jHU%2F0RWcOjlfbqyVPMyrgcy2BCOLYE3bpnNerU%2BgLZtA%2Fgwkdcml31qv1V5NUFNdxMsdvZz1RZozW1Djr4%2BlXKB73tb%2FNmoMtckKjKxN30SIHqH4ItHr3MoRf7Lt3Y0RUrHPvMcG74uEglKA6%2FMzzb%2F3vHTrecVxQs%2FYr4twZgH6f%2FISLk%2BnpjymBNGf929gMY8%2Fg7aNdo4q%2BOjqUjvM5L9cD%2B%2FRRtdyPplne4dG1qJmINznmVpuwzjR49TaNQdtyWmdpReBtO9ScrQulnIL3NLwI4ARkvBqSfTDuRaroNh2%2FZEmy3VUOVCnlDxaz2UKMHKM1prU4nPHN8taXZxqvgmVcU30PJRzIHFN7BEBs%2FtTGsXQAY42cbiNp1QlMkQr5LK%2FmFb6W9ZQiuAai0vmwpcTZ4cG4XWEXcYdkQeKnaBBQ2IucEiK8zAi2nJpZ3eZb6ZVnp6DHCe4WySDpUzsSVd7ChBRVL54iGOG6Gdv8UV8vjWpqhiUn0xzDIpffJBjqkAe%2FgsUKkIjDELxByt3C3J%2BMzjbU%2B0rVK5OXYjk%2BFrFsdGn6%2BpBnpwm%2FE5448iImiZ5x8438oj%2FE2KwRm6IvM5MhbwFPiBF5HlzMFgVe9VhDTRxqy1TQLS4oPVW%2Fa3lr2sHPtkS6lJKNfAVlHhif7AX%2FV9kB%2FvOio3bM8EoJg30Tk9ukZkoxGICR2GMaCkaiBDmPJ31DNhHQ4iyoHjfwniUHe5B2z&X-Amz-Signature=ecc8e61ddba4ca7a55c18cc52f83c276b566114f35ec40944da8afc4996c5593&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
Now we can reset the index. Again, it is important to do `inplace=True` as otherwise the DataFrame is not updated properly.
```python
players_df.reset_index(inplace=True)
```
In the updated DataFrame below we now can see that the column `Player` is a *normal* column again and the default index has been re-inserted.
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/1c343a9f-1a8f-4da3-94f2-72dc953341ae/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YUY2J76K%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T220857Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJIMEYCIQDYBIlKM4E%2FB7Gq4l59PEErGhZmNrDdh2ByklgwGLJbgQIhAPcyRYYlwQCiXIm7h8daqH8bjthXjfeyv3m%2BCSgisj1TKv8DCCYQABoMNjM3NDIzMTgzODA1Igw36JPs5ERo8ci4uBYq3AOHRFh8DPZZol3DoBruPLg4buqUDwQatwHCzxvuRDu%2F64MDIawleysjKhRxFKqYM%2FHf8CnJOHBGX50ONqTZfu7EpDQMnWhTqKr8P95RwFVvinhLt3SVQAvXhpNE4nhJowfZu1jHU%2F0RWcOjlfbqyVPMyrgcy2BCOLYE3bpnNerU%2BgLZtA%2Fgwkdcml31qv1V5NUFNdxMsdvZz1RZozW1Djr4%2BlXKB73tb%2FNmoMtckKjKxN30SIHqH4ItHr3MoRf7Lt3Y0RUrHPvMcG74uEglKA6%2FMzzb%2F3vHTrecVxQs%2FYr4twZgH6f%2FISLk%2BnpjymBNGf929gMY8%2Fg7aNdo4q%2BOjqUjvM5L9cD%2B%2FRRtdyPplne4dG1qJmINznmVpuwzjR49TaNQdtyWmdpReBtO9ScrQulnIL3NLwI4ARkvBqSfTDuRaroNh2%2FZEmy3VUOVCnlDxaz2UKMHKM1prU4nPHN8taXZxqvgmVcU30PJRzIHFN7BEBs%2FtTGsXQAY42cbiNp1QlMkQr5LK%2FmFb6W9ZQiuAai0vmwpcTZ4cG4XWEXcYdkQeKnaBBQ2IucEiK8zAi2nJpZ3eZb6ZVnp6DHCe4WySDpUzsSVd7ChBRVL54iGOG6Gdv8UV8vjWpqhiUn0xzDIpffJBjqkAe%2FgsUKkIjDELxByt3C3J%2BMzjbU%2B0rVK5OXYjk%2BFrFsdGn6%2BpBnpwm%2FE5448iImiZ5x8438oj%2FE2KwRm6IvM5MhbwFPiBF5HlzMFgVe9VhDTRxqy1TQLS4oPVW%2Fa3lr2sHPtkS6lJKNfAVlHhif7AX%2FV9kB%2FvOio3bM8EoJg30Tk9ukZkoxGICR2GMaCkaiBDmPJ31DNhHQ4iyoHjfwniUHe5B2z&X-Amz-Signature=9778d5c7666c6419146d2204a32f918ae74a9c845a45cc4a3c35760929cef37e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
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
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/3500737e-2456-4b38-af6d-a0173189cae1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664WLSP4DO%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T220858Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIQCRcP1lKTJdtI%2F0HbuNZ2ogU3wqg8RiofFIWnE97WDcPwIgEDDB%2B0mMFVB7HAYoEvBYPVmMLJ5SUgY4DbOMiMkaYwoq%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDGPYNIFvZiozH57u%2FyrcA5lftclmp%2FDYZfIRrPY1toQC9aAkEldcNArmkk9y9QM5pnkovQsoYJc6BW%2FP8o5u0VnGdVmAI4dIZmoGBPXO8U2GPjvtkabi8%2BK0w8FDfxRYFN9jEkHHtXZl16HDt0YQBr8KupnyUY2mZayKAq8QA0uqbwNFpU1bNSDTkKaJAvUCtSuqHx53ycARmQZTzE0xI5gF%2BuR2thFkisUU38lG%2BMn4uFM6rWsMZugMSCfce4WjkLhyOJeKhVRps3dO5QpLBop2WONPik2VEfq56UGaMqRyr6q5QUk2SbstWxgOxRnm7tzl2lLsyCZaWKBgkkQEv0XOXW1f0r0xhv6bDX5KsdYR4uDVa68VpvrHZPYhri569hzmfqXJp%2FGO4EEsKNpIaaY%2FN%2Fb%2F1TCuD1YW5nq8tMohKgaWYNJmk%2F8gZwt9lbL6cbFCKh1QFhVdiI7hevl8a6tKsgZAJJBMAcJmpGljuwGzPefe%2BfMCzf%2F4TRK7rDum1rNvyHS1L2fTG9uc%2BXO47jz%2BGVWXPvZIYE5J9PEtD5RoE03C5rzpzNs5Z172Tq06mGyYbhIDHxyRoXu3JOx3%2FPC%2Ft2Bs19SzA8Txpc%2FthqiDSr49uko66MXfjOWGwyKOX%2BQy6VgzruChuOOHMOel98kGOqUB0HtPHmO6uU8cjYNxmqCW1mIBCHVra0ITh84Mi8asFrNJInIp0HfBzEtiHl5Li3wmxw9q3bp48CRBe7q8jd63nQ69G7SgB5kSuX1r%2FVIeDXslIJ1ony4uXZeuerZ1NcztGjGXSDOqrVpk6wPOGI8Wle70Eyql9VZyZnH7lSq3gI1oQPsgcXBk2HTme09ELIes7SUJxvh4tDNW3Am392vHQBT30bqb&X-Amz-Signature=fdb696743404cfce8b11e123a2c1c5f2160aac611f58d53ba57863e40297df01&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
We can now get rid of this column by executing the following command.
```python
players_df.drop('Unnamed: 10', axis=1, inplace=True)
```
And the column is removed:
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/6be99418-6837-48ed-ba88-5757a28c6f5e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664WLSP4DO%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T220858Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIQCRcP1lKTJdtI%2F0HbuNZ2ogU3wqg8RiofFIWnE97WDcPwIgEDDB%2B0mMFVB7HAYoEvBYPVmMLJ5SUgY4DbOMiMkaYwoq%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDGPYNIFvZiozH57u%2FyrcA5lftclmp%2FDYZfIRrPY1toQC9aAkEldcNArmkk9y9QM5pnkovQsoYJc6BW%2FP8o5u0VnGdVmAI4dIZmoGBPXO8U2GPjvtkabi8%2BK0w8FDfxRYFN9jEkHHtXZl16HDt0YQBr8KupnyUY2mZayKAq8QA0uqbwNFpU1bNSDTkKaJAvUCtSuqHx53ycARmQZTzE0xI5gF%2BuR2thFkisUU38lG%2BMn4uFM6rWsMZugMSCfce4WjkLhyOJeKhVRps3dO5QpLBop2WONPik2VEfq56UGaMqRyr6q5QUk2SbstWxgOxRnm7tzl2lLsyCZaWKBgkkQEv0XOXW1f0r0xhv6bDX5KsdYR4uDVa68VpvrHZPYhri569hzmfqXJp%2FGO4EEsKNpIaaY%2FN%2Fb%2F1TCuD1YW5nq8tMohKgaWYNJmk%2F8gZwt9lbL6cbFCKh1QFhVdiI7hevl8a6tKsgZAJJBMAcJmpGljuwGzPefe%2BfMCzf%2F4TRK7rDum1rNvyHS1L2fTG9uc%2BXO47jz%2BGVWXPvZIYE5J9PEtD5RoE03C5rzpzNs5Z172Tq06mGyYbhIDHxyRoXu3JOx3%2FPC%2Ft2Bs19SzA8Txpc%2FthqiDSr49uko66MXfjOWGwyKOX%2BQy6VgzruChuOOHMOel98kGOqUB0HtPHmO6uU8cjYNxmqCW1mIBCHVra0ITh84Mi8asFrNJInIp0HfBzEtiHl5Li3wmxw9q3bp48CRBe7q8jd63nQ69G7SgB5kSuX1r%2FVIeDXslIJ1ony4uXZeuerZ1NcztGjGXSDOqrVpk6wPOGI8Wle70Eyql9VZyZnH7lSq3gI1oQPsgcXBk2HTme09ELIes7SUJxvh4tDNW3Am392vHQBT30bqb&X-Amz-Signature=bd0b951d24345b55fae88ff6a894c7ac59f40e489f67da4d5cfe8ac3154b54a8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
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
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/281439eb-3e8c-4578-887f-f90824b57da7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZNQ3K5ET%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T220859Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIQDyok0EtNaf1Rv0Hj%2FTQy9icnSDhNCJTH1%2B4QoGrlpI0gIgXq3OWReCdUSJF%2F48aPUIuXMPFdGejTRy2Oor717f9ikq%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDF4LwF6toqWNxPYKpSrcA78VePL7O9Rvskjc9Fuqcjc1%2FZi90aDNKKU%2FievucgqK9oPtugn%2Fv7oZCIYIIH9%2FEnJU3xEKCqvh%2F4lg0u8DQZKGXyE5tJiuvf6g817uoVYM0wkEHWXwoRVAL951JK5P4QdSqQ6CeMcGTrdZSRq0k2qzk4d7%2BJgj9JBEb8MiU4oHLJnsXYqoF1ShHGsDYHgBuEdEz9i1EzT2hH%2BL7OCh3DeOmyc8X11xwP7k1UNDaMOk9QjShCLm9Zt2ZwGNAi%2BO21koO8pKmOH82T1tXgaNjcjMH%2Fh8yqhAERBxDMBscWUn6%2F%2Fgt8jCGw7H35q6AusA8hZCDhJbVWWhLOt7yl3Ateuef1i8ME3NphVB1fDgQ79szu7ycN2r3cIt5axq66y7uiAfmtqjY9xRhMX%2Flz%2FxGI%2FCylSzHyqqbvHfT7zJIErxnqah%2FWmamfQi18ft3lXvQq4%2BVI90fMxcDC8qfJEtSgOhnuF7u8l%2FYLUbHkizIgACN4kfJJ%2F3YFgQ0VCgmIfU5LJRlw49seKZ3uoJPsPekBJCbMxBiO1hx97Bi1HnGABVOB6VMIEv%2FclsDYPokS%2FitaBsP0ejOzkVur5v8blk8lE87fjfF4tZMyFfnJNVDNl0LJFl3NHO2CpZ3gP0MJGm98kGOqUB5P1W4ec4JGXTOQAKuO1vd1DeZ5VdahWWWqylSgyUcADvAAItcqvEe%2FpaLv1%2BasLShCXou6mo0YMivtYz%2FNjhRRBg%2F62ieDgSBonkN5t%2BHZp4rOmR67Ek8siAFyXOTggbzFP19e8W594HUKjTkdKBG8cJKco%2BCs5l%2Bet2hWMMwJtTNGYlsUXxXs63xlNqujUAOUD50RQT3H7RmDOvoWR7Op%2BsZgEJ&X-Amz-Signature=4ad59e130d3a8812161369f1e7b2d9f549d3e9eeefe3948f01bb4045a27fbea5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
We see that the values have been updated to `NaN`
Let’s remove the column `Team` using `.dropna()`
```python
players_df.dropna(axis=0, how='any', inplace=True)
players_df[:3]
```
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/5f6f5b09-95c7-4fd4-a7fe-ee8d8e53f780/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZNQ3K5ET%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T220859Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIQDyok0EtNaf1Rv0Hj%2FTQy9icnSDhNCJTH1%2B4QoGrlpI0gIgXq3OWReCdUSJF%2F48aPUIuXMPFdGejTRy2Oor717f9ikq%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDF4LwF6toqWNxPYKpSrcA78VePL7O9Rvskjc9Fuqcjc1%2FZi90aDNKKU%2FievucgqK9oPtugn%2Fv7oZCIYIIH9%2FEnJU3xEKCqvh%2F4lg0u8DQZKGXyE5tJiuvf6g817uoVYM0wkEHWXwoRVAL951JK5P4QdSqQ6CeMcGTrdZSRq0k2qzk4d7%2BJgj9JBEb8MiU4oHLJnsXYqoF1ShHGsDYHgBuEdEz9i1EzT2hH%2BL7OCh3DeOmyc8X11xwP7k1UNDaMOk9QjShCLm9Zt2ZwGNAi%2BO21koO8pKmOH82T1tXgaNjcjMH%2Fh8yqhAERBxDMBscWUn6%2F%2Fgt8jCGw7H35q6AusA8hZCDhJbVWWhLOt7yl3Ateuef1i8ME3NphVB1fDgQ79szu7ycN2r3cIt5axq66y7uiAfmtqjY9xRhMX%2Flz%2FxGI%2FCylSzHyqqbvHfT7zJIErxnqah%2FWmamfQi18ft3lXvQq4%2BVI90fMxcDC8qfJEtSgOhnuF7u8l%2FYLUbHkizIgACN4kfJJ%2F3YFgQ0VCgmIfU5LJRlw49seKZ3uoJPsPekBJCbMxBiO1hx97Bi1HnGABVOB6VMIEv%2FclsDYPokS%2FitaBsP0ejOzkVur5v8blk8lE87fjfF4tZMyFfnJNVDNl0LJFl3NHO2CpZ3gP0MJGm98kGOqUB5P1W4ec4JGXTOQAKuO1vd1DeZ5VdahWWWqylSgyUcADvAAItcqvEe%2FpaLv1%2BasLShCXou6mo0YMivtYz%2FNjhRRBg%2F62ieDgSBonkN5t%2BHZp4rOmR67Ek8siAFyXOTggbzFP19e8W594HUKjTkdKBG8cJKco%2BCs5l%2Bet2hWMMwJtTNGYlsUXxXs63xlNqujUAOUD50RQT3H7RmDOvoWR7Op%2BsZgEJ&X-Amz-Signature=5d50757df199e26c93e130e0de3dccc96e15c063ce581d44bf5585810a594cc2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
We see that the players Jamie Vardy and Pierre-Emerick Aubameyang have been removed as they contained at least one `NaN` value (in column `Team`).
---
**Remove columns with ****`NaN`**** value**
Now let’s set all values in column `Goals` to `NaN` values, except the first one.
```python
players_df.iloc[1:, 6] = np.NaN
players_df
```
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/ad5ad8d5-f3a1-4426-8c36-08628fbe3f75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZNQ3K5ET%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T220859Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIQDyok0EtNaf1Rv0Hj%2FTQy9icnSDhNCJTH1%2B4QoGrlpI0gIgXq3OWReCdUSJF%2F48aPUIuXMPFdGejTRy2Oor717f9ikq%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDF4LwF6toqWNxPYKpSrcA78VePL7O9Rvskjc9Fuqcjc1%2FZi90aDNKKU%2FievucgqK9oPtugn%2Fv7oZCIYIIH9%2FEnJU3xEKCqvh%2F4lg0u8DQZKGXyE5tJiuvf6g817uoVYM0wkEHWXwoRVAL951JK5P4QdSqQ6CeMcGTrdZSRq0k2qzk4d7%2BJgj9JBEb8MiU4oHLJnsXYqoF1ShHGsDYHgBuEdEz9i1EzT2hH%2BL7OCh3DeOmyc8X11xwP7k1UNDaMOk9QjShCLm9Zt2ZwGNAi%2BO21koO8pKmOH82T1tXgaNjcjMH%2Fh8yqhAERBxDMBscWUn6%2F%2Fgt8jCGw7H35q6AusA8hZCDhJbVWWhLOt7yl3Ateuef1i8ME3NphVB1fDgQ79szu7ycN2r3cIt5axq66y7uiAfmtqjY9xRhMX%2Flz%2FxGI%2FCylSzHyqqbvHfT7zJIErxnqah%2FWmamfQi18ft3lXvQq4%2BVI90fMxcDC8qfJEtSgOhnuF7u8l%2FYLUbHkizIgACN4kfJJ%2F3YFgQ0VCgmIfU5LJRlw49seKZ3uoJPsPekBJCbMxBiO1hx97Bi1HnGABVOB6VMIEv%2FclsDYPokS%2FitaBsP0ejOzkVur5v8blk8lE87fjfF4tZMyFfnJNVDNl0LJFl3NHO2CpZ3gP0MJGm98kGOqUB5P1W4ec4JGXTOQAKuO1vd1DeZ5VdahWWWqylSgyUcADvAAItcqvEe%2FpaLv1%2BasLShCXou6mo0YMivtYz%2FNjhRRBg%2F62ieDgSBonkN5t%2BHZp4rOmR67Ek8siAFyXOTggbzFP19e8W594HUKjTkdKBG8cJKco%2BCs5l%2Bet2hWMMwJtTNGYlsUXxXs63xlNqujUAOUD50RQT3H7RmDOvoWR7Op%2BsZgEJ&X-Amz-Signature=70ec0c3a1b11496e9f32ee7c92ec38f0c30a3c12bbc0f4b16d5ec1be0d950aa3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
We see that all values in column `Goals` are `NaN` except for the first player.
Let’s try to drop that column `Goals` using `.dropna()`
```python
players_df.dropna(axis=1, how='all', inplace=True)
players_df
```
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/ad5ad8d5-f3a1-4426-8c36-08628fbe3f75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZNQ3K5ET%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T220859Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIQDyok0EtNaf1Rv0Hj%2FTQy9icnSDhNCJTH1%2B4QoGrlpI0gIgXq3OWReCdUSJF%2F48aPUIuXMPFdGejTRy2Oor717f9ikq%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDF4LwF6toqWNxPYKpSrcA78VePL7O9Rvskjc9Fuqcjc1%2FZi90aDNKKU%2FievucgqK9oPtugn%2Fv7oZCIYIIH9%2FEnJU3xEKCqvh%2F4lg0u8DQZKGXyE5tJiuvf6g817uoVYM0wkEHWXwoRVAL951JK5P4QdSqQ6CeMcGTrdZSRq0k2qzk4d7%2BJgj9JBEb8MiU4oHLJnsXYqoF1ShHGsDYHgBuEdEz9i1EzT2hH%2BL7OCh3DeOmyc8X11xwP7k1UNDaMOk9QjShCLm9Zt2ZwGNAi%2BO21koO8pKmOH82T1tXgaNjcjMH%2Fh8yqhAERBxDMBscWUn6%2F%2Fgt8jCGw7H35q6AusA8hZCDhJbVWWhLOt7yl3Ateuef1i8ME3NphVB1fDgQ79szu7ycN2r3cIt5axq66y7uiAfmtqjY9xRhMX%2Flz%2FxGI%2FCylSzHyqqbvHfT7zJIErxnqah%2FWmamfQi18ft3lXvQq4%2BVI90fMxcDC8qfJEtSgOhnuF7u8l%2FYLUbHkizIgACN4kfJJ%2F3YFgQ0VCgmIfU5LJRlw49seKZ3uoJPsPekBJCbMxBiO1hx97Bi1HnGABVOB6VMIEv%2FclsDYPokS%2FitaBsP0ejOzkVur5v8blk8lE87fjfF4tZMyFfnJNVDNl0LJFl3NHO2CpZ3gP0MJGm98kGOqUB5P1W4ec4JGXTOQAKuO1vd1DeZ5VdahWWWqylSgyUcADvAAItcqvEe%2FpaLv1%2BasLShCXou6mo0YMivtYz%2FNjhRRBg%2F62ieDgSBonkN5t%2BHZp4rOmR67Ek8siAFyXOTggbzFP19e8W594HUKjTkdKBG8cJKco%2BCs5l%2Bet2hWMMwJtTNGYlsUXxXs63xlNqujUAOUD50RQT3H7RmDOvoWR7Op%2BsZgEJ&X-Amz-Signature=70ec0c3a1b11496e9f32ee7c92ec38f0c30a3c12bbc0f4b16d5ec1be0d950aa3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
We see that the column Goals was not removed. This is because we set `how` to `'all'`. Therefore, Python drops the column only if all values are `NaN`, which however is not the case as the first player has a normal value in column `Goals`.
Let’s set the value of the first player in column `Goals` to `NaN` as well.
```python
players_df.loc[0, 'Goals'] = np.NaN
players_df
```
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/5ca553a1-414f-4170-9177-39820cbd9529/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZNQ3K5ET%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T220859Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIQDyok0EtNaf1Rv0Hj%2FTQy9icnSDhNCJTH1%2B4QoGrlpI0gIgXq3OWReCdUSJF%2F48aPUIuXMPFdGejTRy2Oor717f9ikq%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDF4LwF6toqWNxPYKpSrcA78VePL7O9Rvskjc9Fuqcjc1%2FZi90aDNKKU%2FievucgqK9oPtugn%2Fv7oZCIYIIH9%2FEnJU3xEKCqvh%2F4lg0u8DQZKGXyE5tJiuvf6g817uoVYM0wkEHWXwoRVAL951JK5P4QdSqQ6CeMcGTrdZSRq0k2qzk4d7%2BJgj9JBEb8MiU4oHLJnsXYqoF1ShHGsDYHgBuEdEz9i1EzT2hH%2BL7OCh3DeOmyc8X11xwP7k1UNDaMOk9QjShCLm9Zt2ZwGNAi%2BO21koO8pKmOH82T1tXgaNjcjMH%2Fh8yqhAERBxDMBscWUn6%2F%2Fgt8jCGw7H35q6AusA8hZCDhJbVWWhLOt7yl3Ateuef1i8ME3NphVB1fDgQ79szu7ycN2r3cIt5axq66y7uiAfmtqjY9xRhMX%2Flz%2FxGI%2FCylSzHyqqbvHfT7zJIErxnqah%2FWmamfQi18ft3lXvQq4%2BVI90fMxcDC8qfJEtSgOhnuF7u8l%2FYLUbHkizIgACN4kfJJ%2F3YFgQ0VCgmIfU5LJRlw49seKZ3uoJPsPekBJCbMxBiO1hx97Bi1HnGABVOB6VMIEv%2FclsDYPokS%2FitaBsP0ejOzkVur5v8blk8lE87fjfF4tZMyFfnJNVDNl0LJFl3NHO2CpZ3gP0MJGm98kGOqUB5P1W4ec4JGXTOQAKuO1vd1DeZ5VdahWWWqylSgyUcADvAAItcqvEe%2FpaLv1%2BasLShCXou6mo0YMivtYz%2FNjhRRBg%2F62ieDgSBonkN5t%2BHZp4rOmR67Ek8siAFyXOTggbzFP19e8W594HUKjTkdKBG8cJKco%2BCs5l%2Bet2hWMMwJtTNGYlsUXxXs63xlNqujUAOUD50RQT3H7RmDOvoWR7Op%2BsZgEJ&X-Amz-Signature=8ae8430187b0f25476b8fff1bb53ec6ce1685bd530f27962f3dbbb45e4c9997b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
We see that the column `Goals` now contains `NaN` values only. So let’s try to run the `.dropna()` command from before again.
```python
players_df.dropna(axis=1, how='all', inplace=True)
players_df
```
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/e67efd46-7779-477d-95d2-b7ad6a53c9bf/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZNQ3K5ET%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T220859Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIQDyok0EtNaf1Rv0Hj%2FTQy9icnSDhNCJTH1%2B4QoGrlpI0gIgXq3OWReCdUSJF%2F48aPUIuXMPFdGejTRy2Oor717f9ikq%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDF4LwF6toqWNxPYKpSrcA78VePL7O9Rvskjc9Fuqcjc1%2FZi90aDNKKU%2FievucgqK9oPtugn%2Fv7oZCIYIIH9%2FEnJU3xEKCqvh%2F4lg0u8DQZKGXyE5tJiuvf6g817uoVYM0wkEHWXwoRVAL951JK5P4QdSqQ6CeMcGTrdZSRq0k2qzk4d7%2BJgj9JBEb8MiU4oHLJnsXYqoF1ShHGsDYHgBuEdEz9i1EzT2hH%2BL7OCh3DeOmyc8X11xwP7k1UNDaMOk9QjShCLm9Zt2ZwGNAi%2BO21koO8pKmOH82T1tXgaNjcjMH%2Fh8yqhAERBxDMBscWUn6%2F%2Fgt8jCGw7H35q6AusA8hZCDhJbVWWhLOt7yl3Ateuef1i8ME3NphVB1fDgQ79szu7ycN2r3cIt5axq66y7uiAfmtqjY9xRhMX%2Flz%2FxGI%2FCylSzHyqqbvHfT7zJIErxnqah%2FWmamfQi18ft3lXvQq4%2BVI90fMxcDC8qfJEtSgOhnuF7u8l%2FYLUbHkizIgACN4kfJJ%2F3YFgQ0VCgmIfU5LJRlw49seKZ3uoJPsPekBJCbMxBiO1hx97Bi1HnGABVOB6VMIEv%2FclsDYPokS%2FitaBsP0ejOzkVur5v8blk8lE87fjfF4tZMyFfnJNVDNl0LJFl3NHO2CpZ3gP0MJGm98kGOqUB5P1W4ec4JGXTOQAKuO1vd1DeZ5VdahWWWqylSgyUcADvAAItcqvEe%2FpaLv1%2BasLShCXou6mo0YMivtYz%2FNjhRRBg%2F62ieDgSBonkN5t%2BHZp4rOmR67Ek8siAFyXOTggbzFP19e8W594HUKjTkdKBG8cJKco%2BCs5l%2Bet2hWMMwJtTNGYlsUXxXs63xlNqujUAOUD50RQT3H7RmDOvoWR7Op%2BsZgEJ&X-Amz-Signature=cf9e9cdfe221dc4be28e6d4a30490305500d233c0754a1dcf748357607c3a2a7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
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
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/b3a38d78-543d-4e69-aabf-aba15f3000db/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SSCKHMP5%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T220902Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIQDqn9KtDTF4fAIRVCIR%2FwfJGZSQqk8SEDjbiARao7X7VgIgPD%2Bw%2FLfbq9ysAp0a4DAq2GB13yDTX8J7VDTWxOaLYcsq%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDAkGPhgMfavjkC3AXircA4KhjmgbU%2Fb57jY7LlDlmY%2BeLDfLt6o1ZMZUCatDKBvAkk1HLZDpZFVu9ZP%2F417rwMLOaH7JEl2UKB5aqtCv%2FgaqS7rRqyXb5myMZR7K0QCzhK4Sm2Rgyb9imDO4Ya3nCqDu6ZmznwTGUZFaahrn%2FStByDib0rzxPOast68Tnr6SeQfvvaVUdl72NC0%2F1QRGxCOHeFa7UnwejiTT0mfNflU3Dl%2FRVuy64YDITBt04rJqqPTGH74Gb1Hpzyh%2BV64jYxCTyoD3MvLfBderl7uzyxw3h%2BLZaGU6wPINysmZ22gOC7DsIpRG5qW4uzf8Xuii4WSoKiOblZLgBlu9TweI4UWNAEcvI6F%2FwiJXR4kY9FFx%2FCZpjZogP6380Ku6Xe8VF9oX4lkv%2BWxHyQCVeHmuQsL3TDHTScN00UAo%2Fvku1q3PfCMtoeTFUhRnbe8yJenGLr3%2Bz8uIr1R%2BbqtMGbJf%2BVMzzhrw5IkMlRZpB%2BvKxeJ4QUAPc78JLBo4MJw68o4nVCqJrXzAzip2bDB8iSKdcFc4LpCLk80hmX4TaW%2Bpxj8EGUNCwR%2FJgwrR%2FRwWBsNmsvEAslxE7MJB6pZKMt8Y8qxzWiJLQrQ7ACUVtAXsX3cfZtmPeFn%2FrQJY7U2aMN6m98kGOqUB5GY%2BQSwDzbJCndGLLMJqXeeWl8kZGMv70e9OvhpW6PxVGWG53EFr%2FzJFZFJESoUUXe2prN6wvJAxYWKYxRKlV7Ob0SkULEE%2FgA6lPsArrvEczDDJE2umcDPZ8knykI3gbuGtUReifVi6g%2BmlJBtywk6vJbaDQZqcJ898Ffoz7jHDPrlqFw9bN1Spc6QsINjruRBMha0%2BihXogzQCkdumr%2BR4qJia&X-Amz-Signature=ea2688a3feb737f6a9453855dcb42d7fcc91cdf79aa01dcdec085b4df6944088&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
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
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/e6cb3aae-51fa-4146-bfe6-5962772911ac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667FSSCWTJ%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T220903Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIAQ8FsOBXuSA%2FbQVO1%2B%2Fat1UXtycDHi27td4t7OM2lZ8AiEA3MYJeiUKU4Baa9DIV%2BNqJl48gNz9leYKt0M1JZo7QAcq%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDOZ%2BM3JvfECZeVBc4ircA5NW2t79RIRSqDE3OXOcvWxW5%2FLmquWa8y2FMPEaBvnH0v87XhqlKvHmzvsiA75gQosPc%2BFgQ08AZvJGnlRvpNC3BDiC45EcMkGxLy0Bej1sC2udWqfTWFy3NgcFuHpponDm17YxZvalHvL1WaYCsgS0wOvVg4Paewa%2F27SeRvZ1IAkNa%2FIziAIS6MECTfwEl9OtxuNC0X3glNxoSPg4ThprsLbDw8847Z0G795gV7erBoHy6yKgVWvOug5zQjf%2B8vyGi68gBJT8g97TRpX60uTQJbL4eepUuntP164l5Jnh2DJLgFJzM8tmBkwOiUL05Qo%2FibO39qDFmpp0KNUYli7%2BPo%2FwqubNPHECrFImzQ2mYVCUh9CRTiG2A099HWEe%2FLgH3OLTCG8NGX1db9BuwKdR0aDAn%2FrWqbBsv0qsxurapWPFw6KnH4eJm4FT2VPXLrzcr0sh17fDNmNlDyY7tYM0frawy1xUSDeoNNda0Z7FDxNoRLMjQkQmK70gmR%2BxQUgskRbDgcZtmWqLk%2BKUBCKC9fRnCggOq1JJxs%2FZyD%2FqBOz0ylNUB%2FD1IgVm2ksgQ9oL16yRS9v0ayy4xqY4TH%2B1KPjXibJR2yWO0hFCbQtYal7vdLywA%2FQqw0mHMPul98kGOqUBzANYoJoOKJyEQpkUnwvnRJeHQ3%2BO72PVKVz5zvkiajNMw4jEngw71TYSOAYoUz6fIqdxqQA00BJii2P1yZ8AZTHlo1JG%2BfOGpEUkobKV5%2BD8jLexacTntqGPvm8nUdCpGMa4wwRdoOEDZ4Vs4xRr2r7eiVFq9IyomREsON%2FmUmHiz9jZWbGhEmpWAFfEy7JE2aVm9T%2BmCUnREJmcQRlSE%2F6SA7Lf&X-Amz-Signature=1213e20d8780a93a7205420715969e169666532d26e6e9e0cb4b190e1d60742f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
We see that we have now a new column `days_played` which currently has the same values as `Minutes played`.
To convert the minutes in column `days_played` to days we can make use of the `.apply()` function.
```python
players_df['days_played'] = players_df['days_played'].apply(lambda x : x / 60 / 24)
players_df
```
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/02dda6da-5622-463a-9140-8612b4cea207/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667FSSCWTJ%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T220903Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIAQ8FsOBXuSA%2FbQVO1%2B%2Fat1UXtycDHi27td4t7OM2lZ8AiEA3MYJeiUKU4Baa9DIV%2BNqJl48gNz9leYKt0M1JZo7QAcq%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDOZ%2BM3JvfECZeVBc4ircA5NW2t79RIRSqDE3OXOcvWxW5%2FLmquWa8y2FMPEaBvnH0v87XhqlKvHmzvsiA75gQosPc%2BFgQ08AZvJGnlRvpNC3BDiC45EcMkGxLy0Bej1sC2udWqfTWFy3NgcFuHpponDm17YxZvalHvL1WaYCsgS0wOvVg4Paewa%2F27SeRvZ1IAkNa%2FIziAIS6MECTfwEl9OtxuNC0X3glNxoSPg4ThprsLbDw8847Z0G795gV7erBoHy6yKgVWvOug5zQjf%2B8vyGi68gBJT8g97TRpX60uTQJbL4eepUuntP164l5Jnh2DJLgFJzM8tmBkwOiUL05Qo%2FibO39qDFmpp0KNUYli7%2BPo%2FwqubNPHECrFImzQ2mYVCUh9CRTiG2A099HWEe%2FLgH3OLTCG8NGX1db9BuwKdR0aDAn%2FrWqbBsv0qsxurapWPFw6KnH4eJm4FT2VPXLrzcr0sh17fDNmNlDyY7tYM0frawy1xUSDeoNNda0Z7FDxNoRLMjQkQmK70gmR%2BxQUgskRbDgcZtmWqLk%2BKUBCKC9fRnCggOq1JJxs%2FZyD%2FqBOz0ylNUB%2FD1IgVm2ksgQ9oL16yRS9v0ayy4xqY4TH%2B1KPjXibJR2yWO0hFCbQtYal7vdLywA%2FQqw0mHMPul98kGOqUBzANYoJoOKJyEQpkUnwvnRJeHQ3%2BO72PVKVz5zvkiajNMw4jEngw71TYSOAYoUz6fIqdxqQA00BJii2P1yZ8AZTHlo1JG%2BfOGpEUkobKV5%2BD8jLexacTntqGPvm8nUdCpGMa4wwRdoOEDZ4Vs4xRr2r7eiVFq9IyomREsON%2FmUmHiz9jZWbGhEmpWAFfEy7JE2aVm9T%2BmCUnREJmcQRlSE%2F6SA7Lf&X-Amz-Signature=66a6a3871d4e529bcc0aa941f31edc294b398c31c6440ad42b3331417a81a101&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
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
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/64f23972-80aa-4d97-bf3a-54c0965029ac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TPZRX3IE%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T220904Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIC%2BKWeImrNSNU8czMic2PBTwL0NCJadEzbGoMFxVvndnAiEA%2FBEkQ2Q8h3PntAGetQXSmaYStCp%2F5a4Xo6SlElsifLkq%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDPBLT8FI4MOZ3BlE4CrcAy98R1soUWEGDIt0QujQW8yP%2Bvx04%2F%2Bb1vyVgkL2zmXwncE8uNvPt7AxH7edBNfkL820V6e5R1o6hxw0XlGGVVuQSmDwCY9sooWkWGpdRE%2FdQJ8AozVPDTlILQXCbzIyDQIub%2F8RmE53RwVl%2BQVjQ%2FxBM4OXvINV5flOkIBb5zgW%2Ff6DWIStUZmbMRGOAVSGREOS7OtoZHQ5oghmc4MD9pT8DwFnMMFlOMuSpTYUalqv%2BhqyTHmup673V%2BP%2B%2BNPFV2VZUpHhU9EFCNJQD03L6SF1LgmKEdrEgMQcz%2FkAWAR6VMiAFfhpyH3ctswBH0BSvGJxhJG9ije9znVAfEKw6WHi1uUwz91k%2BRb%2FDpvFydQmH2od9S2i5DgdzcYpVvkN%2FCTDGKj5b3WSqXkJCOi6p1i6keoKodFLaWZ%2Fcjpo4BoSWhHf6Y8zXXZUmQmKQNwle4bIQKEYORUO7EOWqTaD4oxv8S6ulwGaIjuLedf1vOt6EOm4xWg8tv0P6C1yv3prmoO03Oi22nanMtlrDcVHcmtwUxM7JVlXGMSUXrWjLsm%2FBFxsD%2F7oTnSktx%2FdfnLEfEDt6trfNRbKDmCaYiCKNw37DWgE8C%2FFGgskzpfjRgYsriqLBu2E6kCyyyzwML2m98kGOqUBCv1cnvXChzweZhgdBPMQ6578hZKlcdrCv6tS68nDRiAboZ6hlWnmmE1hX%2FKtVK2S4zg8flXEOO8JMcht8On8LGLNwlTE2MTBXzoTHonhcpBI%2FCyiwe1Q0aQDbUrUVF3AFemnJvQd2nNqQ6jLzBd%2Bb4VuJmpdHLj4Js2CCm4sMhz94U5AsMw7rvHMQL02azzWs5%2FW7VyEx%2BgOPWqaCVBRmSDB7Nui&X-Amz-Signature=3f23f4470939b93f4946073fd825ca8807a2863e140159657ead97cdad01b518&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
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
![Values in column `points_per_game` are displayed with many digits after the point](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/55a9009d-5f21-44bb-9902-54885088791f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W4YPEKZE%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T220907Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJIMEYCIQCh4hQy4RKc8EpYoP3lZRfVJ8j7x06l4P%2FO%2FZR6f49DUwIhAN3Q5cqpFCnhX%2BFbYxnogOSvVy2No8SH7kFHtNHuM31wKv8DCCYQABoMNjM3NDIzMTgzODA1IgwM0ZNpwc%2FnH3JVWjAq3ANKzL8oS0ChoG0ROvZqD2jEvN7o3oyY8CyGUeBhxcMTjUpP6Mdb4S0AKJa0kELU9lOzULm3KsStPN7WjEFKfvzMTruyLTYBOxnOJI6QDRQ%2BlbCaF1jigQeX2hL0YRx%2BaCJfJaoTiSx5j5IBUKPjRMbv3r88x6V%2FvffvT%2FzRphOSK3dRV4pT%2FmVkkbX2zdQGTGFJeE58CZV%2FFPljgqYfkM3T7E7QzobvbS4SaIIeIm92u%2Fvg9y34EiPBenOLpPsJwR3GE2mKPf2NwyMC6k%2F4mMJoCPw9ItggqPlncg26q64PVjTW7etoKcEybZPpmKcuC9VRwP89kjX8tJ1jzBoS3DDHOWKZJmmxFv%2B1k1Ty2uM8rMw834oCWurd2K7LpNK0HtNzxMgAtC7%2FAs913obeKSRbsenOcQeCpcZeKRl56EyGoZpeOvTc7OMtaBV74rBWI4YAhQsUM%2Bonto%2B4WV444sYRlcxBLNrE6vHxPC4%2FJ13s6t%2BGTD%2BRD6xTlq8hwvUzfNphKWv8Eu1Y6nfgMq%2BE1N5sud1cZENLkEk5JSVygd%2BYTlrJY5pv9bbvzRgpHepmIHUsS3xYm92WrO9fKaSb5ewb4iD%2FP9INZqBAVd3%2F5YPOy8ZS9GgpebuYLxw2rzC1pvfJBjqkAZLPgS%2FwBVLUTXpSl7%2BioQiezx7JiPvPwNP0BGdIeI%2BrD03eVtlbDjG%2FFMgG9sUx%2F%2BLnFIjCeBrJF0oxR93X4%2F4XQoEjzLwtSC9h%2FCVNiTqDzJfNUrnUoCpGKv%2FvhwogdO25jCJ6ea2xFnvCgU%2B8N1keUY%2Fe7RoPfzvr4bM4dZJ0dYZsEBCrfPVqRic4qq81DTNQ%2B4oErm7N1wW8ksK4esCNMcBJ&X-Amz-Signature=2bd7dad56cc8442c6e8cea41ec5b888b1768cffc99f2cae4efe27d9f1aab6c3d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
To mitigate this issue we can set the `global display.precision` option to value `2`.
```python
pd.set_option("display.precision", 2)
```
![Values in column `points_per_game` are now display with 2 digits after the point only](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/a0af3d06-c869-442f-b9aa-8db80bce1341/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W4YPEKZE%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T220907Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJIMEYCIQCh4hQy4RKc8EpYoP3lZRfVJ8j7x06l4P%2FO%2FZR6f49DUwIhAN3Q5cqpFCnhX%2BFbYxnogOSvVy2No8SH7kFHtNHuM31wKv8DCCYQABoMNjM3NDIzMTgzODA1IgwM0ZNpwc%2FnH3JVWjAq3ANKzL8oS0ChoG0ROvZqD2jEvN7o3oyY8CyGUeBhxcMTjUpP6Mdb4S0AKJa0kELU9lOzULm3KsStPN7WjEFKfvzMTruyLTYBOxnOJI6QDRQ%2BlbCaF1jigQeX2hL0YRx%2BaCJfJaoTiSx5j5IBUKPjRMbv3r88x6V%2FvffvT%2FzRphOSK3dRV4pT%2FmVkkbX2zdQGTGFJeE58CZV%2FFPljgqYfkM3T7E7QzobvbS4SaIIeIm92u%2Fvg9y34EiPBenOLpPsJwR3GE2mKPf2NwyMC6k%2F4mMJoCPw9ItggqPlncg26q64PVjTW7etoKcEybZPpmKcuC9VRwP89kjX8tJ1jzBoS3DDHOWKZJmmxFv%2B1k1Ty2uM8rMw834oCWurd2K7LpNK0HtNzxMgAtC7%2FAs913obeKSRbsenOcQeCpcZeKRl56EyGoZpeOvTc7OMtaBV74rBWI4YAhQsUM%2Bonto%2B4WV444sYRlcxBLNrE6vHxPC4%2FJ13s6t%2BGTD%2BRD6xTlq8hwvUzfNphKWv8Eu1Y6nfgMq%2BE1N5sud1cZENLkEk5JSVygd%2BYTlrJY5pv9bbvzRgpHepmIHUsS3xYm92WrO9fKaSb5ewb4iD%2FP9INZqBAVd3%2F5YPOy8ZS9GgpebuYLxw2rzC1pvfJBjqkAZLPgS%2FwBVLUTXpSl7%2BioQiezx7JiPvPwNP0BGdIeI%2BrD03eVtlbDjG%2FFMgG9sUx%2F%2BLnFIjCeBrJF0oxR93X4%2F4XQoEjzLwtSC9h%2FCVNiTqDzJfNUrnUoCpGKv%2FvhwogdO25jCJ6ea2xFnvCgU%2B8N1keUY%2Fe7RoPfzvr4bM4dZJ0dYZsEBCrfPVqRic4qq81DTNQ%2B4oErm7N1wW8ksK4esCNMcBJ&X-Amz-Signature=35a10faaf22c293c090814b9784258ef92eda1536c8fc921c0d1cb6a03ed9dad&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
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
![df](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/bcfe397f-55ca-4491-9243-a6f63e35a4ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TD2P2JHF%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T220908Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIQDd%2FYh2yqy7Lf6xaLMQIGxvhhtbAcDVn6JmOznhIo%2FXKQIgWWQVs7CD%2BAQwXWDI2Ssyx8LOuJyV2S626Icc8kY1UFQq%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDEgEm4S%2FEsnW0RZuUSrcA4iWO7hB4P2vjuXaMuLZkFeo1ftd2e3mdhs5xMGHqDYvIPPaJwDhnzh%2B%2FzoNjVi1aI%2FqewceNuCM%2Blw9bFs3EpXzUVa6SD9ZJ6YoBZzGy1Q1cEoURGrZU0BPkBsj1EB0rdeEfIDPcUSl2Vu%2Bh8Wkn8GlXJRn8vj6V%2B9UWvYclxHZVEFycUEYiZ53Q4SsEZMddUTA4wa%2BFxZPkN9G6pnYn3Hf7Y2pE0ZdnujaVIKcg4kTTurlqBc8W%2FydydjdmVUQo7pMnC52KWFGcvfZz0KYknvczE2j8aZrwaZ%2F78fnUxEzXm2eH50N2qlrmaTFmlQ%2B5uOS5cuQq05%2B0OzvTk4SRDWJJ5grHSUmUfHwjTU%2B3asqkJqDW%2BwD5YIt%2BLEYQFJQ5WHHqgwLtMtwZvPSelbqs3u7eD76Wc7Esb8UhnX7RfRRPicGaPFQOLrRAKD5NNDPCxdu6UxIQQ6%2BmY5Y9ibs2RX5a95I10HYbgd1W4PghVkW9ulvn%2Ft%2BKGLXD7gHr6NvsZG18QKfiJ%2B3ZWr7voF1t5UsSh2L4QY0zLUu3A0GebN3zEppBHO%2F9C4aZCgZ2p%2BlVRcn7KSAsv3QGRWqCDij9dz1wFEghn%2BgeNhITCGkmV4YGc5JGtysScYGL6uaMKym98kGOqUBNwrwox3gICct%2F%2Fv5CW0i6kPBmzP%2BVwxgwSYeVqIFm%2Bty3sCLZJpSs9rnicTxMiz0CJnLP16LnBYhItA5D92OZOXNBbH2hdMoT6Jf5aNPq8nK1roBnEY4vVooXp0%2F3QmrhurwYvmEICAB3rFSlNca%2Ba%2BeYisN8PLfnVOlpzronkr5XiNfUiEvU7ltaSIydE7jaACPkR1Wi8tcVLhAnrqBaUgAj5c6&X-Amz-Signature=61669756cdc629a676a4bf0b7dcd926ac164dbec023ceaeab6a85bae0b6db01e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
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
![DataFrame containing dummy variables](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/4055b8ed-a655-4789-8cb6-7c93435f4317/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665QT5DR24%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T220910Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIQCg5xD97xNJpPbdupJSOqIaRcupryL3c4POiWGrpmGQIwIgBoDZncweJju9%2BRBmD9vxyCxkTIGZRtCQnsjFy22ekDAq%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDMwnLRnFMrwdOmPCiSrcA%2FnlYqzeYDWBuuWVzETOOhLW1SgcdSpd%2F0zVQjOKl8mmlLi2C6BBNUNYfjeSDDobb%2F19DhQF9SNAmMljiFEdJzBVF9JQ99ACkLRYtkn75MNcx%2Feft7Kz3Qj8pSbNNVH9a3rtd3cNzLYLD4L%2BeQyl89M5%2B3Q2Yzn9JqTjfOKaKg4H97dAct%2Bl7VB9BMYu4mik7lR1c7S3yvE7j62R%2B7SboqFsQIGHG683atm%2BFpG6aisfC2nI4ra9fmP57eE7uvD5Fh9HO0kIrqWhU9bpp5e1Yoi%2BNrbB26DhZtH5awJX95Ux3iJ8ns2xZmoE5Ep%2F%2B1VQHt8UX45GX6gaecRIv2J546%2F3ICSftBNvGAarBBqIVz%2FdE5p51tKY5kfJn0HwStOicM3JhEeRqzjO%2FGyaecRjDB5D9TWaw06Kj%2FN%2BlJs5aVIUZS99dv%2BWCfEsxX2ke5zovKLCdLARFrrAVJWkFGmsm9gYV%2BY5%2FJUHHst6%2BgiOc%2F%2BqbnX4gkid7Ew5vEVztZbFzDLkEiDuze7q1TqChF8HldkOlo6vpwx1kuWz6osLfw2MTcIGt47suYxIwQ6%2FZBvqTMFIctfe2P3HaAUnNLrS9d240yh8AN1PPwmcgEwhhX%2B7Kl2z6u252pTDrx1nMO%2Bl98kGOqUBHu1KJUH7BuVjhsZuQBDJVspC%2FctLZFGTCu3v4sm%2F%2BpSN%2BRcGCSqJgTw9nFmHd2pbSxBkfa63GB5%2FH%2B1PbaaVxjnZZk7ZtwMcDA1r7HpWAUjwhTaGXT%2B1tmr3CNZsfJkVq45kD%2BidHpAyg2eIIzOQ8qo4lGkenyZoqIKOORRb5aAGaThcvNccwGOfNY3B4XMx6JNOMnH1rmzjcQw8l6iJ9UsqcbHo&X-Amz-Signature=9356c9cc3a8c3300d04bea66c3d7a248e5100b702c500ae03c2b41390bcbaa1f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
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
![DataFrame containing dummy variables for column `Team` of the first 10 players](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/49b381e1-2960-4843-a225-f757446bd0ef/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665QT5DR24%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T220910Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIQCg5xD97xNJpPbdupJSOqIaRcupryL3c4POiWGrpmGQIwIgBoDZncweJju9%2BRBmD9vxyCxkTIGZRtCQnsjFy22ekDAq%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDMwnLRnFMrwdOmPCiSrcA%2FnlYqzeYDWBuuWVzETOOhLW1SgcdSpd%2F0zVQjOKl8mmlLi2C6BBNUNYfjeSDDobb%2F19DhQF9SNAmMljiFEdJzBVF9JQ99ACkLRYtkn75MNcx%2Feft7Kz3Qj8pSbNNVH9a3rtd3cNzLYLD4L%2BeQyl89M5%2B3Q2Yzn9JqTjfOKaKg4H97dAct%2Bl7VB9BMYu4mik7lR1c7S3yvE7j62R%2B7SboqFsQIGHG683atm%2BFpG6aisfC2nI4ra9fmP57eE7uvD5Fh9HO0kIrqWhU9bpp5e1Yoi%2BNrbB26DhZtH5awJX95Ux3iJ8ns2xZmoE5Ep%2F%2B1VQHt8UX45GX6gaecRIv2J546%2F3ICSftBNvGAarBBqIVz%2FdE5p51tKY5kfJn0HwStOicM3JhEeRqzjO%2FGyaecRjDB5D9TWaw06Kj%2FN%2BlJs5aVIUZS99dv%2BWCfEsxX2ke5zovKLCdLARFrrAVJWkFGmsm9gYV%2BY5%2FJUHHst6%2BgiOc%2F%2BqbnX4gkid7Ew5vEVztZbFzDLkEiDuze7q1TqChF8HldkOlo6vpwx1kuWz6osLfw2MTcIGt47suYxIwQ6%2FZBvqTMFIctfe2P3HaAUnNLrS9d240yh8AN1PPwmcgEwhhX%2B7Kl2z6u252pTDrx1nMO%2Bl98kGOqUBHu1KJUH7BuVjhsZuQBDJVspC%2FctLZFGTCu3v4sm%2F%2BpSN%2BRcGCSqJgTw9nFmHd2pbSxBkfa63GB5%2FH%2B1PbaaVxjnZZk7ZtwMcDA1r7HpWAUjwhTaGXT%2B1tmr3CNZsfJkVq45kD%2BidHpAyg2eIIzOQ8qo4lGkenyZoqIKOORRb5aAGaThcvNccwGOfNY3B4XMx6JNOMnH1rmzjcQw8l6iJ9UsqcbHo&X-Amz-Signature=cd58ec826308e7b148ef37e8f1e66e6fea1d4220a61f7a9ab22e9b4c18449aaa&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
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
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/f5eaf646-d1bf-463b-a48d-2f1ddda1b071/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TNS7AOF5%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T220916Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIH13wccKhBtlQLiLXgicAO6whFDErth4OZ1La8V4S36%2BAiEAzxjEVuERxKrBU08uCSaziQu6nUydwhzRgumjwBJ90BIq%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDL5S6yUkRRKvM5VWeSrcAzIWncRgd3OWmcsqAyDWtLFNRgfleTOMp7qqWtr1gChHCkSZlXlyPZIqOK2hflAo6hqQvQcK5VVDyDFX45r9ZTunk9UR3JLiicR7XJtvi%2FhLO5Pt3TQMCsmH0zsmYpdzsBBhfVpwrgKZxUujQGC%2BeMs%2Blxa0npi3jTICmF5aGWqeHYzAT%2B4PNHlapCoHZ1%2BXXOuyU8vJt1A9wrKrYisiaIr4SXEyATp2U8bWFFbD8EoNHY3eZYHGHl2IDM8tvXUZpIg6DmqW33HLLTygSx15sKPDR1bRUEe8rdTlyzzT8odSpKUKs%2B2B5bH2LIXRNRrtOSJ6Iyk7RdB4ZpKS3gWdph3rlD%2FlsKsCagWhTgbxfsfeKF4nTP3iBSA9N522JNYfZRVGJEpL1CFpGKuiH6emDtdpQtjjIi%2BwvV8z1L05AqN2Uwd5Djsa%2BCdGpvCZjlF2Z87BvhCeCxYc%2FefknmAM2Udup3w7A5Z8APTDwZwYK%2BMRKZF7YgNW8YP%2Bwbi8PfYO%2FP7zCPGRuxSlXaVjvcigeIuzQvfo50KzpsOSd0g%2BBpGqfsVVRXCMcULg5RBzWc7%2FvtEb4LNzqb9UrmpDjrBwiMY39JWppucC%2B7gnU74pSyTeA4LGymUOcjOASX%2B9MPOl98kGOqUBck5fuBxK13tmEzvz%2BvJxRauFelodfwoY6yNvFKma87QnVBIhsDmB2iosnGlkcrLh7vjYdYIlE%2FuoYn5WkO7L3qxe6H1pr%2Blind5Ho%2BBIa3YZl6%2FBcrhhzDu8c3djF7PM61yeq1Xo2diyL5xt%2BWeo2CQ4oU1EhVrfC%2Bi%2FMns3tFznIzX7hWWtBMXnT1V9UA3x465oo%2FiazYlmWZ%2BwSWQxJ19aWT%2BX&X-Amz-Signature=09324b73983476887a9b39367eaaf50afa98f5f1fd9c5b4ba98ed952cfbac6aa&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
---
**Rename columns**
We can see that we have now all the information inside a DataFrame. However, the name of the second column looks quite ugly, so let’s rename it.
```python
teams_players_df.columns = ['Team', 'Players in team']
teams_players_df.iloc[:10]
```
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/8881d1f9-9c56-43d5-9f7e-a79ae7fb4c3c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TNS7AOF5%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T220916Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIH13wccKhBtlQLiLXgicAO6whFDErth4OZ1La8V4S36%2BAiEAzxjEVuERxKrBU08uCSaziQu6nUydwhzRgumjwBJ90BIq%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDL5S6yUkRRKvM5VWeSrcAzIWncRgd3OWmcsqAyDWtLFNRgfleTOMp7qqWtr1gChHCkSZlXlyPZIqOK2hflAo6hqQvQcK5VVDyDFX45r9ZTunk9UR3JLiicR7XJtvi%2FhLO5Pt3TQMCsmH0zsmYpdzsBBhfVpwrgKZxUujQGC%2BeMs%2Blxa0npi3jTICmF5aGWqeHYzAT%2B4PNHlapCoHZ1%2BXXOuyU8vJt1A9wrKrYisiaIr4SXEyATp2U8bWFFbD8EoNHY3eZYHGHl2IDM8tvXUZpIg6DmqW33HLLTygSx15sKPDR1bRUEe8rdTlyzzT8odSpKUKs%2B2B5bH2LIXRNRrtOSJ6Iyk7RdB4ZpKS3gWdph3rlD%2FlsKsCagWhTgbxfsfeKF4nTP3iBSA9N522JNYfZRVGJEpL1CFpGKuiH6emDtdpQtjjIi%2BwvV8z1L05AqN2Uwd5Djsa%2BCdGpvCZjlF2Z87BvhCeCxYc%2FefknmAM2Udup3w7A5Z8APTDwZwYK%2BMRKZF7YgNW8YP%2Bwbi8PfYO%2FP7zCPGRuxSlXaVjvcigeIuzQvfo50KzpsOSd0g%2BBpGqfsVVRXCMcULg5RBzWc7%2FvtEb4LNzqb9UrmpDjrBwiMY39JWppucC%2B7gnU74pSyTeA4LGymUOcjOASX%2B9MPOl98kGOqUBck5fuBxK13tmEzvz%2BvJxRauFelodfwoY6yNvFKma87QnVBIhsDmB2iosnGlkcrLh7vjYdYIlE%2FuoYn5WkO7L3qxe6H1pr%2Blind5Ho%2BBIa3YZl6%2FBcrhhzDu8c3djF7PM61yeq1Xo2diyL5xt%2BWeo2CQ4oU1EhVrfC%2Bi%2FMns3tFznIzX7hWWtBMXnT1V9UA3x465oo%2FiazYlmWZ%2BwSWQxJ19aWT%2BX&X-Amz-Signature=13a08e74a97a81b22e41927aa692050a93df32f09e933eb3b6c405ee6e0bcebf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
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
![goals_assists_df](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/3d4c5199-1890-4496-8ce1-bd0754874750/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TNS7AOF5%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T220916Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIH13wccKhBtlQLiLXgicAO6whFDErth4OZ1La8V4S36%2BAiEAzxjEVuERxKrBU08uCSaziQu6nUydwhzRgumjwBJ90BIq%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDL5S6yUkRRKvM5VWeSrcAzIWncRgd3OWmcsqAyDWtLFNRgfleTOMp7qqWtr1gChHCkSZlXlyPZIqOK2hflAo6hqQvQcK5VVDyDFX45r9ZTunk9UR3JLiicR7XJtvi%2FhLO5Pt3TQMCsmH0zsmYpdzsBBhfVpwrgKZxUujQGC%2BeMs%2Blxa0npi3jTICmF5aGWqeHYzAT%2B4PNHlapCoHZ1%2BXXOuyU8vJt1A9wrKrYisiaIr4SXEyATp2U8bWFFbD8EoNHY3eZYHGHl2IDM8tvXUZpIg6DmqW33HLLTygSx15sKPDR1bRUEe8rdTlyzzT8odSpKUKs%2B2B5bH2LIXRNRrtOSJ6Iyk7RdB4ZpKS3gWdph3rlD%2FlsKsCagWhTgbxfsfeKF4nTP3iBSA9N522JNYfZRVGJEpL1CFpGKuiH6emDtdpQtjjIi%2BwvV8z1L05AqN2Uwd5Djsa%2BCdGpvCZjlF2Z87BvhCeCxYc%2FefknmAM2Udup3w7A5Z8APTDwZwYK%2BMRKZF7YgNW8YP%2Bwbi8PfYO%2FP7zCPGRuxSlXaVjvcigeIuzQvfo50KzpsOSd0g%2BBpGqfsVVRXCMcULg5RBzWc7%2FvtEb4LNzqb9UrmpDjrBwiMY39JWppucC%2B7gnU74pSyTeA4LGymUOcjOASX%2B9MPOl98kGOqUBck5fuBxK13tmEzvz%2BvJxRauFelodfwoY6yNvFKma87QnVBIhsDmB2iosnGlkcrLh7vjYdYIlE%2FuoYn5WkO7L3qxe6H1pr%2Blind5Ho%2BBIa3YZl6%2FBcrhhzDu8c3djF7PM61yeq1Xo2diyL5xt%2BWeo2CQ4oU1EhVrfC%2Bi%2FMns3tFznIzX7hWWtBMXnT1V9UA3x465oo%2FiazYlmWZ%2BwSWQxJ19aWT%2BX&X-Amz-Signature=776f89bcd33e179ed105c3775dba2dd22704664c64df3f1c79068fd0398582d9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
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
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/17ab1dcf-24fc-485d-b844-14c2bd68e3ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UNTNNWSH%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T220917Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIFdzOToSEyQ1YE5PqG%2BLxYMPUBAcKyosj0CxdfzopJD0AiEA5bx9bVtHJE8trenGB6QKBnnS3TTdpBhUw%2BGcak7KJ6Aq%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDNRSmqauGuHpYz24QyrcAxWf7VSBY0GoS0XV3NQX4wXpW921h5rQg9L%2B2RFUnoF5gN55PisOIsFhOxfd%2BGPF4jVB%2BCe3Hep3%2FD4EnCzxW%2B1b4DM9nga00kD6J4mnCQlArJrlG6lJ2avGvzL7dQbJh9utmk7H%2BagV9y9TjQeN4L2mdK%2BfkI5cx1cYCA2muR%2FMMtwdPrY%2BGIEOaIUmSQcCM9VauZeSyOtHwoYZQCBVTufQ4oZWmNk41g8U0iZ66g8XLZmH%2BoUHoTdqA9q9eksHk51mArdHIZ1q%2FeoxOac8PQJVpZW2M1cY34sXrpUT0GAjJWOGsTCs564YrvYCE%2B1ZRIC26R4E4KsI7b93DDOUnxb9VerQei6GUonFvnb6%2BTXRTTYEL4U1zpCU8vHHNctA1U8NoE%2BKBA10zccsvL6cntHaCtryC%2B3ApNjAMbsRp%2F8qYqrMWJ%2F0FaxUBzTIFJUD8QQ40%2FDJ2RQUH2K4dVtwaqAJbuGxySOpznUI%2BftI07iuhUaOyvrqz56eVjPq1IblxQt2FG9i31k1F19HkXpGAbhGH2XWgQFgbp3HIObQ6E4BMqv80s4td28nXnQYtWUoTcLcOtyE3X69cqXRaZr%2B%2BaaIKcRL0vqdQk4ijbww9oXj7SxM7ZT%2B7dB1KdC8MLym98kGOqUBH8zw9kejc%2Bmgzp%2FvhCOx%2BzRXnauBwVXTBD6wwMTqj4XdVZ5FTWxLYehM9ekSK6KZ%2FH63aH7Ww2b2y7WsA2mjc%2Biq2ErVvjM%2FP4FfpykQanashVFI%2Fne9FmfWLIlTbp4%2FyqE19hMxnQDWxNMe8vmHehcVsWdPz4AbWK%2FJ0obprxSdXlwZHx1S8i7UMUuOcbkonJRg5UyxNFbiT4m3H4K6xSFkbiet&X-Amz-Signature=34ef28a893e9a0640cbd4e30847d598b9df2944869b69a16575b1cd71fd13016&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
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
![agg_data](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/8b40cc7f-98b7-42de-bb85-b931a1290e6d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QVZFJHJB%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T220917Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJGMEQCIE3PIKa5zQomadquUyAJFZZ26qG7%2FPaUWzdHNtZmF5gcAiAp1y5%2Fxvoj%2FB55UtGBm1dZk5pMbp4IRyG5WD26YRid2Cr%2FAwgmEAAaDDYzNzQyMzE4MzgwNSIM%2FpBUeyhohaED5%2BBcKtwDEnDf%2Bi3Be5KiYv52DCEr9%2FgwXBa8SEo16COO1xjI8YyFnuT2Gu0WR5E4GlIeIyu8k4M9qXxYBwOoif%2Br72Ss0lppl4A0JoHfTCPohyyZKADb0Q5gyeV%2BhezcwM9wPfJV76R5WrlNzlfyHDzqSjj3h0GApW%2Bpl4jNtKG9ZKCr%2FLz4P2rDEeqqcrDr5g0P%2BUevLLd%2BZIfNk9aznCSGUpsdJ53ur5RYWNjiFgiGFyCzWogYTkXW3NZRoECFh0bhUbm96zUaEhsAmN3AMr3aGTFPQOVe65PBkeiiAqLsm96JICOteyzap8p5OEryHon%2F0X6mpK0YyyPzmAHdXKkmHBBCdQapSmsNGqm0uxzsCXwJcC2KJDmO4ZcpXNVdkvwTMA9aEWlg%2FtvfEEIEzAawOFHzEwmiJzbPQKs4XhoSBn7UBvq7Txj%2B8rpJzXNGv%2B2dGlqqXpsSXUxCrQtODzaLa%2FwYsMJsjtaUqOcXG%2BmBhqRzYzOqcQ7malpMvjUfH%2BPWvGmaFysA7aLaZvE52WtMG%2FkcC5wE4586GSo8XX2ZGQKvI4ydSFPJlYdNqvCkk%2BzAbjAoRqcOLViF19BADBltJ9A1fqy592aq2rLeGwZ2wpY9ah2B8RDLhNzWnFgcv0Qw1KX3yQY6pgEFHsXkogef7CYFPVI3Y8c1t3qqIn%2F0JSK%2FPJOIVXDmbsCordKcXEUCIKPdSXy4NVbhdh0oRINMJtXlXf8P%2FplGIfLqIaaS%2FMXIL%2BIojAnzogvraQK4vgdraAR4WXLRgP8ypfOjmyra1WpMRLAr7ogKJdqiW0gU9FsgoF6NJfD9wmJJVCl89NSA6HgR8pQN10B9pzngaaPYqLTE8%2FwqlIiskYC2ETtg&X-Amz-Signature=bc18c178ed6b11d252bf49a01fe6ee7af137a69f5a5ae37726bc1ac31f468e82&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
We can see that we have now an overview about `Goals`, `Assists` and `Total points` per team.
---
But we still don’t know within a few seconds which team was the most productive one in terms of total points. So let’s sort the aggregated DataFrame based on column `Total points`. 
```python
agg_data.sort_values('Total points', ascending=False)
```
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/e035d01e-ef72-4e95-8a61-58b2b61d4aa7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QVZFJHJB%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T220917Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJGMEQCIE3PIKa5zQomadquUyAJFZZ26qG7%2FPaUWzdHNtZmF5gcAiAp1y5%2Fxvoj%2FB55UtGBm1dZk5pMbp4IRyG5WD26YRid2Cr%2FAwgmEAAaDDYzNzQyMzE4MzgwNSIM%2FpBUeyhohaED5%2BBcKtwDEnDf%2Bi3Be5KiYv52DCEr9%2FgwXBa8SEo16COO1xjI8YyFnuT2Gu0WR5E4GlIeIyu8k4M9qXxYBwOoif%2Br72Ss0lppl4A0JoHfTCPohyyZKADb0Q5gyeV%2BhezcwM9wPfJV76R5WrlNzlfyHDzqSjj3h0GApW%2Bpl4jNtKG9ZKCr%2FLz4P2rDEeqqcrDr5g0P%2BUevLLd%2BZIfNk9aznCSGUpsdJ53ur5RYWNjiFgiGFyCzWogYTkXW3NZRoECFh0bhUbm96zUaEhsAmN3AMr3aGTFPQOVe65PBkeiiAqLsm96JICOteyzap8p5OEryHon%2F0X6mpK0YyyPzmAHdXKkmHBBCdQapSmsNGqm0uxzsCXwJcC2KJDmO4ZcpXNVdkvwTMA9aEWlg%2FtvfEEIEzAawOFHzEwmiJzbPQKs4XhoSBn7UBvq7Txj%2B8rpJzXNGv%2B2dGlqqXpsSXUxCrQtODzaLa%2FwYsMJsjtaUqOcXG%2BmBhqRzYzOqcQ7malpMvjUfH%2BPWvGmaFysA7aLaZvE52WtMG%2FkcC5wE4586GSo8XX2ZGQKvI4ydSFPJlYdNqvCkk%2BzAbjAoRqcOLViF19BADBltJ9A1fqy592aq2rLeGwZ2wpY9ah2B8RDLhNzWnFgcv0Qw1KX3yQY6pgEFHsXkogef7CYFPVI3Y8c1t3qqIn%2F0JSK%2FPJOIVXDmbsCordKcXEUCIKPdSXy4NVbhdh0oRINMJtXlXf8P%2FplGIfLqIaaS%2FMXIL%2BIojAnzogvraQK4vgdraAR4WXLRgP8ypfOjmyra1WpMRLAr7ogKJdqiW0gU9FsgoF6NJfD9wmJJVCl89NSA6HgR8pQN10B9pzngaaPYqLTE8%2FwqlIiskYC2ETtg&X-Amz-Signature=8e94fa9f6e24760333760201d4be8a6422275190a801cd75faea1cfe6b2ce4af&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
We see now that Manchester City was the most productive team with 169 points.
---
## [`.merge()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.merge.html)
---
**Syntax**
With this function we can merge two DataFrames together into a single one. If you are familiar with SQL, `.merge()` is Panda’s equivalent to SQL Joins.
`pd.merge(<< Left DataFrame >>, << Right DataFrame >>, << mode >>, << left key-column >>, << right key-column >>)`
For the `<< mode >>` parameter we have four different options / types of merge we can do:
`'inner'`
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/5408a8e0-787f-4825-a1d7-569d613696af/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YGQ265N4%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T220921Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIAunT%2BcAfdmlOvVhrGR82pOXXj41oL132JiFxDHucE0eAiEA94fJVGrWAZEeCtEzgu4HOTr9XM8VirWEirB5Ao%2BogBwq%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDFaGReb7Qq9lSInAVSrcA6O6SGxL9RyggJJDK9hCwJ0EjT8TUzMI%2BytN8TQHEKFKubvv2fYJYeKkIT71BDbJr1hh0r2KQbfF8n%2F0nVAyLXKP7%2BEVn%2BV%2FiIbVA6W3zji5FzqG107SvGGrqf3z%2Fpqoxsf83q%2BLi3c%2F%2B4JGDcOfSfFGurO57Pd1mfcaSQGrInwQpen59riQpEhM97%2BERTZkS1Gj%2F%2FLR%2FVDmPVqVeAeEcXR6MhalXZDEQ4%2BTmk%2FtaLN0QnkzQZyd%2F%2BcXv0aznwpLmKt5YGy1FFokpHg48K1Silq9WxmHQEQhu1%2FtKsjH3lO06%2FoN%2FFXOBu1GeF7yTOiPoSN%2BIxdJ1w49NjWqi2lUBUNJvy%2FVwN%2BIf8BjQX1%2FibPwt1Xt7VEqtL2hqe89eBxXlRvEv0WhTUv4tl1fZfeXnBNxVsUoFieQn3FLXPtXmJJxhD%2FSyWz8UhSQwyphv9IxMVn01hmbAtBQSPC4PsrAPXjbUs0xeyHNDPYKtrKBQJxUX4cradt5Zjs35iD6eCusIgtr7vvgaLSNHIKlTL8eXUgDMcupVlUXmOall9YT9hBNv16P5CHEfZWSFLvga3v2Bvlm2I4Dcqv7vPSCEdUvVgbiu1OGHgywvLl6C1tj5ig8azOq19%2BwyihPF0g4MJKm98kGOqUBaaCwKL4x0puf4RbdhHh75yWbCPPk7Ofq%2F84VjbFwYbd%2BJBl%2Bt1v966TGLHcAV%2BQFwetX2quNY6%2FC%2BgRcxAZwYPvmvQjgRINOPf68iN4aRaBlqdA3X1CvbTny%2FGtUfdX%2B8T%2ByEUnyqzHSHXv2Q3sw5fkjaED8abBrnHLmRAxZcg4HFVBRqMCaruoEyfWWggSYHprbMptFAFTh2Dj9wOsd8xIPnS3U&X-Amz-Signature=f16084b2de73dc13bdf2234ef91cd65082a6731142a00fcad092dc98c8f328ac&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
`'left'`
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/09e2253a-b6d9-411d-836b-faa79515429b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZVPLJ24U%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T220921Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIBlmP5slSnDHrTsyK8TF1l51PEq%2FetFslpZgBGcYxK%2FyAiEAq6UT59MoTiXvT3Y0p%2BGX42klxfNhJCAS9%2Fq%2BQdiWILoq%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDJZl7d7cj9YFMfxCFCrcA0jg0%2BOZjJXuNytQntsite8rRbBDMnlIlkfkk8E9ON%2BsworG8AdU0PBdJuZPesVKdZj9bDE7RXepmOXBlEGV0XYUtIpsDFSgfysrMxW%2F9oYmCYlxLBoOTnyhVGPtyY4TUh6Orn1OlrhUt%2B1VhqltNCnPH8d2Dytt8EJ5gEFWoRvPn0Ku%2BcbSQWkJ8rRfRFjn46MtomimFu1b4zjlw08QPEB8Gs80FpS49yGSjjwwpYOcYF8vakD65fdaCwKDZYJ%2BbZY%2BhKB3Cu4asjUQ0oMQ%2F9qravcnfxq3wONYIFV4r27HfPNCJ9gTI8OKQuaI2dhs2SN3ATi6%2Fsi5U7GJbXZE28OpbIssTvWEQsUb7hOq1T6VZXYnWa8hcsN7il2viiI6r9mC1DLNrexiMm35S7NzM912%2FsMmXliulLrk%2FDeTuex8XYJzEcAzrs0GDpG21IO1T1H31ppA9spnihfEFsRl2O23m0AqtITPSjdrzJcY54l1JpuU%2Bq85vcnZPhxQ%2BDYjs0nUc3du3Mw3OOG2sOoaqIis%2Fcfildlh1fk9tE9hh1ftYNUr3ubaD55pQGpgvQ0gUU2k3HzAvV%2BwOZKfw8nkBoqbuGNALKu71RWRwM9ThHu6MGLSu4l2r%2BokuZh1MKum98kGOqUBFetc4M%2BTd0cRloD4LL7KvINOlIKW9bhAubc9Q2sGaqXxbQtC%2BbJqgmZdJzT8%2BWZMWhjLGhdgK1LgQBQWp6Bb0FmTO8yF7%2Fujk3VmTeAT84lGZvoLoIbuJlCiHNnnR3USXYBnscu9PX7i5cunwUYLQqS8M%2F2i6OC9Vm3Vo5PG3LernkdEO9avtPXOYRc8ckXLy83R7lFK0EpXSUXCxQGCkDFTS5TV&X-Amz-Signature=0010dc985e071444a4ad7e59708c30435e1f68f066a5523f36db882d0f91c6e2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
`'right'`
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/15e33ac0-53d8-4e72-867c-7d17c8d7a3e2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XTUB54UH%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T220922Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJIMEYCIQCWoPNdO6Gb0SIjVEKpxsQN7ea8N8%2FjVEBSH9QFiKvJPwIhAIBjw2G5gOWIDqgigiZ9m6TJvx2EMj29a4erRWJskfufKv8DCCYQABoMNjM3NDIzMTgzODA1IgyRDLr5UTEtOGjZ2qwq3AOmMZPYig2HmDBHGT%2B6mR3ZL%2B%2Fvh6LTSuuDloJSJSi3zFHtk2sO4wXM%2FVXXIoEUfWQ%2B4ow7hkaFhJBZnIV5Ggii3NwceebmXG%2FL5eJPIHnDZpasfYKZ%2Bb9du%2F0nOt7Gnb589QsDRqfN%2BGUE2vYvJU3w4yX9zOZNyVT6js17zLPvDk6uQIHf4tHQ6uMu%2FyPs0doGiIaLDBBy1h7AL4oGgjuiIZK%2F0vUzGFUHF4oL0xIf4jn%2BP71LBMk5R66i9x6jhS02P7x2FGhEW9etdrU4GsVzGAlYMDO%2FJTsFJ%2FOyO1V2xaxRDUoy6cYU75HaaSBnU3Tu6T35vF8GB%2F8DB1eQ%2FKYg%2BtXdtgwJAHDCwJrNr5xGrTw%2FoF6lT2AFxpPjdclmYx04WWqgUqgZo9a3nsnyv2rnWxqrtXIRIuvZ7Z7Q3J2U0Dvq9vBlJSJBKXI%2FVKHLrtBqwuaKZ9Aod7B5KLE5y%2FNC9vTWRK6geFWQfGJvjQmKRimpbjoKy0Ny3k6cvLE37%2BYx5YsYrY3dCqFoipFUozpwdq8y4FDX6zmIoqcxIptRdyEZrDagtW3GbXh9H4Y1dviIAsBDaThWPsrX5%2BLSbnDk63TLXmHERq%2F05d0%2F0p2e644jZmMHSRttFlp3uTDDpffJBjqkAaiioZFzS97U66o7FD5dpv2Zdt6PsBDkOjEZbbEhFssF7A2SiPlCehpr5H2nc6lc2K3veE%2FkN2Hx809cswpAzPlAxzJEr19WAbEuCFtLCz1SMRfUyET3lNAMFT1zOACZ8Uth9Ktfz4qYqUb5b60b4jFrxYfbf5Ft0LLBf0l3TXmKuKnEPP7cO8fBAbL8i%2BLpCDrelMYu7z79E%2BeEPKansoEkGq0S&X-Amz-Signature=cdc0e02cb5f970d1f78facc6b300bd8eefb765b761b54bc2dc5ed41c57fa9fb6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
`'outer'`
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/806d7472-621f-489c-b76f-7cfde93b8afc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466STAZDOYB%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T220924Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIQCrsPT0USP4DUsztktozi40U4AyhfN8EVgy8mrdRwO6IAIgV5eLjzjCOvDt73Mt1JlVawHu8GFpNptrcZK0gD6glNgq%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDL4HtprNIpHkxdcoBCrcA73S36s4Th4fu6C1X7x6lzmIN5AZyovBrDuw5vDNeANUEOAErxS11t%2FOCiiv6k3J8VvM%2B2TQcK%2BrZGag7aifGinLCY5RGaBtNgo9Pt%2BNPw4apRHJYm2HXbRNB8M4qaf7xwtbJWXOb8pqo7ezSbHSPaUdq5ZUMUD4OzVaVvdEEWCy2qL6pXAfy%2FBhNES5qc5mdd4lkPU0dxivLNJ7UEwUdH4vA29pybnm3WSpIjB8cjEX5M0oxEDOy%2BXhRoBTnmLcxawyJuTNE8cWio1UgCJE7oO7SSX0XguFF7cblQXCYtPM%2BDxOZ7%2Bg90UblurnQkMxaG92kshAnVt16RX8PmVTDX40BAwJDpZZqAfdvH7wQAONCQztiqRfQfMex79lHq2tdwH%2BNRyud1xQTJek7PKcKxhHl%2FfSLUKXsoa%2B5hmtUEz3lZUccut658h7rSHyPoY2sfLDPCzqiTTKipNa0AgUbqi%2FuSyVxBFwgFffP4MRMphaYuEdB4Q7A5l1VOXRmJNeCW3uiHWUuuJc1y1b9gCrqPBCXa1L64p1f0k%2BugFlKZslYJhrP8e2yacw72vsTGdc1097qU24y%2F1LAy%2FlAI%2BjjoSV%2Fa7LsVOj0Aq%2FifVb%2B22gryPVwzAlOT7De6u6MJKm98kGOqUB7cC9T43aAzez2hYA%2FU%2BQVOKceO8k5%2BOgVWCalyxbbPWD8N90xYv318JBcMbGd1BexkQlJdiBMotEewwFyLX0yUJOImaxsdhkKLqb9OoYcouFM4meQKPw9Y7Z9WXTRDTsFvCI5o1C4FpgpA34LPSS0%2F6gwUuH3RbgmTXakhlrAFxQpGHWG9IagQHCNcrInpG%2BCzxWrcKSExx1rh1x3dEe%2F%2BZvVIzh&X-Amz-Signature=5a52697fb5b1be104f7139b2ede9e640772a18a48751964743bf5e0e5116bb32&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
We will cover each of the four merge types in examples below.
---
**Simple merge**
Let’s assume we have two DataFrames:
`teams_players_df`
Tells us how many players each team has whose total points are higher than the median value.
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/717dc77f-d8a4-4bcc-8e02-f6ad22ea7515/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RV3SLQAC%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T220925Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJIMEYCIQDW%2B2BZx4IMbwrX0MHj5xEcCXa1FtdUGlxzh9z%2BC6I%2BPQIhAIxNYDQ4YBZvNoIPiGrhWjfZJ9aR053%2F%2BaQlcCXYAEVqKv8DCCYQABoMNjM3NDIzMTgzODA1Igy9hb2vXGyP%2BUcf1K8q3AMKvCPPSeK5FUNcryGyGNndIBo0RDZ5ABgaqVJsHLx2mPrjaKHz66fEN4wCv7lT1Sv%2FPe1rFlbSWffwavtJzxJ%2FK6j2xNvP5vG6euFHKNZvxNyG1cP6N%2FzGhnh73cP6KqZLjF2Yrdj%2FL2hMmRvBOXTzIcd0wHcplQge3zTk7ORxSqpdlXE4oWviA4rX2dIYyenlc69QDMVH61%2FsUWopmo0Pz2vIbmW5WSVTYmxQlwDw3rogJZX6OWGI%2BaqOXbYlBG1yN7avIK8hX4hVCsBmUNjLBmKALimRctAdEEnGr5WLzi%2FOoerqeECS6yuYKZLGTNc7nUIHluqkHMaBj9ou8xdtZa3LBgeN16hAkjMXq8rTzWHO1d7KjBAqsPpQ2iJBnPwhA%2BtzLwqLBjDpmAT9RQNqHoJft%2FCthWDa70kYTw%2BNGM0v73DRgCYepHXLWkUI7%2BhsGsVN0SE7e5lXxcR5%2Bh3yqIfklTC0s%2B3CMM%2BxT%2Bh9AuxQuFx7euH%2FcfYQCa1J8WvGW1cpNMoyxv69FR0rHir5gV%2FKHDncpZs%2FP583t9wXLcfvq1IfQKz%2Fktf6S%2BujEh59ghyEnwMlNkRvuej2fcfkJ3NB5ooS3DedlT64zz6uT2Y5zUnkUG8qufjrDDCJpvfJBjqkAVvjG%2Bz4H6Kiv08zIykyTv%2BsiFHVKOoDrkZlfumm8dH4slVP%2F2T1T5d6woco5Qjf%2Bupa1K6ycq%2B9218wBGqG7hD5oVcEP4T3T3ks6ddd8Q1JsfWIJes6ndbyHEYSG2X6KoTnxYleKHOHiAiV89zYw1YDZ37VSsYaDpRhimHsX5uHZBQRoOKcOeuXvoz88diPne2Cajv3%2BkjH0wQzG4C7gPNY%2BT9q&X-Amz-Signature=cf47a37370bd566480d38b710b4e0840c1d6729a41b27f83b5732f953210f76b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
`teams_goals_df`
Tells us how many goals each team scored in total
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/8aeb3499-93e4-4e75-93bd-8cfbfb15ef89/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W4LRGDCH%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T220925Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIDvetM2iRUzSh3cxQehADTa95XAynTnUqCtQ1xm8uFrKAiEAkPIHK2vqu90VDjWJBwrF9Ms4omyitJtc03JAcfOowjAq%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDIQlGuXY5iPHzLTTQircAy6qylKNWzJx3DWz6ilz%2F34HtQdVEDRJhFGy%2FRs0Rh%2B9KA%2BeEMbGyR0BcHPGdrzuonSLRjU2Ia5zEgQ%2B3pEbUoZQOkFVaPU448s8pHgomRq%2FC%2Bzk24i3HvUfvxLDvt4DiQYkbYX6rxA9tzXg4TjhqKV9A8W0hj%2BcLNLEoFjV6TiBzZN2Mt2yfSVrZeJ2OMVIN5q%2FTK5oeIh1U4Xd%2BWzdL%2F31jwiv1dQYhmWF7idvTrIdRM9lqOxGvCt1rxU5F0XdNDQF%2FNoScq3KzCOHENmgBz%2FVZJw3M4cnVWiaCtWWLqLcODaggWr36CXLP%2BAGCVRKUzt2IePhNYIrLsMkKoX7DpzpjJ7oZhTXiZLuiIYNfLAC7fRNZQvxftLQImG2ArgqslASneCODI514uDB8GuT7T95x4u7DkrFcikHgNREuCxWF25ieKJlechvPLukvWtqc4yCYXEtwpx8cmCoTTkX11sb%2FinJSBCiIRMafPyPQQ8mmNdVF%2B8k1Ab8vjVmGfZORs2f64JAOcAwYtvvfvKeVtq%2B8x%2BEaHK%2F5kriWt1vjjzIjBsDVCT6LP2TkLv6e2fbevOT0NYoY5lEUkW%2BVDVIWG4UJ3mIHUlU3TIl1GbuWy%2FqklJe9n%2FXWPKFRYYSMOql98kGOqUBCPnZRPixzLDI1Mcn8I6459ORA02Kf5meg%2B2ixaw4f6M4xtFCFXgiv32gQG25oA0I6TST%2Bv06IPtwxxT8ki7RMsOrnKjIbJO4Rsz9rnY%2F2xVmPIfukDBF8GHDpGl8vEhOVW%2BMIfVsHJ4nOtdrYrPbOkHpaZloDMMqo8x3s3p743nflZu5Dx1KM2a4QfmbJ975GeoxBTXNSlZ1VEasAObjZ0ldvNIL&X-Amz-Signature=420c732f6c3f27a17087d0c04adfa5919059c430ea6ef7c980591a07d423aced&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
Now our goal is to merge these two DataFrames together into one single DataFrame. To do so, we must check if they have a something in common. We see that both DataFrames have a column `Team`, a so-called **key-column**. 
Thus, Python can use this key-column to connect the DataFrames together. Because if we want to get rid of the `teams_goals_df` DataFrame, Python must know where it should put the values in column `Total team goals` and Python does that by mapping the values in the key-columns.
We can now execute the merge command as follow:
```python
team_stats_df = pd.merge(teams_players_df, teams_goals_df, 'inner', left_index = True, right_index = True)
```
We got a new DataFrame called `team_stats_df`. As you can see the two DataFrames are now combined.
![team_stats_df](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/f966153d-f56f-4c61-a446-0ab9b688a507/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RFTB4NO4%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T220919Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIQC5rafry1dGPKiE90t363UTzlsm556US0Kf4uQEsMX1GwIgcNo5dx5GqbOL4dlw%2BE3EnKRFTJeW9mgrj7%2BQmB7GdL8q%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDNujcdxXC0A1CmmyXyrcA1iLAZ1kWQWiaAC7kN%2FRG2%2FQNaLAuGF2Hu9Suml3WZQLuvNVaeQKp0AppPJi8SXMxAQnQRLPR3sqiV8HDVhpwZ9SGtPflj9ASxaShJgt7oHsLSCoSAp8%2FnPDlTqm47OLfoveQ%2FjJdLrZyNro3HFi52LONuM4CuqmNKSWas12EwknP25WLNh6ts0VjMRMKYZdK4f22HnuYA1eUxWbxE1f9cmkthW2%2FVLZFmkpyAI2wzmArgUPm8zlBlQw4WQaXWQir1zt0RRgNBd9Azk6lvEVQ9%2B7kTMCJeSCneZ4M0vkeDbog4xWr6z9sNzcCSAcHbY2fO%2BsFXR82y%2FJpzS4i6Z5s5nXMEtePSwUxez99kD6onolO%2B7jJXrsrz6UZEri5FiO4cCnqkCioOO3rK3Ae%2FI6u%2FAnqsrww44tPasvizZy%2BiFZUZNIHqlfscR14%2FUpch%2Bfo%2F%2BuZaH6sXE4fHnIoWOxT4kIPpoNfSNEDJHZpDYzmlCQBwvNScrNRVSfnGwqKOX5tkBW8jLkcS46204za2oJTAE4ANEYsUtUAOidqg4HYz4lW1luDDUGDR6aHdrQF0WTefpUAs6eCDZXWlX700hCDR8M5e9kvleJC3f1zwvM82fbrTQtBbzCT19Hi%2FRcML2m98kGOqUBlJfTGSajykZMSIr7SHqfmispwKONh5CztJsmvOeNZ0HgprXTxfl8iCY2lAnN1gxGxU3qDq6hwt4u592Pa1aYkHb7QObFF297alBfKNyaj99Gp%2B6YfVNRBh%2FFQKGLvKCecy4PJA1oRTFSC4LgUXq2qfZbHXk4P4nvJVJ%2F7raONzX3TAD1WFyr2pJNqS8VvnohF47P%2F4xb1nMhqMcTlBBD84hi1rcQ&X-Amz-Signature=f5d775fe2a78d112ae932d98bb0e06b57fa795ea5e8f14246c1943846ed60626&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
As each value in column `Team` is found in both DataFrames, `teams_players_df` and `teams_goals_df`, i.e., both DataFrames contain exactly the same football teams, it does not matter whether we do an `inner`, `outer`, `left` or `right` merge. 
More precisely, we can also do an `outer` merge and get the same result. 
```python
team_stats_df = pd.merge(teams_players_df, teams_goals_df, 'outer', left_on = 'Team', right_on = 'Team')
```
![team_stats_df](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/f966153d-f56f-4c61-a446-0ab9b688a507/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RFTB4NO4%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T220919Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIQC5rafry1dGPKiE90t363UTzlsm556US0Kf4uQEsMX1GwIgcNo5dx5GqbOL4dlw%2BE3EnKRFTJeW9mgrj7%2BQmB7GdL8q%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDNujcdxXC0A1CmmyXyrcA1iLAZ1kWQWiaAC7kN%2FRG2%2FQNaLAuGF2Hu9Suml3WZQLuvNVaeQKp0AppPJi8SXMxAQnQRLPR3sqiV8HDVhpwZ9SGtPflj9ASxaShJgt7oHsLSCoSAp8%2FnPDlTqm47OLfoveQ%2FjJdLrZyNro3HFi52LONuM4CuqmNKSWas12EwknP25WLNh6ts0VjMRMKYZdK4f22HnuYA1eUxWbxE1f9cmkthW2%2FVLZFmkpyAI2wzmArgUPm8zlBlQw4WQaXWQir1zt0RRgNBd9Azk6lvEVQ9%2B7kTMCJeSCneZ4M0vkeDbog4xWr6z9sNzcCSAcHbY2fO%2BsFXR82y%2FJpzS4i6Z5s5nXMEtePSwUxez99kD6onolO%2B7jJXrsrz6UZEri5FiO4cCnqkCioOO3rK3Ae%2FI6u%2FAnqsrww44tPasvizZy%2BiFZUZNIHqlfscR14%2FUpch%2Bfo%2F%2BuZaH6sXE4fHnIoWOxT4kIPpoNfSNEDJHZpDYzmlCQBwvNScrNRVSfnGwqKOX5tkBW8jLkcS46204za2oJTAE4ANEYsUtUAOidqg4HYz4lW1luDDUGDR6aHdrQF0WTefpUAs6eCDZXWlX700hCDR8M5e9kvleJC3f1zwvM82fbrTQtBbzCT19Hi%2FRcML2m98kGOqUBlJfTGSajykZMSIr7SHqfmispwKONh5CztJsmvOeNZ0HgprXTxfl8iCY2lAnN1gxGxU3qDq6hwt4u592Pa1aYkHb7QObFF297alBfKNyaj99Gp%2B6YfVNRBh%2FFQKGLvKCecy4PJA1oRTFSC4LgUXq2qfZbHXk4P4nvJVJ%2F7raONzX3TAD1WFyr2pJNqS8VvnohF47P%2F4xb1nMhqMcTlBBD84hi1rcQ&X-Amz-Signature=f5d775fe2a78d112ae932d98bb0e06b57fa795ea5e8f14246c1943846ed60626&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
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
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/fa07d056-415f-49e7-84b0-94cfa9734610/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WIYEAQUD%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T220927Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIQDlnhn92%2BEixzNl0GCOPiN%2FImA2FxxJ70Cyq%2F16S1XsSgIgf8GBVHZ176JBS6hJF7r0EMLWNSvo0JDr%2F8v1CjdP8LEq%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDCHrZdd6327BzvueZCrcA5Dtd0ZE9Lma4%2BpOc1Cl7XWOy0EkyrS7JoeQdnmIdy1IbD%2B3w3r66SqNawvPALrNLI5scmBHybDseiB5grgJtuQnax8Alh4Ey2XP3DJhAzmqT6BSzMe7cBXT9bjRFX6mBzYO7MqmzyYnQ65cKeWiR%2FNRaEmqA0j94g8JKwdnOd0lcLARYhEwM%2F7BPEb%2FgChAV3b9bwUtmyTGsYNpLImOPFojap%2BUbvL8KVU5cZ4j0pFnUtmAm%2Fy7M5MYnHWfGw3dUChA2CSGmVNkbIQHgLclolEiT7VCfr7CghtRGIXQnPUPBRi2ceo7PlYvCgs9%2BWGw4uuD%2Bbi2N5Z0otzHf5JRReoY%2FDPRktLQruLueSkmx8c6S6lUV0KSwZK%2FgztSbuQFsAUC%2BTAWRUNnn4himJUio2Fzl2aFuscqMZITBZ47IurEqIzz2SK3HsQ95HXmV5rlSX5ZCzGcK%2Fo7hfq9v55fbY5eULgUyyRpnVA0jiS8ScIsog%2B%2BakFDFMpmn167O093vbM7EqPVHvFYwAlnH8gwqFnuh132NeaduSO40e3dwzPPz%2BWbBN9nC4LMwAso9u3XJOwb1vCp4GoZSpNETlTU8CgWooLL8kBskDheGCkwwehx6%2F2bkH97gthUcOimMJ%2Bm98kGOqUB%2B8BvGrsGH6RJIGMMdVr4%2Bs5iUD3RMJ41QePhxVqLqUAvkIjwv5dlxcYVgR6NP6AV7nyKSMAYtp5L9V9Me8R9AWoveiBG1YrmuUvooo1MRpPxzEbMIgHqasdDFi%2B9KW2uwySoyw1m9c5utXzzbs8%2BJj02rYTmo14vVuzhBC0U1tEKdgCeNP5wpJvzR6lmhAcst3rYPeRvKIgL1vPwNpBTkllxBSRL&X-Amz-Signature=e014dc28f2140c919fd76e9abd32becd683349a3abf07523eb9eeaa91b342cd2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

`teams_goals_df`
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/c92e9e38-25a7-447f-acc3-6d29a922c350/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466444N32HP%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T220927Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJGMEQCIGer1tHF5u70xaYsjfOAFxQgRLiAM%2BM05WfYQ1OhzS7CAiAPCT07NwSHuDid5E2GJHGB6pQOr3YWiwEU4Zc1xgeMNir%2FAwgmEAAaDDYzNzQyMzE4MzgwNSIMPYK3lKfe%2BWw%2BfMUcKtwDz2DkyPiVuzdf4LH4b%2FDgVmIbkPKmWzOR3ioOxCPyxe8t0%2BAmZ039%2BUhZD9Zq42C832BK4LMal%2FNp2KY%2BNSFb3IuTsGuLgHnpE2KJe7n%2FD0NYGEYNiYRSfe6vUqBTSb7fXFC4zm7Mfv7NFidjdZlGpxw6kj56BFnQqAMG7zysTWPacNaqlIZaZVczFGMIdcuPQbi6tkzzuAxdSMRJRsi12LDv0PFFgxu1L%2Fo%2FJSRSHN5E%2F4nXAuQ%2BmfJ3FeMPF0fTJL0WkZImJ5aBCmUIDJ%2FvQP3Ebev5hTTJ6ALIRFBxZwagYk29dWkhV7%2FjWBbILTPzcArDu96lwIcR%2F%2B3W4MSDxa3QuU3b3WYxHQTYGGff2QC9YNnEttRgSG%2BjzeQPlBqRJLOG7zPZBMt38f9EPpR8WFP9%2FFrAnzuMwFZ9RXN4Z%2Bjxwu4eeOukxaIYjdXW7tlFoTP7ufndH4LkKqyxMtMiIh1eIzcRyYRS9UvROCD6j8d5mw2TswRDyc54u7WZ6%2F6y8jMQKAL6a%2BMe7SGsgTBdnHXGQwvDP70pz1bUxKP9wNm15Rfmxp2qS5O6ZRr5TTh1jTXx7pUkcu6gtnfzcMhwMHCBKnd9v9zysSaNLhlpqnXyPtqrUSrmrHZqlWgw3aX3yQY6pgFNaTP%2FtOjiywGu4mC16e5o%2B7eQQSP8MeoUfFe%2B1Vw0CfgtsMxBBrIc1P2xRtdRudhKCPvoxl3QFukXs9AIjkC0dzHd4h%2F8EzSwSHB%2Bux9kO2GiqoymCrcWLZeapVXAfJdfodyyDAGmZ24FnbQ%2FwhU1G90i8n1WrLA%2FWvrw%2BZoqvy%2B9qYje7kolQ2K0%2BBGLs0TT9YWLWqkegu6x9tAxXSFaYeNSWikH&X-Amz-Signature=10ee8a25cda2b34076094c793018f0f44dc4aa4803d6d4f8e0fa010be6b7d83f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
Now if we want to merge the two DataFrames together we can simply specify the `left_index=` and `right_index=` parameters and tell Python that the indexes should be use as key-columns and we get the same output as before.
```python
team_stats_df = pd.merge(teams_players_df, teams_goals_df, 'inner', left_index = True, right_index = True)
```
![teams_stats_df](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/f966153d-f56f-4c61-a446-0ab9b688a507/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RFTB4NO4%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T220919Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIQC5rafry1dGPKiE90t363UTzlsm556US0Kf4uQEsMX1GwIgcNo5dx5GqbOL4dlw%2BE3EnKRFTJeW9mgrj7%2BQmB7GdL8q%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDNujcdxXC0A1CmmyXyrcA1iLAZ1kWQWiaAC7kN%2FRG2%2FQNaLAuGF2Hu9Suml3WZQLuvNVaeQKp0AppPJi8SXMxAQnQRLPR3sqiV8HDVhpwZ9SGtPflj9ASxaShJgt7oHsLSCoSAp8%2FnPDlTqm47OLfoveQ%2FjJdLrZyNro3HFi52LONuM4CuqmNKSWas12EwknP25WLNh6ts0VjMRMKYZdK4f22HnuYA1eUxWbxE1f9cmkthW2%2FVLZFmkpyAI2wzmArgUPm8zlBlQw4WQaXWQir1zt0RRgNBd9Azk6lvEVQ9%2B7kTMCJeSCneZ4M0vkeDbog4xWr6z9sNzcCSAcHbY2fO%2BsFXR82y%2FJpzS4i6Z5s5nXMEtePSwUxez99kD6onolO%2B7jJXrsrz6UZEri5FiO4cCnqkCioOO3rK3Ae%2FI6u%2FAnqsrww44tPasvizZy%2BiFZUZNIHqlfscR14%2FUpch%2Bfo%2F%2BuZaH6sXE4fHnIoWOxT4kIPpoNfSNEDJHZpDYzmlCQBwvNScrNRVSfnGwqKOX5tkBW8jLkcS46204za2oJTAE4ANEYsUtUAOidqg4HYz4lW1luDDUGDR6aHdrQF0WTefpUAs6eCDZXWlX700hCDR8M5e9kvleJC3f1zwvM82fbrTQtBbzCT19Hi%2FRcML2m98kGOqUBlJfTGSajykZMSIr7SHqfmispwKONh5CztJsmvOeNZ0HgprXTxfl8iCY2lAnN1gxGxU3qDq6hwt4u592Pa1aYkHb7QObFF297alBfKNyaj99Gp%2B6YfVNRBh%2FFQKGLvKCecy4PJA1oRTFSC4LgUXq2qfZbHXk4P4nvJVJ%2F7raONzX3TAD1WFyr2pJNqS8VvnohF47P%2F4xb1nMhqMcTlBBD84hi1rcQ&X-Amz-Signature=f5d775fe2a78d112ae932d98bb0e06b57fa795ea5e8f14246c1943846ed60626&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
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
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/c7d7e7df-3a32-451a-98bf-c558a0dd3f4e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WJG5JD3B%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T220929Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIC%2BzEjezTv9R63l3chLxuhlQdB9qQEyXM3WDO2rXO734AiEAn8cACt7pg%2Blt5UvCoseXwkykBGMuHAiN7NNK5nB3IjYq%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDNjsqyRONKIcpXFYaSrcA5brVm8NsFExTo%2FqUoKW6TxWgZTr82FNK2VsdFPuLEmYfTTeTMBQt35b5ky1BusV3OuZQdQai5UrIARp80dN6z0ds%2Fzh4t56U29iggDf8CE87flE4563l0%2BMfYjcPcB7fz%2Bf8Jvvas0tjhKyhGPwntibI%2BSKTDmOcgxjGwlInTUhaBhlj%2FsYztAafXod4l8kFv6XzAjcxYVu4gRMf49wLvEGwVV9HDbUm9j%2FBs7bNWGFo3qx5RR9T62E5iAKCNPcHKD3gajG61dU29vV5MHTyUpiQO5OEa7Z8LdpgAqrsA35qls5gK7zkdFOpYUGSAQhmLO2Hg4xzQp187V6YedMYzjIfdAQSxV0rIQe31AC3wpC9NPOaiNszq477Y8aV4oe6QeJPuavETmDW6gDCHfmbKuMH4J3YYxsH%2F7a%2B1ezqV6IxuOPsToSdhL1G0zimKw4XduRTwcT5%2FL79sWIpfohTTIzSvdT0kkhFtIFyOI2jrSvFeMX8oGy%2FfkEkVD5c%2FlAzDAQtb8EcTb8DjsTZ4NrFqPdpBeYIZSkdkobMbl7wpYVj716GkLw%2BpLNxlJnO5YjfS4%2F%2BOq6XxghMvl8fuIGmLzyRJvyPRWLgl4JfPApjTtPVudRB55kzIvp7spuMMal98kGOqUBDSbg7NbIqdIYSNL0vcTpTbvsGCfiBhcwIVrNijvw1B4a7uDtFmtB3ElPY44XwJ6USXijkAvOlauwyr6CiTKLGJdb6uVpxkueVr7%2FyhHhC4K4EGo8rDmDOEftf%2FPSidrn4JyPUUWcJ%2BdDRAV0CWvFg5I3uUYyVK2EZGy0RZdhsfHiUz41fgZyfW4N2YISgJXq8g3oe3dDfK7DCoDF6H8Pb4sZUSN7&X-Amz-Signature=e9df092827bffb548561273f13a326a9c4e2652d866bad12b5d255c0dbe724ed&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
`teams_goals_new`
Chelsea and Burnley are missing
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/4a460f8b-2082-49cc-a749-a2543eec972c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667RFNKY7Y%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T220929Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJIMEYCIQC24%2FMexGFzWbcf8w2cP1iTSBpOAMGZ0CcbW5sMIbSoCAIhAOrFr7MOiUUtytFw4%2FUxgXmhBbXSZwZr%2FPp8y4%2BtlhPnKv8DCCYQABoMNjM3NDIzMTgzODA1IgyFyaqrafQ0Euv%2BNroq3AOZZWdGU20TRIxx0lVAMvzXC31ZwQ9dapr8GunfJV1Tphc%2FsntAoAjE43CrdhxVzyk2tazsEu6sCDO6EZOBOOktJ3yFuoPGImHALKxwYioSMUXTPC4u77QNXUvZKGivPxJ0ZSgoEAYqrNIOXqKt7uVDHg8n%2BkjyYHSHgYgjHLo5tWjZFzLw%2B2%2FIYXpZt9bhSPJjpVxaXJY%2FVHZB0IUUEMJRYbTbOMjeO5mmeT1EZY92kfQqu6mrpdrDaCdWFCLV7FLbTZfqFJeuVDEeVULnuLFebe2%2F%2F%2Bee5cMCEF4JGx8Ec5Wjqp77Q65wsk5TtieUK25yBCEdKI89YQqo4ThVrb8mN6PfQTYeIlBcOE8xpzoQ0Qw790dvbU085VPeEsyAYgS92GNkzX8uNHaSvqV3Oh7J8qeziHFIgM0N%2BTLiLABhep2GH5Hn9ntHAQJgg23o%2Bkn7UFx%2BLR81SuQYnlXhwVzoNtGOLUATmrBPVARRwxDf3UfO%2FHlWxnioUKjnlWgOdJAVVQw1nWonD98ul2XPqwu7kzMyFZwq1XawOjDd678z3IBvmLENYdPUz1CyJLhTrHCKekAeoNmKZ1BI7xm2H8UpZZ6n0N11uXde1ZR78wq94fSXLSIY5oyoQYkxwTDdpvfJBjqkAZsVPTYnuojNJK7bPCxlst9Xk2V7cuTCrJrpN7QXGCfCpCcQw0qoE3tezAtfQHk%2BTRasMDvokfRzIRfSrVaqbRv%2BLkPOhsY1sxIM%2FrWGlNwt3Kho5zFzO%2FtLYj8mBV15ll8nCF5lEG3Nmgs%2FkP37NWoGs3NEozy5HNCA4H9SFnlSA4%2BhtiCK6BCGxo8t3nMNpJpqixMvwK9%2FYc1af%2FaWGiq3i0J9&X-Amz-Signature=cacc4adf9db6ea8a8e3d846f6ceb38c07f77ff70d3683dea5df562c94f2def3f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
---
**Inner merge**
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/5408a8e0-787f-4825-a1d7-569d613696af/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RFTB4NO4%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T220919Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIQC5rafry1dGPKiE90t363UTzlsm556US0Kf4uQEsMX1GwIgcNo5dx5GqbOL4dlw%2BE3EnKRFTJeW9mgrj7%2BQmB7GdL8q%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDNujcdxXC0A1CmmyXyrcA1iLAZ1kWQWiaAC7kN%2FRG2%2FQNaLAuGF2Hu9Suml3WZQLuvNVaeQKp0AppPJi8SXMxAQnQRLPR3sqiV8HDVhpwZ9SGtPflj9ASxaShJgt7oHsLSCoSAp8%2FnPDlTqm47OLfoveQ%2FjJdLrZyNro3HFi52LONuM4CuqmNKSWas12EwknP25WLNh6ts0VjMRMKYZdK4f22HnuYA1eUxWbxE1f9cmkthW2%2FVLZFmkpyAI2wzmArgUPm8zlBlQw4WQaXWQir1zt0RRgNBd9Azk6lvEVQ9%2B7kTMCJeSCneZ4M0vkeDbog4xWr6z9sNzcCSAcHbY2fO%2BsFXR82y%2FJpzS4i6Z5s5nXMEtePSwUxez99kD6onolO%2B7jJXrsrz6UZEri5FiO4cCnqkCioOO3rK3Ae%2FI6u%2FAnqsrww44tPasvizZy%2BiFZUZNIHqlfscR14%2FUpch%2Bfo%2F%2BuZaH6sXE4fHnIoWOxT4kIPpoNfSNEDJHZpDYzmlCQBwvNScrNRVSfnGwqKOX5tkBW8jLkcS46204za2oJTAE4ANEYsUtUAOidqg4HYz4lW1luDDUGDR6aHdrQF0WTefpUAs6eCDZXWlX700hCDR8M5e9kvleJC3f1zwvM82fbrTQtBbzCT19Hi%2FRcML2m98kGOqUBlJfTGSajykZMSIr7SHqfmispwKONh5CztJsmvOeNZ0HgprXTxfl8iCY2lAnN1gxGxU3qDq6hwt4u592Pa1aYkHb7QObFF297alBfKNyaj99Gp%2B6YfVNRBh%2FFQKGLvKCecy4PJA1oRTFSC4LgUXq2qfZbHXk4P4nvJVJ%2F7raONzX3TAD1WFyr2pJNqS8VvnohF47P%2F4xb1nMhqMcTlBBD84hi1rcQ&X-Amz-Signature=faafb37699ff833626ed799d376882bf60ba48cd92d93c0a111787805c26a37b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
As we now have some difference in our DataFrames we can analyse how the four different merging modes work and we start with the inner merge.
```python
inner_merge_df = pd.merge(teams_players_new, teams_goals_new, 'inner', left_on = 'Team', right_on = 'Team')
```
![inner_merge_df](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/79a226fa-2761-47e7-b051-752ec50a0f14/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RFTB4NO4%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T220919Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIQC5rafry1dGPKiE90t363UTzlsm556US0Kf4uQEsMX1GwIgcNo5dx5GqbOL4dlw%2BE3EnKRFTJeW9mgrj7%2BQmB7GdL8q%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDNujcdxXC0A1CmmyXyrcA1iLAZ1kWQWiaAC7kN%2FRG2%2FQNaLAuGF2Hu9Suml3WZQLuvNVaeQKp0AppPJi8SXMxAQnQRLPR3sqiV8HDVhpwZ9SGtPflj9ASxaShJgt7oHsLSCoSAp8%2FnPDlTqm47OLfoveQ%2FjJdLrZyNro3HFi52LONuM4CuqmNKSWas12EwknP25WLNh6ts0VjMRMKYZdK4f22HnuYA1eUxWbxE1f9cmkthW2%2FVLZFmkpyAI2wzmArgUPm8zlBlQw4WQaXWQir1zt0RRgNBd9Azk6lvEVQ9%2B7kTMCJeSCneZ4M0vkeDbog4xWr6z9sNzcCSAcHbY2fO%2BsFXR82y%2FJpzS4i6Z5s5nXMEtePSwUxez99kD6onolO%2B7jJXrsrz6UZEri5FiO4cCnqkCioOO3rK3Ae%2FI6u%2FAnqsrww44tPasvizZy%2BiFZUZNIHqlfscR14%2FUpch%2Bfo%2F%2BuZaH6sXE4fHnIoWOxT4kIPpoNfSNEDJHZpDYzmlCQBwvNScrNRVSfnGwqKOX5tkBW8jLkcS46204za2oJTAE4ANEYsUtUAOidqg4HYz4lW1luDDUGDR6aHdrQF0WTefpUAs6eCDZXWlX700hCDR8M5e9kvleJC3f1zwvM82fbrTQtBbzCT19Hi%2FRcML2m98kGOqUBlJfTGSajykZMSIr7SHqfmispwKONh5CztJsmvOeNZ0HgprXTxfl8iCY2lAnN1gxGxU3qDq6hwt4u592Pa1aYkHb7QObFF297alBfKNyaj99Gp%2B6YfVNRBh%2FFQKGLvKCecy4PJA1oRTFSC4LgUXq2qfZbHXk4P4nvJVJ%2F7raONzX3TAD1WFyr2pJNqS8VvnohF47P%2F4xb1nMhqMcTlBBD84hi1rcQ&X-Amz-Signature=5ef57e3225249648870c3392ea54ebe105bb34e4479710efc8db182e968ba81a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
We can now see that the `inner_merge_df` only has 16 rows but the source DataFrames, `teams_goals_new` and `teams_players_new` both have 20 rows.
Why is that? Well with the inner merge we only include those rows in the output that are present in both DataFrames. As we do the merge using column `Team` as key-column we must look at this column which leads us to the following observation:
The values Arsenal and Manchester are present in the key-column (`Team`) of the right DataFrame (`teams_goals_new`) but not in the left DataFrame (`teams_players_df`)
→ these two rows are not included in the output.
The values Chelsea and Burnley are present in the key-column (`Team`) of the left DataFrame (`teams_players_new`) but not in the right DataFrame (`teams_goals_new`)
→ these two rows are not included in the output.
> 💡 **Inner merge only includes overlapping values in the output. If a value is present in one but not the other DataFrame, its entire row is excluded.**
---
**Left merge**
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/09e2253a-b6d9-411d-836b-faa79515429b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RFTB4NO4%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T220919Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIQC5rafry1dGPKiE90t363UTzlsm556US0Kf4uQEsMX1GwIgcNo5dx5GqbOL4dlw%2BE3EnKRFTJeW9mgrj7%2BQmB7GdL8q%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDNujcdxXC0A1CmmyXyrcA1iLAZ1kWQWiaAC7kN%2FRG2%2FQNaLAuGF2Hu9Suml3WZQLuvNVaeQKp0AppPJi8SXMxAQnQRLPR3sqiV8HDVhpwZ9SGtPflj9ASxaShJgt7oHsLSCoSAp8%2FnPDlTqm47OLfoveQ%2FjJdLrZyNro3HFi52LONuM4CuqmNKSWas12EwknP25WLNh6ts0VjMRMKYZdK4f22HnuYA1eUxWbxE1f9cmkthW2%2FVLZFmkpyAI2wzmArgUPm8zlBlQw4WQaXWQir1zt0RRgNBd9Azk6lvEVQ9%2B7kTMCJeSCneZ4M0vkeDbog4xWr6z9sNzcCSAcHbY2fO%2BsFXR82y%2FJpzS4i6Z5s5nXMEtePSwUxez99kD6onolO%2B7jJXrsrz6UZEri5FiO4cCnqkCioOO3rK3Ae%2FI6u%2FAnqsrww44tPasvizZy%2BiFZUZNIHqlfscR14%2FUpch%2Bfo%2F%2BuZaH6sXE4fHnIoWOxT4kIPpoNfSNEDJHZpDYzmlCQBwvNScrNRVSfnGwqKOX5tkBW8jLkcS46204za2oJTAE4ANEYsUtUAOidqg4HYz4lW1luDDUGDR6aHdrQF0WTefpUAs6eCDZXWlX700hCDR8M5e9kvleJC3f1zwvM82fbrTQtBbzCT19Hi%2FRcML2m98kGOqUBlJfTGSajykZMSIr7SHqfmispwKONh5CztJsmvOeNZ0HgprXTxfl8iCY2lAnN1gxGxU3qDq6hwt4u592Pa1aYkHb7QObFF297alBfKNyaj99Gp%2B6YfVNRBh%2FFQKGLvKCecy4PJA1oRTFSC4LgUXq2qfZbHXk4P4nvJVJ%2F7raONzX3TAD1WFyr2pJNqS8VvnohF47P%2F4xb1nMhqMcTlBBD84hi1rcQ&X-Amz-Signature=6d0c1640131cf1e1a85ec695460156ff1462faf7ebcd408f6ba6adcdd6403341&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
While the inner merge includes the overlapping rows only, the left merge includes all rows from the left DataFrame plus the values from the right DataFrame for the overlapping rows. 
```python
left_merge_df = pd.merge(teams_goals_new, teams_players_new, 'left', left_on = 'Team', right_on = 'Team')
```
![left_merge_df](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/fc5638ad-e2c6-491c-81ca-3d9dee8fa8a2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RFTB4NO4%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T220919Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIQC5rafry1dGPKiE90t363UTzlsm556US0Kf4uQEsMX1GwIgcNo5dx5GqbOL4dlw%2BE3EnKRFTJeW9mgrj7%2BQmB7GdL8q%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDNujcdxXC0A1CmmyXyrcA1iLAZ1kWQWiaAC7kN%2FRG2%2FQNaLAuGF2Hu9Suml3WZQLuvNVaeQKp0AppPJi8SXMxAQnQRLPR3sqiV8HDVhpwZ9SGtPflj9ASxaShJgt7oHsLSCoSAp8%2FnPDlTqm47OLfoveQ%2FjJdLrZyNro3HFi52LONuM4CuqmNKSWas12EwknP25WLNh6ts0VjMRMKYZdK4f22HnuYA1eUxWbxE1f9cmkthW2%2FVLZFmkpyAI2wzmArgUPm8zlBlQw4WQaXWQir1zt0RRgNBd9Azk6lvEVQ9%2B7kTMCJeSCneZ4M0vkeDbog4xWr6z9sNzcCSAcHbY2fO%2BsFXR82y%2FJpzS4i6Z5s5nXMEtePSwUxez99kD6onolO%2B7jJXrsrz6UZEri5FiO4cCnqkCioOO3rK3Ae%2FI6u%2FAnqsrww44tPasvizZy%2BiFZUZNIHqlfscR14%2FUpch%2Bfo%2F%2BuZaH6sXE4fHnIoWOxT4kIPpoNfSNEDJHZpDYzmlCQBwvNScrNRVSfnGwqKOX5tkBW8jLkcS46204za2oJTAE4ANEYsUtUAOidqg4HYz4lW1luDDUGDR6aHdrQF0WTefpUAs6eCDZXWlX700hCDR8M5e9kvleJC3f1zwvM82fbrTQtBbzCT19Hi%2FRcML2m98kGOqUBlJfTGSajykZMSIr7SHqfmispwKONh5CztJsmvOeNZ0HgprXTxfl8iCY2lAnN1gxGxU3qDq6hwt4u592Pa1aYkHb7QObFF297alBfKNyaj99Gp%2B6YfVNRBh%2FFQKGLvKCecy4PJA1oRTFSC4LgUXq2qfZbHXk4P4nvJVJ%2F7raONzX3TAD1WFyr2pJNqS8VvnohF47P%2F4xb1nMhqMcTlBBD84hi1rcQ&X-Amz-Signature=ec73c29164e585cf4c00a7993801bffb4bcf06cac6f9f4b5ccb620a71b5bc4a3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
We can now see that the `left_merge_df` has 18 rows in total and two `NaN` values.
Why 18 rows? We know already that the teams Arsenal and Manchester City are in the right DataFrame (`teams_players_new`) but not in the left one (`teams_goals_new`). As we do a left merge all rows from the left DataFrame are included regardless if the team is in the right DataFrame too (or not). This is why the teams Arsenal and Manchester City are not included in the output but the teams Chelsea and Burnley are still there.
Why are there two `NaN` values? Well, the teams Chelsea and Burnley are not in the right DataFrame, thus we don’t have the information how many goals these two teams scored. Therefore, Python just fills this missing data cells with `NaN` values.
> 💡 **Left merge includes all rows from the left DataFrame plus all overlapping rows and where values are missing, `NaN` is inserted.**
---
**Right merge**
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/15e33ac0-53d8-4e72-867c-7d17c8d7a3e2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RFTB4NO4%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T220919Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIQC5rafry1dGPKiE90t363UTzlsm556US0Kf4uQEsMX1GwIgcNo5dx5GqbOL4dlw%2BE3EnKRFTJeW9mgrj7%2BQmB7GdL8q%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDNujcdxXC0A1CmmyXyrcA1iLAZ1kWQWiaAC7kN%2FRG2%2FQNaLAuGF2Hu9Suml3WZQLuvNVaeQKp0AppPJi8SXMxAQnQRLPR3sqiV8HDVhpwZ9SGtPflj9ASxaShJgt7oHsLSCoSAp8%2FnPDlTqm47OLfoveQ%2FjJdLrZyNro3HFi52LONuM4CuqmNKSWas12EwknP25WLNh6ts0VjMRMKYZdK4f22HnuYA1eUxWbxE1f9cmkthW2%2FVLZFmkpyAI2wzmArgUPm8zlBlQw4WQaXWQir1zt0RRgNBd9Azk6lvEVQ9%2B7kTMCJeSCneZ4M0vkeDbog4xWr6z9sNzcCSAcHbY2fO%2BsFXR82y%2FJpzS4i6Z5s5nXMEtePSwUxez99kD6onolO%2B7jJXrsrz6UZEri5FiO4cCnqkCioOO3rK3Ae%2FI6u%2FAnqsrww44tPasvizZy%2BiFZUZNIHqlfscR14%2FUpch%2Bfo%2F%2BuZaH6sXE4fHnIoWOxT4kIPpoNfSNEDJHZpDYzmlCQBwvNScrNRVSfnGwqKOX5tkBW8jLkcS46204za2oJTAE4ANEYsUtUAOidqg4HYz4lW1luDDUGDR6aHdrQF0WTefpUAs6eCDZXWlX700hCDR8M5e9kvleJC3f1zwvM82fbrTQtBbzCT19Hi%2FRcML2m98kGOqUBlJfTGSajykZMSIr7SHqfmispwKONh5CztJsmvOeNZ0HgprXTxfl8iCY2lAnN1gxGxU3qDq6hwt4u592Pa1aYkHb7QObFF297alBfKNyaj99Gp%2B6YfVNRBh%2FFQKGLvKCecy4PJA1oRTFSC4LgUXq2qfZbHXk4P4nvJVJ%2F7raONzX3TAD1WFyr2pJNqS8VvnohF47P%2F4xb1nMhqMcTlBBD84hi1rcQ&X-Amz-Signature=273645447a6edd4921d3668cbeae7cc8d78743d311156aeb3f1ed440897a34bb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
The right merge is the pendant to the left merge. With the only difference that the right merge includes all rows from the right DataFrame plus the values from the left DataFrame for the overlapping rows.
```python
right_merge_df = pd.merge(teams_goals_new, teams_players_new, 'right', left_on = 'Team', right_on = 'Team')
```
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/039bd199-4137-4018-b9d7-2221c16121dd/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RFTB4NO4%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T220919Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIQC5rafry1dGPKiE90t363UTzlsm556US0Kf4uQEsMX1GwIgcNo5dx5GqbOL4dlw%2BE3EnKRFTJeW9mgrj7%2BQmB7GdL8q%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDNujcdxXC0A1CmmyXyrcA1iLAZ1kWQWiaAC7kN%2FRG2%2FQNaLAuGF2Hu9Suml3WZQLuvNVaeQKp0AppPJi8SXMxAQnQRLPR3sqiV8HDVhpwZ9SGtPflj9ASxaShJgt7oHsLSCoSAp8%2FnPDlTqm47OLfoveQ%2FjJdLrZyNro3HFi52LONuM4CuqmNKSWas12EwknP25WLNh6ts0VjMRMKYZdK4f22HnuYA1eUxWbxE1f9cmkthW2%2FVLZFmkpyAI2wzmArgUPm8zlBlQw4WQaXWQir1zt0RRgNBd9Azk6lvEVQ9%2B7kTMCJeSCneZ4M0vkeDbog4xWr6z9sNzcCSAcHbY2fO%2BsFXR82y%2FJpzS4i6Z5s5nXMEtePSwUxez99kD6onolO%2B7jJXrsrz6UZEri5FiO4cCnqkCioOO3rK3Ae%2FI6u%2FAnqsrww44tPasvizZy%2BiFZUZNIHqlfscR14%2FUpch%2Bfo%2F%2BuZaH6sXE4fHnIoWOxT4kIPpoNfSNEDJHZpDYzmlCQBwvNScrNRVSfnGwqKOX5tkBW8jLkcS46204za2oJTAE4ANEYsUtUAOidqg4HYz4lW1luDDUGDR6aHdrQF0WTefpUAs6eCDZXWlX700hCDR8M5e9kvleJC3f1zwvM82fbrTQtBbzCT19Hi%2FRcML2m98kGOqUBlJfTGSajykZMSIr7SHqfmispwKONh5CztJsmvOeNZ0HgprXTxfl8iCY2lAnN1gxGxU3qDq6hwt4u592Pa1aYkHb7QObFF297alBfKNyaj99Gp%2B6YfVNRBh%2FFQKGLvKCecy4PJA1oRTFSC4LgUXq2qfZbHXk4P4nvJVJ%2F7raONzX3TAD1WFyr2pJNqS8VvnohF47P%2F4xb1nMhqMcTlBBD84hi1rcQ&X-Amz-Signature=ad8e788457489c36a118c764b68401fdd7d87480a6a5df12f348c87eb27c363a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
Again you can see that there are 18 rows in total. This time the teams Chelsea and Burnley are left out as they are only present in the left DataFrame (`teams_goals_df`) but not in the right DataFrame (`teams_players_df`).
Also, for those teams that are in the right but not in the left DataFrame, Manchester City and Arsenal, `NaN` is inserted as we don’t have information available about the number of players they have.
> 💡 **Right merge includes all rows from the right DataFrame plus all overlapping rows and where values are missing, `NaN` is inserted.**
---
**Outer merge**
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/806d7472-621f-489c-b76f-7cfde93b8afc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RFTB4NO4%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T220919Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIQC5rafry1dGPKiE90t363UTzlsm556US0Kf4uQEsMX1GwIgcNo5dx5GqbOL4dlw%2BE3EnKRFTJeW9mgrj7%2BQmB7GdL8q%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDNujcdxXC0A1CmmyXyrcA1iLAZ1kWQWiaAC7kN%2FRG2%2FQNaLAuGF2Hu9Suml3WZQLuvNVaeQKp0AppPJi8SXMxAQnQRLPR3sqiV8HDVhpwZ9SGtPflj9ASxaShJgt7oHsLSCoSAp8%2FnPDlTqm47OLfoveQ%2FjJdLrZyNro3HFi52LONuM4CuqmNKSWas12EwknP25WLNh6ts0VjMRMKYZdK4f22HnuYA1eUxWbxE1f9cmkthW2%2FVLZFmkpyAI2wzmArgUPm8zlBlQw4WQaXWQir1zt0RRgNBd9Azk6lvEVQ9%2B7kTMCJeSCneZ4M0vkeDbog4xWr6z9sNzcCSAcHbY2fO%2BsFXR82y%2FJpzS4i6Z5s5nXMEtePSwUxez99kD6onolO%2B7jJXrsrz6UZEri5FiO4cCnqkCioOO3rK3Ae%2FI6u%2FAnqsrww44tPasvizZy%2BiFZUZNIHqlfscR14%2FUpch%2Bfo%2F%2BuZaH6sXE4fHnIoWOxT4kIPpoNfSNEDJHZpDYzmlCQBwvNScrNRVSfnGwqKOX5tkBW8jLkcS46204za2oJTAE4ANEYsUtUAOidqg4HYz4lW1luDDUGDR6aHdrQF0WTefpUAs6eCDZXWlX700hCDR8M5e9kvleJC3f1zwvM82fbrTQtBbzCT19Hi%2FRcML2m98kGOqUBlJfTGSajykZMSIr7SHqfmispwKONh5CztJsmvOeNZ0HgprXTxfl8iCY2lAnN1gxGxU3qDq6hwt4u592Pa1aYkHb7QObFF297alBfKNyaj99Gp%2B6YfVNRBh%2FFQKGLvKCecy4PJA1oRTFSC4LgUXq2qfZbHXk4P4nvJVJ%2F7raONzX3TAD1WFyr2pJNqS8VvnohF47P%2F4xb1nMhqMcTlBBD84hi1rcQ&X-Amz-Signature=218396514fd0dc4e40552270add275af02e2f4f0d0a5f5b8d0ec8d7fb85db596&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
The outer merge is the combination of the left and right merge. This means that the outer merge includes all rows from both DataFrames and thus no rows are left out in the output.
```python
outer_merge_df = pd.merge(teams_goals_new, teams_players_new, 'outer', left_on = 'Team', right_on = 'Team')
```
![outer_merge_df](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/2431d095-7483-492f-b1ec-5fe0a2250ea9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RFTB4NO4%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T220919Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIQC5rafry1dGPKiE90t363UTzlsm556US0Kf4uQEsMX1GwIgcNo5dx5GqbOL4dlw%2BE3EnKRFTJeW9mgrj7%2BQmB7GdL8q%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDNujcdxXC0A1CmmyXyrcA1iLAZ1kWQWiaAC7kN%2FRG2%2FQNaLAuGF2Hu9Suml3WZQLuvNVaeQKp0AppPJi8SXMxAQnQRLPR3sqiV8HDVhpwZ9SGtPflj9ASxaShJgt7oHsLSCoSAp8%2FnPDlTqm47OLfoveQ%2FjJdLrZyNro3HFi52LONuM4CuqmNKSWas12EwknP25WLNh6ts0VjMRMKYZdK4f22HnuYA1eUxWbxE1f9cmkthW2%2FVLZFmkpyAI2wzmArgUPm8zlBlQw4WQaXWQir1zt0RRgNBd9Azk6lvEVQ9%2B7kTMCJeSCneZ4M0vkeDbog4xWr6z9sNzcCSAcHbY2fO%2BsFXR82y%2FJpzS4i6Z5s5nXMEtePSwUxez99kD6onolO%2B7jJXrsrz6UZEri5FiO4cCnqkCioOO3rK3Ae%2FI6u%2FAnqsrww44tPasvizZy%2BiFZUZNIHqlfscR14%2FUpch%2Bfo%2F%2BuZaH6sXE4fHnIoWOxT4kIPpoNfSNEDJHZpDYzmlCQBwvNScrNRVSfnGwqKOX5tkBW8jLkcS46204za2oJTAE4ANEYsUtUAOidqg4HYz4lW1luDDUGDR6aHdrQF0WTefpUAs6eCDZXWlX700hCDR8M5e9kvleJC3f1zwvM82fbrTQtBbzCT19Hi%2FRcML2m98kGOqUBlJfTGSajykZMSIr7SHqfmispwKONh5CztJsmvOeNZ0HgprXTxfl8iCY2lAnN1gxGxU3qDq6hwt4u592Pa1aYkHb7QObFF297alBfKNyaj99Gp%2B6YfVNRBh%2FFQKGLvKCecy4PJA1oRTFSC4LgUXq2qfZbHXk4P4nvJVJ%2F7raONzX3TAD1WFyr2pJNqS8VvnohF47P%2F4xb1nMhqMcTlBBD84hi1rcQ&X-Amz-Signature=e5fabc396e02c267d560b30b941b44360b107be5d439ff3ba39addb01bcf0aa1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
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
![Joined DataFrame `teams_players_new` & `teams_goals_new`](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/b538673d-13e4-4314-b241-aeba47efd6d8/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UUHOLCZ4%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T220929Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJGMEQCIBFz02LZ8ai0AWAeNXqIr5T1ht%2BrqwisSOcwXVnkIQqWAiAgAFTU1KBSFZdoB5y9CVkPgGLMqS1eTcLGrExARoj1Jir%2FAwgmEAAaDDYzNzQyMzE4MzgwNSIMxFcWnI95N9iTIadPKtwDZGs3JuLXvSirYegXukSxMneAgmV%2BNeXYZ0%2Bnk%2BU%2BpZoS84PfRTIkQ3XjvEcwc6iRJt9qIbA2tUrgRQvAEm99WZiwQuLgnPZtA4WQbddhwErcl%2FF1Zb3yBIBZMpbuw5DKA7Di5flmk%2FlsmhB0jr0D4Ss94e1x7aha6Sq9aMURkm%2BN6tw916zo7HYws%2B19ufxrnHbd3dZNf7WBhzEuyXqJvzQ6kut6ySfbn7QOXzd%2BjxsN6qdH1u4bJJr%2FyMhXp7s%2FIYWeYws1luMpANU3gokbt36xLFUd0Hu9IL398rCrF226WAMEcdfjNm32fDT5uTLK0HUW2WaR8TU9pvSFqgMzAGWWfBEmDUfQq%2BEK%2FXLiLdemz%2FRLdfOpY7yWixlFui6jLnw%2FpvdpZAvzlegxxok5RXRKbHrYZmaaUwk2jTCB2SiR3YIfeP0YqcxiJmp8tM0mc7fVDEFQeGqVKh3RKr4NOfW9iHvHEpsHp8dNmyMgd%2FS5IC4qfJ6r3DDcPfGieMDtlYnIQYL2FFXEZ9acv1q%2Btwv0SVmHRa3hGuLE3WOFPVRRewzgu4Dkx4goGuNffbIGuZZb2qEjit5eYhxHPtqSCHaxyvcC%2B7gQlDV23svRLrrqzUPYRP9zrq%2FSkXIw5aX3yQY6pgHIU6tNIscqo0LHw9riMGhTTDMo%2Bof0zwNQkltmsb7gswEt3r881us5XEuajD%2FqaNuLIcksEcO7plMuvco%2BurD0a5xtP%2FWmkF97DR1w5MGAwFO3Ev1tQCApce8cn4SNobKcANRBwWaWNZn7QKXw7rm9r9vBABZpurpjfxHypGpQWPaYjz1o4kaXHHvo0GbJqkgVb8lzdWj0kG53wkAkFnwpSzRVjYLL&X-Amz-Signature=8fdd5f68c65890c62357fce81e8b18b379702d7b44f462ede6ff8c4b212a32ff&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
In the output DataFrame we can observe two things.
Firstly, the data from the right DataFrame is just appended but not actually merged with the data from the left DataFrame. Therefore, we still have two columns with team names and some teams have two different index values. For example, Crystal Palace is in `Team_left` at index position 16 and in `Team_right` at index position 18. So, no new index ordering is created when doing a `.join()`.
Secondly, some index positions are missing, i.e., there are some gaps → 0, 2, 11 and 12 are missing. This is because the index positions 0 and 11 do not exist in the left DataFrame `teams_player_new` and the index positions 2 and 12 do not exist in the right DataFrame `teams_goals_new` (see pictures below). And since we do an `'inner'` join these rows are consequently excluded from the output.
![`teams_players_new` with missing index positions 0 and 11](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/ca5f11a7-7993-4b97-a4dc-f04a32c79b77/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VPKHJTX5%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T220931Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCICsSzlfe0%2BaB15kCxwB2%2F8AkKk3G2BqzRi%2FvEKwocPMzAiEAjH5oqnSEUEXEq0riqyYyEUoQ%2BBc8N76WGNHessWVLhcq%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDNt67cXUahnKlAeORyrcAxrdTABSsL%2Bhzvi6xlLVtAbQIqLNbTL3GAWcFlGP6MOJf65BJ1FcNKsw%2FA4H9iTXXnXkoxG8qR8mSuGQPC5mS0I4YMQQP8JgEkfPFRrqRor1BasXInjfw8CeKI7bWDCKUwfLFdn3iI%2FZEkRM%2B3symwe2YpEdoSrYtP0%2BXU0sGknT%2FEg2%2FpBx6AUSCWu4uWKvNhkbnZjqrodFcYm98ATCYWcoXm3A2lT8nbjM8Z0kO2FjrRsVbpfTHJkAjDtPzlauDiwhmUo%2BwztzU7%2F9C76KI5lR1IqAhSghV5z%2F6IbVOenudd%2Fury1o6thS%2FnDNXiKRqwjTic6mzJcSNXp25sxpIVW2ck9pydPBTNCO%2FUP1yfrRk%2FSqZtKSSf%2B77S27WbM5A04WHwOKclfDOPsUVaGRow0vflO6S%2FFC9VjOVPfPhRBk2FoTxTk36Py8cjWre9JYTDIquUpLIpnbAMJYvH69aYtGFNeBU%2Fa%2FHiIIjwzRhKhqTA4WhG8xYhZoICZMvyqrt9lQEyek7GHjtkckEpqVax1DJJ0vxvI%2B6P%2FuuvhDU4bcOtPtJcieRpl5EtwVIzSKKNxs4I9sAO7gttxiUvY4SuqMA1E3UQlfZnrrny3%2BXmOoVw8wFt3cbjgiPCYMML2m98kGOqUBEtUbRltIchdvAHOCaW51bDI0pbz6kTHM%2BXNvCjgjZBXr9l%2FZpWUMtC7ESUnVuCi5P5%2B6QqpbQtbyq%2FVe4NjkWVMrqpeMDgbx8P3UwCKrTkU1Av5JqRxdlmu%2FCwq%2FCdHHxNSZL%2FCbCz4LpRkI5aJp13%2Few04idAkGA6fmpAAS1INAI5EcXyFDhRPPemIDS7UsNdEsZIGcGPTl8NHSGr2lKHMlnWeL&X-Amz-Signature=e9b3844807ba67b26fc57db3ab04b340568b7c637493ae9cdb4ce6e43a30c6b2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
![`teams_goals_new` with missing index positions 2 and 12](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/675a20f5-92cf-4684-b55d-caae3e9b9ef0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y3GTHSJW%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T220931Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIFAnCRBecjTVpPxrsNpQ%2BJ7zUvMGhfzPxFklUNSMO33nAiEAo2HilAOtg9DvFJFtOV7vaBQEsR9PFCPQycJS5G6LUswq%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDI3znNBlvsQ9YCBHFSrcA9lbpu5xXBlAshyCmnb0khcEwOQ93seJSh3RoUOz6yWm2sY596oqZ0qoNpu9RkvxWJ0UlC3HNKtlmIgS%2FYrkt1%2BnZomYEiAg%2BFdOVp9c625XZBdVTwL%2BRUtAohAV7VMNWlg4pEsq3wR9esmtFDtZ0GmDqlczeHHbqKXjAPhfFMw1dZarvzHZ0zLnFsdIQfYNSMr5jlYY0yiYn5boqBbxHAJk2b1yXZEz0%2FBJ%2FxdV71l0Poi5xrrHFAYVC%2FgriA8WHgQXoxJ5Q1UvfO3Yogi3IX7OJtFBGDVNCLP2jEsweQYaMo9p0iISsSZ%2Fgh%2B5z06xUTfM%2FObud7I%2BUnhSPz7qzyWTDxQ%2F80VUA3JTj04xRg359P8mRF4Va2C2cnPcT%2BGzOtAbiYIzw7fxftFpp4XsZ%2BmS4p36VlqshI0AU%2F%2BHgB9e2ixIL54BI0THfYTzPHXihlXqfMrwM8GKvRoO5vik7DcBmy15WK2T40UbHhxgCVIEqLmyPcSAzUUlblzVUvZRXwsrzKaejEeG9BadusD%2B%2FUlLzQlihYH32HsPCDQYuLhQU9p4p5oGUWU0P%2BmUtZDG3S9ahZRfBKhVtxZ6uRnQ8GG4zBLChSLrBow9OJAGcOg39yuggBYBFlpmcKDpMK6m98kGOqUBaTPsgLP8zamnPSJDkAUuT7o2PTidFQ5RTQQ8dzhL3Q%2FOC2SZO2z1Nd6PYyMgsBhq%2BvGF6%2BbsKNBlkYcD5hxGKRynZHKH6bPs6ayq70ioDmdl5By5p6EqXhOfXwT%2BuZ4TtYwjgU6BUfk%2FC7SEejYieUfiWg%2BuHE3prUXgW2yG5N66%2F3rGVqkgjqbgGoez50baSzZJmKoqN4xpt2jmpsmnBIhxg64G&X-Amz-Signature=ffd040cf5fff9ea40ec260761884878f701352fd9559d012a90fdbc9a299d1f1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
---
**Left join**
As we already learned, the left-join is the default join method. Thus, when we want to do a left join we don’t have to specify the `how=` parameter.
```python
teams_players_new.join(teams_goals_new, lsuffix='_left', rsuffix='_right')
```
![Joined DataFrame `teams_players_new` & `teams_goals_new`](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/1059a0f9-71b6-4c0e-9ce9-154e1334b735/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UUHOLCZ4%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T220929Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJGMEQCIBFz02LZ8ai0AWAeNXqIr5T1ht%2BrqwisSOcwXVnkIQqWAiAgAFTU1KBSFZdoB5y9CVkPgGLMqS1eTcLGrExARoj1Jir%2FAwgmEAAaDDYzNzQyMzE4MzgwNSIMxFcWnI95N9iTIadPKtwDZGs3JuLXvSirYegXukSxMneAgmV%2BNeXYZ0%2Bnk%2BU%2BpZoS84PfRTIkQ3XjvEcwc6iRJt9qIbA2tUrgRQvAEm99WZiwQuLgnPZtA4WQbddhwErcl%2FF1Zb3yBIBZMpbuw5DKA7Di5flmk%2FlsmhB0jr0D4Ss94e1x7aha6Sq9aMURkm%2BN6tw916zo7HYws%2B19ufxrnHbd3dZNf7WBhzEuyXqJvzQ6kut6ySfbn7QOXzd%2BjxsN6qdH1u4bJJr%2FyMhXp7s%2FIYWeYws1luMpANU3gokbt36xLFUd0Hu9IL398rCrF226WAMEcdfjNm32fDT5uTLK0HUW2WaR8TU9pvSFqgMzAGWWfBEmDUfQq%2BEK%2FXLiLdemz%2FRLdfOpY7yWixlFui6jLnw%2FpvdpZAvzlegxxok5RXRKbHrYZmaaUwk2jTCB2SiR3YIfeP0YqcxiJmp8tM0mc7fVDEFQeGqVKh3RKr4NOfW9iHvHEpsHp8dNmyMgd%2FS5IC4qfJ6r3DDcPfGieMDtlYnIQYL2FFXEZ9acv1q%2Btwv0SVmHRa3hGuLE3WOFPVRRewzgu4Dkx4goGuNffbIGuZZb2qEjit5eYhxHPtqSCHaxyvcC%2B7gQlDV23svRLrrqzUPYRP9zrq%2FSkXIw5aX3yQY6pgHIU6tNIscqo0LHw9riMGhTTDMo%2Bof0zwNQkltmsb7gswEt3r881us5XEuajD%2FqaNuLIcksEcO7plMuvco%2BurD0a5xtP%2FWmkF97DR1w5MGAwFO3Ev1tQCApce8cn4SNobKcANRBwWaWNZn7QKXw7rm9r9vBABZpurpjfxHypGpQWPaYjz1o4kaXHHvo0GbJqkgVb8lzdWj0kG53wkAkFnwpSzRVjYLL&X-Amz-Signature=91fbd4f789b75e0545a32aecab94d3c06e74543708195049491107fafc199469&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
In the output DataFrame we can observe that the indices 0 and 11 are still missing - why? These indices are present in the right DataFrame but not in the left one and thus no overlapping indices are found for these two rows. Since we are doing a left-join, these two rows are excluded from the output.
Also we see that for two rows there are some `NaN` values - why?
These rows, indices 2 and 12 are included in the left DataFrame but not in the right DataFrame. Since we are doing a left-join the rows are not excluded from the output, instead `NaN` is inserted in the cells where no data could be found in the right DataFrame for these two rows.
---
**Right join**
We can perform a right-join with the following command.
```python
teams_players_new.join(teams_goals_new, how='right', lsuffix='_left', rsuffix='_right')
```
![Joined DataFrame `teams_players_new` & `teams_goals_new`](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/033050c2-1732-452b-ac1e-177ed308e54d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UUHOLCZ4%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T220930Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJGMEQCIBFz02LZ8ai0AWAeNXqIr5T1ht%2BrqwisSOcwXVnkIQqWAiAgAFTU1KBSFZdoB5y9CVkPgGLMqS1eTcLGrExARoj1Jir%2FAwgmEAAaDDYzNzQyMzE4MzgwNSIMxFcWnI95N9iTIadPKtwDZGs3JuLXvSirYegXukSxMneAgmV%2BNeXYZ0%2Bnk%2BU%2BpZoS84PfRTIkQ3XjvEcwc6iRJt9qIbA2tUrgRQvAEm99WZiwQuLgnPZtA4WQbddhwErcl%2FF1Zb3yBIBZMpbuw5DKA7Di5flmk%2FlsmhB0jr0D4Ss94e1x7aha6Sq9aMURkm%2BN6tw916zo7HYws%2B19ufxrnHbd3dZNf7WBhzEuyXqJvzQ6kut6ySfbn7QOXzd%2BjxsN6qdH1u4bJJr%2FyMhXp7s%2FIYWeYws1luMpANU3gokbt36xLFUd0Hu9IL398rCrF226WAMEcdfjNm32fDT5uTLK0HUW2WaR8TU9pvSFqgMzAGWWfBEmDUfQq%2BEK%2FXLiLdemz%2FRLdfOpY7yWixlFui6jLnw%2FpvdpZAvzlegxxok5RXRKbHrYZmaaUwk2jTCB2SiR3YIfeP0YqcxiJmp8tM0mc7fVDEFQeGqVKh3RKr4NOfW9iHvHEpsHp8dNmyMgd%2FS5IC4qfJ6r3DDcPfGieMDtlYnIQYL2FFXEZ9acv1q%2Btwv0SVmHRa3hGuLE3WOFPVRRewzgu4Dkx4goGuNffbIGuZZb2qEjit5eYhxHPtqSCHaxyvcC%2B7gQlDV23svRLrrqzUPYRP9zrq%2FSkXIw5aX3yQY6pgHIU6tNIscqo0LHw9riMGhTTDMo%2Bof0zwNQkltmsb7gswEt3r881us5XEuajD%2FqaNuLIcksEcO7plMuvco%2BurD0a5xtP%2FWmkF97DR1w5MGAwFO3Ev1tQCApce8cn4SNobKcANRBwWaWNZn7QKXw7rm9r9vBABZpurpjfxHypGpQWPaYjz1o4kaXHHvo0GbJqkgVb8lzdWj0kG53wkAkFnwpSzRVjYLL&X-Amz-Signature=8bcf2498e664ba594ab14ab672df3ae1e336b72f755aa42aa5deec63c719bf3c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
We can again observe that some indices are missing, 2 and 12 specifically. It’s the same concept as in the previous example: These indices are present in the left DataFrame but not in the right DataFrame and since we are doing a right-join these two rows are excluded.
And missing data cells are again filled with `NaN` values. This affects the rows that are present in the right DataFrame but not in the left DataFrame and are not excluded from the output as we are doing a right-join.
---
**Outer join**
We can perform an outer-join with the following command. 
```python
teams_players_new.join(teams_goals_new, how='outer', lsuffix='_left', rsuffix='_right')
```
![Joined DataFrame `teams_players_new` & `teams_goals_new`](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/a52156c7-c866-4fd1-ab19-6e21622433bb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UUHOLCZ4%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T220930Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJGMEQCIBFz02LZ8ai0AWAeNXqIr5T1ht%2BrqwisSOcwXVnkIQqWAiAgAFTU1KBSFZdoB5y9CVkPgGLMqS1eTcLGrExARoj1Jir%2FAwgmEAAaDDYzNzQyMzE4MzgwNSIMxFcWnI95N9iTIadPKtwDZGs3JuLXvSirYegXukSxMneAgmV%2BNeXYZ0%2Bnk%2BU%2BpZoS84PfRTIkQ3XjvEcwc6iRJt9qIbA2tUrgRQvAEm99WZiwQuLgnPZtA4WQbddhwErcl%2FF1Zb3yBIBZMpbuw5DKA7Di5flmk%2FlsmhB0jr0D4Ss94e1x7aha6Sq9aMURkm%2BN6tw916zo7HYws%2B19ufxrnHbd3dZNf7WBhzEuyXqJvzQ6kut6ySfbn7QOXzd%2BjxsN6qdH1u4bJJr%2FyMhXp7s%2FIYWeYws1luMpANU3gokbt36xLFUd0Hu9IL398rCrF226WAMEcdfjNm32fDT5uTLK0HUW2WaR8TU9pvSFqgMzAGWWfBEmDUfQq%2BEK%2FXLiLdemz%2FRLdfOpY7yWixlFui6jLnw%2FpvdpZAvzlegxxok5RXRKbHrYZmaaUwk2jTCB2SiR3YIfeP0YqcxiJmp8tM0mc7fVDEFQeGqVKh3RKr4NOfW9iHvHEpsHp8dNmyMgd%2FS5IC4qfJ6r3DDcPfGieMDtlYnIQYL2FFXEZ9acv1q%2Btwv0SVmHRa3hGuLE3WOFPVRRewzgu4Dkx4goGuNffbIGuZZb2qEjit5eYhxHPtqSCHaxyvcC%2B7gQlDV23svRLrrqzUPYRP9zrq%2FSkXIw5aX3yQY6pgHIU6tNIscqo0LHw9riMGhTTDMo%2Bof0zwNQkltmsb7gswEt3r881us5XEuajD%2FqaNuLIcksEcO7plMuvco%2BurD0a5xtP%2FWmkF97DR1w5MGAwFO3Ev1tQCApce8cn4SNobKcANRBwWaWNZn7QKXw7rm9r9vBABZpurpjfxHypGpQWPaYjz1o4kaXHHvo0GbJqkgVb8lzdWj0kG53wkAkFnwpSzRVjYLL&X-Amz-Signature=59dd926e0b67772ecd0ba90a6226c1306ecfb4cf24d01c9ebac42ffcb6c35c3e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
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
![outer_merge_df](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/2431d095-7483-492f-b1ec-5fe0a2250ea9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RSFUEGPN%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T220932Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJIMEYCIQDNPTb5FNCYnc01kSr1Yf7a2n%2BICPlUK9%2B7IFpbgeECFQIhAJtHEQlZFPHOV3AhFFc2%2BVKcHguQ0UCEtv989GJbtKDsKv8DCCYQABoMNjM3NDIzMTgzODA1IgzrzrB4Qs4fzNkVKI0q3AMIz9LaiCzLlQjbzDkxF%2FIPSQ4PyhxoRVxpFrKpqr%2FKaQR%2FNippoBVruG1urSKtkpqQe36ZyfxKTT1crt%2Fxa7NWZ75%2B8%2B6ZB6Y1kjLu%2FbE1Pur42Onmo%2BV85zQOWWREL3%2FkLv%2BhoEmwB656LR5t1SSrZ94SXeqLuCVkl07AGx%2FdbQBtbklkNy4randR1gloh%2Bet%2FEl6G0VfWVJIJUuUag0i8I7rrKmpfBCahjt5lL7%2BYHItmHoWVfERgUzAXY4CVT04%2FRF9EX%2BbDgu09ckGqpXM%2FLqNR0x5vpO%2FJfmmDVlJVTthrGGc1WzX6VLkrtTkk5qAPRsMok9%2FJjO2QlHWNPon4MOdAmDgcD0wE2qQ1UjpKijFcqrIdkgs6UTuPpyH38GWFiQLdvm57tDIc1Wjx38DCTMLExzJ7X7IF8bGFpyvcDKpjxUEfQetUyY8jV3IiFp0AKuSPFf%2BI5UrtcIjv3f%2B3TNHP2FuX6A0%2B5IJdnkdMXDKnwK7yG1MHIu1%2FnI66%2B0Wl3j9fV2boOGvBS84gnP%2FaxYrsZFWv7fpKiUcahhGWpunIsuofuKHFdv9tPxwe%2Bqtsh4MCAj2C1qhApIRdADROYH3h0Xicj4tDG4w5ynBRT5tOktXfdD5eUxUCTCMpvfJBjqkAW9fHAmpRkM82UAI88H%2BQe23LdUM%2FgefbMKz78%2BBS21iVqLPYx8XBlulvZZwLyRz74%2Bz%2Bn50eulbAx6TMhxJDWJie8nxIXs3o%2FuVvGiPFtvD92htJUlv6bQIukMNg86BNweHRpbsuJsrQT6N2SPPqCmpvpUs%2BZbH23SkHyH5LPQmQ2lrTxc8bEoE9SPrkVMVgf%2FqQBRif8sYDlHh5vxV59mYml8H&X-Amz-Signature=d6d20c7903ea31c51c588e4c633be110e42f63aef3aeec6ae6326d2aeb1453b5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
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
![df](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/e2a194f9-0d78-4736-836b-59261da98028/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VVJDDPB4%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T220933Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIGPCxudFBsGj3kfrNzN57PvW%2FezeUyg1VFUeyb14x8rPAiEAgOlDr8ctBVqQkhK2o%2BKP48xni7JTY5ZVoY8G%2BvIQke4q%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDAsIec36lm2weU1%2FwyrcA5lHaOTM8cINHVktKPTnUipbtbzoH5FGvVybkeB9sq%2FnWFeA8wIHdhM2cfCjDl3%2BYdJAmK3fM%2Fsz9XHDEmmWScgxT%2BgfL%2F3rgYKgkzYicZFcLmjdO6F7ocnY%2FuTtwmaVcY96jogn0%2B5z8fD5pOc3PsIQoaa8UuceCZ8qqHqL%2BP4HT5SHtqucoUt%2FZUXh8fS%2FLUXRbu%2BP3XOo8kXpw4O7Dh8Onhe%2BDKV1nmDfgOxz6ed45zteRse%2F0gMdtd4H3U8tZNdL3obC%2BQHUEPvnJZdXDSCiWDTEBaXiM5CziZbDBjSTAUs94Dz19zIglIxJdC3QN9RUvFNzkDMsUPWUBLGoyAh6HWi%2FbSqCJvmGBiNCMWY3aySiJ7fHDUiRtLy8OpQIv9ZY1Uswo0dx4dU5Ki65dF%2BUJyoyVdUJRI2BGkm5vcQeVjm2HYVSkurnTaPZSO%2FGYPKx%2BlZjDoKOVclyfWj%2FF%2FtfxLfA9o0vYgq94czdbbHlHXyspcV5peqhglMDsU8kiBthtTlYNW0fBPjz96g8XCMq4RlWbTlMR7VgeX05vxfDEYTp7kmglRhxXWUlkm930aGgyJprPc9dNPQX7nihjUUQAK0Z%2BcYr1JFp36tb0BCD5SoyVEGdnaqr8sU9MNSl98kGOqUBfkQroq5xJ5SUj1LC8UbiB2rnfN0wa%2FxGvHOazgjHtPsdjNeaCpDKeYLbzLJ4oKGRJ4HKSzRG1lr%2Ft%2BQDB4mPDzakTkRsvE2iIOkfKtlnrvBx7pf%2Bx7rrxOqtstP2z3sOIGumQKsiqLBJR0ioORkiGvtwoX7DOqpZ8fu9qJtbHnXSY1bDcM2T19kMUgNZqFLv%2FH2%2BpMXrx5VOVb%2FmlXuywKrLV%2F5L&X-Amz-Signature=9a1454a624ff7ba1bdfac127a071baf614108c849e661bd468328deecb2b82ab&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
If we now want to create a second version of this DataFrame and store it in a new variable `df_2`, we can simply create a copy of `df`.
```python
df_2 = df.copy()

df_2
```
![df_2](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/25b4b04b-4667-48fd-8a2d-1d13102917f8/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VVJDDPB4%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T220933Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIGPCxudFBsGj3kfrNzN57PvW%2FezeUyg1VFUeyb14x8rPAiEAgOlDr8ctBVqQkhK2o%2BKP48xni7JTY5ZVoY8G%2BvIQke4q%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDAsIec36lm2weU1%2FwyrcA5lHaOTM8cINHVktKPTnUipbtbzoH5FGvVybkeB9sq%2FnWFeA8wIHdhM2cfCjDl3%2BYdJAmK3fM%2Fsz9XHDEmmWScgxT%2BgfL%2F3rgYKgkzYicZFcLmjdO6F7ocnY%2FuTtwmaVcY96jogn0%2B5z8fD5pOc3PsIQoaa8UuceCZ8qqHqL%2BP4HT5SHtqucoUt%2FZUXh8fS%2FLUXRbu%2BP3XOo8kXpw4O7Dh8Onhe%2BDKV1nmDfgOxz6ed45zteRse%2F0gMdtd4H3U8tZNdL3obC%2BQHUEPvnJZdXDSCiWDTEBaXiM5CziZbDBjSTAUs94Dz19zIglIxJdC3QN9RUvFNzkDMsUPWUBLGoyAh6HWi%2FbSqCJvmGBiNCMWY3aySiJ7fHDUiRtLy8OpQIv9ZY1Uswo0dx4dU5Ki65dF%2BUJyoyVdUJRI2BGkm5vcQeVjm2HYVSkurnTaPZSO%2FGYPKx%2BlZjDoKOVclyfWj%2FF%2FtfxLfA9o0vYgq94czdbbHlHXyspcV5peqhglMDsU8kiBthtTlYNW0fBPjz96g8XCMq4RlWbTlMR7VgeX05vxfDEYTp7kmglRhxXWUlkm930aGgyJprPc9dNPQX7nihjUUQAK0Z%2BcYr1JFp36tb0BCD5SoyVEGdnaqr8sU9MNSl98kGOqUBfkQroq5xJ5SUj1LC8UbiB2rnfN0wa%2FxGvHOazgjHtPsdjNeaCpDKeYLbzLJ4oKGRJ4HKSzRG1lr%2Ft%2BQDB4mPDzakTkRsvE2iIOkfKtlnrvBx7pf%2Bx7rrxOqtstP2z3sOIGumQKsiqLBJR0ioORkiGvtwoX7DOqpZ8fu9qJtbHnXSY1bDcM2T19kMUgNZqFLv%2FH2%2BpMXrx5VOVb%2FmlXuywKrLV%2F5L&X-Amz-Signature=4b795663da7a6d3c70e6b5d5dc3e5686b158ad85c0c576fbd03a55ddb8838c49&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
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
![df](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/cedfaef2-c0a6-48ee-b82e-0aba216bca06/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VVJDDPB4%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T220933Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIGPCxudFBsGj3kfrNzN57PvW%2FezeUyg1VFUeyb14x8rPAiEAgOlDr8ctBVqQkhK2o%2BKP48xni7JTY5ZVoY8G%2BvIQke4q%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDAsIec36lm2weU1%2FwyrcA5lHaOTM8cINHVktKPTnUipbtbzoH5FGvVybkeB9sq%2FnWFeA8wIHdhM2cfCjDl3%2BYdJAmK3fM%2Fsz9XHDEmmWScgxT%2BgfL%2F3rgYKgkzYicZFcLmjdO6F7ocnY%2FuTtwmaVcY96jogn0%2B5z8fD5pOc3PsIQoaa8UuceCZ8qqHqL%2BP4HT5SHtqucoUt%2FZUXh8fS%2FLUXRbu%2BP3XOo8kXpw4O7Dh8Onhe%2BDKV1nmDfgOxz6ed45zteRse%2F0gMdtd4H3U8tZNdL3obC%2BQHUEPvnJZdXDSCiWDTEBaXiM5CziZbDBjSTAUs94Dz19zIglIxJdC3QN9RUvFNzkDMsUPWUBLGoyAh6HWi%2FbSqCJvmGBiNCMWY3aySiJ7fHDUiRtLy8OpQIv9ZY1Uswo0dx4dU5Ki65dF%2BUJyoyVdUJRI2BGkm5vcQeVjm2HYVSkurnTaPZSO%2FGYPKx%2BlZjDoKOVclyfWj%2FF%2FtfxLfA9o0vYgq94czdbbHlHXyspcV5peqhglMDsU8kiBthtTlYNW0fBPjz96g8XCMq4RlWbTlMR7VgeX05vxfDEYTp7kmglRhxXWUlkm930aGgyJprPc9dNPQX7nihjUUQAK0Z%2BcYr1JFp36tb0BCD5SoyVEGdnaqr8sU9MNSl98kGOqUBfkQroq5xJ5SUj1LC8UbiB2rnfN0wa%2FxGvHOazgjHtPsdjNeaCpDKeYLbzLJ4oKGRJ4HKSzRG1lr%2Ft%2BQDB4mPDzakTkRsvE2iIOkfKtlnrvBx7pf%2Bx7rrxOqtstP2z3sOIGumQKsiqLBJR0ioORkiGvtwoX7DOqpZ8fu9qJtbHnXSY1bDcM2T19kMUgNZqFLv%2FH2%2BpMXrx5VOVb%2FmlXuywKrLV%2F5L&X-Amz-Signature=8ecceed0beee0beada1e6ea6350518207ea89b79575c74ad73480c1411e374b3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
However, when we output now `df_2` we can see that row 6 was dropped fom this DataFrame as well. This is because no copy was created in the frist place, thus variables `df` and `df_2` are pointing to the same DataFrame.
![df_2](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/cedfaef2-c0a6-48ee-b82e-0aba216bca06/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VVJDDPB4%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T220933Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIGPCxudFBsGj3kfrNzN57PvW%2FezeUyg1VFUeyb14x8rPAiEAgOlDr8ctBVqQkhK2o%2BKP48xni7JTY5ZVoY8G%2BvIQke4q%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDAsIec36lm2weU1%2FwyrcA5lHaOTM8cINHVktKPTnUipbtbzoH5FGvVybkeB9sq%2FnWFeA8wIHdhM2cfCjDl3%2BYdJAmK3fM%2Fsz9XHDEmmWScgxT%2BgfL%2F3rgYKgkzYicZFcLmjdO6F7ocnY%2FuTtwmaVcY96jogn0%2B5z8fD5pOc3PsIQoaa8UuceCZ8qqHqL%2BP4HT5SHtqucoUt%2FZUXh8fS%2FLUXRbu%2BP3XOo8kXpw4O7Dh8Onhe%2BDKV1nmDfgOxz6ed45zteRse%2F0gMdtd4H3U8tZNdL3obC%2BQHUEPvnJZdXDSCiWDTEBaXiM5CziZbDBjSTAUs94Dz19zIglIxJdC3QN9RUvFNzkDMsUPWUBLGoyAh6HWi%2FbSqCJvmGBiNCMWY3aySiJ7fHDUiRtLy8OpQIv9ZY1Uswo0dx4dU5Ki65dF%2BUJyoyVdUJRI2BGkm5vcQeVjm2HYVSkurnTaPZSO%2FGYPKx%2BlZjDoKOVclyfWj%2FF%2FtfxLfA9o0vYgq94czdbbHlHXyspcV5peqhglMDsU8kiBthtTlYNW0fBPjz96g8XCMq4RlWbTlMR7VgeX05vxfDEYTp7kmglRhxXWUlkm930aGgyJprPc9dNPQX7nihjUUQAK0Z%2BcYr1JFp36tb0BCD5SoyVEGdnaqr8sU9MNSl98kGOqUBfkQroq5xJ5SUj1LC8UbiB2rnfN0wa%2FxGvHOazgjHtPsdjNeaCpDKeYLbzLJ4oKGRJ4HKSzRG1lr%2Ft%2BQDB4mPDzakTkRsvE2iIOkfKtlnrvBx7pf%2Bx7rrxOqtstP2z3sOIGumQKsiqLBJR0ioORkiGvtwoX7DOqpZ8fu9qJtbHnXSY1bDcM2T19kMUgNZqFLv%2FH2%2BpMXrx5VOVb%2FmlXuywKrLV%2F5L&X-Amz-Signature=8ecceed0beee0beada1e6ea6350518207ea89b79575c74ad73480c1411e374b3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
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
![players_df with old column labels](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/21964fa8-a672-418d-8f2d-f80e59e55bf3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663RA4VSSA%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T220934Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIBQxHzSNuoiosDjrF4kUgRniU3v4DuSu4oh67PKb3dhfAiEA0MQsTQhhBmrldfeGcicPjH9heJKXZWCBoqssH6hGwroq%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDMPOC83wD2Nylb3iOCrcAxYahiyaajtpfYjXP8%2F5fK2LhvI82d7SAAR6QQZCbf%2BJqG7eS%2BPgqsu2bCm617%2Bp88aY%2B4O2bmT8Exki00nSnJJ6Gr488CW0xgnnAgFyRyB09%2Byv8LBlf1aUtGTTRMfGfKKPzjojJk7m0%2FvYOA71jZL5oyBUjLl0W22m65YVMx2%2FwG61IiikiRst5BLnMrNVhzJoY0Z%2FcVzet4caiXYAFY9sj4h28oEBpIkDWtdvRuSRJ4Q%2FzS50DP4zPDghdKvgAXYIf145xOu0UhwmyZWZCkk0E8ZUXlL4Fp%2FF6dpAxInHJ5brZDSeIkaAPbp8Ljp2NHfX3ZoZBm%2BUOxg9Q8Rhxol2eL9vsI5ylA27jUjKV5pqbfCAXzyxnq%2F2%2Fkw3SUNRG%2FKtGa3svN5%2B7JHJHdzU4nddOPpPTGjY3tqNkMxqg%2FKaT02N5XC4HGZBbfdeRv4E5eV7Z%2FH6aGcV%2Fu7Exjdqwtz%2F27WpEtGBHsxT3IB%2FGaYoQUHUF9JgVNS05P9SU5vDnPxbK4Bp3NlRzFhtGKywFCo8WmJ1puuKGN1pznSn6obQxEcuyqGuV5IyXzhmiSBLyBG10L8MLDOSUadKjqLmouQ8el7uLWyVlFLkpXTrfquD%2FPSyH60sMDhjIHlfMJ6m98kGOqUB0dxutAssSJXu3z03OdZ9WIjd71ZnBbH%2FIqfZ9taM93jI1ir2Yl2DxaCpH1w3kFf0IM2nWRp2qBlCsUpazUcP4k8Emo2L7lrq9h2fy98xNHPskaaQDhRKQ4iRv55km2kCv%2B1%2BqzwnxGAMH1gIMKfls5LrUFlPJg2I%2FlputfgSGPMC8CKtMDFWeC%2BQprFAighn69irjgS2QkjPCSVsrDr3MWAZgvLz&X-Amz-Signature=41c2bbeac9e7679bd1faec54cc2dba0b0f5667ee675ce6c01c4401913c9bb070&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
We can achieve that by running the following command:
```python
mapping_dict = {
		'total_points' : 'Total points',
		'points_per_game' : 'Points per game',
		'days_played' : 'Days played'
}

players_df.rename(mapping_dict, axis=1, inplace=True)
```
![playes_df with new column labels](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/c2cf77df-7b1d-4b9f-8a5c-aeeaaf7ae0bb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663RA4VSSA%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T220934Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIBQxHzSNuoiosDjrF4kUgRniU3v4DuSu4oh67PKb3dhfAiEA0MQsTQhhBmrldfeGcicPjH9heJKXZWCBoqssH6hGwroq%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDMPOC83wD2Nylb3iOCrcAxYahiyaajtpfYjXP8%2F5fK2LhvI82d7SAAR6QQZCbf%2BJqG7eS%2BPgqsu2bCm617%2Bp88aY%2B4O2bmT8Exki00nSnJJ6Gr488CW0xgnnAgFyRyB09%2Byv8LBlf1aUtGTTRMfGfKKPzjojJk7m0%2FvYOA71jZL5oyBUjLl0W22m65YVMx2%2FwG61IiikiRst5BLnMrNVhzJoY0Z%2FcVzet4caiXYAFY9sj4h28oEBpIkDWtdvRuSRJ4Q%2FzS50DP4zPDghdKvgAXYIf145xOu0UhwmyZWZCkk0E8ZUXlL4Fp%2FF6dpAxInHJ5brZDSeIkaAPbp8Ljp2NHfX3ZoZBm%2BUOxg9Q8Rhxol2eL9vsI5ylA27jUjKV5pqbfCAXzyxnq%2F2%2Fkw3SUNRG%2FKtGa3svN5%2B7JHJHdzU4nddOPpPTGjY3tqNkMxqg%2FKaT02N5XC4HGZBbfdeRv4E5eV7Z%2FH6aGcV%2Fu7Exjdqwtz%2F27WpEtGBHsxT3IB%2FGaYoQUHUF9JgVNS05P9SU5vDnPxbK4Bp3NlRzFhtGKywFCo8WmJ1puuKGN1pznSn6obQxEcuyqGuV5IyXzhmiSBLyBG10L8MLDOSUadKjqLmouQ8el7uLWyVlFLkpXTrfquD%2FPSyH60sMDhjIHlfMJ6m98kGOqUB0dxutAssSJXu3z03OdZ9WIjd71ZnBbH%2FIqfZ9taM93jI1ir2Yl2DxaCpH1w3kFf0IM2nWRp2qBlCsUpazUcP4k8Emo2L7lrq9h2fy98xNHPskaaQDhRKQ4iRv55km2kCv%2B1%2BqzwnxGAMH1gIMKfls5LrUFlPJg2I%2FlputfgSGPMC8CKtMDFWeC%2BQprFAighn69irjgS2QkjPCSVsrDr3MWAZgvLz&X-Amz-Signature=45d97bc0117973b11ac06889c31916cda47ae9fbb0289bea4b4a03f320d0d74e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
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
![players_df with old index labels](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/25ecc7fb-79c8-400a-b6f6-a5555e6f1257/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663RA4VSSA%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T220934Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIBQxHzSNuoiosDjrF4kUgRniU3v4DuSu4oh67PKb3dhfAiEA0MQsTQhhBmrldfeGcicPjH9heJKXZWCBoqssH6hGwroq%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDMPOC83wD2Nylb3iOCrcAxYahiyaajtpfYjXP8%2F5fK2LhvI82d7SAAR6QQZCbf%2BJqG7eS%2BPgqsu2bCm617%2Bp88aY%2B4O2bmT8Exki00nSnJJ6Gr488CW0xgnnAgFyRyB09%2Byv8LBlf1aUtGTTRMfGfKKPzjojJk7m0%2FvYOA71jZL5oyBUjLl0W22m65YVMx2%2FwG61IiikiRst5BLnMrNVhzJoY0Z%2FcVzet4caiXYAFY9sj4h28oEBpIkDWtdvRuSRJ4Q%2FzS50DP4zPDghdKvgAXYIf145xOu0UhwmyZWZCkk0E8ZUXlL4Fp%2FF6dpAxInHJ5brZDSeIkaAPbp8Ljp2NHfX3ZoZBm%2BUOxg9Q8Rhxol2eL9vsI5ylA27jUjKV5pqbfCAXzyxnq%2F2%2Fkw3SUNRG%2FKtGa3svN5%2B7JHJHdzU4nddOPpPTGjY3tqNkMxqg%2FKaT02N5XC4HGZBbfdeRv4E5eV7Z%2FH6aGcV%2Fu7Exjdqwtz%2F27WpEtGBHsxT3IB%2FGaYoQUHUF9JgVNS05P9SU5vDnPxbK4Bp3NlRzFhtGKywFCo8WmJ1puuKGN1pznSn6obQxEcuyqGuV5IyXzhmiSBLyBG10L8MLDOSUadKjqLmouQ8el7uLWyVlFLkpXTrfquD%2FPSyH60sMDhjIHlfMJ6m98kGOqUB0dxutAssSJXu3z03OdZ9WIjd71ZnBbH%2FIqfZ9taM93jI1ir2Yl2DxaCpH1w3kFf0IM2nWRp2qBlCsUpazUcP4k8Emo2L7lrq9h2fy98xNHPskaaQDhRKQ4iRv55km2kCv%2B1%2BqzwnxGAMH1gIMKfls5LrUFlPJg2I%2FlputfgSGPMC8CKtMDFWeC%2BQprFAighn69irjgS2QkjPCSVsrDr3MWAZgvLz&X-Amz-Signature=cd1d55f22509843902d4929e849577ed3d4a81181d82c74b70f18aaee70f15f9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
We can achieve that by running the following command:
```python
mapping_dict = {
		1 : 'Player One',
		3 : 'Player Three',
		5 : 'Player Five'
}

players_df.rename(mapper=mapping_dict, axis=0, inplace=True)
```
![players_df with new index labels](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/7717e680-7d76-46c6-8103-047a0ed4deb6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663RA4VSSA%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T220934Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIBQxHzSNuoiosDjrF4kUgRniU3v4DuSu4oh67PKb3dhfAiEA0MQsTQhhBmrldfeGcicPjH9heJKXZWCBoqssH6hGwroq%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDMPOC83wD2Nylb3iOCrcAxYahiyaajtpfYjXP8%2F5fK2LhvI82d7SAAR6QQZCbf%2BJqG7eS%2BPgqsu2bCm617%2Bp88aY%2B4O2bmT8Exki00nSnJJ6Gr488CW0xgnnAgFyRyB09%2Byv8LBlf1aUtGTTRMfGfKKPzjojJk7m0%2FvYOA71jZL5oyBUjLl0W22m65YVMx2%2FwG61IiikiRst5BLnMrNVhzJoY0Z%2FcVzet4caiXYAFY9sj4h28oEBpIkDWtdvRuSRJ4Q%2FzS50DP4zPDghdKvgAXYIf145xOu0UhwmyZWZCkk0E8ZUXlL4Fp%2FF6dpAxInHJ5brZDSeIkaAPbp8Ljp2NHfX3ZoZBm%2BUOxg9Q8Rhxol2eL9vsI5ylA27jUjKV5pqbfCAXzyxnq%2F2%2Fkw3SUNRG%2FKtGa3svN5%2B7JHJHdzU4nddOPpPTGjY3tqNkMxqg%2FKaT02N5XC4HGZBbfdeRv4E5eV7Z%2FH6aGcV%2Fu7Exjdqwtz%2F27WpEtGBHsxT3IB%2FGaYoQUHUF9JgVNS05P9SU5vDnPxbK4Bp3NlRzFhtGKywFCo8WmJ1puuKGN1pznSn6obQxEcuyqGuV5IyXzhmiSBLyBG10L8MLDOSUadKjqLmouQ8el7uLWyVlFLkpXTrfquD%2FPSyH60sMDhjIHlfMJ6m98kGOqUB0dxutAssSJXu3z03OdZ9WIjd71ZnBbH%2FIqfZ9taM93jI1ir2Yl2DxaCpH1w3kFf0IM2nWRp2qBlCsUpazUcP4k8Emo2L7lrq9h2fy98xNHPskaaQDhRKQ4iRv55km2kCv%2B1%2BqzwnxGAMH1gIMKfls5LrUFlPJg2I%2FlputfgSGPMC8CKtMDFWeC%2BQprFAighn69irjgS2QkjPCSVsrDr3MWAZgvLz&X-Amz-Signature=4a3ef560baf93b5e781a6c83af1df4bd966d24bf823158ae61e274aedb41b428&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
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
![outer_merge_df](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/c09b5108-a06d-464d-9777-48fd059e0031/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667S6GXX5M%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T220937Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJGMEQCIGUQM3g3BELJMste4fny0REPfYZA376J02nOQtRo4uM1AiAg%2BtQsPrjSDOMGK6%2BQfVayu4VXEafwYy40HnfUxd67pCr%2FAwgmEAAaDDYzNzQyMzE4MzgwNSIMXfVwWwNK5XFRTYrkKtwDEvCyTytWo3qOJuC62TzdNHHI2jtKTvCv3q4Dclky4NWPGn4h6C3L%2FsTp2aEmy6WQHnopLST9CnIgCYojAIP956XMmWhidhsrs%2BuqUAhH2RfruGabO8Y6ZbOnu0nEwD7BaJ6KGBlrrwPkLsdTGf35SERBAO58EJSOZXAJUyRnJ9naIWDkDz6PfKg%2BE9rJN5OMHVcnsl%2BWKSM6XtmDzSQIXedGxZHsLw9z%2FLM7jOR0TkrQ52jbQCWXCa%2BRqBXou23SObSEf0OHfIdY9aYAl00hU%2Fol%2FjnvGwvvHEAW7d%2F3IZfCkS1tYbJMtaUWCaXgkvkyV6o485fqqnLvsOBjLi3l49CcZEzrNbqa%2FpZRtqrkTYfRXCRMyI9KC0APbhSHfnLWE5Dy%2FwM6lUEsmoi96%2FRjVPREd8GEgBOxoLFE1nWPWBlfjqCxHLvnz3PaQ4Oxqe8RQ1vTCpnyFUpzxyo3ZvfgC8HcsCEqfumvvmIb%2B7dWQ1sMK86e7jOM4a091ogbx9ZPBjMrTRH7VDn9cbGKWBnVa9chTu%2B1Fn28fzl0WXzZd5ereUDeLcSETf2bzCK7U9PpQlkTyje0S9Bg%2FRE1pvKScnTAvI0P8MFyp4yzw0KkoyRVCmynIEFLqyPx6Z0w06X3yQY6pgGujFM%2B143aX4K%2F2uWpueTKuCJCrlRPj83l0%2FMaowQc0oeh8Om7YG0dZhscyXuQtCq3Makfx31XIFipUUHa%2FcEQJLjFw%2FKfek3uwlsdHXrJW8EcbdyKXKxZOnF3jarsZXzR2PB7IK1dzmpyRIqXhQt69Xw%2FFOtvtXz86yy5UTgkZdie7HVWw58EJRNc0yxtNciEGPldrLy6GuiFvZwlCh9v9ACDWBdU&X-Amz-Signature=5e16634237eb8a89500fe4d2495338bdfbb88897edc5c050355fede761485409&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
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
![outer_merge_df](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/c09b5108-a06d-464d-9777-48fd059e0031/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664DKKCFO6%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T220941Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJIMEYCIQCJnYD%2BLZCacNGk0tNhi28Htq8XM7xLtYnJbD5m2DsIvAIhAOIXXnRi9GzGUYqXKnfH17KJYovNRgSb1QYZB2664O3%2BKv8DCCYQABoMNjM3NDIzMTgzODA1IgzwrkXzBjX047Rfx3oq3AOYlQ4UGPvECRfI2kmaUaAemkyvBZH99OM7BhgVj2gSkI4FDF9xHIxteklBDRH1rAUryI1Y0V3CEPZuISOK9XCDJFct%2FZfj2tXJn6SVWDCK0UcagsE6bizHP%2BAG9HtZ55oNYyb5MYyyptACaXPSrzNTqHs6W4CB2iK1y9dS%2FmNyMH3mYHuVRpLU3ml541%2ByoTHnwF4PNGv7C7HMgqDTKC0%2FPxT6HWcdjUP0GOjNTIQzv18M%2BiIdQ1WeqedifL1zoT2bEdpd9m7YSCqAnUFFj%2BS3BijXNeHTyXDB9xWzLDUOma8Llfylmyd6bM8DCy%2FzfAIsG6LcAU%2FZ0hq8YDN87GIUN4ul6vZ5CFwP30gKqdCEwwSwIAHDvFFYU4hFBWR11MYE7Q8ojVtBwKZIyzgLcQ%2B7t%2Bk0yiBjaBjQX%2FoipUXkGBJ3ZVD2v%2Fp8LNCB%2FUq1cDtOOnE%2BfAXjoqMj7LKH7ufmKuFUOL4rpEItI4HHg670igtPSBu2C6rEwI7hVZ9qTTrCoKxBpabBCplyQ%2Bl%2BLR%2BMDUazZIIhdTcwngtfNe7wjInTDN2Dq20STk7jgztWl8iHAaMaT%2FF8Jg%2FJTgibYHafaq2jjM%2Fh4oZeBEEgqNY0f9SRDVHsfUXtM1EyWTDqpffJBjqkAcXhV%2FvhIGrrnhfQbB%2FBi80YzSSeyOrSyzyW3b2mTEO0u3u%2BX5JfqxShWRqx6AFihWn9p%2FJhutIhzOyH%2FlOMk%2FCZ6XoPmFuTLtFT1VtzPga4FDtXqJBeurOd5YIKakKmFRUoKLuUn%2BuVTV4TUczZdfq2UXaWyNgLemxNPuf0NUaZh89E8MUE0YdHeKSjIGuJrm1jlBAQDpaMKvAyLpAyOCb4OIdb&X-Amz-Signature=a1d0f6d530883b62f2c74ae7c285303504d6e9ee76252f4f0062b3c385328c41&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
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
![DataFrame is returned with the stats measures in the index and all columns with numeric data in `players_df` as columns](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/d744d39a-d451-4172-b2c3-42c4dea5c4c6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664WFI3RH2%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T220944Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJIMEYCIQCW4CptCbliW8IyrGmdFx6VXifjANogiSAwvZPilbncQwIhALsG3z0iEZauh9pLJq8iwzA%2FPyoSsbEs%2B7sgiphnoohJKv8DCCYQABoMNjM3NDIzMTgzODA1IgzWGiLK6vUagKVVwtoq3APjp8Pa71V0kNIIlQ9%2FTWHI9iVDzLJjhvVMs1lwDQbl8RBxX2iQQAo%2F4Ex9HUFo5fx9zpodAmevSQRRsjmbyPJrYDcCqmZ7W52DUbvGKjwpkUbtfpmRdCbHVefCs6YiA6X978sT6OwQDhzwb5AFx%2F6dH1hdctOQGBjHbboFtWynspKu2aS%2FENJDfOOWmoE8LZYQp4NlNQeK5%2F12utng%2BsPw7vuLQp1M6vfYHxwZgAtxuEvLu99SaXvoj%2FfjAFKV5PvhgVKJ1%2B7IeyfaFqj9tsnSO31MLlMtQSw5tV6%2BmVhDKjvYbbTex6LNwZAfBCXyt0SkT%2BBn7EZ84pagqksYBe3dgfVVOWsY%2BMWJKFslyDxTmvRAO2NFXZHg1CFVaDhTlLnBI7bk%2BjMErEH8f2TorEsouVPifPTfiYj3Cvo2%2BJaXESPMD%2B3q1AKVrkzZ88e0yO8UYLL1GSZi183g3cmd5NL6J0TiTvlEeMq42bDH2890GxZFvKaDvb2XaKwJhS7IPVroEJni4T4YzasJDWmxEt8D64L3U9F7cJvGUwDQh97zVVnuoKYOXVxIO%2BjIBbGwJBbUpwrJHf%2FjVRXpDxGdxMxKwvmeWf6ey7kwFSyMTviMltzjpclIQln0qNIaCTCspvfJBjqkARQuMtwfaaPCdI0ylgl8SfMxBGG5YEmkL58feIrYK1XE137t2mfI2XM9AVgonfVOICbNaOgDXRIhGz1VoRgCe8geoCCrI847o7ogQae0cuL6spZy3eBJhWUc%2FjNcu2UOJMAhB%2FySClX77jSoIbLw%2B289vGSwfvzpPPvm9Nb6BYguJtYefE%2F4nveplhgyB42KBStr33qIwtRtXfi4zaqGjDoS4keJ&X-Amz-Signature=4574c1f65fcb4457a119a0d9acc4f3629acbb71f1450f90a49fa3427d115d854&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
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
![Simple histogram that shows that the majority of players has achieved close to zero points](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/f2df9952-028a-4b16-acf5-4e33b3acb75c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46674KOEKC4%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T220945Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJGMEQCICAEGtcaca1s1lh0MAw0NLgLFB%2FC3NRXGpuYWeMribmoAiB5lspoCj3xVnL5Svcll%2F5%2BF9q7Zgsj01bvj4BYILTGnir%2FAwgmEAAaDDYzNzQyMzE4MzgwNSIMeEhu4XWb3V%2BuRB1%2BKtwDdh1P57vs62jVZLGQwC26ctyBn3j50mdyISLI9HlnRU7Jq%2FoLxMznDrCcLz7Lv5OpvbuPLxV3bnul3rv4oq9MlHYpIm%2FAP5bVRdnEIzx1iZ1Vkds2r%2BviVAGcQcydau9EC%2BLNYV59UuBNL4qy1Zd3nK5GzoYGgmVHW71YlzZnGjBU6JkzMWXuEijw4G0XmEsjEHhGuDVpvBa3rVJuTC7F7l%2F%2Fzu4GHl7fHtAnKqbJvTaNBhk5zKNCO1CG2MlNxUkB1TOPmAcF8p9dEUQukJMPclTqIiIA71lhaaV5xPzjn5UHM8662OLFxek%2FjIasxlc5iWD04Y3kOBBOA%2FcbNXtiNMgl2BQ7XQ6Pcz0sQpHY5zCOY6n6hpOadoRd23XS0D4qugyFciVY2VmZtKxUUkOu7ySp98mTICDeqPf59vOz5j2479fMUGmPoulVjwXlIWoFGufsJUOpzQ7tC2uvl3S2Fo%2FVqFIjXV1FMWj3CxyCbjKEkaeMi1pjH5YxSoXGqTL208V%2BtHjouAqANaVu8lYXfFV32Q0sXkIoFu1ZCSKu7jq9JwWyPlLSb3f2PniZ8N2pC48Rpngyxc2RTYb%2F7yhjeTOgO7eAH3Fvgw5cXWEh4ns6d9V8C1A8VhlK5jAw8KX3yQY6pgFVZQ2Fdgk7rLQEVAgi8yNKSqS61JQx481AtFZX7tWGCBRzClqsNz2tIKRsxoPaiftJfzg2cYRUaEYsqgDXc1xtySERWGxdCKgKrhRShom66w570L7dwEeM6ObiE5b9Q%2FiGWmheSVtHie3oO5TVIozgG8F4iqG5v6og39z07L4647sJaCBvAV%2BCbFaC16QCqao9GVps6rreg%2BfvIsmO2lS%2B2utNNgle&X-Amz-Signature=dc8bcb1d8e797e39a5e7cfe9cc98ee14298d23b05e1dfaf1527e5260e8d83204&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
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
![Unsorted players_df](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/ddbf4cb0-bf1f-491d-b50a-cda8910a5fee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YDADA4B4%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T220947Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJIMEYCIQCO%2BxCy9k2n%2Bd1cHJWb2qYHRQfekKloVWwTXo6whEQCtgIhAPKMHwiUjX6OKvuTKkCxLip%2Bp5Ycv5GFxOTvzt1N1571Kv8DCCYQABoMNjM3NDIzMTgzODA1Igy%2FwCgOLPcVzFVHX44q3AMaPd%2BVJ%2Bf5QVWh%2Fy%2Fjx7SD1HXfAcN8HFyx5TwJMBKzjIAOAPLZx7oW9kW0OjqWfaYJGp2go1mqvxKaaLyayva3WLqLizLKaVlVAOLjop1GWmdu2YeASm7DRpSNRNpL%2FR4XacEO1f9KoZHp%2F%2BLqEKUcREi1hx%2FuXveE0BUnrSSzgQEPDjkzeTjXsI%2Bu%2Bp616imEZMFxOpp%2FxWKmpe5U2f4cfvlr3MQx9EsXD1KTFZmoQsFBq8Ka8HhyU5kLe3aC07Fi%2B5YHho%2F2Q%2B4dkhQ36D0wJBwnAXU%2FaflPX6BF7YoE7yjqXDjc%2FbY2FYLQ%2FtvPkq1Cws06yv9WoDevG%2FkiMt67m6o7StE%2FUsQV3Gc5JEwnhzUIyl%2FK6x%2BhHmkmwZ3BtJJ0V3bEeA1Naw5whgSqKyVveupR0j1c%2FiNH9f0m%2BTnQqDGO2G5n5S7LtjLMNEmTB%2BZ8aveWYg2fBtdEGon0cv0NsK1FJFDDmhnMyl4tmSba4eTy2b%2FFUWgkcGFS88i1wojwP1Fa5nj9RMz%2FEB8wIimdM77tuWbDPcJMQHpTetmv8MJ1Xl%2FLH5xy2KMcD7TcZjKxFPtgo7R%2BbjsmNK6IfwFrmGjPHLwRlaUMR54jInq1gz5SIPimTNDqVaJq3DCrpvfJBjqkAeghEvhuukeoBhFxWbfeIgS%2Bx%2FeOhJFluymwaCX948b7VI4ugfZ6YJK1eK9TY%2BodgkCACssHBQtb4yiyrzsK5Ro2JDRItgCAKXdL%2B%2FTMlFUdJd3Gf2AKPuPiKU2ssVXcokCwogdXsofmWqONUn6%2Fu1Pcpec6G0qlkMTQbxIp9H8dPrtGMcIPcK%2BArCz7S%2BcFQedSIdf%2B%2F7B%2Fs4ZxDYTOruKzfjl5&X-Amz-Signature=1b0cde00313b7e64f89f7a73b98cce041aa7021854d2e1e03ba233e0914b5ff4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
We can now restore the correct order by sorting the DataFrame again:
```python
players_df.sort_index(inplace=True)
```
![Sorted players_df](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/efdd00d4-abfb-4ddb-887e-e03a6a2e2064/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YDADA4B4%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T220947Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJIMEYCIQCO%2BxCy9k2n%2Bd1cHJWb2qYHRQfekKloVWwTXo6whEQCtgIhAPKMHwiUjX6OKvuTKkCxLip%2Bp5Ycv5GFxOTvzt1N1571Kv8DCCYQABoMNjM3NDIzMTgzODA1Igy%2FwCgOLPcVzFVHX44q3AMaPd%2BVJ%2Bf5QVWh%2Fy%2Fjx7SD1HXfAcN8HFyx5TwJMBKzjIAOAPLZx7oW9kW0OjqWfaYJGp2go1mqvxKaaLyayva3WLqLizLKaVlVAOLjop1GWmdu2YeASm7DRpSNRNpL%2FR4XacEO1f9KoZHp%2F%2BLqEKUcREi1hx%2FuXveE0BUnrSSzgQEPDjkzeTjXsI%2Bu%2Bp616imEZMFxOpp%2FxWKmpe5U2f4cfvlr3MQx9EsXD1KTFZmoQsFBq8Ka8HhyU5kLe3aC07Fi%2B5YHho%2F2Q%2B4dkhQ36D0wJBwnAXU%2FaflPX6BF7YoE7yjqXDjc%2FbY2FYLQ%2FtvPkq1Cws06yv9WoDevG%2FkiMt67m6o7StE%2FUsQV3Gc5JEwnhzUIyl%2FK6x%2BhHmkmwZ3BtJJ0V3bEeA1Naw5whgSqKyVveupR0j1c%2FiNH9f0m%2BTnQqDGO2G5n5S7LtjLMNEmTB%2BZ8aveWYg2fBtdEGon0cv0NsK1FJFDDmhnMyl4tmSba4eTy2b%2FFUWgkcGFS88i1wojwP1Fa5nj9RMz%2FEB8wIimdM77tuWbDPcJMQHpTetmv8MJ1Xl%2FLH5xy2KMcD7TcZjKxFPtgo7R%2BbjsmNK6IfwFrmGjPHLwRlaUMR54jInq1gz5SIPimTNDqVaJq3DCrpvfJBjqkAeghEvhuukeoBhFxWbfeIgS%2Bx%2FeOhJFluymwaCX948b7VI4ugfZ6YJK1eK9TY%2BodgkCACssHBQtb4yiyrzsK5Ro2JDRItgCAKXdL%2B%2FTMlFUdJd3Gf2AKPuPiKU2ssVXcokCwogdXsofmWqONUn6%2Fu1Pcpec6G0qlkMTQbxIp9H8dPrtGMcIPcK%2BArCz7S%2BcFQedSIdf%2B%2F7B%2Fs4ZxDYTOruKzfjl5&X-Amz-Signature=5ad4c514634eccbbe513fd2f8576ab38d7dec925a41f3fccdac3e968bc89f87a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
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
![`players_df` sorted based on column `Assists` in descending order](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/b453e607-898f-4093-80d9-39f634fd6f61/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RFTB4NO4%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T220948Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIQC5rafry1dGPKiE90t363UTzlsm556US0Kf4uQEsMX1GwIgcNo5dx5GqbOL4dlw%2BE3EnKRFTJeW9mgrj7%2BQmB7GdL8q%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDNujcdxXC0A1CmmyXyrcA1iLAZ1kWQWiaAC7kN%2FRG2%2FQNaLAuGF2Hu9Suml3WZQLuvNVaeQKp0AppPJi8SXMxAQnQRLPR3sqiV8HDVhpwZ9SGtPflj9ASxaShJgt7oHsLSCoSAp8%2FnPDlTqm47OLfoveQ%2FjJdLrZyNro3HFi52LONuM4CuqmNKSWas12EwknP25WLNh6ts0VjMRMKYZdK4f22HnuYA1eUxWbxE1f9cmkthW2%2FVLZFmkpyAI2wzmArgUPm8zlBlQw4WQaXWQir1zt0RRgNBd9Azk6lvEVQ9%2B7kTMCJeSCneZ4M0vkeDbog4xWr6z9sNzcCSAcHbY2fO%2BsFXR82y%2FJpzS4i6Z5s5nXMEtePSwUxez99kD6onolO%2B7jJXrsrz6UZEri5FiO4cCnqkCioOO3rK3Ae%2FI6u%2FAnqsrww44tPasvizZy%2BiFZUZNIHqlfscR14%2FUpch%2Bfo%2F%2BuZaH6sXE4fHnIoWOxT4kIPpoNfSNEDJHZpDYzmlCQBwvNScrNRVSfnGwqKOX5tkBW8jLkcS46204za2oJTAE4ANEYsUtUAOidqg4HYz4lW1luDDUGDR6aHdrQF0WTefpUAs6eCDZXWlX700hCDR8M5e9kvleJC3f1zwvM82fbrTQtBbzCT19Hi%2FRcML2m98kGOqUBlJfTGSajykZMSIr7SHqfmispwKONh5CztJsmvOeNZ0HgprXTxfl8iCY2lAnN1gxGxU3qDq6hwt4u592Pa1aYkHb7QObFF297alBfKNyaj99Gp%2B6YfVNRBh%2FFQKGLvKCecy4PJA1oRTFSC4LgUXq2qfZbHXk4P4nvJVJ%2F7raONzX3TAD1WFyr2pJNqS8VvnohF47P%2F4xb1nMhqMcTlBBD84hi1rcQ&X-Amz-Signature=3c2e0017e9816c7609b34391761044fc845edf3053ed4bcbef6dcafd4ad7d33d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
In the code snippet we can see that we explicitly specified the `ascending=` parameter. This is necessary as per default `ascending=` is set to `True`, so if we want to sort in descending order, we need to set this parameter to `False`.
---
**Sort DataFrame based on multiple columns**
Let’s extend the previous example and sort the DataFrame first based on column Assists and then based on column Goals.
```python
players_df.sort_values(by=['Assists', 'Goals'], ascending=False, inplace=True)

players_df.head(10)
```
![`players_df` sorted based on column `Assists` and `Goals` in descending order](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/857b7752-594c-4f3f-ab41-99f60bea6a56/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RFTB4NO4%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T220948Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIQC5rafry1dGPKiE90t363UTzlsm556US0Kf4uQEsMX1GwIgcNo5dx5GqbOL4dlw%2BE3EnKRFTJeW9mgrj7%2BQmB7GdL8q%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDNujcdxXC0A1CmmyXyrcA1iLAZ1kWQWiaAC7kN%2FRG2%2FQNaLAuGF2Hu9Suml3WZQLuvNVaeQKp0AppPJi8SXMxAQnQRLPR3sqiV8HDVhpwZ9SGtPflj9ASxaShJgt7oHsLSCoSAp8%2FnPDlTqm47OLfoveQ%2FjJdLrZyNro3HFi52LONuM4CuqmNKSWas12EwknP25WLNh6ts0VjMRMKYZdK4f22HnuYA1eUxWbxE1f9cmkthW2%2FVLZFmkpyAI2wzmArgUPm8zlBlQw4WQaXWQir1zt0RRgNBd9Azk6lvEVQ9%2B7kTMCJeSCneZ4M0vkeDbog4xWr6z9sNzcCSAcHbY2fO%2BsFXR82y%2FJpzS4i6Z5s5nXMEtePSwUxez99kD6onolO%2B7jJXrsrz6UZEri5FiO4cCnqkCioOO3rK3Ae%2FI6u%2FAnqsrww44tPasvizZy%2BiFZUZNIHqlfscR14%2FUpch%2Bfo%2F%2BuZaH6sXE4fHnIoWOxT4kIPpoNfSNEDJHZpDYzmlCQBwvNScrNRVSfnGwqKOX5tkBW8jLkcS46204za2oJTAE4ANEYsUtUAOidqg4HYz4lW1luDDUGDR6aHdrQF0WTefpUAs6eCDZXWlX700hCDR8M5e9kvleJC3f1zwvM82fbrTQtBbzCT19Hi%2FRcML2m98kGOqUBlJfTGSajykZMSIr7SHqfmispwKONh5CztJsmvOeNZ0HgprXTxfl8iCY2lAnN1gxGxU3qDq6hwt4u592Pa1aYkHb7QObFF297alBfKNyaj99Gp%2B6YfVNRBh%2FFQKGLvKCecy4PJA1oRTFSC4LgUXq2qfZbHXk4P4nvJVJ%2F7raONzX3TAD1WFyr2pJNqS8VvnohF47P%2F4xb1nMhqMcTlBBD84hi1rcQ&X-Amz-Signature=616a0861e7a38fabb596d875a32f2212dccfcaf1b2b962968f4901d4cc94803f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
We looking at the top 10 rows in the DataFrame we can see that the sorting worked. Three players have 10 assists, but one player has more goals than the other two, thus the player Mohamed Sala Ghaly is displayed correctly before the other two players with 10 assists. 
We can also see in the code snippet that we can simply extended the list that we pass as `by=` parameter value with another column name.
---
**Sort DataFrame based on column containing text**
Let’s assume we have the following DataFrame `players_df_new`.
![players_df_new](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/59998ff6-4439-4f6e-8d92-b267731f85cf/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RFTB4NO4%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T220948Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIQC5rafry1dGPKiE90t363UTzlsm556US0Kf4uQEsMX1GwIgcNo5dx5GqbOL4dlw%2BE3EnKRFTJeW9mgrj7%2BQmB7GdL8q%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDNujcdxXC0A1CmmyXyrcA1iLAZ1kWQWiaAC7kN%2FRG2%2FQNaLAuGF2Hu9Suml3WZQLuvNVaeQKp0AppPJi8SXMxAQnQRLPR3sqiV8HDVhpwZ9SGtPflj9ASxaShJgt7oHsLSCoSAp8%2FnPDlTqm47OLfoveQ%2FjJdLrZyNro3HFi52LONuM4CuqmNKSWas12EwknP25WLNh6ts0VjMRMKYZdK4f22HnuYA1eUxWbxE1f9cmkthW2%2FVLZFmkpyAI2wzmArgUPm8zlBlQw4WQaXWQir1zt0RRgNBd9Azk6lvEVQ9%2B7kTMCJeSCneZ4M0vkeDbog4xWr6z9sNzcCSAcHbY2fO%2BsFXR82y%2FJpzS4i6Z5s5nXMEtePSwUxez99kD6onolO%2B7jJXrsrz6UZEri5FiO4cCnqkCioOO3rK3Ae%2FI6u%2FAnqsrww44tPasvizZy%2BiFZUZNIHqlfscR14%2FUpch%2Bfo%2F%2BuZaH6sXE4fHnIoWOxT4kIPpoNfSNEDJHZpDYzmlCQBwvNScrNRVSfnGwqKOX5tkBW8jLkcS46204za2oJTAE4ANEYsUtUAOidqg4HYz4lW1luDDUGDR6aHdrQF0WTefpUAs6eCDZXWlX700hCDR8M5e9kvleJC3f1zwvM82fbrTQtBbzCT19Hi%2FRcML2m98kGOqUBlJfTGSajykZMSIr7SHqfmispwKONh5CztJsmvOeNZ0HgprXTxfl8iCY2lAnN1gxGxU3qDq6hwt4u592Pa1aYkHb7QObFF297alBfKNyaj99Gp%2B6YfVNRBh%2FFQKGLvKCecy4PJA1oRTFSC4LgUXq2qfZbHXk4P4nvJVJ%2F7raONzX3TAD1WFyr2pJNqS8VvnohF47P%2F4xb1nMhqMcTlBBD84hi1rcQ&X-Amz-Signature=b68981d066854bb705a5ec8ba2ed8db6496b20f5f83b887ddf08e8390b4b796b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
As we can see the column `Player` includes the player names. Sometimes the name of the player is written in lower letters.
Let’s sort the DataFrame based on the column `Player`.
```python
players_df_new.sort_values('Player', inplace=True)
```
![players_df_new sorted incorrectly](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/c0c0379f-1513-4eba-a177-4213fdaf1436/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RFTB4NO4%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T220948Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIQC5rafry1dGPKiE90t363UTzlsm556US0Kf4uQEsMX1GwIgcNo5dx5GqbOL4dlw%2BE3EnKRFTJeW9mgrj7%2BQmB7GdL8q%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDNujcdxXC0A1CmmyXyrcA1iLAZ1kWQWiaAC7kN%2FRG2%2FQNaLAuGF2Hu9Suml3WZQLuvNVaeQKp0AppPJi8SXMxAQnQRLPR3sqiV8HDVhpwZ9SGtPflj9ASxaShJgt7oHsLSCoSAp8%2FnPDlTqm47OLfoveQ%2FjJdLrZyNro3HFi52LONuM4CuqmNKSWas12EwknP25WLNh6ts0VjMRMKYZdK4f22HnuYA1eUxWbxE1f9cmkthW2%2FVLZFmkpyAI2wzmArgUPm8zlBlQw4WQaXWQir1zt0RRgNBd9Azk6lvEVQ9%2B7kTMCJeSCneZ4M0vkeDbog4xWr6z9sNzcCSAcHbY2fO%2BsFXR82y%2FJpzS4i6Z5s5nXMEtePSwUxez99kD6onolO%2B7jJXrsrz6UZEri5FiO4cCnqkCioOO3rK3Ae%2FI6u%2FAnqsrww44tPasvizZy%2BiFZUZNIHqlfscR14%2FUpch%2Bfo%2F%2BuZaH6sXE4fHnIoWOxT4kIPpoNfSNEDJHZpDYzmlCQBwvNScrNRVSfnGwqKOX5tkBW8jLkcS46204za2oJTAE4ANEYsUtUAOidqg4HYz4lW1luDDUGDR6aHdrQF0WTefpUAs6eCDZXWlX700hCDR8M5e9kvleJC3f1zwvM82fbrTQtBbzCT19Hi%2FRcML2m98kGOqUBlJfTGSajykZMSIr7SHqfmispwKONh5CztJsmvOeNZ0HgprXTxfl8iCY2lAnN1gxGxU3qDq6hwt4u592Pa1aYkHb7QObFF297alBfKNyaj99Gp%2B6YfVNRBh%2FFQKGLvKCecy4PJA1oRTFSC4LgUXq2qfZbHXk4P4nvJVJ%2F7raONzX3TAD1WFyr2pJNqS8VvnohF47P%2F4xb1nMhqMcTlBBD84hi1rcQ&X-Amz-Signature=c3c32c6fda97d661b9aed1612a62362f74a19653542cf7bcd6cd970cd92cdc76&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
We can see now that the player Sadio Mané is displayed before the player harry kane although the letter S comes after letter H in the alphabet. This is because the `.sort_values()` method is case-sensitive and goes from A, B, … Z first and only then starts with a, b, … z, i.e., with the lower letters.
For this reason we must provide a `key=` parameter and a `lambda` function as value which transforms all the values in column Player to lower letters before the actual sorting is done. 
```python
players_df_new.sort_values('Player', key=lambda x:x.lower(), inplace=True)
```
![players_df_new sorted correctly](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/2831e596-6fd1-47ec-93e3-e19fea8667ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RFTB4NO4%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T220948Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIQC5rafry1dGPKiE90t363UTzlsm556US0Kf4uQEsMX1GwIgcNo5dx5GqbOL4dlw%2BE3EnKRFTJeW9mgrj7%2BQmB7GdL8q%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDNujcdxXC0A1CmmyXyrcA1iLAZ1kWQWiaAC7kN%2FRG2%2FQNaLAuGF2Hu9Suml3WZQLuvNVaeQKp0AppPJi8SXMxAQnQRLPR3sqiV8HDVhpwZ9SGtPflj9ASxaShJgt7oHsLSCoSAp8%2FnPDlTqm47OLfoveQ%2FjJdLrZyNro3HFi52LONuM4CuqmNKSWas12EwknP25WLNh6ts0VjMRMKYZdK4f22HnuYA1eUxWbxE1f9cmkthW2%2FVLZFmkpyAI2wzmArgUPm8zlBlQw4WQaXWQir1zt0RRgNBd9Azk6lvEVQ9%2B7kTMCJeSCneZ4M0vkeDbog4xWr6z9sNzcCSAcHbY2fO%2BsFXR82y%2FJpzS4i6Z5s5nXMEtePSwUxez99kD6onolO%2B7jJXrsrz6UZEri5FiO4cCnqkCioOO3rK3Ae%2FI6u%2FAnqsrww44tPasvizZy%2BiFZUZNIHqlfscR14%2FUpch%2Bfo%2F%2BuZaH6sXE4fHnIoWOxT4kIPpoNfSNEDJHZpDYzmlCQBwvNScrNRVSfnGwqKOX5tkBW8jLkcS46204za2oJTAE4ANEYsUtUAOidqg4HYz4lW1luDDUGDR6aHdrQF0WTefpUAs6eCDZXWlX700hCDR8M5e9kvleJC3f1zwvM82fbrTQtBbzCT19Hi%2FRcML2m98kGOqUBlJfTGSajykZMSIr7SHqfmispwKONh5CztJsmvOeNZ0HgprXTxfl8iCY2lAnN1gxGxU3qDq6hwt4u592Pa1aYkHb7QObFF297alBfKNyaj99Gp%2B6YfVNRBh%2FFQKGLvKCecy4PJA1oRTFSC4LgUXq2qfZbHXk4P4nvJVJ%2F7raONzX3TAD1WFyr2pJNqS8VvnohF47P%2F4xb1nMhqMcTlBBD84hi1rcQ&X-Amz-Signature=227f368e9998ead67108f3cd6b909fcdf9e716efe503d5063ac2e45e013e13c7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
---
## [`.T`](https://pandas.pydata.org/pandas-docs/version/0.25.0/reference/api/pandas.DataFrame.T.html)
---
**Syntax**
This attribute allows us to transpose a DataFrame.
`df.T`
Transpose simply exchanges rows with column. This means that each index label becomes a column and each column stands now in the index of the DataFrame.
![[Simple example](https://www.w3resource.com/pandas/dataframe/dataframe-transpose.php) of how transpose work](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/8a8c29ad-29e1-4d93-8b7f-d11607362931/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V4CVIKX3%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T220949Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJIMEYCIQCejYa6%2BStzvhZZ8zWtYVCdGLy2xU4cH%2BxcyPx%2BJEnrowIhAO34dlM3gJ1RqUX2ULEPZkVyIORa%2FpcnCsiV6%2FZR%2BS2JKv8DCCYQABoMNjM3NDIzMTgzODA1IgxUBnoXZwc45jVcWLkq3AMBNHBLhU6mfHO%2F4yYcylTfuYzQPwBfCTJHvRk8K7HXm7UhOE9WjZc1XzXSHIpm5Aj36FoKdl4tGvWQaIuCy6ruAdxd%2BR7O19yGdBhyXxwx%2BbeU566HEUoVss4teZkw2%2BWtEieXnXhJ4Xqwh%2FfGymrJwLgl1q7vbMksD47rwoDVLN1jJGDPHpnQOIj1JnZnqHCSYdaHwvy7fccH6MIvk9B0adKCOvriwtRsw0UslifH135TpwYeNTm9y2UMrK0%2BjATgmF84vwX2vJzBk8a4oNB0QCCXesJDyszoqCesrteH0m%2BTSaIT1ZgP522txNmAw7rn6ACvGZrmq20dWrQkxKTeuniv7eG96OU5mqjwTwp2HI%2FOzIpw3PFye24hGt6kxvBA31JO5zLB8Lm%2FMr%2FfUF2w%2FkxKz%2BCTvbocFD5RybHVVN4hj4eWkq1l9ng23eOZdh4LtKTfCX33W5eCrUDXVk630Ey1AsMEReDXEIBu7VRNUCWE0hyWWAnbNzcGpw9mmNZPhNoC90XTj98WwMhCBg7Y5RH4ndwTP87dh1WkqBGkBB4lGLkDx0HZ2Lp8xUsl8RnltnwbtLFef0qn5l785fnC1Tc8wAaKa63nXh9S995QEW044kwUHxZZ2sIC0jDfpvfJBjqkAayRLur5%2FlxAn7sOOfHt0Jl6QUWqrdq%2Bh%2BZWstR%2FMG5cwEHl5Z4VzCAwjXYIeMGEHc1HB6oUWaS1K3Z3UcmtkTVrwVHMBljHps0d3UV73Wvsboqp4%2F1gn4T39NkAHLUndY5EImNc9Ykf8WdkqV2AKvSTSQL7rwULlrJvNKyx7CycH6N8tV69poI%2BLKTrYjs2SEwTNZNFDwBzMM0zOgWs%2F2ZzpSOR&X-Amz-Signature=dbc4b468319d184d36d74412fcd80c47dbca97ee6500b1959d113cee013e8a78&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
---
**Transposing a DataFrame**
Let’s transpose the DataFrame `outer_merge_df`.
```python
palyers_df.T
```
![Transposed DataFrame `players_df`](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/89702bec-4246-4790-9f9c-f88c8d756671/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V4CVIKX3%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T220949Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJIMEYCIQCejYa6%2BStzvhZZ8zWtYVCdGLy2xU4cH%2BxcyPx%2BJEnrowIhAO34dlM3gJ1RqUX2ULEPZkVyIORa%2FpcnCsiV6%2FZR%2BS2JKv8DCCYQABoMNjM3NDIzMTgzODA1IgxUBnoXZwc45jVcWLkq3AMBNHBLhU6mfHO%2F4yYcylTfuYzQPwBfCTJHvRk8K7HXm7UhOE9WjZc1XzXSHIpm5Aj36FoKdl4tGvWQaIuCy6ruAdxd%2BR7O19yGdBhyXxwx%2BbeU566HEUoVss4teZkw2%2BWtEieXnXhJ4Xqwh%2FfGymrJwLgl1q7vbMksD47rwoDVLN1jJGDPHpnQOIj1JnZnqHCSYdaHwvy7fccH6MIvk9B0adKCOvriwtRsw0UslifH135TpwYeNTm9y2UMrK0%2BjATgmF84vwX2vJzBk8a4oNB0QCCXesJDyszoqCesrteH0m%2BTSaIT1ZgP522txNmAw7rn6ACvGZrmq20dWrQkxKTeuniv7eG96OU5mqjwTwp2HI%2FOzIpw3PFye24hGt6kxvBA31JO5zLB8Lm%2FMr%2FfUF2w%2FkxKz%2BCTvbocFD5RybHVVN4hj4eWkq1l9ng23eOZdh4LtKTfCX33W5eCrUDXVk630Ey1AsMEReDXEIBu7VRNUCWE0hyWWAnbNzcGpw9mmNZPhNoC90XTj98WwMhCBg7Y5RH4ndwTP87dh1WkqBGkBB4lGLkDx0HZ2Lp8xUsl8RnltnwbtLFef0qn5l785fnC1Tc8wAaKa63nXh9S995QEW044kwUHxZZ2sIC0jDfpvfJBjqkAayRLur5%2FlxAn7sOOfHt0Jl6QUWqrdq%2Bh%2BZWstR%2FMG5cwEHl5Z4VzCAwjXYIeMGEHc1HB6oUWaS1K3Z3UcmtkTVrwVHMBljHps0d3UV73Wvsboqp4%2F1gn4T39NkAHLUndY5EImNc9Ykf8WdkqV2AKvSTSQL7rwULlrJvNKyx7CycH6N8tV69poI%2BLKTrYjs2SEwTNZNFDwBzMM0zOgWs%2F2ZzpSOR&X-Amz-Signature=6781df8fde2060c1c96a9d0c3e948d43c5fb620e920a51148392c7b7f6cdb2e5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
We see that the DataFrame has now only 9 rows but 540 columns. This is because there are 540 players in the dataset and as we transposed the DataFrame all these players became now columns.
---
## [**`.pivot()`**](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.pivot.html)
---
**Syntax**
This function allows us to re-organise and summarise the data in a DataFrame and thus view it from a different perspective.
`df.pivot( << index >> , << column >> , << values >> )`
The parameters of the .pivot() function are very intuitive, we basically just need to tell Pandas what values should be put where in the pivoted DataFrame.
![Structure of pivoted DataFrame](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/ce3fbd7a-7ed0-4aca-813b-7b876b8a9341/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZOVHUDJO%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T220951Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIQC74RnR861lvJoYwCW4KHqzogV1XdUVzpkvX9h3TomL2gIgZZOB19CIbV1zOnOVUT%2FhCkHapN6xkgUnK%2FqRxlyWaKcq%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDJy%2BTx4glcvuQE7VBSrcA8uQhe%2BYkfJ%2Bd5ILEiI1gSPJtzKnvWZUrfgQasah86gWSkCidUHL%2FPi7l0DBRwW86xIAUsl9RN3DSd4lWrI1El7Cp%2FQWo3UgC4ThNVx86i8rsA39Wry14%2BGKNR2SCb%2BDk2Sv4KEYyu6z3%2FpmgLMrDCYE9pz%2Bp9FjF8dmVz%2FvzpJXKOpkXVjWnJtmHrwgjDmu5mZJ%2F%2BPdpNzXdzaNQK5lVSrICpCu%2FbB0vmJ1CrPDRGpJxeRec90d2VCMdnkUFW14K0Ye7CgNvOnEDOj5ZHbjD0D1Kr%2BLM7XrFj%2ByU8hejPuRIAMxpQCA2oNR4lgHBFftpnOnKNI9f3Ve2keylfQ65wKB3LajLfz0UYjLQ1FYeLi%2FiD%2F7G5Fmo%2BWJ2xB7KaASUkuP0Fx0SYcgrSGuKj190Dq4vRGEGSbkf0aCjubjs9k%2BYvNX1REwfd8v6kC98UbakvEPWUfi4RMbBSrGeEjtxE1Mdo%2FGNN9IWAqel%2FTlpxIlCNljVnk%2FQ1nDoN6vFi3cxlZkqmAtqpy9Y2SAnT8uA%2F0ebisygRqD2czQEX4Bd72l0GO8cxCUtLCrnf5kSM3qa8ANX2gwmW9iOAdOWNJ2skSsOiKTkKXXUbhaClWH2zl401t3Qkg4VYmUFQhKMKGm98kGOqUBNrGDkdsCA8qIN1FluvGAXGbKke5PmLTBZiPY8YjSnAPdIg2fWHIsfyIuw8rp7ZyHTxfEtYsM8%2FTAxZeu0mcjybQEVEayXUhCZ7S0rDN49GLXeYbh7AVpl4l9xMDXLLIymADLW22QF5gkGzkdj7Y0gj7rrgL6RU9qRFkov6JQucVStcr3KHwtKTs62G7icmeh0nsw%2B1wGCaU%2FFThpuHmU0F2VSc5e&X-Amz-Signature=ace840ce7fc535c26db199eb73517a6925c51c3dfc49baf1ae4a275534ac6bca&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
---
**Create simple pivot table**
Assume that we sliced the 10 players with most goals from `players_df`, which gives us the following DataFrame `players_df_top10`.
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/3662a662-2783-4f3c-b27d-bafa37d5e277/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZOVHUDJO%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T220951Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIQC74RnR861lvJoYwCW4KHqzogV1XdUVzpkvX9h3TomL2gIgZZOB19CIbV1zOnOVUT%2FhCkHapN6xkgUnK%2FqRxlyWaKcq%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDJy%2BTx4glcvuQE7VBSrcA8uQhe%2BYkfJ%2Bd5ILEiI1gSPJtzKnvWZUrfgQasah86gWSkCidUHL%2FPi7l0DBRwW86xIAUsl9RN3DSd4lWrI1El7Cp%2FQWo3UgC4ThNVx86i8rsA39Wry14%2BGKNR2SCb%2BDk2Sv4KEYyu6z3%2FpmgLMrDCYE9pz%2Bp9FjF8dmVz%2FvzpJXKOpkXVjWnJtmHrwgjDmu5mZJ%2F%2BPdpNzXdzaNQK5lVSrICpCu%2FbB0vmJ1CrPDRGpJxeRec90d2VCMdnkUFW14K0Ye7CgNvOnEDOj5ZHbjD0D1Kr%2BLM7XrFj%2ByU8hejPuRIAMxpQCA2oNR4lgHBFftpnOnKNI9f3Ve2keylfQ65wKB3LajLfz0UYjLQ1FYeLi%2FiD%2F7G5Fmo%2BWJ2xB7KaASUkuP0Fx0SYcgrSGuKj190Dq4vRGEGSbkf0aCjubjs9k%2BYvNX1REwfd8v6kC98UbakvEPWUfi4RMbBSrGeEjtxE1Mdo%2FGNN9IWAqel%2FTlpxIlCNljVnk%2FQ1nDoN6vFi3cxlZkqmAtqpy9Y2SAnT8uA%2F0ebisygRqD2czQEX4Bd72l0GO8cxCUtLCrnf5kSM3qa8ANX2gwmW9iOAdOWNJ2skSsOiKTkKXXUbhaClWH2zl401t3Qkg4VYmUFQhKMKGm98kGOqUBNrGDkdsCA8qIN1FluvGAXGbKke5PmLTBZiPY8YjSnAPdIg2fWHIsfyIuw8rp7ZyHTxfEtYsM8%2FTAxZeu0mcjybQEVEayXUhCZ7S0rDN49GLXeYbh7AVpl4l9xMDXLLIymADLW22QF5gkGzkdj7Y0gj7rrgL6RU9qRFkov6JQucVStcr3KHwtKTs62G7icmeh0nsw%2B1wGCaU%2FFThpuHmU0F2VSc5e&X-Amz-Signature=1e21d4d109df01d5dd40cd5d83ee7ae5d54eaaba407a24c8cb65641d07d047ba&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
Now we want to analyse the Goals and Assists of these players in more detail. We can thus create a pivot table to summarise the data in these columns more efficiently. Specifically, we define that the player name should stand in the Index, the number of goals as columns and the number of assists should be the actual values in the table. We can execute the following command. 
```python
players_df_top10.pivot('Player', 'Goals', 'Assists')
```
![Pivoted DataFrame with NaN values](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/59679060-a9fd-444c-b16c-d3fec05c116b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZOVHUDJO%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T220951Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIQC74RnR861lvJoYwCW4KHqzogV1XdUVzpkvX9h3TomL2gIgZZOB19CIbV1zOnOVUT%2FhCkHapN6xkgUnK%2FqRxlyWaKcq%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDJy%2BTx4glcvuQE7VBSrcA8uQhe%2BYkfJ%2Bd5ILEiI1gSPJtzKnvWZUrfgQasah86gWSkCidUHL%2FPi7l0DBRwW86xIAUsl9RN3DSd4lWrI1El7Cp%2FQWo3UgC4ThNVx86i8rsA39Wry14%2BGKNR2SCb%2BDk2Sv4KEYyu6z3%2FpmgLMrDCYE9pz%2Bp9FjF8dmVz%2FvzpJXKOpkXVjWnJtmHrwgjDmu5mZJ%2F%2BPdpNzXdzaNQK5lVSrICpCu%2FbB0vmJ1CrPDRGpJxeRec90d2VCMdnkUFW14K0Ye7CgNvOnEDOj5ZHbjD0D1Kr%2BLM7XrFj%2ByU8hejPuRIAMxpQCA2oNR4lgHBFftpnOnKNI9f3Ve2keylfQ65wKB3LajLfz0UYjLQ1FYeLi%2FiD%2F7G5Fmo%2BWJ2xB7KaASUkuP0Fx0SYcgrSGuKj190Dq4vRGEGSbkf0aCjubjs9k%2BYvNX1REwfd8v6kC98UbakvEPWUfi4RMbBSrGeEjtxE1Mdo%2FGNN9IWAqel%2FTlpxIlCNljVnk%2FQ1nDoN6vFi3cxlZkqmAtqpy9Y2SAnT8uA%2F0ebisygRqD2czQEX4Bd72l0GO8cxCUtLCrnf5kSM3qa8ANX2gwmW9iOAdOWNJ2skSsOiKTkKXXUbhaClWH2zl401t3Qkg4VYmUFQhKMKGm98kGOqUBNrGDkdsCA8qIN1FluvGAXGbKke5PmLTBZiPY8YjSnAPdIg2fWHIsfyIuw8rp7ZyHTxfEtYsM8%2FTAxZeu0mcjybQEVEayXUhCZ7S0rDN49GLXeYbh7AVpl4l9xMDXLLIymADLW22QF5gkGzkdj7Y0gj7rrgL6RU9qRFkov6JQucVStcr3KHwtKTs62G7icmeh0nsw%2B1wGCaU%2FFThpuHmU0F2VSc5e&X-Amz-Signature=4271c330b1f75a311e38a64735bd5b0bb40bf65487c9b7dd56b534ff6d6c3637&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
From the output we can read now easily for each player how many goals and assists they have achieved, only if there would’t be these disturbing `NaN` values. We can get rid of those using the [`fillna()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.fillna.html) function.
```python
players_df_top10.pivot('Player', 'Goals', 'Assists').fillna('')
```
![Pivoted DataFrame without NaN values](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/2d52b792-ba61-4b0d-8ed5-5d7498041672/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZOVHUDJO%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T220950Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIQC74RnR861lvJoYwCW4KHqzogV1XdUVzpkvX9h3TomL2gIgZZOB19CIbV1zOnOVUT%2FhCkHapN6xkgUnK%2FqRxlyWaKcq%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDJy%2BTx4glcvuQE7VBSrcA8uQhe%2BYkfJ%2Bd5ILEiI1gSPJtzKnvWZUrfgQasah86gWSkCidUHL%2FPi7l0DBRwW86xIAUsl9RN3DSd4lWrI1El7Cp%2FQWo3UgC4ThNVx86i8rsA39Wry14%2BGKNR2SCb%2BDk2Sv4KEYyu6z3%2FpmgLMrDCYE9pz%2Bp9FjF8dmVz%2FvzpJXKOpkXVjWnJtmHrwgjDmu5mZJ%2F%2BPdpNzXdzaNQK5lVSrICpCu%2FbB0vmJ1CrPDRGpJxeRec90d2VCMdnkUFW14K0Ye7CgNvOnEDOj5ZHbjD0D1Kr%2BLM7XrFj%2ByU8hejPuRIAMxpQCA2oNR4lgHBFftpnOnKNI9f3Ve2keylfQ65wKB3LajLfz0UYjLQ1FYeLi%2FiD%2F7G5Fmo%2BWJ2xB7KaASUkuP0Fx0SYcgrSGuKj190Dq4vRGEGSbkf0aCjubjs9k%2BYvNX1REwfd8v6kC98UbakvEPWUfi4RMbBSrGeEjtxE1Mdo%2FGNN9IWAqel%2FTlpxIlCNljVnk%2FQ1nDoN6vFi3cxlZkqmAtqpy9Y2SAnT8uA%2F0ebisygRqD2czQEX4Bd72l0GO8cxCUtLCrnf5kSM3qa8ANX2gwmW9iOAdOWNJ2skSsOiKTkKXXUbhaClWH2zl401t3Qkg4VYmUFQhKMKGm98kGOqUBNrGDkdsCA8qIN1FluvGAXGbKke5PmLTBZiPY8YjSnAPdIg2fWHIsfyIuw8rp7ZyHTxfEtYsM8%2FTAxZeu0mcjybQEVEayXUhCZ7S0rDN49GLXeYbh7AVpl4l9xMDXLLIymADLW22QF5gkGzkdj7Y0gj7rrgL6RU9qRFkov6JQucVStcr3KHwtKTs62G7icmeh0nsw%2B1wGCaU%2FFThpuHmU0F2VSc5e&X-Amz-Signature=958ba5a3ce79e6b255b9ed7e97415c52e318b459a7cd61702e5ddd194956efc9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
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
![Four players have the same umber of assists which causes problem when trying to create a pivot with Assists in the index](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/ad30fa93-727a-4e0f-9a2d-32466cefc3a3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZOVHUDJO%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T220951Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIQC74RnR861lvJoYwCW4KHqzogV1XdUVzpkvX9h3TomL2gIgZZOB19CIbV1zOnOVUT%2FhCkHapN6xkgUnK%2FqRxlyWaKcq%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDJy%2BTx4glcvuQE7VBSrcA8uQhe%2BYkfJ%2Bd5ILEiI1gSPJtzKnvWZUrfgQasah86gWSkCidUHL%2FPi7l0DBRwW86xIAUsl9RN3DSd4lWrI1El7Cp%2FQWo3UgC4ThNVx86i8rsA39Wry14%2BGKNR2SCb%2BDk2Sv4KEYyu6z3%2FpmgLMrDCYE9pz%2Bp9FjF8dmVz%2FvzpJXKOpkXVjWnJtmHrwgjDmu5mZJ%2F%2BPdpNzXdzaNQK5lVSrICpCu%2FbB0vmJ1CrPDRGpJxeRec90d2VCMdnkUFW14K0Ye7CgNvOnEDOj5ZHbjD0D1Kr%2BLM7XrFj%2ByU8hejPuRIAMxpQCA2oNR4lgHBFftpnOnKNI9f3Ve2keylfQ65wKB3LajLfz0UYjLQ1FYeLi%2FiD%2F7G5Fmo%2BWJ2xB7KaASUkuP0Fx0SYcgrSGuKj190Dq4vRGEGSbkf0aCjubjs9k%2BYvNX1REwfd8v6kC98UbakvEPWUfi4RMbBSrGeEjtxE1Mdo%2FGNN9IWAqel%2FTlpxIlCNljVnk%2FQ1nDoN6vFi3cxlZkqmAtqpy9Y2SAnT8uA%2F0ebisygRqD2czQEX4Bd72l0GO8cxCUtLCrnf5kSM3qa8ANX2gwmW9iOAdOWNJ2skSsOiKTkKXXUbhaClWH2zl401t3Qkg4VYmUFQhKMKGm98kGOqUBNrGDkdsCA8qIN1FluvGAXGbKke5PmLTBZiPY8YjSnAPdIg2fWHIsfyIuw8rp7ZyHTxfEtYsM8%2FTAxZeu0mcjybQEVEayXUhCZ7S0rDN49GLXeYbh7AVpl4l9xMDXLLIymADLW22QF5gkGzkdj7Y0gj7rrgL6RU9qRFkov6JQucVStcr3KHwtKTs62G7icmeh0nsw%2B1wGCaU%2FFThpuHmU0F2VSc5e&X-Amz-Signature=6ad319a571e6912329590dec5e17b827186e900fe4b1252e103c66d03542112c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
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
![Melted DataFrame with Player as identifier variable and Games played as value variable.](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/376279f1-3a8f-4131-b498-cada89cf6c52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YZXB4CVX%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T220953Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIEBMvXNm%2Fwh4LOJSJPxxFImkArJH0OwIfmWpKUrRpmjtAiEA3uk2zMAyGyjihNrQHKe6auS9eIc9qS%2FYhioVnDFABU0q%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDOtrWrUhAhmU6AMCcSrcAw0bUG3IixweJrZM4NE4pvsi5f6kmxFUCJPM%2BSpEV4YEAhB8PB3pLmFNddcXEYKCJxdwcTCNEYcx06fpAs9dEeM3m0wU%2BDJy4YD0R9Ji5C24VKBToMyejeFWlJJW6G53T%2FUdWCBwj%2B3AZvJDfKt5mDaNzPK72KlXHaPitB%2Fqkmkx4JezBT5CAV09W7r68tWg1KEg9drj2GPLbFe8iVRITVTLhLiGo1t3yGDYVEtjfZp298EmM4WP1hhRg1H5Y3lXflJmPH0B8UyT%2FV0oMFgNUf7SbmD3kpg9%2FWFJvEDPW9z92HjOzFQEMv8P67CyhW3ECICu9socIGihOlFuV%2BfJ9QWDxyhgF7FjAwHx03jFtj6P9jZnG5L4Aa3GU1rfxYscP%2FRcrQnJmE%2FYPzDRl%2FbYK%2Bk5giDbqyvdlYonWPmJ7Dk%2BJpKKVozG85obp1J23qQXh6%2FJeGB0OCs1V3BPuU2Sh21tGI6kBf9CDh5DEtXto4ZseBoUXBjqJ03DuMvwGu3G%2FOTn4b6Ojps2qkTuZzc%2BfWVFFiUx7IfAnLASFWNGdkVANmckesyI0re8isYNukYiDrn0CxWv1BRoa4UODK5HBcypjZ4%2FoBIzHLRB2ew5fKdnlPpQ4V7RigR60Rq8MJ2m98kGOqUBnVzR%2Bxd4JY7zvIYFLD1nVVcDtc64fOZJ6ppMrUK5hrUtjx%2FHfj4GT6V7yvzW%2FWLUk7yUIO%2FKru2ilWU%2BFidwcIWDOu4gpZIp%2FFmoiadtg3E09KidZ%2Bb%2FX3BRytMd8KqkEeo0UiicmflavSOOkzUo0yJlLfzJ2tmTUkGiXY4LFBUspQXLx9k7bi11g%2FjKzFCfX%2F2hENrj31XQhisMXN52%2BzKY40Bk&X-Amz-Signature=0f8fd47ba6ba942f3d530f0fb3aa1ba888e35abbabc4eb563bb08ca4ef13778a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
We can see that the column label `'Games played'` is now also a value of the DataFrame, thus we now read the DataFrame from left to right, i.e., in wide-orientation and no longer from top to bottom as the column labels, except from the identifier variable `Player` have not a lot of meaning anymore.
---
**Melting with multiple variables**
We can also pass multiple labels as identifiers and value variables to the melt() function
```python
pd.melt(players_df, id_vars=['Player', 'Team'], value_vars=['Games played', 'Goals', 'Assists'])
```
![Melted DataFrame that contains multiple identifier and value variables](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/2d3d4d02-c126-4579-a159-9c1aaee826b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YZXB4CVX%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T220953Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIEBMvXNm%2Fwh4LOJSJPxxFImkArJH0OwIfmWpKUrRpmjtAiEA3uk2zMAyGyjihNrQHKe6auS9eIc9qS%2FYhioVnDFABU0q%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDOtrWrUhAhmU6AMCcSrcAw0bUG3IixweJrZM4NE4pvsi5f6kmxFUCJPM%2BSpEV4YEAhB8PB3pLmFNddcXEYKCJxdwcTCNEYcx06fpAs9dEeM3m0wU%2BDJy4YD0R9Ji5C24VKBToMyejeFWlJJW6G53T%2FUdWCBwj%2B3AZvJDfKt5mDaNzPK72KlXHaPitB%2Fqkmkx4JezBT5CAV09W7r68tWg1KEg9drj2GPLbFe8iVRITVTLhLiGo1t3yGDYVEtjfZp298EmM4WP1hhRg1H5Y3lXflJmPH0B8UyT%2FV0oMFgNUf7SbmD3kpg9%2FWFJvEDPW9z92HjOzFQEMv8P67CyhW3ECICu9socIGihOlFuV%2BfJ9QWDxyhgF7FjAwHx03jFtj6P9jZnG5L4Aa3GU1rfxYscP%2FRcrQnJmE%2FYPzDRl%2FbYK%2Bk5giDbqyvdlYonWPmJ7Dk%2BJpKKVozG85obp1J23qQXh6%2FJeGB0OCs1V3BPuU2Sh21tGI6kBf9CDh5DEtXto4ZseBoUXBjqJ03DuMvwGu3G%2FOTn4b6Ojps2qkTuZzc%2BfWVFFiUx7IfAnLASFWNGdkVANmckesyI0re8isYNukYiDrn0CxWv1BRoa4UODK5HBcypjZ4%2FoBIzHLRB2ew5fKdnlPpQ4V7RigR60Rq8MJ2m98kGOqUBnVzR%2Bxd4JY7zvIYFLD1nVVcDtc64fOZJ6ppMrUK5hrUtjx%2FHfj4GT6V7yvzW%2FWLUk7yUIO%2FKru2ilWU%2BFidwcIWDOu4gpZIp%2FFmoiadtg3E09KidZ%2Bb%2FX3BRytMd8KqkEeo0UiicmflavSOOkzUo0yJlLfzJ2tmTUkGiXY4LFBUspQXLx9k7bi11g%2FjKzFCfX%2F2hENrj31XQhisMXN52%2BzKY40Bk&X-Amz-Signature=13e16fcee79e6af07b334bc95322e8de98d288f2307588a63d96310051d8877e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
We can see now that the output DataFrame contains a lot more records (1620) than the one before (540). This is because we have now three value variables and thus three times as much as records as before when we had only one value variables. 
To understand what is happening in detail it helps to look at one player only and compare the melted DataFrame with the normal one.
![melted DataFrame](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/e810c7eb-a76f-4663-bf34-e5c7d9be01a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WUJGTWM2%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T220955Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJGMEQCIBEw%2F8PU9%2BiY7Esr8mns%2FsMxKJcufqZpC1ikRGjlufhXAiA6VWrV8Pc9KRFYs5yFZ%2Fr4OA%2B2gK2cfndWB0ohE4BjRSr%2FAwgmEAAaDDYzNzQyMzE4MzgwNSIMk4yds8fPx%2Fu89SklKtwD86YjC8NkzpS7Ps1TDXsVNIpTYNlA9M956u%2Fb12zIAiQ7sXtKX23xVEDUggViUVKc02pe8id9xCDmPTzRraRlDD7bbPswuGeUwn%2B62G4qen%2BkZJ9lryzIjrWHDFgUH7pxeDfOa52HyZ9sx1kudpav08AAobyhJHrcTzdG2uw90ilZFBSoSm8RZJYbNckzhY4LlbnZX7V4E0n6CVP7uyeQqjLTKh%2FfNZfmrJnFnGm11fkEK6arrHxocbHEIFsW2C8glmGiTK45VPKEe8VQsKsfoIuAaOVs8IxogFifYCfW8om%2F%2BtSwfykbjLO9eFDn%2BWVPJzuqxaBKDY5%2FfU3bwpAV7wQEP3XlyIZMLfwcXnML30PqTiiWPI4VabhHLxTEv%2FTJV2vtOB%2BfpRgweB%2BkNHnf%2FOlrPmdxTCgXXRwUMI3T5rZl0kZ3L2qMgAjRoIMZ3QfHGjgK3j6uOT4UJCjen9mM7H60c0Cu3u6knYKYwDv6%2F%2B%2FOtvAXjPj16Zz78FoxJH7Rs%2B6UD62RZUKjnve%2FUAoRpkFoJU1H35%2FOcAcM7xunp5k%2B9dL0RGTLPY0xJ2SmtAa%2BBLD8EMS5kBkPG8d83gbWWAT%2BWsLiyXZGy6Z2lL7bI8BoQ0KA%2FVk2us9adnYwnKb3yQY6pgE9OLmOdTi939O%2BVD4yJO5QEBVkFDZGojKqzUsCOf%2FKLipakkGe%2Bv333jjxY2qGLt%2BFZd%2FNRixwwJZDwU5m8FLkdT%2FZejyTawnH9%2B%2BAzZh3I8Q1ap2iPJyhl1aTyhWinTvIXErvUHg5dk3XOX87HjDY2%2FsLizE70B2v%2Fm3aKmOtuMz2QRHnJNfT0Ljm4pk2P17L43jYQoFfMuMgPHY6XM0YjWfPGmLN&X-Amz-Signature=8369bb0e2fc99d1f7519e88f56d75ff7d47b1cf58b58ce71c2972f72aaaa204e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
![regular DataFrame](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/5782aa33-0a88-4833-9ec1-3545e2cb104c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664WMAO7DS%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T220957Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJIMEYCIQCwDU2xejU9FCZqS0Ig7nMQxqxOab4mt4AhBOXBKOG6ZQIhANCihMSVdL8DwOQeABgpxtAmQlikdU31T9xgQmTF4TqSKv8DCCYQABoMNjM3NDIzMTgzODA1IgxYcYitZ%2B88b0hlSKgq3APAX6ZcFrpEjxGGZyEHWCee6bBMulJw0ASfiSK1jIZHS2vCJD5nW2NqPs%2FuEK4ei7Cj6kBDJvYF54vp77ZMhL%2B8cympcvuQlkfJ9XgZLZoh9MoFjdHqQr%2BpOWuQlg4bWYKwRbArgSga2Z15m%2Fr6vr6h6wLTV3Jx2fdAKTR3Xr0SiU6h2GuRsCGD%2FDxPb%2BQa13sRcqNN16%2BSIIcmN7u0qCla8tFXXys71qQMmavZ0rd5W2jMdEu7EBoHCSj%2BGYgDXvPXL74sMT6aTSp6FNhz4EUM%2F1AV8xfDXiEYVIGwS49SN1e2pmJVgrR4j8N696vlbtWBNcXGWGFRwr8%2BDycng0WlwqemdsK1SjCYUqCHu%2FoUwJs9SsFS%2B3gD28DLRMVGq2dPM2Q64Dh%2F5mOOpzSuQdNFfJxEfUd9sb6A%2B7eAQ7pwlNyFijBNWb%2FdyyJFqz5Xs68zBlSkvIwu3L%2Feu8RwBFkRFJn72udGJWalTlK41In1K4COypDOKclCZRR8%2ByLgQnffeCO4zugBVanymho6ceQpE41rCmwWjJFhXyrGZerIg0r%2FlkpoicvFbTna4aQ4EuH0U%2FhGr0RRZd2WPrapyFiG34Oy35UN9OHEGjP8pc%2BrXxHLcJt%2Fzd6ZK6p1ljCSpvfJBjqkAfXiSDkSik23DgN7kk2dOOLao%2BCqIybeM3pZA2%2BB7vJbqFtzUh54G9ZKhGdF5Pfo7x0VghwsxndoVz0O7KSB3ChiaIjNXaxNtTf%2BvC1qsk2gdZpA6V1dGJxlvO7T3Sy2Sh6Dr%2FHkGpk367A7ZFw0i2zb4Tsyrnu8jNuydQF%2FyS18yytbNJ3bRlLKQTHs5Z31%2FQyR7u1esin5WpgTFKHiZRbdAkHK&X-Amz-Signature=cb696ceb3c4888c317b1ec580e0743f54b14ca02be7c6ccef8ce596aade1a86b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
![DataFrame `players_df` with new column `last_updated`](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/8a1db142-80f5-44af-8755-ffad5c54575a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667JTZZCU3%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T220958Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJGMEQCIGGni0IrlGSbFsCuzeoWK%2FxTLJnqFLT7QKHnvxZY5r7QAiBsZ7RHlUJF9dHl64GywiMpb1puaTQpgrw4yuTV6HqWZCr%2FAwgmEAAaDDYzNzQyMzE4MzgwNSIMSncHMSrth0TGtgKUKtwDi6WMGy%2F7dEFwM%2FHAysUaNNofq5TxfPW86RXsEttAqCV2T1HJPa3hdE%2B7kbA1E8n%2BlkGGTeL5of1sV2HxxX5X0YGQDAkAmdcnTYHfIgG8lwAzilHodKdIb2mlwcHv5XqLJSqy8BkNun6uk0Mi3tPiVh%2B%2BNve%2BNGpwonOL30rU4akffnC6VmCdwnr81V3qsmaNY4T4Pzkv7Cnb%2Bi1O3HzSQRm9%2BsIsJ5JD0vES0ODBnWg6pn8Vvy7VXBFfvtd7tCVB%2Be%2F8POF6A9Cy3uHlaFgm55DQB1x5PdWKUk%2B0W6QIlGVFU11qKCLbnoNFvMTPyidnMS%2FzAKp8sK%2FCV5dQyetUUaSmU4tCrGTi53TXK971h455LetF36hct9owGN5PvXFwCBU4gTvxS15q1usoCleS%2F9ctijHQPsaI99e5fucNmnnSj0ekk2XTT0XJvLnmn%2FI87mTlFHcAOjK3bIyLKbMAAfW5h22u3LSo7wlKeQ%2B3Ggm5t0RyH8nIrEox14o7gBYl2YKd4i%2F5ffYL3VdBZAl0404oqJQLdFFoe6lBYASW5IfslG%2Bsdet0jyr7o2fL%2FtTCBlbosfKHo6%2F9Ug7WjPe1h7oAgpjNOaLpQOB6MWtlzOC%2BhyVwwB9sTEmKXaUwxqX3yQY6pgHCy%2FRpkZSx9%2BZx0WixEb%2FlOREzB1eOXMV6X2XadkIEhPJs5I8XU8g8ZGUKQDljkvnnLvbPqaHX7jCiRfMBxdqkFAdP3W5bS0NUpJWwOLIpUAzdW7bpJTG%2BlBXtSyCKhapbuKZgnkZEjAWJqJ1zzovkGwi5z0xVpgiE50oSvmlpyZI8S5LFGhXdOvIr27XdzND2EIyQhjtgUtUQcG%2FXspzfY9u%2BfdSJ&X-Amz-Signature=709f5f1466841b6dc2f59cc73fb1ad7014ad5b58521f4255a313fb781b5c5ab6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
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

