# Labs 27 Jupyter Notebook folder

notebooks     <- Jupyter notebooks. Naming convention is a number (for ordering),
    │            the creator's initials, and a short `-` delimited description, e.g.
    │            `1.0-jqp-initial-data-exploration`.
    │            `_dc_newspaper3k_spacy_exploration`.
    │            `1_dc_data_exploration`.
    │            `Data_Cleaning_Labs`.
    │            `dc_data_praw_newspaper3k`.



See 0.0-template to get started. 

Notebooks from Labs 25 used as reference only. 

### Scraping References

'Data_Cleaning_Labs' contains methods useful for refining additional statistical data sets.

'dc_data_praw_newspaper3k' provides steps to scraping reddit data, and parsing that data using the newspaper library.

'_dc_newspaper3k_spacy_exploration' holds exploratory NLP techniques using the SpaCy library, implemented on text data parsed using newspaper3k.

'1_dc_data_exploration' shows exploration done using the PRAW library. This is how reddit scraping is completed. 

Think of these questions to help guide you during your scraping:

 * What library will I use to scrape stories?(example: PRAW for reddit)

 * How will I extract the story text ? (example: newspaper LIbrary)

 * What library will I use to parse the stories and titles?(example: NLTK)

 * How will I send this data through to backend? (example: FastAPI)

For more directions and guidance, check the data directory, and the project directory.