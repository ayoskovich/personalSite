---
title: The Beauty of `.transform()`
author: ''
date: '2020-03-06'
slug: the-beauty-of-transform
categories:
  - python
tags: []
---


&emsp; Suppose I have a dataframe, and I'd like to compute the sum of a variable by group, but I'd like to keep this sum in the original table. I could solve this by computing the sum and then merging this table back into the original, but I have to either create a new dataset or overload `pd.merge` with a horrible block of code.

&emsp; Luckily, there is a function in `pandas` called `.transform()`, and here's an example of it in action.

```
df['sum'] = df.groupby('state').transform(lambda x: sum(x))
```

Read more [here](https://nbviewer.jupyter.org/github/ayoskovich/personalSite/blob/master/pyNotebooks/beautyTransform.ipynb)
