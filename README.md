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
f57b41ef-c608-485a-8a79-1a6034b0b93a
'''
### (3) app name
'''
ml-regression-01
'''

### BUILD Docker Image
'''
docker build -t<image name>:<tag name> .

### note- image name for the docker must be in lower order

