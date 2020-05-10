---
title: Adventures in creating fake data
date: 2020-04-09
summary: 'and some insights into a larger idea'
draft: true
---
- Main point
    - Abstracting tasks (or partitioning work into 'context specific' and general can be helpful)
- Summary
    - Creating fake data from known rules can be a tad challenging
    - In the development process, "I'm waiting for data" shouldn't stop someone from continuing
    - Conditional probability can be dealt with
- Motivation 
    - Worked on a project where we were waiting on someone to give us data
    - We had given them a sheet to fill out, ensuring the data was in an easy to digest format (good consulting skill)


```python
import pandas as pd
import numpy as np

SEATS = ['silk', 'expression']
AMOUNTS = [10, 20]

df = pd.DataFrame({
    'name':np.repeat(SEATS, len(AMOUNTS)),
    'size':np.tile(AMOUNTS, len(SEATS))
})
```

*comment about np.repeat vs np.tile here*

Now, if I wanted to add random prices, they would obviously have a distribution. However, let's say I just know that the 20 size will be around \$5 more, that is also a distribution.


```python
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name</th>
      <th>size</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>silk</td>
      <td>10</td>
    </tr>
    <tr>
      <th>1</th>
      <td>silk</td>
      <td>20</td>
    </tr>
    <tr>
      <th>2</th>
      <td>expression</td>
      <td>10</td>
    </tr>
    <tr>
      <th>3</th>
      <td>expression</td>
      <td>20</td>
    </tr>
  </tbody>
</table>
</div>




```python
def addPrices(df):
    """ Conditionally add prices to the dataframe.
    
    df (pd.DataFrame): Input data
    pct_mk (float): Percentage markup for the 20 size.
    """
    # 
df.apply(lambda x: x['size'] + 10, axis=1)
```




    0    20
    1    30
    2    20
    3    30
    dtype: int64


