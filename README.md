# Setup/Start
- open finals folder or place files in the same dir.
- load terminal preference.
- call the python files. e.g. py averageplot.py

# Data Analysis Checklist 7/2020
[] Load the Data
- Data loaded correctly
- Data types didn't at first match my expectations # started removing variables I don't want to deal with and converting to csv.

[] Describe and Explore Data
- Data is distributed in a blank format after scraping it from the web, need to convert it, 
to a csv file to start data analysis # get the freqency of heights, and weights and reaches etc.
- Groupby to determine frequency of values in a column. # get the freqency of heights, and weights and reaches etc.
x For continuous variables create a histogram
- Any outliers # yes there is a records value that sometimes has '(1 NC)' for No contest fighters, where a fighter was disqualified and it didnt add to their win/loss/dq ratio. They will impact my analysis and I would like to remove them from the data, but still showcase them as a possible factor.
- Issues with missing data? Why might data be missing? Is it possible that will impact your analysis?
- Yes I have an issue with missing data, and the data is missing because it was not inputed into the database or they just don't have accurate, up to date information to input. For certain fights this will greatly impact my analysis and it will create more of a timesink in collecting data for certain fighters. I think the best route to take is to focus on a fighter that has been around for a long time and only show fighters that have no blank values in their data.

[] Research your Topic
- See what others have done to do better analysis. # don't reinvent the wheel.

[] Build your Analysis Plan
- What data do you need to solve your problem? # index based on fighters names who they're versus and how their stats compare to average of
all fighters in the data and also vs each other.
- Need to clean the data? # I do need to clean the data, and fix up Nan / NoneType values when trying to create averages/freqency lists.
- no new columns need to be created, except maybe one for index values
- What techniques can you use to answer your question? # simple math for the most part, and iterating over a csv column-rows. Specifically, round, title, sum/len, list comprehension, if/elif/else statements, csv module, indexing/slicing, functions # start simple, chunk the problem up, tackle chunks
- What do you consider a successful answer? # I'd love to explore if the fighter stats correlate into their wins, directly.  If a fighter has better stats than another fighter, do they usually win? Y/N and if yes, then this is a good odds calculator, otherwise it could be random, and more change. but the successful answer will be a percentage of how effect comparing stats is. Trying to see if stats matter to predict fights.

[] Turn your plan into code
- Put your plan into action

[] Explore the possibilities
- Add a visual component to your final
