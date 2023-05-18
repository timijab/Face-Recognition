import face_recognition
import os

#  search through the folder with known people both staff and students and encode the data.
# choose and input your own file directory to known individuals

folder_dir = "/Users/Isaac Afolayan/Desktop/Face dectection/known_people"

list_images = []
unknown_people = []
encoded_list_known = []
unknown_images = []


# Load each image into a numpy array
class FacialDetection():
    def __init__(self, filepath):
        self.intruders = []
        self.path = filepath
        for images in os.listdir(folder_dir):
            self.new = face_recognition.load_image_file(f"{folder_dir}/{images}")
            #     encode each image
            encoded_list_known.append(face_recognition.face_encodings(self.new)[0])
        self.known_faces = encoded_list_known

        # load unknown images into numpy arrays
        # Check each image in unknown_pictures and flag for any unrecognised person.

        for images in os.listdir(self.path):
            list_images.append(images)
            self.unknown = face_recognition.load_image_file(f"{self.path}/{images}")
            try:
                unknown_people.append(face_recognition.face_encodings(self.unknown)[0])
            except IndexError:
                pass
                print(
                    "I wasn't able to locate any faces in atleast one of the images. check the image files. aborting....")

        # loop through list_known for each image

    def setup(self):
        i = 0
        while i < len(unknown_people):
            results = face_recognition.compare_faces(self.known_faces, unknown_people[i])
            # print("Is the unknown face a new person that we've never seen before? {}".format(not True in results))
            i += 1
            print(i)
            if True in results:
                self.intruders.append(list_images[i])

    def send_back(self):
        return self.intruders
