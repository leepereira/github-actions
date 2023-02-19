# github-actions

## how does this work

- update the code in the app.py file. This is the code for the Flask
- Commit the code 
- This should run github workflow that would build the image and push it to the docker registry
- Push will be to the following dockerhub repo : leepereira/hayden:latest
- Once Job completes, validate  that the image has been pushed to dockerhub.io

Perform a pull locally on the machine
```bash
docker pull leepereira/hayden:latest
```

Run the image locally 
```bash
docker run -p 5000:5000 leepereira/hayden:latest
```

Check the update on the webpage at : http://localhost:5000

