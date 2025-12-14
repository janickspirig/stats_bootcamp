---
title: "Quiz 8 "
notion_id: "b0908e82-d870-4e3b-802a-93e78912a002"
notion_url: "https://www.notion.so/Quiz-8-b0908e82d8704e3b802a93e78912a002"
exported_at: "2025-12-13T23:17:14.754013+00:00"
---

# Quiz 8 

## Question 1
Given is a *pd.DataFrame* **df** with a fixed and default index, several rows and the four columns **a**, **b**, **c** and **d** in that exact oder. 
Which of the following statements will always return a *pd.Series* that contains the full column **a** of **df**?
✅ `df.a`
❌ `df.iloc[:, 'a']`
❌ `df.loc[:, ['a']]`
✅ `df.loc[0:, 'a']`
❌ `df.iloc['a']`
✅ `df.['a']`
❌ `df.iloc[:, ['a']]`
❌ `df.T.loc['Name']`
✅ `df.T.iloc[0]`
❌ `df.loc['a']`

<details>
<summary>Explanation</summary>

Let’ assume that DataFrame **df** looks like this:
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/ee0d79a9-f5d5-403e-94ef-83b6082ccc01/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SYYGULGU%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T231704Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJGMEQCIGK6J9EE2FfSzah7dyXKOrn2YOK5pRq7Yj6p89dOiuj2AiBmp1ngve%2Bde5L8%2FPIp%2By6aW%2B8lFBLkj5xapHd%2Fevphmyr%2FAwgnEAAaDDYzNzQyMzE4MzgwNSIMD9nz%2BU5BCW0mM7qVKtwDkYTO3C%2ByZxgGnDvvOAKjFOKJ%2Fn5PC%2BMxiJaPdYbG0pijH%2Bh2Lo3y%2FAobQ99Dkadq%2FQ%2FMjRZI9%2B4XrJBeXvjnsQFcFWWz0TJEMjQ3rdLzBXrSgvyZN2zKDnCL3yhN3IXkBD7xGb4WxBz1mGzzDdXUwk9s4MDSN70BmkccYfvW8qiHUVKGakUwBPDJyf9XsCMbKyoBBF757jOn7kBz4mkA40ZxwlfIDWQghXwjXB2WOLnm3lentggn%2F2i3HKUMqGBVkyCAuBnFHHYbjleEyEBCfFcgUODoSoEAIUrb8FpggWQnDVq468e9MV%2FnphY4XbKuQxExSLLF0CE2NbhvAkbow%2B%2B%2B%2FpQwpZGYOeBd2UspPRmGzkBTz0%2B%2Fan%2Frq9spzSXgq3QTwNxf%2B%2Fy%2B7Ee6P1JxXWkMdyoDRMIdW9wib7BQQHy7TQvkrqIwlfC%2BW3l61Fec1A6DSyx6r6mw74XJIqSOWlZwTUuPtDLmgXT%2FDUXgnEtZe5Vu%2BlcyfDdTlPZ7dXTtZvT2KplrA%2FxMgDiw2TawB6nC1Vzl8q64Y0fEVF9QqKClxYRbTN5RgQ%2BT4mGPCtJ4EgBn5cKp56C6AH6ibV%2FEvGeeQ6DyF4I9mig4YwmoV8YRwfusMx7xK8MRPIww5c33yQY6pgGwiidJw2IrHAmvTH2Y94zAovV02w0se2ruEovWqTKhWToI81i933bu%2B1pxHBp2cgaAx9HzN%2FHHVBVRhxeC1khMH7tbO3M6TwmjBoRqn7RQrdgCDvOgmHrdFnindfa0NZWdqotu6Wm7fVUFbRCXLhmUINYla6jIu%2FgR59D6DsFVFMazulempuOHd9TOf07PEO6bHulTC0JOJmF99Ky0SIIMN3Ktys2d&X-Amz-Signature=9f773589e14c2613ae2263d1229704df9b3149fb690c9b789fdcf5bbf8b5ae13&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
Below you can find an overview of each statement’s return value.
✅ `df.a` → pd.Series
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/b1f61fb3-eb02-46d0-a103-be82889c5473/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665C52WUIZ%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T231704Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJGMEQCIBzWsPbK27owZV6v3OFk8MMe8TrwcAI391zfK71A3shJAiA6K8SKuf1XgWbtFVe4pBLzQLvPJzETc3DqbpOgM0%2FIzCr%2FAwgnEAAaDDYzNzQyMzE4MzgwNSIMFX%2Bb5SICGDC5fszrKtwDDPgZImJHjDCFvuxkuT6Bkg2fumgbIcKI3P4Rop%2BwEjZEKEgACSb2PMluFrN2RKYP6obkRkyfvhYdcarUXiIFw2QhkfUoue16HZ1gIdKEofngfeHdpzPGQEjtUvWLf6SZhAhWHw4O%2FM15qwtKLpwH2Kqm4kfrF8V7PPpRwKSTiAC0knc7vVk51iBvxObpFhBLlFiEUyYmOHazPIKRXZiiyMBvTI51wfweHRa2XZUp6CzIPcLO7y9VXKStPguwHmfPGxcGBWNzi3YsVFWX7ND4dJcN6znih%2BCKPWXazFLghSPtztL1n8Frd2MECk8dg0tl6WeFZdzYaK0mq0kshI0q28%2BTMqqB2iiETRUpOkCMbR%2BwLTrGK1joysY47CvxIiRQkzKSL6oDRVHTJCOJ3NV%2Bl%2Ba%2F4loPtdVk7UAL0OQ%2B8UT7K0%2BDdpenBMX9XjYcOWPUhbtvhdOhzxwlGUUj1GNaQlsNRue9WLSVan1bkUzjwguJh6F6MFHJkzvWja%2BBUG%2BzmzSLYMIxhrS7LyrtDrhbw3jTpodAy6U58nwBHWOD49rztrOhKzdHHHDXEwEeBnDEwozr8ZgujTxKzFX5eSpPA1aAZTaXJK%2B0XYH%2BCdhW6CeVudWdaj0Rqrzx4Lowq873yQY6pgGO9G2UoHyZUZZomKKYcDxipwbcsqsbqYvFFy4mutOOpvSLdWyImmTp57x16PQgsdNMA2aoAyJGjrV7ih5zkXM5EjjWk%2F4HOqF9g0A4lphC%2BwtvUFXrFYIZWyl0Ypq4e5M%2FtyV%2BwHvK%2Fo3fkaxghWM8YJLu62slHDDfNasAoS7vr%2Be%2FxhVc6IzUe%2BTo28xbFQsa8bq66tXaRRDRXfxGsNcSIu6zk9KE&X-Amz-Signature=9390916be1b2d1a9fe04ee8e896ca03f760ca969ef69ac3fcc50fdddd3c4678e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
❌ `df.iloc[:, 'a']` → error message
ValueError, `.iloc[]` can only be used with index positions and not column labels
❌ `df.loc[:, ['a']]` → pd.DataFrame
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/cf0d4d18-5a8b-4532-b215-6f0e381c8819/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XRH7GXYK%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T231706Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIQDCLIvP3PTXP2m9G1R%2FFUSBSLmX8f9J2eV%2FBKNXDDnjpAIgdPC%2BbdF2D3TfuJEErJlvcNiWOfXSNqBA%2F6Gz12RPbJEq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDKp6Aq2jFVbFFn8S1CrcA6qfIdlbaOAtNOypGN1JM3%2Bz77SVSv3jgn8uz3MxHsT18Sy4ZOlNuUko03SiCG8cfTn1fdP2H04hsAHODtqP6ReUKaHSOGvkkYU5f96DcB9el1ltI7W28fd9FVHpEuO3tPKvWn7z97Hsoh0pdpQ0H8U39pm%2FkfVnEjqJ65HO5u6I0SkaRYUv5fxPbRTb%2BVRs1d4iTYiOHY9RBKZq7OKhVt2mijeyrLGBA1ijRCH5OWCWT2lj6L1uR48JEEmgYyIENg2f2HOR1zC07CFTpK5PbVK4QVMaF5akvBOFLB1N3KlNY1Upd1bCihbDhDtTPFTT7LhxpBvsVBuO%2FX1OXwd8NHAHuSiMtpsQ0MnSUxjmQXkFrMPpf6sufGp5u054tagMvcWWGEwTzpzI6vmlxHpTBxlYB8TKj5UHNkNG%2FWTH4Uzmc%2BwDawfpTBGcV2eLEWuSqdHQL%2F5OOVoJydaHzTLeOPfDU6qspvBwtAX9pIf1CRYn0SIdzL%2F0E8U8ux3R3vg%2BU3rOgRoNZOi%2FSqLiCuj7Z2C%2FbykUZ%2BN1X5uFOzHElC0OdXZk1xUGxjd6zgXzMvg%2FDYr%2B5zyS6KCp3i4%2BFyVGpJ9XOgzYkDCoEZJsobdIK4Yu4%2FY9ldUy75LXR6QjMKPO98kGOqUBqV2suvqS6hXM25Se1t%2BhaAEhoyE0jFR1Wo8OcQdNZfhDIyrcsCSXRfEBTzcxlPihnH6shRPcogw0ijrkZYMsyGGAEeMByIFOl4Tznem13ZPzrauml6tXEzRw6TLBrjH6kPunh9Lh%2Bjgqapl%2F4uBGb71qUsyF5QNP80oTgJWg%2FKW1Z4ESvaOin2n%2FqTCZ8%2Fh%2FVLWEEjKp5wUwdN5sQCNCT4ujn238&X-Amz-Signature=57a6476654b8c332b43d8bf473386d7b1f5a574981090fb5af777dcc9cfe2460&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
✅ `df.loc[0:, 'a']` → pd.Series
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/2aefc3c8-f861-4e01-89c6-d60a50a40838/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QPAGCRJZ%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T231706Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIQCkSzbYPCrtaA0nYlAFn7VUcw0Zrf3jJJaveOVuMKRs0QIgJ0IPH40pd93SeXc6up2dVa64Ow0idXAVAoOJQGe4ecAq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDE8TGK%2FNRJrhZX7NwCrcA%2B4VMMsCaVbf9BSZzNF7LtLr5uUYBw9OHkwfiyeePnwJm4HSmHgFIwBkN1%2FvnMMXIidaOhiNgM65nY%2Bjxo%2FQBLy%2BeRuzp4FJ%2F9dX%2BmLRt0l9QZI0G3mELgP8ieTkkZ62S72NLPeqnetKq6yrZmrdrck4AdjmWfJBQ1Z0QFqWZoNMMNwOk8iePV0kgxqBTd52SaGPV5b%2BVBGH96QlfMju1S4YWHCbUB4CF1dwpX%2BmkGeiyaVo6E8NwRJ5A59PCh0VWzS4MAaxUWmM4OsDpxvSyrv6ExswMokQb4mP0HqBYJH2mHHLa1IkhUMTPm5cB973vtfnfazPPJDq1qc3XMx2lLEkC6%2BT4IbbVO7qt0c%2BRFSpDzraHGDLN6ewSjWa%2BhgqtHxvlXxtuwHzm4NA609eLOcIfyjtJvfJtGYP72%2FtlFxETFIMY1%2BxKftjxcCQpYv4rZS24zThM6ZqubVr0y0Z%2B90PV8bBnFcy%2FtpGYMR2g7HN285mDGOfRtiMYljKCvuAgDF96iCdUXUHqUSvNY3fPHXz2Ov9S1wXskaZI9CcEgvoXElNrKPXVnvgmM8px3BSxdg3DdyBn%2FrGvKvIUUdtJ8fVhqoozK%2B9rzRCt10ZSVYgG74c60Ln9duA57ylMNbO98kGOqUB0KhBiPTcs%2BLwSOeYMc6vwRIsyUQmvk5vuPuNsvTdnH5nbHjMjHs5t9LVSVvWQkRe0zLYXLsQfZCl1PM5fLw8tqTSKaVU8xwGK3VxtVqcoLXprFO9dUIYUdoVUSgDnROMtjA5l2bhjHj8PnMO7DBo0UkAfuRmLx2XtnUOo4W%2BFRzqJ6Kee%2BzRXlWh5InJZTyhTBhKupDEcnSRL1C9wY7v35y%2FDTs5&X-Amz-Signature=a4299761cfc3ce40b5370083308a64e01065aef657f20fb283e59e83e67322e2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
❌ `df.iloc['a']` → error message
TypeError, `.iloc[]` can only be used with index positions and not column labels 
✅ `df.['a']` → pd.Series
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/a315c7b8-e11d-438b-aa95-6df4c0da5b50/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QW2ZSOJT%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T231707Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJGMEQCIGFvkwg1CO9Pe49EDyTDVFWn3NcCC2vTOvxZCQ67gqZTAiAgyS5sML2N1Yae3oGhMV%2BsTVUaKO9VQF91FVTbIpn9eir%2FAwgoEAAaDDYzNzQyMzE4MzgwNSIM5cUxfVui9I%2BNproaKtwDoApxPE1B0Lq5PoCUF9BTT7i5p%2BcUdqGo%2Fvkygnyd3dIzl6TyjnDIMt6RhiNtAn6qAd0P%2BY9yRz13eVgh2VgfB7VISkvGl7y%2F2dVNIFMP7n7b7cD3psbedMKsvoopfQt4yfku5SSgiZytgzn4jSyjKHJgSVatqQWTEZiKcceOnkaLFIBk8gsQkUICR2Wga2FJnBvcCcSzAAbQAUREStnbsBxhTc1tKutwMhbUtMOgb5xn6BzYHMgbhtLPwoaSCtIP9ZlglxUybyQpQMtmzw8pHwOxpJOM%2BxJlZqv5JKgC8vxkYXF944WHZPQ3eXEq0ulhv3VuM7VLYHkbdXRgP0%2BeQxJT8qmyKtS%2BN99sfd4EDTKThOfC%2Bb6Qv1ZM2bmwQ6HnFEDh%2F7KeefskAAxLzaR8tEmLL2uQD8FOqTvXBCeTSl4Fh9CEVTdv8%2FwEUEVgbxgoDXM8x7wyp9nCK6zLb2oV8fvu%2BVS%2FkTPK6rEPhimsL9uYQ8bISg5OFemUZJZTUlqMS6QDu9QbV9xoTKivvr9SBK4rAJi9VkI765C%2FEBYKvaIZ2GKB2TQh8CApOTkquBzVASycfZVBjrpIsUrt6basta1Z4r9cHwi4DeWWRkcLbPJynd%2FMLmOCq7Uj3Bowjs73yQY6pgG6y2TM%2F1Rw6ineOZbn8VDm%2F%2BUTQWQWPopObDPS0NL5IPCXdI%2FwDQtCj3YnirTIZwsDtRQgSmdqghxt4ky011d0HScD8Ei8%2FestPxu7yxvzMwaXziT%2BlWG3A18JxMgPPh80HHEP4CUiFB9Ik0tIiZcDp%2B0kwXIsJQ%2FP6FYRsidjBuQkq2zj1nUljrXWW3Jdn8omvCEVOxF2YRhfkhZYWeYAr%2FfCzpe%2F&X-Amz-Signature=aef71f4b346bbca30307c950b30252aed98bb32c0aad9288cc2e49a2ba16058a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
❌ `df.iloc[:, ['a']]` → error message
IndexError, `.iloc[]` can only be used with index positions and not column labels
❌ `df.T.loc['Name']` → error message
KeyError, there is no column called **‘Name’** in the DaaFrame
✅ `df.T.iloc[0]` → pd.Series
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/a315c7b8-e11d-438b-aa95-6df4c0da5b50/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667CTJMAFM%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T231708Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQC%2FBJ6FmZkfjrLBBlXmxZntnZPPfa0w60TwBrtaVOaROAIhAIS9mAsRhB%2Ba8X1g5BPEarikNY9nQgtOsI99kAgxYIXjKv8DCCcQABoMNjM3NDIzMTgzODA1Igxs8T%2BX1JuLdHOZas0q3ANDW7xpiETUHyW2UGC7Eczu4TAkLkVFP3UXMOz7MBrKKqqTJG%2FiqrnUWuwNdNcE1pOgPmgAoHmqCpYivLD7Vl8XHakxe85ioVTxVaVM9KwgINUCiS2Q9aaP75bKQfc8e%2FsJmxZEYGt5dvNZWDOCp%2FGPMBsxeUaBph3u62yMr2WwL%2BqUOE8VrwvNlEq29XOBonlTOjHOFwxLCGc35lJGkVAs97EYVDmcgp5ljv17KK7o7%2FbzsOI39%2F9VkjO08YI%2Fnlu8gbCMlcKk5Put9iu2NUOQ23Gd5O3b9Xok9hnoT55N3MOhqLOyKbxqbppcvkccGTr6tI6bhvHsP2vYO%2FmGtjW3MpZaso%2BsGnnbyiTc7LXWSaZ%2FR1W39NxbVPYyR%2BQeJXN%2FJHKSNZDFgEEXTGyierLD2KEgq%2F8H2a%2BAVf3MDlbIMlamLDEtkbuMFiXTZK5MVyrn6cGDUPqiHdmu1Jb%2Bkc93%2B998%2FPyKpkvCo0N%2Fh4zJhjAzVxopzJTtV%2FfFxr6EJxbojv47qeK1V8tQ8q%2FZ8PZqksl2STPiLv9VLZUr7qeK4yQH8uOI%2BfKu5FR7NOiKGQ5qVbPjs93D6iKmwt95MvuhrMT8O2f1SZUhavi%2BokpS85GM9g1OtSKwdjma%2FTDZzvfJBjqkAQwcDQOhVEPFsgmsatuLhCHOh3WqUseBL7PdaUqA66MFzhcjwCjLV0hQpb9OdkxcDiy6n%2FHSvn7ZUWx9BodRU7OMXx4LEFoStOQHNPN8bGMaF8DxOFjDDzAA8QYexyLa6QJIoCezTxJ%2B%2FbhHWXDrfD%2BaHLFnMiLmxA7%2BxKaIlPVos2ialwXc3peZ%2BeAIq78fuoGtBS0FzUmxFSD6pSqFZZfcF%2FPo&X-Amz-Signature=6da6b6dd1814f357a3fa2bc98fcdbeed1b652f49c45ecce1fcc018cf23d9c5c6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
❌ `df.loc['a']` → error message
KeyError, there is no row in the DataFrame with value **‘a’** as index label
</details>
---
## Question 2
Given is the following code snippet from Assignment 8. 
The function should compute the ratio of gross/budget for each movie and return a DataFrame with that information. Why is it not working as intended?
```python
def gross_per_budget():
	df = DF.copy()
	df = df[['director_name', 'movie_title', 'gross', 'budget', 'duration']]
	df['gross/budget'] = df['gross'] / df['budget']
	df = df.sort_values(by='movie_title', ascending=False)
	return df
```

❌ The original DF is modified in the current code. Line 2 needs to be changed to
```python
df = DF
```
✅ The resulting DataFrame also contains the column `duration` which is not included in the above mentioned criteria and therefore should be removed in line 3.
✅ In line 5, the dataframe needs to be sorted by the column “gross/budget”
```python
df = df.sort_values(by='gross/budget', ascending=False)
```
❌ After line 3, empty values (NaN) need to be removed like this:
```python
df = df.dropna(axis="columns")
```
❌ There is nothing wrong with this code. It works perfectly!
✅ After line 3, empty values (NaN) need to be removed like this:
```python
df = df.dropna(axis="index")
```

<details>
<summary>Explanation</summary>

❌ **Incorrect**, because the original DataFrame `DF` is not modified, rather a copy of it is created by suing the `.copy()` method. This new DataFrame is then saved in variable `df`.
✅ **Correct**, the criteria mentions that only the columns `direct_name`, `movie_title`, `gross`, `budget` and `gross/budget` should be included.
✅ **Correct**, the criteria mentions that it should be sorted based on column `gross/budget` and in descending order, this is why the parameter `ascending=` must be set to `False`.
❌ **Incorrect**, this code would drop remove any column from the DataFrame that contains at least one NaN value.
`axis='columns'` → drops columns that have at least one NaN value
`axis='index'` → drops rows that have at least one NaN value
Let’s assume there is one movie with no director name. Then the column `direct_name` would be deleted entirely and we loose this information for all the movies.
❌ **Incorrect**.
✅ **Correct**, we want to remove any rows that have some missing values. Which we can achieve through `axis='index'`.
</details>
---
## Question 3
Given is the DataFrame DF from Assignment 8. 
Which of the following code snippets returns a list of genres for the movie at the given integer position ***position***?
Remember that the ***genres*** for a movie are saved in the column genres, and are in a format like in the following example: “Action|Adventure|Fantasy”.
✅ **Code 1**
```python
def get_genres(position):
	genres = DF.iloc[position]['genres']
	if pd.isna(genres):
		return []
	else:
		return genres.split("|")
```
**❌ Code 2**
```python
def get_genres(position):
	genres = DF.iloc[position]
	if pd.isna(genres):
		return []
	else:
		return genres.split(" | ")
```
**❌ Code 3**
```python
def get_genres(position):
	genres = DF[position]['genres']
	if pd.isna(genres):
		return []
	else:
		return genres.split("|")
```
**❌ Code 4**
```python
def get_genres(position):
	genres = DF.iloc[position]['genres']
	if pd.isna(genres):
		return []
	else:
		return genres
```

<details>
<summary>Explanation</summary>

✅ **Correct**. With `.iloc[]` we select the movie at the index position ***position***. By chaining the selector with `DF.iloc[position]['genres']` we select the value inside column `genres`. This value is a string. Thus we must split the string by delimiter `|` which returns a list containing all genres, or an empty list if the movie does not have any genres.
❌ **Incorrect**. Here we only select the entire row of the movie at position ***position***, but not the column `genre` only. Thus, the `genres` variable does not exist and Python will throw an error when trying to access it.
❌ **Incorrect**. Here we don’t use `.iloc[]` to select a the specific movie. Therefore, Python will try to select the column with label ***position***. This results in an error as no column with a numerical label exists in the DataFrame.
❌ **Incorrect**. We don’t split the value in `genres`. Remember that the genres are saved as strings in the DataFrame and delimited by a straight bar `|`. Thus, if we don’t split this string, the function will not return a list.
</details>
---
## Question 4
Given is a pd.DataFrame as **df**.
Which datatype(s) can end up in variable **x** after the following statement:
**x = df.iloc[42]**
Assume, that the queried entry exists, meaning that **x** is not empty. 
❌ **x** can be of datatype *pd.Series* and *pd.DataFrame*. 
✅ **x** will have exclusively the datatype *pd.Series*.
❌ None of the other options. 
❌ **x** will have exclusively the datatype pd.DataFrame.

<details>
<summary>Explanation</summary>

`df.iloc[42]` selects the row in the DataFrame which has index position 42. Thus it will select the 43th row in the DataFrame.
Whenever a **single** row or column is returned by a selector, then the return value is a **Series**.
Whenever **multiple** rows or columns are returned by a selector, then the return value is a **DataFrame**. 
</details>
---
## Question 5
It cannot be that for a *pd.DataFrame* **df**, the result **df.loc[x]** and **df.iloc[x]** are equal even if the value of **x** is the same in both cases.
❌ True
✅ False

<details>
<summary>Explanation</summary>

The result can be equal. To do so the index position must be the same as the index label. Let’s assume the following DataFrame `df`:
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/77f0afdf-245b-4050-ba01-3fb30b8f7e8c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RJ3KTIPH%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T231713Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQCnfjeqBf1nDzHH%2Fb%2FM5sXq9jS3V0IcFPo67F0fX6nwbAIhAPOAMy04qsbcScDV8UktE39YtwBGxxNBeZBQfT2MQlFmKv8DCCcQABoMNjM3NDIzMTgzODA1IgyPOmBzryqdH7dV47Uq3ANsCPEeu4zX8I7yskfG%2Fy1coTUwZOZlhHuojM%2FrIzXvYqsZ3UEWZoYN2u0XXpkgWvD8kjhuXf1maI3ZEi7kAlLQpqrpkTa6Gp%2BjiQsDhbPMrj5gysg6v9otT4TRJOD%2BcffSo92POHfERGy04HhDrLCIE5BTJ%2B78wDW6pJokyS90BHvbsyWC6q4zpZEeJLs67Xns6J9jDjMdXJlDwiAxkylOGlgnYnDbH%2BtZcFcLuQuTSlUBxs4XHvzv1eojL%2BhhuuYizt5uq%2BcTrpkxWthSL1QMlEexq9cdxjgVaPmn9oBGd3RtMVJtqfOBgcupQJ4t9GX7940%2Fdb8b0W%2FOLTyVmoTKVosI7Bg6uqy8x%2BmDK6oNP%2Bidd3CXOvwQTRbAXzmUYRJVqPO1s3Hd3pNtoz2cfmw0Sp0Hl6d1Gal8PpwaZxkPysvf5GpY55mxOacE14Wqfrk47F2%2FFC%2Ba0xsYk67Sj%2BQfswY6vT4tl7BCHsc0UrijO7PR%2BOSsBb%2FEYkwzUC7vuFcZCCafzohBnbKKW9hkhHvfNTj14q9ziBFzjIF3h6fVpymuLWP2dnH0EPlTgeYv%2BJEBv9vezErng7lXUsK1cCHJaMFQrof8lQ3mu4qZSHmvsDMVmN2Z895g99k%2FITDAzvfJBjqkASZhvo2UcfSAtGZtXwaEH%2FV264kxTEDPoBCIJXd8%2FrIfYebE1gLL18pl5tdJbna6ajsO0u%2Fzw7GPdqRgYyq6bEZnM1XzMhoNROw7pz8wS1J0dA96L%2FkuqkGq8UHHRGS3hZLK%2BwOX8GKq2tv91A9IM0w6Q2lq1HeWS5UyxeH4LHp%2FK%2BIYPuqb6xW02%2F4%2BqOU1B%2Bp2BXe5HDLrb9zMjGy%2FSM8j4r3r&X-Amz-Signature=7156fb6cf9ff7177cbff820a558bc41a23f6e9a8d2222c4cd62d7e545a25df76&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
We can see that in the index column we have stored integer numbers from 0 to 4. The first row has the label 0, the second row the label 1 etc.
If we want to access now a specific row, e.g., the first one, then we can either use `.loc[0]` or `.iloc[0]`. The result will be the same. 
```python
df.loc[0]

a     1
b     5
c     6
d    10
Name: 0, dtype: int64

df.iloc[0]

a     1
b     5
c     6
d    10
Name: 0, dtype: int64
```
And of course, we can store the number 0 in a variable `x` and provide `x` as parameter to the two selectors:
```python
x = 0

df.loc[x]

a     1
b     5
c     6
d    10
Name: 0, dtype: int64

df.iloc[x]

a     1
b     5
c     6
d    10
Name: 0, dtype: int64
```
</details>
---
## Question 6
We have the following *pd.DataFrame* **df**. The column **index** is defined as the index of **df**.
| index | value1 | value2 |
| --- | --- | --- |
| 2 | aa | z |
| 22 | b | y |
| 10 | c | x |
| 24 | d | w |
| 30 | e | v |
| 7 | f | u |
| 13 | g | t |
| 15 | h | s |
| 33 | i | r |
Which index does the command return: `df.iloc[6]`

<details>
<summary>Explanation</summary>

`df.iloc[6]` returns the row at position 6 in the DataFrame. 
The first row has position 0. Thus, the seventh row has position 6. 
The following row is at position 6:
| index | value1 | value2 |
| --- | --- | --- |
| 2 | a | z |
| 22 | b | y |
| 10 | c | x |
| 24 | d | w |
| 30 | e | v |
| 7 | f | u |
| **13** | **g** | **t** |
| 15 | h | s |
| 33 | i | r |
This row has the integer value **13** as index label.
</details>
---
## Question 7
Given is the following *pd.Series* as variable **s**:
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/e86f9897-778d-4350-9e4c-1f744594578d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XLDPPUIZ%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T231703Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJGMEQCIHNai4fse0WcIz%2Fe2iyqhWaNzP9ewAddUDGu47Qb7HL0AiAauUvt6rGXIafLs3UjnzMsaw3X97Rts3TBD9VH8p92yir%2FAwgnEAAaDDYzNzQyMzE4MzgwNSIMDtoLSHRqLwtpzR3iKtwDT6b9PgQ6wiLM%2B8zn3DK0I8iROEAb7lxgVbuD%2FyffGu%2BAXpa%2FUpi0cooQngZj5yhFy2QikJLnuZ%2FOgjP6i6dYskmkFY6z1M9ZzCx%2BvA1bjD9jD%2BiiOO3JUba7RBGsVUbkcYNY7eqhZaoleOY1s5VDHjBLsQaFhnvfs83TEEyIgvQ01iihyheBLWQwXNv%2BICl9qZvrYKZFZgDx61CiqlVIUzji%2BK%2BVUfmzuux%2Bp7fTCiGvCi6gsgCKOqwaWKMUjGBHX8e2bzvzD6CPA6l%2F40bLqNfuFm3phIfbrHx4DtWocJCwJg%2FUJ4ZhsniaB3Yd3eGrlVfV%2FX4HURvNmFOOGT08cNXJI0Ry7uMdNYlKmwbtZyBEOZSwVy6RV9KtWUq9Nq9Q38Vkb91SG5Tw7ga1QwMWBa6FpD4%2F2ZmuJgPr50y1LO15DDw6i4nHVozQwUm3uRcHNvDfrGiGXuTgKrK9QCoAlgSgSqdEkGhrEuaVitlB%2B4f4TkxMnZyRpX63jqm2uz2Zw%2F8Vq%2F7A7XqrhGf28qeKSF0FR243U3syES3qiXuJyf%2B4ZaOrhrWHF%2B%2FRU4UVVPclsD%2FFxQTWARHPGuP0Nd6vrtWk4tg9GmMderAV5dhRIrpn8VKolcGAheibcjMw3833yQY6pgGBDkgMvz6zQ7RpILzt4GW8O3eA%2BBaMmBSJhBU5iQA1tKWVpYpoVN2OzgsDaVltbaFsi3WXfJFRQZKWDhhLvEbjXvkkCdxutDN%2F%2FqzyHEe%2FUDcYVJFIgyQNHg8Fa%2F6jcOgOTSwTMHEHWSr4IkuNVL%2BRyS30becwssrMuimtu3KN8ODI2JpEO%2Bs63jiy5GB7l55fsl538QIjFRtZySU449pyKfgpqM8B&X-Amz-Signature=d09682473265aadc4c7728a0817c0c3d3e29a8609b358b1f0960bd1f389162fc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
What is the result of the statement
**s.mean()**
6.6

<details>
<summary>Explanation</summary>

The `.mean()` function ignores empty values (NaN). Thus, Python does the following calculation:
7.0 + 6.0 + 5.0 + 6.0 + 9.0 = 33
33 / 5 = <u>**6.6**</u>
</details>
---
## Question 8
Given is a *pd.DataFrame* **df** with 100 rows and a continuous index starting from 0 to 99.
What happens if we add a new row with an index that already exists? 
✅ The new row is added, non-unique indices are no problem. 
❌ Similar to SQL/Databased, the index is a *primary key*, so the new row can’t be added and it will fail with an error. 
❌ Adding to the end will result in an automatic matching index: Here, the added row will have the index 100. 
❌ Pandas recognizes that you add the same index twice and will automatically create a *MultiIndex*, hence use the next column additionally as an index.

<details>
<summary>Explanation</summary>

Here, you just have to remember that Pandas allows us to insert rows that have the same index value. 😄 
In SQL, this is <u>**not**</u> possible. I.e., each index value must be unique.
</details>
---

