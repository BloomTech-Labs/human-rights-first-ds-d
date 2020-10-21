Each file holds respective labs groups work.

Labs 27 did a lot of exploration and analysis in the hopes of setting up future teams for success. We were assigned to gather more data from different sources. Between scraping various government entities for statistical data , and using PRAW to dig deeper into Reddit's rich sub-communities , we have pulled together various sources of potential stories to add to the deployed app. 

logisticregression.ipynb is a different approach to the classification model currently being implemented. We used stratification to split our data before training the model . Comparing resulting accuracies proves to show that the model ends up being overfit. This can be further analyzed with evaluation metrics such as ROC/AUC , PCA, and validation curves.

Data_Cleaning_Labs.ipynb holds the data cleaning done on two of the government sources used for the statistical data set. This includes data cleaning techniques such as dimensionality reduction through feature removal, and checking value counts to ensure consistency among data sets.

dc_data_praw_newspaper3k.ipynb and _dc_newspaper3k_spacy_exploration.ipynb both hold data exploration tactics which are useful . The methods used in these notebooks can also be found in "reddit_pull.py" which resides in the project directory. We used PRAW to scrape stories directly from reddit. These stories can have their titles be evaluated with NLP using the spacy library. We can also scrape the full story text through the newspaper library, which can also be evaluated for police brutality by passing the text through a text parser like SpaCy or NLTK.

Read through the notebooks above to get a feel about how to approach this problem. Use reddit_pull.py to see what a resulting .csv of stories can potentially look like. 

For a project to be a home-run success, all of these pieces must come together.

* An interactive web app with live endpoints
* Endpoints should serve backend by providing either freshly pulled news stories, or statistical data depending on what's needed
* A classification model which filters news stories into cases of police brutality, or not .
* Thorough documentation for the next team to be able to pick up where the last left off, and improve / explore upon the methods implemented.