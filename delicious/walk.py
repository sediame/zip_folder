import os

for folderName, subfolders, filenames in os.walk('home/ahsan/delicious'):
    print('THe curent folder is' + folderName)  

    for subfolder in subfolders:
        print('subfolder of '+ folderName + ': ' + subfolder)
        
    for filname in filenames:
        print('file inside '+ folderName + ': ' + filname)
print('')


