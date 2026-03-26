# tout les import
import os
import shutil
import tkinter as tk
from pathlib import Path
from tkinter import filedialog
from tkinter import messagebox

#variable de depart
dossier_choisis = None
clicked = False

#toute les liste
image = ['.png','.jpg','.jpeg','webp','.gif']
document = ['.txt','.pdf','.docx']
fusion = ['.stl','.obj']
video = ['.mp4','.mkv','.avi','.mov']


# action des boutons
def action():
  global clicked
  if clicked == False:
    messagebox.showerror("vous n'avez pas choisis le dossier a trier" )
  else:
    print('le bouton_valider a ete clicker')
    fenetre.destroy()
def dossier():
  global dossier_choisis
  global clicked
  dossier_choisis = filedialog.askdirectory(title='selectioner un fichier',mustexist=True)
  clicked = True
  print(dossier_choisis)

# creation fenetre
fenetre = tk.Tk()
fenetre.title('auto download organized')
fenetre.geometry('800x600+100+100')

# creation message
message = tk.Label(fenetre,text='bienvenue dans auto-download-organized')

#bouton creation dossier
CheckValue = tk.BooleanVar()

BoutonCheck = tk.Checkbutton(fenetre,text='creation de dossier',var=CheckValue)
BoutonCheck.place(x=350,y=300)

# creation bouton chosir dossier
bouton_choisir = tk.Button(fenetre,text='choisir le dossier a trier')
bouton_choisir.place(x=350,y=200)
bouton_choisir.config(command=dossier)

# bouton valider
bouton_valider = tk.Button(fenetre, text='valider')
bouton_valider.place(x=700,y=500) 
bouton_valider.config(command=action,bg='green')

# apparition de la fenetre
message.pack()
fenetre.mainloop()

#fonction 
def deplacer_fichier():
  
  #toute les variables

  espace = '\\'
  chemin_image = Path.home() / 'Pictures'
  FichierTrie = os.listdir(dossier_choisis)
  print(FichierTrie)
  chemin_documents = Path.home() / 'Documents'
  chemin_video = Path.home() / 'videos'
  Chemin_3D = Path.home() / '3D'
  Chemin_3D.mkdir(exist_ok=True)
  
  
  #boucle de trie
  while  FichierTrie:
   
    Chemin = Path(dossier_choisis,'\\',FichierTrie[0])
    extension = Chemin.suffix
    STRchemin = str(dossier_choisis)
    depart = STRchemin + espace + FichierTrie[0]
  
  
    if extension in image :
      STRchemin =  str(chemin_image)
      arriver = STRchemin + espace + FichierTrie[0]
      shutil.move(depart,arriver)
 
    elif extension in document:
      STRchemin = str(chemin_documents)
      arriver = STRchemin + espace + FichierTrie[0]
      shutil.move(depart,arriver)

    elif extension in video:
      STRchemin = str(chemin_video)
      arriver = STRchemin + espace + FichierTrie[0]
      shutil.move(depart,arriver)
 
    elif extension in fusion:
      STRchemin = str(Chemin_3D)
      arriver = STRchemin + espace + FichierTrie[0]
      shutil.move(depart,arriver)
 
    else :
      print('laisser dans telechargement')

    del FichierTrie[0]
def Cree_dossier():
    #toute les variables

  espace = '\\'
  os.mkdir(dossier_choisis + espace + 'image')
  os.mkdir(dossier_choisis + espace + 'document')
  os.mkdir(dossier_choisis + espace + 'video')
  os.mkdir(dossier_choisis + espace + '3D')
  chemin_image = dossier_choisis + espace + 'image'
  chemin_documents = dossier_choisis + espace + 'document'
  chemin_video = dossier_choisis + espace + 'video'
  chemin_3D = dossier_choisis + espace + '3D'
  FichierTrie = os.listdir(dossier_choisis)
  print(FichierTrie)
  
  
  #boucle de trie
  while  FichierTrie:
   
    Chemin = Path(dossier_choisis,'\\',FichierTrie[0])
    extension = Chemin.suffix
    STRchemin = str(dossier_choisis)
    depart = STRchemin + espace + FichierTrie[0]
  
  
    if extension in image :
      STRchemin =  str(chemin_image)
      arriver = STRchemin + espace + FichierTrie[0]
      shutil.move(depart,arriver)
 
    elif extension in document:
      STRchemin = str(chemin_documents)
      arriver = STRchemin + espace + FichierTrie[0]
      shutil.move(depart,arriver)

    elif extension in video:
      STRchemin = str(chemin_video)
      arriver = STRchemin + espace + FichierTrie[0]
      shutil.move(depart,arriver)
 
    elif extension in fusion:
      STRchemin = str(chemin_3D)
      arriver = STRchemin + espace + FichierTrie[0]
      shutil.move(depart,arriver)
 
    else :
      print('laisser dans telechargement')

    del FichierTrie[0]









if  CheckValue.get():
  print('il faut cree des dossier')
  Cree_dossier()
else:
  print('il faut deplacer les fichier')
  deplacer_fichier()
