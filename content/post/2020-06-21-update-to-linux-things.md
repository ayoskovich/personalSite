---
title: grep and find on MacOS
author: ''
date: '2020-06-21'
slug: update-to-linux-things
categories: []
tags: []
subtitle: ''
summary: 'The little differences between Mac OS and Linux Lite'
authors: []
lastmod: '2020-06-21T18:13:02-04:00'
featured: no
image:
  caption: ''
  focal_point: ''
  preview_only: no
projects: []
---

My last post was about some useful bash commands like `grep` and `find`. I just learned that while Mac OS is a unix based system, these commands work a tad differently. For example, on Linux 

```bash
$ grep "baseball" -r
```

needs to be changed to

```bash
$ grep "baseball" -r .
```

Otherwise you get a very spooky `grep: warning: recursive search of stdin`. The `.` at the end is needed to specify the location to search recursively. A similar thing happens with `find`.

For example, on Linux...

```
$ find -regex ".*_names"
```

turns into 

```
$ find . -regex ".*_names"
```

Again, we need the `.` in order to specify the location of the search.

---

### Expanding search results in grep

The `grep` usage I showed above only shows the line on which the match occurs. By using the `-B` and `-A` options we can specify how many lines before and after we want to see. For example: 


```bash
$ grep -B 1 -A 1 "baseball" searchme.txt
```

```
Here is a sentence before.
baseball
This is the sentence after.
```

And now grep will show 1 sentence before (`-B`) and 1 sentence after (`-A`) the match.

Onward to more command line knowledge...

