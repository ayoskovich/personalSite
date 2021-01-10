---
title: Estimating My Morning Cup
author: ''
date: '2021-01-09'
slug: coffee
categories: []
tags: []
subtitle: ''
summary: 'How long does my morning coffee take?'
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

I've always wondered about the amount of time it takes me to brew a cup of coffee. In order to answer this question,  every day for over 3 months I kept track of a few key variables that determine the amount of time it takes me to make a cup of coffee.

---

### Tl;dr / Summary
On average it takes me 13 minutes to make a cup of coffee and that average varies by 2 minutes. I became faster measuring out the beans but didn't get more accurate when dumping them out of the bag. 

The amount of time it took to grind the beans was different across coffees as well as the amount of time it took for all the water to pass through the ground beans. 

I'd end up saving money in less than a year if I purchased an electric grinder and scale.

---

### Coffee Brewing Process

The way I brew coffee looks something like this:
![](pourover.jpeg)

I start with a bag of whole bean coffee, count out 173 beans, and then grind them using a manual coffee grinder. I pour hot water over the coffee beans and voilà, I have a cup of coffee. Throughout this process, I decided to kept track of a few things: 

- **cTime**: Time to count out the beans 
- **gTime**: Time to grind the beans manually
- **bTime**: Time for the water to pass through the coffee grounds
- **count**: Number of beans I was supposed to count out 
- **over**: Number of beans I actually poured out 
- **duration**: Total amount of time the cup took to make

Here's a screenshot of the data, and you can find the [github repo here](https://github.com/ayoskovich/coffee-log).

![](data.png)

---

I recorded data 104 times between October 27th, 2020 and December 26th, 2020. The below plot shows the total amount of time the coffee brewing process took each day.
![](total.png)

It took 13.3 minutes to brew a cup of coffee on average and the times vary by around 2 minutes. The fastest cup took 10 minutes to make, and the longest cup took 20 minutes to make.

---

Things like brew time and grind time seem to vary by the type of coffee, but this likely has more to do with the coffee bean shape / size / weight than anything I can control.

![](total_brew.png)

![](grind_time.png)

![](draw_down.png)


---

As I started to record data consistently, I began to wonder if I was getting any faster at counting out the beans.
![](c_over_time.png)

The first 20 or so times I improved quite a bit, but the gains dimished after that and settled at around 2 minutes. Looks like I improved upon my time I mentioned in [this blog post](https://anthonyyoskovich.com/post/coffee-without-a-scale/) I wrote back in August! 

---

I also wondered the same thing about my pouring accuracy. In other words, am I getting better at eyeballing the number of beans I need to pour out?
![](overages.png)

Doesn't look like I really improved on pouring them out, and I was much more likely to overpour than underpour. 
![](overages_by_cof.png)

The Stovetop Buesaco, Stovetop Sakicha, and Starbucks Brazil coffees were the main culprits of my underpouring.

---

## Money Money Money
I could reduce the total brewing time if I had more electronic equipment. For example, I wouldn't have to manually count out the beans if I had a scale, and I could grind the beans almost instantly if I had an electric coffee grinder. 

These tools would cost (roughly):
- Scale: around $50
- Electric grinder: $200 (yes that's 2 zeros, I need a good one...)

In order to start judging whether or not these investments are worth my money, I need some sort of measurement for the value of my time. I'd say I value 1 hour of my time at around $25. I know that with my current, no equipment setup, I'm spending at least this much time:

- Avg count time: 2 minutes
- Avg grind time: 2 minutes

I'll assume that the equipment will completely eliminate any time related to counting out or grinding the coffee. So, by purchasing a scale and an electric grinder, I would save around 4 minutes every day.

_....Math incoming...._

At $25 / hour, (25/60) * 4 = $1.66. I'd save $1.66 each use. After inputting these values into my handy, custom built calculator <a href="http://www.amisaving.com" target="_blank">amisaving</a>, I'd start saving money after 150 uses, which is a little less than half of a year. 


So yeah, I think for my wallet AND my sanity it would be a good idea to invest in some technology to bring me out of the stone age.

<br>
<br>

---

### Notes

Here are the values I entered into the <a href="" target="_blank">online cost saving calculator</a>:

| field                           | value |
|----------------------------------|-------|
| Cost of equipment                | 250   |
| Cost per unit with investment    | 0     |
| Cost per unit without investment | 1.66  |
