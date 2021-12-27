---
title: Kitchen Calculation Riff
date: 2021-12-27
summary: "In an jupyter notebook"
draft: true
---


```python
import pandas as pd

%run ./helpers.py
```

    foo
    




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
      <th>a</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
    </tr>
  </tbody>
</table>
</div>




```python
!jupyter nbconvert index.ipynb --to markdown
```

    [NbConvertApp] Converting notebook index.ipynb to markdown
    [NbConvertApp] Writing 972 bytes to index.md
    
