import tkinter as Tk
import customtkinter
from tkinter import filedialog, messagebox, Toplevel, PhotoImage
from facial_detector import FacialDetection
from PIL import ImageTk, Image

import time

# system setting
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

valid_photograph = None


# Incase we do not want the default theme.
# customtkinter.set_default_color_theme("path/to/your/custom_theme.json")
class MyFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)


class Platform(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        # app initializer
        # Original tkinter
        self.geometry('700x700')
        self.title("SPEECH TO TEXT")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        #     mainframe

    def getFolderPath(self):
        """ Get the folder path from button """
        folder = filedialog.askdirectory()
        if folder:
            # calling facial detection
            face_detection = FacialDetection(folder)
            face_detection.setup()
            list_of_unknown = face_detection.send_back()
            """ Gui frame to display pictures """
            box_2 = MyFrame(master=self, width=500, height=200, corner_radius=10, fg_color="white",
                            border_width=2,
                            border_color='#0B2447')
            box_2.grid(row=4, column=0, padx=20, pady=20)
            imag = customtkinter.CTkImage(Image.open(f"unknown_pictures/{list_of_unknown[0]}"), size=(400, 300))

            text_1 = customtkinter.CTkLabel(box_2, image=imag, bg_color="transparent", fg_color="white", text='')
            text_1.grid(row=1, column=0, padx=0, pady=0)


            # Frame-2
            """ Gui frame """
            box_3 = MyFrame(master=self, width=150, height=200, fg_color="#0B2447")
            box_3.grid(row=4, column=1)

            box_5_label = customtkinter.CTkLabel(master=box_3, text_color='white', text=f'These pictures does not '
                                                                                        f'match anyone in our \n'
                                                                                        f'database\n{list_of_unknown}',
                                                 width=200)
            box_5_label.grid(row=1, column=0, pady=40, padx=30)
            messagebox.showinfo(title="Intruder Alert",
                                   message="The identity of some the individuals in these pictures are unconfirmed,"
                                           " please "
                                           "check")
            def ShowMessage():
                """" Popup showing the intruders pictures """
                for messages in list_of_unknown:
                    global pop
                    pop = Toplevel()
                    pop.title("Intruders: Alert")
                    pop.geometry("400x500")
                    pop.config(bg="white")

                    global intruder_picture
                    intruder_picture = customtkinter.CTkImage(Image.open(f"unknown_pictures/{messages}"), size=(400, 300))

                    my_frame = customtkinter.CTkFrame(pop)
                    my_frame.pack(pady=50, padx=30)

                    the_display = customtkinter.CTkLabel(master=my_frame,image=intruder_picture, text='')
                    the_display.grid(row=0, column=0)

            box_5_button = customtkinter.CTkButton(master=box_3, text='Open directory for intruder images', border_width=1,
                                                   border_color='#b2beb5',
                                                   text_color='#0B2447', fg_color='white', height=30, width=100,
                                                   hover_color='#b2beb5',
                                                    command=ShowMessage)
            box_5_button.grid(row=2, column=0, padx=30, pady=20)

        else:
            # we have to return no file chosen in case
            """ Gui frame to display pictures """
            box_2 = MyFrame(master=self, width=500, height=200, corner_radius=10, fg_color="white", bg_color='green',
                            border_width=2,
                            border_color='#0B2447')
            box_2.grid(row=4, column=0, padx=20, pady=20)
            text_1 = customtkinter.CTkLabel(box_2, bg_color="transparent", fg_color="white", text='No intruder')
            text_1.grid(row=1, column=0, padx=0, pady=0)

    def frames(self):
        """ Gui for frame 1 Upload File """
        box = MyFrame(master=self, width=550, height=200, corner_radius=10, fg_color="white",
                      border_width=2, border_color='#0B2447')
        box.grid(row=0, column=0, padx=20, pady=20)
        convert = customtkinter.CTkLabel(box, text='Face Identity Detector', text_color='#0B2447',
                                         bg_color="transparent",
                                         fg_color="white", font=("Helvetica", 15, "bold"))
        convert.grid(row=0, column=0, padx=0, pady=50)
        choose = customtkinter.CTkLabel(box, text='Face to detect', text_color='#b2beb5')
        choose.grid(row=1, column=0)
        button = customtkinter.CTkButton(box, text='Pick file directory', text_color="white", fg_color='#0B2447',
                                         height=40,
                                         width=200,
                                         command=self.getFolderPath,
                                         hover_color='#0591AF')
        button.grid(row=2, column=0, pady=10, padx=100)

        # Frame-1

        """ Gui frame """
        box_1 = MyFrame(master=self, width=150, height=200, corner_radius=10, fg_color="white",
                        border_width=2)
        box_1.grid(row=0, column=1, padx=20)
        check_details = customtkinter.CTkButton(master=box_1, text='Check details', border_width=1,
                                                border_color='#B2BEB5',
                                                text_color="#0B2447", fg_color='white', hover_color='#B2BEB5')
        check_details.grid(row=2, column=0, padx=10, pady=50)

        box_1_label = customtkinter.CTkLabel(master=box_1, width=20, text_color='#b2beb5',
                                             text='Check Details Of Transcription')
        box_1_label.grid(row=1, column=0, padx=10, pady=20)
