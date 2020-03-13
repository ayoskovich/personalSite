---
title: Generating points with a specific correlation
author: ''
date: '2020-03-05'
slug: generating-points-with-a-specific-correlation
categories: []
tags: []
draft: true
---

Sometimes when playing around with statistical techniques, I'd like to generate some data that is correlated. How might I do this? The answer is relatively simple but requires a tad bit of linear algebra.

First, we'll sample from a bivariate normal distribution.

Then, we'll rotate the data points to our specified correlation.

See here:

http://www.acooke.org/random.pdf