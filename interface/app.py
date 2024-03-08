
from extraction import *
import os, sys
import tkinter as tk
from tkinterdnd2 import DND_FILES, TkinterDnD
from tkinter import scrolledtext
from tkinter import filedialog as fd
import tkintermapview as tkmv


file_paths = ""


def drop(event):
    global file_paths
    file_paths = event.data
    print(file_paths)

def get_path():
    global zone_csv_text
    # zone_csv.create_text.destroy()
    zone_csv_text = main(file_paths)
    # zone_csv.create_text(taill, text= zone_csv_text, anchor=W,fill="Blue", font="Arial 10 bold")
    change_text(zone_csv_text)


def conversion(path=""):
    pass


def affichage_dialoge():
    """
    Affiche le formatage du fichier CSV à charger dans le logiciel.
    """
    Text_affiche_form_CSV="""
    #Formatage fichier CSV
    ## Le fichier ne doit pas avoir d'entete
    |Nom du producteur|numero du producteur|la culture|la zone|ville|village|coordonnées|
    |-----------------|--------------------|----------|-------|-----|-------|-----------|
    |kouassi kouadio |0123493833|riz|centre|yamoussoukro|gbangbassou|[[[][]][[][]]]|
    """
    def on_scroll(*args):
        can_can.xview(*args)
    

    can = TkinterDnD.Tk()
    can.config(bg="yellow")
    can.resizable(width=False, height=False)
    can.title("Information formatage fichier CSV")
    can_can = tk.Canvas(can, width=400, height=100, bg="yellow")
    can_can.pack(fill=tk.BOTH, expand=True)

    scrollbar = tk.Scrollbar(can, orient=tk.HORIZONTAL, command=on_scroll)
    scrollbar.pack(side=tk.BOTTOM, fill=tk.X)
    can_can.configure(xscrollcommand=scrollbar.set)

    frame = tk.Frame(can_can)
    can_can.create_window((0,0), window = frame, anchor="nw")

    label = tk.Label(frame, text=Text_affiche_form_CSV)
    label.pack()

    frame.update_idletasks()
    can_can.config(scrollregion=can_can.bbox("all"))

# def drag(event):
#     event.widget.dnd_start(DND_FILES, event.data)


def save_file(file_path):
    # Vérifier si le chemin du fichier existe et est un fichier
    if not os.path.exists(file_path) or not os.path.isfile(file_path):
        print("Erreur: Le chemin spécifié n'est pas valide.")
        return False
    
    # Définir le répertoire de destination où enregistrer le fichier
    destination_dir = "./csv_file_history"  # Vous pouvez changer ce chemin selon vos besoins
    
    # Vérifier si le répertoire de destination existe, sinon le créer
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)
    
    # Extraire le nom du fichier à partir du chemin
    file_name = os.path.basename(file_path)
    
    # Construire le chemin complet du fichier de destination
    destination_file_path = os.path.join(destination_dir, file_name)
    
    try:
        # Copier le fichier vers le répertoire de destination
        shutil.copy2(file_path, destination_file_path)
        return True
    except Exception as e:
        print("Erreur lors de l'enregistrement du fichier:", e)
        return False


def change_text(text):
    zone_csv.itemconfig(item_zone_csv, text=text)

def select_file():
    filetypes = (
        ('geojson', '.geojson'),
        ('All files','*.*')
    )
    filename = fd.askopenfilename(title='Ouvrir un fichier', initialdir="./", filetypes=filetypes)
    view_geojson(filename)

def view_geojson(path):
    data=read_geojson(path)
    for i in range(0, len(data[0])):
        map_widget.set_address("Ivory coast", marker=True, text=data[1][i])
        map_widget.set_polygon(data[0][i],fill_color="springgreen",
                                   outline_color="black",
                                   border_width=8,
                                   name=data[1][i])
    map_widget.set_zoom(10)


# Créer une fenêtre principale
root = TkinterDnD.Tk()
root.geometry('800x500')
root.resizable(width=False, height=False) # Block window resizing
root.config(bg="grey")
zone_csv_text = "Glissez-déposez un\nfichier CSV ici"
#creation de la zone de recuperation du fichier CSV
zone_csv = tk.Canvas(root,bg='ivory',  height=450, width=200)
taill= (10, 450//2)
item_zone_csv=zone_csv.create_text(taill, text= zone_csv_text, anchor=W,fill="Blue", font="Arial 10 bold")
zone_csv.grid(row=1, column=0, rowspan=3, columnspan=2, padx=1, pady=10)

# Zone d'affichage geojson apres conversion
zone_geojson = tk.Canvas(root,bg='grey',  height=450, width=590)
zone_geojson.grid(row=1, rowspan=3, column=3, columnspan=3, padx=1, pady=1)
# ajout de map view
map_widget = tkmv.TkinterMapView(zone_geojson, height=445, width=585, corner_radius=0)
map_widget.place(relx=.5, rely=.5, anchor=CENTER)


bout_Afficher = tk.Button(root, text="VOIR GEOJSON", width=20, height=1, command=select_file)# afficher des données csv
bout_Afficher.grid(row=4,column=1, rowspan=2)
bout_conver = tk.Button(root, text="Conversion", width=20, height=1, command=get_path) #conversion fichier csv en geojson
bout_conver.grid(row=4,column=3, rowspan=2)
bout_quit = tk.Button(root, text="Quitter", command=quit, width=50, height=1)
bout_quit.grid(row=4,column=4, rowspan=2)
bout_info = tk.Button(root, text="CSV info", command=affichage_dialoge)
bout_info.grid(row=4,column=5)



zone_csv.drop_target_register(DND_FILES)
zone_csv.dnd_bind('<<Drop>>', drop)


# Lancer la boucle principale
root.mainloop()
