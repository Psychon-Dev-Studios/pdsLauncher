import os, tkinter as tk, sys, shutil
from time import sleep
from tkinter import messagebox
from urllib import request as urlRequest
from threading import Thread as td

MIRROR_LOCATION = "https://psychon-dev-studios.github.io/pdsLauncher"
PATH = sys.path[0]
WINDRIVE = str(os.environ['WINDIR'].split(":\\")[0])

root = tk.Tk()
root.wm_geometry("336x650")
root.grid_anchor("center")
root.wm_title("PDS Launcher")
root.wm_resizable(width=False, height=False)
root.config(background="lightgray")

appTitle = ("Helvica", 15, "bold")
appTitleColor = "black"

a1_play_text = tk.StringVar()
a2_play_text = tk.StringVar()
a3_play_text = tk.StringVar()
cxr_play_text = tk.StringVar()

a1_installed = None
a2_installed = None
a3_installed = None
cxr_installed = None

# Check to see if the games are installed
if (os.path.isfile(PATH + "/files/arachna.html") == True): a1_installed=True;a1_play_text.set("Play")
else: a1_installed=False;a1_play_text.set("Install")

if (os.path.isfile(PATH + "/files/arachna2.html") == True): a2_installed=True;a2_play_text.set("Play")
else: a2_installed=False;a2_play_text.set("Install")

if (os.path.isfile(PATH + "/files/arachnia.html") == True): a3_installed=True;a3_play_text.set("Play")
else: a3_installed=False;a3_play_text.set("Install")

if (os.path.isfile(PATH + "/files/cxr.html") == True): cxr_installed=True;cxr_play_text.set("Play")
else: cxr_installed=False;cxr_play_text.set("Install")

def RELOAD():

    for widgets in root.winfo_children():
      widgets.destroy()

    a1_title = tk.Label(root, text="Arachna", background="lightgray", font=appTitle, foreground=appTitleColor)
    a1 = tk.Button(root, textvariable=a1_play_text, width=45, command=a1_proxy, background="lightblue")
    a1_update = tk.Button(root, text="Check for Updates", width=45, command=arachna_updater)
    a1_remove = tk.Button(root, text="Uninstall", width=45, command=arachna_uninstall)
    a2_title = tk.Label(root, text="Arachna 2", background="lightgray", font=appTitle, foreground=appTitleColor)
    a2 = tk.Button(root, textvariable=a2_play_text, width=45, command=a2_proxy, background="lightblue")
    a2_update = tk.Button(root, text="Check for Updates", width=45, command=arachna2_updater)
    a2_remove = tk.Button(root, text="Uninstall", width=45, command=arachna2_uninstall)
    a3_title = tk.Label(root, text="Arachnia", background="lightgray", font=appTitle, foreground=appTitleColor)
    a3 = tk.Button(root, textvariable=a3_play_text, width=45, command=a3_proxy, background="lightblue")
    a3_update = tk.Button(root, text="Check for Updates", width=45, command=arachnia_updater)
    a3_remove = tk.Button(root, text="Uninstall", width=45, command=arachnia_uninstall)
    cxr_title = tk.Label(root, text="CamX: Rebirth", background="lightgray", font=appTitle, foreground=appTitleColor)
    cxr = tk.Button(root, textvariable=cxr_play_text, width=45, command=cxr_proxy, background="lightblue")
    cxr_update = tk.Button(root, text="Check for Updates", width=45, command=cxr_updater)
    cxr_remove = tk.Button(root, text="Uninstall", width=45, command=cxr_uninstall)
    blank = tk.Label(root, text="", font=("Helvica", 15), background="lightgray")
    launcher_title = tk.Label(root, text="Launcher", background="lightgray", font=appTitle, foreground=appTitleColor)
    ext = tk.Button(root, text="Exit Launcher", width= 45, command=exit)
    launcher_update = tk.Button(root, text="Check for Updates", width = 45, command=launcher_updater)
    launcher_remove = tk.Button(root, text="Uninstall Launcher", width=45, command=launcher_uninstall)

    a1.bind("<Enter>", on_enter)
    a1.bind("<Leave>", on_leave_play)
    a1_update.bind("<Enter>", on_enter)
    a1_update.bind("<Leave>", on_leave)
    a1_remove.bind("<Enter>", on_enter_cancel)
    a1_remove.bind("<Leave>", on_leave)

    a2.bind("<Enter>", on_enter)
    a2.bind("<Leave>", on_leave_play)
    a2_update.bind("<Enter>", on_enter)
    a2_update.bind("<Leave>", on_leave)
    a2_remove.bind("<Enter>", on_enter_cancel)
    a2_remove.bind("<Leave>", on_leave)

    a3.bind("<Enter>", on_enter)
    a3.bind("<Leave>", on_leave_play)
    a3_update.bind("<Enter>", on_enter)
    a3_update.bind("<Leave>", on_leave)
    a3_remove.bind("<Enter>", on_enter_cancel)
    a3_remove.bind("<Leave>", on_leave)

    cxr.bind("<Enter>", on_enter)
    cxr.bind("<Leave>", on_leave_play)
    cxr_update.bind("<Enter>", on_enter)
    cxr_update.bind("<Leave>", on_leave)
    cxr_remove.bind("<Enter>", on_enter_cancel)
    cxr_remove.bind("<Leave>", on_leave)

    ext.bind("<Enter>", on_enter_cancel)
    ext.bind("<Leave>", on_leave)
    launcher_update.bind("<Enter>", on_enter)
    launcher_update.bind("<Leave>", on_leave)
    launcher_remove.bind("<Enter>", on_enter_cancel)
    launcher_remove.bind("<Leave>", on_leave)
    ext.bind("Leave", on_leave)

    a1_title.pack(pady=5)
    a1.pack()
    if(a1_installed == True):
        a1_update.pack()
        a1_remove.pack()
    a2_title.pack(pady=5)
    a2.pack()
    if(a2_installed == True):
        a2_update.pack()
        a2_remove.pack()
    a3_title.pack(pady=5)
    a3.pack()
    if(a3_installed == True):
        a3_update.pack()
        a3_remove.pack()
    cxr_title.pack(pady=5)
    cxr.pack()
    if(cxr_installed == True):
        cxr_update.pack()
        cxr_remove.pack()
    blank.pack(pady=5)
    launcher_title.pack(pady=5)
    launcher_update.pack()
    ext.pack()
    launcher_remove.pack()


def a1_proxy():
    td(name="proxyscript", target=arachna).start()

def a2_proxy():
    td(name="proxyscript", target=arachna2).start()

def a3_proxy():
    td(name="proxyscript", target=arachnia).start()

def cxr_proxy():
    td(name="proxyscript", target=cxr).start()

def arachna():
    global a1_installed
    if (a1_installed):
        try:os.startfile(PATH + "/files/arachna.html")
        except:messagebox.showerror("PDS Launcher", "Something went wrong while trying to start this game. It may not be installed correctly.")
    else:
        a1_play_text.set("Installing...")

        try:
            mirror = urlRequest.urlopen(MIRROR_LOCATION + "/arachna.html").read()
            local = open(PATH + "/files/arachna.html", "xb")

            local.write(mirror)
            local.close()

            sleep(2)

            a1_play_text.set("Play")
            a1_installed = True
            RELOAD()

        except Exception as err:
            print(str(err))
            a1_play_text.set("Install")
            messagebox.showwarning("PDS Launcher - Install Failed", "Installation of Arachna failed: " + str(err))
            RELOAD()

def arachna2():
    global a2_installed
    if (a2_installed):
        try:os.startfile(PATH + "/files/arachna2.html")
        except:messagebox.showerror("PDS Launcher", "Something went wrong while trying to start this game. It may not be installed correctly.")
    else:
        a2_play_text.set("Installing...")

        try:
            mirror = urlRequest.urlopen(MIRROR_LOCATION + "/arachna2.html").read()
            local = open(PATH + "/files/arachna2.html", "xb")

            local.write(mirror)
            local.close()

            sleep(2)

            a2_play_text.set("Play")
            a2_installed = True
            RELOAD()

        except Exception as err:
            print(str(err))
            a2_play_text.set("Install")
            messagebox.showwarning("PDS Launcher - Install Failed", "Installation of Arachna 2 failed: " + str(err))
            

def arachnia():
    global a3_installed
    if (a3_installed):
        try:os.startfile(PATH + "/files/arachnia.html")
        except:messagebox.showerror("PDS Launcher", "Something went wrong while trying to start this game. It may not be installed correctly.")
    else:
        a3_play_text.set("Installing...")

        try:
            mirror = urlRequest.urlopen(MIRROR_LOCATION + "/arachnia.html").read()
            local = open(PATH + "/files/arachnia.html", "xb")

            local.write(mirror)
            local.close()

            sleep(2)

            a3_play_text.set("Play")
            a3_installed = True
            RELOAD()

        except Exception as err:
            print(str(err))
            a3_play_text.set("Install")
            messagebox.showwarning("PDS Launcher - Install Failed", "Installation of Arachnia failed: " + str(err))

def cxr():
    global cxr_installed
    if (cxr_installed):
        try:os.startfile(PATH + "/files/cxr.html")
        except:messagebox.showerror("PDS Launcher", "Something went wrong while trying to start this game. It may not be installed correctly.")
    else:
        cxr_play_text.set("Installing...")

        try:
            mirror = urlRequest.urlopen(MIRROR_LOCATION + "/cxr.html").read()
            local = open(PATH + "/files/cxr.html", "xb")

            local.write(mirror)
            local.close()

            sleep(2)

            cxr_play_text.set("Play")
            cxr_installed = True
            RELOAD()

        except Exception as err:
            print(str(err))
            cxr_play_text.set("Install")
            messagebox.showwarning("PDS Launcher - Install Failed", "Installation of CamX: Rebirth failed: " + str(err))
            RELOAD()

def arachna_updater():
    try:
        mirror = urlRequest.urlopen(MIRROR_LOCATION + "/arachna.html").read()
        local = open(PATH + "/files/arachna.html", "wb")

        if not (local == mirror):
            a1_play_text.set("Updating...")

            local.write(mirror)
            local.close()

            sleep(2)
            a1_play_text.set("Play")

        else:
            messagebox.showinfo("PDS Launcher - Updater", "Game is already up-to-date!")

    except Exception as err:
        print(str(err))
        messagebox.showwarning("PDS Launcher - Update Failed", "Update failed: " + str(err))

def arachna_uninstall():
    global a1_installed,a2_installed,a3_installed

    confirm = messagebox.askokcancel("PDS Launcher - Game Uninstaller", "Are you sure you want to uninstall the game? Depending on your browser, this game's data not be recoverable!")

    if (confirm == True):
        os.remove(PATH + "/files/arachna.html")
        a1_installed = False
        a1_play_text.set("Install")
        RELOAD()
        

def arachna2_updater():
    try:
        mirror = urlRequest.urlopen(MIRROR_LOCATION + "/arachna2.html").read()
        local = open(PATH + "/files/arachna2.html", "wb")

        if not (local == mirror):

            a2_play_text.set("Updating...")

            local.write(mirror)
            local.close()

            sleep(2)
            a2_play_text.set("Play")

        else:
            messagebox.showinfo("PDS Launcher - Updater", "Game is already up-to-date!")

    except Exception as err:
        print(str(err))
        messagebox.showwarning("PDS Launcher - Update Failed", "Update failed: " + str(err))

def arachna2_uninstall():
    global a1_installed,a2_installed,a3_installed

    confirm = messagebox.askokcancel("PDS Launcher - Game Uninstaller", "Are you sure you want to uninstall the game? Depending on your browser, this game's data not be recoverable!")

    if (confirm == True):
        os.remove(PATH + "/files/arachna2.html")
        a2_installed = False
        a2_play_text.set("Install")
        RELOAD()

def arachnia_updater():
    try:
        mirror = urlRequest.urlopen(MIRROR_LOCATION + "/arachnia.html").read()
        local = open(PATH + "/files/arachnia.html", "wb")

        if not (local == mirror):

            a3_play_text.set("Updating...")

            local.write(mirror)
            local.close()

            sleep(2)
            a3_play_text.set("Play")

        else:
            messagebox.showinfo("PDS Launcher - Updater", "Game is already up-to-date!")

    except Exception as err:
        print(str(err))
        messagebox.showwarning("PDS Launcher - Update Failed", "Update failed: " + str(err))

def arachnia_uninstall():
    global a1_installed,a2_installed,a3_installed

    confirm = messagebox.askokcancel("PDS Launcher - Game Uninstaller", "Are you sure you want to uninstall the game? Depending on your browser, this game's data not be recoverable!")

    if (confirm == True):
        os.remove(PATH + "/files/arachnia.html")
        a3_installed = False
        a3_play_text.set("Install")
        RELOAD()


def cxr_updater():
    try:
        mirror = urlRequest.urlopen(MIRROR_LOCATION + "/cxr.html").read()
        local = open(PATH + "/files/cxr.html", "wb")

        if not (local == mirror):

            cxr_play_text.set("Updating...")

            local.write(mirror)
            local.close()

            sleep(2)
            cxr_play_text.set("Play")

        else:
            messagebox.showinfo("PDS Launcher - Updater", "Game is already up-to-date!")

    except Exception as err:
        print(str(err))
        messagebox.showwarning("PDS Launcher - Update Failed", "Update failed: " + str(err))

def cxr_uninstall():
    global a1_installed,a2_installed,a3_installed,cxr_installed

    confirm = messagebox.askokcancel("PDS Launcher - Game Uninstaller", "Are you sure you want to uninstall the game? Depending on your browser, this game's data not be recoverable!")

    if (confirm == True):
        os.remove(PATH + "/files/cxr.html")
        cxr_installed = False
        cxr_play_text.set("Install")
        RELOAD()



def launcher_updater():
        try:
            mirror = str(urlRequest.urlopen(MIRROR_LOCATION + "/launcher.pyw").read(), "'UTF-8'")
            local = open(PATH + "/launcher.pyw", "w")

            if not (local == mirror):
                cont = messagebox.askokcancel("PDS Launcher - Updater", "Continuing with update will automatically download and install the latest launcher version available. The launcher will automatically after the install finishes.\nDo you want to continue?")
                if (cont == True):
                    local.write(mirror)
                    local.close()

                    os.startfile(PATH + "/launcher.pyw")
                    sys.exit()
            else:
                messagebox.showinfo("PDS Launcher - Updater", "Launcher is already up-to-date")

        except Exception as err:
            messagebox.showwarning("PDS Launcher - Update Failed", "Failed to update launcher: " + str(err))

def launcher_uninstall():

    confirm = messagebox.askokcancel("PDS Launcher - Uninstaller", "Are you sure you want to uninstall the launcher? All related data, including games, will be removed from this device. Game data will be irrecoverable!\nNOTE: THE FOLLOWING DIRECTORY, AND ALL CONTENTS - LAUNCHER OR NOT - WILL BE REMOVED: " + PATH)

    if (confirm == True):
        shutil.rmtree(PATH)
        os.remove(WINDRIVE + ":/Users/" + os.getlogin() + "/Desktop/PDS Launcher.lnk")
        root.iconify()
        messagebox.showinfo("PDS Launcher - Uninstaller", "The launcher has been uninstalled")
        sys.exit()



def on_enter(e):e.widget['background'] = 'lightgreen'
def on_leave_play(e):e.widget['background'] = "lightblue"
def on_enter_cancel(e):e.widget['background'] = 'pink'
def on_leave(e):e.widget['background'] = 'SystemButtonFace'

RELOAD() # Load all the elements to the screen


if (__name__ == "__main__"):
    root.eval('tk::PlaceWindow . center')
    root.mainloop() 