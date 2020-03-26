---
title: Custom logging in python
date: 2019-09-01
summary: "By using decorators and the .pipe method I can create an analysis path that easily documents itself."
subtitle: "Leveraging decorators to create an informed analysis path."
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

or

```
df.shape
```

&emsp; By using decorators and the `.pipe` method I can develop an analysis path that will give me customized output and automate this tedious cycle of `.head()` and `.shape`. Let's take a look.


```python
import pandas as pd
import numpy as np
import functools

np.random.seed(5)
df = pd.DataFrame({
    'group':np.random.choice(['a', 'b', 'c'], 10),
    'x':np.random.randint(0, 10, 10),
    'y':np.random.normal(0, 10, 10)
}); df.head()
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
      <th>y</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>c</td>
      <td>0</td>
      <td>9.118736</td>
    </tr>
    <tr>
      <th>1</th>
      <td>b</td>
      <td>7</td>
      <td>-14.438416</td>
    </tr>
    <tr>
      <th>2</th>
      <td>c</td>
      <td>1</td>
      <td>18.244402</td>
    </tr>
    <tr>
      <th>3</th>
      <td>c</td>
      <td>5</td>
      <td>14.576251</td>
    </tr>
    <tr>
      <th>4</th>
      <td>a</td>
      <td>7</td>
      <td>-9.102582</td>
    </tr>
  </tbody>
</table>
</div>



### Now I'll define some processing functions.

&emsp; These functions all take the dataframe as an argument and pass the dataframe back. A few notes:

- The `pDoc` decorator is what allows me to print out the docstring and the shapes of the df at each step of the process.
- The `startPipe` function may seem useless, but I'm just using it the get the size of the dataframe at the beginning of the analysis path.


```python
def pDoc(func):
    """Print the docstring of a function."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        rv = func(*args, **kwargs)
        print("{}(): \n\t{} -> {}".format(func.__name__, func.__doc__, rv.shape))
        return rv
    return wrapper

@pDoc
def startPipe(df):
    """Begin pipeline"""
    return df

@pDoc
def filterGroups(df):
    """Remove group b from the analysis."""
    return df.query('group != "b"')

@pDoc
def capVal(df):
    """Cap the value of y at 10."""
    dat = df.copy()
    dat['y'] = dat['y'].apply(lambda x: 10 if x > 10 else x)
    return dat

@pDoc
def getMean(df):
    """Add column as mean value of x by group."""
    dat = df.copy()
    dat['g_mean'] = dat.groupby('group')['x'].transform(np.mean)
    return dat
```

&emsp; Now I'll tie all these functions together using `.pipe`.


```python
(df
    .pipe(startPipe)
    .pipe(filterGroups)
    .pipe(getMean)
    .pipe(capVal)).head()
```

    startPipe(): 
    	Begin pipeline -> (10, 3)
    filterGroups(): 
    	Remove group b from the analysis. -> (8, 3)
    getMean(): 
    	Add column as mean value of x by group. -> (8, 4)
    capVal(): 
    	Cap the value of y at 10. -> (8, 4)
    




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
      <th>y</th>
      <th>g_mean</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>c</td>
      <td>0</td>
      <td>9.118736</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>c</td>
      <td>1</td>
      <td>10.000000</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>c</td>
      <td>5</td>
      <td>10.000000</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>a</td>
      <td>7</td>
      <td>-9.102582</td>
      <td>3.5</td>
    </tr>
    <tr>
      <th>6</th>
      <td>a</td>
      <td>1</td>
      <td>-8.175481</td>
      <td>3.5</td>
    </tr>
  </tbody>
</table>
</div>



&emsp; As you can see, I get a really nice log output that shows the function name, docstring, and the shape of its output. I like this solution because it automates the really tedious process of having to ask myself "how many records did I just throw out". By using decorators, the function will always show me the shape of the output.

&emsp; Also, this solution can be really easily extended / modified. Don't like what my `pDoc` decorator is doing? It's really easy to change and customize. You're really only limited by your imagination (and python).


```python

```
