# pip install pyinstaller
import os
import shutil
from pathlib import Path
image = ['.png','.jpg','.jpeg','webp','.gif']
document = ['.txt','.pdf','.docx']
fusion = ['.stl','.obj']
video = ['.mp4','.mkv','.avi','.mov']

FichierTrie = os.listdir('C:\\Users\\matit\\Downloads')
print(FichierTrie)


while  FichierTrie:
  Chemin = Path('C:\\Users\\matit\\Downloads','\\',FichierTrie[0])
  print(Chemin.suffix)
  extension = Chemin.suffix
  depart = 'C:\\Users\\matit\\Downloads\\' + FichierTrie[0]
  
  if extension in image :
    print('cest une image')
    arriver = 'C:\\Users\\matit\\Pictures\\' + FichierTrie[0]
    shutil.move(depart,arriver)
 
  elif extension in document:
    print('sa va dans document')
    arriver = 'C:\\Users\\matit\\Documents\\' + FichierTrie[0]
    shutil.move(depart,arriver)
  elif extension in video:
    print('ses une video')
    arriver = 'C:\\Users\\matit\\Videos\\' + FichierTrie[0]
    shutil.move(depart,arriver)
  elif extension in fusion:
    print('sa va dans 3D')
    arriver = 'C:\\Users\\matit\\Desktop\\FUSION\\' + FichierTrie[0]
    shutil.move(depart,arriver)
  else :
    print('laisser dans telechargement')

  del FichierTrie[0]






