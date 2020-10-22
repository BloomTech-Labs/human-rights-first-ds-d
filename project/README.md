# Labs 27 Updates

* Predict route is now a functional endpoint with a story ID as input. Based on the ID of the story, this endpoint will predict whether or not the story is a case of police brutality, what category of police brutality it falls under, and whether or not lethality was a factor.
* /update endpoint is used to populate the backlog with new stories
* /getdata is used to send the backlog in JSON format to the backend

## Starter Tips

* Make sure to follow the [DS Starter Guide](https://docs.labs.lambdaschool.com/data-science/#tech-stack) to deploy your DS API. Once you're fully deployed, you can begin working on your endpoints.

* Before working on any models or data collection techniques, make sure to properly set up your local environment. [Use this page for guidance](https://medium.com/@nrk25693/how-to-add-your-conda-environment-to-your-jupyter-notebook-in-just-4-steps-abeab8b8d084)

* reddit_pull.py holds a separate python script. When this file is executed, it will populate a .csv of reddit stories from the "police_brutality" subreddit. *Make sure to set up your local environment before running the file. The code in this file can be useful in your implementation of your deployed app