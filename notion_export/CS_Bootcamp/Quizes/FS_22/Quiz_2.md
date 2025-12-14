---
title: "Quiz 2"
notion_id: "03dd5b63-5501-4fb8-b0b3-9d6272413053"
notion_url: "https://www.notion.so/Quiz-2-03dd5b6355014fb8b0b39d6272413053"
exported_at: "2025-12-14T00:52:58.296788+00:00"
---

# Quiz 2

![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/30a33f70-95ef-42bb-9e4b-98cbdd627ade/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ROTP5DW6%2F20251214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251214T005256Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQCw1%2FWF9Ls%2BcDzD1uYD%2Bg3AGSGFKyZR20VSLUMPB2ErDwIhALVF95foh6mTLNn0poZz2oP8yZlLkgvXSoj3O1mEgMzaKv8DCCcQABoMNjM3NDIzMTgzODA1IgzlzpGvb9z7LiKYIUsq3AM4l8MzgIoodhLdOvVPiU8cLTx9ZpxIddFy5trmYPXrtgmEm6WegRKvRtXZ2Q99HJhSUhQUkBWzxjAg7dWiuP5FAPjWf94N3%2FObXJhzbbOqM5rfNfZJno%2Bczr1nMU6SFeJP1yIb9ltdSWJGKGF%2F85CkjXs23qdryeIR7WT8NT7BUBO9IPIlwXXg3EmVytwXV%2B6NHkkw7qCavXxlWj1aww4jvsgK79gRRwL%2FXLoX%2FzMeV61GEgy0Ese9KlxELIkn7Iok7ElpZtuylVgCmSMJaIcCUa%2FYMnlBnS2%2B3ETqT7aTmHf4s1J2jvmtizAWM0MPhS%2FKk4SNLMzXjzG%2BZZYoB3uiobcNQB6MIQ4qvm1Hj%2BqrqB6YySCNqPpYriVprKwGw49fZqLOoDjvHZ8k%2FmDIw%2BWuLPAR8ajvrd0%2FVCno1aOiL92Rvc5chIymcj9RUGtu8WfHM1vda%2BNacxy8RKrfwSyXb2%2FOsvvEN%2BUPG2N8S%2FIvwcVAv9%2B1pngeX%2FRu%2FQYAj5HyFWY%2BzG0d5FzaxUv18cr1X2TzR6mLwQZkySeGQbvPOOqVLGsxWO1QsB9vHR3ajzAyFhkK%2FDdiHjwiDrUKyphIDPxg%2FoOUKJ2qinjCyOUGHZKFTc0YhVwgaTwZjTDCzvfJBjqkAeHimio%2FbFj%2B6mN8qSjI5l2rvhdDbj65ZMdZVHBiWdSplLyatLolbq4O1R%2FXO4Krvq0mrKLXZ8Ns3gtSdb%2FRZJ%2BeNc8AabAX7WZXMg0Gf7fBCKylk7GkOUMBtNM3L%2F3R1F5DcikU%2FZLkrrvZoSqWHgg9VaCvbLcCYDS4jlMCUZnp0037nbkCjzGNt9VcjC63cti7QcbBRq48PddwP2utvdX5puiJ&X-Amz-Signature=1ed8b1f1feb02e55ef18244967a07bace4f5dc2c573deba8a7b2e535d1b2eed8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 5 is the first number to be included
- 14 the first number to be excluded
- 1 is the step size —> we don’t over-jump any number
```python
liste = list(range(5,14,1))
print(liste)
[5, 6, 7, 8, 9, 10, 11, 12, 13]
len(liste) 
9
```
—> The range object consists of 9 elements, thus the loop is executed 9 times

---

![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/61933466-9f7e-4300-9ddf-bb11bcfc9bbd/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ROTP5DW6%2F20251214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251214T005256Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQCw1%2FWF9Ls%2BcDzD1uYD%2Bg3AGSGFKyZR20VSLUMPB2ErDwIhALVF95foh6mTLNn0poZz2oP8yZlLkgvXSoj3O1mEgMzaKv8DCCcQABoMNjM3NDIzMTgzODA1IgzlzpGvb9z7LiKYIUsq3AM4l8MzgIoodhLdOvVPiU8cLTx9ZpxIddFy5trmYPXrtgmEm6WegRKvRtXZ2Q99HJhSUhQUkBWzxjAg7dWiuP5FAPjWf94N3%2FObXJhzbbOqM5rfNfZJno%2Bczr1nMU6SFeJP1yIb9ltdSWJGKGF%2F85CkjXs23qdryeIR7WT8NT7BUBO9IPIlwXXg3EmVytwXV%2B6NHkkw7qCavXxlWj1aww4jvsgK79gRRwL%2FXLoX%2FzMeV61GEgy0Ese9KlxELIkn7Iok7ElpZtuylVgCmSMJaIcCUa%2FYMnlBnS2%2B3ETqT7aTmHf4s1J2jvmtizAWM0MPhS%2FKk4SNLMzXjzG%2BZZYoB3uiobcNQB6MIQ4qvm1Hj%2BqrqB6YySCNqPpYriVprKwGw49fZqLOoDjvHZ8k%2FmDIw%2BWuLPAR8ajvrd0%2FVCno1aOiL92Rvc5chIymcj9RUGtu8WfHM1vda%2BNacxy8RKrfwSyXb2%2FOsvvEN%2BUPG2N8S%2FIvwcVAv9%2B1pngeX%2FRu%2FQYAj5HyFWY%2BzG0d5FzaxUv18cr1X2TzR6mLwQZkySeGQbvPOOqVLGsxWO1QsB9vHR3ajzAyFhkK%2FDdiHjwiDrUKyphIDPxg%2FoOUKJ2qinjCyOUGHZKFTc0YhVwgaTwZjTDCzvfJBjqkAeHimio%2FbFj%2B6mN8qSjI5l2rvhdDbj65ZMdZVHBiWdSplLyatLolbq4O1R%2FXO4Krvq0mrKLXZ8Ns3gtSdb%2FRZJ%2BeNc8AabAX7WZXMg0Gf7fBCKylk7GkOUMBtNM3L%2F3R1F5DcikU%2FZLkrrvZoSqWHgg9VaCvbLcCYDS4jlMCUZnp0037nbkCjzGNt9VcjC63cti7QcbBRq48PddwP2utvdX5puiJ&X-Amz-Signature=0918cba92c5e9f46086be0f512858a5c6ceb9cc54eec92522590616bd42be3a1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
Of course, we can have nested while loops.

---

![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/28281cbd-69cf-4e6c-8635-690cfa17f68f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ROTP5DW6%2F20251214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251214T005256Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQCw1%2FWF9Ls%2BcDzD1uYD%2Bg3AGSGFKyZR20VSLUMPB2ErDwIhALVF95foh6mTLNn0poZz2oP8yZlLkgvXSoj3O1mEgMzaKv8DCCcQABoMNjM3NDIzMTgzODA1IgzlzpGvb9z7LiKYIUsq3AM4l8MzgIoodhLdOvVPiU8cLTx9ZpxIddFy5trmYPXrtgmEm6WegRKvRtXZ2Q99HJhSUhQUkBWzxjAg7dWiuP5FAPjWf94N3%2FObXJhzbbOqM5rfNfZJno%2Bczr1nMU6SFeJP1yIb9ltdSWJGKGF%2F85CkjXs23qdryeIR7WT8NT7BUBO9IPIlwXXg3EmVytwXV%2B6NHkkw7qCavXxlWj1aww4jvsgK79gRRwL%2FXLoX%2FzMeV61GEgy0Ese9KlxELIkn7Iok7ElpZtuylVgCmSMJaIcCUa%2FYMnlBnS2%2B3ETqT7aTmHf4s1J2jvmtizAWM0MPhS%2FKk4SNLMzXjzG%2BZZYoB3uiobcNQB6MIQ4qvm1Hj%2BqrqB6YySCNqPpYriVprKwGw49fZqLOoDjvHZ8k%2FmDIw%2BWuLPAR8ajvrd0%2FVCno1aOiL92Rvc5chIymcj9RUGtu8WfHM1vda%2BNacxy8RKrfwSyXb2%2FOsvvEN%2BUPG2N8S%2FIvwcVAv9%2B1pngeX%2FRu%2FQYAj5HyFWY%2BzG0d5FzaxUv18cr1X2TzR6mLwQZkySeGQbvPOOqVLGsxWO1QsB9vHR3ajzAyFhkK%2FDdiHjwiDrUKyphIDPxg%2FoOUKJ2qinjCyOUGHZKFTc0YhVwgaTwZjTDCzvfJBjqkAeHimio%2FbFj%2B6mN8qSjI5l2rvhdDbj65ZMdZVHBiWdSplLyatLolbq4O1R%2FXO4Krvq0mrKLXZ8Ns3gtSdb%2FRZJ%2BeNc8AabAX7WZXMg0Gf7fBCKylk7GkOUMBtNM3L%2F3R1F5DcikU%2FZLkrrvZoSqWHgg9VaCvbLcCYDS4jlMCUZnp0037nbkCjzGNt9VcjC63cti7QcbBRq48PddwP2utvdX5puiJ&X-Amz-Signature=f59879a0e5c5d60c1e9d1d89780076bc2474db69d706b31e72d05b189cb921cf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
How does our range object look like? `[0, 1, 2, 3, 4, 5, … , 999]`
- First execution of for-loop
- `value = 0`
- `0 % 2` —> `0` —> `0 == 0` —> True —> line 5 is executed
- `‘0’` is added to `values` 
- Second execution of for-loop
- `value = 1`
- `1 % 2` —> `1 `—>  `1 == 0` —> False —> line 5 is not executed
- Third execution of for-loop:
- `value = 2`
- `2 % 2` —> `0` —> `0 == 0` —> True —> line 5 is executed
- `‘2’` is added to `values` 
etc.
In the end, all even numbers are stored in `values`. Since 998 is the last even number in the range object, this is also the last element in the string `values`.

---

![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/540d28f3-1f81-494e-90b7-10e6557ae11b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ROTP5DW6%2F20251214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251214T005256Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQCw1%2FWF9Ls%2BcDzD1uYD%2Bg3AGSGFKyZR20VSLUMPB2ErDwIhALVF95foh6mTLNn0poZz2oP8yZlLkgvXSoj3O1mEgMzaKv8DCCcQABoMNjM3NDIzMTgzODA1IgzlzpGvb9z7LiKYIUsq3AM4l8MzgIoodhLdOvVPiU8cLTx9ZpxIddFy5trmYPXrtgmEm6WegRKvRtXZ2Q99HJhSUhQUkBWzxjAg7dWiuP5FAPjWf94N3%2FObXJhzbbOqM5rfNfZJno%2Bczr1nMU6SFeJP1yIb9ltdSWJGKGF%2F85CkjXs23qdryeIR7WT8NT7BUBO9IPIlwXXg3EmVytwXV%2B6NHkkw7qCavXxlWj1aww4jvsgK79gRRwL%2FXLoX%2FzMeV61GEgy0Ese9KlxELIkn7Iok7ElpZtuylVgCmSMJaIcCUa%2FYMnlBnS2%2B3ETqT7aTmHf4s1J2jvmtizAWM0MPhS%2FKk4SNLMzXjzG%2BZZYoB3uiobcNQB6MIQ4qvm1Hj%2BqrqB6YySCNqPpYriVprKwGw49fZqLOoDjvHZ8k%2FmDIw%2BWuLPAR8ajvrd0%2FVCno1aOiL92Rvc5chIymcj9RUGtu8WfHM1vda%2BNacxy8RKrfwSyXb2%2FOsvvEN%2BUPG2N8S%2FIvwcVAv9%2B1pngeX%2FRu%2FQYAj5HyFWY%2BzG0d5FzaxUv18cr1X2TzR6mLwQZkySeGQbvPOOqVLGsxWO1QsB9vHR3ajzAyFhkK%2FDdiHjwiDrUKyphIDPxg%2FoOUKJ2qinjCyOUGHZKFTc0YhVwgaTwZjTDCzvfJBjqkAeHimio%2FbFj%2B6mN8qSjI5l2rvhdDbj65ZMdZVHBiWdSplLyatLolbq4O1R%2FXO4Krvq0mrKLXZ8Ns3gtSdb%2FRZJ%2BeNc8AabAX7WZXMg0Gf7fBCKylk7GkOUMBtNM3L%2F3R1F5DcikU%2FZLkrrvZoSqWHgg9VaCvbLcCYDS4jlMCUZnp0037nbkCjzGNt9VcjC63cti7QcbBRq48PddwP2utvdX5puiJ&X-Amz-Signature=058e1866b3cc02496e23233b2a6dcf8e816dc329f959c9cf378691062fb74fdf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

How does our range object look like? `[11, 12, 13, 14, 15, 16, 17, 18, 19]`
- In line 4 we convert the value stored in `s` to a string and update the string `s`

---

![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/ef429a85-72bf-4b0f-bdc5-11531e846e34/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ROTP5DW6%2F20251214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251214T005256Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQCw1%2FWF9Ls%2BcDzD1uYD%2Bg3AGSGFKyZR20VSLUMPB2ErDwIhALVF95foh6mTLNn0poZz2oP8yZlLkgvXSoj3O1mEgMzaKv8DCCcQABoMNjM3NDIzMTgzODA1IgzlzpGvb9z7LiKYIUsq3AM4l8MzgIoodhLdOvVPiU8cLTx9ZpxIddFy5trmYPXrtgmEm6WegRKvRtXZ2Q99HJhSUhQUkBWzxjAg7dWiuP5FAPjWf94N3%2FObXJhzbbOqM5rfNfZJno%2Bczr1nMU6SFeJP1yIb9ltdSWJGKGF%2F85CkjXs23qdryeIR7WT8NT7BUBO9IPIlwXXg3EmVytwXV%2B6NHkkw7qCavXxlWj1aww4jvsgK79gRRwL%2FXLoX%2FzMeV61GEgy0Ese9KlxELIkn7Iok7ElpZtuylVgCmSMJaIcCUa%2FYMnlBnS2%2B3ETqT7aTmHf4s1J2jvmtizAWM0MPhS%2FKk4SNLMzXjzG%2BZZYoB3uiobcNQB6MIQ4qvm1Hj%2BqrqB6YySCNqPpYriVprKwGw49fZqLOoDjvHZ8k%2FmDIw%2BWuLPAR8ajvrd0%2FVCno1aOiL92Rvc5chIymcj9RUGtu8WfHM1vda%2BNacxy8RKrfwSyXb2%2FOsvvEN%2BUPG2N8S%2FIvwcVAv9%2B1pngeX%2FRu%2FQYAj5HyFWY%2BzG0d5FzaxUv18cr1X2TzR6mLwQZkySeGQbvPOOqVLGsxWO1QsB9vHR3ajzAyFhkK%2FDdiHjwiDrUKyphIDPxg%2FoOUKJ2qinjCyOUGHZKFTc0YhVwgaTwZjTDCzvfJBjqkAeHimio%2FbFj%2B6mN8qSjI5l2rvhdDbj65ZMdZVHBiWdSplLyatLolbq4O1R%2FXO4Krvq0mrKLXZ8Ns3gtSdb%2FRZJ%2BeNc8AabAX7WZXMg0Gf7fBCKylk7GkOUMBtNM3L%2F3R1F5DcikU%2FZLkrrvZoSqWHgg9VaCvbLcCYDS4jlMCUZnp0037nbkCjzGNt9VcjC63cti7QcbBRq48PddwP2utvdX5puiJ&X-Amz-Signature=382501c066a8304dae78fd45d35c791a4ab3af078a0615a672c177be10a97427&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/5325ec50-2cde-4680-91d6-eb07a26053f1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ROTP5DW6%2F20251214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251214T005256Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQCw1%2FWF9Ls%2BcDzD1uYD%2Bg3AGSGFKyZR20VSLUMPB2ErDwIhALVF95foh6mTLNn0poZz2oP8yZlLkgvXSoj3O1mEgMzaKv8DCCcQABoMNjM3NDIzMTgzODA1IgzlzpGvb9z7LiKYIUsq3AM4l8MzgIoodhLdOvVPiU8cLTx9ZpxIddFy5trmYPXrtgmEm6WegRKvRtXZ2Q99HJhSUhQUkBWzxjAg7dWiuP5FAPjWf94N3%2FObXJhzbbOqM5rfNfZJno%2Bczr1nMU6SFeJP1yIb9ltdSWJGKGF%2F85CkjXs23qdryeIR7WT8NT7BUBO9IPIlwXXg3EmVytwXV%2B6NHkkw7qCavXxlWj1aww4jvsgK79gRRwL%2FXLoX%2FzMeV61GEgy0Ese9KlxELIkn7Iok7ElpZtuylVgCmSMJaIcCUa%2FYMnlBnS2%2B3ETqT7aTmHf4s1J2jvmtizAWM0MPhS%2FKk4SNLMzXjzG%2BZZYoB3uiobcNQB6MIQ4qvm1Hj%2BqrqB6YySCNqPpYriVprKwGw49fZqLOoDjvHZ8k%2FmDIw%2BWuLPAR8ajvrd0%2FVCno1aOiL92Rvc5chIymcj9RUGtu8WfHM1vda%2BNacxy8RKrfwSyXb2%2FOsvvEN%2BUPG2N8S%2FIvwcVAv9%2B1pngeX%2FRu%2FQYAj5HyFWY%2BzG0d5FzaxUv18cr1X2TzR6mLwQZkySeGQbvPOOqVLGsxWO1QsB9vHR3ajzAyFhkK%2FDdiHjwiDrUKyphIDPxg%2FoOUKJ2qinjCyOUGHZKFTc0YhVwgaTwZjTDCzvfJBjqkAeHimio%2FbFj%2B6mN8qSjI5l2rvhdDbj65ZMdZVHBiWdSplLyatLolbq4O1R%2FXO4Krvq0mrKLXZ8Ns3gtSdb%2FRZJ%2BeNc8AabAX7WZXMg0Gf7fBCKylk7GkOUMBtNM3L%2F3R1F5DcikU%2FZLkrrvZoSqWHgg9VaCvbLcCYDS4jlMCUZnp0037nbkCjzGNt9VcjC63cti7QcbBRq48PddwP2utvdX5puiJ&X-Amz-Signature=c6aadeca9e0b293d41cd677650a3a80f7e63cc391ebbf790926bd9ddbbfec888&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- Correct, because we convert the variable `var` to a String which allows us to iterate over the string and store each element / number in the variable `num`, however as we want to calculate a sum, we need to convert the number back to an integer, which we do correctly in line 6 using `int(num)`
- Incorrect, because with every execution of the for-loop we override the variable `ds`, thus `ds` is always equal to `int(num)`, since we do not save the temporary result anywhere
- Incorrect, it is not possible to iterate through an Integer value, we must convert he integer to a string first using `str(var)`
```python
for i in 123:
	print("hello") 

TypeError: 'int' object is not iterable
```

---

![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/adad93ec-eae1-4758-89f9-2934428f09b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ROTP5DW6%2F20251214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251214T005256Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQCw1%2FWF9Ls%2BcDzD1uYD%2Bg3AGSGFKyZR20VSLUMPB2ErDwIhALVF95foh6mTLNn0poZz2oP8yZlLkgvXSoj3O1mEgMzaKv8DCCcQABoMNjM3NDIzMTgzODA1IgzlzpGvb9z7LiKYIUsq3AM4l8MzgIoodhLdOvVPiU8cLTx9ZpxIddFy5trmYPXrtgmEm6WegRKvRtXZ2Q99HJhSUhQUkBWzxjAg7dWiuP5FAPjWf94N3%2FObXJhzbbOqM5rfNfZJno%2Bczr1nMU6SFeJP1yIb9ltdSWJGKGF%2F85CkjXs23qdryeIR7WT8NT7BUBO9IPIlwXXg3EmVytwXV%2B6NHkkw7qCavXxlWj1aww4jvsgK79gRRwL%2FXLoX%2FzMeV61GEgy0Ese9KlxELIkn7Iok7ElpZtuylVgCmSMJaIcCUa%2FYMnlBnS2%2B3ETqT7aTmHf4s1J2jvmtizAWM0MPhS%2FKk4SNLMzXjzG%2BZZYoB3uiobcNQB6MIQ4qvm1Hj%2BqrqB6YySCNqPpYriVprKwGw49fZqLOoDjvHZ8k%2FmDIw%2BWuLPAR8ajvrd0%2FVCno1aOiL92Rvc5chIymcj9RUGtu8WfHM1vda%2BNacxy8RKrfwSyXb2%2FOsvvEN%2BUPG2N8S%2FIvwcVAv9%2B1pngeX%2FRu%2FQYAj5HyFWY%2BzG0d5FzaxUv18cr1X2TzR6mLwQZkySeGQbvPOOqVLGsxWO1QsB9vHR3ajzAyFhkK%2FDdiHjwiDrUKyphIDPxg%2FoOUKJ2qinjCyOUGHZKFTc0YhVwgaTwZjTDCzvfJBjqkAeHimio%2FbFj%2B6mN8qSjI5l2rvhdDbj65ZMdZVHBiWdSplLyatLolbq4O1R%2FXO4Krvq0mrKLXZ8Ns3gtSdb%2FRZJ%2BeNc8AabAX7WZXMg0Gf7fBCKylk7GkOUMBtNM3L%2F3R1F5DcikU%2FZLkrrvZoSqWHgg9VaCvbLcCYDS4jlMCUZnp0037nbkCjzGNt9VcjC63cti7QcbBRq48PddwP2utvdX5puiJ&X-Amz-Signature=f809a909c169145d4c7614eb6b055935dd4fa839f0e85c650a5c40737483dba0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



---

