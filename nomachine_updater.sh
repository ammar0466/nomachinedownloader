#!/bin/bash
url='https://downloads.nomachine.com/download/?id=5'
r=$(wget $url -q -O -)
page=$(echo $r | grep -oP 'link_download.*')
#get link with start with http and end with .deb save to link
link=$(echo $page | grep -oP 'href.*' | awk -F '"' '{print $2}')
# echo $link
currentVersion=$(echo $page | grep -oP 'href.*' | awk -F '"' '{print $2}' | awk -F '/' '{print $NF}')
#save filename to variable currentVersion
echo 'Current version is: '$currentVersion
# echo $currentVersion

# #open noMachineLatest.txt first line and compare with currentVersion
# #if currentVersion is different, then update
# #if currentVersion is the same, then do nothing
# #if noMachineLatest.txt is empty, then update
# #if noMachineLatest.txt does not exists, then update

# #if currentVersion is different, then update
if [ -f noMachineLatest.txt ]; then
    noMachineLatest=$(head -n 1 noMachineLatest.txt)
    if [ "$currentVersion" != "$noMachineLatest" ]; then
        echo 'New version is available!'
        echo 'Downloading...'
        wget $link
        echo 'Done!'
        echo 'Updating noMachineLatest.txt'
        echo $currentVersion > noMachineLatest.txt
        echo 'Done!'
    else
        echo 'No new version available.'
    fi
else
    echo 'noMachineLatest.txt not found!'
    echo 'Downloading...'
    wget $link
    echo 'Done!'
    echo 'Creating noMachineLatest.txt'
    echo $currentVersion > noMachineLatest.txt
    echo 'Done!'
fi

