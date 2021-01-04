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
url_video: ""

draft: true
---

- When did I have this idea
  - I learned lots of useful stuff about cost, but a lot of it was explained to me (and made a lot of sense) mathematically. However, math is usually a touchy subject so I wanted to make something that would help people make decisions without needing to know any math.

- How to use 

I've built an [online calculator](http://www.amisaving.com) to help people save money. You put in the costs associated with 2 spending options (ex. brewing coffee at home vs. getting from starbucks) and the output is your breakeven between the two options. For example, "Before 30 purchases you save money getting coffee from Starbucks and after 30 purchases you save money brewing from home".

Lots of things can be consumed different ways. 
- Coffee can be made at home or you can go to Starbucks. 
- Buy the unlimited pass at the carwash or pay each time you go. 
- Rent a chainsaw each use or just buy one.

The inputs to the calculator are the costs associated with each decision. Usually one option requires a fixed investment followed by a cost for each consumption, and the other option skips the fixed investment and is traded off with a higher variable cost. The output of the calculator is the number of purchases at which point your decision would change. Lots of similar calculators exist, but almost all the intended purposes are for renting / buying a house. They require lots of user input and are a little complicated. The goal with this tool is to be quick to use and be general enough to help you shop.

<hr>

## Technical Work

When I started this project I had a few goals. I wanted to:

1. Use a new python library.
2. Actually deploy the project.
3. Make something genuinely useful for me and others.

- Goals (deploy, do some webdev, make a tool)
- Improvements / hard parts / easy parts

## Further Work
- Personal account with timevalue
  - Accounts would have different comparison profiles
  - Notifications when money is saved
  - Summaries of monthly / yearly savings or spendings
