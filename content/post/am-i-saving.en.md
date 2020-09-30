---
title: Am I Saving?
author: ''
date: '2020-09-30'
slug: am-i-saving
categories: []
tags: []
subtitle: ''
summary: 'And other consumer thoughts'
authors: []
lastmod: '2020-09-30T14:25:24-04:00'
featured: no
image:
  caption: ''
  focal_point: ''
  preview_only: no
projects: []
draft: true
---

I've done a bit more planning on my most recent project than I have in the past. I think it's easy to get caught in a rut where the projects you work on just reuse the same technologies or techniques. So one of my goals with my current project is to challenge myself while learning something new.

In this case, it's deploying a bokeh application to the web using heroku. I've got the deployment figured out, just need to edit the DNS records so that [amisaving.herokuapp.com](https://amisaving.herokuapp.com/main) redirects to [amisaving.com](http://amisaving.com/).

On herkou I enabled auto-deployment from `master` which means that every time I push changes to the `master` branch the application is redeployed. I also created a `dev` branch, so I can test things locally and then merge with `master` when I'm ready to update the live site.

---

### Vim tip...

Use `&` while in normal mode to repeat the last substitution on the current line.
