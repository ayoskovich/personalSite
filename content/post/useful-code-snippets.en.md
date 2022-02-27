---
title: Useful code snippets
author: ''
date: '2020-09-10'
slug: useful-code-snippets
categories: []
tags: 
  - ramble
subtitle: ''
summary: 'Compiling all my random one liners.'
authors: []
lastmod: '2020-09-10T20:22:17-04:00'
featured: no
image:
  caption: ''
  focal_point: ''
  preview_only: no
projects: []
---

I've been adding a ton of [gists](https://gist.github.com/ayoskovich) to my github account. I think this is a better way to store useful snippets than in a physical notebook.

--- 

#### An example gist

The other day I was looking for a more visually appealing way to read manual pages, and this bash command will convert the `ssh` man page into a nicely formatted pdf file:

```
man -t ssh | ps2pdf - ssh.pdf
```

Or if that's not interesting, here's one that exports jupyter notebooks to raw python files automatically every time a notebook file changes in the current directory:

```
ls *.ipynb | entr jupyter nbconvert *.ipynb --to python --output-dir=./src
```

I've got tens of these things, tens!
