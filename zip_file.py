import os, zipfile

folder = os.path.abspath('delicious')
print(folder)

number = 1

while True:
    zipFilename = os.path.basename(folder) + '_' + str(number) + '.zip'
    if not os.path.exists(zipFilename):
        break
    number += 1

backupZip = zipfile.ZipFile(zipFilename, 'w', zipfile.ZIP_DEFLATED)

for folder_name, sub_folders, file_names in os.walk(folder):

    current_dir = os.path.basename(folder_name)
    backupZip.write(folder_name)
    print('current directory is      :', current_dir)
    for filename in file_names:
        print('filename is           :', filename)
        backupZip.write(os.path.join(folder_name, filename))
    print('##################################################')

backupZip.close()

print('Done')
