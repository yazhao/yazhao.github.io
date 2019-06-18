Title: Don't p-hack: Three Lessons for Data Science in a Public Relations Setting
Date: 2018-11-14
Slug: dont-p-hack
Tags: statistics, business, marketing, public relations, pr

I used to work as a data analyst on the marketing team at [GrubHub](https://www.grubhub.com/), an online food delivery company. During this time, some of the more interesting data science tasks I was given included trying to find insights for our public relations team. Some of these were based on current events, like for this article about [food orders during the 2012 election](https://www.huffingtonpost.com/2012/11/07/election-night-food-delivery-grubhub_n_2090161.html). Others were more self-directed, like this analysis a colleague did for NPR about [pizza size and value](https://www.npr.org/sections/money/2014/02/26/282132576/74-476-reasons-you-should-always-get-the-bigger-pizza).

I thought of this because of an article I read earlier this year about [Brian Wansik](https://www.buzzfeednews.com/article/stephaniemlee/brian-wansink-cornell-p-hacking#.bmxLG1XPpN), a Cornell professor whose work garnered widespread media attention over the years before it was found that he had committed scientific misconduct. Specifically, Wansik "p-hacked," manipulating his data and analysis until he got a p-value below 0.05, the generally accepted threshold for [statistical significance](https://en.wikipedia.org/wiki/Statistical_significance). And while academic and public relations are very different fields, what Wansik did wrong can still help to guide data science for public relations.

### Lesson One: Don't p-hack

This is the most immediate takeaway from Wansik's mistakes. It should be obvious that trying to manipulate your data and analysis to get a significant result is a bad idea. To be clear, this doesn't preclude subsetting or otherwise adjusting your approaching during the course of your analysis, but it does mean that once you get a bad result, you can't just keep changing things until you get a good result.

At a conceptual level, it might be difficult to tell the difference between p-hacking and legitimate adjustments of data or analyses in order to correct for mistakes or other problems with what you have done. In general, though, if you are:

1. Precommitting to a hypothesis beforehand (that is, before you get the data or start diving into it), and
2. You have reasonable explanations or hypotheses for why you are adjusting your data approach (for example if you believe that there is a seasonality effect), and
3. You are adding, not removing information (adding more variables or columns), with the exceptions of,
4. a. Adding more to your sample size indefinitely (which will inevitably get you a significant p-value), or
   b. Removing outliers

Then what you're doing will tend to stick to the right side of the legitimate adjustment/p-hacking line.

### Lesson Two: Precommit to hypotheses (and some other stuff) beforehand

As highlighted in the guidelines above, and as a general good practice, you should commit to what hypothesis you want to test beforehand. If you believe that you have a question that people would find interesting, clearly articulate what it is before you start doing analysis on the data. If you're collecting the data yourself, you need to make sure you specify how many observations you'll be collecting as well as what information you want. This avoids two common problems that can lead to bad data science. First, it prevents the scenario where you are blindly digging around the data just to find something interesting (which leads to p-hacking). Second, it prevents retroactively creating a hypothesis based on data you've already looked at. This kind of retroactive hypothesis is especially bad because it defeats the entire purpose of doing data science. Creating a retroactive hypothesis is like looking up spoilers for a movie before seeing it and then making a prediction about how it ends: it is no great feat of analysis to "predict" an answer you already know, and using the data to generate your hypotheses retroactively means that your analysis is not particularly helpful or useful.

### Lesson Three: If not testing, list out your methodology beforehand

Not all data science for public relations involves answering questions with a kind of yes or no answer like the one about whether food orders increased on election night. The staple of any kind of analysis done for PR is usually the list, where a company either releases the "most popular X in country Y" or "the most popular Z by state/province" or "the cities with the most (blank)."  There's nothing wrong with this kind of work, but two good rules to follow include:

1. Making your sure explicitly define what metric you're ranking by, and
2. Making sure you specify any kinds of adjustments you'd do to the rankings to make it not just dominated by the most popular answer

The second rule is mostly done because places with higher populations will just generally have more of something, and it is extremely boring if every ranking just had say New York first (sometimes people want to see if something is disproportionately popular in a place, for example). In general, try to avoid constantly remaking your rankings just because you think that the results are not to your liking. This is a good rule of thumb whenever you do data science, but especially so when you're dealing with PR work, because such work is prone to suffering from this problem.

### Bottom Line

While there might be some edge cases here and there when dealing with this kind of work, in general these lessons are good guidelines for making sure that your data science work for PR purposes is both interesting and analytically sound. In short, if you

1. State out what you want to test or how you're ranking before you start doing the analysis
2. Don't constantly readjust your analysis just because the results are not to your liking
3. Don't try to cut up your data by subsetting in order to "salvage" a result

You should be able to produce insightful data science work that both is generally sound and will give your marketing teams something worthwhile to generate PR.