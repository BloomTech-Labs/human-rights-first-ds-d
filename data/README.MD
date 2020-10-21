data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.

police_use_force.csv - A CSV with two columns. Col[name] is the name of a story. col[police_brutality] is irrelevant(never varies)

news.csv - A CSV with 1000 scraped news headlines.

redditbrutality_posts.csv - A csv with recent reddit posts and URL's to the linked stories. Missing datetime stamps, but these can be pulled using PRAW.