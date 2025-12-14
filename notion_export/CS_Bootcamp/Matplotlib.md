---
title: "Matplotlib"
notion_id: "10c38918-e9a8-4ef7-9c80-40d2fba85e2e"
notion_url: "https://www.notion.so/Matplotlib-10c38918e9a84ef79c8040d2fba85e2e"
exported_at: "2025-12-13T22:27:10.757652+00:00"
---

# Matplotlib

# Motivation
---
We have [numpy](/ccc5737dc7c64936bced118aca375cf9) arrays to store n-dimensional data and do computations efficiently. We have [Pandas](/1867045b058343e1a66b677961515907) to wrangle around and manipulate data and we have Matplotlib to visualise data.
As you already know, top-managers prefer to see charts over endless DataFrames containing thousands of data rows. Matplotlib provides us the tools to visualise nicely the data in numpy arrays and Pandas DataFrames. 
Numpy is very powerful and comes with many customisation options. There are however some common plots that are used very commonly and you should be familiar with. Below first the structure of a Matplotlib plot is explained, followed by examples of the most important plots.
---
# Structure of Plot and Axes
---
**High-level**
The structure of a Matplotlib plot is the following:
![Structure of any Matplotlib plot](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/ff6704ea-30d1-4ada-8cd6-b70b4c5eebe3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ROTP5DW6%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T222646Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQCw1%2FWF9Ls%2BcDzD1uYD%2Bg3AGSGFKyZR20VSLUMPB2ErDwIhALVF95foh6mTLNn0poZz2oP8yZlLkgvXSoj3O1mEgMzaKv8DCCcQABoMNjM3NDIzMTgzODA1IgzlzpGvb9z7LiKYIUsq3AM4l8MzgIoodhLdOvVPiU8cLTx9ZpxIddFy5trmYPXrtgmEm6WegRKvRtXZ2Q99HJhSUhQUkBWzxjAg7dWiuP5FAPjWf94N3%2FObXJhzbbOqM5rfNfZJno%2Bczr1nMU6SFeJP1yIb9ltdSWJGKGF%2F85CkjXs23qdryeIR7WT8NT7BUBO9IPIlwXXg3EmVytwXV%2B6NHkkw7qCavXxlWj1aww4jvsgK79gRRwL%2FXLoX%2FzMeV61GEgy0Ese9KlxELIkn7Iok7ElpZtuylVgCmSMJaIcCUa%2FYMnlBnS2%2B3ETqT7aTmHf4s1J2jvmtizAWM0MPhS%2FKk4SNLMzXjzG%2BZZYoB3uiobcNQB6MIQ4qvm1Hj%2BqrqB6YySCNqPpYriVprKwGw49fZqLOoDjvHZ8k%2FmDIw%2BWuLPAR8ajvrd0%2FVCno1aOiL92Rvc5chIymcj9RUGtu8WfHM1vda%2BNacxy8RKrfwSyXb2%2FOsvvEN%2BUPG2N8S%2FIvwcVAv9%2B1pngeX%2FRu%2FQYAj5HyFWY%2BzG0d5FzaxUv18cr1X2TzR6mLwQZkySeGQbvPOOqVLGsxWO1QsB9vHR3ajzAyFhkK%2FDdiHjwiDrUKyphIDPxg%2FoOUKJ2qinjCyOUGHZKFTc0YhVwgaTwZjTDCzvfJBjqkAeHimio%2FbFj%2B6mN8qSjI5l2rvhdDbj65ZMdZVHBiWdSplLyatLolbq4O1R%2FXO4Krvq0mrKLXZ8Ns3gtSdb%2FRZJ%2BeNc8AabAX7WZXMg0Gf7fBCKylk7GkOUMBtNM3L%2F3R1F5DcikU%2FZLkrrvZoSqWHgg9VaCvbLcCYDS4jlMCUZnp0037nbkCjzGNt9VcjC63cti7QcbBRq48PddwP2utvdX5puiJ&X-Amz-Signature=fed08f1ec86e75028a6f711811fba1c59ee87ee6a7671f0ce0dc211555c58dd4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
A **Figure** refers to the entire chart. An **Axes** is the area within the figure that contains the data. There can be multiple **Axes** in the same **Figure**. Each **Axes** has one or multiple **Axis**, depending on whether the data is one, two or three dimensional (visualizing more than 3 dimensions is almost impossible).
When we create a plot we usually follow the steps below.
1. Create empty Figure and Axes
1. Extract `x_data` and `y_data` from DataFrame
1. `x_data` → labels on the x-axis
1. `y_data` → data that we want to visualise, e.g., the data that should determine the height of a bar or the trend of a curve
1. Add data to axes
1. Customize plot by adding labels to data, figure and axis titles etc.
---
**Low-level (structure of an Axes)**
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/538bd85d-681a-4d76-89f1-2c8328330627/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ROTP5DW6%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T222646Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQCw1%2FWF9Ls%2BcDzD1uYD%2Bg3AGSGFKyZR20VSLUMPB2ErDwIhALVF95foh6mTLNn0poZz2oP8yZlLkgvXSoj3O1mEgMzaKv8DCCcQABoMNjM3NDIzMTgzODA1IgzlzpGvb9z7LiKYIUsq3AM4l8MzgIoodhLdOvVPiU8cLTx9ZpxIddFy5trmYPXrtgmEm6WegRKvRtXZ2Q99HJhSUhQUkBWzxjAg7dWiuP5FAPjWf94N3%2FObXJhzbbOqM5rfNfZJno%2Bczr1nMU6SFeJP1yIb9ltdSWJGKGF%2F85CkjXs23qdryeIR7WT8NT7BUBO9IPIlwXXg3EmVytwXV%2B6NHkkw7qCavXxlWj1aww4jvsgK79gRRwL%2FXLoX%2FzMeV61GEgy0Ese9KlxELIkn7Iok7ElpZtuylVgCmSMJaIcCUa%2FYMnlBnS2%2B3ETqT7aTmHf4s1J2jvmtizAWM0MPhS%2FKk4SNLMzXjzG%2BZZYoB3uiobcNQB6MIQ4qvm1Hj%2BqrqB6YySCNqPpYriVprKwGw49fZqLOoDjvHZ8k%2FmDIw%2BWuLPAR8ajvrd0%2FVCno1aOiL92Rvc5chIymcj9RUGtu8WfHM1vda%2BNacxy8RKrfwSyXb2%2FOsvvEN%2BUPG2N8S%2FIvwcVAv9%2B1pngeX%2FRu%2FQYAj5HyFWY%2BzG0d5FzaxUv18cr1X2TzR6mLwQZkySeGQbvPOOqVLGsxWO1QsB9vHR3ajzAyFhkK%2FDdiHjwiDrUKyphIDPxg%2FoOUKJ2qinjCyOUGHZKFTc0YhVwgaTwZjTDCzvfJBjqkAeHimio%2FbFj%2B6mN8qSjI5l2rvhdDbj65ZMdZVHBiWdSplLyatLolbq4O1R%2FXO4Krvq0mrKLXZ8Ns3gtSdb%2FRZJ%2BeNc8AabAX7WZXMg0Gf7fBCKylk7GkOUMBtNM3L%2F3R1F5DcikU%2FZLkrrvZoSqWHgg9VaCvbLcCYDS4jlMCUZnp0037nbkCjzGNt9VcjC63cti7QcbBRq48PddwP2utvdX5puiJ&X-Amz-Signature=6891b286fb3a171450020cafba75bdd2437bbbd118626af207b93e6021df5e57&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
---
# Example plots
---
Below some examples of the most important plot types that we have in Matplotlib are given. It is important to understand how we proceed to create each of these plots.
All examples are based on the following DataFrame `players_df`.
![players_df](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/7dd40f51-55e2-4145-aab9-1461b59e5963/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667TMZMJD7%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T222648Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJGMEQCIFIaod3sqRgfSOjPaLMXVNPbnuW%2BBRgF5uv%2BEkOubEWGAiASTo5m64ZFLwX6%2FmTcCPguwnBIu3owytJUiufM5N0xNir%2FAwgnEAAaDDYzNzQyMzE4MzgwNSIMJV6S0acE5rB1pPs%2FKtwDQHmZ8nmximumo1nA9BFKVsDwqGI4ggFVBkTco95x5cVcBO9r20Vmf3FVVLYtyHvu4GBhpMt1LFsQvEsrAxd6MmmZwQ4tot40glQ4iTt%2FVz%2BVREwvhTLycYk2%2Fib2Hur%2BR63ZklL4uU%2Fg2EHniElSpAHC%2F22FQb7NO1R6Yz0cQLC4O%2FBE6ncz63KQjGWY4QYyAd6N27vqHOswt%2BafQqZhulodmwDnxJ%2BFS51kF%2BxG3%2Fzdp%2BKDb5F%2FLuTNprS0jt92mMy7Nq%2FsZn1ChbVD7wQ7wXeg%2BbnrdMyvAWMWjZkKNMvDDmxNpKZh9QqPq6BGTC%2BpKXDJczgghr3TGbL6ATKG9jY4dE3643Mdmmbp7oSVBY3OEK2HAswFjfUirBr7gdMwAVOXYlGmnZtOUreQPFvN4GnNw1rbl67oOnNNGFNMNtFx7rR%2FYFz8ONNlEN%2BAvCuLCJlA6RZ5j2CMeXvekaf6xa%2BtL5c8K8guWCghcivyEkbiVMsrji0i%2FqxoC3L%2BZH5vqg9n8K1v08synC0%2BbjVAg7fl8qYhbFwKqZjNnijUJL0nhGsKmM9TQBNmoZTkglfrqiGR2je49qjLXIpB8fSVR0%2B%2Bh%2BziGMcbyBiOXb5mf5d8SCgolG9eA%2BUloAkw8M33yQY6pgE9ZmI5NgUZET2vNIKv2QGkWheODc%2FB9nr4UJX957YYPP8AOAwl%2BfiA38%2FKnnYEOnQ6mdGrDDbZDuWKAQQW%2FU3tXpIwUKvU%2Bx%2F7dT9w%2FHb8yIwte4vb103m8fVYqiufb2HWo7evyQGt2oprtSjPxarKOGsktUjYPJprlqGjDqQNESlIHeRbLFypOgzGlsqQpXLQDCQF367q%2FMnN6ZHYwHXLEb0ANU7r&X-Amz-Signature=aa009425bfe6f575fb40818268a2d4c170e3ec328e21547f308db92ef7234a2d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
## Multiple Lineplot
---
[Video](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/5e7407c7-2c60-42cd-92a7-548479a8246d/Untitled.mp4?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VWG32L43%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T222648Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCICVfn9dhNxYWxmFn1sZUaNrYUBAYkzZsMGbtAZYSoOGKAiEAxB%2F3Q67SMLpQlm5KyeK%2F1mR2Cl5n5bPAfrEvKycUWJYq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDLomELBeif%2BBRFvWxircA%2FAsJ04CBz3Z4FaDG6kIyd3WK3X8Z0HxoX1kaliTyguuZaIQfm1jQw%2BhICynZMesBTJInnx%2B9wHsbeI8UhRugaFaEcfzysCS16vIr0FlWZJ%2ByomDpLKQdrGAYRWYbkfrLMeIVkDu9Vy%2Bkdwl2RPeB%2BV3QrAtKQnEyKxJRLzyKdBH%2FZ6wFkok8EsKtBFglLCRdIWf%2BmA3ZoZKimLYuD5zZLl5CzJBbg8KBivO5Ky75mZLwzehRpfCZsAHB9ci%2F40hnp82ps5xKlqzDaVhgdQSZBFlCas4uozT92wJWc3xIbLupoljO3Wdui9dbj6wUb1Lv8EkhxefyUUl6vd26pcfT98Dx0%2B4jwFJ95PmwYu9i%2Fn3BsSHU7ILvzMP7h5hARf%2F8LYSVNI96O0cMUjHWArbiAHk76nG2IjwW7FLSI9zQ3EBjR%2FMCxltfU6veNCTMWpEH5XoeCqd8tpE%2BmH%2FX4duTtgMq8oNtyyVwcVRmD5uvmn3sIB9gCF9J2BKU9oSDvS8MuPPrAwguDze5LutsvZB1vZAlr9mU6YnI6jCVLh13JnBD%2FhNvyFA3YhLanBaPtKBbEGwB7R95xsepbJCJyqB4rFciGnBeG6SBWiv9h8UdWFUSpH2HKk5iaXs73vpMIzO98kGOqUBIgiX5GZSA5haofy5jCouwsGmSXJFfVA8NLH%2F%2BuYCA38w9eQVp9hQ%2BnNzw7C32ONB5zC44w3iK5whFj%2FICMs0dRzL5EEGaKrMGED33Y%2Br2kW%2FEl1WhZ2N62fTV8U5ohL5c%2Fyqyzj3BUVfpQ4Xt9ilsAWWJRO99yZoyUBNJW2%2FOp5X14X2LJSccf234%2Ft7579HYMPFJ%2BlUKMUN%2BSXZrrwYnjowvNO7&X-Amz-Signature=190738ec338573cf403e3c317c20365b3e06df3dc364da3af66f1761f6021c8d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
---
![Multiple Lineplot shows that the top 10 players follow all the same trend among the different variables](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/eec7af85-7a4f-44c2-9bc2-7906de265eec/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VWG32L43%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T222648Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCICVfn9dhNxYWxmFn1sZUaNrYUBAYkzZsMGbtAZYSoOGKAiEAxB%2F3Q67SMLpQlm5KyeK%2F1mR2Cl5n5bPAfrEvKycUWJYq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDLomELBeif%2BBRFvWxircA%2FAsJ04CBz3Z4FaDG6kIyd3WK3X8Z0HxoX1kaliTyguuZaIQfm1jQw%2BhICynZMesBTJInnx%2B9wHsbeI8UhRugaFaEcfzysCS16vIr0FlWZJ%2ByomDpLKQdrGAYRWYbkfrLMeIVkDu9Vy%2Bkdwl2RPeB%2BV3QrAtKQnEyKxJRLzyKdBH%2FZ6wFkok8EsKtBFglLCRdIWf%2BmA3ZoZKimLYuD5zZLl5CzJBbg8KBivO5Ky75mZLwzehRpfCZsAHB9ci%2F40hnp82ps5xKlqzDaVhgdQSZBFlCas4uozT92wJWc3xIbLupoljO3Wdui9dbj6wUb1Lv8EkhxefyUUl6vd26pcfT98Dx0%2B4jwFJ95PmwYu9i%2Fn3BsSHU7ILvzMP7h5hARf%2F8LYSVNI96O0cMUjHWArbiAHk76nG2IjwW7FLSI9zQ3EBjR%2FMCxltfU6veNCTMWpEH5XoeCqd8tpE%2BmH%2FX4duTtgMq8oNtyyVwcVRmD5uvmn3sIB9gCF9J2BKU9oSDvS8MuPPrAwguDze5LutsvZB1vZAlr9mU6YnI6jCVLh13JnBD%2FhNvyFA3YhLanBaPtKBbEGwB7R95xsepbJCJyqB4rFciGnBeG6SBWiv9h8UdWFUSpH2HKk5iaXs73vpMIzO98kGOqUBIgiX5GZSA5haofy5jCouwsGmSXJFfVA8NLH%2F%2BuYCA38w9eQVp9hQ%2BnNzw7C32ONB5zC44w3iK5whFj%2FICMs0dRzL5EEGaKrMGED33Y%2Br2kW%2FEl1WhZ2N62fTV8U5ohL5c%2Fyqyzj3BUVfpQ4Xt9ilsAWWJRO99yZoyUBNJW2%2FOp5X14X2LJSccf234%2Ft7579HYMPFJ%2BlUKMUN%2BSXZrrwYnjowvNO7&X-Amz-Signature=992b2f50505956999c82320f00e061ebbdf2f57c8d5ef97ba31def24c9b1511e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
```python
# set index to player name
top10_players.set_index('Player', inplace=True)

# select only these columns from DataFrame that we want to visualize
y_data = top10_players[['Games played', 'Games started', 'Goals', 'Assists', 'total_points']]

# select the labels that should be on the x-axis
x_data = y_data.columns

# create the empty figure and axes
fig, ax = plt.subplots(figsize=(10, 8))

# add each player as line to the figure
ax.plot(x_data, y_data.iloc[0], label=y_data.index[0])
ax.plot(x_data, y_data.iloc[1], label=y_data.index[1])
ax.plot(x_data, y_data.iloc[2], label=y_data.index[2])
ax.plot(x_data, y_data.iloc[3], label=y_data.index[3])
ax.plot(x_data, y_data.iloc[4], label=y_data.index[4])
ax.plot(x_data, y_data.iloc[5], label=y_data.index[5])
ax.plot(x_data, y_data.iloc[6], label=y_data.index[6])
ax.plot(x_data, y_data.iloc[7], label=y_data.index[7])
ax.plot(x_data, y_data.iloc[8], label=y_data.index[8])
ax.plot(x_data, y_data.iloc[9], label=y_data.index[9])

# add a legend to the plot
ax.legend()

# add a title
ax.set_title("Top 10 Players")

# display plot to user
plt.show()
```
---
## Multiple Barchart
---
[Video](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/6a550786-a1ef-4049-98f6-90cc8956ff48/Untitled.mp4?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z4JJTGMI%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T222649Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIDyrEFUNPpm8UwOr9u9CJtVPDtQQ9Bl9GmmYTR1ro6URAiEAxpVryNiku3H9Rf7ftqEx8Eie5G3e5dYEFiIu4%2B2sE8wq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDJ%2BnwBybhiosUGMqEyrcAzkZ6KPbwaIDEZxKlQoLaQT8WBWNbzUCAAYRLtIxyvuLJTPd%2F6Z0MokrMKMmj4cB27TBhVU4SqmVq2Yg4FnVruqO8uoSAbDRP2sLHVpfx4bEyDquFvsm5BAKyWmHh%2BiNzJYv8w8MS7%2B9axDj1NjHWbRZQHeabTg%2BIgT7h9%2FyTYxI3zxPCwwbhyKRB0edTGuumkNke7z6Py0h2hV9ZNcFNdMli0J2fXgcVJT3TohhBWH99gPCYpVTIQdS0c8Q9z4qV8DRFkw28Nt4J0bL4yAYX%2BaNja7JAgAPyA9hhToYuTxOx9H8QKJ1fmFn3hJUVNkmkmXxN13kN44yx4DaXhH2ViA2%2F4Eq7OlZabO37g9c1asQ2O76e6qVaDS5f1ABC4WLBjxHnxhmFQZ01tVTNe0ef1SohATK%2FXCexJCaJGFK41gE%2F7ouQ3QTNzDJFJqgON5%2BR4OX8h3mxuSoKgLhmkjioTSXwqYquF0d2RdsDwFSKGNYml2gh%2Bec8EzvD5k%2Bxl0611kdO7XyUDGjqWrvQVqyTgN0aLmW1pv6Xx3B7yuhSsuE00c1KUYhW40rFsecwszF3Qlf2omxcP4GSxDaDaY8W%2B835sTjt9IOPvVhwckkbAbaU8WtaaMxVxCB9a6kMI7O98kGOqUBQtI2j1AEca%2FaqR%2BcUbebPLrFKaohMTg%2FHWE%2FjhvDwbKktf2s8CThd%2B8m2HPdiJEesbiw90P7TW05gTGlEBZCMXgP2k13fxyw1Vo1h6q40VMl1FrU5hQPPYE%2F8M6BXAatLozerQiJwAzxDByqgSRUgs0hOlF2DY2hiKmtSa7Pym3g5i8FQQtCbWHqLdq4VxQb1QqLpVeXxUsfDQEVfjhe0WmA10Xq&X-Amz-Signature=41a631a89a355adfec3b2322df464273a422677143432ba91078ea79e0d5f89a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
![Multiple Barchart visualising Total, Points, Goals and Assists of the top 10 players](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/85d2fc7f-6bb0-4352-919c-9e63616f31c1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z4JJTGMI%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T222649Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIDyrEFUNPpm8UwOr9u9CJtVPDtQQ9Bl9GmmYTR1ro6URAiEAxpVryNiku3H9Rf7ftqEx8Eie5G3e5dYEFiIu4%2B2sE8wq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDJ%2BnwBybhiosUGMqEyrcAzkZ6KPbwaIDEZxKlQoLaQT8WBWNbzUCAAYRLtIxyvuLJTPd%2F6Z0MokrMKMmj4cB27TBhVU4SqmVq2Yg4FnVruqO8uoSAbDRP2sLHVpfx4bEyDquFvsm5BAKyWmHh%2BiNzJYv8w8MS7%2B9axDj1NjHWbRZQHeabTg%2BIgT7h9%2FyTYxI3zxPCwwbhyKRB0edTGuumkNke7z6Py0h2hV9ZNcFNdMli0J2fXgcVJT3TohhBWH99gPCYpVTIQdS0c8Q9z4qV8DRFkw28Nt4J0bL4yAYX%2BaNja7JAgAPyA9hhToYuTxOx9H8QKJ1fmFn3hJUVNkmkmXxN13kN44yx4DaXhH2ViA2%2F4Eq7OlZabO37g9c1asQ2O76e6qVaDS5f1ABC4WLBjxHnxhmFQZ01tVTNe0ef1SohATK%2FXCexJCaJGFK41gE%2F7ouQ3QTNzDJFJqgON5%2BR4OX8h3mxuSoKgLhmkjioTSXwqYquF0d2RdsDwFSKGNYml2gh%2Bec8EzvD5k%2Bxl0611kdO7XyUDGjqWrvQVqyTgN0aLmW1pv6Xx3B7yuhSsuE00c1KUYhW40rFsecwszF3Qlf2omxcP4GSxDaDaY8W%2B835sTjt9IOPvVhwckkbAbaU8WtaaMxVxCB9a6kMI7O98kGOqUBQtI2j1AEca%2FaqR%2BcUbebPLrFKaohMTg%2FHWE%2FjhvDwbKktf2s8CThd%2B8m2HPdiJEesbiw90P7TW05gTGlEBZCMXgP2k13fxyw1Vo1h6q40VMl1FrU5hQPPYE%2F8M6BXAatLozerQiJwAzxDByqgSRUgs0hOlF2DY2hiKmtSa7Pym3g5i8FQQtCbWHqLdq4VxQb1QqLpVeXxUsfDQEVfjhe0WmA10Xq&X-Amz-Signature=51375c47f1d298beffa947f2c7148e2a7e7be40e6a7ebb52c628636c4f1c5cc9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
```python
# set index to player name
top10_players.set_index('Player', inplace=True)

# select only the data we want to visualize as bars in the end
y_data = top10_players[['Goals', 'Assists', 'total_points']]

# sort y_data so that the player with the most points is displayed first and the player with the least points last
y_data.sort_values(by='total_points', ascending=False, inplace=True)

# create empty figure and axes
fig, ax = plt.subplots(figsize=(20,10))

# select the x labels / player names
x_labels = top10_players.index

# create the x-values where each bar group should be positioned
# this gives us back an array with the numbers from 0 to 9
xvals = np.arange(len(y_data))

# define the width of each bar
width = 0.2

# add the first bar group (blue) which should be positioned at 0 - 0.2 = - 0.8, 1 - 0.2 = 0.8, 2 - 0.2 = 1.8, etc.
ax.bar(xvals - width , y_data['total_points'].values.tolist(), width = width, color='blue', label = 'Total Points')

# add the second bar group (red) which should be positioned at 0, 1, 2, etc.
ax.bar(xvals, y_data['Goals'].values.tolist(), width = width, color='red', label='Goals')

# add the third bar group (green) which should positioned at 0 + 0.2 = 0.2, 1 + 0.2 = 1.2, 2 + 0.2 = 2.2, etc.
ax.bar(xvals + width, y_data['Assists'].values.tolist(), width = width, color='green', label='Assists')

# set the dots at the x-axis
ax.set_xticks(xvals)

# set the labels at the x-axis
ax.set_xticklabels(x_labels, rotation=20)

# add the legend
ax.legend()

# add a title
ax.set_title('Total Points, Goals and Assists of Top 10 players')

# add axis titles
ax.set_xlabel('Player')
ax.set_ylabel('Number')

# add bar labels
for p in ax.patches:
  ax.annotate(str(p.get_height()), (p.get_x() + 0.05, p.get_height() + 0.1))

# display plot to user
plt.show()
```
---
## Stacked Barchart
---
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/296c8797-2893-4d70-9bf6-811108d787a1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YJTL7HQO%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T222649Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIQDXI9%2B0%2BYtXkHN%2BGluSDtMkIRkGbD4r7y0Rk80pneHeJAIgT%2BhRfK%2F%2FQczTdXHeUXOFzzy9n9Cel7c35Iy9llzSsAAq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDHglKi2%2Bq7ahybie9SrcA06dyyuCkBAFl37VuYe%2FAFFn8s%2FeQXrVXV50jRygqQZ4MwV3gpUnWa2gYfOI4osY2ZfRg6kGD%2BDFHswbYe27lDHzwlPtZRB%2F0zgq9STg1WhbpQOLPOjVxYrRDYjtftpIj7fzSWN6Fti1BcG%2F%2F8TYpf36Wb5jdPc3%2FlfbBH7u2lJoM6cTnTBLarck%2B4OfMMZoTEWU%2BRq8zHUUgExxbqG2eB97rVCU55Rck48QrcyDuctEu9KTrxoPeewWZ64xkm5nl8JED3YOTjdwrQqATyMwJ8jxqOhw1HdwNy3o%2BXJnlsiDDYz7oJJX9bz4VuNC9Z8pTTpuZ%2Fh%2BEPCMxFDMiSAZjzupG6gGKFQSIzhmXEzP4L3OaAevDXYoZgjlpEyrPq6lIL1k4wSBH6l1dZJsZGOdtxg53V91AgYlIk2Os79YRV595ZJM%2BkzoYfCR9KzsEHvfpHR7OSfMELMJ6tJvjJG3O5nHUSKVkaJhJtdPIVgaT%2BeBxKTkziHyfzM7Z%2FjEWayN2I9EsvNFsZS%2BPmO7zwEHmTEMoH7zucAZUfXCTixeNCBDRG9irdVvmbX2mI7sDNF2Y%2BPsf50K2Q3iDxufCn%2FByAP8ieqxXpGhIO6O0lOf2EZEvzxMVF23gVIA6VdDMMDO98kGOqUBJ%2B6N6z4loo7yD64AQTVfcuQ653LLp6HxCQP1afNl01SLHObFDO2UWtjDMULg%2BKoXV8OjojO473m53pZpu%2F278654Iw1gxrQKeyCNoQhnin3E3W9JaRLGpYjcBUH7sn1Q0oxPG%2BGofbkczSTaTcW60sj0YZcGRzU%2BalIpQTKhPCxZk3QegMUbsaMKab9D0uIXmy%2BE6uMHI6twbRe5HHhAvFH6XnAj&X-Amz-Signature=aa26b1287b1ffb80dbcc79a189ccb32305e44150c8cc5cec65bb7d45ff4f992d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
---
![Stacked Barchart visualising Goals, Assists and Total points of the top 10 players](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/8c5b2d84-ddcd-4218-a79d-540b92d555f7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YJTL7HQO%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T222649Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIQDXI9%2B0%2BYtXkHN%2BGluSDtMkIRkGbD4r7y0Rk80pneHeJAIgT%2BhRfK%2F%2FQczTdXHeUXOFzzy9n9Cel7c35Iy9llzSsAAq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDHglKi2%2Bq7ahybie9SrcA06dyyuCkBAFl37VuYe%2FAFFn8s%2FeQXrVXV50jRygqQZ4MwV3gpUnWa2gYfOI4osY2ZfRg6kGD%2BDFHswbYe27lDHzwlPtZRB%2F0zgq9STg1WhbpQOLPOjVxYrRDYjtftpIj7fzSWN6Fti1BcG%2F%2F8TYpf36Wb5jdPc3%2FlfbBH7u2lJoM6cTnTBLarck%2B4OfMMZoTEWU%2BRq8zHUUgExxbqG2eB97rVCU55Rck48QrcyDuctEu9KTrxoPeewWZ64xkm5nl8JED3YOTjdwrQqATyMwJ8jxqOhw1HdwNy3o%2BXJnlsiDDYz7oJJX9bz4VuNC9Z8pTTpuZ%2Fh%2BEPCMxFDMiSAZjzupG6gGKFQSIzhmXEzP4L3OaAevDXYoZgjlpEyrPq6lIL1k4wSBH6l1dZJsZGOdtxg53V91AgYlIk2Os79YRV595ZJM%2BkzoYfCR9KzsEHvfpHR7OSfMELMJ6tJvjJG3O5nHUSKVkaJhJtdPIVgaT%2BeBxKTkziHyfzM7Z%2FjEWayN2I9EsvNFsZS%2BPmO7zwEHmTEMoH7zucAZUfXCTixeNCBDRG9irdVvmbX2mI7sDNF2Y%2BPsf50K2Q3iDxufCn%2FByAP8ieqxXpGhIO6O0lOf2EZEvzxMVF23gVIA6VdDMMDO98kGOqUBJ%2B6N6z4loo7yD64AQTVfcuQ653LLp6HxCQP1afNl01SLHObFDO2UWtjDMULg%2BKoXV8OjojO473m53pZpu%2F278654Iw1gxrQKeyCNoQhnin3E3W9JaRLGpYjcBUH7sn1Q0oxPG%2BGofbkczSTaTcW60sj0YZcGRzU%2BalIpQTKhPCxZk3QegMUbsaMKab9D0uIXmy%2BE6uMHI6twbRe5HHhAvFH6XnAj&X-Amz-Signature=7148bb9820f0fadfbd67d7e537448107bd3c104b42f526fd40f5307102492086&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
```python
# set the player names as index
top10_players.set_index('Player', inplace=True)

# select only the data that we want to visualize
y_data = top10_players[['Goals', 'Assists', 'total_points']]

# sort data so that bars are displayed in descending order eventually
y_data.sort_values(by='total_points', ascending=False, inplace=True)

# create empty axes and figure
fig, ax = plt.subplots(figsize=(20,10))

# select the x-labels, i.e., the names of the players
x_labels = top10_players.index

# create position values for each bar -> array with numbers from 0 to 9
xvals = np.arange(len(y_data))

# define width of bars
width = 0.3

# add the first bar group to the axes (red) at position 0, 1, 2, etc.
ax1 = ax.bar(xvals, y_data['Goals'].values.tolist(), width = width, color='red', label='Goals')

# add the second bar group to axes (green) at same position so that the green bar is placed on top of the red one
ax2 = ax.bar(xvals, y_data['Assists'].values.tolist(), width = width, bottom=y_data['Goals'].values.tolist(), color='green', label='Assists')

# add x-ticks
ax.set_xticks(xvals)

# add the player names as labels to the x-axis
ax.set_xticklabels(x_labels, rotation=20)

# add a legend
ax.legend()

# add a title
ax.set_title('Total Points, Goals and Assists of Top 10 players')

# add axis titles
ax.set_xlabel('Player')
ax.set_ylabel('Number')

# add bar labels
for r1, r2 in zip(ax1, ax2):
  h1 = r1.get_height()
  h2 = r2.get_height()
  plt.text(r1.get_x() + r1.get_width() / 2., h1 / 2., "%d" % h1, ha="center", va="center", color="white", fontsize=14, fontweight="bold")
  plt.text(r2.get_x() + r2.get_width() / 2., h1 + h2 / 2., "%d" % h2, ha="center", va="center", color="white", fontsize=14, fontweight="bold")

# display plot to user
plt.show()
```
---
## Scatterplot
---
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/65d8f1be-8c74-4064-aa94-ebad99413a07/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RUJCRZUQ%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T222649Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIGYdm9vm6Wscr%2BVVEu5aLCVxt3XjU0RmxVQlX3dmuDgjAiEAo9yuQe%2BGLy0%2B73lAB3lBczG2PP6hdzi%2FzDnj0pAu038q%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDMEgmQXgArQZgTBU7ircA8ZUDOlQRZu4WyBvAL%2FXKjiJsd7u07omZvZVnIyfrGaD3%2FRkPOwlL2Uo%2FS1FGwqZnRn1zJ8oJCTepUi5VqzNFzW%2F%2FkDgD7JRYd6fgVDjagiv98SPiJxhOXwXtmW3FqhfY1fg%2FZYoLKJsa%2FVsyVyY43tiBV3vsz3tF5OciqQ63NK3azdvrWdrp9ZtdFkGLZ%2FLKZEad3JM0vPU8d6jNqeDSiAvcbLHqrn4MFb0XN7flCLCdMbaMzhUXHpv88iBLxPMmymK%2BvWgjeLxnBLQWrnh2QITrVapyUmzOZJkkgYX9UAv178uopmJ8dQmO1YxVYX%2BCHVyaKnW8N0iz5owx6HfEpjmxPoewvimdfFLrfQwGc%2B2JZqAEUXAfDGnQvitM5v1Aad%2B3wFCZSWqSHfxpX%2BAapeWAQj2H4cR0yoH%2FADLKWimpAJKmXMTHJXjRRBEnE0iVpN8AI0Ip20FS3st7tGQDNZWnPwPjqg5CAsKt4%2BOPubDcl5CsapBm1rnOX1ZMybMzpNswsgaSGtTwub6zBodcfDB73R0UQh%2B1fuU8yKf62fevOYPboi4ReI%2B12n4myz1t5naryppRljkb2NwdWUdqkfYRyN6Zjy9tIrmfz%2BvU0zBOXU8l9%2B0kTgtTJ5fMJbO98kGOqUBxH6FXquETzMEoSC2MqTz7e0%2F6qWHBIojlmwJxdZ%2B2bvyDzob4Fqh%2FWEZv1xbN6Fjaa1uxxW%2FSby%2FucdUbV6KiHAMBgo%2BzbDTwqanwvmDratCpXDMm0xEj4esAn9tSYPjNh%2B3ay1exvNqxkJV185EgLN%2BM3glS3tGm361E7ElJNFStcjNvG0%2FGXKeQCLjr6KCDQ4CQBnq%2FQJOZLdwigWy534fU78v&X-Amz-Signature=032642fdf773dbf5bd57687be61b787a9fa74039378a06aeb658d8502b5fbedf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
---
![Scatterplot showing that some relationship exists between individual goals scored and Team goals](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/9291c994-7678-4085-8772-708110007747/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RUJCRZUQ%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T222649Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIGYdm9vm6Wscr%2BVVEu5aLCVxt3XjU0RmxVQlX3dmuDgjAiEAo9yuQe%2BGLy0%2B73lAB3lBczG2PP6hdzi%2FzDnj0pAu038q%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDMEgmQXgArQZgTBU7ircA8ZUDOlQRZu4WyBvAL%2FXKjiJsd7u07omZvZVnIyfrGaD3%2FRkPOwlL2Uo%2FS1FGwqZnRn1zJ8oJCTepUi5VqzNFzW%2F%2FkDgD7JRYd6fgVDjagiv98SPiJxhOXwXtmW3FqhfY1fg%2FZYoLKJsa%2FVsyVyY43tiBV3vsz3tF5OciqQ63NK3azdvrWdrp9ZtdFkGLZ%2FLKZEad3JM0vPU8d6jNqeDSiAvcbLHqrn4MFb0XN7flCLCdMbaMzhUXHpv88iBLxPMmymK%2BvWgjeLxnBLQWrnh2QITrVapyUmzOZJkkgYX9UAv178uopmJ8dQmO1YxVYX%2BCHVyaKnW8N0iz5owx6HfEpjmxPoewvimdfFLrfQwGc%2B2JZqAEUXAfDGnQvitM5v1Aad%2B3wFCZSWqSHfxpX%2BAapeWAQj2H4cR0yoH%2FADLKWimpAJKmXMTHJXjRRBEnE0iVpN8AI0Ip20FS3st7tGQDNZWnPwPjqg5CAsKt4%2BOPubDcl5CsapBm1rnOX1ZMybMzpNswsgaSGtTwub6zBodcfDB73R0UQh%2B1fuU8yKf62fevOYPboi4ReI%2B12n4myz1t5naryppRljkb2NwdWUdqkfYRyN6Zjy9tIrmfz%2BvU0zBOXU8l9%2B0kTgtTJ5fMJbO98kGOqUBxH6FXquETzMEoSC2MqTz7e0%2F6qWHBIojlmwJxdZ%2B2bvyDzob4Fqh%2FWEZv1xbN6Fjaa1uxxW%2FSby%2FucdUbV6KiHAMBgo%2BzbDTwqanwvmDratCpXDMm0xEj4esAn9tSYPjNh%2B3ay1exvNqxkJV185EgLN%2BM3glS3tGm361E7ElJNFStcjNvG0%2FGXKeQCLjr6KCDQ4CQBnq%2FQJOZLdwigWy534fU78v&X-Amz-Signature=c7b411a96f7b0066201b5e0c2726fc0b7b877518a21e6dffaf8ec9e479429a70&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
```python
# let's select the x data and y data first

# create empty axes and figure
fig, ax = plt.subplots(figsize=(10,5))

# select x data -> goals scored per player
# select y data -> total goals scored by the team
x = players_teams_df['Goals'].values.tolist()
y = players_teams_df['Total team goals'].values.tolist()

# create scatter plot
ax.scatter(x, y, c=x, cmap='plasma')

# add figure title and axis titles
ax.set_title('Relationship between individual goals and team goals')
ax.set_xlabel('Individual goals scored')
ax.set_ylabel('Team goals')

# add trendline
z = np.polyfit(x, y, 1)
p = np.poly1d(z)

# display plot to user
plt.plot(x, p(x), "r-o")
```
---
## Subplots
---
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/423d00fe-f79b-4b14-a3bc-1ef9140ea670/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZCRQNB47%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T222650Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQC2abLrAa6%2BbydYPbjVKzG8zDlA0FyhhwJ49fKHnSRLkgIhAOYam78W0rzP9zV8PHRSmUWH0oPYKC3DH8JiR7PlIaHtKv8DCCcQABoMNjM3NDIzMTgzODA1IgzWBipJmip%2FzGaHXyQq3APaWF6GiCvyPgsGx7KZTQ1RGRdaL8P%2FTKlObUU12fMHcXVj%2BG7UhLZB01tLIfmbH6t6r2pSDUselnjnFV4MQDnl2OCUCbrmi22F3yi%2FIPNH0f1GdL%2FB5yCscSvlsLvIsXqSN%2BGqSDRETRqwD5b5%2B5zs5XhAjZBrxgZIfoAuKDcLaHyJ0pgLXYMFqPdu9bJBO7jIiXt2nWNH2oF%2F5z55iwl%2BM25Y%2BaY55N2%2FVOsYw8hD%2F6%2FnxyLKXd5oSz1LjERTzhptjilFDnyzjRy%2BRZx4tN5%2BRSm3dPyUXflxHwSGuRSgfr9qtgAxvj7BqOz%2FoEyGaXZrkj4za5fK%2FZs5uIhpOso3%2FtqCTpVZCmyIZXYPjh8l%2BfOxZYC%2BQPa8W8d6HifjlLupZPKwoE5ocx2C1GLtoOUqoHfmm%2FTIXbNvRnQwJqTFRKM2URunrXN2my7aLjxg%2FEmc6Vm9SilbFCvL6PVys0SnZ55gkXmiwyXoSpIt43SsNY3xCf2ehUY3f598Eet9LwS6QlwPCCNZpAQqT6WbERmozfBYvBVolXvsWkvaza3jHLkl6V0N%2Fp0ktFC8vht1F63qd5H6gKoigzF2dWPPaDGOB0%2B22aBvhBV1Y%2F7ZyJKtVqLREc82THrIrM5WijChzvfJBjqkAbsfMdDYziG5Pn0v9B3HjcOkIgj8%2BpTVB6RgtsPoWqHzvtXJcKfFEpvSGKAt2qAFzvOvVHmaKKEWi8LRIDJN%2BHchlPiWPv2N8YTpeP%2Bd75g8XQZrIhCZ%2F0g7O8B4aprPMq%2B8q%2FtmDt6QH%2FcEcI1bWUQuO%2BRNj9o%2BWhq5E8%2BnvImbt4pKrhDQdFjuASGeL%2F8Zo9g%2FVFk7RChyrerkSzFOtMGUCR0v&X-Amz-Signature=d7ed291f4dfe8cdec84a2e718cc4dfb2308ea592a886c4cc6f4618c530348794&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
---
![Figure containing 9 subplots, each of which is a Barchart of the top 9 players](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/4c3f752d-f738-4939-b044-f8fd8d24e94a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZCRQNB47%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T222650Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQC2abLrAa6%2BbydYPbjVKzG8zDlA0FyhhwJ49fKHnSRLkgIhAOYam78W0rzP9zV8PHRSmUWH0oPYKC3DH8JiR7PlIaHtKv8DCCcQABoMNjM3NDIzMTgzODA1IgzWBipJmip%2FzGaHXyQq3APaWF6GiCvyPgsGx7KZTQ1RGRdaL8P%2FTKlObUU12fMHcXVj%2BG7UhLZB01tLIfmbH6t6r2pSDUselnjnFV4MQDnl2OCUCbrmi22F3yi%2FIPNH0f1GdL%2FB5yCscSvlsLvIsXqSN%2BGqSDRETRqwD5b5%2B5zs5XhAjZBrxgZIfoAuKDcLaHyJ0pgLXYMFqPdu9bJBO7jIiXt2nWNH2oF%2F5z55iwl%2BM25Y%2BaY55N2%2FVOsYw8hD%2F6%2FnxyLKXd5oSz1LjERTzhptjilFDnyzjRy%2BRZx4tN5%2BRSm3dPyUXflxHwSGuRSgfr9qtgAxvj7BqOz%2FoEyGaXZrkj4za5fK%2FZs5uIhpOso3%2FtqCTpVZCmyIZXYPjh8l%2BfOxZYC%2BQPa8W8d6HifjlLupZPKwoE5ocx2C1GLtoOUqoHfmm%2FTIXbNvRnQwJqTFRKM2URunrXN2my7aLjxg%2FEmc6Vm9SilbFCvL6PVys0SnZ55gkXmiwyXoSpIt43SsNY3xCf2ehUY3f598Eet9LwS6QlwPCCNZpAQqT6WbERmozfBYvBVolXvsWkvaza3jHLkl6V0N%2Fp0ktFC8vht1F63qd5H6gKoigzF2dWPPaDGOB0%2B22aBvhBV1Y%2F7ZyJKtVqLREc82THrIrM5WijChzvfJBjqkAbsfMdDYziG5Pn0v9B3HjcOkIgj8%2BpTVB6RgtsPoWqHzvtXJcKfFEpvSGKAt2qAFzvOvVHmaKKEWi8LRIDJN%2BHchlPiWPv2N8YTpeP%2Bd75g8XQZrIhCZ%2F0g7O8B4aprPMq%2B8q%2FtmDt6QH%2FcEcI1bWUQuO%2BRNj9o%2BWhq5E8%2BnvImbt4pKrhDQdFjuASGeL%2F8Zo9g%2FVFk7RChyrerkSzFOtMGUCR0v&X-Amz-Signature=a729e5da9403ea65a5bf7296441b85fa0143d7b4cc6c9f7b88daa90704f2e3c5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
```python
# set index to player names
top10_players.set_index('Player', inplace=True)

# select the data that we want to display as bars
y_data = top10_players[['Games played', 'Games started', 'Goals', 'Assists', 'total_points']]

# select only the first 9 players as we don't have space for 10 subplots (well we have but then the chart would look a bit odd)
y_data = y_data.iloc[:9, :]

# select the column names as x-labels
x_data = y_data.columns

# create empty figure that contains 9 empty subplots
fig, ((ax1,ax2,ax3), (ax4,ax5,ax6), (ax7,ax8,ax9)) = plt.subplots(3, 3, figsize=(15,8),   sharex=True, sharey=True)
subplots = [ax1, ax2, ax3, ax4, ax5, ax6, ax7, ax8, ax9]

# go through each of the 9 subplots, select one of the players and the data to the subplot
ax1.bar(x_data, y_data.iloc[0], width=0.4,label=y_data.index[0],color=np.random.rand(3,))
ax2.bar(x_data, y_data.iloc[1], width=0.4, label=y_data.index[1], color=np.random.rand(3,))
ax3.bar(x_data, y_data.iloc[2], width=0.4, label=y_data.index[2], color=np.random.rand(3,))
ax4.bar(x_data, y_data.iloc[3], width=0.4, label=y_data.index[3], color=np.random.rand(3,))
ax5.bar(x_data, y_data.iloc[4], width=0.4, label=y_data.index[4], color=np.random.rand(3,))
ax6.bar(x_data, y_data.iloc[5], width=0.4, label=y_data.index[5], color=np.random.rand(3,))
ax7.bar(x_data, y_data.iloc[6], width=0.4, label=y_data.index[6], color=np.random.rand(3,))
ax8.bar(x_data, y_data.iloc[7], width=0.4, label=y_data.index[7], color=np.random.rand(3,))
ax9.bar(x_data, y_data.iloc[8], width=0.4, label=y_data.index[8], color=np.random.rand(3,))

# simpler approach using a for loop
for i, y_data_ in enumerate(y_data):
	ax.plot(x_data, y_data_, label=y_data.index[i])

# add bar labels
for bp in subplots:
  bp.legend()
  bp.set_xticklabels(x_data, rotation=20)

# display figure to user
plt.show()
```
---
## Boxplot
---
A boxplot (also known as a whisker plot) displays a summary of the range and statistical distribution of the data. The box itself represents the interquartile range (IQR), which is the range where the middle 50% of your data points lie. This is also known as the 1st quartile (25th percentile) to the 3rd quartile (75th percentile).
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/fd06423b-c4cf-4779-842a-ac6488fdb79f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TW5VG23U%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T222650Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIQDYSSa6BXfh84vMCAHXf4lByUWqGzCPMgh%2Bhi6RoxkN1wIgGzGYsjxQcsDiiXhqrL1so%2BmWUBIOk%2FswtI3UH6aBrmEq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDC5kvNAizNzaBpmdyyrcA4eR5xsqfkPfJzkwsVccWSYRxwVdM1dlvuQ1HV0g9D9K1h81dAo2AySV60Yu72jjf7ya0uh9ejzv7wP%2BOrshZqXqoNobZ%2FscAQpE6pHKyfBF0x59AILqiUhK4rh7h5PL20w1XwNJkzs0nm0YGoc6OV4GkX2%2Fti6b8V9cEmrn852WfGDRxaovl91S9NAn1X1X2TO%2FgYq2ZEyyTrlR%2FYApTusN9QmTpaWQ5Q6527L61Ng7k577bgeZ7WgUfdm%2BSzEMMgWK68z6AMYZbMxtQu1ZcjC1Qjf0pRtBuR656QHiAdYvMQ%2BOo9NP%2BjgkVmOtTKraMBIftItbI4BGHDWNmZpD3m1Jm8v2ApfQqyKGtZlOhhfVxqRSNIdwUNbxj8Iq6X8mOM0vQ45XvzcSTja496YEdorFkARRT%2FQyLwDZdEk%2FDMTVx9%2F7%2Fp4Lw%2B7MiMDd%2FBXbDePQ4K83LGLRI5BYEO7FpE8XaxNzCA3Z9fqjWOWT1QtWRjpVzyaCY2uCudVU90PIw28hmUOYIuqD2anYyMW4RV74QyQtUFJTtjf3z%2B68SXXTEkS%2FGfI18E2GeFC55ufIvx%2Bu9Le2KlvgMQZ0tEp9OQaYRGDIXnIJnet5pDvMq%2FKXg5aI%2BROoFoCrcJtcMPnN98kGOqUBAAkeNMO6sDD2%2F7qjP8fygnneksRqGNkt00Tgak09Cr%2B%2BQVIAHbJWxpRqSTyyfSog040hOuNsB6R5WbfSLeVjF%2Bt3BW3444OROok5mfUZpzzJTpEMVTQWUcfb12tNYrYuF5xNPHiIHPXPsOKtjOTu54FxLLttJa27VyoMIOgXi7WLvMxuUWQ%2FtxncQ%2FZcu40NIhhsEkgR7Ra1C4ctw2H6yTxo1MCZ&X-Amz-Signature=6cce0243613ffdda7b225bbb826852a73ac8d4722537ba7efdd0cd760a9cda7b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
Each quartile represents 25% of the data, thus the **box in the middle** represents 50% of the data.
---
# Functions
---
Below you find an overview of the most important Matplotlib functions that you should be familiar with and remember. All examples are based on the [example plots](/10c38918e9a84ef79c8040d2fba85e2e#0b85cc271c2947129e8bc21729bbc905) from above.
## [`.subplots()`](https://www.google.com/search?client=safari&rls=en&q=matplotlib%20subplots&ie=UTF-8&oe=UTF-8)
---
**Syntax**
With this function we can create multiple subplots.
`plt.subplots( << n_rows >>, << n_col >>, << figsize >>, << sharex >>, << sharey >>)`
**Input**
`<< n_rows >>` : optional (default 1)
- Integer
*→ the number of rows of subplots*
`<< n_col >>` : optional (default 1)
- Integer
*→ the number of columns of subplots*
`<< figsize >>` : optional (default `[6.4, 4.8]`)
- Tuple in the format `(<< width >>, << height >>)`
*→ the total size of the figure *
`<< sharex >>` : optional (default **False**)
- Boolean
*→ whether the x-axis labels should be shared amongst the subplots or not*
`<< sharey >>` : optional (default **False**)
- Boolean
*→ whether the y-axis labels should be shared amongst the subplots or not*
**Output**
- [Figure object](/10c38918e9a84ef79c8040d2fba85e2e#2f3203d6fd97468c96b2299a9702c9be) containing the figure
- One or multiple [Axes objects](/10c38918e9a84ef79c8040d2fba85e2e#2f3203d6fd97468c96b2299a9702c9be), one for each subplot
---
**Create figure with 2x3 subplots**
Assume we want to create a figure that contains 6 subplots in total: 2 rows and 3 columns and the x- and y-axis should be shared amongst the subplots.
```python
fig, ((ax1,ax2,ax3), (ax4,ax5,ax6)) = plt.subplots(2, 3, figsize=(11,6), sharex=True, sharey=True)
```
![Figure consisting of 6 subplots](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/084b14e5-65bd-49a8-bf0e-2b0d3f339eb2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TD2A5LYO%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T222651Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQCNXxOAaM0TbHj5t7cHA89JwvzCDyXOz8eBp36l1Bp%2BuQIhAOov%2FzEeWJ0%2BnI5fVBBpTXHwva258akM3D4N4Ee6pDIyKv8DCCcQABoMNjM3NDIzMTgzODA1IgyRHFLNOWfcFyj98Xkq3AMyuxmQ6IX5ZeKjHKSnBRC2CsISQxhMbBgn0d4au%2BLcEs%2BZ0I2SgirmQ%2FbTZZI3DCGZfmHv%2Bqr4vxg%2BMwiaEdEejoPcH6ZQqmGA22xdk1ImEzdGFc3V%2BqbnB%2B%2BI%2Bdc55wQPYFbTJ088GB45JIXj7U8v%2Bno30gNAf%2BZCwxNmZv2GcfyjSn5Xc%2BT3usiFVnCTCNoE0ctTSBRk6HzHW%2FN8wjPpNufOYfbdbECMihmzNy2dn1Wykw22nqgfTLGJ5l13rDgLR%2F3SQr%2FRHlvijHk6GeNnTFptHnlVU8GbPAWX2egPGymoESsvCTzEEyPFqVX%2BjYmw2lpz2jSWCBG%2BSJylkBvSEk4OB60c%2B2YU6PMu%2Fo1Gpj%2FlpQKj1svX%2BCsxA641fiTaQ6kSF6HwEsLyt7oUGy1DOScp%2Bdv91LG4zdbwVvniS1ppcepAydwBQazMCiwPOXFsZCz0WfvxUhoLNk4dW4fFX%2FpMW2j5K7dId9xGDYquJcmVKnohtLLz9jjEoqPzt9CJr0vhY0iSSKBKyLgXkAgPADIUeM%2Bi45msZnZopjfXlLuP6u6OTjAaYs3JF3HVDQcZGAyTfT%2BSkWAmpQKu8es8HDqb%2ByyY%2F1T7VlW3Ex%2FJmHSztfQ3l7dSocsJGzDnzvfJBjqkAb2MZTlZC988YxhoR4zbRo%2BcVtwbaBWlwnsp1wlVHq4jb4GJWrDUdKZtYrVrnrAgO5nUrlw59eerWf0I%2B4GmP%2FZ7PZ%2FkFCi28omVWJ9qzn86KRafbAO3v6o7Uh87tk5KaXzp9wN8sUXHZ2wvwyzqGYVbMx%2BDdXEl%2B14c4Uxw2Ofp7vHcsICy3k2kAlePjzIvVeKN6NIJYzOulhpUkBufATrUJhZf&X-Amz-Signature=3fa33ab4c72e711a58a3c5fee1247d874987244d14f752159214d41107d0c6d0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
If we want to access now a specific subplot, we can do so over the according axes which are saved in the tuple: `((ax1,ax2,ax3), (ax4,ax5,ax6))`, for example by using the [`.plot()`](/10c38918e9a84ef79c8040d2fba85e2e#c9af98cf80ba468aa1947825383ef41e) or [`.bar()`](/10c38918e9a84ef79c8040d2fba85e2e#7f417ec8d30647888b638c6e367259e1) method. You can see an example of this also in the [example plot](/10c38918e9a84ef79c8040d2fba85e2e#c7208eae4e864eedaa12c6212c0007a1).
---
## [`.plot()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html)
---
**Syntax**
With this function we can plot a line in our figure.
`<< axes >>.plot(<< x_data >>, << y_data >>, << format_string >>, << label >>)`
<!-- Unsupported block type: unsupported -->
**Input**
`<< x_data >>` : required
- Numpy Array **OR** List
*→ the data points of the line on the ****x-axis**** in the figure*
`<< y_data >>` : required
- Numpy Array **OR **Pandas Series** OR** List
*→ the data points of the line on the ****y-axis**** in the figure*
`<< fromat_string >>` : optional
- String
*→ a format string as **`[color][marker][line]`** which specifies formatting*
`<< label >>` : optional
- String
*→ the label / name of the line which will later appear in the legend*
**Output**
None
---
**Add new data line to figure**
Let’s assume we have an empty Matplotlib plot stored in `ax` and a dataframe `top5_players`.
`ax`
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/577f0d43-7182-44c5-babb-e0c447eb87e8/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V2OFOQPX%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T222654Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJGMEQCIFEyVQaovkjUhhBdqyFKRnDIMhhbMIGEyrvYM4J6tGJtAiA9jXXGyXEuFNw5U0uPY4nAWfELsvBaeIVtY72HD7c4Air%2FAwgnEAAaDDYzNzQyMzE4MzgwNSIMG%2FmzXfvqEDzUC9jYKtwD4dtDany8oBlZFD2OACjRpzSn0RZo5RycBslHNsJrhUq7QF6ss7Hfw15FBcIeivEJN7JhnfLwwpkpucMOWhvVpEgteKqftiLE9EdRJ8%2FymoPqeCswWIKgrwHGBO4Dvkl%2BUU0%2FERq2IPGUAWeQAPSeCdW3VKLgkR%2F3QU9WjHriYiAgI7%2BEpV8f1Im4oOq4GF%2BPmt2C9dU%2FIzeXpm2MuXFft9aXpXa0xqP2%2Blmkr%2FSdZgzSpPFQfVjUNnzNHi5PL8mi%2FJuTnKB1oqc9PybmvxGwxNrq3XLr8iNLQ7N%2FGJ0ZPfwEeeNxXftixEMBl2OvgPiFCUiLqu4tVF7dw0AZ2t9AAmRrrkCxeEOtsTgSS0Qw1b5sf58w%2BGWrrJGiKQM6z6I5Jff1Om5zCxqkQaNrN6LsQrfLm0b9noid9KMqGEB2I3Yhx%2B0umNH%2FmDWjz8%2BkbWyHcjgJqst1MXqe9qXDLjuDebpw1hIkqQsD%2Fe3xUrPTB6fGdkbXO7qGQHpixplrkWh2Ln3zUtf1K%2B%2F5K9cSApYU6VHOOkn12WpXNGSJEeKswR04VQANRZ9ZlLxhjPox5YgGlwVoA5q1%2FUvLYKfK88o%2FHsxMab%2BBhXMyvzL4OiICzT6mvkKEWLOXecOdwPkw4M33yQY6pgE5sCWRAZ%2B%2BylMaFDgOcNod8c5YcfvyBjsly9kXjlkhmc9aeyW5Yd%2Fi7nx9DyyhpHCGmJYSWsgc1FWv7qYDLaJOd1hu0eRIZ%2FgoYa6ISaziXsrp1SQMU6vzexXOkIMMIi4Gao8TVCwNML6XXtNbuXoqr9n4jWhsjnJSEbhCdVvWFsYJZ8DWbrYR%2FtqQLvZs1mG9iqWtpmA3AjbIAIlJGfYGVlt%2BX%2BDg&X-Amz-Signature=52951df7365c76c50deca1ace58c2a63409e2d6098c831f2e3f5fd9529005a39&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
`top5_players`
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/447fa778-3be3-4d94-b825-4dea8d88eea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RLTI7NM3%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T222654Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQD04NmRtr7%2FwaEKPSyuVLYZKPNXzsEJS6tbcZfxZmcITQIhAPfVfcqw4h7iDX67zC46o7FydoA9MctF4EiSlL%2BAN%2FSZKv8DCCcQABoMNjM3NDIzMTgzODA1IgwDcIckQI6jWg%2BdYCoq3AM1blfa0ScL7JbkHq0tkeQhARYRs25SZI9kGALEOqq1fgv7XBngoK7jEtpPA7rS7%2FeH3CCXvFwQ3fnewBVe94FO0rGlO%2FCRlsXsT2f4LK3iJ6rFXVHdLLGA3vB%2BmU2uPUF0KwBBnoz%2FPnBVJizJ64Fm1%2FwBwLE%2BLcnDkEjkI%2Fv59MOKzW2FNEZY68HZ3lzuJiwFYCz%2F2K2GMZKtYZUnOrlldYq4u%2FeHYVF04KadYgA9DbIfAskp4MevuHRgBUwVr0G%2BiH2vsbgqshVKulzBnAXuuGtoJ9LEEdGjveBJGwioS15XsREvAjQRhV%2FC0OA3e0Yx8vJdivKQIshdvKJwdER5N05LgqL%2FzwqN%2BvPK0uiH%2BSrqOJowXGvdcUnnppmeGgIl%2B2SCksb7L%2Bq23Ck4Oxy0YUF0KrwpKSZSEHeg%2ByTEgrhb2jHyVFXauSu9rvlp%2B0cY%2FjpCI2Tr9%2BgDN4uCTpSMa38BjfoTwNM65QAGnx4Eftex9MtpR7BhhK1qzxU%2BUMNZ3d%2FWTO1P%2B0%2FxOiJASXOxNhLQ5FAYECuGI6lapfWd%2FesgmmcStbm9yq3e3Gz8lt%2Fl5Yzqey%2BsXugpquj1AT0TO2yzVvNnLkdlhuvbJtNBUWbWLnI1bW%2BDoImBHjDfzffJBjqkASd3lBzZapBvTZxzHFPcmlnZbnmKJdvOd8xR6G1qmZ6%2B2vdHTY3DeYaYj3MblEugvdbTT73Rj0S8HrO4ZUqb5TLvujnvIwfrfWQSC2FvHxn2PYlIznMZw%2Frhh9ywFJesNDWbTPeeJL78WeltDcXm4rym30yRbRmYu49vwrMYZNTIihcNfxr09Y3dw13SbjyJmNRALfMF9O%2FUa6Ey2nyajpHSwDVS&X-Amz-Signature=bd0591d906cf508e35c26a159d73e317325429be54b6dfe0b1ca7841f171b33f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Now we want to add the data of the first player to the plot. 
---
In a first step we need to extract the x-axis data. On the x-axis we want to have following values.
![Values on the x-axis](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/e56dec9f-7b13-43be-a5bf-93646fbf99e8/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466432AAMJ6%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T222652Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJGMEQCICLnWADcc0Ex9TPInqJxGfvme9PQVYBc2LWhNz8c61ynAiB89oaKnJjvlnK8GT%2FoOpfvz6uLPNPx2uFHA7rR7ncgQCr%2FAwgnEAAaDDYzNzQyMzE4MzgwNSIM3u6NzQhI4706lMjQKtwD6VCrPJaj2KDnvXDVTcV0s1tvsVx35DjbsCt7gw3CHkpFxuM6eu3RJKxZgXTVKvl%2BcPVGygi1KUfq6jdat1j4VpV6i%2FJAknqUh1a1VZnuwEXVbzGwP4WRd6PZAaKLYCcwo2w2mA95Emozxky9TtPPVjV0pfHWSZXdcmhmMqGF5rFR6ga48OGf7jmqLwcmOsz%2FEdDTiTSo2%2Be8cm%2FGZ6lvqDQBlxbDv7UwIDz%2BkLyc2ZNe8L4p%2Fc7O3ITYlcAP1rs432%2FGyGU2qelTXRGJVJkcBM2UGtVyKZcPwkGBEwT%2B3eQhdF1ahY4QDuasRBW%2B7H4nDYmVf6XvoLB%2B41jPKFLhggjdO8Wf3DsADedjET%2BI%2BPcHp3CTxxxoVlSkg2grtzzbIclx1MEtCTi3wzMUAZZ5EHHUj%2FBVH1FbFkGSZHAd7dplIsSHjTCj6C0lvoke6hA0dJAYSHPzcALce%2BezqKiszG6WXkYdc3yPNTZ44zykJzRBxyIu7EP67%2Fz4rLPhxbCkjOYDHKcreNlpdKAmflModl4eCRDbFwbEO8uGM9lsdBjm4BLhYIwkeHVkIbLlZyDFh%2BXVPLII8T92Yvij%2BrHaeTDbVNqOnFsKqrWp%2FE0c6LumlYospEbkkIUnfOwwyM73yQY6pgERc7OpQR8tqnm41wPyTHDrTVjjmjJcsrafSzx3nlyfnDK3brJYyusmjoa40cbT6yuwBS4wGw2U0tWtoVXeNph6HaZoNTQ6MwfMCG6YakdmDrmu%2BTYknBgwzupQTK5lbKuHNQVa0VqEM2AUTLCrJUqZuHW1oUGgmgVtChvCY1aCjw9%2F8jsJiKGjg2Rb7yNE8d4Z1vo4wGBgrhjjplHLkykVCAKTnrfF&X-Amz-Signature=823875c0e3045d36c738fda03654d4c380fec380b9d5c71ebea00eb121b39626&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
We see that these values are equal to the column names in `top5_players`. Therefore, we simply need to extract the column names from the dataframe and save it in `x_data`.
```python
column_names = list(top5_players.columns)

column_names
['Player',
 'Team',
 'Games played',
 'Games started',
 'Goals',
 'Assists',
 'Shots',
 'Shots on goal',
 'total_points']

x_data = column_names[2:]

x_data
['Games played',
 'Games started',
 'Goals',
 'Assists',
 'Shots',
 'Shots on goal',
 'total_points']
```
We see that we extract only those column names that contain numerical values, e.g., the ones that we want to visualise later.
---
In a second step we need to extract the y-axis data. On the y-axis we want to have the numerical values of the player, e.g., the values for `Games played`, `Goals`, `Shots`, etc.
Thus, we need to extract these values from the dataframe as well. To do so, we can simply use the [`.iloc[]`](/1867045b058343e1a66b677961515907#659a00c8972e48a992e0dcabacb0cd4f) selector.
```python
y_data = top5_players.iloc[0, 2:]
```
---
In a third step, we need to extract the label for the data line. This data we extracted belongs to the first player, i.e., Jamie Vardy. Thus, we want to extract this player name from teh dataframe, which we can achieve by using [`.iloc[]`](/1867045b058343e1a66b677961515907#659a00c8972e48a992e0dcabacb0cd4f) again. 
```python
player_name = top5_players.iloc[0, 0]

player_name
'Jamie Vardy'
```
---
Now, as we have our data ready:
- x-axis data in `x_data` 
- y-axis data in `y_data` 
- label in `player_name`
We can add the line to our plot `ax` by calling the [`.plot()`](/10c38918e9a84ef79c8040d2fba85e2e#c9af98cf80ba468aa1947825383ef41e) method. 
```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(10, 8))

ax.plot(x_data, y_data, label=top5_players)
```
![Simple line plot visualizing the data of the first player, Jamie Vardy](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/424afeee-7a62-4799-bcb5-7349f9bdb6ac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466432AAMJ6%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T222652Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJGMEQCICLnWADcc0Ex9TPInqJxGfvme9PQVYBc2LWhNz8c61ynAiB89oaKnJjvlnK8GT%2FoOpfvz6uLPNPx2uFHA7rR7ncgQCr%2FAwgnEAAaDDYzNzQyMzE4MzgwNSIM3u6NzQhI4706lMjQKtwD6VCrPJaj2KDnvXDVTcV0s1tvsVx35DjbsCt7gw3CHkpFxuM6eu3RJKxZgXTVKvl%2BcPVGygi1KUfq6jdat1j4VpV6i%2FJAknqUh1a1VZnuwEXVbzGwP4WRd6PZAaKLYCcwo2w2mA95Emozxky9TtPPVjV0pfHWSZXdcmhmMqGF5rFR6ga48OGf7jmqLwcmOsz%2FEdDTiTSo2%2Be8cm%2FGZ6lvqDQBlxbDv7UwIDz%2BkLyc2ZNe8L4p%2Fc7O3ITYlcAP1rs432%2FGyGU2qelTXRGJVJkcBM2UGtVyKZcPwkGBEwT%2B3eQhdF1ahY4QDuasRBW%2B7H4nDYmVf6XvoLB%2B41jPKFLhggjdO8Wf3DsADedjET%2BI%2BPcHp3CTxxxoVlSkg2grtzzbIclx1MEtCTi3wzMUAZZ5EHHUj%2FBVH1FbFkGSZHAd7dplIsSHjTCj6C0lvoke6hA0dJAYSHPzcALce%2BezqKiszG6WXkYdc3yPNTZ44zykJzRBxyIu7EP67%2Fz4rLPhxbCkjOYDHKcreNlpdKAmflModl4eCRDbFwbEO8uGM9lsdBjm4BLhYIwkeHVkIbLlZyDFh%2BXVPLII8T92Yvij%2BrHaeTDbVNqOnFsKqrWp%2FE0c6LumlYospEbkkIUnfOwwyM73yQY6pgERc7OpQR8tqnm41wPyTHDrTVjjmjJcsrafSzx3nlyfnDK3brJYyusmjoa40cbT6yuwBS4wGw2U0tWtoVXeNph6HaZoNTQ6MwfMCG6YakdmDrmu%2BTYknBgwzupQTK5lbKuHNQVa0VqEM2AUTLCrJUqZuHW1oUGgmgVtChvCY1aCjw9%2F8jsJiKGjg2Rb7yNE8d4Z1vo4wGBgrhjjplHLkykVCAKTnrfF&X-Amz-Signature=daa03bc53da75175b8ba6d76dd74f45933426c25ca8636ed5b7f3918593393f3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
---
## [`.bar()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html)
---
**Syntax**
With this function we can add a group of bars to a plot.
`<< axes >>.bar(<< positions >>, << heights >>, << width >>, << label >>)`
**Input**
`<< positions >>` : required
- Numpy Array **OR **List
*→ the position of each bar on the x-axis*
`<< heights >>` : required
- Numpy Array **OR **List
*→ the height of each bar*
`<< width >>` : optional
- Float
*→ the width of the bars*
`<< label >>` : optional
- String
*→ the label of the bar group*
**Output**
Barplot
---
**Add bar group to plot**
Let’s assume we want to add the shots of the players in [`top5_players`](/10c38918e9a84ef79c8040d2fba85e2e#84b746f85685409faa2112f902d32b3c) as bars to our empty figure [`ax`](/10c38918e9a84ef79c8040d2fba85e2e#aeceede5d5344076a521bca2b96ad759). So in the end, our plot should contain 5 bars, each one representing the number of shots of a player. 
---
In the first step, we need to select the data on the y-axis, i.e., the heights of the five bars. We can do that by extracting the values in column `Shots`.
```python
y_heights = top5_players['Shots']

y_heights

Rank
1    71
2    66
3    70
4    68
5    95
Name: Shots, dtype: int64
```
We see that we receive a Pandas Series now. However, as we can see from the [syntax section](/10c38918e9a84ef79c8040d2fba85e2e#9d79b19e7b42439caaa6444928cd3593) we must provide a numpy array or a list.
We can simply convert this series to a list by using the `.values` attribute and the `.tolist()` method.
```python
y_heights = y_heights.values.tolist()

y_heights
[71, 66, 70, 68, 95]
```
---
In the second step, we need to define where our bars should be placed at. Differently to the [`.plot()`](/10c38918e9a84ef79c8040d2fba85e2e#c9af98cf80ba468aa1947825383ef41e) we don’t provide here text labels as we don’t have two dimensional data, but must rather tell Python where to place the bars. 
Assume we want to have the first bar displayed at position 0, the second one at position 1, the third one at position 2, etc. 
So in the end we need a data structure like a list that contains the values from 0 to 4, which we can achieve by using the [`range()`](/5b0832dbf9454eb1941b7632e68a9abb#945ca671e7cb4dbea2b73be19473e385) function.
```python
x_positions = list(range(5))

x_positions
[0, 1, 2, 3, 4]
```
---
In the third step, we need to extract the label for our bar group. The bar group visualizes the number of goals per player. Thus, we must extract the text `'Goals'` from the dataframe column headers.
```python
bar_label = top5_players.columns[4]

bar_label
'Goals'
```
---
Now, as we have our data ready:
- bar positions in `x_positions` 
- bar height in `y_heights` 
- bar label in `bar_label`
We can add the five bars to our plot `ax` by calling the [`.bar()`](/10c38918e9a84ef79c8040d2fba85e2e#7f417ec8d30647888b638c6e367259e1) method.
```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(8, 5))

ax.bar(x_positions, y_heights, width=0.4, label=bar_label)

ax.legend()
```
![Barplot in which each bar is representing a player and the bar’s height  the number of shots the player has fired.](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/a0271c86-a61d-4547-a7de-fe099be8ae53/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y44ND6OT%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T222655Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJGMEQCIDE3Rww95puWdO4G70t%2FLxCdy7nBgVxXABMqUS174GHxAiAYg5fC1tBuXhWeiwvubn%2BpuHJoUsPXBOlMyD8MMP9ZEir%2FAwgnEAAaDDYzNzQyMzE4MzgwNSIMYy88vLCDw8vIYWOsKtwD0WTBpTTCxssYk1SbwdfBrYVj6k41hAbkK7WFxHHtWNK3AMDu%2FSLpdk9rHJHPRlQsi6Mlidq5aY349CUeuBxQhglD66pPCNHYX1jNSFlvAS%2BfX6tkCmGC8dsBag9MNXLJIp7Z9LF6U0lGftylLDTZe2p2ihLK%2FcY1VzGsCN5rndO7OhLtbpAYJcH8HSkmyRSvySYjVfyltm%2BP%2BS4lcK%2BGzj3fkmBVArIVATwMVL%2FZV6eViamryWwFGMcoxzmWeNYum%2BuCq4w%2B1SWsI007i2BOEIIasTcFfLDeHKQkjZFqrrIiPjbfg4Dru3AyFLgqjfg6BqibQ%2FZ6jjY%2Fd%2BvQZ9TPWWOVP63dZPDcGRJmvinEwTqFDnBwt7FrBwaTIBA%2FvtCOByMo50iUubGeadb4bfwiP%2FVuBHi83PMgnZEmPmpsLMP%2FfzBwJZpq9vxn935jYCf%2Bv90JHAvZsTA30rDFWakprOO0uVTQ8%2BGPGIFgJiakJ4T9XiO89oi4PQKWb2Myp7BYDIww0yOIdFshDBLXMJaMB6FmKErW%2FaMzhGixl3rCA6s6E2gPbn%2BPz9h5p%2FMck6o6mdGIPyeASWocAxwU%2F4xRpTHVW6JTt9wOwBJb7CeQXMD8fjydjtO8ty2SGYow%2Fc33yQY6pgG1wlHAW%2FHIgvJQLanaDLZ7EEJ22GJ%2FQm3Oj%2FqgKWbihzYvxasSStAqoXFLdO7XYREOdYKjujcl%2BLZovyQjTIE%2FoLDJ81I8c20kHonm%2FF%2Bdx%2BAdS6iemiqHImtW2PQ7E2HAclfFxFgBNbkdi2rV5anlvqTelGUxppzSNIev6VwYxkJKVLwYKiBo34Zb5UboIDcqLv4h0X8%2BAjhIflIFN0txRvc2WVQq&X-Amz-Signature=f06b323e13466af639e2d2eddfec9201bc6daa7344eebdd0f78465b31eeb37ff&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
---
## [`.barh()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.barh.html)
---
**Syntax**
With this function we can create horizontal bar plots.
`<< axes >>.barh(<< y_pos >>, << width >>, << height >>, << color >>)`
**Inputs**
`<< x_pos >>` : required
- Numpy Array **OR** List
→ *the x coordinates of the bar plot*
`<< y_pos >>` : required
- Numpy Array **OR** List
→ *the y coordinates of the bar plot*
**Output**
Horizontal Barplot
---
**Creating a horizontal barplot**
Let's say we have a data distribution of the world population per age group.
```python
age_groups = ['0-14', '15-24', '25-54', '55-64', '65+']
population = [1800, 1200, 2300, 800, 700]
```
- `age_groups` represent y-coordinates (vertical position)
- `population` represents the width of each bar.
we can illustrate this information in a horizontal bar plot.
```python
import matplotlib.pyplot as plt

# Create empty Figure and Axes object
fig, ax = plt.subplots()

# Create a horizontal bar chart
ax.barh(age_groups, population, color='skyblue', edgecolor='black')

# Add label to x-axis
plt.xlabel('Population in millions')

# Add title to figure
plt.title('World population per age group')

# Show plot
plt.show()
```
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/9ea36f69-faca-4896-a2ab-dda14fdf860f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RIJUES25%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T222656Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJGMEQCIFZ4mH859GK8T92W9Bt0x9jmGqpWIVtvHXW7JwRgl4j9AiATlzdckoarl6n%2F7ysqc2Kgp5dD5ra%2BxOT%2BiGLTe8sUHSr%2FAwgnEAAaDDYzNzQyMzE4MzgwNSIMnziJTuXT9J5lm48ZKtwD4fu2ZdecsHRoX9LvjNJpMaKfxDy60ss4pa1%2BWJ96fkvjhZbMS2prcp%2BlGXW1ji1yL%2FgjvRDXUD0g08pWFQIYV%2F2UORKA51R8TAwMTH7DcJGjW042dU2lSVqxV27qNcKW081xvoxKQ84vKBQKllTx1jEwMxHI3cQGJgzuR29lqrMIuebFr%2FBn7GARHvgFcNCrn93knDAJioE3gOkcbvBZgZ02D9yKF2UEr%2FdIzgdh0tOvHPxEOsJf%2FxY3ur19QA%2Bui6p3YYtBvgaxz18ue83TcIefdBCApC5ik0cVXDcT8ilgKLD50keWRLg45N93EpUYIG0FzzGrSuwu2oFDjrsVgg%2FO2xnFlvjtcSjmSUa5uTDhVuWOyhBBbuwZTNPsq%2BmZ2XFLgmWVGvuvo69pOXtjhTOBx2ydRd%2FMmIR6eR2rj%2BQMgZDqf%2BRAsfqsW8Dd1tqVsYcW8KqXDz1SCqaG0AJ58Gdtu4N%2Bbvyqj1XesK6JxyrqsqU5sO5ItDcdmntX1%2Fmpw0bb0pPSeVzfNVKaNhraqR%2F45Gdl10l0uxNMV0yLqRgeN9h4KxztkdyRnkGgYiMeabxXJBwluaiAEJvMky2j1kOI3l%2FYtqS0IBzyZcix2QUvpIVxsEXtvutrYUkw%2FM33yQY6pgEciLQnvldIHBIBYQxY1PFCv3TX7ylmgvWbrZO61HHjUgVsNnLHLgKyiyjLmWtCDKDkDbW3Yo%2FeqieNScEEIx0d1S6IhFCIGUisWWceuBUcfsIW6Ct3TCW3OMSplOyZM78ibGM8xLDRAQU3%2F%2BSP8kPE7vK7vzXP7u4zykcTkOx8Ih54wiQgLsc25kdSirOKa1wB1S%2BhS3ZpBvV9U90repSdFsz1B0mE&X-Amz-Signature=f4f1b52fc7183c4bafeac99b8dde96f041cedf37cb3398fc1794957983e462e9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
Each horizontal bar represents an age group, and its width corresponds to the population of that age group. This is a simple and effective way to visualise such data.
If you want, you can also specify the color and the edge color of your bars by providing the `color` and `edgecolor` parameters.
---
## [`.boxplot()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html)
---
**Syntax**
With this function we can visualize the distribution of data based on the five-number summary: minimum, first quartile (25%), median (50%), third quartile (75%), and maximum.
`<< axes >>.boxplot(<< data >>, << vert >>, ...)`
**Input**
`<< data >>` : required
- Numpy Array, Dict, DataFrame **OR** List
*→ the data to be displayed*
`<< vert >>` : optional
- Boolean
*→ determines whether the boxplot should be vertically or horizontally oriented*
**Output**
Boxplot visual
---
**Plotting a Boxplot**
Assume we want to visualize the number of goals of the 200 players that scored the most goals.
Firstly, we extract the age-group data for our boxplot visualization.
```python
goals_scored = players_df["Goals"][:200].values.tolist()

goals_scored
[23, 22, 22, 20, 19, 18, 18, 17, ..., 1, 1, 1]
```
---
Now, we are ready to plot our data using the `.boxplot()` function. 
```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(8, 5))

ax.boxplot(goals_scored, vert=True)

plt.show()
```
![Boxplot representing the distribution of the number of goals.](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/babf9c08-ad63-40bd-9584-5f2573c8f676/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665XMJM3HV%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T222658Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCID3I7u05ZZnrIJjnmPdwTKJCOR7RCr7gvlc%2B3VyiRDInAiEAoeQyMUdYSSNlzQR0t%2FZWGkvSMMhrpBhAqWsyPlp091Uq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDKUqCAFs9ElT29JX%2FircA9ifONRHdwBBIS%2FcSZXSDyWaHFx4wqDoTqIA7ZglsatVInbFnIsd60ufwjVh3O2Yge8YSiAv8W6rUl11btVWjXNeN6ERZgEzHJ5qs%2FjK0cLhME7odRqF2XOWp%2FN6wMX5ZQCeb7ZH0R%2F3SxAEuJK5oGnSR8BTF72KdI%2ByeeWMAzt4gWOPtu8RtYKI8X5cW8MwmZyNjcgAgSmBPv0zWmKYPFWDEu86y3iuvWRjtqUnlUsnbB6XR6mjd9P00VluD0GrYHY78BRrubszNUtIuWekuC16PYwNJ8FZy7hbX53MA%2BYcQ9in8%2BQftllJXkSZqooLwLcK70381t7K1hw6sIT6VRBPJF7saPAyLJi0P3Ib7n9afc45IZtuQl9YOlxNSsay6T%2Fx1zhqjt1QMcRLXUyfWEcZopKz6i5OWCu2MPRknTx3DRjHUyGItUxuFbWoPudEJvXprxcpBr6wX9XJEd9j0ZXdqGbfTuddh2CsvWvBBvJ9lDAo%2FWSbZdsCQsI8NNMlrjhVjx70qrqozkxXFzECGiTTz9Phg%2BfLol8xj9GV3%2BAapExKPK%2FNc6O3Cy1uTLi%2F7lkEl7H6fiQztIhje2TSe68GUU9HZKiKkcffL8ilLF6ZHEu6rjGH6D%2FaFiPMMNHO98kGOqUBu%2F8euU%2F6jNt3jMCQ0pZBant8jlhIhrIcX90pTSvteetl3qqP2MME87SMw%2BpcK46m7ENN58Z93ClvQ7iCeN6qV9e1jCZTs4AKGEOoA0GEjhkWOTLkDlf5vPJHQJ3nNLORQxn8VeA524TrjE%2F8%2FAUnfQCcz0x9CEUsNQswc%2FP5HjV72%2B3iwayeDIFnBZdkejTmmqq0L1UEqdq152GhE4umU5dugqhf&X-Amz-Signature=88e7f3bae7648871fbf8e71e9f2bdf43b4ec93ad2dbaef34069cdb0c3d838f69&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
As we can see from the Boxplot, the median is below 5 goals and there are quite a few outliers on the upper end. If you don’t know how to interpret a boxplot, check the [explanation here](/10c38918e9a84ef79c8040d2fba85e2e#29e8af14c0a848898738443608b4a50a).
---
## [`.hist()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.hist.html)
---
**Syntax**
With this function we can create a histogram of a data distribution.
`<< axes >>.hist(<< data >>, << bins >>, << edgecolor >>)`
**Input**
`<< data >>` : required
- Numpy Array **OR** List
*→ the data that you want to plot as a histogram*
`<< bins >>` : optional
- Integer
*→ the number of bins that the histogram should have*
`<< edgecolor >>` : optional
- String
*→ the color of the edges of the histogram bins*
**Output**
Histogram visual
---
**Create Histogram**
Assume we want to visualize the number of goals of the 200 players that scored the most goals.
Firstly, we extract the age-group data for our boxplot visualization.
```python
goals_scored = players_df["Goals"][:200].values.tolist()

goals_scored
[23, 22, 22, 20, 19, 18, 18, 17, ..., 1, 1, 1]
```
---
Now, we are ready to plot our data using the `.hist()` function. 
```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(8, 5))

ax.hist(goals_scored, bins=30, edgecolor="black")
ax.set_xlabel("Number of goals")
ax.set_ylabel("Number of players")

plt.show()
```
![Histogram visualizing the distribution of goals scored of the top 200 players.](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/ef1e252c-0604-45a6-8a70-945324656a1d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z4EPHJA5%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T222659Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJGMEQCIC277NYu27jD6e6BSrJu5zgGq8wciZxDyubzkBCs3R5CAiA3ygPiJwH7ZJcYgg9Ra%2FLmAtV5gb%2B4166yCIFVOi4Moyr%2FAwgoEAAaDDYzNzQyMzE4MzgwNSIM%2F5%2F%2FcaBA2uRk9iwlKtwDmLulDdNoteUJJMqYGwn%2Ffcwm7U1bdDNNKuHZEV%2Fyb6aY5yphBX3pQYi6J3kHKqcH0aP0K%2BQ2UOLLDifZa0R3LHCKbaIqPtDoMlLWY8DyAlmrI8Jl0CAu0xk5wEIOLAFGHCirBVxPFGoKTRj6gXKqR0H4WKgTIoOy1wzg%2FTgLmodrp1G9q4Ti%2B%2FiqHvhZbHB9TCs2%2BUPLocbVC5Kgowed7aNYSdLgPbmaBCnY4GAG0G54h%2BFlFNQnX3bhpCTWFFHgmLZmOCbl0cCVwlXSPWnnFQjiQW0bbGYN1OatL%2BSmRXlvXDUMtSyMu1NIzmNp%2BEBj1Ee5NrQ7yLhJrNLsABKYgxQJWVAAcns5K20S%2F6HZDXFsrQ1xUClNtJ15Jo%2FeIv9jzSd4dJip1ByWc1I2eBAGtWxP3ww%2FC%2F%2B0w9a5xUKpT1He%2B5suF2bInwV1Lyd5cch%2Bw%2FXbSyai65vwkUg9%2B%2B4V9w%2FZ98vZpzl2iAd1d7m914XDR6ezJmgZvLh1gcTDyh65F3pNgOnKGyZbnT%2FF4KlfvcAepT1f3yErhY9YON5THZ%2F0IFH%2F53JlBEsS6WYuXznTpb2Vvfs5bnDlGtkW4iF8IjYqAC2WaofvLelcU1iGOCwpk9Zf61DlfE4lwKIwjs73yQY6pgEUZjmCWXFJTFSnAsRzkjAeBcFkEzzx%2Bnhhf%2BX088oH6cUe2Z%2FX4L9xTkkV34ZuMsRKfU7v4WHI%2BRTKQ9ZqOcY7qkVIs%2Fg5j5hqFCBIX%2FEkLuIFtChzhbvwabq0PFD5IMULBG9lx62OnII%2FSpYeS47siQdwfkrbM%2BRkt34rtXuM1NuyREJIB211oDVihH%2BPz3gEk0l%2FH%2BuPvg3ofQuuN%2BkbWklwvPo%2F&X-Amz-Signature=d4d150d89eca4f105322f0554d364be2d9d8b4735b1f3e953313a259e5e76894&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
This histogram helps us visualize the Goals scored distribution: most players scored less than 5 goals. The `bins` argument divided the age ranges into 30 equal parts. Therefore, there are exactly 30 bars visualized. The `edgecolor` argument puts a black border around each bar in the histogram.
---
## [`.hist2d()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.hist2d.html)
---
**Syntax**
The function creates a two-dimensional histogram. This type of histogram is useful when you need to visualize the relationship between two numerical variables (each represented on the X and Y axes respectively), and the frequency (or count) of observations that fall within a certain range of values (represented as density level on the graph).
`<<axes>>.hist2d(x, y, bins=(xdim, ydim), cmap='<<colormap>>', ...)`
**Input**
`x, y` : required
- Numpy Array **OR** List
*→ the data to be visualised.*
`bins=(xdim, ydim)` : optional
- Tuple/List
*→ determines the number of bins in each dimension.*
`cmap='<<colormap>>'` : optional
- String
*→ the color map to use.*
**Output**
2D Histogram
---
**Visualising world population per age**
Let's say we have a data frame `world_population` that contains information on the world's population split by age (`Age`) and the count of people in millions(`Count in Millions`) in that age group.
```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Creating sample data
np.random.seed(0)
age = np.random.randint(0,100,500)
count_in_millions = np.random.randint(1,500,500)

world_population = pd.DataFrame({"Age":age, "Count in Millions":count_in_millions})

# Display the first few rows of data
world_population.head()

   Age  Count in Millions
0   44                 47
1   47                214
2   64                218
3   67                115
4   67                389
```
---
We can now create a 2D histogram to visualize this data:
```python
# Set up the figure and axis
fig, ax = plt.subplots(figsize=(8,8))

# Prepare the data
x = world_population["Age"]
y = world_population["Count in Millions"]

# Create the histogram
counts, xedges, yedges, im = ax.hist2d(x, y, bins=(20,20), cmap='viridis', cmin=1)

# Add color bar for reference
fig.colorbar(im, ax=ax)

# Show the plot
plt.show()
```
![Histogram showing the distribution of a random world population per age group.](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/08d0cdb1-758e-48a2-908d-22e7e4d71cf6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46636FNQ5QI%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T222700Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJGMEQCIAXiuKIF6UBcSPNPegQUXv5wqc1jewa3EKWI5sMKuGc7AiBnsxUPQLYMaMVFAfh11NgjTCjsung5NtrSSNDtG%2BUw9ir%2FAwgoEAAaDDYzNzQyMzE4MzgwNSIMx4y3vxNza3iTlQO0KtwDweUaT35gV53ZEBoOG8LM%2Fexu8aARbsiq%2FX69G6NlrpmZCkU7ESKZZnxmfVz1DrwWwhMD7dINCCDRtNEzg2Y%2F7FLXsAWUTrqe0bdA0ByE4YsVcLLwqw1JeTH2FscumIYX6dwNNqSOpDXVSjyy7hoKpb%2BgTaQb79hNooFu%2FeyBUU5P1zcQuw%2F8pQahkkAr1X1i7xX%2FVZULW9Wtxz3ApWGA8v7vGbjH8wC32jRquv1ARqAIqewXc9NegpCG%2BbE7XGX9%2Bpja4GfkIT%2B0DiekwkDxUU8QTvTGDa4cIHPlizOk9pXwNQyEx%2BDgjYEXsdzrQEJl93IUENQ%2F%2FSYG7w1WKmEoLB3qps6WNWqxD7CCdUkEPIdk0xJ5ZFh33TSFOvvkKhWResMPJohRPp9idpsKj2JnRna74sMtcRK2QJmCSpLyLpxpG6VlPNv6K0b2MwFFnvTYMSfuetR5tt4dNN5IZVv9h4O6LHaV9jSTy2pUbJ7cHt2Q9NFWzW8twcJ5vRuNNqke6nB2ChmiavR9giCueO2c4DI10YCXvglA4zqvqxYIEpj2WVgafhPhZXN3zWYMaW3L3zsBvGoxHyFDo1sMRQOU9IQ8z0Mg%2BUo4BcJHP%2FtpEIhEQzx%2F5FOuh5cPz2Ywqs73yQY6pgEStr%2FsIdvIaDBCus4Xpd21ShPt4Ga1e%2BU92emEDX8PMQqYb2gOa%2FwR5A%2FDx8V5X5iNanuxIZH6%2FyYaUl2%2BzSVj9wYtrORiMgq1R2bsY8YjbgcnmjVZhfAKaXSpn1tAWEHmnfK5YsKKxjM9BwoSm5hLpe5HyYg8yjNh%2FFohNjpLr8gP9CdU1EsYZ71Cq40w6wBqI0OqjY2Ugq9Eouzm%2BiUM5OPkTLkB&X-Amz-Signature=04182a937038182ae04ea8ea9e5363b69b1ff92c587d1340f0a7a22ec1b71ce0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
As you can see, we obtain a 2D histogram with Y-axis representing "Count in Millions", X-axis representing "Age", and the color intensity representing the number of observations (counts) in the bin. The color bar to the right indicates the relationship between color intensity and count.
Note: `cmin=1` is used to ignore bins where the count is less than 1.
---
## [`.scatter()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.boxplot.html)
---
**Syntax**
With this function we can generate a scatter plot that visualizes the datapoints along two dimensions.
`<< axes >>.scatter(<< x_data >>, << y_data >>)`
**Input**
`<< x_data >>`: required
- Numpy Array **OR** List
*→ x-values for scatter plot*
`<< y_data >>`: required
- Numpy Array **OR** List
*→ y-values for scatter plot*
**Output**
Scatterplot
---
**Visualizing world population distribution by age groups**
Let’s assume we have fictive data on the world population distribution by age groups and we want to create a scatter plot to visualize this.
In this case, our X-axis will represent the age groups and Y- axis will be the corresponding population count.
---
Firstly, we need to define our x-values and y_values. If we have them in a list, pandas series or numpy array, it will work.
```python
x_age_group = ['0-9', '10-19', '20-29', '30-39', '40-49', '50-59', '60-69', '70-79', '80+']
y_population = [1400000000, 1200000000, 1000000000, 800000000, 700000000, 600000000, 500000000, 300000000, 100000000]
```
Next, we can create our scatter plot.
```python
import matplotlib.pyplot as plt

# Create empty figure and axes
fig, ax = plt.subplots(figsize=(8,5))

# Plot the data
ax.scatter(x_age_group, y_population, s=70, c='b', marker='o', alpha=.7, edgecolors='k', label='population by age group')

# Add a legend tot he Axes
ax.legend()

# Display the plot
plt.show()
```
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/d6de8b52-c25f-4496-a907-727cea1d4e37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46645LQNNLH%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T222701Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQDJ8RHmH%2FT14Gmfns6p2RmAp8yhBemiqr49PMwYNTnpNQIhALxJyAsJhGKJNAUQqDFmue%2Bj2Argk72Pge8eXBmfAbHkKv8DCCcQABoMNjM3NDIzMTgzODA1IgyGOUnCRF57EV0%2Fscsq3APFRoZwMlkNuTaZQjFdcgZlUzxZ96kyr02spkP4FZTItum0a6e1JBRuaTWA602J4YO23s9max%2FsQAKSO09UlKmKxhnn0SxQCwsJZd8nOYC3%2BsQMkRrM3ypUbtXkqwFHalBE3oP2ni1H9vuoHNdeLxSZFj5Cyk0uFZYhMewY%2FTVWw5fAEZ8r5VoP9T420c%2FWcFn4bX0%2BD2pZPVzVaJezH%2Bik7UPg4y3AQighy7Kgr57wpj1T36VWrTC2GU2y75iZdnCPFmRh1tZ4lYZE3XUx5dMxe5ProytRCiJJGzpIysx7FEopRhXMKQXxrBVNJu3VY%2Fb36JTkPA%2Fm41JVwezn9DU7SRpJJeX5DxwDEtTHryFq6M%2BoTgOmpij6ktSFqUR992a%2Be8k0wAh3jYunr3QT6dj%2BzLNDEuQJhn%2ByUwWwXPwzSn1F0zV2AEdZbB5CEgyaFNzcUn9a9U5m0dQw1K0aoOtBSBWeTj0SnpxOuKpzU20nXyD00fPemu6u2o10V58mYn0%2F6w5eXELa5Kvnd6huzcgID6A012D7uomL9ZQAaT6kpB1DNcm9rQXp7doPGH5rGAeVxDnDCAeOXw4dTRAXcxIMiFH4tqPvkENlZy5Q7PpaiVFl5NXilj9fWRQ4RzDFzvfJBjqkAUrkQZtGgSk1w2RP%2F3FC0PYSuun%2BLQXIEDdHGtN1eZgaQqW83TYyrzuw1ocqjMMon7xi8%2BmOp2KppE123Das3Ou1BxigNS7885jdzB%2F1pB6sOS94fQqa3%2BOUegG6JYn0ysbyGy8O730cPArkKdGghjGqtsYyQSPQwvVjsAb8k0BkryM%2BUZH5cRlOeZksYDAshh9IFYFhGIUjAMEBWsDc6avAoBpU&X-Amz-Signature=e4094fd8304598d7a22e53ca60f13813af4d888f771258d3517687f0a027b583&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
As you can see, the scatter plot gives us a clear idea about how the world population is distributed among different age groups.
---
## [`.legend()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html)
---
**Syntax**
With this function we can add a legend to our figure.
`<< axes >>.legend()`
**Input**
None
**Output**
None
---
**Add legend to lineplot**
If we want to add a legend to our plot to display the player name, we can simply call [`.legend()`](/10c38918e9a84ef79c8040d2fba85e2e#6be4dc7a33704989af7042858aefaa9e).
```python
ax.legend()
```
![Simple lineplot including now a legend](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/11e6fffc-6f30-4a62-896c-1943395ce3e5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZKBPHDSM%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T222703Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIQCKAM2Z%2BQp%2B7j9pIcoDSHU5Q0dTn4Pd%2B7tdLx%2BR5rHo4AIga1W6beN7AIR%2BwJkHW6Qjr7nc2rkOtPdXUbKNRwql8m8q%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDIXoa1TfnsfCs5GEHircA1FPi08d4KVO%2BcYp6tt1s2RankRGtXAsa6xPiFC8PZ30Ef%2BZ6SUFMU644VMfGgygY3X8zTJ9yBGMDrBAQ7ffzGLUVCaGQCbOMwhECNTFOVwVl%2F32dGYlHlGSDaqAd7%2F%2BZeFk2VmtIVzsXdncSt76pypD0ICDD6w6G82H2%2Fx03UN9mCwSh%2F6l1jTS8nU87oyQvvjpg1oC34nE0Ike7cLns%2BqjNiPIstRokOqXp0G2RMn3fqT78g98K%2B8VvOL0ldQ2%2BUaW3cwmapF5Fosys0%2BWePsOcwlERLcOKEK%2BL4v44Odo26MqBlLVBB%2FKe4CiwFYvsxJg5MnOEWqBjPjaxTZp5WZwgM9rKnkzQ5%2FcxsgG8p9nS3JQlvd8x5pB1Fxcx8UQ6%2BxT39F%2BjRNVaqYd%2F1f1tuHg4ZFrK0ZXIEU5EvLDM4XFvbvivUF6fXG4ZYy8m882Mt%2BiC71a2vT%2F%2FW1xP4g31zmFgI0xBxhqypfbaJjO2NSu%2F4X5vW30enNYPJgO6Jw5L8079VbcwJOOkQGcBW04lEskpbVDd8r82%2F6UXOgOJzUIlrBTo7M%2FsU5gg5rKJx5RKfDhCvK6%2F51idFj%2Fq4PvYk%2FCBXpphuGSt84Exs0Kj9x0B3WMxcun6kFsfR6aMM%2FO98kGOqUBbvfwM%2BsZpzw3sdrqEK618fnv29VrQOOt0n5hna4yoB97hMEFDbVTQpIrsYQF8%2Fi2w89zupxiIbUlLzTzZhp8Gs7dSnDxzvr0ObCNrM%2BpEjkWolcb7R9TNtnuwyT2POiCTYVqYGMzhyg8UdF0bOp%2FVy8oijC20yUVgewxHn2ennoADuCluXJBM%2BMYrVayxuNTshEs17MRazOVIGwRaxHeb8S6fPsO&X-Amz-Signature=976749a1d66f9e488ecdc5fb2122d6847db2c90a1a4ae12eca69b0b99f3c9c1c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
---
## [`.set_xticks()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xticks.html#matplotlib-axes-axes-set-xticks)
---
**Syntax**
With this function we can se the x-ticks on the x-axis.
`<< axes >>.set_xticks(<< tick_positions >>)`
**Input**
`<< tick_positions >>` : required
- List of Floats  
*→ the positions on the x-axis where the labels should be set*
**Output**
None
---
First, we need to create a list consisting of the x-axis locations, where the tick labels should be set. We can see that the bars are placed at locations 0 to 4. Thus, we simply create a list consisting of these integer numbers. 
```python
tick_positions = list(range(5))

tick_positions
[0, 1, 2, 3, 4]
```
Now we can set the xticks.
```python
ax.set_xticks(tick_positions)
```
---
## [`.set_xticklabels()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html)
---
**Syntax**
With this function we can modify the labels of the xticks.
`<< axes >>.set_xticklabels(<< tick_labels >>, << rotation >>)`
**Input**
`<< tick_labels >>` : required
- List of Strings  
*→ the new labels of the x-ticks*
`<< rotation >>` : optional
- Integer
*→ how many degrees the labels should be rotated*
**Output**
None
---
**Set tick labels in figure**
Let’s assume that in our bar chart plot we want to know which bar belongs to which player. For this reason, we want to set the player names as the xtick labels.
![Barchart with missing xtick labels](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/1a13fe42-7f7a-4543-924b-5a3ab3aaab00/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662CGJ2LTH%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T222709Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIQD%2B3Se3KRwZ%2BaSouoR9jc9rO3NgQEMex%2FoS%2Bg5QRbzOsgIgZQN6n%2Boe%2FrORq6Pg%2BxL2Q1N5ggi5ygzb03OmC8x1PW8q%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDCjdZyvvo3o46i274SrcA4rTgt5HjHStu3eUmmJAJRrvyHS6KdIgsCZCoCjK9dzJP%2FcekFI%2F3N%2Fkg%2BqVnm4v0hGekEmGOSU9i0AGze9fX8yH3QGpsjFBTxoIbXhGIGtW5xrN3%2FG5zoJP%2FFE2pdNankivsa79ZR4pLjH3Ex9QszKdEkeeo14NszcoFGpCTDY2JkNkyTlVYWOaiAEI0F%2BLHTglmawNVSPKkfVA0Owpdi%2BLYKNXRSk7ndfyH9MnOZwmr7oHS8ckKogBn8mGJEizb6JBK2tmVifwzzHFu2u7hGytpGkH7DgZpcWiVCqnc%2BH47ZfNs5jJ7VuQi5Wmf4xdJ98445JyxCsAAUi1WRxE8kRYM08kY9wDNxjhvHyZ8NOvddnDhMv5Uv4RY1FWT%2FNy1NVONhF9k9R4S6MCGq8KA41jWWvf2jIyPgy1inMIHZ7C%2FmRFpDI2kWCLtE%2Fzf0DWb0DhImwfC4biOLwcnqn8GQsXM0K0vvCnbM7scqfFBccrtfTrDn49qbg4F7zte4DdHoE5nDLGbhMjgHgz6EVR8u8%2FRELNUTgAj5lyixG%2FdpA40gPxIZ1hnchH7gBVES9yhlsknTAHbm1Gq7RyP0Cyb4FJnCN2PQGZjJLK%2Bx4ax8hGx8NIla1ilWN%2Bf%2BEpMI%2FO98kGOqUBEVH3nVAKOyYxejf7X4Z0g6U6sbuv%2FFp8GyY%2F6cpi4gCS2j050vw4rghWHVdSwd0vx9Ym5YKO8JlgMUL0yOKXW2dFh6ANvXLl0FM0EZOeV%2B2Jx2u8%2BKLpWwhPQIZzGlHLeOw%2FWLX8IR%2FeVQZ9NbW5HlfYAsMr7y2EyuU2ngRkD3bvctnvi2fvfGw17EsOWHXPBxh7LX4TlXGn1d%2B4tOWFviDV7hnc&X-Amz-Signature=51f4ad5c36294bcf0cad0622442424d34f61b5456d48c8b63d1a5e16286fe14d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
First, we need to extract the player names form the dataframe `top5_players`. 
```python
tick_labels = top5_players['Players'].values.tolist()

tick_labels
['Jamie Vardy',
 'Danny Ings',
 'Pierre-Emerick Aubameyang',
 'Raheem Shaquille Sterling',
 'Mohamed Salah Ghaly']
```
Now we can modify the tick labels.
```python
ax.set_xticklabels(tick_labels, rotation=20)
```
![Bar chart with the player names as tick labels](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/bc24ae12-1eae-44df-98ed-208b5384b886/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662CGJ2LTH%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T222709Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIQD%2B3Se3KRwZ%2BaSouoR9jc9rO3NgQEMex%2FoS%2Bg5QRbzOsgIgZQN6n%2Boe%2FrORq6Pg%2BxL2Q1N5ggi5ygzb03OmC8x1PW8q%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDCjdZyvvo3o46i274SrcA4rTgt5HjHStu3eUmmJAJRrvyHS6KdIgsCZCoCjK9dzJP%2FcekFI%2F3N%2Fkg%2BqVnm4v0hGekEmGOSU9i0AGze9fX8yH3QGpsjFBTxoIbXhGIGtW5xrN3%2FG5zoJP%2FFE2pdNankivsa79ZR4pLjH3Ex9QszKdEkeeo14NszcoFGpCTDY2JkNkyTlVYWOaiAEI0F%2BLHTglmawNVSPKkfVA0Owpdi%2BLYKNXRSk7ndfyH9MnOZwmr7oHS8ckKogBn8mGJEizb6JBK2tmVifwzzHFu2u7hGytpGkH7DgZpcWiVCqnc%2BH47ZfNs5jJ7VuQi5Wmf4xdJ98445JyxCsAAUi1WRxE8kRYM08kY9wDNxjhvHyZ8NOvddnDhMv5Uv4RY1FWT%2FNy1NVONhF9k9R4S6MCGq8KA41jWWvf2jIyPgy1inMIHZ7C%2FmRFpDI2kWCLtE%2Fzf0DWb0DhImwfC4biOLwcnqn8GQsXM0K0vvCnbM7scqfFBccrtfTrDn49qbg4F7zte4DdHoE5nDLGbhMjgHgz6EVR8u8%2FRELNUTgAj5lyixG%2FdpA40gPxIZ1hnchH7gBVES9yhlsknTAHbm1Gq7RyP0Cyb4FJnCN2PQGZjJLK%2Bx4ax8hGx8NIla1ilWN%2Bf%2BEpMI%2FO98kGOqUBEVH3nVAKOyYxejf7X4Z0g6U6sbuv%2FFp8GyY%2F6cpi4gCS2j050vw4rghWHVdSwd0vx9Ym5YKO8JlgMUL0yOKXW2dFh6ANvXLl0FM0EZOeV%2B2Jx2u8%2BKLpWwhPQIZzGlHLeOw%2FWLX8IR%2FeVQZ9NbW5HlfYAsMr7y2EyuU2ngRkD3bvctnvi2fvfGw17EsOWHXPBxh7LX4TlXGn1d%2B4tOWFviDV7hnc&X-Amz-Signature=2f67365a3b0413f27d3494aab27356be2b223b36df1306f6a4e5cbefac961564&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
---
## [`.text()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html)
---
**Syntax**
With this function we can insert a text into the axes.
`<< axes >>.text(<< x_position >>, << y_position >>, << text >>)`
**Input**
`<< x_position >>` : required
- Float  
*→ the position on the x-axis where the text should be inserted*
`<< y_position >>` : required
- Float
*→ the position on the y-axis where the text should be inserted*
`<< text >>` : required
- String
*→ the text that should be inserted in the axes*
**Output**
None
---
**Insert text in axes**
Let’s assume that in our line plot we want to mark the highest point (Shots) with the letter **‘Here is the highest point’.**
First, we need to figure out the y-position. In the [dataframe](/10c38918e9a84ef79c8040d2fba85e2e#84b746f85685409faa2112f902d32b3c) we can see that Jamie Vardy has scored 71 goals. Thus we can extract this value using [`.iloc[]`](/1867045b058343e1a66b677961515907#659a00c8972e48a992e0dcabacb0cd4f) and save it in a variable.
```python
y_position = top5_players.iloc[0, 5]

y_position
71
```
Second, we need to figure out the x-position. We can see that **Shots** is the fourth value in the lineplot.
![Values in Lineplot by number; Shots is at position 4](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/718711cf-3cce-423a-837c-c95a3d0a441b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V2ZC675S%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T222710Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJGMEQCIEoSPYxt%2FgrZFxt0HFzwGwIwIyueZfzX3Jw7fJLe%2FzplAiBR3I6p%2BS2l1UUct7PoH0%2FzU%2FU%2FEmt%2FK95Xm0M9yjgwxSr%2FAwgnEAAaDDYzNzQyMzE4MzgwNSIM9SpHexRjRf8869GuKtwDMZC3PIaDbILcqAFBFzHhh8M7l%2BoS%2BpRfSh5jyD6vb7TANtY2v%2FK%2FvGfvUfmkPOpDXJ3mCcpKWWuFfisGbXbXAECMBhYn0x%2BsQnlNBnEITrUOXMH0KQcuDqDgO9%2FvEe5SUxgir9od6eZwV8el2vv6HUvsIDd5kAsqt%2B9B1afiKlI%2BR8kmncGp%2BO0hS4W76%2B%2B3qwznoPleaRd%2F1MTb7QjgY0hwzYMvEMyeqXSniNZFBCvGLk%2FvUj7nwAPxqmGSuTBFKtnecUvyqVYGu9ZVkZZwXQdXePdSALL9mQPpaOaBXRgcRa%2BwnGUqOsGhW4flxPIr8lyidilKfTkOf7%2BznIv7qbaLZcdKfBQHT2H0hUHVGbvAEhhWHcV%2BlMgKQl%2FalF0%2FPpxI%2B04RqM0SHUHSaeiaOYb%2F2IiVliUOQRjTwNxijCPBZsgx72McaNjY74P5dVrX333W%2Bf1DfAS5%2BzyekQcVJSVAFPxbZIcXCtjxGgVoD3mgfvMvhQtKLrQr%2F6AVoH5tibycZbouJuQ6l7sLh98hQyhajKVc74vuW%2BFkxVBsDjZrzXBpPDb5XttD2tPnV0IgFL6P2Yxi81TR%2F7mS1%2BOi4S%2BFppWmA3GrEoEaBREggjbUUPHxRHClxedYQXQw7833yQY6pgEjIUZQqdCpktRLbn3%2B9luzJjItpacyfrJ4kw0CaLf%2BtTssVB72KYOFDYiUGNvGTSnBPuvkGAp%2F6M8FZKmjH71d%2BUW4vVWh0qVunNq06MRWReOcc6Hre%2BMIO%2FrPKxAGbzSJZvzm7VHQBIldoWbFPOcVk3oyPEfcVFHjoAUJnl6nIe0ygmiBHyfhJo3sj8%2BzbqXDjWe0OsGThHr%2BmDastv1XXGGM9voD&X-Amz-Signature=435fd29f6a237af2b2d5877eee01be535d9d5f48949710def41d1006bfaebb75&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
Thus, the x-position of the text we want to insert is **4**.
Now, as we know the y-position and x-position we can insert the text **‘Here is the highest point’ **in the Lineplot.
```python
fig, ax = plt.subplots(figsize=(10, 8))

ax.plot(x_data, y_data, label=player_name)

ax.text(4, 71, 'Here is the highest point')

ax.legend(loc='upper left')
```
![Updated Lineplot with text at highest point](https://prod-files-secure.s3.us-west-2.amazonaws.com/85904fa9-813f-4181-815c-7a9adaee3156/c1abbd6e-7d38-466e-8873-c4b3a62f46ac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V2ZC675S%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T222710Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJGMEQCIEoSPYxt%2FgrZFxt0HFzwGwIwIyueZfzX3Jw7fJLe%2FzplAiBR3I6p%2BS2l1UUct7PoH0%2FzU%2FU%2FEmt%2FK95Xm0M9yjgwxSr%2FAwgnEAAaDDYzNzQyMzE4MzgwNSIM9SpHexRjRf8869GuKtwDMZC3PIaDbILcqAFBFzHhh8M7l%2BoS%2BpRfSh5jyD6vb7TANtY2v%2FK%2FvGfvUfmkPOpDXJ3mCcpKWWuFfisGbXbXAECMBhYn0x%2BsQnlNBnEITrUOXMH0KQcuDqDgO9%2FvEe5SUxgir9od6eZwV8el2vv6HUvsIDd5kAsqt%2B9B1afiKlI%2BR8kmncGp%2BO0hS4W76%2B%2B3qwznoPleaRd%2F1MTb7QjgY0hwzYMvEMyeqXSniNZFBCvGLk%2FvUj7nwAPxqmGSuTBFKtnecUvyqVYGu9ZVkZZwXQdXePdSALL9mQPpaOaBXRgcRa%2BwnGUqOsGhW4flxPIr8lyidilKfTkOf7%2BznIv7qbaLZcdKfBQHT2H0hUHVGbvAEhhWHcV%2BlMgKQl%2FalF0%2FPpxI%2B04RqM0SHUHSaeiaOYb%2F2IiVliUOQRjTwNxijCPBZsgx72McaNjY74P5dVrX333W%2Bf1DfAS5%2BzyekQcVJSVAFPxbZIcXCtjxGgVoD3mgfvMvhQtKLrQr%2F6AVoH5tibycZbouJuQ6l7sLh98hQyhajKVc74vuW%2BFkxVBsDjZrzXBpPDb5XttD2tPnV0IgFL6P2Yxi81TR%2F7mS1%2BOi4S%2BFppWmA3GrEoEaBREggjbUUPHxRHClxedYQXQw7833yQY6pgEjIUZQqdCpktRLbn3%2B9luzJjItpacyfrJ4kw0CaLf%2BtTssVB72KYOFDYiUGNvGTSnBPuvkGAp%2F6M8FZKmjH71d%2BUW4vVWh0qVunNq06MRWReOcc6Hre%2BMIO%2FrPKxAGbzSJZvzm7VHQBIldoWbFPOcVk3oyPEfcVFHjoAUJnl6nIe0ygmiBHyfhJo3sj8%2BzbqXDjWe0OsGThHr%2BmDastv1XXGGM9voD&X-Amz-Signature=28b233e0d894686c7dcfa616841ab70bffa9957b704cfa9941c0d540f34a14b6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
---


