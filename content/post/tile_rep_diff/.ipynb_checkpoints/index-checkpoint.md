---
title: Comparing np.tile vs np.repeat
date: 2020-04-09
summary: 'There are a couple different ways to repeat a list of items.'
draft: true
---
I've recently been sharpening my fake data creation skills. Mainly because I've been in a couple situations where I've needed to develop things but real data was not available. `numpy` is full of great functions to make this a streamlined process and I'm going to talk through the `.tile` and `.repeat` functions. Let's get some context for the data I'm going to fakify.

> We've got some data that tracks the different quantity options of different types of product.

For example, we can sell different types of chairs in quantities of 10 and 20.


```python
import pandas as pd
import numpy as np
pd.DataFrame({
    'name':np.repeat(['silk', 'expression'], 2),
    'size':np.tile([10, 20], 2)
})
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
      <td>0</td>
      <td>silk</td>
      <td>10</td>
    </tr>
    <tr>
      <td>1</td>
      <td>silk</td>
      <td>20</td>
    </tr>
    <tr>
      <td>2</td>
      <td>expression</td>
      <td>10</td>
    </tr>
    <tr>
      <td>3</td>
      <td>expression</td>
      <td>20</td>
    </tr>
  </tbody>
</table>
</div>



Here is a really quick demonstration of the differences of these 2 functions. `.repeat` will element-wise repeat each value, while `.tile` will repeat the entire sequence that many times. Very helpful! Let's extend this a tad to get something we can play around with. If we really think about this here, we need to repeat the names (unique vals) times, and we need to tile the values (unique names) times.


```python
names = ['silk', 'expression']
vals = [10, 20]

pd.DataFrame({
    'name':np.repeat(names, len(vals)),
    'size':np.tile(vals, len(names))
})
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
      <td>0</td>
      <td>silk</td>
      <td>10</td>
    </tr>
    <tr>
      <td>1</td>
      <td>silk</td>
      <td>20</td>
    </tr>
    <tr>
      <td>2</td>
      <td>expression</td>
      <td>10</td>
    </tr>
    <tr>
      <td>3</td>
      <td>expression</td>
      <td>20</td>
    </tr>
  </tbody>
</table>
</div>



By adding `len(vals)` and `len(names)`, if I want to create another name or add a value to my list it won't require me to change anything. I'll wrap the df construction in function and prove it to you.


```python
def buildFrame(names, vals):
    """ Create a dataframe with names and values.
    
    Args:
        names (list): Some names
        vals (list): Some values
    Returns:
        pd.DataFrame: Dataframe with a record for each name and value
    """
    
    return pd.DataFrame({
        'name':np.repeat(names, len(vals)),
        'size':np.tile(vals, len(names))
    })

n1 = ['anthony', 'jim']
v1 = [10]

n2 = ['a', 'b', 'c']
v2 = [10, 20]
```


```python
buildFrame(n1, v1)
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
      <td>0</td>
      <td>anthony</td>
      <td>10</td>
    </tr>
    <tr>
      <td>1</td>
      <td>jim</td>
      <td>10</td>
    </tr>
  </tbody>
</table>
</div>




```python
buildFrame(n2, v2)
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
      <td>0</td>
      <td>a</td>
      <td>10</td>
    </tr>
    <tr>
      <td>1</td>
      <td>a</td>
      <td>20</td>
    </tr>
    <tr>
      <td>2</td>
      <td>b</td>
      <td>10</td>
    </tr>
    <tr>
      <td>3</td>
      <td>b</td>
      <td>20</td>
    </tr>
    <tr>
      <td>4</td>
      <td>c</td>
      <td>10</td>
    </tr>
    <tr>
      <td>5</td>
      <td>c</td>
      <td>20</td>
    </tr>
  </tbody>
</table>
</div>




```python

```
