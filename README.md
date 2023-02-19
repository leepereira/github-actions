# github-actions

## how does this work

- update the code in the app.py file. [function/app.py] This is the code for the Flask
- you can just change the function/app.py at https://github.com/leepereira/github-actions/blob/main/function/app.py#L6 and change the return message.
- this is just to simulate a new version update to the app. 
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

Next steps to be tried out would be 
- Setup a Kubernetes cluster in its context
- Authenticate to the cluster
- Apply the deployment and services