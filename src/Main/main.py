import tkinter as tk
from PIL import Image, ImageTk
from tkinter import filedialog as fd
import cv2
import src.MatchImage.surf_func as surf
import src.MatchImage.sift_func as sift

image = ""
path = ""

# create a window for app
root = tk.Tk()
root.title("Template Matching")
root.geometry("1050x600+200+100")
root.resizable(False, False)

# create a frame label for match image
matching_label_frame = tk.LabelFrame(root, text="Matching:")
matching_label_frame.pack(fill="both", expand="yes")


# def show file dialog
def openFileImage():
    file = fd.askopenfilename(initialdir="/",
                              filetypes=(("all files", "*.*"), ("png files", "*.png"), ("jpeg files", "*.jpg")))
    global path
    path = file
    img = Image.open(file)
    img = img.resize((800, 300), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    match_label.configure(image=img)
    match_label.image = img


def with_sift():
    list_data = sift.load_data()
    list_good = sift.compare_sift(path)
    good = []
    for i in range(0, len(list_data)):
        good.append(list_good[list_data[i]])
    good.sort(reverse=True)
    list_img = []
    for i in range(0, 5):
        for k, v in list_good.items():
            if v == good[i]:
                list_img.append(k)

    img1 = Image.open(list_img[0])
    img1 = img1.resize((200, 300), Image.ANTIALIAS)
    img1 = ImageTk.PhotoImage(img1)
    coca1_label.configure(image=img1)
    coca1_label.image = img1

    img2 = Image.open(list_img[1])
    img2 = img2.resize((200, 300), Image.ANTIALIAS)
    img2 = ImageTk.PhotoImage(img2)
    coca2_label.configure(image=img2)
    coca2_label.image = img2

    img3 = Image.open(list_img[2])
    img3 = img3.resize((200, 300), Image.ANTIALIAS)
    img3 = ImageTk.PhotoImage(img3)
    coca3_label.configure(image=img3)
    coca3_label.image = img3

    img4 = Image.open(list_img[3])
    img4 = img4.resize((200, 300), Image.ANTIALIAS)
    img4 = ImageTk.PhotoImage(img4)
    coca4_label.configure(image=img4)
    coca4_label.image = img4

    img5 = Image.open(list_img[4])
    img5 = img5.resize((200, 300), Image.ANTIALIAS)
    img5 = ImageTk.PhotoImage(img5)
    coca5_label.configure(image=img5)
    coca5_label.image = img5

    path2 = list_img[0]
    img_result = sift.draw_key_sift(path, path2)
    img_result = img_result.resize((800, 300), Image.ANTIALIAS)
    img_result = ImageTk.PhotoImage(img_result)
    match_label.configure(image=img_result)
    match_label.image = img_result


def with_surf():
    list_data = surf.load_data()
    list_good = surf.compare_surf(path)
    good = []
    for i in range(0, len(list_data)):
        good.append(list_good[list_data[i]])
    good.sort(reverse=True)
    list_img = []
    for i in range(0, 5):
        for k, v in list_good.items():
            if v == good[i]:
                list_img.append(k)

    img1 = Image.open(list_img[0])
    img1 = img1.resize((200, 300), Image.ANTIALIAS)
    img1 = ImageTk.PhotoImage(img1)
    coca1_label.configure(image=img1)
    coca1_label.image = img1

    img2 = Image.open(list_img[1])
    img2 = img2.resize((200, 300), Image.ANTIALIAS)
    img2 = ImageTk.PhotoImage(img2)
    coca2_label.configure(image=img2)
    coca2_label.image = img2

    img3 = Image.open(list_img[2])
    img3 = img3.resize((200, 300), Image.ANTIALIAS)
    img3 = ImageTk.PhotoImage(img3)
    coca3_label.configure(image=img3)
    coca3_label.image = img3

    img4 = Image.open(list_img[3])
    img4 = img4.resize((200, 300), Image.ANTIALIAS)
    img4 = ImageTk.PhotoImage(img4)
    coca4_label.configure(image=img4)
    coca4_label.image = img4

    img5 = Image.open(list_img[4])
    img5 = img5.resize((200, 300), Image.ANTIALIAS)
    img5 = ImageTk.PhotoImage(img5)
    coca5_label.configure(image=img5)
    coca5_label.image = img5

    path2 = list_img[0]
    img_result = surf.draw_key_suft(path, path2)
    img_result = img_result.resize((800, 300), Image.ANTIALIAS)
    img_result = ImageTk.PhotoImage(img_result)
    match_label.configure(image=img_result)
    match_label.image = img_result


# create frame for button
button_frame = tk.Frame(matching_label_frame, relief="raised", borderwidth=1)
button_frame.pack(side="right", padx=5, pady=5)

button_image = tk.Button(button_frame, text="...", command=openFileImage)
button_image.pack(fill="x", padx=5, pady=5)

button_sift = tk.Button(button_frame, text="Sift", command=with_sift)
button_sift.pack(fill="x", padx=5, pady=5)

button_surf = tk.Button(button_frame, text="Surf", command=with_surf)
button_surf.pack(fill="x", padx=5, pady=5)

# create frame for match image
path_hust = r"D:\document\xulyanh\btl\code\hust.jpeg"
hust = Image.open(path_hust)
hust_show = ImageTk.PhotoImage(hust)

match_label = tk.Label(matching_label_frame, relief="raised", borderwidth=1, image=hust_show)
match_label.config(width=800, height=300)
match_label.image = hust_show
match_label.pack(fill="both", side="right", padx=5, pady=5, expand="yes")

# create a frame label for show 4 image like in
equal_label = tk.LabelFrame(root, text="The most like image:")
equal_label.pack(fill="both", expand="yes")

path_coca5 = r"D:\document\xulyanh\btl\code\hust.jpeg"
coca5 = Image.open(path_coca5)
coca5 = coca5.resize((200, 300), Image.ANTIALIAS)
coca5_show = ImageTk.PhotoImage(coca5)

coca5_label = tk.Label(equal_label, relief="raised", borderwidth=1, image=coca5_show)
coca5_label.config(width=200, height=300)
coca5_label.image = coca5_show
coca5_label.pack(side="right", padx=5, pady=5, fill="y")

path_coca4 = r"D:\document\xulyanh\btl\code\hust.jpeg"
coca4 = Image.open(path_coca4)
coca4 = coca4.resize((200, 300), Image.ANTIALIAS)
coca4_show = ImageTk.PhotoImage(coca4)

coca4_label = tk.Label(equal_label, relief="raised", borderwidth=1, image=coca4_show)
coca4_label.config(width=200, height=300)
coca4_label.image = coca4_show
coca4_label.pack(side="right", pady=5)

path_coca3 = r"D:\document\xulyanh\btl\code\hust.jpeg"
coca3 = Image.open(path_coca3)
coca3 = coca3.resize((200, 300), Image.ANTIALIAS)
coca3_show = ImageTk.PhotoImage(coca3)

coca3_label = tk.Label(equal_label, relief="raised", borderwidth=1, image=coca3_show)
coca3_label.config(width=200, height=300)
coca3_label.image = coca3_show
coca3_label.pack(side="right", padx=5, pady=5)

path_coca2 = r"D:\document\xulyanh\btl\code\hust.jpeg"
coca2 = Image.open(path_coca2)
coca2 = coca2.resize((200, 300), Image.ANTIALIAS)
coca2_show = ImageTk.PhotoImage(coca2)

coca2_label = tk.Label(equal_label, relief="raised", borderwidth=1, image=coca2_show)
coca2_label.config(width=200, height=300)
coca2_label.image = coca2_show
coca2_label.pack(side="right", pady=5)

path_coca1 = r"D:\document\xulyanh\btl\code\hust.jpeg"
coca1 = Image.open(path_coca1)
coca1 = coca1.resize((200, 300), Image.ANTIALIAS)
coca1_show = ImageTk.PhotoImage(coca1)

coca1_label = tk.Label(equal_label, relief="raised", borderwidth=1, image=coca1_show)
coca1_label.config(width=200, height=300)
coca1_label.image = coca1_show
coca1_label.pack(side="right", padx=5, pady=5)

root.mainloop()
