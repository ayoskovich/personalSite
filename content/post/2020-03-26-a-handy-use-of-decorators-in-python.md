---
title: A handy use of decorators in python
author: ''
date: '2020-03-04'
slug: a-handy-use-of-decorators-in-python
categories: []
tags: []
subtitle: ''
summary: 'Need a function that takes a function as its argument and returns a function? Look no further.'
authors: []
lastmod: '2020-03-26T13:51:43-04:00'
featured: no
image:
  caption: ''
  focal_point: ''
  preview_only: no
projects: []
---

&emsp; Lets say I have the following function, and for some weird reason I want it to be called twice every time I call it.

```
def foo():
  print('hello')
```

&emsp; I could solve this in a couple of different ways.

```
def foo():
  print('hello')
  print('hello')
```

```
def foo()
  print('hello')
  
foo()
foo()
```

&emsp; So...the first way is bad because if I want to extend this functionality to other funtions, I would have to copy and paste the code everywhere. Also, to switch it on and off would be a mess. The second way is even clunkier.

&emsp; This is where decorators come in handy. I can write a function, that takes in a function as an argument, and then modify that function. Here's what it looks like:

```
def doTwice(function):
  def wrapper(*args, **args):
    function()
    function()
    
  return wrapper
```

&emsp; Let's break down what's going on here.

1. The `doTwice` function first takes in another function as an argument.
2. There is a function inside of it, called `wrapper`, that simply calls `function` twice.
3. `doTwice` returns `wrapper`, which is actually a function.

&emsp; Now that we have the `doTwice` function, we'll need to use it to "decorate" the `foo` function. The syntax in python is simple.

```
@doTwice
def foo():
  print('hello')
```

&emsp; Now, every time I call `foo`, 'hello' will be printed twice, mission accomplished. The beauty of this solution is that I can now use `doTwice` on as many functions as I'd like. I would simply add `@doTwice` above each function definition.

&emsp; There are tons more helpful things you can do with decorators, and I think in the future I'll write some more posts about them. Thanks for reading!

<br>

***

**Note**: The @ syntax isn't the only way to decorate functions, the python documentation lays out another way that requires a bit more explaining.