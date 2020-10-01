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
---

Every day when I make my coffee in the morning I log how long each part of the process takes, from weighing the beans, to grinding, and finally to brewing. My goal is to estimate the how long making a cup of coffee takes me, as well as estimate time variability between different coffees. I've been logging for around a month so I have 60ish data points.

I decided that my next project would be to build a dashboard using python that would help me visualize the cost of alternatives. In other words, I could go and buy a cup of coffee at Starbucks every day and wouldn't have to spend my own time brewing it. However, by brewing it myself, the only accounting (not economic) cost is the beans themselves which from a cost perspective is much lower than the full price at Starbucks (which includes much more than simply the beans).

I've used this project to advance one of my recent goals, which has been to spend more time outside of my comfort zone, so I deployed this project using bokeh and heroku [here](https://amisaving.herokuapp.com/main). The deployment part is nearly complete, now I just need to add some buttons and polish it up. The code can be found [here](https://github.com/ayoskovich/amisaving.git) and I expect to have the dashboard complete by October 7th.

I've got the heroku app auto-deploying from a `master` branch which allows me to test things locally on a `dev` branch without letting my wild experimenting leak into on the deployed version.

I'm going to shelf the cost analysis of my coffee data for another post, as this is more of a journal entry than a report.

---

### Bonus vim tip

Press `&` while in normal mode to repeat the last substitution on the current line.
