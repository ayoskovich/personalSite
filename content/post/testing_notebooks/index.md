---
title: Note to myself, from Jupyter
date: 2022-02-16
summary: 'and others interested in writing posts in jupyter notebooks'
---
I have written one of these posts using a jupyter notebook before, but it's been a while. When I went to write a new post in a notebook, I realized that I left myself absolutely no documentation about how render the `.ipynb` file once I was done. So, in the spirit of helping my future self and any other interested party, here's how I do it.

---

Create a jupyter notebook in a new folder under `post/`. The first cell should be the *raw* type and look something like this (yaml):

```
---
title: Jupyter note to my future self
date: 2022-02-16
summary: ', and to others'
---
```

Add whatever python content you want, and convert the notebook to markdown using:

```
!jupyter nbconvert --to markdown index.ipynb
```

That command (without the !) can be executed from the terminal instead of the notebook if you don't want readers to see it at the end.

Once the `index.md` file is created, `blogdown::serve_site()` should render the `index.md` file to your blogdown site.

<br><br><br>


```python
# Look familiar? :)
!jupyter nbconvert --to markdown index.ipynb
```

    [NbConvertApp] Converting notebook index.ipynb to markdown
    [NbConvertApp] Writing 1334 bytes to index.md



```python

```
