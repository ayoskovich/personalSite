---
title: Peter Kennedy Doesn't Think Undergraduates Understand Sampling Distributions
author: ''
date: '2020-03-03'
slug: peter-kennedy-doesn-t-think-undergraduates-understand-sampling-distributions
categories: []
tags: []
---


&emsp; In May of 1998, Peter Kennedy wrote a paper in the American Economic Review discussing teaching undergraduate econometrics. In it, he claims that most students don’t understand sampling distributions and puts forth reasons for this thought. In the paper he emphasizes the importance of simulations and suggests a simple one. I’ll be working through his example using R. Here is his suggested example:

>  - Draw 50 x values from a uniform distribution between 3 and 12.
>  - Draw 50 z values from a standard normal distribution.
>  - Compute 50 w values as 4 - 3x + 9z.
>  - Draw 50 e values from a standard normal distribution.
>  - Compute 50 y values as 2 + 3x + 4w + 5e.
>  - Regress y on x and save the x slope coefficient estimate blI
>  - Regress y on x and w and save the x slope coefficient estimate bbl.
>  - Repeat this procedure from (d) to get 1,000 b and bb values.
>  - Compute the averages of these sets of 1,000 values to get B and BB, respectively.
>  - Compute the variances of these sets of 1,000 values to get VB and VBB, respectively. 
 
> Should B or BB be closer to 3? Should VB or VBB be closer to 0?


&emsp; Clearly B is going to be closer to 3 and have a lower variance. By only regressing y on x, we aren’t capturing the effect w has on it. We’re missing a variable and our estimates will be all over the place. I also performed this simulation in R, the results are summarized below:


| *Model* | *Mean*  | *Variance* |
|-------|-------|----------|
| A     | -9.02 | 4.19     |
| B     | 3     | 0.14     |

