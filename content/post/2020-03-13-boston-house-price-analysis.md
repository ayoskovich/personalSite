---
title: A Hybrid Jupyter Notebook Workflow
author: ''
date: '2020-03-13'
slug: boston-house-price-analysis
categories:
  - dataAnalysis
tags: []
draft: true
---

&emsp; I use jupyter notebooks quite a bit and have developed a workflow that allows me to leverage python modules in order to give the notebook more structure. <a href="https://www.youtube.com/watch?v=7jiPeIFXb6U" target="_blank">This</a> talk does a great job describing some problems and pain points I have also encountered when working in a notebook environment.

&emsp; Most times if I work exclusively in a notebook I tend to not be very smart with the program architecture due to the ability to execute cells in an arbitrary order that I forget about. Then, when I restart the kernel, everything explodes and I'm left confused due to all the hidden variables and states that were hovering in the workspace.

&emsp; There are a few advantages to importing functions relevant to the analysis as modules.

1. The notebook immediately becomes less cluttered.
2. External modules can be tested.
3. External modules can be re-used.
4. Analysis paths can rapidly be changed or pivoted due to this modular structure.

&emsp; I created a notebook that demonstrates this idea and can be found <a href="https://nbviewer.jupyter.org/github/ayoskovich/personalSite/blob/master/pyNotebooks/housing/housePrices.ipynb?flush_cache=True" target="_blank"> here</a>. The imported modules can be found <a href="https://github.com/ayoskovich/personalSite/tree/master/pyNotebooks/housing" target="_blank">here</a>.
