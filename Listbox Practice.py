from tkinter import *

def play():
    songs = []
    for index in listbox.curselection():
        songs.insert(index,listbox.get(index))
    print("You are now listening to: ")
    for index in songs:
        print(index)

def add():
    listbox.insert(listbox.size(),entry.get())
    listbox.config(height=listbox.size())

def delete():
    for index in reversed(listbox.curselection()):
        listbox.delete(index)
    listbox.config(height=listbox.size())


window = Tk()

logo = PhotoImage(file="spotify.png")

window.title("Spotify List")
window.iconphoto(True, logo)

listbox = Listbox(window,
                  width = 20,
                  font = ("Ariel", 20, "underline"),
                  bg = "#1DB954",
                  selectmode = MULTIPLE)
listbox.pack()

listbox.insert(1, "Wiz Khalifa")
listbox.insert(2, "Migos")
listbox.insert(3, "Ariana Grande")
listbox.insert(4, "G-Eazy")
listbox.insert(5, "2Pac")

listbox.config(height = listbox.size())

playbutton = Button(window,
                    text = "Play",
                    command = play,
                    bg = "#1DB954",
                    font = ("Ariel", 20, "bold"))
playbutton.pack()

entry = Entry(window,
              width = 13,
              bg = "#1DB954")
entry.pack()

add = Button(window,
                    text = "Add",
                    command = add,
                    bg = "#1DB954",
                    font = ("Ariel", 20, "bold"))
add.pack()

delete = Button(window,
                    text = "Delete",
                    command = delete,
                    bg = "#1DB954",
                    font = ("Ariel", 20, "bold"))
delete.pack()


window.mainloop()