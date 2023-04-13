Here's the "rubric":

- Here are the **suggested sections** of your Final Report:
    - **Introduction**: A short paragraph introducing your project to the audience and a motivation for why this project is important. It's fine to say your group has an interest in this topic and were keen to explore it more.
    - **Exploratory Data Analysis**: A summary of the **highlights** of your EDA, where you can show some visualizations of the exploratory data analysis your group did.
    - **Question 1 + Results**: Clearly state your research question, and include 2-3 visualizations that helped you answer your research question. You can create multi-panel figures, but each of your visualizations must speak directly to your research question, and any insights you were able to get from it should be clearly articulated in the figure caption/description.
    - **Question 2 + Results**: Same as above.
    - **Question 3 + Results**: Same as above.
    - **Summary/Conclusion**: A brief paragraph that highlights your key results and what you learned from doing this project.


## Introduction

Given the increasing advocacy towards mental health and mental health support, we primarily aimed to explore how music may impact mental wellbeing, considering the influence of diverse music genres, amount of music listening, and extent of involvement with music. Eventually, we decided to explore the correlation of some additional factors to mental health as well, to further enrich our project. Utilizing our findings, we have produced detailed, comprehensive data visualizations that will aid the general public in understanding the influence of music and additional factors on their mental health.  


## Exploratory Data Analysis

![graph 1](images/analysis1eda1.png)
<br>

I conducted an initial analysis on the distribution of anxiety and depression scores for those who identified as composers, instrumentalists, both or neither. The figure demonstrates that the group that did not participate in either composing or instrument playing was very concentrated towards the higher ends of the spectrum for both anxiety and depression. A similar concentration is observed for other groups, but they are not as severe. 
<br>

![graph 1](images/analysis1eda2.png)
<br>

We were interested in the distribution of the four mental health conditions, anxiety, depression, insomnia, and OCD. Based on this figure, we could learn that overall, anxiety was more severe at an average of around 6, whereas OCD was the least severe at an average of around 2.

## Question 1 + Results (Alyssa Kong)
**What is the relationship between the active participation of music in one's lifestyle (composing, playing an instrument, listening to music on a greater than average amount, or neither) in relation to the severity of mental health disorders among these individuals? How do these factors influence how they percieve the effect of music?**

To answer this question, I grouped individuals into four groups: composers, instrumentalists, both, or neither. I then created an "Overall Mental Health" score based on the four components of anxiety, depression, OCD and insomnia. Anxiety and depression was 35% of this score, insomnia was 20% and OCD was 10%. The higher the score reflected more degrees of anxiety, depression, insomnia, and OCD.
<br>

Figure 1: Effects of Music Participation on Mental Health.

![graph 1](images/analysis1graph1.png)

As seen in Figure 1, there is no strong correlation demonstrated between different types of music participation and overall mental health scores. All four categories had a concentration of overall mental health scores at around the 4-6 range. It should be noted on this figure that the composer group had lower data points than the other groups.
<br>

Figure 2: Overall mental health based on hours of music listened to per day. 
![graph 2](images/analysis1graph2.png)<br>

Figure 2 also demonstrates that there is no correlation between overall mental health scores and amount of time spent listening to music. Hours of day spent listening to music was calculated based on a standardized percentage, based on the maximum value, standard deviation, and the mean of the dataset. The percentage of hours per day spent listening to music centers at around 0%-20%, which translates to about 1-4 hours per day. The overall mental health, however, is evenly distributed therefore no strong relationship is demonstrated.
<br>

Figure 3: Type of Music Participation and percieved effects of music.
<br>

![graph 3](images/analysis1graph3.png)

<br>
In Figure 3, all four groups of music participation demonstrated that it is mostly percieved that music improves mental health. Almost 60-80% of each group believed that music improved mental health, whereas 20-30% believed it had no effect, and 0-20% believed it had a worsening effect. Out of all the groups, the composing group had the most amount of individuals who believed that music improved mental health, whereas the group that did not participate in either activity, had the least amount of individuals who believed music improved mental health.

Based on the figures demonstrated above, there is no correlation between those who participate in different types of music and their reported severity in their overall mental health. This is shown in the violin chart, where the data is pretty much centered around the 4-7 range in terms of overall mental health score for each group of individuals. In addition, there is also no correlation between the amount of music listened to per day and the overall mental health of an individual. This can be seen in the hex-plot figure, where the overall mental health is pretty much evenly distributed for each hour of music listened to per day. Despite this, it can be seen that the type of music participation can affect how the music effects on mental health is percieved. Those who are composers tend to report that music improved their mental health moreso compared to those who did not participate in music composing or playing. However, it can be seen in the heat map that all three groups percieve music to have a positive effect on their mental health in general.

## Question 2 + Results (Haider Mohammad)

**Is there a correlation between the frequency of how often individuals between the ages of 15-30 listen to their favourite music genre, and if those habits have any underlying effects on mental health conditions? Are there external factors impacting greater insomnia levels for people who listen to more EDM?**

### Figure 1: Mental Health Score for Each Genre

![graph 1](images/analysis2graph1.png)

In my dataset, I made a column titled "Mental Health Score" which found the average between an individuals anxiety, depression, and insomnia levels. Based on this, I compared those numbers to people's favourites genres to get a big picture of how music genres are connected to mental health conditions. I got these results by creating a facet grid. The results were pretty interesting since genres like Jazz, Rock and EDM showed higher levels of mental health levels compared to genres like Country, Classical and Folk. 

Obviously these numbers don't paint the full picture but it's a good starting point to see if specific genres have different effects on the mind. I also understood there are many factors affecting these results, therefore, I did more research to answer these questions.

### Figure 2: Correlation Between Frequency of Music Genres and Mental Health Conditions  

![graph 2](images/analysis2graph2.png)

To go more in depth, I wanted to see the relationship between each genre and mental health condition, instead of an average of mental health. This would allow me to see some genuine patterns worth studying. Based on my results, I found the following correlations interesting along with my initial thoughts:
1. EDM and Insomnia (positive relationship)
    - This is by far the strongest correlation at 0.21. Electronic Dance Music (EDM) is intended for large crowds of dancers which is far from ideal for sleeping. Listening to EDM before sleeping would make it hard to sleep.
2. Jazz and Insomnia (positive relationship)
    - Jazz requires a lot of different instruments such as trumpet which can be disturbing for those trying to sleep. Similar to EDM, it does make sense why Jazz might lead to bad sleep.
3. EDM and Anxiety (negative relationship)
    - This is the first negative relationship meaning EDM reduces anxiety? It's certainly interesting but I suppose going to places like clubs and parties where EDM is most used could help people forget their troubles for a little bit

### Figure 3: Average EDM Frequency by Insomnia

![graph 3](images/analysis2graph3.png)

Through figure 2, I started going more in depth with the EDM and Insomnia relationship. I found there was a direct connection between the two by making a line chart on Tableau. I studied alchol and smoking consumptions levels and determined those two factors were not necessarily affecting EDM and Insomnia. This was because alchol and smoking levels were increasing as age increased while insomnia levels decrease, suggesting there wasn't a strong enough connection between acohol/amoking and insomnia. 

While EDM likely isn't the only reason behind insomnia, I think it's fair to assume it plays a role based on the research. However, additional research would be required to determine the exact percentage of indluence. 

To see my [entire analysis](https://github.com/ubco-W2022T2-data301/project-group-group12/blob/main/analysis/analysis2Haider.ipynb), you can access my full work.

## Question 3 + Results (Zainab Mohammad)

**Do either the amount of daily music listening or age have an effect on an individual's mental health, and if so, what are the correlation patterns?**

<img src ="images/analysis3graph1.png" class="center"><br>

As visualized in Figure 1, there are two lineplots. The one on the left plots the average ranking of the four mental health conditions against the percentage of day spent listening to music. For all four conditions, a positive correlation is seen, such that as the percentage of music listening in a day increases, the overall average ranking of each of the mental health conditions also increases. This positive correlation can be identified due to the plotted trendlines (dashed gray lines), which increase in the upwards direction for all four of the subplots. Next, the lineplot on the right plots average ranking of the four mental health conditions against age. For all four conditions, the respective trendlines go in the downwards direction as age increases, which suggests a negative correlation between average mental health problems and age. This means that as age increases, the overall average ranking of each of the mental health conditions decrease, such that older individuals experience less mental health problems. Since younger populations experience more mental health problems, an additional dataset was explored which correlated academics (specifically a student's GPA and year of study) to mental health; analysis and visualizations for that can be found in the [analysis file](analysis/analysisZainab.ipynb). 


**Sub-question: Does the choice of primary streaming service (for listening to music) have a correlation with mental health?**

<img src ="images/analysis3graph3.png" class="center"><br>

After discovering the correlation of music listening and mental health conditions, I was curious to explore another aspect of music. I decided to examine if the music streaming service that an individual chooses to use also has an effect on the four different mental health conditions or not. I chose to evaluate the mode values of the rankings since this would indicate what the most common ranking for a mental health condition was for different primary streaming service users. For this purpose, heatmaps seemed logical, as are visualized in Figure 2. Scales are provided for each heatmap, to their right.
<br>

The heatmap at the top left is for anxiety, and it showed the mode rating of anxiety to be around 7 (either 6, 7, or 8) for all the various streaming service users. The heatmap on the bottom left is for insomnia, and it showed the mode rating of insomnia to be around 1 (either 0, 1, or 2) for all the various streaming service users. The heatmap on the bottom right is for OCD, and it showed the mode rating of OCD to be 0 for all the various streaming service users. These three heatmaps all indicate the same results, that **the mental health conditions anxiety, insomnia, and OCD do not have a strong correlation to the choice of streaming service.** 
<br>

The notable heatmap is the top right one, which is for depression. The mode value of rated depression was a 6 by Spotify users, a 0 by Pandora users, a 2 by YouTube Music users, a 5 by Apple Music users, a 2 by users not using any streaming service, and 0 and 6 (bimodal) by users using other streaming services. Most of the mode values were on the lower end of the range, but both Spotify users and Apple Music users had relatively higher mode values, indicating that **Spotify and Apple Music users tend to have higher depression levels than all other music listeners**. Also, Pandora had the lowest mode value of 0, suggesting **Pandora users experience the least amount of depression.** 


<img src ="images/analysis3graph4.png" class="center">
<br>

Figure 3 was created to prove the findings concluded from Figure 2. The barplot has the average values of the various streaming service options plotted against the rating of depression (on a scale out of 10), and indeed, it can be seen that **Spotify and Apple Music users both have relatively higher average depression scores of over 5, whereas all other averages are around 4 or less. Pandora clearly has the lowest average, indicating that Pandora users are indeed the least depressed.


## Summary/Conclusion

In conlusion, our chosen datasets yielded lots of fascinating trends. 

Alyssa and haider summarize their results:

There is a positive correlation between daily music listening and mental health conditions, and negative correlation between age and mental health conditions. This implies that younger individuals who listen to more music every day likely have much worse mental health than older individuals who listen to minimal music in a day; younger individuals may have worse mental health due to academic reasons, like a lower CGPA and higher year of study. Lastly, it was found that Spotify and Apple Music users are likely to have higher levels of depression and Pandora users are likely to have lower levels of depression, compared to all other streaming services users; in contrast, for anxiety, insomnia, and OCD, the severity of each mental health condition was generally similar in all users regardless of which streaming service was used. 

In closing, the idea of "correlation does not imply causation" should be revisited- just because we witnessed correlation between various variables through this project does not imply causation, so further research should be conducted before these results can be further published. It should also be noted that repeating these surveys may also be worthwhile as that will increase the sample size, allowing for more accurate results. 







Further detail on Zainab's analysis and conclusions can be found [here](analysis/analysisZainab.ipynb).





During EDA, I made the overall mental health plots. explain why I kept outliers, and why I made individual plots for each mental health condition instead of keeping it as one. 












Based on our earlier conclusion that the quantity of music listening and mental health problems have a positive correlation. Based on these previous questions, it can be seen that overall, people rank their mental health problems quite high on the scale, especially their anxiety and depression. Thus, it suggests that even though a lot of people are listening to music for only around 8.3% (and __) of their days, they should try to further lessen this number as this may help bring down their mental health problems. 


Ok now. The first set of research questions yielded very interesting results. Since depression and anxiety are the two most prevalent mental health conditions based on the box plot, and we learned that younger populations tend to suffer more, i thought i’d explore to see what other factors may be contributors. Young populations often include students, so I found a dataset on student mental health. This dataset correlates anxiety and depression presence to year level and CGPA. I wanted to learn if either of these factors possibly contribute to anxiety and depression:









