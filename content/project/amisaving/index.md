---
date: "2021-01-03T00:00:00Z"
external_link: ""
image:
  caption: 
  focal_point: Smart
slides: example
summary: An interactive cost saving dashboard.
title: Am I Saving?
url_code: "https://github.com/ayoskovich/amisaving"
url_pdf: ""
url_slides: ""
url_video: ""

draft: true
---

- When did I have this idea
- Goals (deploy, do some webdev, make a tool)
- How to use 
- Improvements / hard parts / easy parts

I've built a [calculator](http://www.amisaving.com) to help people make purchasing decisions and ultimately answer the question, "Am I saving?". Lots of consumable items have multiple ways to be consumed. Coffee can be made at home, or you can get a cup of coffee from Starbucks. You can buy the unlimited pass at the carwash, or just pay each time you go. The inputs to the calculator are the costs associated with each decision. Usually one option requires a fixed investment followed by a cost for each consumption, and the other option skips the fixed investment and is traded off with a higher variable cost. The output of the calculator is the number of purchases at which point your decision would change. 

For example, "Before 30 coffee purchases, you save money just going to Starbucks. After 30 purchases, you would save money by investing in equipment." This could be extended a TON of different ways:

- At what fixed cost do I save money after 15 purchases?

## Technical Work

When I started this project I had a few goals. I wanted to:

1. Use a new python library.
2. Actually deploy the project.
3. Make something genuinely useful for me and others.


## Further Work
- Personal account with timevalue
  - Accounts would have different comparison profiles
  - Notifications when money is saved
  - Summaries of monthly / yearly savings or spendings
