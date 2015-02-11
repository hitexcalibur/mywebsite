from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response, render
from django.conf import settings

import os

def readFile(fileName):
    fin = open(fileName, 'r')
    buff = fin.readlines()
    fin.close()
    return buff

def personal(request):
    fileName =  os.path.join(settings.PROJECT_DIR, 'resources/intro.txt')
    intro = readFile(fileName)[0]
    
    fileName =  os.path.join(settings.PROJECT_DIR, 'resources/education.txt')
    buff = readFile(fileName)
    educationList = []
    for line in buff:
        edu = {}
        parts = line.split(';')
        edu['time'] = parts[0]
        edu['pos'] = parts[1]
        edu['dept'] = parts[2]
        edu['org'] = parts[3]
        educationList.append(edu)
        
    fileName =  os.path.join(settings.PROJECT_DIR, 'resources/paper.txt')
    buff = readFile(fileName)
    paperList = []
    paperPath = "http://web.engr.oregonstate.edu/~chenshen/papers/"
    for line in buff:
        paper = {}
        parts = line.split(';')
        paper['title'] = parts[0]
        paper['author'] = parts[1]
        paper['conf'] = parts[2]
        paper['url'] = paperPath + parts[3].strip()
        paperList.append(paper)
        
    
    fileName =  os.path.join(settings.PROJECT_DIR, 'resources/service.txt')
    serviceList = readFile(fileName)
    
    
    return render_to_response('personal.html',{'educationList':educationList, 'intro':intro, 'paperList':paperList, 'serviceList':serviceList},context_instance=RequestContext(request))
    