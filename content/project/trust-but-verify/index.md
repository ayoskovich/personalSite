---
date: "2020-05-12T00:00:00Z"
external_link: ""
image:
  caption: 
  focal_point: Smart
slides: example
summary: A journey down the (chicken) rabbit hole.
title: Trust But Verify
url_code: "https://github.com/ayoskovich/chickens_trust"
url_pdf: ""
url_slides: ""
url_video: ""

draft: true
---

## Motivation

A recent [bloomberg article](https://www.bloomberg.com/news/articles/2020-05-11/why-chicken-is-plentiful-during-the-pandemic-and-beef-is-not?srnd=premium&utm_medium=social&utm_source=twitter&utm_campaign=socialflow-organic&utm_content=markets&cmpid%3D=socialflow-twitter-markets&sref=XQtHDW1P) authored by [Justin Fox](https://twitter.com/foxjust) piqued my interest. In the article, Fox describes how the prices and consumption of 3 different types of meat have changed over time. He gives some good insights into why the price of chicken has stayed low in recent years (due to the ease of automation), and I would encourage you to give the article a read.

In the article, Fox brings up a large amount of statistics and percentages. My goal here is to find the data he references and perform an identical analysis. 


## Process
I'm going to go and get the prices of chicken, beef, and pork and adjust them for inflation. I'll get data from the BLS, which he references in his article. A more granular overview of this process can be found [here](https://github.com/ayoskovich/chickens_trust/blob/master/price_check.md). 

## Findings
I'm not able to recreate the exact numbers he references in his article because I couldn't find data that goes back to 1935. However, the relative directions of the price moves were all identical, and by extrapolating the historic changes back to 1935, both the price of chicken and the price of beef were only 5% and 3% different, respectively.

#### Here's what I tried to find data that goes back to 1935:

1. [FRED](https://fred.stlouisfed.org)
2. BLS directly [here](https://www.bls.gov/regions/mid-atlantic/data/averageretailfoodandenergyprices_usandmidwest_table.htm)
3. [This](https://www.nationalchickencouncil.org/about-the-industry/statistics/wholesale-and-retail-prices-for-chicken-beef-and-pork/) data from the national chicken council has prices that go back to 1960.
4. [This](https://www.ers.usda.gov/data-products/meat-price-spreads/) data from the US Department of Agriculture only has prices that go back to 1970.

I don't want to get bogged down on this specific article because I think there is a larger idea lurking around here.

#### Obviously I could reach out to the author and get these things clarified. However, should I have to?

I have no inherent distrust in Fox's numbers, but there is a cost associated with the verification process.

The verifiability of a data-driven claim is a function of 3 main things:

1. **Technical Resources:** The reader must have the same technical resources to verify claims. 
  - These technical resources are the computer programs used, the technical prowess in order to actually perform the analysis, and the time to actually complete the analysis. Using open source languages such as python and R lower this cost, while performing an analysis in SAS essentially shuts out anyone who doesn't have thousands of dollars for a valid user license.

2. **Data availability:** The reader must have access to the data that was used in order to verify, and the reader must know *exactly* where to get the data. Citing statistics that come from proprietary data sources effectively squashes all hopes at any semblence of verifiability. 
  1. I need directions
  2. I need to be allowed to download the data myself.
  
  - Imagine your friend makes a really good frozen burrito they got from the store and you want to go to the store and find it. Their directions say, "I got it at Walmart". Citing the BLS or the USDA is equivalent to telling me that you got the burrito at Walmart with no further instructions.

3. **Process transparency:** The reader must be given the author's assumptions and exact process. Any filtering, aggregation, data cleaning, buttons pushed should be clearly defined *somewhere*. Not necessarily in the article or main medium itself, but a technical description of the entire (and exact) process should be made available to the reader (such as an external github repository).


# Zooming out and moving on

[Nate Silver's](https://twitter.com/NateSilver538) website [fivethirtyeight](https://fivethirtyeight.com) does a wonderful job making data analysis verifiable and transparent. They host their data and code on [github](https://github.com/fivethirtyeight/data) so the interested (or skeptic) reader can dive in. 

The New York Times does something similar with their "The Upshot" section, hosting code [here](https://github.com/TheUpshot), but it looks fairly inactive (last update seems to be in March of 2019). I tried to read more about the methodology for [this](https://github.com/TheUpshot/nyt_weddings) project but conveniently ran out of my free articles for the day.

