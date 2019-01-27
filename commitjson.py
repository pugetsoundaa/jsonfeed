import git
import datetime

def commitjson():
	repo = git.Repo('./meetingdata')
	repo.git.add('meetingdata.json')
	repo.git.commit('-m',datetime.datetime.now())
	repo.git.push('origin','master')