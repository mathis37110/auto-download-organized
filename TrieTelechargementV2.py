
import os
import shutil
import tkinter as tk
from pathlib import Path

image = ['.png','.jpg','.jpeg','webp','.gif']
document = ['.txt','.pdf','.docx']
fusion = ['.stl','.obj']
video = ['.mp4','.mkv','.avi','.mov']

espace = '\\'
chemin_image = Path.home() / 'Pictures'
chemin_downloads = Path.home() / 'Downloads'
FichierTrie = os.listdir(chemin_downloads)
chemin_documents = Path.home() / 'Documents'
chemin_video = Path.home() / 'videos'
Chemin_3D = Path.home() / '3D'
Chemin_3D.mkdir(exist_ok=True)



while  FichierTrie:
  Chemin = Path(chemin_downloads,'\\',FichierTrie[0])
  extension = Chemin.suffix
  STRchemin = str(chemin_downloads)
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






