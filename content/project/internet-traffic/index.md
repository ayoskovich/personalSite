---
date: "2020-06-10T00:00:00Z"
external_link: ""
image:
  caption: 
  focal_point: Smart
slides: example
summary: When is the best time to be on the internet?
title: Analyzing Internet Speed
url_code: "https://github.com/ayoskovich/int-traffic"
url_pdf: ""
url_slides: ""
url_video: ""

draft: true
---

## Motivation
I recently changed operating systems (Linux Lite) and like messing around with various computer related things in the command line. One thing you can do is use `cron` in order to schedule a task to run at a certain time. For example, if I wanted to change my background image every 15 minutes, this could be done using `cron`.

Me messing around with scheduled jobs, and a curiosity of how my internet speed changes over time led me to create a bash script which logged my internet specs (`ping` and `traceroute`). Using `cron` I have these specs auto generate upon reboot of my pc and run all day. Essentially I'm tracking my internet speed all the time, saving it into a file that can be easily ingested into python.

## Research Questions
I had a few main questions I wanted answers to.

1. Has my internet speed been changing over time?
2. When is my internet speed the most variable?
3. When is my internet speed the most consistent?
4. When is the best time for me to get on the internet?

I'll now define some terms that will be helpful.

- Internet speed: The time (in milliseconds) it takes to ping google.com
- The most variable / consistent: Does 3pm always have fast speeds? Or is it random? Maybe 5pm always has very high speeds?
- The best time: The time of day that has the least variable and highest average ping time. AKA the distribution of ping times is as left and as close to eachother as possible.


## Process



## Findings
## Summary

