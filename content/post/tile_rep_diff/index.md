---
title: Comparing np.tile vs np.repeat
date: 2020-04-09
summary: 'Interestingly enough, there isnt just one way to repeat a list.'
draft: true
---
Waiting for data can make things take a bit longer than usual. However, I don't think you should ever have that excuse. If you know the format of how the data will be formatted you can still get a lot of work done. The data wrangling / actual mechanical analysis can be completed. However, the actual interpretation cannot be done, but that's not a lot of the project. In this post I explain how to use `np.tile` and `np.repeat` in order to make fake data that help this process.

- Sometimes you wait for data
    - You can still make a lot of progress
    - There are some parts of the project that only rely on the format of the data
    - Actual interpretation cannot be done
    - Further discussion of this idea is for another post
- Creating fake data is an artform
    - I use `np.tile` and `np.repeat` in order to help this process


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


