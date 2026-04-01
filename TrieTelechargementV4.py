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
espace = '\\'
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
  elif Choix_deplacer.get() != 'cree' and Choix_deplacer.get() != 'deplacer':
    messagebox.showerror("vous devez choisir que une methode de deplacement" )
  else:
    print('le bouton_valider a ete clicker')
    fenetre.destroy()
def dossier():
  global dossier_choisis
  global clicked
  dossier_choisis = filedialog.askdirectory(title='selectioner un fichier',mustexist=True)
  clicked = True

# creation fenetre
fenetre = tk.Tk()
fenetre.title('auto download organized')
fenetre.geometry('800x600+100+100')

# creation message
message = tk.Label(fenetre,text='welcome to auto-files-organized',font=('arial',30))
message.pack(pady=30)

# creation bouton chosir dossier
bouton_choisir = tk.Button(fenetre,text='choisir le dossier a trier',height=2,width=20,font=('arial',10))
bouton_choisir.pack(pady=50)
bouton_choisir.config(command=dossier)



#bouton deplacer
Choix_deplacer = tk.StringVar()
BoutonCheck2 = tk.Radiobutton(fenetre,text='deplacer les fichier dans les dossier par default ',var=Choix_deplacer,value='deplacer',font=('arial',10))
BoutonCheck2.pack(pady=30)



#bouton creation dossier
BoutonCheck = tk.Radiobutton(fenetre,text='creation de dossier dans le dossier choisis',var=Choix_deplacer,value='cree',font=('arial',10))
BoutonCheck.pack(pady=20)

# bouton valider
bouton_valider = tk.Button(fenetre, text='valider',width=10,height=1,font=('arial',15))
bouton_valider.pack(pady=30) 
bouton_valider.config(command=action,bg='green')
# apparition de la fenetre
fenetre.mainloop()

#fonction principal
def deplacer_fichier():
  
  #toute les variables

  espace = '\\'
  chemin_image = Path.home() / 'Pictures'
  FichierTrie = os.listdir(dossier_choisis)
  print(FichierTrie)
  chemin_documents = Path.home() / 'Documents'
  chemin_video = Path.home() / 'videos'
  chemin_2D = Path.home() / '2D'
  chemin_2D.mkdir(exist_ok=True)
  
  
  #boucle de trie
  while  FichierTrie:
   
    Chemin = Path(dossier_choisis,'\\',FichierTrie[0])
    extension = Chemin.suffix
    STRchemin = str(dossier_choisis)
    depart = STRchemin + espace + FichierTrie[0]
    existe_image = True
    existe_document = True
    existe_2D = True
    existe_video = True
    deplacer_image(extension,chemin_image,FichierTrie,depart,dossier_choisis,espace,existe_image)
    deplacer_document(extension,chemin_documents,FichierTrie,depart,dossier_choisis,espace,existe_document)
    deplacer_2D(extension,depart,chemin_2D,FichierTrie,dossier_choisis,espace,existe_2D)
    deplacer_video(extension,depart,chemin_video,FichierTrie,dossier_choisis,espace,existe_video)
 
    
    del FichierTrie[0]
def Cree_dossier():
    #toute les variables

  espace = '\\'
  
  chemin_image = dossier_choisis + espace + 'image'
  chemin_documents = dossier_choisis + espace + 'document'
  chemin_video = dossier_choisis + espace + 'video'
  chemin_2D = dossier_choisis + espace + '2D'
  FichierTrie = os.listdir(dossier_choisis)
  print(FichierTrie)

  
  #boucle de trie
  while  FichierTrie:
     chemin = Path(dossier_choisis + espace + 'image')
     existe_image = Path.exists(chemin)
     chemin = Path(dossier_choisis + espace + 'Documents')
     existe_document = Path.exists(chemin)
     chemin = Path(dossier_choisis + espace + 'Video')
     existe_video = Path.exists(chemin)
     chemin = Path(dossier_choisis + espace + '2D')
     existe_2D = Path.exists(chemin)
     Chemin = Path(dossier_choisis,'\\',FichierTrie[0])
     extension = Chemin.suffix
     STRchemin = str(dossier_choisis)
     depart = STRchemin + espace + FichierTrie[0]
  
     deplacer_image(extension,chemin_image,FichierTrie,depart,dossier_choisis,espace,existe_image)
     deplacer_document(extension,chemin_documents,FichierTrie,depart,dossier_choisis,espace,existe_document)
     deplacer_2D(extension,depart,chemin_2D,FichierTrie,dossier_choisis,espace,existe_2D)
     deplacer_video(extension,depart,chemin_video,FichierTrie,dossier_choisis,espace,existe_video)
     del FichierTrie[0]


# fonction deplacer
def deplacer_image(extension,chemin_image,FichierTrie,depart,dossier_choisis,espace,existe_image):
  if extension in image :
    if not existe_image:
      os.mkdir(dossier_choisis + espace + 'image')
    STRchemin =  str(chemin_image)
    arriver = STRchemin + espace + FichierTrie[0]
    shutil.move(depart,arriver)
def deplacer_document(extension,chemin_documents,FichierTrie,depart,dossier_choisis,espace,existe_document):
  if extension in document :
    if not existe_document:
      os.mkdir(dossier_choisis + espace + 'document')
    STRchemin = str(chemin_documents)
    arriver = STRchemin + espace + FichierTrie[0]
    shutil.move(depart,arriver)
def deplacer_2D(extension,depart,chemin_2D,FichierTrie,dossier_choisis,espace,existe_2D):
 if extension in fusion:
   if not existe_2D:
     os.mkdir(dossier_choisis + espace + '2D')
   STRchemin = str(chemin_2D)
   arriver = STRchemin + espace + FichierTrie[0]
   shutil.move(depart,arriver)  
def deplacer_video(extension,depart,chemin_video,FichierTrie,dossier_choisis,espace,existe_video):
  if extension in video:
    if not existe_video:
      os.mkdir(dossier_choisis + espace + 'video')
    STRchemin = str(chemin_video)
    arriver = STRchemin + espace + FichierTrie[0]
    shutil.move(depart,arriver)






if  Choix_deplacer.get() == 'cree':

  Cree_dossier()
elif Choix_deplacer.get() == 'deplacer':

  deplacer_fichier()

 