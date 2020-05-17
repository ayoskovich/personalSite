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

In the article, Fox brings up a large amount of statistics and percentages. My goal here is to find the data he references and perform an identical analysis. Then I'll see if I get the same numbers as him. This should be a great exercise in reproducible research.


## Process
I'm going to go and get the prices of chicken, beef, and pork and adjust them for inflation. I'll get data from the BLS, which he references in his article. A more granular overview of this process can be found [here](https://github.com/ayoskovich/chickens_trust/blob/master/price_check.md). 

Feel free to skip this link if you aren't interested in the technical details.

## Findings
I'm not able to recreate the exact numbers he references in his article because I couldn't find data that goes back to 1935. However, the relative directions of the price moves were all identical, and by extrapolating the historic changes back to 1935, both the price of chicken and the price of beef were only 5% and 3% different, respectively.

## Thoughts

I can't seem to find pricing that goes back to 1935. Here's what I tried:

1. [FRED](https://fred.stlouisfed.org)
2. BLS directly [here](https://www.bls.gov/regions/mid-atlantic/data/averageretailfoodandenergyprices_usandmidwest_table.htm)
3. [This](https://www.nationalchickencouncil.org/about-the-industry/statistics/wholesale-and-retail-prices-for-chicken-beef-and-pork/) data from the national chicken council has prices that go back to 1960.
4. [This](https://www.ers.usda.gov/data-products/meat-price-spreads/) data from the US Department of Agriculture only has prices that go back to 1970.

I don't want to get bogged down on this specific article because I think there is a larger idea lurking around here.

#### Obviously I could reach out to the author and get these things clarified. However, should I have to?

What is the threshold for transparency? Is a general link enough? I'll be honest, pointing me to the homepage of a government website and saying "I got the data from here" literally means nothing to me. There is so much more work involved in order to locate and download the data. I see 3 big ideas here:

1. **Technical Skills:** The first is the technical skills required to get the data. Surely most individuals can follow a link and click the 'export to csv' button. However, what if the data isn't available to be exported? What if I need to build a web scraper in python in order to get it in a format suitable to analyze?

2. **Data availability:** if the author of an article is using proprietary information in order to make claims about something, should the nature of the data be explicitly stated? In other words, should I see a note that says "you wouldn't be able to gather this data if you tried?". Surely that would sprinkle some salt into peoples interpretations of numbers.

3. **Process transparency:** The authors assumptions or exact process are not known, and if they aren't in the article, some authors may be harder (some impossible) to reach for clarification.

- What is the standard for sharing the data gathering / wrangling process?
- Websites like fivethirtyeight are incredibly transparent with their statistics
- What is the expectation in terms of 'public ingestion'?
  - Should we be critical / spend the time and effort to check things?
    - I think yes (lots of political things like this already exist)
    - Call out to my personal quest of "fact/process checking/revealing"
    - Should open source tools be used to complete analyses so that anyone with a computer can recreate the numbers? (providing SAS code nukes people who don't have a liscense.)