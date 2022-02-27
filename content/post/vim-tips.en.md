---
title: Vim tips
author: ''
date: '2020-08-18'
slug: vim-tips
categories: []
tags: 
  - vim
subtitle: 'No time for an introduction when vim tips are involved'
summary: 'Correcting misspelled words and inserting special characters in the worlds most powerful text editor'
authors: []
lastmod: '2020-08-18T10:51:23-04:00'
featured: no
image:
  caption: ''
  focal_point: ''
  preview_only: no
projects: []
---


### Spellcheck

To highlight misspelled words in a vim session:

```
:set spell
```

There are a few handy motions that come with this:

| Keystroke | Description                                                         |
|-----------|---------------------------------------------------------------------|
| z=        | Display suggested correct spelling for misspelled word under cursor |
| ]s        | Move cursor to the next misspelled word                             |
| [s        | Move cursor to the previous misspelled word                         |


If you're interested in a more thorough description of this functionality, `:help spell` will take you to the docs.

---


### Accented characters

It's really simple to add characters that don't exist on common keyboards. While in insert mode, 

```
CTRL-k + <digraph> 
```

A digraph is basically a pair of keys that represent a character. For example, `a'` is a digraph for `á`.

Here's some of the ones I've found useful (prepend each keystroke with `CTRL-k`).

| Digraph   | Output |
|-----------|--------|
| ~n        | ñ      |
| a'        | á      |
| ~?        | ¿      |
| ~!        | ¡      |

`:help i_CTRL-k` for more help on this, and `:digraphs` will display all available digraphs and their output.

Thanks for reading! ☺  (`0u` is the digraph for the smiley face)

