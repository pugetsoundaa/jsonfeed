import git
import datetime

def commitjson():
	repo = git.Repo('./meetingdata-test')
	repo.git.add('meetingdata.json')
	repo.git.commit('-m',datetime.datetime.now())