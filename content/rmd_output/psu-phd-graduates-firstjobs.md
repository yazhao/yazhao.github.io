---
Title: Where Do Penn State Statistics PhD Students Go After They Graduate?
Date: 2019-06-17
Slug: psu-phd-graduates-firstjobs
Tags: statistics, eda, jobs, pennstate
---



As a statistics PhD student, I am often asked what I intend to do after I graduate. After I give my answer, the next natural question is "where do PhD students from your department usually go after they graduate?" This question also comes up every year when prospective students visit our department.

In the past, my answer to that second question was that 1/3rd of our graduates went to academia, 1/3rd went into industry, and roughly 1/3rd went into what could loosely be defined as "other," which are jobs that are not quite academia but also not industry either, such as those at a national lab, a government agency, or a think tank like the RAND Corporation. This was more of a guess than anything based on real data, mostly because while we do have a webpage with where our alumni go after they graduate (http://stat.psu.edu/alumni), that information is not in a format that's easily analyzable.

Nonetheless, I do actually want the answer to this question. Part of this is so that I can actually give a good answer to prospective students (or other people who are curious), and part of it is just to satisfy my own curiosity. I recently spent some time organizing the available data into a more manageable CSV file so that I can finally answer the question of where Penn State statistics PhD graduates go.

### The Data
All of the data was taken off of the website link above for graduates from 2010 until 2018. I chose to cutoff at 2018 because 2019 graduate information isn't yet fully available and because data before 2010 seems more incomplete. Additionally, data from more than 9 years ago might not be so representative of recent trends in our department. Overall, this meant that I had information on 94 graduates and the first jobs and institutions they went to.

I will note as a major caveat that this information is self reported. While I think the information provided is accurate, it is possible that there is some kind of bias with who actually fills out this form. All of the data as well as the RMarkdown file (with the R code) can be found here: https://github.com/yazhao/PSUPhdGrads

### Definitions

For the purposes of this analysis, I looked only at the first job taken by graduates right after they got their PhD. It's entirely possible that many of these people switched career tracks, but tracking down that full information proved to be difficult. Additionally, I'm mostly interested in where people are *first* placed, not necessarily where they ultimately end up. I wanted to see what the immediate next step of a Penn State statistics PhD would be. The three categories of jobs were:

**Academia**: This includes any job working at an academic institution like a university. It also included any first job where the title was postdoc. This was an overly broad definition, and so I included people who weren't strictly on a tenure-track assistant professorship, but rather anyone who got a job in an academic setting.

**Industry**: Anyone who went to work at a private company was put into this category.

**Other*: This included jobs and institutions that weren't necessarily academia but also clearly were not industry. In this category included working at a government agency, a national lab, and non-profit think tanks.

In the cases where I didn't have a first job title, I used the first job location to define the job type.

### Summary


```
## 
## Academia Industry    Other 
##    61.70    30.85     7.45
```

![center](/figure/psu-phd-graduates-firstjobs/summary-1.png)

Based on the past 9 years worth of data, it seems that by and large our PhD graduates go into academia. Over 60 percent of our graduates end up in academia with their first job, a little over 30 percent go into private industry, while only about 7.5 percent go into that Other category. It seems that my initial impressions (and the answer I've been giving people) were wrong. And while these numbers might be inflated due to my broad definition of an academic job, it seems that our department largely prepares people for academia.

### Trends

I was curious to see if the trends behind these first jobs had changed over the time of the dataset. Was this pattern of mostly academic jobs relatively consistent, or have there been changes in the composition of jobs over time?

![center](/figure/psu-phd-graduates-firstjobs/trends-1.png)![center](/figure/psu-phd-graduates-firstjobs/trends-2.png)

It seems like there has definitely been changes in the category compositions over time. Initially, basically all graduates went into academia. However, around 2013, that trend started shifting, as a more even number of students went into industry. That trend reversed in 2016, though that change was mostly because of people going into the Other category. Last year was the first one in recent memory where more people went into industry than academia.

### Conclusion
My intuition that our department was roughly evenly split among the three types of jobs for graduates was obviously incorrect. Based on historical data, that split is closer to 60/30/10 for academia/industry/other. In recent years, however, that trend has been changing. I think it's fair to say that roughly 55-65 percent of our department's graduates go into academia, with the balance (35-45 percent) going into industry or some other type of job. This gives a much different picture of my department than I initially believed, one that (for obvious reasons) is more focused on training people for academia.

Of course, this kind of analysis has a lot of caveats. It's possible that people going into industry might not be as interested in filling out this information, or people going into jobs that they don't particularly like. It's also possible that a lot of the people who first get an academic job (notably, many of those who are lecturers or postdocs) might end up switching tracks and going into industry or some other type of job, while the reverse trend might be much less common. 

Nonetheless, this information does indicate that Penn State's statistics department does primarily focus on putting students into academic jobs. In any case, at least now I have a more accurate answer to the question of "Where do Penn State statistics PhD students go after they graduate?" the next time somebody asks.
