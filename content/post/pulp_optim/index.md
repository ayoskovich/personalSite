---
title: Optimization in pulp
date: 2022-02-17
summary: 'other notes'
draft: true
---

```python
from pulp import *

x = LpVariable("x", 0, 3)
y = LpVariable("y", 0, 1)

prob = LpProblem("myProblem", const.LpMinimize)

prob += x + y <= 2
prob += -4 * x + y

status = prob.solve(PULP_CBC_CMD(msg=0))

print(f'Status: {const.LpStatus[status]}')
print(f'Objective function at optimal: {value(prob.objective)}')

print('Variables values:')
for var in prob.variables():
    print(f'{var} = {var.varValue}')

```

    Status: Optimal



```python
!jupyter nbconvert --to markdown index.ipynb
```

    [NbConvertApp] Converting notebook index.ipynb to markdown
    [NbConvertApp] Writing 314 bytes to index.md



```python

```
