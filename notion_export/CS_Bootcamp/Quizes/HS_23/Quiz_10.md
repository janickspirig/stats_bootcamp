---
title: "Quiz 10"
notion_id: "43798974-fa1c-41b6-8f18-a46d346e7715"
notion_url: "https://www.notion.so/Quiz-10-43798974fa1c41b68f18a46d346e7715"
exported_at: "2025-12-13T23:22:24.924914+00:00"
---

# Quiz 10

## Question 1
We have the following *pd.DataFrame ***df** of fruit sales. The code below was used to create the given figure.
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/5ecb8592-f208-42fa-ba9a-7e451775c803/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46676BGLV75%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T232220Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJGMEQCIFT6VXdM55%2B0xtheI%2BJrYVevvuhXDzNXft9rEixeubXXAiBT6d4LKApf%2BMmXuju9DeNud2wyL5uxKJYLwMF91dD%2Bjyr%2FAwgnEAAaDDYzNzQyMzE4MzgwNSIMiM7%2BowZfOUWw9aERKtwDuJCXD1Q4DtsaSk3HBpGc1YPAjK9ErUiAWkbb5cjp9ymB9HntA2iACwHJHxBrnbD9wzXfjLLMtF6s4%2FAeQtz%2FllxslC0gSzRarY8XF8G9xYBdAKdkBVAVwmCY42%2F4qxUqSOg1P9m3CFbGmZqNun8QIvMAgnRsGQADRwj92j2xHImmWHDzTrhKcrUZ4PwIdpmDyxvLq5gYOqWsFz7ihSyYr68Eh0YZ7TcdwtstPsKoUrTLVDUeKW%2FibX4gY5GhSFIfW3J%2BHNCwHof7%2BHjibHCLwjGGP6Ab4msG%2BGREdSXDq5LE3C0jv2kYDwbp2y%2FNa9Bvhpdmb3myQvUQRtrjlhX3r2blJQZjt1%2FLRse8oztlg4j%2FUcXALza%2BKwTk9QLroGK10rpZp1vlY6hQWuEW2y5rv7MawZmwBtBSM9EyJQs3aPCMqnJ%2BK6czWwY%2FV3dhUA1xounQqTpsSQ4YV5paaoKnkX%2F7aI0zhQKENpQiVk%2FVHO%2BhRBszyyglxvNAQRxusOQHuuG0iDplLe9dFDNxzRaYt%2FhzY7B9bf1fV67BhNA%2BnjGuu3xfn7HyVa8PYjfhn4RKKZj2hKkCnv5QamSAWc3nHjMmQooStEaWpmk4twr%2Biv15B08H7l4tHiPtZJowxM73yQY6pgFtv337xnDIQm3Ju9wk0XCbPlVe%2B5WCnEetybq4S%2BciqagqyA14WacdN4G4cSyapEgWYAgkYup9XR0hn8ca4V4pXNYRHYl2rsZULbTMpiPa28Gh0ZcQ4SGhnzFiGeMMmEahsf3Dpbhrd%2BFE5Z%2FkWtpZTNeFfyseAm4HA9bgenRk3AfHJ0GIABCyK4ZNvhzx%2FF0vXIAEIzC%2FLkWHbpdvuIVs8odnm8ch&X-Amz-Signature=7b2f9fc7e9839c3defcb747b6a8a156a7bbea7875590cabcb661220f080c1f26&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
```python
fig, ax = plt.subplots(figsize=(8,6))

ax.bar(df.columns, df.max(), color='green')
ax.bar(df.columns, df.loc['Banana'], color='blue')
ax.bar(df.columns, df.min(), color='red')

plt.show()
```
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/873e4980-985f-43d3-87ee-044ba976e19a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46676BGLV75%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T232220Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJGMEQCIFT6VXdM55%2B0xtheI%2BJrYVevvuhXDzNXft9rEixeubXXAiBT6d4LKApf%2BMmXuju9DeNud2wyL5uxKJYLwMF91dD%2Bjyr%2FAwgnEAAaDDYzNzQyMzE4MzgwNSIMiM7%2BowZfOUWw9aERKtwDuJCXD1Q4DtsaSk3HBpGc1YPAjK9ErUiAWkbb5cjp9ymB9HntA2iACwHJHxBrnbD9wzXfjLLMtF6s4%2FAeQtz%2FllxslC0gSzRarY8XF8G9xYBdAKdkBVAVwmCY42%2F4qxUqSOg1P9m3CFbGmZqNun8QIvMAgnRsGQADRwj92j2xHImmWHDzTrhKcrUZ4PwIdpmDyxvLq5gYOqWsFz7ihSyYr68Eh0YZ7TcdwtstPsKoUrTLVDUeKW%2FibX4gY5GhSFIfW3J%2BHNCwHof7%2BHjibHCLwjGGP6Ab4msG%2BGREdSXDq5LE3C0jv2kYDwbp2y%2FNa9Bvhpdmb3myQvUQRtrjlhX3r2blJQZjt1%2FLRse8oztlg4j%2FUcXALza%2BKwTk9QLroGK10rpZp1vlY6hQWuEW2y5rv7MawZmwBtBSM9EyJQs3aPCMqnJ%2BK6czWwY%2FV3dhUA1xounQqTpsSQ4YV5paaoKnkX%2F7aI0zhQKENpQiVk%2FVHO%2BhRBszyyglxvNAQRxusOQHuuG0iDplLe9dFDNxzRaYt%2FhzY7B9bf1fV67BhNA%2BnjGuu3xfn7HyVa8PYjfhn4RKKZj2hKkCnv5QamSAWc3nHjMmQooStEaWpmk4twr%2Biv15B08H7l4tHiPtZJowxM73yQY6pgFtv337xnDIQm3Ju9wk0XCbPlVe%2B5WCnEetybq4S%2BciqagqyA14WacdN4G4cSyapEgWYAgkYup9XR0hn8ca4V4pXNYRHYl2rsZULbTMpiPa28Gh0ZcQ4SGhnzFiGeMMmEahsf3Dpbhrd%2BFE5Z%2FkWtpZTNeFfyseAm4HA9bgenRk3AfHJ0GIABCyK4ZNvhzx%2FF0vXIAEIzC%2FLkWHbpdvuIVs8odnm8ch&X-Amz-Signature=ea2a278f2634c1e00316fc4a5847e9d69a758cc5945c8b70445b33f48c28ec3c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
Mark all the statement that are true.
✅ Sunday is the day with the fewest sales in total.
❌ Relative to the other fruits on the same day, most bananas were sold on Wednesday. 
❌ Friday is the day with fewest sales in total.
❌ This is a stacked bar plot. 
✅ From the plot, it is impossible to know how many bananas were sold on Friday. 
✅ Bananas were the most sold fruit on Tuesday because the blue bar is the largest there. 
❌ On Thursday, Friday, and Saturday, the sales for bananas were 0. 

<details>
<summary>Explanation</summary>

> 💡 **[.subplots()](/10c38918e9a84ef79c8040d2fba85e2e#eaf7b9caca0a4167b5e87f638665032d), [.bar()](/10c38918e9a84ef79c8040d2fba85e2e#7f417ec8d30647888b638c6e367259e1)**
✅ **Correct**, don’t get irritated by the heights of the bars, as they are not stacked on each other but rather just overlapping.
❌ **Incorrect**, most bananas were sold on Tuesday. 
❌ **Incorrect**, Sunday is the day with the lowest sales.
❌ **Incorrect**, it is a simple multiple bar plot. The bars are just overlapping each other, which is why it appears like a stacked bar chart. If we want to create a stacked bar chart we would need to define the `bottom=` parameter.
✅ **Correct**, because the green and the red bar are overlapping the blue bar, thus we can not infer from the plot how many bananas were sold on that day.
✅ **Correct**, the blue bars represent the sales of bananas.
❌ **Incorrect**, the sales was not zero, the bars are simply not visible in the plot as they are overlapped by the other bars.
</details>
---
## Question 2
Given is the following code:
```python
fig, ax = plt.subplots(figsize=(8, 6))

width = 0.3

xticklabels = fruits.columns
xticks = np.arange(0, len(xticklabels))

ax.bar(xticks - width, fruits.loc['Cherry'], width = width, color='green', label='Cherry')
ax.bar(xticks, fruits.loc['Banana'], width=width, colot='blue', label='Banana')
ax.bar(xticks + width, fruits.loc['Apple'], width=width, color='red', label='Apple')

ax.set_xticks(xticks)
ax.set_xticklabels(xticklabels)

ax.legend()

plt.show()
```
Which figure does the code produce?
**✅ Figure 1**
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/671fec9e-0d8b-481a-8e6d-5e86347f6490/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46676BGLV75%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T232220Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJGMEQCIFT6VXdM55%2B0xtheI%2BJrYVevvuhXDzNXft9rEixeubXXAiBT6d4LKApf%2BMmXuju9DeNud2wyL5uxKJYLwMF91dD%2Bjyr%2FAwgnEAAaDDYzNzQyMzE4MzgwNSIMiM7%2BowZfOUWw9aERKtwDuJCXD1Q4DtsaSk3HBpGc1YPAjK9ErUiAWkbb5cjp9ymB9HntA2iACwHJHxBrnbD9wzXfjLLMtF6s4%2FAeQtz%2FllxslC0gSzRarY8XF8G9xYBdAKdkBVAVwmCY42%2F4qxUqSOg1P9m3CFbGmZqNun8QIvMAgnRsGQADRwj92j2xHImmWHDzTrhKcrUZ4PwIdpmDyxvLq5gYOqWsFz7ihSyYr68Eh0YZ7TcdwtstPsKoUrTLVDUeKW%2FibX4gY5GhSFIfW3J%2BHNCwHof7%2BHjibHCLwjGGP6Ab4msG%2BGREdSXDq5LE3C0jv2kYDwbp2y%2FNa9Bvhpdmb3myQvUQRtrjlhX3r2blJQZjt1%2FLRse8oztlg4j%2FUcXALza%2BKwTk9QLroGK10rpZp1vlY6hQWuEW2y5rv7MawZmwBtBSM9EyJQs3aPCMqnJ%2BK6czWwY%2FV3dhUA1xounQqTpsSQ4YV5paaoKnkX%2F7aI0zhQKENpQiVk%2FVHO%2BhRBszyyglxvNAQRxusOQHuuG0iDplLe9dFDNxzRaYt%2FhzY7B9bf1fV67BhNA%2BnjGuu3xfn7HyVa8PYjfhn4RKKZj2hKkCnv5QamSAWc3nHjMmQooStEaWpmk4twr%2Biv15B08H7l4tHiPtZJowxM73yQY6pgFtv337xnDIQm3Ju9wk0XCbPlVe%2B5WCnEetybq4S%2BciqagqyA14WacdN4G4cSyapEgWYAgkYup9XR0hn8ca4V4pXNYRHYl2rsZULbTMpiPa28Gh0ZcQ4SGhnzFiGeMMmEahsf3Dpbhrd%2BFE5Z%2FkWtpZTNeFfyseAm4HA9bgenRk3AfHJ0GIABCyK4ZNvhzx%2FF0vXIAEIzC%2FLkWHbpdvuIVs8odnm8ch&X-Amz-Signature=0630aa0bf0d0b6934d7e404eadacc7a395ee76db724bca1221f6e6495a4dcc93&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
**❌ Figure 2**
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/695a6b05-f2f8-40a9-bf6a-a39a44b06cb5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46676BGLV75%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T232220Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJGMEQCIFT6VXdM55%2B0xtheI%2BJrYVevvuhXDzNXft9rEixeubXXAiBT6d4LKApf%2BMmXuju9DeNud2wyL5uxKJYLwMF91dD%2Bjyr%2FAwgnEAAaDDYzNzQyMzE4MzgwNSIMiM7%2BowZfOUWw9aERKtwDuJCXD1Q4DtsaSk3HBpGc1YPAjK9ErUiAWkbb5cjp9ymB9HntA2iACwHJHxBrnbD9wzXfjLLMtF6s4%2FAeQtz%2FllxslC0gSzRarY8XF8G9xYBdAKdkBVAVwmCY42%2F4qxUqSOg1P9m3CFbGmZqNun8QIvMAgnRsGQADRwj92j2xHImmWHDzTrhKcrUZ4PwIdpmDyxvLq5gYOqWsFz7ihSyYr68Eh0YZ7TcdwtstPsKoUrTLVDUeKW%2FibX4gY5GhSFIfW3J%2BHNCwHof7%2BHjibHCLwjGGP6Ab4msG%2BGREdSXDq5LE3C0jv2kYDwbp2y%2FNa9Bvhpdmb3myQvUQRtrjlhX3r2blJQZjt1%2FLRse8oztlg4j%2FUcXALza%2BKwTk9QLroGK10rpZp1vlY6hQWuEW2y5rv7MawZmwBtBSM9EyJQs3aPCMqnJ%2BK6czWwY%2FV3dhUA1xounQqTpsSQ4YV5paaoKnkX%2F7aI0zhQKENpQiVk%2FVHO%2BhRBszyyglxvNAQRxusOQHuuG0iDplLe9dFDNxzRaYt%2FhzY7B9bf1fV67BhNA%2BnjGuu3xfn7HyVa8PYjfhn4RKKZj2hKkCnv5QamSAWc3nHjMmQooStEaWpmk4twr%2Biv15B08H7l4tHiPtZJowxM73yQY6pgFtv337xnDIQm3Ju9wk0XCbPlVe%2B5WCnEetybq4S%2BciqagqyA14WacdN4G4cSyapEgWYAgkYup9XR0hn8ca4V4pXNYRHYl2rsZULbTMpiPa28Gh0ZcQ4SGhnzFiGeMMmEahsf3Dpbhrd%2BFE5Z%2FkWtpZTNeFfyseAm4HA9bgenRk3AfHJ0GIABCyK4ZNvhzx%2FF0vXIAEIzC%2FLkWHbpdvuIVs8odnm8ch&X-Amz-Signature=125d19ded04860574d874ce80bcad2584b01074a55694259ff50a09ad1631797&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
**❌ Figure 3**
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/3d5de852-f8cf-4ece-88eb-e79c917123e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46676BGLV75%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T232220Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJGMEQCIFT6VXdM55%2B0xtheI%2BJrYVevvuhXDzNXft9rEixeubXXAiBT6d4LKApf%2BMmXuju9DeNud2wyL5uxKJYLwMF91dD%2Bjyr%2FAwgnEAAaDDYzNzQyMzE4MzgwNSIMiM7%2BowZfOUWw9aERKtwDuJCXD1Q4DtsaSk3HBpGc1YPAjK9ErUiAWkbb5cjp9ymB9HntA2iACwHJHxBrnbD9wzXfjLLMtF6s4%2FAeQtz%2FllxslC0gSzRarY8XF8G9xYBdAKdkBVAVwmCY42%2F4qxUqSOg1P9m3CFbGmZqNun8QIvMAgnRsGQADRwj92j2xHImmWHDzTrhKcrUZ4PwIdpmDyxvLq5gYOqWsFz7ihSyYr68Eh0YZ7TcdwtstPsKoUrTLVDUeKW%2FibX4gY5GhSFIfW3J%2BHNCwHof7%2BHjibHCLwjGGP6Ab4msG%2BGREdSXDq5LE3C0jv2kYDwbp2y%2FNa9Bvhpdmb3myQvUQRtrjlhX3r2blJQZjt1%2FLRse8oztlg4j%2FUcXALza%2BKwTk9QLroGK10rpZp1vlY6hQWuEW2y5rv7MawZmwBtBSM9EyJQs3aPCMqnJ%2BK6czWwY%2FV3dhUA1xounQqTpsSQ4YV5paaoKnkX%2F7aI0zhQKENpQiVk%2FVHO%2BhRBszyyglxvNAQRxusOQHuuG0iDplLe9dFDNxzRaYt%2FhzY7B9bf1fV67BhNA%2BnjGuu3xfn7HyVa8PYjfhn4RKKZj2hKkCnv5QamSAWc3nHjMmQooStEaWpmk4twr%2Biv15B08H7l4tHiPtZJowxM73yQY6pgFtv337xnDIQm3Ju9wk0XCbPlVe%2B5WCnEetybq4S%2BciqagqyA14WacdN4G4cSyapEgWYAgkYup9XR0hn8ca4V4pXNYRHYl2rsZULbTMpiPa28Gh0ZcQ4SGhnzFiGeMMmEahsf3Dpbhrd%2BFE5Z%2FkWtpZTNeFfyseAm4HA9bgenRk3AfHJ0GIABCyK4ZNvhzx%2FF0vXIAEIzC%2FLkWHbpdvuIVs8odnm8ch&X-Amz-Signature=4e1858747c96af70b6dce8c8bd7be05b1dd919b5fc0e76ceba60aafc9d9f318b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
**❌ Figure 4**
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/28f2f2fb-1f68-4c7b-bcd1-b8a02271a5b7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46676BGLV75%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T232220Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJGMEQCIFT6VXdM55%2B0xtheI%2BJrYVevvuhXDzNXft9rEixeubXXAiBT6d4LKApf%2BMmXuju9DeNud2wyL5uxKJYLwMF91dD%2Bjyr%2FAwgnEAAaDDYzNzQyMzE4MzgwNSIMiM7%2BowZfOUWw9aERKtwDuJCXD1Q4DtsaSk3HBpGc1YPAjK9ErUiAWkbb5cjp9ymB9HntA2iACwHJHxBrnbD9wzXfjLLMtF6s4%2FAeQtz%2FllxslC0gSzRarY8XF8G9xYBdAKdkBVAVwmCY42%2F4qxUqSOg1P9m3CFbGmZqNun8QIvMAgnRsGQADRwj92j2xHImmWHDzTrhKcrUZ4PwIdpmDyxvLq5gYOqWsFz7ihSyYr68Eh0YZ7TcdwtstPsKoUrTLVDUeKW%2FibX4gY5GhSFIfW3J%2BHNCwHof7%2BHjibHCLwjGGP6Ab4msG%2BGREdSXDq5LE3C0jv2kYDwbp2y%2FNa9Bvhpdmb3myQvUQRtrjlhX3r2blJQZjt1%2FLRse8oztlg4j%2FUcXALza%2BKwTk9QLroGK10rpZp1vlY6hQWuEW2y5rv7MawZmwBtBSM9EyJQs3aPCMqnJ%2BK6czWwY%2FV3dhUA1xounQqTpsSQ4YV5paaoKnkX%2F7aI0zhQKENpQiVk%2FVHO%2BhRBszyyglxvNAQRxusOQHuuG0iDplLe9dFDNxzRaYt%2FhzY7B9bf1fV67BhNA%2BnjGuu3xfn7HyVa8PYjfhn4RKKZj2hKkCnv5QamSAWc3nHjMmQooStEaWpmk4twr%2Biv15B08H7l4tHiPtZJowxM73yQY6pgFtv337xnDIQm3Ju9wk0XCbPlVe%2B5WCnEetybq4S%2BciqagqyA14WacdN4G4cSyapEgWYAgkYup9XR0hn8ca4V4pXNYRHYl2rsZULbTMpiPa28Gh0ZcQ4SGhnzFiGeMMmEahsf3Dpbhrd%2BFE5Z%2FkWtpZTNeFfyseAm4HA9bgenRk3AfHJ0GIABCyK4ZNvhzx%2FF0vXIAEIzC%2FLkWHbpdvuIVs8odnm8ch&X-Amz-Signature=61103bef9613a645cc8b7682832b0e6f62a7fa30b88f17647fb8b2f085e40548&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

<details>
<summary>Explanation</summary>

> 💡 **[.bar()](/10c38918e9a84ef79c8040d2fba85e2e#7f417ec8d30647888b638c6e367259e1), [.arange()](/ccc5737dc7c64936bced118aca375cf9#82ad4caa17294f6a89ccfeb254bcf289), [.loc[]](/1867045b058343e1a66b677961515907#a1fa1f2124f7454a8a893c785ff9b87d), [.set_xticks()](/10c38918e9a84ef79c8040d2fba85e2e#1a8b5ac6cd6f4f24a77276097215a64f), [.set_xticklabels()](/10c38918e9a84ef79c8040d2fba85e2e#b88bafe085734ba0acc0d42797d954c8)**
Here the trick is to know how the bars are positioned. We can figure this out by looking at the following lines in the code:
```python
ax.bar(xticks **- width**, fruits.loc['Cherry'], width = width, color='green', label='Cherry')
ax.bar(xticks, fruits.loc['Banana'], width=width, colot='blue', label='Banana')
ax.bar(xticks **+ width**, fruits.loc['Apple'], width=width, color='red', label='Apple')
```
The first parameter of the .bar() method are the x-positions of the bars.
We can see that:
- for the **Cherry** fruit, we deduct the width (-0.3) from `xticks`. Thus, the Cherry bars are positioned to the left. 
- for the **Banana** fruit, we don’t deduct or add any value from `xticks`. Thus, the Banana bars are positioned in the middle. 
- for the **Apple** fruit, we add the width (+0.3) to `xticks`. Thus, the Apple bars are positioned to the right. 
In Figure 1, **Cherry** is on the left, **Banana** in the middle and **Apple** on the right. 
</details>
---
## Question 3
We want to produce this plot:
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/5363df47-9e70-4389-9327-e859bf892a00/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46676BGLV75%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T232220Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJGMEQCIFT6VXdM55%2B0xtheI%2BJrYVevvuhXDzNXft9rEixeubXXAiBT6d4LKApf%2BMmXuju9DeNud2wyL5uxKJYLwMF91dD%2Bjyr%2FAwgnEAAaDDYzNzQyMzE4MzgwNSIMiM7%2BowZfOUWw9aERKtwDuJCXD1Q4DtsaSk3HBpGc1YPAjK9ErUiAWkbb5cjp9ymB9HntA2iACwHJHxBrnbD9wzXfjLLMtF6s4%2FAeQtz%2FllxslC0gSzRarY8XF8G9xYBdAKdkBVAVwmCY42%2F4qxUqSOg1P9m3CFbGmZqNun8QIvMAgnRsGQADRwj92j2xHImmWHDzTrhKcrUZ4PwIdpmDyxvLq5gYOqWsFz7ihSyYr68Eh0YZ7TcdwtstPsKoUrTLVDUeKW%2FibX4gY5GhSFIfW3J%2BHNCwHof7%2BHjibHCLwjGGP6Ab4msG%2BGREdSXDq5LE3C0jv2kYDwbp2y%2FNa9Bvhpdmb3myQvUQRtrjlhX3r2blJQZjt1%2FLRse8oztlg4j%2FUcXALza%2BKwTk9QLroGK10rpZp1vlY6hQWuEW2y5rv7MawZmwBtBSM9EyJQs3aPCMqnJ%2BK6czWwY%2FV3dhUA1xounQqTpsSQ4YV5paaoKnkX%2F7aI0zhQKENpQiVk%2FVHO%2BhRBszyyglxvNAQRxusOQHuuG0iDplLe9dFDNxzRaYt%2FhzY7B9bf1fV67BhNA%2BnjGuu3xfn7HyVa8PYjfhn4RKKZj2hKkCnv5QamSAWc3nHjMmQooStEaWpmk4twr%2Biv15B08H7l4tHiPtZJowxM73yQY6pgFtv337xnDIQm3Ju9wk0XCbPlVe%2B5WCnEetybq4S%2BciqagqyA14WacdN4G4cSyapEgWYAgkYup9XR0hn8ca4V4pXNYRHYl2rsZULbTMpiPa28Gh0ZcQ4SGhnzFiGeMMmEahsf3Dpbhrd%2BFE5Z%2FkWtpZTNeFfyseAm4HA9bgenRk3AfHJ0GIABCyK4ZNvhzx%2FF0vXIAEIzC%2FLkWHbpdvuIVs8odnm8ch&X-Amz-Signature=d66add5f50b94038b79371c0c9acf06e24ff5d613050f3d3665495923988490f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
Which keyword argument is required to create this plot?
`fig, axes = plt.subplots(3, 1, `**`sharex=True`**`)`

<details>
<summary>Explanation</summary>

> 💡 **[.subplots()](/10c38918e9a84ef79c8040d2fba85e2e#eaf7b9caca0a4167b5e87f638665032d)**
With `sharex=True`, the x-ticks are shared amongst the subplots. Thus, the name of the weekdays are only displayed ones. 
The `sharex` argument in `plt.subplots()` is used to control the sharing of properties among x (or y) axes. If `sharex=True`, it means the x-axis will be shared among all subplots, i.e., displayed only once. This is useful when you want all subplots to have the same x-axis, which is the case when you want to distribute the data among weekdays.
</details>
---
## Question 4
How many axes are created with the statement:
```python
fig, axes = plt.subplots(4, 4)
```
**16**

<details>
<summary>Explanation</summary>

> 💡 **[.subplots()](/10c38918e9a84ef79c8040d2fba85e2e#eaf7b9caca0a4167b5e87f638665032d)**
The statement `fig, axes = plt.subplots(4, 4)` creates 16 axes. This is because the `subplots()` function takes two arguments: the number of rows and the number of columns. In this case, 4 rows and 4 columns are specified, so 4*4 equals 16 subplots or axes in total.
</details>
---
## Question 5
We want to create the following line plot with the values from following *pd.DataFrame* **df**.
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/ba7cae60-975c-45ea-9d4d-d5740d079a09/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46676BGLV75%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T232220Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJGMEQCIFT6VXdM55%2B0xtheI%2BJrYVevvuhXDzNXft9rEixeubXXAiBT6d4LKApf%2BMmXuju9DeNud2wyL5uxKJYLwMF91dD%2Bjyr%2FAwgnEAAaDDYzNzQyMzE4MzgwNSIMiM7%2BowZfOUWw9aERKtwDuJCXD1Q4DtsaSk3HBpGc1YPAjK9ErUiAWkbb5cjp9ymB9HntA2iACwHJHxBrnbD9wzXfjLLMtF6s4%2FAeQtz%2FllxslC0gSzRarY8XF8G9xYBdAKdkBVAVwmCY42%2F4qxUqSOg1P9m3CFbGmZqNun8QIvMAgnRsGQADRwj92j2xHImmWHDzTrhKcrUZ4PwIdpmDyxvLq5gYOqWsFz7ihSyYr68Eh0YZ7TcdwtstPsKoUrTLVDUeKW%2FibX4gY5GhSFIfW3J%2BHNCwHof7%2BHjibHCLwjGGP6Ab4msG%2BGREdSXDq5LE3C0jv2kYDwbp2y%2FNa9Bvhpdmb3myQvUQRtrjlhX3r2blJQZjt1%2FLRse8oztlg4j%2FUcXALza%2BKwTk9QLroGK10rpZp1vlY6hQWuEW2y5rv7MawZmwBtBSM9EyJQs3aPCMqnJ%2BK6czWwY%2FV3dhUA1xounQqTpsSQ4YV5paaoKnkX%2F7aI0zhQKENpQiVk%2FVHO%2BhRBszyyglxvNAQRxusOQHuuG0iDplLe9dFDNxzRaYt%2FhzY7B9bf1fV67BhNA%2BnjGuu3xfn7HyVa8PYjfhn4RKKZj2hKkCnv5QamSAWc3nHjMmQooStEaWpmk4twr%2Biv15B08H7l4tHiPtZJowxM73yQY6pgFtv337xnDIQm3Ju9wk0XCbPlVe%2B5WCnEetybq4S%2BciqagqyA14WacdN4G4cSyapEgWYAgkYup9XR0hn8ca4V4pXNYRHYl2rsZULbTMpiPa28Gh0ZcQ4SGhnzFiGeMMmEahsf3Dpbhrd%2BFE5Z%2FkWtpZTNeFfyseAm4HA9bgenRk3AfHJ0GIABCyK4ZNvhzx%2FF0vXIAEIzC%2FLkWHbpdvuIVs8odnm8ch&X-Amz-Signature=55f38fa07968593088ad9451ad4da086730f4dab52a79e1257f1dc432b019721&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
The *pd.DataFrame* **df** looks like this:
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/8855b98d-ce33-4262-99e5-5ab81fcf48a2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46676BGLV75%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T232220Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJGMEQCIFT6VXdM55%2B0xtheI%2BJrYVevvuhXDzNXft9rEixeubXXAiBT6d4LKApf%2BMmXuju9DeNud2wyL5uxKJYLwMF91dD%2Bjyr%2FAwgnEAAaDDYzNzQyMzE4MzgwNSIMiM7%2BowZfOUWw9aERKtwDuJCXD1Q4DtsaSk3HBpGc1YPAjK9ErUiAWkbb5cjp9ymB9HntA2iACwHJHxBrnbD9wzXfjLLMtF6s4%2FAeQtz%2FllxslC0gSzRarY8XF8G9xYBdAKdkBVAVwmCY42%2F4qxUqSOg1P9m3CFbGmZqNun8QIvMAgnRsGQADRwj92j2xHImmWHDzTrhKcrUZ4PwIdpmDyxvLq5gYOqWsFz7ihSyYr68Eh0YZ7TcdwtstPsKoUrTLVDUeKW%2FibX4gY5GhSFIfW3J%2BHNCwHof7%2BHjibHCLwjGGP6Ab4msG%2BGREdSXDq5LE3C0jv2kYDwbp2y%2FNa9Bvhpdmb3myQvUQRtrjlhX3r2blJQZjt1%2FLRse8oztlg4j%2FUcXALza%2BKwTk9QLroGK10rpZp1vlY6hQWuEW2y5rv7MawZmwBtBSM9EyJQs3aPCMqnJ%2BK6czWwY%2FV3dhUA1xounQqTpsSQ4YV5paaoKnkX%2F7aI0zhQKENpQiVk%2FVHO%2BhRBszyyglxvNAQRxusOQHuuG0iDplLe9dFDNxzRaYt%2FhzY7B9bf1fV67BhNA%2BnjGuu3xfn7HyVa8PYjfhn4RKKZj2hKkCnv5QamSAWc3nHjMmQooStEaWpmk4twr%2Biv15B08H7l4tHiPtZJowxM73yQY6pgFtv337xnDIQm3Ju9wk0XCbPlVe%2B5WCnEetybq4S%2BciqagqyA14WacdN4G4cSyapEgWYAgkYup9XR0hn8ca4V4pXNYRHYl2rsZULbTMpiPa28Gh0ZcQ4SGhnzFiGeMMmEahsf3Dpbhrd%2BFE5Z%2FkWtpZTNeFfyseAm4HA9bgenRk3AfHJ0GIABCyK4ZNvhzx%2FF0vXIAEIzC%2FLkWHbpdvuIVs8odnm8ch&X-Amz-Signature=781db7c7d1c9bd0d30159881a26843e130d0119183a0c3e38deddd4ea956066e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
How can you get the x-values and y-values for the **blue** line?
x-values: `df.columns`
y-values: `df.loc['Banana']`

<details>
<summary>Explanation</summary>

> 💡 **[.columns](/1867045b058343e1a66b677961515907#b56cca6739ca4649ab31ebab1ee61f83), [.loc[]](/1867045b058343e1a66b677961515907#a1fa1f2124f7454a8a893c785ff9b87d)**
**x-values**
The x-values are the ones that are displayed on the horizontal axis, i.e., the weekdays. We see that in the DataFrame **df**, the weekdays are the column names. With `.columns` attribute we can select the column names of a DataFrame.
**y-values**
The y-values are the ones that determine how the blue line flows (if it goes up or down). Each line represents a fruit. The blue line represents the fruit Banana. We can see that each fruit has a row in the DataFrame. Thus, we want to select the Banana row which we can do by using `df.loc['banana']` or `df.iloc[1]` (Banana is the second row in the DataFrame).
</details>
---
## Question 6
Given are the following three boxplots.
In the image, select the region where 50% of the *sepal* width observations for *Versicolor* are visualized.
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/74518876-1b87-44f7-b914-783cb42a8308/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46676BGLV75%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T232220Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJGMEQCIFT6VXdM55%2B0xtheI%2BJrYVevvuhXDzNXft9rEixeubXXAiBT6d4LKApf%2BMmXuju9DeNud2wyL5uxKJYLwMF91dD%2Bjyr%2FAwgnEAAaDDYzNzQyMzE4MzgwNSIMiM7%2BowZfOUWw9aERKtwDuJCXD1Q4DtsaSk3HBpGc1YPAjK9ErUiAWkbb5cjp9ymB9HntA2iACwHJHxBrnbD9wzXfjLLMtF6s4%2FAeQtz%2FllxslC0gSzRarY8XF8G9xYBdAKdkBVAVwmCY42%2F4qxUqSOg1P9m3CFbGmZqNun8QIvMAgnRsGQADRwj92j2xHImmWHDzTrhKcrUZ4PwIdpmDyxvLq5gYOqWsFz7ihSyYr68Eh0YZ7TcdwtstPsKoUrTLVDUeKW%2FibX4gY5GhSFIfW3J%2BHNCwHof7%2BHjibHCLwjGGP6Ab4msG%2BGREdSXDq5LE3C0jv2kYDwbp2y%2FNa9Bvhpdmb3myQvUQRtrjlhX3r2blJQZjt1%2FLRse8oztlg4j%2FUcXALza%2BKwTk9QLroGK10rpZp1vlY6hQWuEW2y5rv7MawZmwBtBSM9EyJQs3aPCMqnJ%2BK6czWwY%2FV3dhUA1xounQqTpsSQ4YV5paaoKnkX%2F7aI0zhQKENpQiVk%2FVHO%2BhRBszyyglxvNAQRxusOQHuuG0iDplLe9dFDNxzRaYt%2FhzY7B9bf1fV67BhNA%2BnjGuu3xfn7HyVa8PYjfhn4RKKZj2hKkCnv5QamSAWc3nHjMmQooStEaWpmk4twr%2Biv15B08H7l4tHiPtZJowxM73yQY6pgFtv337xnDIQm3Ju9wk0XCbPlVe%2B5WCnEetybq4S%2BciqagqyA14WacdN4G4cSyapEgWYAgkYup9XR0hn8ca4V4pXNYRHYl2rsZULbTMpiPa28Gh0ZcQ4SGhnzFiGeMMmEahsf3Dpbhrd%2BFE5Z%2FkWtpZTNeFfyseAm4HA9bgenRk3AfHJ0GIABCyK4ZNvhzx%2FF0vXIAEIzC%2FLkWHbpdvuIVs8odnm8ch&X-Amz-Signature=97b4a55023f34c3d15675971fdb22a914f3b3e7563c98e3f6ceb90d9ec944261&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
<details>
<summary>Explanation</summary>

> 💡 **[Boxplot](/10c38918e9a84ef79c8040d2fba85e2e#29e8af14c0a848898738443608b4a50a)**
A boxplot (also known as a whisker plot) displays a summary of the range and statistical distribution of the data. The box itself represents the interquartile range (IQR), which is the range where the middle 50% of your data points lie. This is also known as the 1st quartile (25th percentile) to the 3rd quartile (75th percentile).
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/fd06423b-c4cf-4779-842a-ac6488fdb79f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T4NZ6EOE%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T232224Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJGMEQCICK7nb80HtlaejYxUZUNdEbU5UVOYfPniOYdysYokdjyAiBSLJtvlsh%2FpKJrzRAkEg3oq4Kt3KbH2BDRZx5s11fPTir%2FAwgnEAAaDDYzNzQyMzE4MzgwNSIMpCbKdH096h1xGe1vKtwDZrmtrCaeA7G57cdUGUKZiopUoAGNqe9YW2n3N6N9R%2FyQGgxGBcB%2BUtGiW3wLbnmO7ezd%2FgQe1VzUAld1RBVMqrmHaYfzSP%2FuNFOfQbD9gUBBQjlpfG9cMPREwBz%2FQ2l9GUrIGqiaZB%2BUB3Sqiz0chslb%2BiDmNtYAvM3dqPdtTQ2nteTb8yOFIoZvH%2BcQuPZYW9jJISq3IjcNUp0c6qgIE9mOqto%2FQsHU4SydEmW9uXOFLfL5EzI%2BohSYwx%2BC51r7vKJhODtzlifqpK%2B6mZ4BLL5o1KgNDyoXtdbcDNbFf%2FIP0OzXBRW8BXsAL0VRip9n6nqjgzMXGDxQdPcE%2BYZey8uSyqIGbmAZvOSUFEgQsb8ls4Q%2F8Nzwoo70Rj6DSB7aeTv9LaUNJpyc80pV2sH%2FwPkFU2uMfw0vGYxI%2BJAIExu20iOmh3K3covfTGmOlIG217wayC0vQveRmbRRHf5zhc80QSGXxliUJcH4MJB4krvPe6abwvCf%2BF%2BIaMesHICocs1BOPU%2Fl1x2JwblFZpVPpgH7Y6RBliheVMphXb69WY%2Bc4jZn2UYsgs4k25ulsrNSbzv85IEUhBzYnqVRiKpSF%2FKWKHIDiuUFGXn3aORMgON7jjIoZLuLdQcReYw1873yQY6pgFsKDkF1lCj7aiA4gUoibqFymqOI7mbLtUncd3UpubKTKnPYYWIUIjeK5S5acFC5uzpAHAQRn%2FsFdNkKFnnkORdef2ug0lUSS2tMte1r9T60ofiFRlFoUWusn7Yec3eGXiwd9teMMEcuYAZMEOTnCy0gffLl7kgjTgzejxy4wHGYy1blzrTXAZkLx4LR0sunJkvdskb4Dd3nJsx6g1DkvY2ScYgoHz%2B&X-Amz-Signature=9ddd17920e62e3e7ff9fe7815debf4e6eeb7aa7ec10e5dbe75ad874ca9836563&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
Each quartile represents 25% of the data, thus the **box in the middle** represents 50% of the data.
</details>
---

