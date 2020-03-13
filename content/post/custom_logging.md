---
title: Custom Logging in Python
author: ''
date: '2020-03-05'
slug: applying-complicated-conditionals-to-pandas-dataframes
categories:
  - python
tags: []
---

&emsp; When working with data, there are a lot of things I need to keep track of in my head.

- How many observations do I have in total?
- I just filtered some out, how many did I throw out?
- Am I aggregating before or after I filter?
- Where should I add this chunk of code?

&emsp; In order to keep track of these questions when working in a jupyter notebook I end up having *tons* of cells that look like this:

```
df.head()
```

&emsp; or 

```
df.shape
```

&emsp; By using decorators and the `.pipe` method I can develop an analysis path that will give me customized output. See the jupyter notebook <a href="https://nbviewer.jupyter.org/github/ayoskovich/personalSite/blob/master/pyNotebooks/logging.ipynb?flush_cache=True" target="_blank">here</a>.