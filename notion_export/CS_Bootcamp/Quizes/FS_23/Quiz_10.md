---
title: "Quiz 10"
notion_id: "1257073f-2c29-4c6c-a718-a9af4ca867a9"
notion_url: "https://www.notion.so/Quiz-10-1257073f2c294c6ca718a9af4ca867a9"
exported_at: "2025-12-14T01:03:53.669863+00:00"
---

# Quiz 10

# Question 1
Wie viele Diagramme (axes) werden von folgendem Ausdruck erzeugt?
**fig, axs = plt.subplots(39, 37)**
1’443

<details>
<summary>Explanation</summary>

> 💡 **[subplots()](/10c38918e9a84ef79c8040d2fba85e2e#eaf7b9caca0a4167b5e87f638665032d)**
The syntax of the subplot() function is as follow:
`plt.subplots( << n_rows >>, << n_col >>)`
Thus, with the command above a grid with **39 rows** and **37 columns** is generated.
Hence, in the variable `axs` a **nested list** will be stored that contains 39 lists (rows) and each list contains 37 elements (plots per row). In the end there will be 39 * 37 = **1’443 **subplots.
</details>
---
# Question 2
Gegeben sind die folgenden drei Boxplots.
Bitte klicken Sie in der Figure an die Stelle, an welcher der Median der petal length für Virginica dargestellt wird.
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/461e7a15-add0-4599-bc2c-ab3062e85d3d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YYRAOVAB%2F20251214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251214T010325Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJIMEYCIQCBGspEhrcBo%2F72MAJomQX%2Bi0CTDp89y9tAS6xHyG9%2FegIhANDYNUJtCE48TvC%2F0ibeFFFDcBJmvs44fqfx9vlcBNrmKv8DCCoQABoMNjM3NDIzMTgzODA1Igy8QXo5Ap97f1DmxYkq3ANyVQqMxexP3b4vtEkU%2FDVIVbsV4bg2Qmuy%2B1pln70oAtQGvyn5wkGJro9BN%2Fk%2BpdV5D8IBOsreF099JxokApScDMpBRsk8XBOYj2GG4rXgL5KPRzr99VMQ%2B2U4ZbNoh3EaHNpLPNruKak44bYlFxx0mYpxLguWMW5LoAhiMfBH7dtpkoNA89x9VY%2FwQfWH7yISf9Doosv%2B0SS%2F4nI26eRt44vl8y3beQU0SFOsjt%2FvngPkbufmRs0F2cmhtuPsNNR3L4MuJju4knAXKZ8AT6k0vIFuswEFjC6ZqWcUTzcM728RlzA1u7q7e8WilJSz1%2FkQWosvse53o%2BFeiiAWXZSuxqcm11ASLxYOtEMH5czVJBh6OvcKC0xQeHz8s%2F0NCra2L8kO6gHDTM53mTVTKZtOp5U5%2BT15A8i4u4Qyot1%2B2AvU79wJXfV9naGykvZjihzmSW%2FpXtm048oCYY%2FQlkTvwVV8dpBTM73E%2BGhQYtWM5n4HC3CgxoS61ruZNXjytrQCsCOsXs8doRF9ix1lNY2H3UUM8Oo%2FdCO0HYnxoEyk1w6EKnonxON8yGMbPeSqZWVTgfa8rz1LQxFt%2FTZvdGbIVRReYtX%2BJblIb1%2B0xHaOycDiF6IbzoeijdU4VjDilvjJBjqkAfzTFAjzyP58C%2BwL24gGNu1oO%2B12YQzq35n3z97JA8PWQhaR9A24Lu3Qkh0pD294I4nn76A%2FIbiwwxH%2B2%2BW3Ut5kNkvgITZf3VTObIjkeGiteJtLbuKm7n1eUyqExZhHXhprhrqAoGdsuToVVBHVcYaUhkpGgb90E1abI1x5tfTJrOB8PAlCzwSTG81nVmsfjU%2B%2BwFuJcXXBrmI7zuwfobd2S9Jv&X-Amz-Signature=68028f2b6f98cfbddf1a2e89c98a6317ac43e04ae99347dd9149bbff935e5337&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

<details>
<summary>Explanation</summary>

> 💡 **[Boxplot](/6ac6e358ebd649cbab8c4f731dfa5cc8#29b3bf078dde4d20ae32783413578357)**
As the chart below shows, the **horizontal line** in the box represents the Median.
![Elements of a boxlot](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/9ca63491-9ce3-4d62-bae0-fdde85c85fec/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YZCY32C6%2F20251214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251214T010327Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJGMEQCIDreidG%2FiEetc0OT6dtbSIu1yz7yD6r5bEGb1wwdoYvRAiAl4heULevrrYSOnz4EFB2J2CrCvUK5tmXFmeeoAn2g4Cr%2FAwgqEAAaDDYzNzQyMzE4MzgwNSIMn%2Bf6eFMIwXioNBwQKtwD1yHx4IUuYyEI8%2BzoPsD%2Fg%2Fp8E1TCwHYx9fEAAE90b%2F3P4zEqszbbNjflGksdJGad7p5bdME9f0riLu%2BvVjYxIAoscciJ9jtEx3T0V1a%2BvESIwFuGRkZl6LUVmczDQeAfx%2BWbdsQlDOEquT%2F8vjIj1L82Acv0PWvS5XTK0d9kvo3E5wqnOhWCtAc7aJ4wFe2Q2u7Zk3aeFjQAuKlo2yt6Q17SuuQsaUnKnT0rFDb7TyVD4tckftdCnSn7DF%2BuG%2BMYVtCakCHMPRH7aTXcTZ7dWFQcpN%2BxAE%2BVvaUUspwJN6t3RJrpeeoiLJJtBJezwTeB2DlHMvcPLJj0TuqykjRTTIZLORebCpBdQMGw8sy2djGOP3lEwkVvquI%2FI4AXAHRGx9MfPxTfDdPfNBfX9vZArhtLqLO7Cx7r4eVznq%2FiWRqfYL9qmxLWAeOhCEVbsL4lkqFks3CjcN4o6A0K7a2j7hZWW0c1NvgkbjKAoi23EUVZZEV%2BVQY2S%2BBlk6jhSz4Vz6u1Dj8JaSDLLjhP9M6cjfWBMqJpkb4vcPoYfFPoKAZuaJs1on6jqR9mxzPGU%2FUOEry5M4u9m5nw69JmUy4GzgCudflaxRaDzXFtDjeQp2RHVTPEM5iob3zTrzUw%2BZb4yQY6pgFu2yjSKG2W0HwCYcWZmo64WlLXusbqBB6vgIsBJFKl98Ree%2BlMd2XktF1kpS3oHenEEoUnkMq8NknglRGKf%2FMgcubSqN37ysWgj4BvpGFNWa09E%2FOhn0mqHF4i%2BNJtUNm11si3SLLKTUfzdFvHNu3q3E5Dzk7mzbntVPosPmEQGaMBD1unDB855nLdhq58oDeGu1K5DJG2%2BVfX%2BKIyBqwArEFQasbF&X-Amz-Signature=afab22eea19499161c91da0efe13c3ac84c8a63e5ecf1c6df8c03e469ea77f58&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
</details>
---
# Question 3
Das Argument **sharey** beim Aufruf von z.B. **plt.subplots()** bedeutet, dass
❌ wenn es **True** gesetzt wird, nur einmal die y-Koordinaten übergeben werden müssen, da sich die Diagramme (*axes*) der subplots diese Koordinaten teilen.
❌ der hier zugewiesene Wert in allen Diagrammen (axes) der subplots dargestellt wird. Damit das aber funktioniert, braucht es auch noch ein **sharex**-Argument, sonst wäre der zugehörige x-Wert immer 0.
✅ wenn es **True** gesetzt wird, die y-Achsen (*axis*) der Diagramme (*axes*) der *subplots* gleich skaliert werden.
❌ wenn es **False** gesetzt wird, die y-Achsen (*axis*) der Diagramme (*axes*) der *subplots* weggelassen werden. Das ist bei qualitativen Vergleichen der Kurvenverläufe in den *subplots* nützlich.

<details>
<summary>Explanation</summary>

> 💡 **[subplots()](/10c38918e9a84ef79c8040d2fba85e2e#eaf7b9caca0a4167b5e87f638665032d)**
❌ **Incorrect**. The y-coordinates must be given for each subplot. Otherwise Python does not know what to plot (e.g., how to draw the line or how high to make the bar). Also, `sharey` does **not** make the subplots **share the y-coordinates** but makes sure that the **y-axis** across the different subplots is **shared**.
For example, we can have multiple line charts in subplots and each subplot has **its own y-coordinates** (the plotted lines are different):
```python
fig, axs = plt.subplots(2, 2)

axs[0][0].plot([2, 4, 5, 7])
axs[0][1].plot([10, 6, 3, 4])
axs[1][1].plot([3, 8, 1, 7])
axs[1][0].plot([12, 5, 4, 6])
```
Thus, the **scale of the y-axis is different** for each subplot (e.g. top left goes from 2 to 7 and bottom left from 4 to 12):
![Subplots with different y-coordinates](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/3b16e380-4f6d-4a51-9579-054fc1832c97/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZMRS24PI%2F20251214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251214T010327Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJHMEUCIQCKVBw652KEMDb3VqTiap9s5l8TrN4WRRfUDKKVDgQoZgIgJLrla0kAQsgAd9AJIi3eBsWM1z585d0qjUY5C6jeco4q%2FwMIKhAAGgw2Mzc0MjMxODM4MDUiDK0geRUn4WkmKhooECrcA8a1Q6EZe53t%2FHU8YpUNYgHxXtBv6ErBaxD%2FasK%2Bi1X5MNKCYdjQgfdoTLAct%2FDKJW%2Fh31KbA2slrNIPub9NPo6J7IVthpc1qeN0I9qkcO7H%2BXZpDGyjcwiGsXD4lsp8gJeOWYO9MFjMc8pSY3ZizymXZ4ICqd%2BdT4z7HCI4VrCH%2BvnronRk9NpH5HzGnRNlt187M1xsXFSYZ%2BlRCvZONLaGGlsKpJEcscSnh7BEJlFAgynhAOTU4k%2BI2eknleqCm8TLm4L1vXyaRne50CrPsg1KcwfawFAz2DhlMSLshA%2Bg72CNv5VlFkUTjX%2FdyihgKlqkWlXHLFUM1kgHqNmS6nbsmrzzeHbnLd10C9kkOZNl3%2BXpsOaCEKWu4LbZSOpJL6C7TxxVGXVVvC7HBpmvsQNKzeu58Yco3WzLhz8xfT0rJCHI9dl9sIotbt0yzJXPkEn7d6OMz6NVwKD2tpYjNW0bOjmnaSx7nulsHA3bF%2BDar46lzKaSgDZSeC5sqvA6UxvibZV9W4hijYLca7UJ%2FQPQBlEWxH6YOwxGPVB41acPld0E92NDNe%2FqBBBy3s52Ie8UlqlX16%2B9G83w9IHZB%2BC3coef4uPk3wr%2FidSLAwJ6AY0aLbORlboP1FK9MIqW%2BMkGOqUBCr97YoK1NtrvckDwS8sj3oM0SpDec49dkpnvTkGFbt%2FbVA2BJHb5D6%2Fbak1jTq8hWBiprwfxJhxs4MnkhHxtflE9g4q%2B0UwcbKseODOlqBJxFTmIV2WIpd9t%2FbDFeiASajQegULgsgT8muix8hk3OP0fujrOuJV1DPFW2zmHSNnYdpi7RSqDxgYCYuT7a4hPbzdmelcMI6c%2FMgqNFyx9KYYyAvBn&X-Amz-Signature=b245f3f1b2d3470b8d74410d8937ced9c089d0fc12550dbaa4f86bd8bcf2bf40&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
Now when we add parameter `sharey=True` to the first command:
```python
fig, axs = plt.subplots(2, 2, sharey=True)
```
The y-axis will be shared across all subplots:
![Subplots with different y-coordinates but shared y-axis](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/223c7937-1818-41eb-9e48-3aee7bd3bebe/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZMRS24PI%2F20251214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251214T010327Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJHMEUCIQCKVBw652KEMDb3VqTiap9s5l8TrN4WRRfUDKKVDgQoZgIgJLrla0kAQsgAd9AJIi3eBsWM1z585d0qjUY5C6jeco4q%2FwMIKhAAGgw2Mzc0MjMxODM4MDUiDK0geRUn4WkmKhooECrcA8a1Q6EZe53t%2FHU8YpUNYgHxXtBv6ErBaxD%2FasK%2Bi1X5MNKCYdjQgfdoTLAct%2FDKJW%2Fh31KbA2slrNIPub9NPo6J7IVthpc1qeN0I9qkcO7H%2BXZpDGyjcwiGsXD4lsp8gJeOWYO9MFjMc8pSY3ZizymXZ4ICqd%2BdT4z7HCI4VrCH%2BvnronRk9NpH5HzGnRNlt187M1xsXFSYZ%2BlRCvZONLaGGlsKpJEcscSnh7BEJlFAgynhAOTU4k%2BI2eknleqCm8TLm4L1vXyaRne50CrPsg1KcwfawFAz2DhlMSLshA%2Bg72CNv5VlFkUTjX%2FdyihgKlqkWlXHLFUM1kgHqNmS6nbsmrzzeHbnLd10C9kkOZNl3%2BXpsOaCEKWu4LbZSOpJL6C7TxxVGXVVvC7HBpmvsQNKzeu58Yco3WzLhz8xfT0rJCHI9dl9sIotbt0yzJXPkEn7d6OMz6NVwKD2tpYjNW0bOjmnaSx7nulsHA3bF%2BDar46lzKaSgDZSeC5sqvA6UxvibZV9W4hijYLca7UJ%2FQPQBlEWxH6YOwxGPVB41acPld0E92NDNe%2FqBBBy3s52Ie8UlqlX16%2B9G83w9IHZB%2BC3coef4uPk3wr%2FidSLAwJ6AY0aLbORlboP1FK9MIqW%2BMkGOqUBCr97YoK1NtrvckDwS8sj3oM0SpDec49dkpnvTkGFbt%2FbVA2BJHb5D6%2Fbak1jTq8hWBiprwfxJhxs4MnkhHxtflE9g4q%2B0UwcbKseODOlqBJxFTmIV2WIpd9t%2FbDFeiASajQegULgsgT8muix8hk3OP0fujrOuJV1DPFW2zmHSNnYdpi7RSqDxgYCYuT7a4hPbzdmelcMI6c%2FMgqNFyx9KYYyAvBn&X-Amz-Signature=36972990982a2dd34fefe2a84a2c464f368d48014ab79bfad8ce34b482721c84&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
❌ **Incorrect**. `sharey=True` does **not** make the subplots share the y-coordinates, i.e., the data that is shown. In the example above, each subplot is showing a **different** line.
Also, as we have seen above, it is possible to **share the y-axis** while **not sharing the x-axis**. There is no dependency between the two parameters.
✅ **Correct**. `sharey=True` makes the subplot **share the y-axis**. Therefore, the y-axis is scaled to a range that captures the **max-value** and the **min-value** across **all** subplots.
❌ Incorrect. As seen above, when doing `sharey=False` (or not providing a value for this parameter at all), the y-axis are **not discarded**, but each subplot will have **its own** y-axis.  
</details>
---
# Question 4
In Assignment 10 haben Sie mit dem fruits DataFrame gearbeitet. Die Zeilen-Label haben die Namen der Früchte enthalten, die Spalten-Label haben die Namen der Wochentage enthalten, und die Kombination (z.B. Zeile 1, Spalte 2) hat die Anzahl Verkäufe einer spezifischen Frucht an einem spezifischen Wochentag enthalten.
Sie möchten nun in einem einfachen Liniendiagramm (Lineplot) die durchschnittlichen Verkäufe (Durchschnitt aller Früchte, y-Achse) im Wochenverlauf (über die Wochentage, x-Achse) darstellen. Wie lautet die zugehörige Codezeile?

plt.plot(fruits**.columns**, fruits**.mean()**, ‘m:’, label='Durchschnitt")

<details>
<summary>Explanation</summary>

> 💡 **[plot()](/10c38918e9a84ef79c8040d2fba85e2e#c9af98cf80ba468aa1947825383ef41e), [.columns](/1867045b058343e1a66b677961515907#b56cca6739ca4649ab31ebab1ee61f83), [mean()](/1867045b058343e1a66b677961515907#898be62444fb4cf5bb07bbb36bdb94d5)**
The **fruits** DataFrame looks as follow:
![DataFrame fruits](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/d57f73a4-7024-4ebd-93d2-bca3d6b7d248/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664WQYHWVN%2F20251214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251214T010328Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJIMEYCIQCS9sB6ozJNcbTc3D%2FunIL%2FcXv4XX9iVCBRaJ8KGLKXDAIhAPAjbb15v1J0Oiem8Zi6wrUVG29ttJ1MyG%2B4SFiXSEtOKv8DCCoQABoMNjM3NDIzMTgzODA1IgyQVcY8Kja1cd8sV%2Bwq3ANGFZSDER02bhZ5jgjNdi%2F8HlihebB6F0DtGIrmEAyzOJ%2FP8syEOuxhpYniM2TJITQhe9OOqPaIx2W3u85tiS7CMJ%2FY%2B7Jv3XmTZCh2Y9mxkrNpM%2FBZxqCDwNCIFkJ5BYQAQEfgjSu5x0Nyvs60Cz9VWBmtafX%2BruESjbZBBnaqOm%2BN84XmVAXLZN%2Fg7GHLo4XKBYy0pJr3Ovr9ALjw%2FQDhnbxDDOwYH1vns9mevnDkFplY5LIZm9LBFeK%2FEgRkrkyx7wvPR52RjFSxDNZb1w3OhwxnectF9kUM%2FuAi%2BiP%2F%2BsRsuPqQ0D3lx8QhCOyFeIrt5bWpTFlKUbZhAiCo54gd3Hd92b1mZ%2Bz2gzSexg0q7J8WDtXyOEL0KdoMeIdoPgccVBnQcUlSyj5g15rnzL%2FTfpSBebRsMGjLmfcQsJqDdydT3dtJOJD6ZnSuECfG25fIP7cb6yVlDL5yoIVPXbMymRuAcPyrDmIYyY3AJ9thPeMD4nf2z83BeB06OS5jDQdkM9Wt3liUnCG18iNGyekkqzOXRWz0qKnVpKPGcGCre3wIYAz%2BNv0nR%2Blnsyee6g6HSOGrIsNThpnASQhpWcJtt%2Bb9A0Rzn5eMgpme9Jwee27ZO9N6syOdjI3gKzCzlvjJBjqkARiS45n8Fjs8E2Swio%2BjA5K1x9L4VC4l%2FuCt99eLVCTaaR32IC24N80vuKQB6i7i3X%2BRnrPdpXLBtLJFI9orWt95cmmDHQf17lr%2B7IAcxLOWp30yuKFQeA7AEs7fIKDayMWhd2157tQWh1puUWodmy%2Bn1iV5rLjnXLyvy7e6%2FrAi1liEkQrDZWzhRu8vxQe5cNpd%2F2y5izz7FWdcxytD1Wzi0%2F1A&X-Amz-Signature=ab551d9a2750341d47630f2320c38febc3c5bcfd7d79ee447d882ad0790eafc5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
And the Lineplot that should be generated looks as follow:
![Lineplot showing average sales per weekday](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/844d157e-d8b9-4553-af0c-192d8b1f77ce/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664WQYHWVN%2F20251214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251214T010328Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJIMEYCIQCS9sB6ozJNcbTc3D%2FunIL%2FcXv4XX9iVCBRaJ8KGLKXDAIhAPAjbb15v1J0Oiem8Zi6wrUVG29ttJ1MyG%2B4SFiXSEtOKv8DCCoQABoMNjM3NDIzMTgzODA1IgyQVcY8Kja1cd8sV%2Bwq3ANGFZSDER02bhZ5jgjNdi%2F8HlihebB6F0DtGIrmEAyzOJ%2FP8syEOuxhpYniM2TJITQhe9OOqPaIx2W3u85tiS7CMJ%2FY%2B7Jv3XmTZCh2Y9mxkrNpM%2FBZxqCDwNCIFkJ5BYQAQEfgjSu5x0Nyvs60Cz9VWBmtafX%2BruESjbZBBnaqOm%2BN84XmVAXLZN%2Fg7GHLo4XKBYy0pJr3Ovr9ALjw%2FQDhnbxDDOwYH1vns9mevnDkFplY5LIZm9LBFeK%2FEgRkrkyx7wvPR52RjFSxDNZb1w3OhwxnectF9kUM%2FuAi%2BiP%2F%2BsRsuPqQ0D3lx8QhCOyFeIrt5bWpTFlKUbZhAiCo54gd3Hd92b1mZ%2Bz2gzSexg0q7J8WDtXyOEL0KdoMeIdoPgccVBnQcUlSyj5g15rnzL%2FTfpSBebRsMGjLmfcQsJqDdydT3dtJOJD6ZnSuECfG25fIP7cb6yVlDL5yoIVPXbMymRuAcPyrDmIYyY3AJ9thPeMD4nf2z83BeB06OS5jDQdkM9Wt3liUnCG18iNGyekkqzOXRWz0qKnVpKPGcGCre3wIYAz%2BNv0nR%2Blnsyee6g6HSOGrIsNThpnASQhpWcJtt%2Bb9A0Rzn5eMgpme9Jwee27ZO9N6syOdjI3gKzCzlvjJBjqkARiS45n8Fjs8E2Swio%2BjA5K1x9L4VC4l%2FuCt99eLVCTaaR32IC24N80vuKQB6i7i3X%2BRnrPdpXLBtLJFI9orWt95cmmDHQf17lr%2B7IAcxLOWp30yuKFQeA7AEs7fIKDayMWhd2157tQWh1puUWodmy%2Bn1iV5rLjnXLyvy7e6%2FrAi1liEkQrDZWzhRu8vxQe5cNpd%2F2y5izz7FWdcxytD1Wzi0%2F1A&X-Amz-Signature=f390fc21a7995c667309eeb5877f6cb6d9de72ab7cd8f2aa1ee869e9ee85f010&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
We can see that the Lineplot show the average sales per weekday. 
How do we get to this plot? 
We know that the syntax of the **plot()** function looks as follow:
`<< axes >>.plot(<< x_data >>, << y_data >>, << format_string >>, << label >>)`
Thus, we always must ask ourselves which data do we want to show on the:
- **x-axis**
- weekdays
- where are the weekdays stored?
- in the columns of the DataFrame **fruits**
- How can we access the column names?
- `fruits.columns`
```python
Index(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday',
       'Sunday'],
dtype='object')
```
- **y-axis**
- average sales per weekday
- where are the sales per weekday stored?
- each column in the DataFrame **fruits** represents a weekday
- how can we compute the average per column?
- `fruits.mean()`
```python
Monday       12.000000
Tuesday       8.666667
Wednesday     7.000000
Thursday     13.333333
Friday       24.333333
Saturday     63.000000
Sunday       37.000000
dtype: float64
```

Therefore, `fruits.columns` is used as **first** parameter and `fruits.mean()` as **second** parameter.
The **third** parameter `'m:'` is a format string that tells Matplotlib **how to format** the line. It has the following syntax:
`[color][marker][line]`
Thus, in this example above, `m` is the color and stands for **magenta**. `:` is the line and stands for **dotted line** style. The marker is skipped. As a result, a **dotted magenta** line is shown in the plot. 
Finally, the **fourth** parameter `label` gives the dotted magenta line a **name** which is **shown in the legend** in the top-left of the plot.
</details>
---
# Question 5
Ordnen Sie die Funktionsaufrufe den Diagrammtypen zu:
| Diagrammtyp | Funktionsaufruf |
| --- | --- |
| Boxplot | sns.boxplot() |
| Streudiagramm/Scatterplot | plt.scatter() |
| Streudiagramm/Scatterplot mit Regressionsfunktion | sns.regplot() |
| Liniendiagramm/Lineplot | plt.plot() |
| Horizontales Balkendiagramm | plt.barh() |

<details>
<summary>Explanation</summary>

> 💡 **[boxplot()](/6ac6e358ebd649cbab8c4f731dfa5cc8#bd387c5aad634663b85b90e663417f85), [scatter()](/10c38918e9a84ef79c8040d2fba85e2e#8a2779f2348c459db050ee81519ebe28), [regplot()](/6ac6e358ebd649cbab8c4f731dfa5cc8#2cc0db7a99fb4b648afc870d00e8059d), [plot()](/10c38918e9a84ef79c8040d2fba85e2e#c9af98cf80ba468aa1947825383ef41e), [barh()](/10c38918e9a84ef79c8040d2fba85e2e#93afc91e1e5e4f1e93355554eb690c49)**
There is not much to explain here. Just remember which function call creates which plot. Also note, that for Boxplot and Regplot the [seaborn](/6ac6e358ebd649cbab8c4f731dfa5cc8) library is used and for the other ones the plain [Matplotlib](/10c38918e9a84ef79c8040d2fba85e2e) library.
</details>
---
# Question 6
Der nachfolgende Python-Code soll ein Balkendiagramm mit folgenden Anforderungen erzeugen:
- Es soll Balkenpaare aus je einem blauen und einem roten Balkendargestellt werden.
- Die beiden Balken eines Balkenpaars sollen ohne Zwischenraum direkt nebeneinander dargestellt werden.
- Ein Balken darf einen anderen Balken nicht überdecken- auch nicht teilweise.
Um das zu erreichen, müssten noch die Breiten der Balken definiert werden. Welche Werte für **width_1** und **width_2** sind hierfür zulässig?
```python
data_y1 = # Bitte nehmen Sie an, dass hier eine Liste mit int-Werten definiert wird
data_y2 = # Bitte nehmen Sie an, dsas hier enie Liste mit int-Werten definiert wird
					# die Listen data_y1 und data_y2 erfüllen folgende Bedingung:
					# len(data_y1) == len(data_y2)

# Hier müssen noch die Balkenbreiten (width_1, width_2) definiert werden:

data_x1 = range(len(data_y1))
data_x2 = [x + width_1/2 + width_2/2 for x in data_x1]

plt.bar(data_x1, data_y1, width=width_1, color='blue')
plt.bar(data_x2, data_y2, width=width_2, color='red')
plt.show ()
```
Markieren Sie **alle** richtigen Antworten.
❌ Option 1
`width_1 = 0.6`
`width_2 = 0.6`
❌ Option 2
`width_1 = 1`
`width_2 = 1`
✅ Option 3
`width_1 = 0.3`
`width_2 = 0.3`
✅ Option 4
`width_1 = 0.1`
`width_2 = 0.1`
✅ Option 5
`width_1 = 0.5`
`width_2 = 0.4`
❌ Option 6
`width_1 = 0.1`
`width_2 = 1`

<details>
<summary>Explanation</summary>

> 💡 **[multiple barchart](/10c38918e9a84ef79c8040d2fba85e2e#4a56b6e5ec454ce4bda78bcd8133eb4b)**
Let’s assume that `data_y1` and `data_y2` contain both 5 numbers. Thus in total 10 bars should be displayed in the figure eventually. 
We know that the list `[0, 1, 2, 3, 4]` is stored in `data_x1`.
Thus, the bars from `data_y1` will be inserted at following positions.
![Positions on x-axis of `data_y1`](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/0e86d183-723f-43e8-8a93-b286b4064a26/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46654XQ5CLY%2F20251214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251214T010340Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJHMEUCIQCWR4d8o0fC5sXUQCn8EUSnYc6fB%2Bidveg6JElX9cbXFAIgCl5ObK7I5g21cPG8wp3u4fQmzr1Q8Y4ukDmpSV58ZLUq%2FwMIKhAAGgw2Mzc0MjMxODM4MDUiDFSr5ougNGtmZqjkXSrcA2pcxGH7obxOIlxoEHWGkdRhu%2BLvCDW3E7hwsjdLzea3UWfwZkYEC2On9Wkj3wXjpBnN63G6FXK14VNGbyTf4ev7aLsHB6%2FCIKwBd32Gax%2BDMW17%2B%2B28iHWkVDILUxNeuwNMAcvQWo3b7ZIWWEt0WUJA%2Fu18HWdpca8EYsQCGDPv5cIj1GYe7PArsa0Skby8qoCYWFKkcKqMUGCrQDPqSHwOvZyGBYkMeR6QmnDMKcG9kzZyIwpBatLtR%2B2dRHhv4Vakvy1AugLs9iJUVydPP2v%2Bl6H0flCk5GhZhFavu9EBJ%2FtkeJdoyLu4c6ZqMNRVJRBJQBSDrIqeS2ZF6L%2BXOoL%2FuBq2Lg3pBt7vvEDEn1%2FBWPdfk4HE7oT1rli1CzOU3Y8%2BbtNcfgDZDmtgNJdpeHx6qpo0Yp9LsvOmPQ9j%2BPGbokAo0z0BrxYIZq8%2FFWtIU7EWTqO2BvJzPe1woq%2BYriiyQZ8725YtviK851x5IEJqC%2FROprjdR2XbwY6%2Ft3qzfxvydUFWyyjF9taGJ2D2mA51fMMkGtA7f1pN14zpMbUWMVHvehIgPQzJuw0owBU2wCVvOqyNXgSgROrugXWujQFa8Sr27lX2uREh7giY84oPzr53FCsCyWemTYuzMKqW%2BMkGOqUBgp1D0at2HAktaW3Bfi9zZF%2F8jOmYopMtV6N%2F4W%2BbXw26eQf2gD7JJMcwtiU4JKKMsh6lrSlxhY7QC9mXd1DRhS7eHlz%2Bxve1WH%2F8XFImUIs0DDad4xelfY9ojSDbNdtwC27Aju4liPQYzIMYGbQzZAIOUtqseFsf0ea6poFwkEHQwrUnbW1JolfKI9SMW%2FNNpqdFIy%2Bx%2F3ovx0EXfSmbnxQaqtwJ&X-Amz-Signature=86516f9fda5542b50379e8be7bfd0da9aaa5a6dcd02aa63ab2a0a1583353f67e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
The question is now how to choose the correct values for `width_1` and `width_2` so that the following two conditions are met:
1. **not overlap** of the next bar group (where to position the bars?) 
We know that the positions of the x-axis are calculated as **x + width_1/2 + width_2/2**
Considering only position **x1** (0) and position **x2** (1) we must find values for **width_1** and **width_2** that meet following condition:
$$
0 + width_1/2   + width_2/2 + width_2/2 <= 1 - width_1/2
$$
From where is the last term width_2/2 coming from?
0 + width_1/2   + width_2/2  is the `position` where the bar of `data_y2` will be placed. However, this bar itself also **has a width**, i.e., will **go to the right** to some extent. And for this fact the last term width_2/2  is accounting for. 
1. **no empty spac**e between two bars (how wide to make the bars?)
This means that the **second bar should begin where the first bar terminates**. We know that the first bar will have a width of width_1. And we know that the second bar begins at position 0 + width_1/2   + width_2/2.  Thus, we can formulate the following condition:
$$
0 + width_1/2 = 0 + width_1/2   + width_2/2 - width_2/2
$$
We have here width_1/2  as the **position on the x-axis** of a bar always represents the **middle of the bar**. Then half of the width goes to the left and half of the width to the right.
<u>*Note:*</u> If you have a closer look at the second condition, you will note that it will **always** be True. We can simply **remove** + width_2/2 - width_2/2  as this **cancels out** to 0. However, this is only in this exercise the case. It could be that the x positions of `data_y2` are **different** in another exercise and then we would need to update the formula.
Equipped with this knowledge we can now go through each possible answer and check if the conditions are met.
<details>
<summary>❌ **Incorrect**. The bars will overlap.</summary>

❌ <u>Condition 1</u> → the bars will overlap
0 + 0.6/2   + 0.6/2 + 0.6/2 <= 1 - 0.6/2
0.9 <= 0.7
False
✅ <u>Condition 2</u> → there will be no spaces between the bars
0 + 0.6/2 = 0 + 0.6/2 + 0.6/2 - 0.6/2
0.3 = 0.3
True
![Output when using `width_1 = 0.6` and `width_2 = 0.6`](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/0a3532b8-7d9d-4d1d-91aa-479f5c2ed59c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46657JYOSIC%2F20251214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251214T010343Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJGMEQCIDfmHDOeMtlOtSUnrxEFP3NXkQMbHzZcjHvnWI5NlpWcAiB1cRTlo3VUDXolScxnqPzbZBgEqkhJRJxmf2GDl0Vj0Sr%2FAwgqEAAaDDYzNzQyMzE4MzgwNSIM6Tg4UDqv5poBw90lKtwDpfYLQv8MPZY8apq3at5%2FJZhTkM%2BIIRZttx9TqeDxTQ32qS%2FC2f7Bse47W67Xp0knUbw80ucUerZTrc2AhKIpCjr9C8UqUCBgRZvHfpuBJhl2bgsy618wpAsb3UE%2BWJv5DPJoDrHb5hbuEriySgpbls6%2FT%2BrccRdz2BsAFAy7esY0i3cBHjS3d9CtsBUO9ypO6yekP7Kh4%2BtqnUSg02v%2Bft70xcYgKCgkkkgYR%2FuRREVrLvyKKMKQfeWSnaLwv5J4GFFxIgdkfb1RJbF6Lzpyw0SEDtsb0sW1y4N9f%2BtNNI57q5Tad%2FCZtp9jTZ7ZBWmEgNaQDxSUZn5b29zMTW7u2lkEo4vr1NdA3%2BsXMFWZ%2F%2FCjpuP1ViJFr4RdgffcJfHdc3FUOZtdmHQJJUfD%2Fmr24FMIZvUpre2TBeJKkYmEu8i2Lck0LFB6wScrvVg1AAvbeuy5u83ZQwUV9m16WIXBP%2BD3UI4tZ%2FAzyCnwvtWXXJ51jpt%2BXBBPO7M5aYqAM7xdqbFDgYacbyZb6x385v%2FJ1lRp7NbwijmDVv0WSomVzi2kFr7RKpshOkEX7gSQcMV6MWUZ2gZJkdAtzIrXgQipL6KJEC6sPKEgZ6TrudwHDrBHz6RiSK%2F8EQuOxcMwmpf4yQY6pgGne10K%2B3f8L0l%2FaT8IlAnayEJ%2BBOxt9gWOLXFKoMxs2LOcBp%2BfTWu2TCfNrdYZitA6wrZ5biymVRzR3LczpA24O8qryetbF3mQHUyvFHLldFdXgCyYaIMbhMTKeE7EKfigr1kvh2ZPAAoMx7hvIO4LHPywl9ybzghcjRddEWQfg4JnU8%2FlJK9QKdMwKKBbgG%2FXzCkAldRHOTo14hVJQydaeuGIHa%2Bx&X-Amz-Signature=e2ee12611204e91a37b88288d08e5da6c3ab0e828e3d6f448abadbe315312334&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
</details>
<details>
<summary>❌ **Incorrect**. The bars will overlap.</summary>

❌ <u>Condition 1</u> → the bars will overlap
0 + 1.0/2   + 1.0/2 + 1.0/2 <= 1 - 1.0/2
1.5 <= 0.5
False
✅ <u>Condition 2</u> → there will be no spaces between the bars
0 + 1.0/2 = 0 + 1.0/2 + 1.0/2 - 1.0/2
0.5 = 0.5
True
![Output when using `width_1 = 1.0` and `width_2 = 1.0`](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/d1f8d14e-3260-4c15-841e-a8f5ad99de5f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XCWOQKZ2%2F20251214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251214T010345Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJHMEUCIQCBQcahLBAUiJ0iQbm59hsV0UtrVqdfNuC9UJza%2FgK2wwIgRCPIhy5CIgUPVEbAVhOJBhpumRC1bBoiivuwLSJ3Mj0q%2FwMIKhAAGgw2Mzc0MjMxODM4MDUiDGmilvvavg2El0tz%2FCrcA%2BKoDn%2BFt2GofOu7huTX1Hm1gbTnDu8zLOlpiWMvGpJbwybYWKkIsnbLp7z9jIAjl4061xFjZVYVTDT0iWJiihT0INDB2q967n4hklteIgegWmGRhaTXaEqb9pLFdt8FkXySSJ8i7glkgUb8vP4eQD0KnqXsMr9U1RUtykCa492G9yni5Tkl9GD9Her2ZTLAUjnjYqeAN%2F%2Bg7cxG38BNd4u2snsrdVpUlwuUTyeg5QnAMfXL5bLeYWCdzMTeik%2F6RtAW36xfisGd2hKBg3RPGHkdcoXk%2FKcATxqQh776RLxGuQ%2Fu%2B4UoqYVLV2tApnrQQXyE7z9g8uSD60LXKAtSxYpLVbmMBG6djBfUI7i38bWNmzTOo5cWUsNtDEhQT%2FWgdeW5FfzQfiVV3bfhXPki%2BNwMNONDn3igapLgaAcMx2oZPfVNkl%2B3Ev%2FYjM45flxLO0vupGFLcaon8VC8MfXbjTu74gfogcTC4odc6BUc4ER1IXQYruDfmzXqAXQCbOzmBjh6nSnqrAZ8IDlA8XjwM2VF9Z5QgtGoWddf0XVU3UPm5PorYQcgyQSBHay%2FTZPgzf4BHcxv%2BemIlXGkaLeeRdFhMmx9NbnSUz98Yd0WH8yGUyNlNYlaPVtSPIexMIiW%2BMkGOqUB5hZx0Z2HI%2F7OcMog8PboQcdVmwcglqO9W9VQ8bGZwSJuCOWpjneaDLEY%2B8P2iBEo%2BmjPyg3LfYZ0ZvNS08eL%2BSaiP6rCz75h06MXKCV5F%2FiyQXdY57CPaw4nMEoWAywIH0JrDaeCX0rwunSKgVTAMyhw367BJ6OC8vPuR7A1DJTyXM3228hAPE2L1nn3%2Bt2fkTKJciLdirr5TP09Dkl6vsCSWJyU&X-Amz-Signature=8fa1ff5f3eb0bf6d0ce30b1c91bf78810b9989d666e8259861a89b5a894533a9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
</details>
<details>
<summary>✅ **Correct**. Both conditions are met.</summary>

✅ <u>Condition 1</u> → the bars will not overlap
0 + 0.3/2   + 0.3/2 + 0.3/2 <= 1 - 0.3/2
0.45 <= 0.85
True
✅ <u>Condition 2</u> → there will be no spaces between the bars
0 + 0.3/2 = 0 + 0.3/2 + 0.3/2 - 0.3/2
0.15 = 0.15
True
![Output when using `width_1 = 0.3` and `width_2 = 0.3`](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/3d9aa130-4908-4a45-8f67-21824f1a2471/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667R5OJRQO%2F20251214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251214T010346Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJIMEYCIQDIin0wkAfjbg4WG%2Fyg4mDqQE4wapf7TwvWQNAAceVX6AIhAL57%2F3IJL%2BWjyh5N0tLqFbavPIPoQzU0j3zTuNoRu5eCKv8DCCoQABoMNjM3NDIzMTgzODA1IgxbbnwheLxcfJhfkgwq3AOMTxOxTL4EbiWDibaY2RkW5gMgcONjcALohc7Cl9caAQzahwp4m64HXyma9sG4rXT5eve3sWXWHD5CaWSJMsX2nb%2FIJnfBjXr16lDb7rEL%2B5Iu51MTchhi8%2BQewkoiIVuJOxqvrJ1j5A5qvxUDJEyDgNq8eIbt7JrTT4ASgeUg6xQXFZ8qowOys583r0Mn134UOUDLt2Xwg2s90PuL%2FbQnMKwm%2FNTO5REBnRv57NKOH6IH9BKhUXy661gyW5rAqUvfD%2FHdSXJONWIco0Wk94L17yRBR3111HxbXnZ3aRTY55sYzCZJIu434gccsF2%2B%2Fb237%2FCgYzMusNP%2F4IAMBeToq%2B7VowWdewqWtsNOGtFNqD5hPNcezcF11TinKDKWQgR7of6DmnOy2mMSITCs7kJDe9q3qPAS30s3mNx1mq6mbSGftL7cCV9LAS3SN1rJTU1ayo1CLAfkirfQcCfHCNTnSWwCqAIBLC8v%2BtB%2BjAejZVzy7eL1zDUEeWLEcO45mqA1JKpaQMOEFK6idPq1paVsKPT5MFOu6wFY9O3BjE36dOgbh%2Fr2BxTQtX34Es9uCNGk%2FGx%2FvUsbpOO3MyT5d56yMfVHUpakg49O5ojcmHI2bLIhVO2cynIuBaNv5DCqlvjJBjqkAfM3bIk7vzr%2BGkWke2OvznyIVWAsx0BNtj%2BULfhVR2iDtHzVomiFSMGXRw4f7CuamyuZvN1HpzmggDXpwLy5O1bavAPwiPBgwqK0ZYk%2FqT3q5%2Fsggr4Fmeq%2BZlKjfYLtQjIJ7S4p8NEbpGqtP6wv2JG4WNaE9nsfWJKm7t8SvDCYB6XswOwTbQhy9R4IF32OGJxG2iVETmMge7tGjS7UQDTXE%2B2A&X-Amz-Signature=fe6adc96cdc4cfd22644e3001b8ad7a280fa0341ecb81f604a7ae492e9259572&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
</details>
<details>
<summary>✅ **Correct**. Both conditions are met.</summary>

✅ <u>Condition 1</u> → the bars will not overlap
0 + 0.1/2   + 0.1/2 + 0.1/2 <= 1 - 0.1/2
 0.15 <= 0.95
True
✅ <u>Condition 2</u> → there will be no spaces between the bars
0 + 0.1/2 = 0 + 0.1/2 + 0.1/2 - 0.1/2
0.05 = 0.05
True
![Output when using `width_1 = 0.1` and `width_2 = 0.1`](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/b54fa942-f8ae-42a6-b581-af1c834b2598/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QHXTQSMT%2F20251214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251214T010349Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJHMEUCIQDDvvI9jOffdAmFzOW1pbiUXdyO8z2uti1ExSHRSNr9HAIga42YntWJUhAJxJya7eKIhSE8x5vm6otY15Ug4A2wxEoq%2FwMIKhAAGgw2Mzc0MjMxODM4MDUiDD4yYMnVdTqKpytgbircA34UGnO9g4AhO4bF2mTaLgMCJzSuoZMSgEHwGGiEX2Q3AZT45NnOuNtBMAyU3y6cA2kzF52RwLdeT2nvBZ3Ue6kClsh5Dfx0YoH4l%2F0jccYDSadKkQUSNB7M29Q9j0VHYJPdDqi%2B5pzAHZ0qjgpVcL6bbA6ZE3gG0xP4g%2BJrbsmcIrhfs1TtxklCPR3WFXX1mH%2F0XkfbDe4siVGYnl9X1cLHKycdpiLX%2FkSfzD8cDLiVzQyBHTiHJqSPSZ8G6mEejt%2FgRMzNJTWvzw3Q9o%2Be6iK%2Bschq%2B5N8TwlcQLcV3qQoKxOJhLcUWO5NqOywjbzblEH9RZ29PbD2mwi6y5ytNmbkmkVwvHdD0k4%2BiyXWhs0qdIQYxnKcTiQtFH3j39ZS8QS2Fd2o9vExpd%2BhUCu1TIGeKICheRMDJFLJbJKrfoeCabHiWAkxBlYLG%2BVnQI1qJk5LLt7uLmdUuOENNwmooN3WD0N4Thef7eRHAL7hA6NkuVXxDdV%2BYnZwhgJ0d7oL2mx6V14O95zHpTQBczGg6FU4AbKBH8Pb9HwoC1UIbPkIw9%2FRRvdZ%2BXUCun1%2Bt5iFL1SsZJseCGkQgfz%2Bdw6%2FIxe5a75XxZ%2FQWOV4zZkFWfM%2BqJXzKQs%2By21q1zA6MOGW%2BMkGOqUB5iaQEYWcAPp48vm0TZQLp8nb%2FrYPLzshqFp4xM9DqlrsDg3mAWRG4byLrHj3ns51dWGSQwMwhaZQxf1coQbU1iOpu%2FWPRBsc%2BG1MaiMLGpKzH6CpNVox6oIvVM0n3Iuaff0%2BaeDkfeR2Zonw6%2Ft8oIQEkFPzc%2FR%2BmJYMwxxMMhIgdrWS6aJeQi1KweG9kTHTbRd3H0syF1pd8VhXIy7nQFQKpws%2F&X-Amz-Signature=ac71f457273df7ede39607419200960e4c747f3a408aeedc37b6cd0548bdcfee&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
</details>
<details>
<summary>✅ **Correct**. Both conditions are met.</summary>

✅ <u>Condition 1</u> → the bars will not overlap
0 + 0.5/2   + 0.4/2 + 0.4/2 <= 1 - 0.5/2
 0.65 <= 0.75
True
✅ <u>Condition 2</u> → there will be no spaces between the bars
0 + 0.5/2 = 0 + 0.5/2 + 0.4/2 - 0.4/2
0.5 = 0.5
True
![Output when using `width_1 = 0.5` and `width_2 = 0.4`](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/c8e54f56-f26c-446d-947a-35788889e1d6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S6GTKHHM%2F20251214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251214T010352Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJHMEUCIQDF39Q8vXecaExiEK9IEmjCfPQkqjAzBhIuV%2BbSJrMAnQIgHDY794aT1spBMvk%2FC59iUonh9lRNE38HLBq4DiJxhC0q%2FwMIKhAAGgw2Mzc0MjMxODM4MDUiDJLNbxaZqYIrNWQ7TSrcA4yVPm%2BopSy1GE3MqdsslS07WLrqDQjwckuLZ3lWK%2Fsau6ikGc8CGwLBSFGk0FgrWwvBtrr20RxZkX3AIpm3o%2BL7GxPOAHH5vABxD7%2FvSFvKhzg2rG2dvQKCD2x41zPmoDI5eJ%2FoUPp4YkYfRKnMmt7nYm8INkX3KZ4xGsVZ5lDYEZchf9Pbuznhu3VW0MNt0DgpcQIQTAkvAY3TGQ3zUtYCKY5mPQrHtjujesiqqMZb24Fg3NuKi7Oj9SxBfEQCKyfMWTxixHPSkL%2BeseJ0HOtVLBbLgq338r77HAGlBk4F0ar9T042p%2FbcVRxRDxhhNDXKsbdexGv2L4q0cVgBBGacGdkSaba9Sx0CBDGTML3OFU6psrEIkT4alXmPqmoDUMrPOO1ICaB9%2BNAV3V9XGKj4%2BmDu%2FbrdLJxdnG76v5qox47qL4Ks6tawq6hvI3mu7Hr9%2BTWpC8qr1dShwZoEEC9sWcluEXNrZjKiwPUOgF1%2FWIkb%2BlmtMvmeL40r2T7nhaZvr3ue9OmCfxfOnPkNtZ%2B%2Fhi3ra7Gf8zNOe72qCq7fTblwVQbJ70xmxv1Ad%2BTXNqYqzn5A7itQj1eAvPqy5vrPWwe%2FtPPbPoNFUtm%2Bg14y2enNfpgW1IF9d%2FecMKSX%2BMkGOqUB89%2FdTXHBKNpYucIunJOmdGmjE7N1peUi9Wmb8bt6WO44E5a6kT01QBRru4BaB4ojA28gKEK36Zq5UfrqjFAISQLAMh2w3yaoH6HEseC7%2Bv3j10QjmyzP0iuiVfn%2FniKC4zCsV9h0H9N5N4AWNNoZZbaFdXqYg2Bg0kghP2VjZqhN6CHQ8lgTQ2fNiKcqvhCk23j6vqLWyeXF9JIDgW%2BW3yc9o4AV&X-Amz-Signature=a417c94ea9e669c47e1dcc9e4c3dba00d34cdfbbde3c8676fc607b7cfa453ec7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

</details>
<details>
<summary>❌ **Incorrect**. The bars will overlap</summary>

❌ <u>Condition 1</u> → the bars will overlap
0 + 0.4/2   + 1.0/2 + 1.0/2 <= 1 - 0.4/2
1.3 <= 0.8
False
✅ <u>Condition 2</u> → there will be no spaces between the bars
0 + 0.4/2 = 0 + 0.4/2 + 1.0/2 - 1.0/2
0.2 = 0.2
True
![Output when using `width_1 = 0.4` and `width_2 = 1.0`](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/3a9c70a3-e6e1-4800-b8e8-1bc30573319b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RWLMGJNN%2F20251214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251214T010353Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJGMEQCIFw13S4dq%2BjolaW0LWEmG62NLFip4knGt4TU5jR8o58PAiBeztNFQr0ua5zr%2B16hDu8W4kj3BOC09bAuB2u%2FIvyGRir%2FAwgqEAAaDDYzNzQyMzE4MzgwNSIMU1bqT58VbPJ0Z4w%2FKtwDDQ7a4N0tZYRl4PLv06HIpaqXNlVm9XtSOqqDrAgJjoJrTr7i9zb%2F7U43dzFtGkcYxUgJh8ibPY4FLbtgNUK1Tz0iqhgFeKqIVqJZxreiaFQ4KgunM2NtSVnXy3DiZWCUTSWvcQ89i%2FqJYAO2kS2enFP%2Bs4I9OdyxDXCLrpSOn4pIG3AUclNeqHDeplHPQCDmVYovirws40brEb1dDIx5yv3aED1LDRGQMNfrqzIEjQWHbw%2BxzTtfAHKnrJW0FHdXRG%2BgVipluFTM%2BZfvNHTfJC4QyZGVvZr103cPsEJPbFHTILxQCoT%2B7gnuZYVJkuPfCrnQP2rIGP82Tg2oT2VbIQW6vpT0pXrs8uZ8%2FTu0NFVZcs2SOHRCPaQEbO%2Fxy2jOgnTwF3sx5m3wI%2BtsCla9X01j4bn1m8slXdPG2ZUF6jD%2F2u3X8w7Kppz9ePyP0uNlOVXZRdX4NGmxRlCO3vcLYdXO%2BropWBr94Xo9KPDCf9jdjHTv6Bp1gz7xvil0y4YK5MaFhlF6H9nsToGhcHQlvE6KPsucFQ%2FtFtHFYDtTRLcraqpQYSmhkiv0VXpnLSwnuEYegJ5anCELCVYLSXLE6eLMpxPLHblfg2i3wK9K%2B0dUNi7u%2BojnJrBJJXAw4pb4yQY6pgFDWbhApM2etMcWx5VdJMI%2BulFCOUNrZwwNCCofs1ikvbK7R%2FXZMHJXoL3t6Girj8MP1Fr%2FTvcpLEGypxxWhx%2F2Nsjy9tBU%2BBaIKQyYCNR1nKXei6s4TPB8mDJifNfykjU2ztS4Q0Ij5hJfuf8NVZXcLHtnGe86YhkGgetvrw%2BtDKuTudotELBoGudV3gNIzIQQZhgRigJY7NLnsDV6Xw3VM%2FvZKCSO&X-Amz-Signature=ec510070e9090c2992b9f6de1f68aab9bfe7ad4d5ee4edb42dfa06b3258b2608&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
</details>
</details>
---

