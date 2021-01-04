---
date: "2021-01-03T00:00:00Z"
external_link: ""
image:
  caption: 
  focal_point: Smart
slides: example
summary: An interactive cost saving dashboard.
title: Am I Saving?
subtitle: View the dashboard [here](http://www.amisaving.com).
url_code: "https://github.com/ayoskovich/amisaving"
url_pdf: ""
url_slides: ""
url_video: "https://www.youtube.com/watch?v=RUKujjKL9Ys"

draft: true
---

## What is it and how do I use it?
I built an [online calculator](http://www.amisaving.com) to help people save money. After entering the costs associated with 2 spending options the calculator outputs the breakeven number of purchases between the two options. For example: 

> Before 30 purchases you save money with Option A and after 30 purchases you save money with Option B.

Here are some example decisions the calculator can help with: 

- Make coffee at home or go to starbucks. 
- Buy the unlimited pass at the carwash or pay each visit. 
- Rent a chainsaw each time you need one or just buy one.

The general assumption is that one option will have only a per consumption cost, and the other option will have a per consumption cost PLUS some sort of fixed investment.

I've made a [quick 2 minute video](https://www.youtube.com/watch?v=RUKujjKL9Ys) that explains how to use the calculator.

<hr>

## Why I Made This
I created this for a couple reasons. The first is that while I understand the math involved in comparing costs effectively, it's really clunky and I lose personal efficiency points when I need to manually do algebra to compare purchasing decisions. Having a deployed calculator means no manual algebra and I have access to the tool anywhere / anytime.

The second reason is that this tool makes cost saving calculations available to everyone, regardless of their mathematical inclination. No algebra, no fractions, just a quick informative result about their options.

The third and final reason is that lots of cost saving online calculators exist but they are primarily geared towards deciding about renting vs. buying housing. As a consequence, they require lots of context specific user input (interest rates, mortgage rates, etc.) and are not well suited for general cost comparisons. 

<hr>

That completes the general overview of the project, and everything below discusses the technical aspect of the project.

<hr>

## Technical Work
I built the interactive graph using [bokeh](https://bokeh.org), wrote the html jinja template, styled the front end using [bootstrap](https://getbootstrap.com), and deployed the application using [Heroku](https://www.heroku.co://www.heroku.com). This was my first time deploying an application and I don't think I would have survived without git!  

When I started this project I had a few goals. I wanted to:

1. Use a new python package
2. Deploy the project
3. Visualize results
4. Make something genuinely useful for me and others

I'd say I accomplished all my goals!

1. I used bokeh to serve an interactive dashboard.
2. I deployed the project using Heroku and a custom domain name.
3. I designed the webpage using html and css (lots of bootstrap).
4. I used this tool the other day to investigate an espresso machine.

## Other Ideas
This project really sat in my mind as something that would never end, as I have lots of ideas on how to extend it even further. Here are a other things:

- Take into account the time each option requires
- Have the user input have a "flip" option. 
  - At what costs do I save money after 40 uses?
- Create an account system to keep track of different decisions
  - Accounts could have different comparison profiles
  - Notifications when money is saved
  - Summaries of monthly / yearly savings or spendings
