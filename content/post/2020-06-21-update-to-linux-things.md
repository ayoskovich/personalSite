---
title: Update to linux things
author: ''
date: '2020-06-21'
slug: update-to-linux-things
categories: []
tags: []
subtitle: ''
summary: 'The little differences between Mac OS and Linux Lite and also some tmux stuff.'
authors: []
lastmod: '2020-06-21T18:13:02-04:00'
featured: no
image:
  caption: ''
  focal_point: ''
  preview_only: no
projects: []
draft: true
---

My last post was about some useful bash commands like `grep` and `find`. I just learned that while Mac OS is a unix based system, these commands work a tad differently. For example, on Linux 

```bash
$ grep "baseball" -r
```

needs to be changed to

```bash
$ grep "baseball" -r .
```

Otherwise you get a very spooky `grep: warning: recursive search of stdin`. The `.` at the end is needed to specify the location to search recursively, which on linux is just the current location. A similar thing happens with `find`.

For example, on Linux...

```
$ find -regex ".*_names"
```

turns into 

```
$ find . -regex ".*_names"
```

Again, we need the `.` in order to specify the location of the search.

