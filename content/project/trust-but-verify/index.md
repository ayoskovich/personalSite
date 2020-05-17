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

draft: true
---

## Motivation

A recent [bloomberg article](https://www.bloomberg.com/news/articles/2020-05-11/why-chicken-is-plentiful-during-the-pandemic-and-beef-is-not?srnd=premium&utm_medium=social&utm_source=twitter&utm_campaign=socialflow-organic&utm_content=markets&cmpid%3D=socialflow-twitter-markets&sref=XQtHDW1P) authored by [Justin Fox](https://twitter.com/foxjust) piqued my interest. In the article, Fox describes how the prices and consumption of 3 different types of meat have changed over time. He gives some good insights into why the price of chicken has stayed low in recent years (due to the ease of automation), and I would encourage you to give the article a read.

In the article, Fox brings up a large amount of statistics and percentages. My goal here is to find the data he references and perform an identical analysis. 


## Process
I'll focus on 3 things he said.

> 1. "poultry costs U.S. consumers 62% less in inflation-adjusted terms than it did in 1935"
> 2. "Pork, now also raised mostly at factory scale indoors, is 12% cheaper"
> 3. "Beef, which isn’t, costs 63% more."

I'm going to go and get the prices of chicken, beef, and pork and adjust them for inflation. I'll get data from the BLS, which he references in his article. A more granular overview of this process can be found [here](https://github.com/ayoskovich/chickens_trust/blob/master/price_check.md), where you can look at the exact code and data sources I gathered. 

## Findings
I'm not able to recreate the exact numbers he references in his article because I couldn't find data that goes back to 1935. However, the relative directions of the price moves were all identical, and by extrapolating the historic changes back to 1935 both the cost decreases of chicken and beef are within 5%. My estimate for the price change in pork was fairly different (my -27% against his -12%), but this is likely due to my not so elegant extrapolation. 

Here's what I tried to find data that goes back to 1935:

1. [FRED](https://fred.stlouisfed.org)
2. BLS directly [here](https://www.bls.gov/regions/mid-atlantic/data/averageretailfoodandenergyprices_usandmidwest_table.htm)
3. [This](https://www.nationalchickencouncil.org/about-the-industry/statistics/wholesale-and-retail-prices-for-chicken-beef-and-pork/) data from the national chicken council has prices that go back to 1960.
4. [This](https://www.ers.usda.gov/data-products/meat-price-spreads/) data from the US Department of Agriculture only has prices that go back to 1970.

**It would take me 2 seconds to reach out to Fox on twitter and ask for clarification about the data that goes back to 1935.**

I have no reason to distrust Fox's numbers, and I don't doubt the legitimacy of the bloomberg publication at all. But there is a cost associated with the verification process.

The cost associated with verifying a data-driven claim is a function of 3 main things:

1. **Technical Resources:** These are the programming languages, skills, and time required to actually perform the analysis. Using open source languages such as `python` and `R` lower this cost, while performing an analysis in `SAS` or any other licensed solution gatekeeps individuals out of verification.
    
    
2. **Data availability:** The reader must go out and acquire the data used.
  1. Ability to navigate to the exact location of the data
      - Citing price data simply by saying [BLS](https://www.bls.gov) or the [USDA](https://www.usda.gov) is absolutely not enough to make the data easily available. These websites are **dense** and often contain many different cuts of the same data. Readers need to know the <u>exact</u> location (series ID, name, etc.).
  2. Ability to download the data
      - Once the reader has navigated to the source of the data, do they have access to it?
       
       
3. **Process transparency:** The reader must be given the author's assumptions and exact process. 
  - Any filtering, aggregation, data cleaning, buttons pushed should be clearly defined *somewhere*. Not necessarily in the article or main medium itself, but a technical description of the entire (and exact) process should be made available to the reader (such as an external github repository).


# Zooming out and moving on

[Nate Silver's](https://twitter.com/NateSilver538) website [fivethirtyeight](https://fivethirtyeight.com) does a wonderful job making data analysis verifiable and transparent. They host their data and code on [github](https://github.com/fivethirtyeight/data) so the interested (or skeptic) reader can dive in. 

The New York Times does something similar with their "The Upshot" section, hosting code [here](https://github.com/TheUpshot), but it looks fairly inactive (last update seems to be in March of 2019). I tried to read more about the methodology for [this](https://github.com/TheUpshot/nyt_weddings) project but conveniently ran out of my free articles for the day.
