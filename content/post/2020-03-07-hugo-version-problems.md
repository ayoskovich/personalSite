---
title: HUGO_VERSION problems
author: ''
date: '2020-03-07'
slug: hugo-version-problems
categories:
  - blogdown
tags: []
---


<<<<<<< HEAD
&emsp; In order to build this site, I use [blogdown](https://bookdown.org/yihui/blogdown/) and then I deploy it with [Netlify](https://www.netlify.com/). The nice thing about netlify is that I can have the site as a repo on GitHub, and every time I push changes, the site will update. However, the other day one of my site builds kept failing. This was due to the Hugo version being different on my local machine than the one that is on Netlify.
=======
&emsp; In order to build this site, I use [blogdown](word) and then I deploy it with [Netlify](https://www.netlify.com/). The nice thing about netlify is that I can have the site as a repo on GitHub, and every time I push changes, the site will update. However, the other day one of my site builds kept failing. This was due to the Hugo version being different on my local machine than the one that is on Netlify.
>>>>>>> 295d8f2b0d6215a8b49ea2fa60f8c11c981f8fe7

&emsp; Luckily, and probably for the first time in my entire life, I found the answer in the first place I looked! If you are ever [getting an error with exit code: 255](https://docs.netlify.com/configure-builds/common-configurations/#hugo), set the `HUGO_VERSION` environment variable (on Netlify) to the Hugo version you have installed locally. It's pretty easy to check, in Rstudio just:

```
blogdown::hugo_version()
```

&emsp; This should output a string (mine was ‘0.60.1’), and that string should be the environment variable. More info on setting the evironment variable [here](https://docs.netlify.com/configure-builds/environment-variables/)
