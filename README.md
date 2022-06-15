## Machine-Learning-Project

### creating environment
'''
conda create -p projenv python==3.7 -y
'''
### to activate virtual environment
'''
conda activate projenv/
'''
### to select shell command is
'''
conda init bash
'''
### to add file to the git
'''
git add .
 or
 git add <file_name>
 '''
### to restrict any file to github use gitignore . write that file name to gitignore file.

### to check the git status
'''
git status
'''
### to check all version maintened by git
'''
git log
'''
### to create new version/commite by git
'''
git commit -m "message why did changed"
'''
### to send changes or version to github command is
'''
git push origin main
'''
### to check remote url
'''
git remote -v
'''
## to setup ci/cd pipeline on heroku we need these three things

### (1) email id
'''
sumitbhagat472@gmail.com
'''
### (2) heroku api key
'''
<__hidden__>
'''
### (3) app name
'''
ml-regression-01
'''

### BUILD Docker Image
'''
docker build -t<image name>:<tag name> .

### note- image name for the docker must be in lower order

### To list docker Images
'''
docker images
'''
### Run Docker image
'''
docker run -p 5000:5000 -e PORT=5000 e0f3e193335d
'''
### To check running containers in docker
'''
docker ps
'''
### To stop any container
'''
docker stop<container_id>
'''
###
