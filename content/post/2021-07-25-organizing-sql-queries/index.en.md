---
title: 'Organizing SQL Queries'
author: ''
date: '2021-07-25'
slug: []
categories: []
tags: []
subtitle: ''
summary: 'A personal tool'
authors: []
lastmod: '2021-07-25T12:51:13-04:00'
featured: no
image:
  caption: ''
  focal_point: ''
  preview_only: no
projects: []
draft: true
---

I tend to have lots of different SQL queries that I use for different things. The 2 main variables are:

1. Table
2. Level of aggregation

The difference between the queries is usually that they are getting information from different tables, or they're at a different level of aggregation. I'm trying to brainstorm a sort of data portal for myself that does a few things:

- Makes it easy to search / see what information and tables the queries get from
- Has useful notes and comments about things I should keep in mind when using the tables
- Makes it easy to use the queries / select them

## Easy to search

This will probably be a drop-down.

## Has useful notes and comments

I'll have to think about this

## Easy to use the actual query

I'm thinking of a "click here to move the queries to a folder", then I'll select the folder I want to move the query to and it'll do it

The thing that is difficult about my current workflow is that I'm pretty much communicating to myself about the content of the query based on the filename, which I dont like. 

- prof_by_grade
- prof_by_student
- prof_by_school

These are all filenames that I tend to use. Ideally, I'd use one base query and then either have R code pop up or a query that gets things at a certain level. I like the idea of having 1 base sql query and then doing the filtering / aggregation in R. That would drastically decrease the amount of sql I would need to manage.


Maybe it would be better to get a big list of all the different measures / levels I've had to compute in order to help me be strategic about all of this.

So I'd have 1 base sql query, then for each base query I'd then have accompanying R code that would get ran based on my selections in the data portal. (Group by / filtering / creating new columns)

I'm trying to think how I would then go from sql tables to R code though, as there must need to be some sort of code that is always copy and pasted. Again, if this was views it would probably be a lot easier

I'd also like some sort of checker functions to use that would run whenever I got data.

I'm actually starting to think that this would work well (potentially) ((I think I use too many `()`)) as a package.

```r
aimsweb('student')
aimsweb('school')
aimsweb('nha')

nwea('student')
nwea('school')
```

So the function names would be the names of the data I'd like to get, then the things I pass are essentially the grouping. Behind the scenes, all `aimsweb` calls would reference the same query. However, 'school', and 'nha' would then have some r code. So basically

```r
aimsweb <- function(grouping){
  aimsweb_student <- function(df){
    df %>%
      group_by(StudentDWID, AcademicYear, CalendarSegment,
               Subject) %>%
      filter(...)
  }

  dbGetQuery('aimsweb.sql') %>%
    {
      if ___ then aimsweb_student
      else if ___ then aimsweb_school
    }
}
```

The only hard part I see here is version control. Like if I update the package, then a ton of old code that was using an old version may stop working? This is where I kind of like the idea of copying and pasting tbh...

Maybe it makes more sense to have them as snippets within Rstudio. Or I could make a project .Rmd template that used multiple files? That would be kind of a hybrid approach. The templates live within a package, but "create from template" essentially copy and pastes from a central location. Different versions would be possible, as I could just change the template.


