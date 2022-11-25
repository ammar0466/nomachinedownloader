import requests
import bs4
from bs4 import BeautifulSoup
import tqdm
import os
import subprocess
import urllib3
from nomachineScraper import downloadNomachineDeb

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def CheckNewVersion():
    url = 'https://downloads.nomachine.com/download/?id=5'
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    # print(soup)
    # #parse html and get link from id=link_download
    link = soup.find(id='link_download')
    #parse link and get only href
    href = link.get('href')
    print(href.split('/')[-1])
    return href.split('/')[-1]

def compareVersion():
    #check latestVersion.txt content and compare with CheckNewVersion()
    #if not found download and update latestVersion.txt
    #if found do sleep
    #if not found download and update latestVersion.txt
    #read latestVersion.txt, check all line
    #save value form CheckNewVersion() to variable
    #if variable not in latestVersion.txt
    #download and update latestVersion.txt
    #if variable in latestVersion.txt
    #do sleep
    #if not found download and update latestVersion.txt
    currentVersion = CheckNewVersion()

    #open latestVersion.txt first line and compare with currentVersion
    with open('latestVersion.txt', 'r') as file:
        data = file.read()
        if currentVersion == data:
            print('Already Latest Version')
        else:
            print('New Version Released')
            #downloadNomachineDeb()
            downloadNomachineDeb()
            with open('latestVersion.txt', 'w+') as file:
                file.write(currentVersion)

compareVersion()