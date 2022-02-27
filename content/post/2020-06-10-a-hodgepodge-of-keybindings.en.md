---
title: A hodgepodge of keybindings
author: ''
date: '2020-06-10'
slug: a-hodgepodge-of-keybindings
categories: []
tags: 
  - vim
subtitle: ''
summary: 'Documenting my favorite keybindings and shortcuts'
authors: []
lastmod: '2020-06-10T09:20:12-04:00'
featured: no
image:
  caption: ''
  focal_point: ''
  preview_only: no
projects: []
---

I am a huge fan of the keyboard and feel the opposite way about the mouse, which is slow and bulky. I won't unleash my full rant here, but long story short I really like keyboard shortcuts. So, without anyone's request here are some of my current favorites.

Sidenote: Here are some helpful links if you aren't familiar with any of the things named down there:

- [IPython](https://ipython.org/): Interactive python
- [vim](https://www.vim.org/): The world's most absurdly powerful text editor
- [tmux](https://github.com/tmux/tmux/wiki): Terminal multiplexer
- [ranger](https://github.com/ranger/ranger): Terminal based file explorer


| Program | Command/Keystroke  | Explanation                                           | 
|---------|----------|-----------------------------------------------------------------|
| IPython | %who     | Show variables currently in memory                              |
| IPython | %whos    | Sames as `%who`, just gives more info                           |
| IPython | %load    | Fill cell with text contained in a file                         |
| IPython | !ls      | Handy to quickly check the contents of current directory        |
| IPython | !pwd     | Show the working directory (these can also be saved into a var) |
| vim     | ZZ       | Save and close current file (faster than `:wq`)                 |
| vim     | ZQ       | Close (dont save) current file (faster than `:q!`)              |
| vim     | ctrl-g   | Show current file name, line number                             |
| vim     | /test\c  | Case insensitive line search                                    |
| vim     | R        | Enter replace mode (on current line)                            |
| vim     | :tab :help usermanual  |  Open user manual in new tab                      |
| vim     | :gt      | Change tabs                                                     |
| vim     | f        | Move cursor to next occurrence of `,` press `;` to find next    |
| vim     | F        | same as `f` but search left                                     |
| vim     | :help wordmotion  | This is a useful help page                             |
| vim     | :help motion |      This is another useful help page                       |
| vim     | u        | Undo change                                                     |
| vim     | U        | Undo all changes on line                                        |
| vim     | .        | Repeat last motion                                              |
| tmux    | ctrl-w-w | Swap between panes in vim                                       |
| tmux    | ctrl-b-q | Show pane numbers in tmux, can type number to swap to that pane |
| tmux    | ctrl-b-w | Display all current windows                                     |
| Firefox | ctrl-d   | Save bookmark                                                   |
| ranger  | S        | Open shell in current directory                                 |
| ranger  | @vim     | Open currently selected file in vim                             |

