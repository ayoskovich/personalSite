---
title: New photo site!
author: ''
date: '2020-06-29'
slug: new-photo-site
categories: []
tags: []
subtitle: ''
summary: 'Im creating a dedicated site for my pictures, see [here](https://yoskophotos.xyz/).'
authors: []
lastmod: '2020-06-29T09:50:22-04:00'
featured: no
image:
  caption: ''
  focal_point: ''
  preview_only: no
projects: []
---
 
I've decided to create a standalone [website](https://yoskophotos.xyz/) for some of the pictures that I take with my film cameras. The site is pretty barebones right now, but that's because I'm doing all the html, css, server stuff, hosting, domain, etc. This should be a nice way to build something from the ground up.

--- 
#### A quick aside

I've been using ssh in order to connect to my server and have had to find an easy way to copy and paste text from the local machine to the remote one. 

For example, I wanted to embed an image through flickr but it's this gigantic jumble of characters that I would absolutely mess up if I were to manually type the entire link. Here's my solution:

1. Create a file called `toUpload` on the local machine containing the link.
2. Use `scp` in order to transfer `toUpload` to the remote machine.
3. While inside vim on the remote machine, use `!!cat toUpload` to paste the file's contents into vim.

Not the most elegant solution but it works!

