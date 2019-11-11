import os, sys, urllib.request
from tkinter import *
from tkinter.messagebox import *

__version__ = 2
__filename__ = "ShutDownNet"
__basename__ = os.path.basename(sys.argv[0])
__savepath__ = os.path.join(os.environ['APPDATA'], "QuentiumPrograms")
__iconpath__ = __savepath__ + "/{}.ico".format(__filename__)

try:urllib.request.urlopen("https://www.google.fr/", timeout=1); connection = True
except:connection = False
if not os.path.exists(__iconpath__):
    try:os.mkdir(__savepath__)
    except:pass
    if connection == True:
        try:urllib.request.urlretrieve("http://quentium.fr/+++PythonDL/{}.ico".format(__filename__), __iconpath__)
        except:pass

if connection == True:
    try:script_version = int(urllib.request.urlopen("http://quentium.fr/programs/index.php").read().decode().split(__filename__ + "<!-- Version: ")[1].split(" --></h2>")[0])
    except:script_version = __version__
    if script_version > __version__:
        if os.path.exists(__iconpath__):popup = Tk(); popup.attributes("-topmost", 1); popup.iconbitmap(__iconpath__); popup.withdraw()
        ask_update = askquestion(__filename__ + " V" + str(script_version), "Une mise à jour à été trouvée, souhaitez vous la télécharger puis l'éxécuter ?", icon="question")
        if ask_update == "yes":
            try:os.rename(__basename__, __filename__ + "-old.exe")
            except:os.remove(__filename__ + "-old.exe"); os.rename(__basename__, __filename__ + "-old.exe")
            if "-32" in str(__basename__):urllib.request.urlretrieve("http://quentium.fr/download.php?file={}-32.exe".format(__filename__), __filename__ + ".exe")
            else:urllib.request.urlretrieve("http://quentium.fr/download.php?file={}.exe".format(__filename__), __filename__ + ".exe")
            showwarning(__filename__, "Le programme va redémarrer pour fonctionner sous la nouvelle version.", icon="warning")
            os.system("start " + __filename__ + ".exe"); os._exit(1)

__filename__ = __filename__ + " V" + str(__version__)

import subprocess, time

def start_shutdown():
    computer = value1.get()
    if len(computer) >= 4:
        subprocess.Popen("shutdown -s -f -t 1 -m " + computer, stdout=subprocess.PIPE, shell=True)
        time.sleep(2)
        shutdownnet.destroy()
    else:
        showwarning(__filename__, "Erreur : L'ID du PC est trop court !")

shutdownnet = Tk()
width = 750
height = 500
shutdownnet.update_idletasks()
x = (shutdownnet.winfo_screenwidth() - width) // 2
y = (shutdownnet.winfo_screenheight() - height) // 2
shutdownnet.geometry("{}x{}+{}+{}".format(width , height, int(x), int(y)))
shutdownnet.resizable(width=False, height=False)
shutdownnet.configure(bg = "lightgray")
if os.path.exists(__iconpath__):
    shutdownnet.iconbitmap(__iconpath__)
shutdownnet.title(__filename__)
Label(shutdownnet, text="Bienvenue dans le programme de Shutdown !", font="impact 30", fg="red", bg="lightgray").pack(pady=50)
Label(shutdownnet, text="IP du PC a shutdown :", font="impact 20", fg="black", bg="lightgray").pack(pady=20)
value1 = StringVar()
Entry(shutdownnet, textvariable=value1, width=30, font="impact 20").pack()
Button(shutdownnet, text="Commencer à shutdown", command=start_shutdown, relief=GROOVE, width=25, font="impact 20", fg="black").pack(pady=50)
shutdownnet.mainloop()
