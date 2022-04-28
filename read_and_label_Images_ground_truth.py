from hashlib import new


def read_and_label_Images_ground_truth(old_data_path, new_data_path,val_size):
    """
    Diese Funktion liest den mvtec Datensatz ein und speichert diesen in einem neuen Ordner ab. 
    Alle Bilder werden etntweder als good oder bad abgelegt. ground_truth wird dabei nicht berücksichtigt 
    old_data_path = relativer Pfad zum mvtec Datensatz 
    new_data_path = relativer Pfad für den bereinigten Datensatz 

    """

# ------------------Imports---------------

    import numpy as np
    import pandas as np
    import os
    import shutil
    import glob
    import uuid


# ----------------Function-----------------

    dst_dir = new_data_path
    scr_dir = old_data_path

    # neues Verzeichnis erstellen
    objects = []
    objects_0 = os.listdir(scr_dir)

    # Alle Datein die Keine Verzeichniss sind löschen
    for k in range(len(objects_0)):
        if os.path.isdir(scr_dir+objects_0[k]):
            objects.append(objects_0[k])

    if not os.path.exists(new_data_path):
        os.makedirs(new_data_path)

    if not os.path.exists(new_data_path+'/train/'):
        os.makedirs(new_data_path+'/train/')

    if not os.path.exists(new_data_path+'/validation/'):
        os.makedirs(new_data_path+'/validation/')



# Daten in neues Verzeichnis kopieren
    
    folder_list = ["/ground_truth"]
    counter = 0
    for member in range(len(objects)):
        for i in range(len(folder_list)):
            scr_dir2 = scr_dir+objects[member]+folder_list[i]
            labels = os.listdir(scr_dir2)
            for n in range(len(labels)):
                if counter <= val_size:
                    #print(glob.iglob(os.path.join(scr_dir2+labels[n], "*.png")))
                    #print(os.path.join(scr_dir2+labels[n], "*.png"))
                    for jpgfile in glob.iglob(os.path.join(scr_dir2+"/"+labels[n], "*.png")):
                        filename = str(uuid.uuid4())+"_"+objects[member]
                        shutil.copy(jpgfile, dst_dir +'/validation/'+filename+'.png')
                else:
                    for jpgfile in glob.iglob(os.path.join(scr_dir2+"/"+labels[n], "*.png")):
                        filename = str(uuid.uuid4())+"_"+objects[member]
                        shutil.copy(jpgfile, dst_dir +'/train/'+filename+'.png')
                counter=counter+1
                        
