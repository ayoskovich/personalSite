---
title: Effective .transform in python
date: 2019-09-01
summary: 'Want to remerge a summary statistic back into a table? Stay away from `pd.merge`...'
---

Merging summary statistics back into a table is quite a common thing to do. At first glance, a solution to this problem is to simply compute the statistics in a new table and merge the table back in. However, with `pandas` we don't have to do that.


```python
import pandas as pd
import numpy as np

np.random.seed(124)
df = pd.DataFrame({
    'group':np.random.choice(['a', 'b'], 5),
    'x':np.random.randint(100, 200, 5)
}).sort_values(by='group'); df
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
      <th>group</th>
      <th>x</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>a</td>
      <td>141</td>
    </tr>
    <tr>
      <th>1</th>
      <td>a</td>
      <td>164</td>
    </tr>
    <tr>
      <th>4</th>
      <td>a</td>
      <td>178</td>
    </tr>
    <tr>
      <th>2</th>
      <td>b</td>
      <td>120</td>
    </tr>
    <tr>
      <th>3</th>
      <td>b</td>
      <td>128</td>
    </tr>
  </tbody>
</table>
</div>



Here I've got some rows that having a grouping column called `group`, and I'd like to calculate the sum of `x` within each group and integrate it into my table.


```python
df['g_sum'] = df.groupby('group')['x'].transform(np.sum); df
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
      <th>group</th>
      <th>x</th>
      <th>g_sum</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>a</td>
      <td>141</td>
      <td>483</td>
    </tr>
    <tr>
      <th>1</th>
      <td>a</td>
      <td>164</td>
      <td>483</td>
    </tr>
    <tr>
      <th>4</th>
      <td>a</td>
      <td>178</td>
      <td>483</td>
    </tr>
    <tr>
      <th>2</th>
      <td>b</td>
      <td>120</td>
      <td>248</td>
    </tr>
    <tr>
      <th>3</th>
      <td>b</td>
      <td>128</td>
      <td>248</td>
    </tr>
  </tbody>
</table>
</div>



A key idea is that `.transform` will apply its function argument to the dataframe and **return a result that is the same size as the input frame.**

### We can also use `.transform` with a user defined function


```python
def max_minus_one(col):
    """ Get the max - 1 of a list"""
    return np.max(col) - 1

df['udf'] = df.groupby('group')['x'].transform(max_minus_one); df
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
      <th>group</th>
      <th>x</th>
      <th>g_sum</th>
      <th>udf</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>a</td>
      <td>141</td>
      <td>483</td>
      <td>177</td>
    </tr>
    <tr>
      <th>1</th>
      <td>a</td>
      <td>164</td>
      <td>483</td>
      <td>177</td>
    </tr>
    <tr>
      <th>4</th>
      <td>a</td>
      <td>178</td>
      <td>483</td>
      <td>177</td>
    </tr>
    <tr>
      <th>2</th>
      <td>b</td>
      <td>120</td>
      <td>248</td>
      <td>127</td>
    </tr>
    <tr>
      <th>3</th>
      <td>b</td>
      <td>128</td>
      <td>248</td>
      <td>127</td>
    </tr>
  </tbody>
</table>
</div>



### ...and even lambda functions


```python
df['use_lam'] = df.groupby('group')['x'].transform(lambda x: np.max(x) - 1); df
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
      <th>group</th>
      <th>x</th>
      <th>g_sum</th>
      <th>udf</th>
      <th>use_lam</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>a</td>
      <td>141</td>
      <td>483</td>
      <td>177</td>
      <td>177</td>
    </tr>
    <tr>
      <th>1</th>
      <td>a</td>
      <td>164</td>
      <td>483</td>
      <td>177</td>
      <td>177</td>
    </tr>
    <tr>
      <th>4</th>
      <td>a</td>
      <td>178</td>
      <td>483</td>
      <td>177</td>
      <td>177</td>
    </tr>
    <tr>
      <th>2</th>
      <td>b</td>
      <td>120</td>
      <td>248</td>
      <td>127</td>
      <td>127</td>
    </tr>
    <tr>
      <th>3</th>
      <td>b</td>
      <td>128</td>
      <td>248</td>
      <td>127</td>
      <td>127</td>
    </tr>
  </tbody>
</table>
</div>


