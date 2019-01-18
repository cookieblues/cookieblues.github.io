---
title: "Analysis of the biyearly evaluations at the IT University of Copenhagen, part 1: Data scraping"
layout: post
tags: ITUEVAL
excerpt_separator: <!--more-->
---
The [IT University of Copenhagen (ITU)](https://www.itu.dk/){:target="_blank"} conducts a student evaluation of the courses and the university itself each semester. The evaluations are one of the only ways that students can provide feedback to the lecturers, which can improve the learning environment, course material, exercises, and so on. The evaluations are also packed with interesting data, and naturally, as a data science student, I cannot keep my hands off them.\\
This analysis of the evaluations will be a series of posts, where I'll dive into some of the interesting data that we can get out of the evaluations. On top of that, these first few posts will serve as notes for the first project of the [First Year Project](https://mit.itu.dk/ucs/cb_www/course.sml?course_id=2708256&mode=search&lang=en&print_friendly_p=t&goto=1547640286.000){:target="_blank"} course. This time we'll focus on elementary [data scraping](https://en.wikipedia.org/wiki/Data_scraping){:target="_blank"}, which in its broadest sense is the act of collecting data.
<!--more-->

### Browser automation with Selenium
To scrape data, firstly, we'll need to find a place where our wanted data is located and free to use. Luckily, the ITU has made the evaluations publicly available on [their website](https://en.itu.dk/about-itu/organisation/facts-and-figures/quality-and-educational-environment/course-evaluation){:target="_blank"}. Also, I spoke to someone at ITU, and they said that we can do anything we want with the evaluations, as long as the data is publicly available. So far, so good.\\
Secondly, now we'll have to come up with a way to actually collect the data. The link on ITU's website leads to a webpage, where we can choose specific evaluation results for any evaluation period we desire. While the number of evaluation periods is small enough for us to manually collect the results, there are several benefits to not collecting the results this way. First of all, by avoiding performing a task the naive way we might learn something new. Second of all, if our method is broad enough, it might generalize to other tasks and save us time in the long run. Third of all, if we were to manually collect the results, the naive way would be to download the HTML pages, and afterwards clean the data for our purpose - however, we can clean the data as we collect it, if we don't do it the naive way.\\
Now, there are many ways to scrape data from websites, and depending on the specific website there might be a plethora of tools better suited for your purpose (public APIs, specific modules, etc.), especially if you want to scrape data from more popular sites. In this brief introduction to data scraping, we'll utilize [Selenium](https://github.com/SeleniumHQ/Selenium){:target="_blank"}, which is definitely not the most efficient library for browser automation, but we don't have a lot of data to scrape, and we want something that is user-friendly.

{% highlight python %}
from selenium import webdriver

driver = webdriver.Firefox()
url = "https://mit.itu.dk/ucs/evaluation/public.sml?lang=english"
driver.get(url)
{% endhighlight %}

We're going to use the WebDriver API from Selenium, which makes browser automation as intuitive as normal web browsing. By "getting" the URL, a new Firefox window will open, which is run by the driver. We can now manoeuvre around on the webpage by using the driver's functions and with a little bit of knowledge of [XPath](https://en.wikipedia.org/wiki/XPath){:target="_blank"}. By right-clicking on the webpage and looking at the page source, we can see that the radio buttons, that dictate the results you get, can be identified by their value. For now, we'll look at the evaluations of ITU in general, which is the radio button of value 0. We find the element through the driver, and click on it.

{% highlight python %}
driver.find_element_by_xpath(
    "//input[@type='RADIO'][@value=0]"
).click()
{% endhighlight %}

Then we want to select the evaluation period. We can use one of the WebDriver's support classes for this. With a bit of foresight, we can tell that we're going to do this a lot, so let's write a function that can do this for us. If we inspect the drop-down list, we can see that the different choices are called "2018october", "2018march", "2017october", "2017march", etc. (except for "2002april" which is the odd one out). We can use this as input in the function (as well as the driver). The second thing we can use is the submit method of a form in Selenium. By inspecting the site a bit more, we find that the evaluation results and periods all lie in a form. After choosing our desired evaluation results and period, we can submit the form and get to the next page.

{% highlight python %}
from selenium.webdriver.support.ui import Select

def enter_eval_period(period,driver):
    evaluation_form = driver.find_element_by_xpath("//form[1]")
    evaluation_period = Select(evaluation_form.find_element_by_name("dir"))
    evaluation_period.select_by_value(period)
    evaluation_form.submit()

enter_eval_period("2018october",driver)
{% endhighlight %}

The next page lets us choose, which students (part- or full-time) we want the evaluations for. While I don't want the analysis to be overly thorough, I will scrape the evaluations from part-time students and full-time students individually - even though there are way fewer part-time students. Since both boxes are checked, we'll just make a function that unchecks the full-time students.

{% highlight python %}
def pick_parttime(driver):
    student_form = driver.find_element_by_xpath("//form[1]")
    student_form.find_element_by_xpath(
        "//input[@type='CHECKBOX'][@value='orduni']"
    ).click()
    student_form.submit()

pick_part_time(driver)
{% endhighlight %}

### Scraping data with BeautifulSoup and Pandas
BeautifulSoup is a wonderful library for parsing HTML documents, and it works naturally together with Pandas. We're currently in the part-time students' evaluations for October, 2018. We have some numerical data at the top of the page in a table, and the textual data is underneath in lists. To get the table data, we can use BeautifulSoup to parse the page source, find the table we need, and then use Pandas to put the table in a DataFrame.

{% highlight python %}
import pandas as pd
from bs4 import BeautifulSoup

def get_numerical(driver):
    soup_page = BeautifulSoup(driver.page_source)
    table = soup_page.find_all("table")[3]
    df = pd.read_html(str(table),header=1)[0]
    return df.rename(columns={"Unnamed: 0":"statement"})

numerical_df = get_numerical(driver)
{% endhighlight %}

To quickly explain the function: it turns out, it's the fourth (index three) table that we need. Pandas' read_html function returns a list, since it expects a list of tables, however, we only give it one, and therefore we take index zero. We also set the second (index one) row to be the header as the first row is irrelevant. Lastly, we rename the first column for readability. This gives us the numerical data in a DataFrame.

The next thing we need is the textual data. This is a little more complicated, since the textual data is wrapped in a lot of lists. By inspecting the page source, we can see that all the textual evaluations are wrapped in ul tags. By further inspection, every fourth ul tag are "Good things about the IT University", and the ones following are "Things that could be improved". We could grab all the ul tags and use some regular expressions to get what we want, [but you should not attempt to parse HTML with regex](https://stackoverflow.com/a/1732454){:target="_blank"}. In each ul tag we have li tags, where only a few contain text that we need. The function below gets us exactly what we want.

{% highlight python %}
def get_textual_1(driver):
    soup_page = BeautifulSoup(driver.page_source)
    good = list()
    bad = list()
    for idx,ul in enumerate(soup_page.find_all("ul")):
        if idx % 4 == 1:
            bad += [evaluation.get_text() for evaluation in ul.find_all("li")]
        elif idx % 4 == 0:
            good += [evaluation.get_text() for evaluation in ul.find_all("li")]
    df = pd.concat([pd.Series(good),pd.Series(bad)],axis=1)
    return df.rename(columns={0:"good",1:"bad"})

textual_df = get_textual_1(driver)
{% endhighlight %}

You might have noticed that I called this function get_textual_1, and that's because a few of the evaluations follow a slightly different template. For the other template we can use the following function, which follows the same idea.

{% highlight python %}
def get_textual_2(driver):
    soup_page = BeautifulSoup(driver.page_source)
    good = list()
    bad = list()
    for idx,ol in enumerate(soup_page.find_all("ol")):
        if idx:
            bad += [evaluation.get_text() for evaluation in ol.find_all("li")]
        else:
            good += [evaluation.get_text() for evaluation in ol.find_all("li")]
    df = pd.concat([pd.Series(good),pd.Series(bad)],axis=1)
    return df.rename(columns={0:"good",1:"bad"})

textual_df = get_textual_2(driver)
{% endhighlight %}

If we use the wrong function for an evaluation template, we'll return an empty DataFrame. We can therefore make one function that takes care of both scenarios.

{% highlight python %}
def get_textual(driver):
    if get_textual_1(driver).shape[0] != 0:
        return get_textual_1(driver)
    else:
        return get_textual_2(driver)
{% endhighlight %}

We can now go back, enter the full-time students' evaluations, scrape their data, and go all the way back to choosing a different period. A simple back method exists for the driver.

{% highlight python %}
driver.back()
{% endhighlight %}

Coming back from the part-time students, we have to uncheck the part-time students and check the full-time students.

{% highlight python %}
def pick_fulltime(driver):
    students_form = driver.find_element_by_xpath("//form[1]")
    students_form.find_element_by_xpath(
        "//input[@type='CHECKBOX'][@value='openuni']"
    ).click()
    students_form.find_element_by_xpath(
        "//input[@type='CHECKBOX'][@value='orduni']"
    ).click()
    students_form.submit()
{% endhighlight %}

That's it! We can now go through all the different evaluation periods, scrape the data, and save the DataFrames.


