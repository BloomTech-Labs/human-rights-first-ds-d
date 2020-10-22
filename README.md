# Human Rights First Police Use of Force Map

You can find the deployed project at [This Address](https://boiling-retreat-77102.herokuapp.com/).

#### Additional Repos used for this project
- [Front End](https://github.com/Lambda-School-Labs/Labs27-D-HRF-FE)
- [Back End](https://github.com/Lambda-School-Labs/Labs27-D-HRF-BE)
## The Team
- [Hira Khan](https://github.com/Hira63S)[<img src="https://github.com/favicon.ico" width="15"> ](https://github.com/Hira63S)   [ <img src="https://static.licdn.com/sc/h/al2o9zrvru7aqj8e1x2rzsrca" width="15"> ](https://www.linkedin.com/in/hira-shahid-991b1583/) - Team Project Lead

- [Cedric Winbush](https://github.com/caw442000)[<img src="https://github.com/favicon.ico" width="15"> ](https://github.com/caw442000)   [ <img src="https://static.licdn.com/sc/h/al2o9zrvru7aqj8e1x2rzsrca" width="15"> ](https://www.linkedin.com/in/cedricwinbush/) - Team Project Lead

- [Virginia Davenport](https://github.com/virginia-d90)[<img src="https://github.com/favicon.ico" width="15"> ](https://github.com/virginia-d90)   [ <img src="https://static.licdn.com/sc/h/al2o9zrvru7aqj8e1x2rzsrca" width="15"> ](https://www.linkedin.com/in/virginia-davenport/)   - Back End Engineer

- [Juan Rivera](https://github.com/Juan-Rivera)[<img src="https://github.com/favicon.ico" width="15"> ](https://github.com/Juan-Rivera)   [ <img src="https://static.licdn.com/sc/h/al2o9zrvru7aqj8e1x2rzsrca" width="15"> ](linkedin.com/in/juan-rivera-dev) - Back End Engineer

- [Barbara Moore](https://github.com/barbaralois)[<img src="https://github.com/favicon.ico" width="15"> ](https://github.com/barbaralois)   [ <img src="https://static.licdn.com/sc/h/al2o9zrvru7aqj8e1x2rzsrca" width="15"> ](https://www.linkedin.com/in/barbaralois/ ) - Front End Engineer

- [Blayze Stone](https://github.com/blayzestone)[<img src="https://github.com/favicon.ico" width="15"> ](https://github.com/blayzestone)   [ <img src="https://static.licdn.com/sc/h/al2o9zrvru7aqj8e1x2rzsrca" width="15"> ](https://www.linkedin.com/in/blayze-stone/) - Front End Engineer

- [Marta Krawczyk](https://github.com/MartaKode)[<img src="https://github.com/favicon.ico" width="15"> ](https://github.com/MartaKode)   [ <img src="https://static.licdn.com/sc/h/al2o9zrvru7aqj8e1x2rzsrca" width="15"> ](https://www.linkedin.com/in/marta-janina-krawczyk/) - Front End Engineer

- [David Cruz](https://github.com/DAVIDCRUZ0202)[<img src="https://github.com/favicon.ico" width="15"> ](https://github.com/DAVIDCRUZ0202)   [ <img src="https://static.licdn.com/sc/h/al2o9zrvru7aqj8e1x2rzsrca" width="15"> ]( https://www.linkedin.com/in/daavidcruuz/) - Data Science Engineer

- [Johann Augustine](https://github.com/DataLovecraft)[<img src="https://github.com/favicon.ico" width="15"> ](https://github.com/DataLovecraft)   [ <img src="https://static.licdn.com/sc/h/al2o9zrvru7aqj8e1x2rzsrca" width="15"> ](https://www.linkedin.com/in/johannaugustine/) - Data Science Engineer
<br>
<br>


## Project Overview

[Trello Board](https://trello.com/b/685sxSXo/team-d-2009)

[Product Canvas](https://whimsical.com/U1CQr6HWFXTPn8WnGbEww)

Our team is developing an interactive map that identifies potential instances of police use of force across the United States of America for Human Rights First, an independent advocacy and action organization.

We're pulling data from similiar APIs(All locations V2 - https://raw.githubusercontent.com/2020PB/police-brutality/data_build/all-locations-v2.json, 846- https://api.846policebrutality.com/api/incidents) and from Twitter and Reddit. We want to identify aggregate these instances.

### Key Features

- Interactive Map
- Filters for refined searches
- Classification Model for potential cases of Police Brutality
- Statistical History of police databases for comparison

##  Tech Stack

### Data Science API built using:

- Heroku:
Used for API hosting. AWS EB is even better, future teams should strive to deploy there instead!
- FastAPI:
Useful for automatic JSON-ification of objects. Makes it easier to pass information back and forth between DS and Backend
- Uvicorn: ASGI server implementation which handles asyncronous data sending and receiving from multiple threads and/or processes.

### Libraries used

- Pandas
- scikit-learn
- spacy
- nltk
- PRAW
- Tweepy

#### Data Science API should be deployed to AWS EB. HRF Team D in Labs 27 is providing back-up information for deploying to Heroku, in case it's necessary.

## Data Science API

We are sending json objects to the backend with information about instances of police use of force. This information includes location data (city, state, and geocode) and relevant details about the incident, like the type of force that was used.

## 2️⃣ PRAW

PRAW, The Python Reddit API Wrapper, makes it easy for users to analyze Reddit data. We used PRAW to scrape Reddit for potential instances of police of force.

## 3️⃣ Tweepy

Tweepy is a Python library that allows users to access the Twitter API. We used Tweepy to scan Twitter to find instances of police use of force.

# 3️⃣ Environment Variables

In order for the app to function correctly, the user must set up their own environment variables. There should be a .env file containing the following:

    *  PRAW_CLIENT_ID  - keys for Reddit API
    *  PRAW_CLIENT_SECRET - keys for Reddit API
    *  PRAW_USER_AGENT - keys for Reddit API
    *  TWEEPY_CONSUMER - keys for Twitter API
    *  TWEEPY_SECRET - keys for Twitter API
    *  TWEEPY_ACCESS - keys for Twitter API
    *  TWEEPY_ACCESS_SECRET - keys for Twitter API

# 4️⃣ Installation Instructions

[Deploy to AWS EB](https://docs.labs.lambdaschool.com/data-science/#tech-stack)
[Deploy to Heroku](https://davidcruz0202.github.io/2020-10-19-HRF/)
[Help with Conda Environments](https://medium.com/@nrk25693/how-to-add-your-conda-environment-to-your-jupyter-notebook-in-just-4-steps-abeab8b8d084)
# Contributing

When contributing to this repository, please first discuss the change you wish to make via issue, email, or any other method with the owners of this repository before making a change.

Please note we have a [code of conduct](./CODE_OF_CONDUCT.md). Please follow it in all your interactions with the project.

## Issue/Bug Request

**If you are having an issue with the existing project code, please submit a bug report under the following guidelines:**

- Check first to see if your issue has already been reported.
- Check to see if the issue has recently been fixed by attempting to reproduce the issue using the latest master branch in the repository.
- Create a live example of the problem.
- Submit a detailed bug report including your environment & browser, steps to reproduce the issue, actual and expected outcomes, where you believe the issue is originating from, and any potential solutions you have considered.

### Feature Requests

We would love to hear from you about new features which would improve this app and further the aims of our project. Please provide as much detail and information as possible to show us why you think your new feature should be implemented.

### Pull Requests

If you have developed a patch, bug fix, or new feature that would improve this app, please submit a pull request. It is best to communicate your ideas with the developers first before investing a great deal of time into a pull request to ensure that it will mesh smoothly with the project.

Remember that this project is licensed under the MIT license, and by submitting a pull request, you agree that your work will be, too.

#### Pull Request Guidelines

- Ensure any install or build dependencies are removed before the end of the layer when doing a build.
- Update the README.md with details of changes to the interface, including new plist variables, exposed ports, useful file locations and container parameters.
- Ensure that your code conforms to our existing code conventions and test coverage.
- Include the relevant issue number, if applicable.
- You may merge the Pull Request in once you have the sign-off of two other developers, or if you do not have permission to do that, you may request the second reviewer to merge it for you.

### Attribution

These contribution guidelines have been adapted from [this good-Contributing.md-template](https://gist.github.com/PurpleBooth/b24679402957c63ec426).
