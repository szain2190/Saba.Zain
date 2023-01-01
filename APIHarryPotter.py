import tkinter as tk
import requests

response = requests.get("http://hp-api.herokuapp.com/api/characters/students")
data = response.json()

root = tk.Tk()
root.title("Harry Potter Characters")

index = tk.IntVar(root)
name = tk.StringVar(root)
gender = tk.StringVar(root)
house = tk.StringVar(root)
eye = tk.StringVar(root)
hair = tk.StringVar(root)
actor = tk.StringVar(root)
entry = tk.StringVar(root)

index.set(0)
name.set(data[index.get()]["name"])
gender.set(data[index.get()]["gender"])
house.set(data[index.get()]["house"])
eye.set(data[index.get()]["eyeColour"])
hair.set(data[index.get()]["hairColour"])
actor.set(data[index.get()]["actor"])

def back():
    index.set(index.get()-1)
    name.set(data[index.get()]["name"])
    gender.set(data[index.get()]["gender"])
    house.set(data[index.get()]["house"])
    eye.set(data[index.get()]["eyeColour"])
    if eye.get() == "":
        eye.set("UNKNOWN")
    hair.set(data[index.get()]["hairColour"])
    if hair.get() == "":
        hair.set("UNKNOWN")
    actor.set(data[index.get()]["actor"])

def forward():
    index.set(index.get()+1)
    name.set(data[index.get()]["name"])
    gender.set(data[index.get()]["gender"])
    house.set(data[index.get()]["house"])
    eye.set(data[index.get()]["eyeColour"])
    hair.set(data[index.get()]["hairColour"])
    actor.set(data[index.get()]["actor"])

def change(i):
    index.set(index.get()+i)
    name.set(data[index.get()]["name"])
    gender.set(data[index.get()]["gender"])
    house.set(data[index.get()]["house"])
    if house.get() == "":
        house.set("UNKNOWN")
    eye.set(data[index.get()]["eyeColour"])
    if eye.get() == "":
        eye.set("UNKNOWN")
    hair.set(data[index.get()]["hairColour"])
    if hair.get() == "":
        hair.set("UNKNOWN")
    actor.set(data[index.get()]["actor"])
    if actor.get() == "":
        actor.set("UNKNOWN")

def find(search_name):
    for i in range(len(data)):
        if data[i]["name"] == search_name:
            index.set(i)
            name.set(data[i]["name"])
            gender.set(data[i]["gender"])
            house.set(data[i]["house"])
            eye.set(data[i]["eyeColour"])
            hair.set(data[i]["hairColour"])
            actor.set(data[i]["actor"])
            break


label_title = tk.Label(root, text = "Character Database")

label_name = tk.Label(root, text = "Name:", width=20, anchor="w")
data_name = tk.Label(root, textvariable = name, width=20, anchor="w")

label_gender = tk.Label(root, text = "Gender:", width=20, anchor="w")
data_gender = tk.Label(root, textvariable = gender, width=20, anchor="w")

label_house = tk.Label(root, text = "House:", width=20, anchor="w")
data_house = tk.Label(root, textvariable = house, width=20, anchor="w")

label_eye = tk.Label(root, text = "Eye Colour:", width=20, anchor="w")
data_eye = tk.Label(root, textvariable = eye, width=20, anchor="w")

label_hair = tk.Label(root, text = "Hair Colour:", width=20, anchor="w")
data_hair = tk.Label(root, textvariable = hair, width=20, anchor="w")

label_actor = tk.Label(root, text = "Actor", width=20, anchor="w")
data_actor = tk.Label(root, textvariable = actor, width=20, anchor="w")

button_back = tk.Button(root, text="<", width=20,command=lambda: change(-1))
button_forward = tk.Button(root, text=">", width=20, command=lambda: change(1))

label_search = tk.Label(root, text = "Name Search", width=20)
label_entry = tk.Entry(root, textvariable=entry)
button_search = tk.Button(root, text="Search", width=20, command=lambda: find(entry.get()))

label_title.grid(row=0, column = 0, columnspan=2)

label_name.grid(row=1, column = 0)
data_name.grid(row=1, column = 1)

label_gender.grid(row=2, column = 0)
data_gender.grid(row=2, column = 1)

label_house.grid(row=3, column = 0)
data_house.grid(row=3, column = 1)

label_eye.grid(row=4, column = 0)
data_eye.grid(row=4, column = 1)

label_hair.grid(row=5, column = 0)
data_hair.grid(row=5, column = 1)

label_actor.grid(row=6, column = 0)
data_actor.grid(row=6, column = 1)

button_back.grid(row=7, column = 0)
button_forward.grid(row=7, column = 1)

label_search.grid(row=8, column=0, columnspan=2)
label_entry.grid(row=9, column = 0)
button_search.grid(row=9, column = 1)

root.mainloop()