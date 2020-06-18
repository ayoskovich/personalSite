---
title: Learning Linux Things
author: ''
date: '2020-06-14'
slug: learning-linux-things
categories: []
tags: []
subtitle: ''
summary: 'Using the command line is harder but not really.'
authors: []
lastmod: '2020-06-12T10:54:56-04:00'
featured: no
image:
  caption: ''
  focal_point: ''
  preview_only: no
projects: []
draft: false
---

Recently I installed the Linux Lite operating system onto my computer. My hardware is a tad old and was getting quite slow with all the Windows overhead, and it was time for a change. I've been using the terminal a lot and really love just messing around inside the command line. One specific thing I've learned how to do is move files that match a certain pattern to another location very quickly. Lets say I have the following file structure:

```
myFolder/
cat_names
dog_names
snakenames
```

My goal is to move the `cat_names` and `dog_names` files to `myFolder/`. I can match the file names using a regex and then pipe them to xargs in order to do this:

```bash
$ find -regex ".*_names" | xargs -I '{}' mv {} test/
```

This might not seem very helpful, but imagine if I had hundreds or even thousands of files that matched that pattern. Plus it's just kind of cool.

Another thing that I've learned about is `grep`. Let's say I need to search through all the files in the `test/` folder and I want to locate where I used the word "baseball". I can do the following:

```bash
$ grep "baseball" -r
```

Which outputs

```properties
names:Anthony: baseball
names:Sam: baseball
scores:baseball scores:
```

This means that the `names` and `scores` files both contain the word baseball.

I've also installed a package called [unclutter](https://wiki.archlinux.org/index.php/Unclutter) which hides my mouse cursor after a certain number of seconds.

