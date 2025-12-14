---
title: "Quiz 9"
notion_id: "09c7128e-aedd-43f1-9a4c-cab47219c8a2"
notion_url: "https://www.notion.so/Quiz-9-09c7128eaedd43f19a4ccab47219c8a2"
exported_at: "2025-12-13T23:17:40.802285+00:00"
---

# Quiz 9

## Question 1
You have the two *pd.DataFrame* objects **persons** and **addresses** with the following columns:
```python
print(addresses.columns)
>>> ["zip", "city", "street", "number"]

print(persons.columns)
>>> ["name", "address_id"]
```
The indices of both DataFrames are continuous non-duplicate integers starting from 0. The column **address_id** in **persons** is supposed to be *foreign key* for the **index** of the **addresses** DataFrame.
There are some persons that do not have an address, so the value of the **address_id** for these entries will be *np.nan/NaN/pd.NA*. 
Additionally, an entry in the addresses DataFrame could be referred to by none, one, or multiple persons.
Which of the following statements returns a *pd.DataFrame* with <u>all</u> columns of both DataFrames **persons** and **addresses** with the following restriction:
The resulting DataFrame must contain all entires form the DataFrames persons and addresses.
❌ `pd.merge(persons, addresses, how='right', left_on='address_id', right_index=True)`
❌ `pd.merge(persons, addresses, how='inner', left_index=True, right_index=True)`
❌ `pd.merge(persons, addresses, how='left', left_index=True, right_index=True)`
❌ `pd.merge(persons, addresses, how='right', left_index=True, right_on='address_id')`
❌ `pd.merge(persons, addresses, how='outer', left_index=True, right_index=True)`
✅ `pd.merge(persons, addresses, how='outer', left_on='address_id', right_index=True)`
❌ `pd.merge(persons, addresses, how='left', left_on='address_id', right_index=True)`
❌ `pd.merge(persons, addresses, how='inner', left_on='address_id', right_index=True)`

<details>
<summary>Explanation</summary>

Lets’s visualise the two data tables first and plug in some example data:
**Persons **(left data table)
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/7496c730-cb41-4f7f-af50-44c35591eec8/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TZWUS5PR%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T231716Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIQDdcFItJTrjZmjonoGyDeY6HjF6VqhtCa%2FZBceYm5GiewIgAMe5srVQYEzONmivcRC9z1rAzTasM4o4SPkP3Nh%2Bx1gq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDOcaqnAzb2wWJJAw7yrcA2yfWvCddUUyKGjICsQG5akwKvNIMIlT5WGUOFYpMZEm%2F713FgxkATur%2FlZRPuSiXUzynfLJBg5C71wqsSOsbwVtbZffumg5C6u3d7SRofHIJmGTy16GVeA4%2BXq9pugUc5Cwl7U9T8Qu17%2FfybyPEpTo5DN2fU7%2FxqtLA1tQsS5uanO%2FEB0vuLur9%2BXpqnSP1cX2gHwH5UEG7Pgw9%2Fc5P8Uh%2B2Cxg%2FsNN37V705tK16QFvK1TEh7UE%2Bhd0WG7MJ7ZOcU4uOLHEqY4zxNSReHVL3igY5cZOlnQ1exw1590MFaNkySrtpurF0ng9fEHe4RwcX6MqulqdyfKQb055ONcKAhPlWRlJMBZXO26kYjd1aheJNIvJ7WJoRwLD8nBWfIPhA64SFo1SL3g9Ir%2BkgATSXcYKCj9VkeLXrxtmTa5ScP%2B8Ugk5la%2FNglOOSVB9Hs3QvDVztVQkTz%2FHBP0D9DbUigxcC0%2ByAoqn0RQ14fCpLj7AM58N9dmTbPrcXw2o6Qp%2BLiBUhFzmgmIv%2B2pwBPgviNgu5MtLf8dDUYXbNXTqmV0XbANrerTJyKTB5YZxSfckxhairRxCHIbxD3EGp5TELjo8sI2B%2Bg674K4kIT%2BBIKiu4%2B9I4zPGwllCKdMMXO98kGOqUBxbOPGyczJi%2FGjK0kRWSzrH5JomOSa11wBGRWBMr%2FTILhydYiGzO60QdZ4hnyLU%2FW8IuTkBx3rzUZ47njKVbrCQRz5J%2B9N5VD3zx5YU7%2FTgZaV40T6mXozJoxYUaj052TwjoOVXOHZo4OxJQ6UwiHp1rZdIqMj6lBY%2Fsm2m7jKlV3kz27xo8wHj3xpRb9Dbv7%2BkuomGn4ZkOqUUmpBtfjsgLDaqGw&X-Amz-Signature=74710cb06d8a17421aac7caf606b3ec3c5860d1c04ce07f9923f1323c9fdeac9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
**Addresses **(right data table)
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/096ac0e8-1fd5-4af6-bd55-5f2706b0e926/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZO5M735H%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T231717Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJGMEQCIH7IAOkt53t8TOWoyZKY7cABQysvnfbWYhrXeJS01yeUAiAun1HYEn%2Fw9biiyDF65xKrz1lgtfLruvnmuMPzgU%2BR%2Bir%2FAwgoEAAaDDYzNzQyMzE4MzgwNSIMK1ng1Jg7gLuJjGAzKtwDuD6pJArderlcxmpahphz1AYMCdhszsrcVeyU0ooNtby80kVfxAvRz84RFs6V%2F2Ht9KHl7nvUD%2Bs0xU3Xn0N4px2DrVrzaRY%2F8DoV7kIIx4lZ3OZixAP%2FR%2FnZse6553QdsPSPo4nuhMZ0cJPYPLlWFZ455%2Bf0%2BTcvX8%2BoWRAX6CjBa90xW4Py2AaVg%2BruPxU6FvFPktpT68FRrd5H4qQX1waFF%2FhYJAoc7U9uG2nhPiAndrZJGbSK2Y0I0hMyRvnMQP24CHol4EKUyY5H%2FF%2FKtsqHyIvpQzFZfFcX3I7wHggN53dWuWBiWM7gpN15z663DrjS35tst%2FYlEtYacUSBk%2Bk7Wl%2BCbHf63%2FIMfktNJkg5ZCUPpfCDS08%2FvHxGEU6rdRdXjp8MHh8K%2FrN7bcO5K7vPkGqFRAPS0v349BBlazn2ivb0zqMSXdtaITUzy6zTNfvSTBFAQBwSsUDjDpM24s%2BKQIbgnfq1zDtY%2FtTglfxoO%2BUUBdy6bwLuIZvpKtWSK4psVK0N3zeULVUfZ%2F18IUBashqGerM9aMnKVqou%2B4hjU3igY%2BTqCUOttkQszK4eKHQkJL3L7DmHKx9yGhKPCurSmSju35JvG63CrtMaljdmMt5y%2FO%2BE%2B%2BiJD3sw4c%2F3yQY6pgGybMhLUCTJj7arAFj1kFxkZbk5z4dUcWedHMv4G2Ztz9uHJNNXe%2FHqAxx41xk1K1Dzgpk0KysAAM9nMWW1KhqfO0pAAk5DbRex1Uyhf0ScFEYwscM63F1ZcK3ZKPSEqJprDtfPj1R2TuB2%2FwktTdBIObHNvGUgxw81VkP%2FQTybH0fDPMXNgpXYSG%2BpUW7%2FPiKynQVYEiSkPtOj2MiiH3V%2BA%2FwBirzk&X-Amz-Signature=8873df39efce2022458452c1ff9fafa9e33941b7cd4f16a2f4dd128c15bb19b8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

By following the foreign key `address_id` in the **Persons** table, we see that Marco and Melanie both live in the same building.
We also see that Friedrich doesn’t have an address and that the third entry in the **Adressess** table is not used by any person.
Now we want to merge the two DataFrames together, without losing any data. This means that the output table should contain all three addresses and all four persons. 
We must define the following parameters to perform this merge:
| Parameter | Value | Explanation |
| --- | --- | --- |
| `how` | `outer` | We want to keep all records from both tables, regardless if an address is used by a person or a person is assigned to an address. |
| `left_on` | `addresses_id` | This column contains the matching value in the left data table. I.e., here we tell Python which person belongs to which address. |
| `right_index` | `True` | The values in `address_id` can be found in the index column in the **Addresses** table. So whenever there is a matching value between `address_id` and the index column in **Addresses**, Python should connect the records. |
This corresponds to the sixth statement in the answer options.
If you are still unsure, check the output per statement below to understand in detail what is happening.
<details>
<summary>❌ `pd.merge(persons, addresses, how='right', left_on='address_id', right_index=True)`</summary>

![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/91295b4a-a196-48b3-a33e-68bbace9fc32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SNGL2EVQ%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T231719Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJGMEQCIFwwgSOSyr%2B2TLoYprijdY8MtQKEz9Ca8kp9Vth5ciTGAiAjctegf6LRWtNVmqSudZXHwzXUxU0hS%2Bg%2BHqE3FtL6Myr%2FAwgnEAAaDDYzNzQyMzE4MzgwNSIMmH2crvsoQMzkqqKUKtwDJUV1lwdv8CKPCLD%2F8NBDQTO7OGJr7Dr8622ZyaM5tEqpMYv2EqZxHpEb4JIaKs%2BZzsNV35kcbrdO%2F%2FCsolxrAduui62azpsfGwE0GTIW5fwhsXZ%2BKSvsWDAyB2SFEQEtfo7SMQlE%2FBkwyX0ayWIzudXnaRxXW6GtLwC6cKG6DyFgCXVth52x6y%2Fuas9n7BuzRwn6L636Q7GDbms0NctrnP0yqOGoZ%2FBWFhvRtS%2F2dZ9rhOqkCppfHqTQLkyN%2F%2BzjR8HN5t08sdY14Di1pmnNaAZ8%2F7Gafj6PxOM0r%2FbNp2LffPrFMk3UbzA0HFMMAakvHOwv5Hobwi%2Boo5thD9a2jaDvRIfHTtt%2F6AclwEXbqRAUpwlSsa7nEsns%2FcNTdS3b6u0sJrxk1AfAwg72hMFIwFl2PeR%2B9NS9U5yri1hA5qAeQzYSPY9eDziRzg4WtqLc1T4xQerq64cbLIUc8vpq47do8AbFLKyI2064zyd2fB2FCTvO9%2BBe62J2Epqm41gfchB4bsV0hXStzLU9JGuQm30lUOxbUUBdAwG9zOfKuN5Q%2Bik5mvVlbWeZEhNX%2FWfT2TfUPrd0RAlts0RauUfeFGD53da1eRRDlnivbia%2ByOMs21J9obEtcSx6P08w8c33yQY6pgEkcAN8r2%2BI26F%2BEyhysxtk9CYcb07qThImUam4tS3FU%2FpzVYDv8Cb8WT147yrEoaTkiZ25dR5ECYQj8STXGH%2FrgeIx0ayQoI3xu32W3CvgxzgdY7HDEXJIbIYZOopPM97T38llJg4Ki0gVhGuuH1M0YdTyFHm74ccX%2FDPhDlbdHptUuGHTaB9OH8bUpYHIW2%2BkqPmb9ggZOX37kSTH%2BtTl8slDsGGZ&X-Amz-Signature=4749ec2d152e24597b3dd162433f6d57d3b309fcbc6e3b3e7f09ce69229d4f12&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
→ all addresses are included, regardless if they are assigned to a person or not
→ where values are missing, NaN is inserted
→ only persons that are assigned to an address are included
</details>
<details>
<summary>❌ `pd.merge(persons, addresses, how='inner', left_index=True, right_index=True)`</summary>

![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/ead1aaf6-c414-42fa-bb00-b88bb8c18882/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667HVGSRG4%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T231719Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIQDkk4hjaygkMfilMARd1cOsiTce0CgmJ57pidK8pCTYXgIgYgC7jy4PxtFjg2rQ3m7G2MEGpvJr2aeTWwjbj1K7vcAq%2FwMIKBAAGgw2Mzc0MjMxODM4MDUiDNXr0%2BZmhppBwh8mwyrcA3B%2BRKgbjXkH7woqsN7WkB9XNm0kVjadyyu3vhZq8Vsn%2FDoLoiMPI0TE0PhIDPJGC9%2F63KSRqvcw3vBlbzcvh2oZVRDuJpYe3bEn7aOP7K5YFWbvsng29tmI%2BNNS50OFmD0izpTkIcD7GnBxHAfCr6GNwMwsUo5UHvYvMNvHkNPUVZjrCi4niRwm2OCQOGwCGYH0U3xPN572lr4CW%2FXNxo3L%2BsVHLcJTtQk3LJfKvAwGeCcA7b%2BVk%2BZr9pWfh9gLCRss%2FHGl73IEBvj9rDteNGXRFtT3rBmPGHpGF7JmuJ9RHFMplHsaoOO9FIhPwNQ3tuRHVS8I54qNhm4q7Q5tv9xkmy%2FxA5EG3M1i0c30rZbPi7XJYq8SY%2FS8DgK3w7KLr6uuBIfVW2sdQlfwdfaVwwQOT8Iup92JIB1N7oZ9QXwsqW6k45OsVmquZaVtq%2FNWq9pgAzXpgz8zFBLP66pDpu9RaZgBsV%2BaR5yWaYUF0mVJLqiqMWxa41Vlel7Jubnv%2BmuFELaRsAUx%2F7Cl1MaypNL0yfgFEH0fgMqxja3DOR%2BE4P9RmanbOmU9U0bRGWXW%2BOR4v8Dix42sDk0m%2BVJAM%2BTb0VUy7eo5wxj8SbilGAFMlcjwdBWS7QUk4xOWMLXO98kGOqUB6TEcNJs0EgZc9lA%2FMA5EoQf%2FnwfqZ0FJmk90hoJE81kgF1vx%2FBXRgN5Y1y1C6wrXoEdRRlL9cQhVMlN162A06k%2BCpVkH9In8EAs5%2B2RP2kroMUW0sJc%2BV7uJQBvvk5uAlT0942KHr8sg3j75M2XJWOg0W3XmmwheP9XrC6r%2BdBlL9XJfIVVv1JEzQJ9%2FLuAhKDX9S8TfcusXxyDYUD0bxH1Sa0v0&X-Amz-Signature=359ec68d7ae42bc76762d0e1c383c56f1a71b3d8e56635ea2ef339bd4060e28b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
→ only addresses that are assigned to at least one person are included
→ only persons that are assigned to an address are included
→ However, matching is done in the wrong way, over the index column in both DataFrames. Thus, Melanie is assigned with the wrong address (Bern instead of St. Gallen)
</details>
<details>
<summary>❌ `pd.merge(persons, addresses, how='left', left_index=True, right_index=True)`</summary>

![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/87be0349-c455-4f07-ad7c-9be7413cb92f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664OUMX5XA%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T231719Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIQCxlklY5NnZ%2FxTxuzJUMRY2q4BGSdGce1oTq6H1F%2BIbBgIgfK1k4dS6cjuVwF0J%2F50IcZAS8K6gaiB1XtuT5F9oZ%2Fgq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDOukLGCzlARWKElpcCrcA4XV0f1mMCoZJtF31peXDjzGE4vqVQngW2MJpEfPXWI%2BU36SoJ6xVTN0DsSQlZAbMXwB0k3J99ZVL6bRrk6otLMSb%2BNo1Cg6pks8SzUE7fyjczLqGbMrqgdNutqeEMNuL9ACAwmXi925YgS0%2Bu5r9lmWBkMT5OrzQjPpa08HQB6IslZFaNr8Foz73UfnaAC2tCtyOdF3lxVOpav5F1hCynEmfN7GFrumswWBCSSmdJ93rOPw4MZfHCimCYu5JPDjWDnULHSSaaJWz3wNS%2FJWVT%2FhWMTZwx67SmDXRtQCahFQC3py4vfS%2Bv%2FBoYfoqTZuJRN0uSdUDlozuestVb2WrHX31nI1VJKXlbHdh007ZRJrWfCJ1aqjGd%2BfH3gixEHJ8YFYbs5%2FIG5y%2FoVLLo0pr5UyImxYK%2F%2FwGIM2JYSoZh8ke4GdYsE50DUNu%2BOciHovFNrGgNCIBbRUkf%2FJtrk3VBWGy9RE96V9cM%2FcBSxwrXpi59LBB9%2ByZY9NbHQNpQERS5x6I2lXpZUWPgi0wBfVv8MzVqlQEzz6Dqolsb%2FlwXkxXn15MYeNL98o1eqtyBLudZOm1k0PiMV%2BgkPVBRpSY12JmFp5S33PmuT0PFAQGcNpUYGb8F858IPCTXCQMIrO98kGOqUBCBk8e4aIkRIIsWMRSTLMvaR5NAPZscjWQ%2BZKsSy4LLiICELtwieMqP5UbdiEs5z%2BGV3uts%2B2uJbTkeSrnFUeZgI4jH2LEiHUc05lK1hE9T3m5eAUdZOFKEGDJYXXj3Chokzz5y8VguoF0UkS7YNnCmBVCizgIkrXYpTJg78lw2hd87n2xnx%2BNkWQZz6Offx7EYUDfMK%2FaNJHpDVqGTL5MDPgQ27A&X-Amz-Signature=4929b87b0767e0988f6ba9ad346b6ab04a76637fe0c260eb91e1ab744814c768&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
→ only addresses that are assigned to at least one person are included
→ all persons are included, regardless if they are assigned to an address or not
→ where values are missing, NaN is inserted
→ However, matching is done in the wrong way, over the index column in both DataFrames. Thus, Melanie is assigned with the wrong address (Bern instead of St. Gallen)
</details>
<details>
<summary>❌ `pd.merge(persons, addresses, how='right', left_index=True, right_on='address_id')`</summary>

**KeyError: **'address_id'
→ There is no column `address_id` in the **addresses** table
</details>
<details>
<summary>❌ `pd.merge(persons, addresses, how='outer', left_index=True, right_index=True)`</summary>

![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/9f0a6977-7c62-42fc-bc16-72859d19254a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZGJPSVCZ%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T231721Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQDrduHS%2FB2WVfO4HdustZmCaO7Qd3WQSIc%2FDXZnmRnapAIhANNacOiHjwhv9mvDfhqRu%2FG%2BGdEDSRjAms7OdCoLpfWCKv8DCCcQABoMNjM3NDIzMTgzODA1IgxjDFICeNQMXNQAdc0q3APKUCL%2FLBGn21XsHvxdwzfTYvLEMNXm5M9izoApHVZwiMEuYjyzgByNp%2FrT4YPOlYnDH3fJ66V71Yl53rLQmBWq9j%2B0O04SLno9D6Fu4S4%2B2BsNMYDipZilgJhaTShStF4Nvev2RSH57RZmRep5TM0f1eDm%2BLK01xJD4nlQ3FrzgUNYECAON%2B5V7PDn8Qu66JOD8q2zREFBBO1pQFYTEt6aMo6x7b%2FXQA7hJagKwqUSQqTtk9HqxNcUUilFIRECw%2FIAU6fn%2Bzi7IAcMhNxxuVlKNChVfkECYRavofwbgeMMQGlXYjbIY0sN9iW7b4r6MvScO3CrqGpsUKVS62umEmh8osVwEQYVRdoIU1zug%2FQwOIEoDnRUKkU6VbjzIlgUqjMaAiLvpKcbcjBF%2FqOVTZMww2uaok8FI0ond0C8yFVP0ZzktI2LRVnTuVqj%2FQiKfac7KGdI3quiXoTL4cPZwcYaShvT%2B0%2FDHyk8crm4G%2B8YHpSA8N8m8Y9qoNPZUo4VORRCC%2BkLf4ZYPCU%2BJbhQZnWz3Qg2jUBZAy5gORwqB0vUuBEjFujST2dmDPWEm2gPqgyVFZBssR6gwapgbmYcO4HHjdY0spCg8fuwlddg56IgGvbnhz6ONOUMFMSVRzCKz%2FfJBjqkAQtAymkCRmAW0ezJJBFgqc2OlMnC%2F9A9Fsht0q%2FK%2BXRSEFil1jzZwnFDDY4MOx8x%2FKW8UYFCh5dMnFGZGtPD%2BN4PmEgGHOC9xfNb4yZXRM7P7rCeEvPiUlhgNvXGVYo32TyeSE5VsW49DIj0GJQOGxf659VuDobOZ9sekRS1p4WqtvXjrUTMF%2BkLYaNgRFCg8sapKR6W3BIx36GPJobC71xuP0xK&X-Amz-Signature=bf1c857439859a8e5bc6f3cfc857f25f8009ee3aaeac733969ca7b9ad8e24627&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
→ all addresses are included, regardless if they are assigned to a person or not
→ all persons are included, regardless if they are assigned to an address or not
→ where values are missing, NaN is inserted
→ However, matching is done in the wrong way, over the index column in both DataFrames. Thus, Melanie is assigned with the wrong address (Bern instead of St. Gallen)
</details>
<details>
<summary>✅ `pd.merge(persons, addresses, how='outer', left_on='address_id', right_index=True)`</summary>

![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/bd8f2a5a-01bb-48bf-9f2b-40d2d8b90f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662GRSH5MQ%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T231721Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJGMEQCIBs1Fm%2FemHn6pwJFPD1v%2BYfRuXAJE9LXKHc%2BvFpz5EKcAiAwhSmrFM4KBBzO2gDAww5N0x16%2F0taeDE5MX9awv7tfCr%2FAwgnEAAaDDYzNzQyMzE4MzgwNSIM%2Fj5Xy04NU5HyyhMNKtwDOtapcfVf2jFIUZIPHsJdjDpf3MgQ%2FiUwKewpAWxnX5L%2BZmV5GGFOl6ULLZrHo%2FyI6az9CZa%2FzYLn8nsdWgevp3IMeDJmwkUItsIwPzin1kRxnFjJdbZFU2S%2FW9pMNKHcpUtowXqdz4xmnU33Myf6OJJe3wbZMXiTmWD2GtI2iDp2vRT7LDaiIkPMQMjXNTnQ9BoMaHUbj2b2%2FKKP1omqsm2KTiY%2FjoKbWoXYtQC2IhJ13%2B1TmRdQpndW7N2zbS1l%2FNMrNnZj78Yp5plsvTocHri219BIlEcZ869ZExgfWtjXFirLvmhWwStAO3Bv0YXQXWeYvrBfB%2F%2Bkujo1Dpf1HHlgv%2FboaUZFvmlQAifETDOFmI19m1kkk6qdFnR9rPG%2Frrftix0kTBfNIEbo0Pc3S2n96AeCQwgaxUB57OVAOPFC5eAXY5%2FAuwQhem%2FGDthLBb0ymnHI%2FMhkIEFQbgP3l2hlamle68pSpF3qW6rMsmgDPsb67er4Lv1SH5wXUXcDSioD0krI9gIRzXFHaSLDrY9IPmKGXS9t3Tm8gmrUSPZMnrDNShR16UTMx15jKBnkknm%2Fc4u5FqL3i%2Bnxop0X9EK4JhiNKBpWsKygjNejT%2FL6kvwy8suxzo0Ib7gw8M33yQY6pgFqiFBPwYawH5O3ZUzVGWrk1T%2FWa5ZECuP7WFQB8ATiI0AX%2FrKowpYBiMOefUYeUYZ0H9dlrt41JIrsnZ7vggM8Fi3vkh8E10qGhQwmdjJwBoj6sry7KGk6Zd9JIBfSmknpyn17KDPvOvq3owowM4Rb%2B4bWyYw%2BQuv7K%2BNMo5Hf17r0s2H6jdvDAtmXeI08TzWHAN8UuyGCn39wQPIytlB3zaTyukn4&X-Amz-Signature=a1af0080a4ca586dd86912175a0e6675703ae320c1ad6f2d222869e38c04758e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
→ all addresses are included, regardless if they are assigned to a person or not
→ all persons are included, regardless if they are assigned to an address or not
→ where values are missing, NaN is inserted
</details>
<details>
<summary>❌ `pd.merge(persons, addresses, how='left', left_on='address_id', right_index=True)`</summary>

![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/79add2f1-05d4-4b12-bf06-902e4b32c1d5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SOO7PJAA%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T231721Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQCmzwVPeCIoR0SIF1xKOKBz%2Fc8tLOjwGNrLDJG2giL0AgIhAJDpiDCl0cANdFf3sCWTgliiN7T1BgjmnJOTvviFLE9UKv8DCCcQABoMNjM3NDIzMTgzODA1IgyWTOamXWdooq6GWzAq3APREwS6lWkziz9w7LUEv2iMPd5bGeE%2B%2FiEOQxUKQjggsEeS7AwS4%2F4lX4qqQ4pUbYMadrAlIff0j3%2B8cK6eo8f6ibxclP8bE1vk0TuutLDgnZMDkgaQPFtWv0vmDsOr0%2BVhHLS4nhuPcFjAVQW7afSteW6ROBjfWmpPsrcVYUUvWTqCSq35mMM%2Bm7rFa%2FWtcRwpEa%2F34D7holHA6R%2BnVi3ERJSd66T92rCX73QP7gvjVPNJ3co0O0Ask%2FcD7Cuoby6xvF8nfGEslQs5NAicLFP3lL0jGh%2FnmxTIPLDEO%2BWHyx8LH3ox65qY37Pb%2B%2BPhlSnqrAvHbqjRc%2BvxgwPhBhfx7hGoTD%2Bq7u2zOBxdXewDPs4%2BgOmcUhv2zX8KKn1z0LypzCZxFbZKnGykg0QaTuHuQTLbgH1SZ6upoUhqZoideMw8Mnmz1CzG6u9JcXHFGC9eGsHhOa5HHKRGCJwCIF%2FyTKbvzJyE2c6Xpfz39HxFO2dlH5XbsgIvIVrYD%2FDecmkuyjObur5j2kEro2%2BfW%2F3ycHN1Npvc0cd2fp1HzkM0WHUXpzLss7KEQ2EwOaXf4TgAD42SG4a9omaBg0NiOSwXOvghb9lnDYV1yH88vRrLDWQyiwZMzw0k5gmeRzCNzvfJBjqkATSf6Ciua0TlR0F7pNgoyJv3GBsa2EZWNao0SXHtykeJWMTDuR2yXHHPg%2B6jsgQDvzVEZCMXtbSvlH2uA7l35EXlIxOjbqxcYdSW2nw72yGC%2FQZcynmcqS7ACDpWcP0FfovFvrK%2FGhGb%2BJc3NjsrjuiMuM6aLPez0nmonC%2BAYg6Ayjbg%2FeiLugK%2FnTLhE%2FE238RoO%2B%2FwNDJ3wZvK0YpOl43S5Vd8&X-Amz-Signature=871757dc157e095381b2874047cee70150166385d2fbba4be5382f25b61d84e3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
→ only addresses that are assigned to at least one person are included
→ all persons are included, regardless if they are assigned to an address or not
→ where values are missing, NaN is inserted
</details>
<details>
<summary>❌ `pd.merge(persons, addresses, how='inner', left_on='address_id', right_index=True)`</summary>

![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/d82929e6-299f-486f-824a-b346718e0dbe/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q7JXL36S%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T231722Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJGMEQCIHCO7E9noy1DqM6ScjyoskJ155SdO7ScVipBZhe2pZIlAiANRae%2BUKLdqxp2Hx5O9bwyQ8uEyhBNu5NdZMmlhE6R%2FSr%2FAwgoEAAaDDYzNzQyMzE4MzgwNSIMy1UJ7JRQfeY2TyZmKtwDJ%2B7wIxAe7j%2BIH5jTaO8ld4dvSMC71SJ6Vo6XV7x3Lkvja3EhwWf1p%2BYMkYZohQc8hm%2BfxdK0c%2B2e%2FGu%2BYX9O9pNv4pmbKFO8DNGBpKimZPD%2BF8uv6Z%2BAeBsL4x0RhAztJrqdPKD%2FCg8mKo2ET%2FjFBAyFyQP0R1rEcZZ8DQcP2pIZVBivH39%2BBEBJwN94t816hkDWKCsIdujLoGbfG%2BhAF9eMyVLd94SVQx1aizFK%2BfW9NzfKqBLZe65M4qMcO1BBloGfs0ct8sla1qnVXq79igUPzayZFy5iDgF5zVOrPCT1ualX2Ck%2Bn5aIAN2yZYIpwga5ritnXXNqogHwB4amKYobt6Pe7wplu6SFNR88GHjZE3j8QHAe0RcVwtsHd2P1Sfzs5Q2VzBtHmAv1u2l%2FaDNReaTtZFOQuugHrVw22l7HAkv4TuuDHzHLlVhZSi95gT7tjEzhoG5HJz16qbQPrFk5IaG4Se%2FbDlizrPuuXBOnj8UkRRi3VP0RFO7fPxqYNzjb1iEjAFfE0AsHIMktnrHtU6yB6QvFNXx2vaskn61pDGdN2uwi0c%2FAHJLnQiyMel03PWb8d2VbLug07SW0mJvPdVpm6VTEXS8aAVPDMplQylPOMNRLncThmE4wwM73yQY6pgE3JsWsintKU%2B5y3b27gUKduJdUMC5SrF3KwBEwvS2cdyf%2F%2B28mfpBzD8lmo8iQgXbrMG4jZ5Pxf0csZbPuXDVWJzqVeLGO4e4Xv4zDL1tRuTI8D%2F2tBq4wxirtsqLRVgc1wstIqC5NqCtblK%2BtWKRwI4SQzzkouJjuyT8WCaBfltr%2BxE1w0VvWZ3ICYcRyrIdVTLtBbv7YfRM27PqIDrkTDnrxYdVA&X-Amz-Signature=833d74525f64ba9ad27cef2a1063eab4012a7e6e0069d6b5b203f3d8f520ece8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
→ only addresses that are assigned to at least one person are included
→ only persons that are assigned to an address are included
</details>
</details>
---
## Question 2
As a nice housemate that you are, you prepared Christmas presents for your family. 
You have measured the height, width, and length of the packages and saved the information in a *pd.DataFrame* **df**. Additionally, for each present, you recorded the name of the recipient in the column recipient which you set as the index for **df**.
How can you aggregate the minimal height, width, and length <u>per recipient</u>?
The result should look something like this:
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/daf59472-35da-4221-aecb-ad0307bc494c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V5OQ225T%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T231715Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJGMEQCIASQQqDXiXM93SPZywnnX%2FpjWGutesERTiXYWCfoUecYAiAxtWHjd2PTCmEbsJRyMyGqcp655yBvbVE8CmUf7Bkbvir%2FAwgnEAAaDDYzNzQyMzE4MzgwNSIMAKDZ%2FQueqJ6jxzpnKtwD9mmpnlCZVYpLe0woPZPdsQunTljAZEflZIVbVYAMvtgIkub5byzAdH%2BDI%2B4rJohpjDt4D3y5PH1e7weL%2BStt4maz5MuwNbTr5Orlbz%2BH72i9sYXBbIUb9tmiiTQU3x3eULXl8KmeZjDus8E32ZObO%2FSTAsNwVBE05fiRIuSxAKOnOINUR59876Y4ziscsiWWNxIF%2BZQTRJ3xx05eD0kTN63KSlac9xzX78Y67AA3JisoI7vtZfLbwn3hAvhlsSvKjEIhHlNTv4u%2B6B%2B19zfP5alb0XtX8hhwDh4gFN%2BbgGzWcfDi4qmL0mFJbFmb%2BsezwdRJpZGlQPoj9GBO5hHN2XzXezQgSKe4Cu5%2FKbFg1Cma%2ByYjLjFNjYwkGwM%2BHu0i9qp4tfddMbrayKZFB1plRmuKHbc077CZWWMmXAJMReFKHF2NB8SIcsUq7AEqsZ9xmof9rZ%2B5vjOUJDq0aVXDG9wMMGCAiipgGW4p0o%2FTVlzox%2FaCCJCw0Qkh3%2B9OSModZavvsM3VCIbebTlXZJEQNgBWNk0q3XlYXdjh1a6xIhBEPag8gJ8aqYQt4BtHQUy6D2qhdZ1oJmn%2Fi0vvWWxvGaUFVfVspWStwFNjB%2FL3IgUycXybPzkKeMFxe8Ywjs73yQY6pgH%2BwX9DPupePbwBcYnTIlsaBokmW5K8M13l2e4oV9YjDyjUpzloBh8ZirvPAY1m2sZN6a%2BhkVxDIMwxjeYMvQJt%2F82XmWoTq7cPV1ZWoaKxzHjvk1HX%2FQlvLYWo5SH3XAR64sUjC1eWVoRx42MOvaG6QR%2BdOtMe25NIj2pqMPPl0BzOXJq9vcBtW6eaLqa1VDIECU1Y8dnwKlXMjC3AgL386hvAhf2M&X-Amz-Signature=f343b26673bca3765f56e8ff6b9abf1e07d617d65cd0d3f95d717ff4215a1ba4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
Mark <u>all</u> statements that result in the variable **agg** contain the *pd.DataFrame* as above. The *recipient* must be the index.
❌ `agg = df.index.min()`
❌ `agg = df.min('index')`
✅ `agg = df.groupby('recipient').agg('min')`
❌ None of the statement will create the wanted DataFrame.
✅ `agg = df.groupby('recipient').min()`
❌ `agg = df.agg('min', axis=1).groupby('recipient')`
✅ `agg = df.groupby('recipient').agg(np.min)`

<details>
<summary>Explanation</summary>

The DataFrame df contains a list of all presents that are gifted. However, there can be more than one present per person (recipient). Therefore, we want to find out the smallest present per recipient in terms of height, width and length.
To solve this question, you must understand how the .groupby() and .agg() functions work. As we can clearly see from this example, there are usually multiple ways that lead to the same output.
❌ **Incorrect**, because it selects the smallest value in the index column, which is the recipient that comes first in the alphabet (Bri).
❌ **Incorrect**, because it selects the smallest value in the index column, which is the recipient that comes first in the alphabet (Bri).
✅ **Correct**, it groups the presents by the values in the index column and then selects the smallest value in each column per recipient.
❌ **Incorrect**.
✅ **Correct**, it groups the presents by the values in the index column and then selects the smallest value in each column per recipient.
❌ **Incorrect**, because it selects the smallest absolute value in each column before the grouping per recipient is done. So the grouping is only done when there are some recipients left out already.
✅ **Correct**, it groups the presents by the values in the index column and then selects the smallest value in each column per recipient.
</details>
---
## Question 3
Which of the following data types *can* a query on a *pd.DataFrame *return?
✅ Panda Series
✅ String
✅ Panda DataFrame
✅ a 64 bit float

<details>
<summary>Explanation</summary>

Let’s take the **Addresses** DataFrame as an example.
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/7795a55f-ad9a-4b4b-bb55-e1f6fd9dbbd4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ROLO356A%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T231722Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJGMEQCIBCR7wEfqIwG2yUOt0%2Bwd0VPt87RLe%2ByQCXVzNWFnva1AiBIDaM03aAKKSkFqXmNqbaq4HxKdYTrsIpw9N%2BWUtLChyr%2FAwgnEAAaDDYzNzQyMzE4MzgwNSIM1%2Bx9xl3PIqZ%2F%2Fo4TKtwDxVBe8dQOotfEaMoTO4g2feIzXNNWpq2nF59wDA4t8Q4y5ywxMkLb5hcjh3UYDjE5Sm9hW7EJC09T1U2%2FZ8YcXJB1pyVdESHseQf0g8PFTXheqRWwW7OMj1fzpNF%2B7%2B2gzwgkTNQTknqFQO8vMZstQnW4ejJK4ERHcokjD8jbzsSEX8HzoSWTG4ClLahL2sszat49%2F%2F1S0UnqdD2w00egcKg2IwTZx24Ezz4BnJaNcGpE0LKpRfUSmJSP7Wu1DOzVwzmj%2BTTjO6Zqi4SQ3hocsG5m2vYKw7ia7lhnRjRHRvbHccv6%2B0%2F54ewluEcJSkN3SEBs0WIG7YOufGRJuRX0pm%2BTMzn1t%2BpdJxblTJMLGP9W0kPCQztrHDJ9ur6d4LLZHz%2BepoGCwPVqzkvXcQGZiHzKESNOxZlafbLVGi4SMcyzRmmiQAoTzVIBW3wNsiq1YMqrAbYext8BQ%2BlZCyOJ35F5%2FdsXR%2FIuBuH1fWWdKjujmaO2zeyRqRyEtP2jgYBr3l32yvYwFlBko2pCL4yafkjgkzcPEtCWea%2B%2FBvwzBHEuslnNXwh8UnDXkdwYoN7CjBWTZriWJvUrB10449oZmEzFQ3in3jeX1lDPQlA2gbBtdlOaTodMX6gFfBYwws73yQY6pgFqwn31ksokdKJzTGJs8yQhK6bhWf5SiYdEeIZIv0bbrld3e2UOeHbONzkH78eoyKBElS1hUV9NBU5CHbqysIfgep5MfzX%2FpecTkEdVrPgbxBQeaDJhyGdyOvyAGNKS7luM16fM%2BM0%2BahxPGn4baB93zeBewheDowFA3GoD9jSLJlrO0O9qR2gjvCnuRQtDl6J5jZIP4GYcFVd9%2BEPqmBcQc8USAM3C&X-Amz-Signature=f945e9cf82cbc59895c84f66243c2f8d3298e710d688de1978de87c434053269&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
For each answer option you can find below an example that queries the according data type from the DataFrame. 
<details>
<summary>✅ Panda Series</summary>

```python
addresses['zip']

0    8001
1    9000
2    3000
Name: zip, dtype: int64

type(addresses['zip'])
pandas.core.series.Series
```
→ whenever we access a single column or a single row, a Series is returned
</details>
<details>
<summary>✅ String</summary>

```python
addresses.iloc[1,1]

'Bärengraben'

type(addresses['zip'])
str
```
→ in the column `city` we have string values stored, so when we access the value of a single cell, a String is returned
</details>
<details>
<summary>✅ Panda DataFrame</summary>

```python
addresses.iloc[1:3,2:4]

type(addresses.iloc[1:3,2:4])
pandas.core.frame.DataFrame
```
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/74745340-74e3-415c-b85a-171ec7a2ebcf/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZIG4Q6PI%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T231723Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJGMEQCIDyiixlSfuFi7VQsrnN9JIvGYu%2FwgaAtLbaFvnGZuAf7AiApQyzI4krj7WqPeMerAUOYKx402mOIxyVVVUZPw5qPQir%2FAwgnEAAaDDYzNzQyMzE4MzgwNSIMXPnPmvbMS4B3CwmoKtwDY%2By1YfDt80t4o0c3K1P5Y7vR5v00t8jBCmKLrW7F4t5Q2ZOOucF9vQiUEw6Bt%2BOeYcUdvVGuPqdx5sBayKGxqMPh7zSfJuKJXUoXcMfC%2F0kbdLUkNqSMG2Vf%2Fw3GRAFLklaYUlxx2hbpWw9cLdP9g8WAK%2FLj0lRt35CP7qlVqxdRyT4PW2rR4LiRc2jS4Yvf9EQcjF0OMpRPCx9OQOij8ah1p%2B94jlzx7H4mJlKk4M6kWNX03SpUwEZm8oazv1aR6kB0g3J%2FRnRqusBnuvtTKosLxpK%2FGQtc9yM9Gv%2ByEfPaaebrMz10MSC%2B64UORDsgUKyTnhH3WNBRAv86FgIfPm3dTCFbPdCaqEwcyjAZ7tm5MQMXBW%2Blrw7rWe0iWGdsdAzEDPxYIQ4EV85zPTYqzC%2FEPX9R2h4J%2BEsauy5c%2FoHPmX3Go6cJmJ3DBCtpg8Pc4A%2BARDLUxDgPPAhvJmQA%2FMB%2BOgbeFGMzu5BjoZe0C82D78yGjq2EPWWbOhhdnQL8ulMLbi6A85RmTZQbjYSP53gKm9oHIz12iWP1F3u2eKulFCWzN5mO8K9pyUyUDkJbjtYFhv9BsSnLO%2B6KFT8aLAFfJYkLmDqRygLcbDQl%2FhxGcvD5k8BSoFDqGCUwj873yQY6pgGU3ogewUr97Z6OaKJgyWjxYn4L8KifacQX20K70YZu3V%2Bqj2hDI9Wef1SVfhmgqzalZhN0yA5Vw19L1HqozV97QtoSrPoQHd0c54wndUnuhKeeFhbvt27QDrePkvkgBMtH%2B3W1C2PJv2bY62wuhNNjPHp3brE5KX8%2FNfUe5rAXtOPTy%2B53aiiB6%2BBiNThqRAl8qtLmCDg6NpNLPzag2Yp36R865YHh&X-Amz-Signature=5717aef56ffa7f018a0290554361b9b4f0b0da4383e76cf7a2baf6c655ba4d3e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
→ whenever we access multiple rows or/and multiple columns a Data Frame is returned
</details>
<details>
<summary>✅ a 64 bit float</summary>

```python
addresses['rooms'][0]
2.5

type(addresses['rooms'][0])
numpy.float64
```
→ in the column `rooms` we have float values stored, so when we access the value of a single cell, a Float is returned
</details>
</details>
---
## Question 4
In Assignment 9 you implemented the function *study_overview()*, which works on the DataFrame STUDIES. It should give an overview of where which combinations of *courses* and *regions* exist.
Now look at the following implementation of the function:
```python
def study_overview():
	return STUDIES.merge(index='bachelor/master', columns='course', values='region')
```
Mark all the correct statements!
✅ The function pivot() must be used instead of merge().
✅ *index* and *values* are set incorrectly, correct would be *index=’region’* and *values=’bachelor/master’*
❌ The function reshape() must be used instead of merge()
✅ The function cannot be executed successfully.
❌ *columns* and *values* are set incorrectly, correct would be *columns=’region’* and *values=’course’*. 
❌ None of the above functions can be executed on the DataFrame.

<details>
<summary>Explanation</summary>

If you did the assignment, then you know that this is about a pivot and not about a merge. Thus, we must use the `pivot()` function.
Before pivoting the `STUDIES` DataFrame looks as follows: 
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/6ccf22e9-5b8a-4115-825d-54ea726f78d7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V3CZDQPT%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T231724Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJGMEQCIE5p6ChEmzaiugf4eVGjbaDkMozjzpcZxHZxqQ6HzdvMAiBjA8um827XvC3yFI2wtEli2mgI1WKcqfKZaQmRXxjARCr%2FAwgnEAAaDDYzNzQyMzE4MzgwNSIM%2BNd%2BB6lXNd2%2FTm%2BtKtwD%2FeAkSkoVMmxCzx1BM2n7%2FkHomldIylgy%2Fa9584TXIGHuF0mnzuyUGkNjru1HeicH7LbnC%2Fc8H%2F9N32AvBFviPMD5BTSuRUk9T05izcIf%2F%2B5lzTrFGkw2R%2BP9rmRSakAfSOyuT0fpsooSn2tParEkuX4lUVRngb29MQ11QOJpXcTG3pMivxrQRfKCu%2BglYKYbPzMR7exQgkLgJbuSN7%2BSR%2BTsec1Uucrb88Sa0OpYs6ktWCUTOSFDzhhQTWeXpzPUA7QkrUbEVyimv%2BS4azErc47gXsxCcDkH4d3I9QVxD2998GlksNupJhnLSOGmFZudeldOcC%2Bl0p56CX%2B1x5BERz4n50VzYrImcDbnotm6QKPwTE9%2FjvmL3sJHspL1WHP4CEExJPlbsuto2B0ZOMQxRqseRF9Ks3dpQ8gaKeZhji6jzrhNtv4L8PRKTCJz%2Flq9QJk2A42Tef3xwRMkVYFTk%2FDtOs2xjsGr0xdk73W%2FETMitasljMoryndY2YfswFN4PqQTgcsPtLB%2BNuS8esyNSCZ0X2l19tiUFodlNjgxA%2BYhZA8ecKej8GuZRtZvegYxmHEYSINGE8JZuGT9vKceYVBmrhyXJ4A30QTf%2B7SPgXyMKJsiEjljfLlCzPwwhc73yQY6pgE5nkMUIAxNzCfDfPePLJvnLpD8397qwt57jyxxiyB1LxLJUbxCreBcaES9tutJJIgjuHoalSzLnk6zisUGP9q5n0fn7xh86fFD4nxTOFqTGI8n4aFWdP1Nv0KG7KFb7yKZ%2FyNhlZ%2Fyx214ae%2FtG7yEMVa3upKa5ZzqvjnZZcrbZBmq5pJsh6cFwLzi3gLscWD161snkzJHKLEL%2FhAROlWPb0DW8VA6&X-Amz-Signature=44c15793b39e5b7aa900b64ddbd1208dea5e846b84abccc24ed8dee88abd8722&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
Now we want to pivot this DataFrame, so that it gives us an overview about which course exist in which region and on which level the course is offered in this region.
In other words, we want to produce this output:
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/7021005c-d1d2-4384-a661-26c1cf321e5d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V3CZDQPT%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T231724Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJGMEQCIE5p6ChEmzaiugf4eVGjbaDkMozjzpcZxHZxqQ6HzdvMAiBjA8um827XvC3yFI2wtEli2mgI1WKcqfKZaQmRXxjARCr%2FAwgnEAAaDDYzNzQyMzE4MzgwNSIM%2BNd%2BB6lXNd2%2FTm%2BtKtwD%2FeAkSkoVMmxCzx1BM2n7%2FkHomldIylgy%2Fa9584TXIGHuF0mnzuyUGkNjru1HeicH7LbnC%2Fc8H%2F9N32AvBFviPMD5BTSuRUk9T05izcIf%2F%2B5lzTrFGkw2R%2BP9rmRSakAfSOyuT0fpsooSn2tParEkuX4lUVRngb29MQ11QOJpXcTG3pMivxrQRfKCu%2BglYKYbPzMR7exQgkLgJbuSN7%2BSR%2BTsec1Uucrb88Sa0OpYs6ktWCUTOSFDzhhQTWeXpzPUA7QkrUbEVyimv%2BS4azErc47gXsxCcDkH4d3I9QVxD2998GlksNupJhnLSOGmFZudeldOcC%2Bl0p56CX%2B1x5BERz4n50VzYrImcDbnotm6QKPwTE9%2FjvmL3sJHspL1WHP4CEExJPlbsuto2B0ZOMQxRqseRF9Ks3dpQ8gaKeZhji6jzrhNtv4L8PRKTCJz%2Flq9QJk2A42Tef3xwRMkVYFTk%2FDtOs2xjsGr0xdk73W%2FETMitasljMoryndY2YfswFN4PqQTgcsPtLB%2BNuS8esyNSCZ0X2l19tiUFodlNjgxA%2BYhZA8ecKej8GuZRtZvegYxmHEYSINGE8JZuGT9vKceYVBmrhyXJ4A30QTf%2B7SPgXyMKJsiEjljfLlCzPwwhc73yQY6pgE5nkMUIAxNzCfDfPePLJvnLpD8397qwt57jyxxiyB1LxLJUbxCreBcaES9tutJJIgjuHoalSzLnk6zisUGP9q5n0fn7xh86fFD4nxTOFqTGI8n4aFWdP1Nv0KG7KFb7yKZ%2FyNhlZ%2Fyx214ae%2FtG7yEMVa3upKa5ZzqvjnZZcrbZBmq5pJsh6cFwLzi3gLscWD161snkzJHKLEL%2FhAROlWPb0DW8VA6&X-Amz-Signature=928a882a94cbcbbcc23da2f72792bd7707c4b3f226ca5c1d46e42eae9101cd50&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
If we look at the structure of the pivot table we see that we must specify three parameters: `index`, `columns` and `values`.
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/ce3fbd7a-7ed0-4aca-813b-7b876b8a9341/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V3CZDQPT%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T231724Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJGMEQCIE5p6ChEmzaiugf4eVGjbaDkMozjzpcZxHZxqQ6HzdvMAiBjA8um827XvC3yFI2wtEli2mgI1WKcqfKZaQmRXxjARCr%2FAwgnEAAaDDYzNzQyMzE4MzgwNSIM%2BNd%2BB6lXNd2%2FTm%2BtKtwD%2FeAkSkoVMmxCzx1BM2n7%2FkHomldIylgy%2Fa9584TXIGHuF0mnzuyUGkNjru1HeicH7LbnC%2Fc8H%2F9N32AvBFviPMD5BTSuRUk9T05izcIf%2F%2B5lzTrFGkw2R%2BP9rmRSakAfSOyuT0fpsooSn2tParEkuX4lUVRngb29MQ11QOJpXcTG3pMivxrQRfKCu%2BglYKYbPzMR7exQgkLgJbuSN7%2BSR%2BTsec1Uucrb88Sa0OpYs6ktWCUTOSFDzhhQTWeXpzPUA7QkrUbEVyimv%2BS4azErc47gXsxCcDkH4d3I9QVxD2998GlksNupJhnLSOGmFZudeldOcC%2Bl0p56CX%2B1x5BERz4n50VzYrImcDbnotm6QKPwTE9%2FjvmL3sJHspL1WHP4CEExJPlbsuto2B0ZOMQxRqseRF9Ks3dpQ8gaKeZhji6jzrhNtv4L8PRKTCJz%2Flq9QJk2A42Tef3xwRMkVYFTk%2FDtOs2xjsGr0xdk73W%2FETMitasljMoryndY2YfswFN4PqQTgcsPtLB%2BNuS8esyNSCZ0X2l19tiUFodlNjgxA%2BYhZA8ecKej8GuZRtZvegYxmHEYSINGE8JZuGT9vKceYVBmrhyXJ4A30QTf%2B7SPgXyMKJsiEjljfLlCzPwwhc73yQY6pgE5nkMUIAxNzCfDfPePLJvnLpD8397qwt57jyxxiyB1LxLJUbxCreBcaES9tutJJIgjuHoalSzLnk6zisUGP9q5n0fn7xh86fFD4nxTOFqTGI8n4aFWdP1Nv0KG7KFb7yKZ%2FyNhlZ%2Fyx214ae%2FtG7yEMVa3upKa5ZzqvjnZZcrbZBmq5pJsh6cFwLzi3gLscWD161snkzJHKLEL%2FhAROlWPb0DW8VA6&X-Amz-Signature=e95a244457c4d97d867e7a1d7d222be3e91c85865bf0ca7a092e14e69a7bbb07&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
Thus, we need to specify the parameters as follow:
- `index = region`
- `columns = course`
- `values = bachelor/master`
And the correct function call becomes:
`STUDIES.pivot(index='region', columns='course', values='bachelor/master')`
</details>
---
## Question 5
In Assignment 09, there was the pd.DataFrame **ORDERS** with the column products that encoded the items and their count as a JSON encoded string. 
As a first step, you fixed the error of the **json** module and overwrote the column products now with a dictionary in the correct format. 
Which of the following statement returns a pd.Series with the same index as df and the minimal number of distinct products as values for each purchase?
❌ `df['products'].apply(lambda r: max(r.keys())`
❌ `df['products'].apply(lambda r: r.values().min())`
❌ `df['products'].apply(lambda r: min(r.keys())`
❌ `df['products'].apply(lambda r: r.values()).min()`
❌ `df['products'].apply(lambda r: min(r)`
❌ None of the given choices will produce a *pd.Series*.
✅ None of the given choices will produce the wanted result, even though it produces a *pd.Series*.

<details>
<summary>Explanation</summary>

The **ORDERS** DataFrame looks like this:
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/d484d0cd-76dc-4a7e-bdcc-97483546438f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664BNWNQ3Y%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T231725Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJGMEQCIFYrrZXZlUToPMGqgpbr5AHq6RmPzz4RHrCDPa0P69ufAiBadQklobyxBKy79THoeyWJgQqRhY19S7KypT8MczUr7yr%2FAwgnEAAaDDYzNzQyMzE4MzgwNSIMWWtEhuPvJR4Sei1tKtwDT8aT%2BUuvzLKHd45hs3iCiA8K%2BCHlb3Oku0%2Fv2HSpNKkEK6cdvbL4JmOzZAFVfqGH2y%2BDFszxNSigtlIQ8CFpeyFgq7G9kOcGS32RfeerzKDkoZRiYn7CqAbyk3ZS4fAmhYbOAkrLjvVCv8xuKBftqtFjJHt409l7zyVqGkL1cVGOnSbJ1L8KEAMTVi2Z2cNQ6cGXO%2Bqe0L0JTMDQRsnRDgKAw7XjZBn7Yq0L4YHwRMMrR2%2Bwykgg%2B6OLRJd64PwoYdtsHwLoYpIX48zD0UAR8%2FjpNetJqFt3qLu503X%2BWNQ%2FJ8hlCESAX5SKA5FfY7gzGgCcfDUYzx29fcP4BdnQfxYnj1S9cYUB6Kd3W0pQ2S69qLN%2BgjWQUFw4ihU72IRxt37EbbwXcsw4IFjyjRvt7j1ULHNIEDgtALfRJk5jo8Q9FaSd6xRuKHNvWKTuOWyWkHEwNt9G8nk6BoXxI2ChKvqIvvf2kofL9lqmXCKEvZmljlb6xHbzRFV01khbEvBjlregD5hjl4J1x1GTFWEhpHW79B3fjy5%2BWKXjK1HjggDXEnuNMSSNi0p3iZNBiNpX%2FsiDKFUzyfAvj%2F49FwVxAYC960h6r12HQMPAl9R%2F6d5P3%2FZe%2FFKi%2FiOozswwvs73yQY6pgGgUewvo0aUZxII57vlwkEpORFR38UNKef%2BWXY4vutJRj2ecD9JTm1gwVekHGOvXF53xftsnZTnnNZDcz%2Fy7Qbu2Ana9WQL0anMox8F8M%2Bvv3EScwDRE9orPY7W0pChseZekAeA13CnzRVt55Fz7i2Rk6YnrWTT4L%2BS7DPXh78g0g70LdKS2mX65bNjDmgyonPzCPUCCxKImBGObPWWRNMYRIti6T0u&X-Amz-Signature=0d89ff3a8d50f58eef264cef7ffa83917f12fa6bc5bf32af067ad2111066732e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
We can see that in the column `products` there is a dictionary that contains all the products and the according quantity that were purchased.
Now we want to count how many different products were purchased in each purchase. 
Let’s look at the second value in `products` (index 1):
```python
products = {'chair': 2, 'apple': 1, 'car': 1, 'smartphone': 2, 'drill': 1, 'mask': 1}
```
We can see that in this purchase 6 products were bought and 8 items in total.
So if we want to know the minimal number of different products that were bought, we need to extract the the number of keys in the dictionary, what we can achieve with the `keys()` method:
```python
products.keys()

dict_keys(['chair', 'apple', 'car', 'smartphone', 'drill', 'mask'])
```
Now this gives us back a list containing all the keys. To count now the number of keys there are, we can simply use the len() method. 
```python
len(products.keys())

6
```
However, none of the answer options contains this code. Thus, no answer is correct.
</details>
---
## Question 6
You have the two *pd.DataFrame* objects **persons** and **addresses** with the following columns:
```python
print(addresses.columns)
>>> ["zip", "city", "street", "number"]

print(persons.columns)
>>> ["name", "address_id"]
```
The indices of both DataFrames are continuous non-duplicate integers starting from 0. The column **address_id** in **persons** is supposed to be *foreign key* for the **index** of the **addresses** DataFrame.
There are some persons that do not have an address, so the value of the **address_id** for these entries will be *np.nan/NaN/pd.NA*. 
Additionally, an entry in the addresses DataFrame could be referred to by none, one, or multiple persons.
Which of the following statements returns a *pd.DataFrame* with <u>all</u> columns of both DataFrames **persons** and **addresses** with the following restriction:
The resulting DataFrame must contain all entires form the DataFrames **addresses** and their referenced person, if one exists. If no person is referenced for an address, the corresponding values for this row should be set to np.nan/NaN/pd.NA.
If a person is not referenced by an address, the person should not be included in the result.
✅ `pd.merge(persons, addresses, how='right', left_on='address_id', right_index=True)`
❌ `pd.merge(persons, addresses, how='inner', left_index=True, right_index=True)`
❌ `pd.merge(persons, addresses, how='left', left_index=True, right_index=True)`
❌ `pd.merge(persons, addresses, how='right', left_index=True, right_on='address_id')`
❌ `pd.merge(persons, addresses, how='outer', left_index=True, right_index=True)`
❌ `pd.merge(persons, addresses, how='outer', left_on='address_id', right_index=True)`
❌ `pd.merge(persons, addresses, how='left', left_on='address_id', right_index=True)`
❌ `pd.merge(persons, addresses, how='inner', left_on='address_id', right_index=True)`

<details>
<summary>Explanation</summary>

Lets’s visualise the two data tables first and plug in some example data:
**Persons **(left data table)
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/7496c730-cb41-4f7f-af50-44c35591eec8/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZICAEUVP%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T231729Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIQDTi2C2DcAwsZXBhfkboIVTaOeMIsB1h7JoVNeKmVFDXwIgEDRmkA1irXPNv9lFHIi5IAWgBZ%2FB7aZhfA4t2U3MMrUq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDBakzGUiOQ0%2BcQwHVircA7Pu11LKkJ1%2Fr5QtPbzGoHMxgyiM2raR651CGPh8EHhjExWchMDbeSjSmpJp9UCAbSPRMRDnMSq5fV%2FsutcQGSrsWOF3YVS8d7KZvKxt%2BFUjwhTm1cFUoVknvWvFuHN3kYi7kI58wxCDlstSenTrOKqBRBBpxL9nOkMu1mbYqN7iMOO7yWh3vbo2ACNk6O%2Bzhwn6WhMxvHWgBz8gN0nt%2BMuC9hNWF7mgqSFamyNW4u5iW9KrzIOFftPFOpm5zUTzlPWb6ywaSyUJWryKaOqU%2FmKyZgEkHmSrJAllv7g2inMureWls8yQMVgMR23ATYHfGtQ8dQ2iWDZqPqcJbRb%2FqUKOg0Fm76%2FoQX9WXPlSlVFXeoGZgv2rBV%2BxeDT%2FfnccTjYtyaKqDaNyqvRBR%2BCV8J%2BnWM0K93aBawPetVUQKTpwVWh%2FuFvutK7UGQXJ%2B9Rxy7u0gSrMKX4brYhO3vLQ0VqSodf5JC1aD5fElZe5yYSya0MCVJVvaq2daS8eLkzE7raMoYUxs2QCNf%2BMLBleE304VsHgSgsLQih0Bg4im5YYccLq2Ui7oU%2B5%2B8%2B%2BpjTsHRqkwdqtaYoluKPBMZayL1ABvl8oUkn7FP8ZyrKm19kF3zupeZlMpxIJdcxiMPXO98kGOqUBspLoRPwB5ytut72ZhDixA%2FUmXiEyym57U%2FXN%2B%2BulnacIf65AuKG6I15nWF309953ZkOti6lae0JubQRjx9baUodBW4aXuMvgUP83Y2tf%2FOkK4T%2FfDgZ06klK2LX1QFSrzJYxy08l7Lc2pCp8YJdThXmbH7Rd1CKPqaA3OUfHlaeFzbU3WdnBPGt6LvAFtX896goZGV4y4hTVxjT%2FER58kpBfoywe&X-Amz-Signature=e262287ccde42742625eb62fa703225bdbcc49bd0c987a963146d80202c999fd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
**Addresses **(right data table)
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/096ac0e8-1fd5-4af6-bd55-5f2706b0e926/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VH7NEW3H%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T231729Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQDGicKx8XhfeA38AVbszJ0y4F7qjRZp3aBYkXl7Ya8MBwIhAMEu%2BF3EdAw1BqAvqipgD%2F8InWErTBrZWo4FSTxc19QJKv8DCCcQABoMNjM3NDIzMTgzODA1IgyTomaPEin%2FvF6fcCYq3ANGHZ0y2Nbh8R%2BuWEmpa1I3skmLqKJhSFKC%2FBDRm6UnIryYZPZLugHPaDo3UPS1Te79RByqmMvU8gLc57jje4r43Q7Yx2xIduDCqTZqM9CnWGj0x4zkV2GQNa3Kp7NL4Del5gj1x04gnEp%2FMbk9Ujaz2C7L4EysB6%2FwO%2B1o5GczwMQlYudV8v0%2BCyJQpb%2FnH5PqhjYmkVLX2669gZlIifFi%2F%2FNpG8sI8mr4irqQ0%2F%2FC0uoMX%2BTCNS8J7mZh1OHrobiwS2M2gIi2dKAcF28UFe1bgyEplZqZuB8aD5KT8AkVvPQlaBEsC9I1j686%2FWqm5X3T1XgvYY0VcHeWcanSfM6TuJ0FmO7lTzfLXIF%2Fi%2FdRgF5JfBCwxW2TGJyuJ4sp0yJQxnWKcegntlmWcOxgZ%2BpR%2BVWfpkFEO6jwO6ev8Ik2HIxEt9GJ%2BziChgSrMR1q97zA6BtYyMiTZX%2B720vy4MahPciG%2FQpwnTBbXUlmPvaP60xD8s0G2lhUAUbSNBVByPRJMKsEDNHfS3meP9QmHPUlkUWmSc3L5FqSPjl6%2B5lTb2Th9fXuv98A52P9t7y22HMyyqo835pK8dkPBBbFVMMs42YIA1O0EqVOLlw3Cscx4MWs%2FHRCWqivJNy%2BSTD7zffJBjqkAV%2FDpunCy6EDB5iqvzFs4zJCNwbTYAU3kSBCil3WKpSFVjgC6ZSIRMcHWGFVBQhoOtScZw%2FBz0PBkww6WtGzIxP4YGQn8vWav3RDe7zz9IbQqKbIPrvGZPzMz32%2BMnrEyXzD2nM4cyDNpLib%2FxuuHzV4AhrBarHx8uIXhkY%2BbD8pVkS6oLvx5fp1VCo9Mcbrfj37QtcNrpVDGdnvETUcN%2FGgCWeP&X-Amz-Signature=cff4cc87140c62e6f9d6b8c92f534cd6448865abaa7bc6750312654ac4d34f87&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

By following the foreign key `address_id` in the **Persons** table, we see that Marco and Melanie both live in the same building.
We also see that Friedrich doesn’t have an address and that the third entry in the **Addresses** table is not used by any person.
Now we want to merge the two DataFrames together, without losing data from the right data table, **Addresses**. This means that the output table should contain all three addresses but only the persons who are assigned to an address: Marco, Anna, Melanie. Friedrich should not be included. 
We must define the following parameters to perform this merge:
| Parameter | Value | Explanation |
| --- | --- | --- |
| `how` | `right` | We want to keep all records from the right table, regardless if an address is used by a person or not. From the left table, we want to include only matching values, i.e., persons that are assigned to an address. |
| `left_on` | `addresses_id` | This column contains the matching value in the left data table. I.e., here we tell Python which person belongs to which address. |
| `right_index` | `True` | The values in `address_id` can be found in the index column in the **Addresses** table. So whenever there is a matching value between `address_id` and the index column in **Addresses**, Python should include the person in the result. |
This corresponds to the first statement in the answer options.
If you are still unsure, check the output per statement below to understand in detail what is happening.
<details>
<summary>✅ `pd.merge(persons, addresses, how='right', left_on='address_id', right_index=True)`</summary>

![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/91295b4a-a196-48b3-a33e-68bbace9fc32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QO4UACHS%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T231735Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIBdoKkpqpdwxc%2BIzF5yNLg%2F2pw2wXIqSyogX9o20L1f4AiEArWJFiovqXPgaWmX5uC5V3oWSQL%2Fw%2B8s71I8msPvavggq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDP5IZY92AN3eGYAlRyrcA9mffsV6NARiUFfKqwBEMhUEAXucXw%2BKWywTLhcyw%2FAkLeCWwJQbDyqE6EUimQk%2B7ycOecrySAUGA6FnzBogjChcBA8jHKQvtCM%2FjtfzG3KIhExIRKeb3FOBwD%2FX7575izOGqFF93IL%2F3rouK17outJaCcBLNFlzVqd1WHBhQ8okxDdiv4gq6scApVeoM9R%2B8m%2FbVCGjQ7A%2FzuADym%2FrVXJfwv3tS%2BKUruk1tMR%2BwkYpUwmVFnECR9wx5Ax6zr3fn1Y8RMga72B7yQsnM5rZb5NB1O3flADlsVz50sjljXA1pp9%2BZAe%2B1gnkCIGetAPJ6S6SQ55vV%2FVQTeX0m0qOI3989pEuCB%2B6oem%2BnUqgbRhHgcBtwBTuFb7XJJtZdYKVta6PV0tvbcy7iQvi3%2FWLB5V0bj%2FsWzDm7Z7bY3tJWiNpNJ31co9%2Fiwx5GXFWuJkMPyvZky2lofDnOxZNcTFdVCzr1xQzGX69cXiSM6fydDw1FMMM6dsIwJ4iWIITYfqE0Qn5Q7GGbb2FGAlaV9bPvXnuqZxUPca8Tdpio4SNqLIef9v3h%2FThN1PavLbMZwyDGJGVJqRd530l8bRMq6857HP1PievGOOlRulZyPgKrsZhRSDkNtEpxcNvw%2BHHMNPO98kGOqUBgXwJKRiB7FhhpA6NTqgQIQ28B1kahoRWBbu0NH1yzlRKN28WnNcPUy8xmdZskPRKn6yiC7dfw3qqm9fypWBqeYYGxfLqiLCxbTY0buezRopUbkOcCJ5zS1P3BlJ0R8kmLLUDhNWdEwQD8veJrPBnAz9tjvXtHp0p3h%2Bm3ZfHufU%2Bx1Aa0uRoHl5yEJzv3%2FPzfJjULVivsty%2BeGjrB%2Bflr0m%2BZ%2BY6&X-Amz-Signature=4c915a18f5bab61d56105c606c641fc95c4e00dd6178b19778b7b15e9522245b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
→ all addresses are included, regardless if they are assigned to a person or not
→ only persons that are assigned to an address are included
→ where values are missing, NaN is inserted
</details>
<details>
<summary>❌ `pd.merge(persons, addresses, how='inner', left_index=True, right_index=True)`</summary>

![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/ead1aaf6-c414-42fa-bb00-b88bb8c18882/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZJLTELLG%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T231735Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQCRTUjwvGBR2o3lJcegMxpfmYRCSAVALV0F57Dm0R9YbAIhAOkjEd1Jqr1cbAruaMJnOCu%2FTvOKtPoQ3abeUOgSh4dfKv8DCCcQABoMNjM3NDIzMTgzODA1IgzT0lfq3n6X1mC4NjIq3AN4SC3xhDbHeiZWd1jO1jcY3xD7NMRaHl231%2Bo2acXY77rohh4NlpY1LH9S8wZysID3Z5i3tx0BjfVSLX1HEK1DKe6s7vqvPW5ved8dRcwuluMFqiwTISQjmU3pwsgdha93LG1IwLbq884pE1QPSn7%2B5fiR4gDLD2OWcCCpHd%2FV9kozk4rLR61qJPu2G8LcIi83zHGlffj3nTN%2F8VubUSI779MFDmBz%2FMg4boFDHeaWoYhwASCSzumNLRiCcTyWHBKdaQmf%2BgsUjX6b4MLGTtqUuNtKAImMUBsK0A71LArPtY%2F06IxT2DtorsGPbYJm2jBcRQIb1%2Bl9yHI7EjIZX%2B2SvierQRLLuisUSKSwIaI76F1LGETX14vg2sIdTw2WkiwuZJN9C0m8Tnk7ameMT%2F0%2FsKDNiSlAniD%2FII327cRKVYX433o0Aebb4KC%2BgAj6K1c8KX7LtF5%2BK5732XiFUrnp55l%2BAehtYCrV6ocsdZdEHOdarIwvLpZjRzbcApsIH7K%2BAuab%2F9Nc3ZAuei%2FCKencyW%2Bip%2BpD%2F7Q1kFMSfBXIjJrW4OvmeAfpZaalW1xIiIdwAz%2FzZLB0u6rKhD2ge5H2DtKS2G3%2F45CjwlLArIK1FiMrO%2BCr%2Fi3SYMdNBzDHzvfJBjqkAefyHfsAb80CRIAh7lhUMYO0iSvyeymOxMQNfSvi9HQHxxQ8BqdhzYXVUviooD%2FrMgvRdcYXa76z0UAVzk9qasvZG24q7opyixwfAbk5TdAn0HQR1sL5xjpHsQnDpTk3s2tOjGyq5gUy330fYc9FY3VRGFeErTOI4Qsht0y%2FFgoFsGsro8TeDhohOZ%2BLVJdZvgKoQbDPq6zOxz6L1YjtOGEysAPY&X-Amz-Signature=8885d53640b57736b11433b858818cccfe8f74bc5ec040b702621cfbf5574151&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
→ only addresses that are assigned to at least one person are included
→ only persons that are assigned to an address are included
→ However, matching is done in the wrong way, over the index column in both DataFrames. Thus, Melanie is assigned with the wrong address (Bern instead of St. Gallen)
</details>
<details>
<summary>❌ `pd.merge(persons, addresses, how='left', left_index=True, right_index=True)`</summary>

![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/87be0349-c455-4f07-ad7c-9be7413cb92f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664BCVGMTK%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T231736Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIQDVa9TZ3%2BFeRcvJ5IsJ%2B7uN8%2FG4xMBx%2FNEEYRF3ClY8hwIgNx4mwljyUmNIxiIyJy6KX6XC7qIzdhKNuDjYnOs4BXsq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDNVT7lUX8kZb%2FKMSqSrcA6%2BEEartnxAYesUUiFT8Bvy5pgji%2F4GX9BUyGTCgZO6IBGeEy0KUHMD6JXBlsBEEvxvBPdJNC4YLNBITTMGYY%2BkCe%2BRUqvjmz%2FZFTg8WLY3Dqxuvru6f0F6Tp3aGj4nGQ7bY6oi3BNXJD%2BPds9GI2fCtXzIpLFNhmr60tELtjQYdn1E5TQqjxfpQY8vlRFZfCEMi04hDGG2i7FRw4%2B28NEP%2BfklFqmzqq8y5Gof6nj37x%2B4YNW50yc%2Bi89cnB4pU1KP%2FSlETAdIL1%2F71Qvef6W7akDU8Xf3iJtCsvXC9PZl%2B6hOKLTBzYtq36%2BlZSottDyiKRdDguBCEAcrgwqqBqChsQJ47WtVlFgPTL%2BzmyFZRukooZ3LISUINptpbEDum0YdyyATpnBq1UY3vrGuhyiYlN5iP42jjPANXgyQJVZczZvRiUJpKgOYpsbIWDjdRop89FKIHpDKEDqnmKm8mAXLwLN5c4a%2FsJO4bwhceLAMeaIxoT%2BzoKRmcZMJ1O5gFw9mrl5sIuEKlQmqW7r8Qn53vee670H1eyEzj8QbjI%2B3EsI0YQKk2WmMrQDD%2B0PLOXz2r%2FaGbHoa1UfMe4FBP%2FAjXfaI1IQKBUtktxgU%2FGJ5h93m4cJweZBi3eAEIMObN98kGOqUBkwO14hgsLLisjGNkQrhcAPHxncaoy7EUS4Cn9mzYf9ELSECo1ItghsNFARxRGXmaaE9RcqzqO0FcuSkdWCHY6ibdKTN2KO9vZyErlBY%2BYm5fCigE7JKivF6m%2FDTUHkYmgTIEuaXZuQKPcja9yYACMCZKeJMv9YipdUPiltixWCU%2Fknn6R9OBszNTUllahgw%2BaCKMNBa%2BVBnYkMa3g8J8g%2BCq5JV6&X-Amz-Signature=6eb5bb9f99da1d7658376fa28b8fa0deeb7180ec39502cdb71ba6d1ae3e471dc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
→ only addresses that are assigned to at least one person are included
→ all persons are included, regardless if they are assigned to an address or not
→ where values are missing, NaN is inserted
→ However, matching is done in the wrong way, over the index column in both DataFrames. Thus, Melanie is assigned with the wrong address (Bern instead of St. Gallen)
</details>
<details>
<summary>❌ `pd.merge(persons, addresses, how='right', left_index=True, right_on='address_id')`</summary>

**KeyError: **'address_id'
→ There is no column `address_id` in the **addresses** table
</details>
<details>
<summary>❌ `pd.merge(persons, addresses, how='outer', left_index=True, right_index=True)`</summary>

![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/9f0a6977-7c62-42fc-bc16-72859d19254a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664I7QZFKT%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T231738Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIQDA%2BTH%2FbQb0Hq1AWaj9UT0IgGtXxGt6YljybzHKhCa4JAIgHuQ6S5Ff1itEo45EhBwQ4uL6VyJDMCwEi0UUH9fHK8Uq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDKuNxMiubijIzS%2FkvyrcAz5cPMuEDJTE97Wo662g6PnkMVr5p1I47qPOarmYYF%2FGNPWjZtOtdd2eaMcRjXYJTgEfdC0%2FmxV1nC51ea8isfcrQf%2BLGJ8pE2WjI7QrIcqAS%2FI%2BgWhIdG0ZTIfr0XBLWuG7J3pBTkFwT4WN9av6uwEENUhGYz94eWH5SlORD6xZDrEHeQYvKAmr3HlTSdwbDlsUG6oUomYMMgGqp0kxTYxwxfXm26S7H8lPnlJOnwu2Ix4fVaAOmz10IHZ7E6nY9QYq4%2Fn5JkjOKjllGdgzS6FXwTdRWVm58Tx%2BcoK14fvoHsshx0PU%2BqHA2n85j4fbKnw3%2FHIrQVmudAyH8MfEo7TqQQywAhDU9duPbd7jGve0jIpzLhxhsp93p57EjlyVZesMKSAtUIoPYNXSQ10Ceo4BGjcutkqqNF4kCL5lYm5nsQ3KpCz6YiyuMXcJ5Bynseen9o4k43iCuvtNKQ7h5o0CeAj7G8N9jlOsf%2F%2FXzd4dsuIxFXd6WnS9MKSqUavV1BMVzPo8c05BlXQMe7ryMkiPQYlgi0ARBGuXi8mH5yTyNtqwU0ee2eS%2BoWrOJ3UlDPLiIt7dS8HpZvPNp7RdoAMEd3IF5l%2BnWnuiWyEBJeTVY7DAUh4KUegvE5kCMPjN98kGOqUBKKndQk%2BHeBcAAy%2FlkB1N%2BVR94qu%2FojWwfNeX28biMfCV9plbgu7XMAlJPHCX7scnyQW6C7GbmoaF6o%2BiF7gG2xiIunQ1RpqFLWTb6F9fN3ji2N%2Fn7A0mz%2BBqMK97ky%2Fsy57aQHptWS5iTrTOyJ7YiC97l3Ciw0yWjc3OFTR1BcbGXumvKIopD7kSYQE20LylIuSjbVTREXVfnyS%2Fs8kQ0MCryvV6&X-Amz-Signature=db162b51573ceec6f56ecc6b9bb2b25610d95cdcb8396b1a0ba328dece80cb1f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
→ all addresses are included, regardless if they are assigned to a person or not
→ all persons are included, regardless if they are assigned to an address or not
→ where values are missing, NaN is inserted
→ However, matching is done in the wrong way, over the index column in both DataFrames. Thus, Melanie is assigned with the wrong address (Bern instead of St. Gallen)
</details>
<details>
<summary>❌ `pd.merge(persons, addresses, how='outer', left_on='address_id', right_index=True)`</summary>

![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/bd8f2a5a-01bb-48bf-9f2b-40d2d8b90f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664G2SXPBS%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T231738Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIEF%2BV5fgQsx1HdCcotH067SPU25qSI7hu5%2Bsidko%2BWW3AiEA%2Bo9Hn4nz0MKvV0m7TENMXxdyg9hg7V6G9XXhClPqG%2BIq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDBEmpOmS8onl9l2KoircAxgRrrA9Kpif83iunk%2B6mztI15gKMNGth2txWjYxxS6a5AQuuFcOgVQaQEJ2NkEEb%2BnkXF3f0tyOW0mP2UubVxOrRzrx5S1lqSV6CdWWp09VoQA3qNDHzZREBJ10OvSfx8qdOi%2BuXqe6zockDR2RGKfO9rOGiWz%2FfmO4omXT%2Bk42%2FY2zULCMsnZRPt0c8rU11p%2Fk8oa2zoyrjUi6f76srW1RXNod5gm%2F%2FUSUMRD6dJN1vKlKcvHnyFMSYUYyjlpzSL1Z6Lw3uTC7ezVU3rXke41IDzj%2FqFRFQISYDWSJBjZg0h2Xi9rGoni5TapJ3Xaap625bhAHmbI7yfDefFuc3Kl8vMFlL4a2VrCq8ZZc9b6gYVrEDTyAGt9e2INhMoWaJVvEdZTkOSMPL4BWh2n48gC1yYBU166yR6g80s1PXQHPADMtF9qfStxgv0aBXcSm%2BW1gndor5rXh1TbWa2RazWleXLdWjUUPdoTouek2yDwNuRUehSSPzQvpB94L9ouD41atoFM7jDmYu83q5uSay9BQ%2B%2BB%2BDvf0GETO9N8dLofzFUkBaWTfMkAUrabIR6oKZB8Ku2NCtPI84YXBIQkQKgX%2FVa3WftDycfZeMEQAGez69p5i8%2FcrbpwK7wvTMLDO98kGOqUBD2Niaz4eSs93DFFmxh5DJPq7lGCnfCXVnFzu4C0v%2FIblJGmSL3wj7eKD7aVnmgWOEvReDL%2FtSdXCjPBS9dbulmYjy0NmiPsjI%2BSdnICtVnl77%2F2Vnzcl2xJzsRdsJsJYjqSWouuYIaTxUljOpYKm%2F%2FrF0GdOl7lIXtKmw9eTMCpaT08%2BJwBnxluqNjVSzbzXgehgXTTHLkrD2ykGXtmnR0iY5bqC&X-Amz-Signature=30e7d2509f68783308aca36d29274369d736e68908469a5ab85401035fc88486&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
→ all addresses are included, regardless if they are assigned to a person or not
→ all persons are included, regardless if they are assigned to an address or not
→ where values are missing, NaN is inserted
</details>
<details>
<summary>❌ `pd.merge(persons, addresses, how='left', left_on='address_id', right_index=True)`</summary>

![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/79add2f1-05d4-4b12-bf06-902e4b32c1d5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VVAC7MGC%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T231740Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQDX%2Bw1X4g4nmROSQSXwGlpbCmbNLgnxcIlXR2ugN%2FqgFgIhAMhhImePsaiqw%2F%2FAchPPWvQLgWcE%2FhgFVs3o8DomMfhHKv8DCCcQABoMNjM3NDIzMTgzODA1Igygt%2BEiSEBRqqafFrkq3AN%2FeMr74gJgfGVW%2B%2B2BCwtGrHeDUM%2B9uezV0BFz0SuhDpJDGzEYZ2eBrSU7XyA6paRTRVNRkv3YE7kF5sZcAkCqU0O%2Bq%2FhZnpTip7geLItqEfnvNRx9iWSVOQWVZ4EoEaVIeTYFYJ4hJx1Gct8%2FxRcsv%2FE5g9IsNJlpiyI%2F8LFo2aRSNW8I5XpJRmvDUI6xPptquR155xrs%2BFFBT3ojv2ek0MzOstrpPeGP6CRKXF6IT1YyDV4Jk6W0nV3cvGDAQ5vC2bQ1bAiMkYhIS9Y7zInet9SXFD2rNXW26N72qsPdkyWIu%2BBIswix7H8M%2Fu2T8lC5gxayQ0B2GIyAoN2lO5fNOAZGQZHKFHmo3GhcHzx1M7nSECQ9OXcFn5gRlj3Sa%2FZuFSt4pUSfH1b1BftW2%2FlGQ0G6menyH1ds6GXrh1pAse%2FmXLNLcsp4YgUaGuxb5HcxpWc9YYUg%2FOUVUdQ8lSNoVzMbi8mWvDmpZvSUJ%2F0G45SOnor50b4DU9HuLB%2ByAiU8GpPnhMmARc01qNo%2FKlbiHTLqz%2Ff3gV1y2krxIgeY1r5GR0gsfVJTT9R2ivi3n5vl5ATaFcvZO4Lco3Mw332tn8A%2Bc0dBlm0BBwTi2yjEHesob5SKOFFOhfGCazCqzvfJBjqkAc2VGXkuRkXIGvtwHq876uhRa8CSVV%2B7rUl%2FSCdTXZJP9OTEwGQW4Ec2EGdj9%2B0zZbU1uLcXxhLu5ofxl1UdrN4k6JErYgj8Wuv%2FKs7j4n6x5vAqQzb1oR7UpwD1NmCArUTxhwJIDaVfAMfHTzxzJ0PxubfJIfWwjCubUQBTSWbk8dwpguetNqrz8RfdKooWAcFuRsNzOCFYsgx4Kx5jLYutSS8V&X-Amz-Signature=8e98b164a1b660367a8d08da4b86fffd9367e5669806495457deaf3e8a507391&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
→ only addresses that are assigned to at least one person are included
→ all persons are included, regardless if they are assigned to an address or not
→ where values are missing, NaN is inserted
</details>
<details>
<summary>❌ `pd.merge(persons, addresses, how='inner', left_on='address_id', right_index=True)`</summary>

![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/d82929e6-299f-486f-824a-b346718e0dbe/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W4YTJ7CY%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T231740Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIQDy4S8owP%2BlAxLLvXZf77RkSSo8F3EqoAhLnfX4C3J8qQIgOS0KysQndIfuLjJ3oIFP9jTTzj6vP9L9dArIyU4fSlYq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDHdDSEfd0Pk%2BDNON%2BCrcA3UdUIKk6upl5n0gWldq76XOXPlvLcBJzYr8Aa1W7kz7yuwQDh8fNplT6DX7orxbqX0tcJuxWN9bMX3gqctp82TNCKj7ZCQ1TiwshkpQG2ZNvVSi6PpDNbPWhL%2Fe8qp2FqKBalkmTk5FylWtE61raekHZqhGy7dxzNYEVJ7E6h2eH0SFAKZrTxP2eGAnPIKW%2BGj%2BKDuF%2BqkG%2Bw9iWvd15b0w2U7s2TXalGdIIs6ZrJuDztVVT%2BGxfgZmeU%2Bhd%2FyJ2PQLjdCekjMZMTznKk4l11FbiKSI%2FSuHRE82OLArRBy97vo73Nb2wPZk%2FCruaR%2FYmOSdoZjoAwUB3kkGa6inhiAZ4x0k3Ds8TTTkDopcNsUjEi%2Byxw5mdAMsFR6g6BpRggDBbGt88vai0vyGBvg9ywgvCJdoQtphfsiXmMd0W04cju5V%2BEigaKV728D6vIy%2B5OlFJi1eP8%2FRnQj5gmx7VX9uktTJsQ8JPmzXKMFF3p0k3mQmcerS7WNteKRcC1WQW95eSkVL2pjboBorsx%2BIMYIk9d%2BBfyqrEhwKXb%2B5oR0dmEFJv%2FG%2BNJZOD7hJznQDQhdL%2FH6YM6%2FvGKj8LPCKR%2FIaZ814bUeGdIDdoEdE5BVvzmrEM5Ef3GqlIcK7MP3N98kGOqUBE3tV%2B9W%2BIMdHZ%2BUOWh3IG20uW2oEvT14o5T5SQqQoXAPqI9Tl77GKEj9b%2Bcl%2BYc2bBiEtfgd070WG9mfqqXpxd%2FwHkfB8jq4ebTfGcOhszleuoTEjr4JARSnSGEAJO89fsB5F6fOpmABS6eWLvHPHIQ7vtD5YtPfQVM8bbmzhBtYKci8Ts%2BP0amL%2B%2BLU%2FiZhL1KK%2BwBngOXJehfSHBAZpTRtuaYD&X-Amz-Signature=ab2a35b59590cadc0c3164c4117864f34183facf89807dc99e74fefb92ef65b4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
→ only addresses that are assigned to at least one person are included
→ only persons that are assigned to an address are included
</details>
</details>
---

