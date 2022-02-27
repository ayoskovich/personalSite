---
title: New project and a bitcoin tracker
author: ''
date: '2021-01-04'
slug: bitcoin
categories: []
tags: 
  - python
subtitle: ''
summary: 'Project done and random bitcoin memes'
authors: []
lastmod: '2021-01-04T21:35:01-05:00'
featured: no
image:
  caption: ''
  focal_point: ''
  preview_only: no
projects: []
draft: true
---

I just posted about my most recent project I completed. See the project [here](https://anthonyyoskovich.com/project/amisaving/). I finally managed to give myself a deadline and finish the project...

In other news, I've been watching the price of bitcoin. I've got a quick little script that goes to the cryptowat.ch api and gets the current price, and a dictionary called `TRADES` that has the price and amount of my bitcoin transactions.

gainz.py
```
TRADES = [
    (...., ....),
    (...., ....)
]
buys = [x[0] for x in TRADES]
amts = [x[1] for x in TRADES]

r = requests.get('https://api.cryptowat.ch/markets/kraken/btcusd/price').json()

gainz = np.sum(
    np.array(amts)*(r['result']['price'] - np.array(buys))
)

print(f"Current price: {format(r['result']['price'], '.2f')}", end=", ")
print(f"Gainz: {gainz}")
```


to run from shell
```
while true; do python3 gainz.py; sleep 10; done
```
