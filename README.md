# Face-Recognition
This application uses a face_recognition library to detect intruders in a visitors directory named (unknown_people).
In the directory known_people are the image of recognised people.
it is advised that all images should have same extension to improve the accuracy of the Face recognition.
CMax should also be downloaded to help the dlib dependency.
special thanks to @ageitgey for the amazing libary. Please check out this link: https://github.com/ageitgey/face_recognition
In the Macos environment, an error may occur after adding images to the directory "OSError: cannot identify image file 'dataSet/.DS_Store'"
This error is from the Macos, everytime a file directory is opened, A .DS_Store file is added to make the os search faster.
To solve this problem, you can delete the file from the terminal using cd and rm.
Check out this link for further information https://stackoverflow.com/questions/47645115/oserror-cannot-identify-image-file-dataset-ds-store
Please its open for further improvements and check out requirement.txt for modules to be installed.
