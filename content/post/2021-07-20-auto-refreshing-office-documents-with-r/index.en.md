---
title: Auto-refreshing Office Documents With R
author: ''
date: '2021-07-20'
slug: []
categories: []
tags: 
  - r
  - automation
subtitle: ''
summary: 'Why spend 10 minutes doing something manually when you could spend 1 hour automating it?'
authors: []
lastmod: '2021-07-20T21:35:14-04:00'
featured: no
image:
  caption: ''
  focal_point: ''
  preview_only: no
projects: []
---

I spend quite a bit of time including plots created from `R` in Microsoft Word and Powerpoint. While it's fairly straightforward to copy and paste plots from Rstudio, something inside me said, ["there had to be another way"](https://www.youtube.com/watch?v=AeSjt7cqq-k).

Ideally my only exposure to Microsoft Office products would be using R Markdown, but the world of cross team collaboration is complicated.

Anyways, when I create plots I usually do something like:

```r
df %>% 
  filter(foo == 'bar') %>% 
  ggplot(aes(...))+
    geom_point(...)
    
ggsave('myfile.svg')
```

and then insert `myfile.svg` into the word doc. This is both annoying and error-prone:

- **Annoying:** Every time the image updates, I need to manually copy and paste it into the document. 
- **Error-prone:** Every time the image updates, I need to _remember_ to copy and paste it into the document. This seems like something a computer would do significantly more reliably than myself.

### A better way

The first step in making this more manageable is not only inserting, but inserting and _linking_ the file within Word or Powerpoint (there is a dropdown in the file explorer to select this option). By linking the image, whenever the file changes the document will update without needing to manually insert the image again.

### Kind of, but not so much

It will refresh the image, but only after closing and reopening the document. Luckily, there is an easy way to close and open applications from within R using `system` and `browseURL`. 

Example: I have a file called `foo.docx`. I could close this file and reopen it like this:

```r
# Kill Microsoft Word
system("TASKKILL /F /IM winword.exe")

# Reopen the closed file
browseURL('foo.docx')
```

Unfortunately the `system` function is killing _all_ instances of word, so it's a bit clunky if for some &nbsp; <sup> sad </sup> &nbsp; reason you need more than one Word doc open at the same time. I usually make a little function out of this (can you tell I use python? lol):

```r
ref_doc <- function(file_name, task_name){
  # file_name (char): File to refresh
  # task_name (char): Task name of program to kill
  #   Microsoft Word: winword.exe
  #   Microsoft Powerpoint: powerpnt.exe
  #
  # Example:
  #   ref_doc('foo.docx', 'winword.exe')
  
  system(paste0("TASKKILL /F /IM ", task_name))
  browseURL(file_name)
}
```

If you need to refresh a different application besides Word or Powerpoint, you can find the `task_name` by opening task manager and viewing the properties of the program you wish to refresh.