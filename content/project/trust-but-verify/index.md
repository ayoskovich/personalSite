---
date: "2020-05-12T00:00:00Z"
external_link: ""
image:
  caption: 
  focal_point: Smart
slides: example
summary: What does verifiable data analysis look like?
title: Trust But Verify
url_code: "https://github.com/ayoskovich/chickens_trust"
url_pdf: ""
url_slides: ""
url_video: ""

draft: false
---

## Motivation

A recent [bloomberg article](https://www.bloomberg.com/news/articles/2020-05-11/why-chicken-is-plentiful-during-the-pandemic-and-beef-is-not?srnd=premium&utm_medium=social&utm_source=twitter&utm_campaign=socialflow-organic&utm_content=markets&cmpid%3D=socialflow-twitter-markets&sref=XQtHDW1P) authored by [Justin Fox](https://twitter.com/foxjust) piqued my interest. In the article, Fox describes how the prices and consumption of 3 different types of meat have changed over time. He gives some good insights into why the price of chicken has stayed low in recent years due to the ease of automation. I would encourage you to give the article a read (the article may be behind a paywall).

In the article, Fox brings up a large amount of statistics and percentages. My goal here is to find the data he references and perform an identical analysis. I'll focus on 3 things he said.

> 1. "poultry costs U.S. consumers 62% less in inflation-adjusted terms than it did in 1935"
> 2. "Pork, now also raised mostly at factory scale indoors, is 12% cheaper"
> 3. "Beef, which isn’t, costs 63% more."

I retrieved price data from the BLS for chicken, beef, and pork and adjusted them for inflation. A more granular overview of this process can be found [here](https://github.com/ayoskovich/chickens_trust/blob/master/price_check.md), where you can look at the exact code and data sources I gathered. Long story short I wasn't able to recreate the exact numbers he references in his article because I couldn't find price data that goes back to 1935. However, the relative directions of all the real price moves were identical. 

Here's what I tried to find data that goes back to 1935:

1. [FRED](https://fred.stlouisfed.org)
2. BLS directly [here](https://www.bls.gov/regions/mid-atlantic/data/averageretailfoodandenergyprices_usandmidwest_table.htm)
3. [This](https://www.nationalchickencouncil.org/about-the-industry/statistics/wholesale-and-retail-prices-for-chicken-beef-and-pork/) data from the national chicken council has prices that go back to 1960.
4. [This](https://www.ers.usda.gov/data-products/meat-price-spreads/) data from the US Department of Agriculture only has prices that go back to 1970.
5. I also tweeted at the author, who responded with [this](https://data.bls.gov/timeseries/CUUR0000SEFF) series, which is actually a price index for poultry that does go back to 1935. I couldn't, for the life of me, figure out how to convert the price index into a real % change.

I don't want to get caught up on this one very specific example because I think there is a bigger idea here.

## What does a verifiable claim look like?

This general process of validating statistics requires a few key pieces of information. I need to know <u>what happened</u> with <u>what data</u> using <u>what tools</u>.

1. **what happened:** I need to know the author's process to analyze the data in an equivalent way to arrive at their conclusion.
  - Was any data filtered out?
  - Were there aggregations?
  
  
2. **what data:** I need to go out and acquire the exact data used.
  - I have to be able to navigate to the exact location of the data
      - Citing price data simply by saying [BLS](https://www.bls.gov) or the [USDA](https://www.usda.gov) is not enough to make the data easily available. These websites are dense and often contain many different cuts of the same data. I need to know the exact location (series ID, name, etc.).
  - Once the data has been navigated to, do I have access to download it?
      - Is the data behind a paywall?
      
      
3. **what tools:** These are the programming languages, skills, and time required to actually perform an identical analysis.

An easily verifiable claim happens when the author is clear about what they did, cites the exact location of the data used, and describes the tools they used in order to complete the analysis.

## Zooming out and moving on

[Nate Silver's](https://twitter.com/NateSilver538) website [fivethirtyeight](https://fivethirtyeight.com) does a wonderful job making data analysis verifiable and transparent. They host their data and code on [github](https://github.com/fivethirtyeight/data) so the interested (even skeptic) reader can dive in. 

The New York Times does something similar with their "The Upshot" section, hosting code [here](https://github.com/TheUpshot), but it looks fairly inactive (last update seems to be in March of 2019). I tried to read more about the methodology for [this](https://github.com/TheUpshot/nyt_weddings) project but unfortunately ran out of free articles for the day. The [pudding](https://pudding.cool) also hosts their data on [github](https://github.com/the-pudding).


I certainly don't think that a lack of 100% transparency should diminish the credibility of analyses that are performed, specifically in the journalism world. But finding the balance between conciseness and explicit descriptions of performed analysis is something that I believe should be taken into consideration.

Thanks for reading! Feel free to send me an email if you have any questions or comments :)