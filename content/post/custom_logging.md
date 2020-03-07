---
title: A Match Made In Heaven
author: ''
date: '2020-03-05'
slug: applying-complicated-conditionals-to-pandas-dataframes
categories:
  - python
tags: []
---

&emsp; Custom logging can be done in python using 2 main things, decorators and the .pipe() function in pandas. I recently worked on a project where there was a large amount of investigation happening. I needed an easy way to toggle filters on and off, post-process in different ways, and change the output format of a dataframe quickly. 


The main chain of events is shown below:
```
final = (
  readDat()
    .pipe(startPipe)
    .pipe(filterData, 'x > 10', 'y < 15')
    .pipe(removeOutliers, 'zScore < 1')
    .pipe(analyze, 'meanIncrease')
    .pipe(postProcess, 'long format')
)
```

The `startPipe` function looked like this:
```
@pShape
def startPipe(df):
  return df
```

And the @pShape decorator looked like this:
```
def pShape(func):
  def wrapper(*args, **kwargs):
    rv = func(*args, **kwargs)
    print(rv.shape)
    
    return rv
  return wrapper
```

&emsp; Now, as long as all the functions in the pipeline are decorated, I should get very nice output that tracks the shape of the dataframe as it goes through this analysis process. This is especially useful for filtering, as I'd like to know how many records are getting removed.

&emsp; In terms of readability, I really like this solution. It's very clear what process is happening and when, and if anyone ever needs to put some additional code somewhere, it's quick to tell where it should go.