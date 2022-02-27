---
title: Creating code free jupyter notebook exports
author: ''
date: '2020-04-09'
slug: creating-code-free-jupyter-notebook-exports
categories: []
tags: 
  - jupyter
  - python
subtitle: ''
summary: 'A quick way to exclude code from jupyter notebooks'
authors: []
lastmod: '2020-04-09T16:33:44-04:00'
featured: no
image:
  caption: ''
  focal_point: ''
  preview_only: no
projects: []
---

This is going to be a really short post! If you've ever exported a jupyter notebook to html or pdf in order to share with someone that doesn't want to see code, I've got the answer right here. To export a jupyter notebook without all the code use the following:

```text
jupyter nbconvert --to markdown --TemplateExporter.exclude_input=True index.ipynb
```

Just replace `index.ipynb` with the name of your jupyter notebook. More info [here](https://nbconvert.readthedocs.io/en/latest/config_options.html?highlight=TemplateExporter.exclude)