---
title: Coffee Analysis
author: ''
date: '2021-01-09'
slug: coffee
categories: []
tags: []
subtitle: ''
summary: 'Analyzing Coffee'
url_code: "https://github.com/ayoskovich/coffee-log"
authors: []
featured: no
image:
  caption: ''
  focal_point: ''
  preview_only: no
projects: []
draft: true
---

I've always wondered about the amount of time it takes me to brew coffee. Does it take me longer to make it earlier in the morning? Does it vary by the type of coffee I have? In order to answer these questions, I kept track of the amount of time it took me to make a cup of coffee. 

---

### Summary
I got faster at counting the beans, but didn't get more accurate when counting them out. Grind times were different between coffees as well as the drawdown times. On average it takes around 14 minutes to make coffee, and on average it varies by xxxxxx. Also, if I value my time at $25 / hour, I xxxxxxx save money by purchasing an electric grinder or scale.

---

### Coffee Brewing Process


The way I brew coffee looks something like this:
![](pourover.jpeg)

I start with a bag of whole bean coffee, count out 173 beans, and then grind them up using a manually cranked coffee grinder. Hot water is poured over ground coffee beans and the water passes through and into some sort of vessel. This process gave me quite a few things I could keep track of:

- Start Time: Time of day I began making the coffee (recorded when I began counting beans)
- Count Time: Time to count out the beans 
- Grind Time: Time to grind the beans manually
- Draw Down Time: Time for the water to pass through the coffee grounds
- Number of beans I was supposed to count out (need to control for this)
- Number of beans I actually poured out (I was eyeballing everything)
- End Time: Time of day when the whole process was done

---

I recorded data 104 between August 27th, 2020 and December 26th, 2020. The below plot shows the total amount of time the coffee brewing process took each day.
![](total.png)

It took 13.3 minutes to brew a cup of coffee on average, and varies by around 2 minutes. The fastest cup took 10 minutes of make, and the longest cupt took 20 minutes to make.

---

Not all records contained all of the fields, as I didn't start recording the start / end times until 30 or 40 records in, so there is some filtering that happens when you see these visualizations. 

I used 11 different types of coffee throughout the project.
![](coffee_bar.png)

Maybe the brew time varies by the type of coffee:
![](total_brew.png)


Maybe the grind time varies
![](grind_time.png)


Or the draw down time
![](draw_down.png)


The drawdowns do appear to vary by coffee.

---

As I did this consistently, I started to wonder if I was getting any faster at counting out the beans.
![](c_over_time.png)

The first few times I got lots better, but the returns appear to be diminishing. Now I'm at less than 100.

---

I wondered the same thing with my pouring accuracy. That is, am I getting better at eyeballing 173 beans after I pour the beans out of the bag?
![](overages.png)

Doesn't look like I really improved on pouring them out, and I was way more likely to overpour than underpour. 
![](overages_by_cof.png)

---

### Money Money Money

Would it make sense for me to buy a scale? Would it make sense to buy an electric grinder? I'll use this data to compute the time I would save.

Avg time counting:
Avg time grinding: 

Insert my timevalue here ($25 / hour)
Use amisaving to compute the savings
