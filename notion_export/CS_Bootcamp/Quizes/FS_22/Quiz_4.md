---
title: "Quiz 4"
notion_id: "7e1e3724-25d2-44b3-af29-5216da59fc81"
notion_url: "https://www.notion.so/Quiz-4-7e1e372425d244b3af295216da59fc81"
exported_at: "2025-12-14T00:52:40.262003+00:00"
---

# Quiz 4

![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/efc1be34-8141-46fb-bce2-7407370f6b2e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46627SNY3GG%2F20251214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251214T005214Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCICa0lKtbkIRSEll65PnT3dpR%2B%2F8HAkUOENkkVnZZBd%2BSAiEAjlGHoQZWIL2XA%2Bp6ge9jvKTmlxzEVm39%2BWrgepR4Qt4q%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDHgdH2h2EKSJNKYjGSrcA2HlEgbsRws5jRthUuQOYarkvTsJ78FbUWyVNYvl%2FTfVkIAjuR6qDfMsU8LZFVIYrxDecNd%2BWJ3MqSsHBGqHFXU6Ksf9NKg%2FYy5ha8VsUh4tNLJ4MssMX8sQLvQATRZ0n041XuG4VTCnr9ZOcZgWOiXkFAuWHXPgd0d8lRXb81pCgKyOQzPGE0Q%2FrMU%2BRvRPBlczHQUdek11Xo56qsHa2olhG%2BpUfV1t8kRlTEGvK7O17zfPjwIl3iywllpdhA3QJu0Ep%2BZCQujHEWPxjqj7jZ5uBpVZJ6Uu%2FGgPj52885lJ98ZTwOZSK3OFR53vNVL2tV2XnynzJr3KEcv3eEAIeQQAn86g2J6vCfu0lnG7EAH9f%2BftYLMha%2FUgNw1%2FEfWNWjNXwVFBn1N%2FVrOcHJFfBI2Lg10iW6PMTLL70K0RpAiLKA0AR98HPRZWFwdYi5h7fMbbFnTRfPh2YTnp7yEoqvmeTEVPSvOMnaaYDS1UhdX5Q14MKE5mwm%2B%2FqnMyXiofLpOE%2FYu6%2BBTd8TSM5%2FHG2nyBQlZPRQbCTQIIB5dV2M%2FE59DcYL9183gXtLoBu4lQLwHmy4csPuP%2BnNthfnEae%2FfPt%2BmIA2%2FdVdSn1Uzn94hvXMiLxntW98epasgSMLLO98kGOqUBien1%2BxtIvWZi0LO%2FiwcCXEGh13Mzk7u6V3UJhmWRyljqkwjQrXrlLfRb4fLnDkprGsbqpxs%2Bb%2F2mypS%2B4UbDlsNpZID%2BVZ%2F63Q1EnpuLKqLOibu2%2FcVuvFZuEEZD4gwMG%2FLf%2FRGWzqqm4I1RXaSMk8YxOFcquNiCSw13WIU60H9BeI2ckSN%2F8p6Su4QTF3zk%2FkVZ4PO0HQm9BOPquhB0wzdfJxPh&X-Amz-Signature=27399e4cfab995806b894aba2da4ff16a0e0292593ca0bd7d695c9dd4f01d9f3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- First we execute `map(f, range(6)) `
- We pass each element in `[0, 1, 2, 3, 4, 5]` into the function `def f(x)`
- Function def f(x) is executed 6 times
- As a result we get `[0, 2, 4, 6, 8, 10]`
- Now we execute `map(f, [0, 2, 4, 6, 8, 10])`
- We pass each element in` [0, 2, 4, 6, 8, 10] `into the function def `f(x)`
- Function def f(x) is executed 6 times
- As a result we get `[0, 4, 8, 12, 16, 20]`
How many times did we execute `def f(x)` ? —> **12 times**

---

![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/3edf55ed-2d5c-43ab-ae1c-95e731a798e1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46627SNY3GG%2F20251214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251214T005214Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCICa0lKtbkIRSEll65PnT3dpR%2B%2F8HAkUOENkkVnZZBd%2BSAiEAjlGHoQZWIL2XA%2Bp6ge9jvKTmlxzEVm39%2BWrgepR4Qt4q%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDHgdH2h2EKSJNKYjGSrcA2HlEgbsRws5jRthUuQOYarkvTsJ78FbUWyVNYvl%2FTfVkIAjuR6qDfMsU8LZFVIYrxDecNd%2BWJ3MqSsHBGqHFXU6Ksf9NKg%2FYy5ha8VsUh4tNLJ4MssMX8sQLvQATRZ0n041XuG4VTCnr9ZOcZgWOiXkFAuWHXPgd0d8lRXb81pCgKyOQzPGE0Q%2FrMU%2BRvRPBlczHQUdek11Xo56qsHa2olhG%2BpUfV1t8kRlTEGvK7O17zfPjwIl3iywllpdhA3QJu0Ep%2BZCQujHEWPxjqj7jZ5uBpVZJ6Uu%2FGgPj52885lJ98ZTwOZSK3OFR53vNVL2tV2XnynzJr3KEcv3eEAIeQQAn86g2J6vCfu0lnG7EAH9f%2BftYLMha%2FUgNw1%2FEfWNWjNXwVFBn1N%2FVrOcHJFfBI2Lg10iW6PMTLL70K0RpAiLKA0AR98HPRZWFwdYi5h7fMbbFnTRfPh2YTnp7yEoqvmeTEVPSvOMnaaYDS1UhdX5Q14MKE5mwm%2B%2FqnMyXiofLpOE%2FYu6%2BBTd8TSM5%2FHG2nyBQlZPRQbCTQIIB5dV2M%2FE59DcYL9183gXtLoBu4lQLwHmy4csPuP%2BnNthfnEae%2FfPt%2BmIA2%2FdVdSn1Uzn94hvXMiLxntW98epasgSMLLO98kGOqUBien1%2BxtIvWZi0LO%2FiwcCXEGh13Mzk7u6V3UJhmWRyljqkwjQrXrlLfRb4fLnDkprGsbqpxs%2Bb%2F2mypS%2B4UbDlsNpZID%2BVZ%2F63Q1EnpuLKqLOibu2%2FcVuvFZuEEZD4gwMG%2FLf%2FRGWzqqm4I1RXaSMk8YxOFcquNiCSw13WIU60H9BeI2ckSN%2F8p6Su4QTF3zk%2FkVZ4PO0HQm9BOPquhB0wzdfJxPh&X-Amz-Signature=fb822b8063c8628786ed321b4839e0b5b76245bf3f5811f7061213ff4336b381&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- We take each element in `[0, 1, 2, 3, 4, 5, 6]` and assign it to `x`
- We multiply `x` by 2 
- Thus, each element is multiplied by 2 and result is `[0, 2, 4, 6, 8, 10, 12]`

---

![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/7925737f-daac-41c5-a855-e605a07160b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46627SNY3GG%2F20251214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251214T005214Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCICa0lKtbkIRSEll65PnT3dpR%2B%2F8HAkUOENkkVnZZBd%2BSAiEAjlGHoQZWIL2XA%2Bp6ge9jvKTmlxzEVm39%2BWrgepR4Qt4q%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDHgdH2h2EKSJNKYjGSrcA2HlEgbsRws5jRthUuQOYarkvTsJ78FbUWyVNYvl%2FTfVkIAjuR6qDfMsU8LZFVIYrxDecNd%2BWJ3MqSsHBGqHFXU6Ksf9NKg%2FYy5ha8VsUh4tNLJ4MssMX8sQLvQATRZ0n041XuG4VTCnr9ZOcZgWOiXkFAuWHXPgd0d8lRXb81pCgKyOQzPGE0Q%2FrMU%2BRvRPBlczHQUdek11Xo56qsHa2olhG%2BpUfV1t8kRlTEGvK7O17zfPjwIl3iywllpdhA3QJu0Ep%2BZCQujHEWPxjqj7jZ5uBpVZJ6Uu%2FGgPj52885lJ98ZTwOZSK3OFR53vNVL2tV2XnynzJr3KEcv3eEAIeQQAn86g2J6vCfu0lnG7EAH9f%2BftYLMha%2FUgNw1%2FEfWNWjNXwVFBn1N%2FVrOcHJFfBI2Lg10iW6PMTLL70K0RpAiLKA0AR98HPRZWFwdYi5h7fMbbFnTRfPh2YTnp7yEoqvmeTEVPSvOMnaaYDS1UhdX5Q14MKE5mwm%2B%2FqnMyXiofLpOE%2FYu6%2BBTd8TSM5%2FHG2nyBQlZPRQbCTQIIB5dV2M%2FE59DcYL9183gXtLoBu4lQLwHmy4csPuP%2BnNthfnEae%2FfPt%2BmIA2%2FdVdSn1Uzn94hvXMiLxntW98epasgSMLLO98kGOqUBien1%2BxtIvWZi0LO%2FiwcCXEGh13Mzk7u6V3UJhmWRyljqkwjQrXrlLfRb4fLnDkprGsbqpxs%2Bb%2F2mypS%2B4UbDlsNpZID%2BVZ%2F63Q1EnpuLKqLOibu2%2FcVuvFZuEEZD4gwMG%2FLf%2FRGWzqqm4I1RXaSMk8YxOFcquNiCSw13WIU60H9BeI2ckSN%2F8p6Su4QTF3zk%2FkVZ4PO0HQm9BOPquhB0wzdfJxPh&X-Amz-Signature=8a6d80718a6b4ab632d8208dc7c53aacddc0b15d1b793e6c7ed07fcb41898882&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- Incorrect, the execution will break as we never meet the stop condition as we pass on a negative numbers as parameters fro the recursive execution
→ `fibonacci(0 - 2)` + `fibonacci(0 - 1)`
- Correct, we see this as in line 10 we call the same function from within this function
- Correct, we don’t have a stop condition so when we pass another number into the function then the function will never terminate. If we execute it with `number = 1` then the if condition in line 7 is met and thus we go not into the else statement and consequently no recursive function call happens and we do not end up in an endless loop.

If you are not familiar how a [recursive fibonacci function](https://www.geeksforgeeks.org/python-program-for-program-for-fibonacci-numbers-2/) is executed, check below.
```python
# Function for nth Fibonacci number
def Fibonacci(n):
   
    # Check if input is 0 then it will
    # print incorrect input
    if n < 0:
        print("Incorrect input")
 
    # Check if n is 0
    # then it will return 0
    elif n == 0:
        return 0
 
    # Check if n is 1,2
    # it will return 1
    elif n == 1 or n == 2:
        return 1
 
    else:
        return Fibonacci(n-2) + Fibonacci(n-1)
 
# Driver Program
print(Fibonacci(5))
```
---
**`fibonacci(5)`** **→ ****5**
n = 5
- **`fibonacci(3)`** + **`fibonacci(4)`** → 2 + 3 = 5
- **`fibonacci(3)`**** → ****2**
- n = 3
- **`fibonacci(1)`** + **`fibonacci(2)`** → 1 + 1 = 2
- **`fibonacci(1)`**** → ****1**
- return **1**
- **`fibonacci(2)`**** → ****1**
- **`fibonacci(0)`** + **`fibonacci(1)`** → 0 + 1 = 1
- **`fibonacci(0)`**** → ****0**
- n = 0
- return **0**
- **`fibonacci(1)`**** → ****1**
- n = 1
- return **1**
- **`fibonacci(4)`**** → ****3**
- n = 4
- **`fibonacci(2)`** + **`fibonacci(3)`** → 1 + 2 = 3
- **`fibonacci(2)`** **→ ****1**
- n = 2
- **`fibonacci(0)`** + **`fibonacci(1)`** → 0 + 1 = 1
- **`fibonacci(0)`**** → ****0**
- n = 0
- return 0
- **`fibonacci(1)`**** → ****1**
- n = 1
- return 1
- **`fibonacci(3)`**** → ****2**
- n = 3
- **`fibonacci(1)`** + **`fibonacci(2)`** → 1 + 1 = 2
- **`fibonacci(1)`**** → ****1**
- n = 1
- return 1
- **`fibonacci(2)`**** → ****1**
- n = 2
- **`fibonacci(0)`** + **`fibonacci(1)`** → 0 + 1 = 1
- **`fibonacci(0)`** **→ ****0**
- n = 0
- return **0**
- **`fibonacci(1)`** **→ ****1**
- n = 1
- return 1
---
Also, check this image below which explains quite well how generally recursive functions work.
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/9358d79b-9cb3-4099-b2ec-363e84197850/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46627SNY3GG%2F20251214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251214T005214Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCICa0lKtbkIRSEll65PnT3dpR%2B%2F8HAkUOENkkVnZZBd%2BSAiEAjlGHoQZWIL2XA%2Bp6ge9jvKTmlxzEVm39%2BWrgepR4Qt4q%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDHgdH2h2EKSJNKYjGSrcA2HlEgbsRws5jRthUuQOYarkvTsJ78FbUWyVNYvl%2FTfVkIAjuR6qDfMsU8LZFVIYrxDecNd%2BWJ3MqSsHBGqHFXU6Ksf9NKg%2FYy5ha8VsUh4tNLJ4MssMX8sQLvQATRZ0n041XuG4VTCnr9ZOcZgWOiXkFAuWHXPgd0d8lRXb81pCgKyOQzPGE0Q%2FrMU%2BRvRPBlczHQUdek11Xo56qsHa2olhG%2BpUfV1t8kRlTEGvK7O17zfPjwIl3iywllpdhA3QJu0Ep%2BZCQujHEWPxjqj7jZ5uBpVZJ6Uu%2FGgPj52885lJ98ZTwOZSK3OFR53vNVL2tV2XnynzJr3KEcv3eEAIeQQAn86g2J6vCfu0lnG7EAH9f%2BftYLMha%2FUgNw1%2FEfWNWjNXwVFBn1N%2FVrOcHJFfBI2Lg10iW6PMTLL70K0RpAiLKA0AR98HPRZWFwdYi5h7fMbbFnTRfPh2YTnp7yEoqvmeTEVPSvOMnaaYDS1UhdX5Q14MKE5mwm%2B%2FqnMyXiofLpOE%2FYu6%2BBTd8TSM5%2FHG2nyBQlZPRQbCTQIIB5dV2M%2FE59DcYL9183gXtLoBu4lQLwHmy4csPuP%2BnNthfnEae%2FfPt%2BmIA2%2FdVdSn1Uzn94hvXMiLxntW98epasgSMLLO98kGOqUBien1%2BxtIvWZi0LO%2FiwcCXEGh13Mzk7u6V3UJhmWRyljqkwjQrXrlLfRb4fLnDkprGsbqpxs%2Bb%2F2mypS%2B4UbDlsNpZID%2BVZ%2F63Q1EnpuLKqLOibu2%2FcVuvFZuEEZD4gwMG%2FLf%2FRGWzqqm4I1RXaSMk8YxOFcquNiCSw13WIU60H9BeI2ckSN%2F8p6Su4QTF3zk%2FkVZ4PO0HQm9BOPquhB0wzdfJxPh&X-Amz-Signature=83a6beef98c18088fd7a272a0ed37e6806789ea735520fe7a77fe875a813e6e1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
---

![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/e200c573-cf87-4f6d-9e23-021bb82af1a0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46627SNY3GG%2F20251214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251214T005214Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCICa0lKtbkIRSEll65PnT3dpR%2B%2F8HAkUOENkkVnZZBd%2BSAiEAjlGHoQZWIL2XA%2Bp6ge9jvKTmlxzEVm39%2BWrgepR4Qt4q%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDHgdH2h2EKSJNKYjGSrcA2HlEgbsRws5jRthUuQOYarkvTsJ78FbUWyVNYvl%2FTfVkIAjuR6qDfMsU8LZFVIYrxDecNd%2BWJ3MqSsHBGqHFXU6Ksf9NKg%2FYy5ha8VsUh4tNLJ4MssMX8sQLvQATRZ0n041XuG4VTCnr9ZOcZgWOiXkFAuWHXPgd0d8lRXb81pCgKyOQzPGE0Q%2FrMU%2BRvRPBlczHQUdek11Xo56qsHa2olhG%2BpUfV1t8kRlTEGvK7O17zfPjwIl3iywllpdhA3QJu0Ep%2BZCQujHEWPxjqj7jZ5uBpVZJ6Uu%2FGgPj52885lJ98ZTwOZSK3OFR53vNVL2tV2XnynzJr3KEcv3eEAIeQQAn86g2J6vCfu0lnG7EAH9f%2BftYLMha%2FUgNw1%2FEfWNWjNXwVFBn1N%2FVrOcHJFfBI2Lg10iW6PMTLL70K0RpAiLKA0AR98HPRZWFwdYi5h7fMbbFnTRfPh2YTnp7yEoqvmeTEVPSvOMnaaYDS1UhdX5Q14MKE5mwm%2B%2FqnMyXiofLpOE%2FYu6%2BBTd8TSM5%2FHG2nyBQlZPRQbCTQIIB5dV2M%2FE59DcYL9183gXtLoBu4lQLwHmy4csPuP%2BnNthfnEae%2FfPt%2BmIA2%2FdVdSn1Uzn94hvXMiLxntW98epasgSMLLO98kGOqUBien1%2BxtIvWZi0LO%2FiwcCXEGh13Mzk7u6V3UJhmWRyljqkwjQrXrlLfRb4fLnDkprGsbqpxs%2Bb%2F2mypS%2B4UbDlsNpZID%2BVZ%2F63Q1EnpuLKqLOibu2%2FcVuvFZuEEZD4gwMG%2FLf%2FRGWzqqm4I1RXaSMk8YxOFcquNiCSw13WIU60H9BeI2ckSN%2F8p6Su4QTF3zk%2FkVZ4PO0HQm9BOPquhB0wzdfJxPh&X-Amz-Signature=0f66c5384138ee6129c8cf97ce3d7e8baafadbd1a66b7e782a439ebdb5e9d7c6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/87d69575-840d-45b7-8007-1d1118cd9ca8/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46627SNY3GG%2F20251214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251214T005214Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCICa0lKtbkIRSEll65PnT3dpR%2B%2F8HAkUOENkkVnZZBd%2BSAiEAjlGHoQZWIL2XA%2Bp6ge9jvKTmlxzEVm39%2BWrgepR4Qt4q%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDHgdH2h2EKSJNKYjGSrcA2HlEgbsRws5jRthUuQOYarkvTsJ78FbUWyVNYvl%2FTfVkIAjuR6qDfMsU8LZFVIYrxDecNd%2BWJ3MqSsHBGqHFXU6Ksf9NKg%2FYy5ha8VsUh4tNLJ4MssMX8sQLvQATRZ0n041XuG4VTCnr9ZOcZgWOiXkFAuWHXPgd0d8lRXb81pCgKyOQzPGE0Q%2FrMU%2BRvRPBlczHQUdek11Xo56qsHa2olhG%2BpUfV1t8kRlTEGvK7O17zfPjwIl3iywllpdhA3QJu0Ep%2BZCQujHEWPxjqj7jZ5uBpVZJ6Uu%2FGgPj52885lJ98ZTwOZSK3OFR53vNVL2tV2XnynzJr3KEcv3eEAIeQQAn86g2J6vCfu0lnG7EAH9f%2BftYLMha%2FUgNw1%2FEfWNWjNXwVFBn1N%2FVrOcHJFfBI2Lg10iW6PMTLL70K0RpAiLKA0AR98HPRZWFwdYi5h7fMbbFnTRfPh2YTnp7yEoqvmeTEVPSvOMnaaYDS1UhdX5Q14MKE5mwm%2B%2FqnMyXiofLpOE%2FYu6%2BBTd8TSM5%2FHG2nyBQlZPRQbCTQIIB5dV2M%2FE59DcYL9183gXtLoBu4lQLwHmy4csPuP%2BnNthfnEae%2FfPt%2BmIA2%2FdVdSn1Uzn94hvXMiLxntW98epasgSMLLO98kGOqUBien1%2BxtIvWZi0LO%2FiwcCXEGh13Mzk7u6V3UJhmWRyljqkwjQrXrlLfRb4fLnDkprGsbqpxs%2Bb%2F2mypS%2B4UbDlsNpZID%2BVZ%2F63Q1EnpuLKqLOibu2%2FcVuvFZuEEZD4gwMG%2FLf%2FRGWzqqm4I1RXaSMk8YxOFcquNiCSw13WIU60H9BeI2ckSN%2F8p6Su4QTF3zk%2FkVZ4PO0HQm9BOPquhB0wzdfJxPh&X-Amz-Signature=3becd83e80516f9fec4f0669a7282e94d186cf1cfb855573bfed381cc07d793b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
We want to remove any elements in the three sub-lists that are not string
What happens if we pass the first sub-list `[1, “Hello”, False]` into `get_strings()`?
- First run
- `element = 1`
- `type(element)` → int → `int == str `→ False
- Second run
- `element = “Hello”`
- `type(element)` → str → `str == str` → True
- `return_value = [”Hello”]`
- Third run
- `element = False`
- `type(element)` → bool → `bool == str` → False
- `[”Hello”]` is returned from function
Function successfully filters out any elements that are not Strings.
How can we apply a function on every element of an Iterable, i.e., on all three sub-lists? → `map() `function → **`result = list(map(get_string, mixed_lists))`**

---

![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/9f552f8f-3ffa-4f12-bbaf-bf26c3a07af7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46627SNY3GG%2F20251214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251214T005214Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCICa0lKtbkIRSEll65PnT3dpR%2B%2F8HAkUOENkkVnZZBd%2BSAiEAjlGHoQZWIL2XA%2Bp6ge9jvKTmlxzEVm39%2BWrgepR4Qt4q%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDHgdH2h2EKSJNKYjGSrcA2HlEgbsRws5jRthUuQOYarkvTsJ78FbUWyVNYvl%2FTfVkIAjuR6qDfMsU8LZFVIYrxDecNd%2BWJ3MqSsHBGqHFXU6Ksf9NKg%2FYy5ha8VsUh4tNLJ4MssMX8sQLvQATRZ0n041XuG4VTCnr9ZOcZgWOiXkFAuWHXPgd0d8lRXb81pCgKyOQzPGE0Q%2FrMU%2BRvRPBlczHQUdek11Xo56qsHa2olhG%2BpUfV1t8kRlTEGvK7O17zfPjwIl3iywllpdhA3QJu0Ep%2BZCQujHEWPxjqj7jZ5uBpVZJ6Uu%2FGgPj52885lJ98ZTwOZSK3OFR53vNVL2tV2XnynzJr3KEcv3eEAIeQQAn86g2J6vCfu0lnG7EAH9f%2BftYLMha%2FUgNw1%2FEfWNWjNXwVFBn1N%2FVrOcHJFfBI2Lg10iW6PMTLL70K0RpAiLKA0AR98HPRZWFwdYi5h7fMbbFnTRfPh2YTnp7yEoqvmeTEVPSvOMnaaYDS1UhdX5Q14MKE5mwm%2B%2FqnMyXiofLpOE%2FYu6%2BBTd8TSM5%2FHG2nyBQlZPRQbCTQIIB5dV2M%2FE59DcYL9183gXtLoBu4lQLwHmy4csPuP%2BnNthfnEae%2FfPt%2BmIA2%2FdVdSn1Uzn94hvXMiLxntW98epasgSMLLO98kGOqUBien1%2BxtIvWZi0LO%2FiwcCXEGh13Mzk7u6V3UJhmWRyljqkwjQrXrlLfRb4fLnDkprGsbqpxs%2Bb%2F2mypS%2B4UbDlsNpZID%2BVZ%2F63Q1EnpuLKqLOibu2%2FcVuvFZuEEZD4gwMG%2FLf%2FRGWzqqm4I1RXaSMk8YxOFcquNiCSw13WIU60H9BeI2ckSN%2F8p6Su4QTF3zk%2FkVZ4PO0HQm9BOPquhB0wzdfJxPh&X-Amz-Signature=d35245d7c977e9c84c3b8b6f7401a5e793dc2dc488fc30cfb10fd505387de182&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
- Correct, `lambda` is an anonymous function, the function does not have a name, unlike a usual `def some_function()`, thus we can not re-call the function
- Correct
- If we multiply an odd number by 2, i.e., 3 * 2 we get an even number as a result
- If we multiply an even number by 2, i.e., 4 * 2 we get an even number as a result
- Thus, the result list will only contain even numbers, no matter if `num` is even or odd
- Incorrect, the function has a name: `lambda` → just a regular function named lambda, remember: we can name functions and variables however we want to
- Correct
- Frist, range(num) is executed → e.g. range(3) → [0, 1, 2]
- Second we iterate over range object
- First run
- `x = 0`
- `x % 2` → 0 → `0 == 0` → True
- `list_of_even_numbers = [0]`
- Second run
- `x = 1`
- `x % 2` → 1 → `1 == 0` → False
- Third run
- `x = 2`
- `2 % 2` → 0 → `0 == 0` → True
- `list_of_even_numbers = [0, 2]`
- Odd number (1) has been filtered out and the result contains only odd numbers

---

![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/7e3bb09b-7cc5-4186-857f-df89edd954cb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46627SNY3GG%2F20251214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251214T005215Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCICa0lKtbkIRSEll65PnT3dpR%2B%2F8HAkUOENkkVnZZBd%2BSAiEAjlGHoQZWIL2XA%2Bp6ge9jvKTmlxzEVm39%2BWrgepR4Qt4q%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDHgdH2h2EKSJNKYjGSrcA2HlEgbsRws5jRthUuQOYarkvTsJ78FbUWyVNYvl%2FTfVkIAjuR6qDfMsU8LZFVIYrxDecNd%2BWJ3MqSsHBGqHFXU6Ksf9NKg%2FYy5ha8VsUh4tNLJ4MssMX8sQLvQATRZ0n041XuG4VTCnr9ZOcZgWOiXkFAuWHXPgd0d8lRXb81pCgKyOQzPGE0Q%2FrMU%2BRvRPBlczHQUdek11Xo56qsHa2olhG%2BpUfV1t8kRlTEGvK7O17zfPjwIl3iywllpdhA3QJu0Ep%2BZCQujHEWPxjqj7jZ5uBpVZJ6Uu%2FGgPj52885lJ98ZTwOZSK3OFR53vNVL2tV2XnynzJr3KEcv3eEAIeQQAn86g2J6vCfu0lnG7EAH9f%2BftYLMha%2FUgNw1%2FEfWNWjNXwVFBn1N%2FVrOcHJFfBI2Lg10iW6PMTLL70K0RpAiLKA0AR98HPRZWFwdYi5h7fMbbFnTRfPh2YTnp7yEoqvmeTEVPSvOMnaaYDS1UhdX5Q14MKE5mwm%2B%2FqnMyXiofLpOE%2FYu6%2BBTd8TSM5%2FHG2nyBQlZPRQbCTQIIB5dV2M%2FE59DcYL9183gXtLoBu4lQLwHmy4csPuP%2BnNthfnEae%2FfPt%2BmIA2%2FdVdSn1Uzn94hvXMiLxntW98epasgSMLLO98kGOqUBien1%2BxtIvWZi0LO%2FiwcCXEGh13Mzk7u6V3UJhmWRyljqkwjQrXrlLfRb4fLnDkprGsbqpxs%2Bb%2F2mypS%2B4UbDlsNpZID%2BVZ%2F63Q1EnpuLKqLOibu2%2FcVuvFZuEEZD4gwMG%2FLf%2FRGWzqqm4I1RXaSMk8YxOFcquNiCSw13WIU60H9BeI2ckSN%2F8p6Su4QTF3zk%2FkVZ4PO0HQm9BOPquhB0wzdfJxPh&X-Amz-Signature=1710d9747ec519fbdd6c33b2733a622bf7856ae564446cffe0c407823706bc9b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- Incorrect
- Correct, we don’t check if the provided parameter is valid (greater than 0) or not, thus the function will be executed and ends in an endless loop which leads to a crash of the Python runtime eventually
- Incorrect, again the function will be executed and will end in a endless loop, thus nothing is returned
- Incorrect, the function will be executed but will crash

---


![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/48e76979-cf0c-4dc1-b92f-10422d1cecb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46627SNY3GG%2F20251214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251214T005215Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCICa0lKtbkIRSEll65PnT3dpR%2B%2F8HAkUOENkkVnZZBd%2BSAiEAjlGHoQZWIL2XA%2Bp6ge9jvKTmlxzEVm39%2BWrgepR4Qt4q%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDHgdH2h2EKSJNKYjGSrcA2HlEgbsRws5jRthUuQOYarkvTsJ78FbUWyVNYvl%2FTfVkIAjuR6qDfMsU8LZFVIYrxDecNd%2BWJ3MqSsHBGqHFXU6Ksf9NKg%2FYy5ha8VsUh4tNLJ4MssMX8sQLvQATRZ0n041XuG4VTCnr9ZOcZgWOiXkFAuWHXPgd0d8lRXb81pCgKyOQzPGE0Q%2FrMU%2BRvRPBlczHQUdek11Xo56qsHa2olhG%2BpUfV1t8kRlTEGvK7O17zfPjwIl3iywllpdhA3QJu0Ep%2BZCQujHEWPxjqj7jZ5uBpVZJ6Uu%2FGgPj52885lJ98ZTwOZSK3OFR53vNVL2tV2XnynzJr3KEcv3eEAIeQQAn86g2J6vCfu0lnG7EAH9f%2BftYLMha%2FUgNw1%2FEfWNWjNXwVFBn1N%2FVrOcHJFfBI2Lg10iW6PMTLL70K0RpAiLKA0AR98HPRZWFwdYi5h7fMbbFnTRfPh2YTnp7yEoqvmeTEVPSvOMnaaYDS1UhdX5Q14MKE5mwm%2B%2FqnMyXiofLpOE%2FYu6%2BBTd8TSM5%2FHG2nyBQlZPRQbCTQIIB5dV2M%2FE59DcYL9183gXtLoBu4lQLwHmy4csPuP%2BnNthfnEae%2FfPt%2BmIA2%2FdVdSn1Uzn94hvXMiLxntW98epasgSMLLO98kGOqUBien1%2BxtIvWZi0LO%2FiwcCXEGh13Mzk7u6V3UJhmWRyljqkwjQrXrlLfRb4fLnDkprGsbqpxs%2Bb%2F2mypS%2B4UbDlsNpZID%2BVZ%2F63Q1EnpuLKqLOibu2%2FcVuvFZuEEZD4gwMG%2FLf%2FRGWzqqm4I1RXaSMk8YxOFcquNiCSw13WIU60H9BeI2ckSN%2F8p6Su4QTF3zk%2FkVZ4PO0HQm9BOPquhB0wzdfJxPh&X-Amz-Signature=cea5e9cda1dae0264c04cb7536a37f73f3fd9a21b4951489d76d9635e8c73c23&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- Incorrect, even though we cannot use `sorted()` wit an integer, we don’t necessarily have to pass a string to the function as parameter, we can also transform the parameter to an integer inside the function, as we do this in line 2
- Incorrect, we can use sorted, we just have to convert the integer to a string first by using `str()` method
- Incorrect, function is intended to return a string and not an integer, thus the function does not do what is should
- Incorrect, Python executed code from the inside to the outside, meaning that first `number` is converted to a string before `sorted()` function is executed
- Incorrect, to convert things to a set we can use `set()` function, however, this function is nowhere used
- Correct, `sorted(’Janick’)` equals `['J', 'a', 'c', 'i', 'k', 'n']` which is a list, thus our function returns a list and not a string

