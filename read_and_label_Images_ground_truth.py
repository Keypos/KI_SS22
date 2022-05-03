from hashlib import new


def read_and_label_Images_ground_truth(old_data_path, new_data_path, val_size):
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
    temp_folder = new_data_path+'tmp/'
    if not os.path.exists(new_data_path+'/tmp/'):
        os.makedirs(new_data_path+'/tmp/')

    folder_list = ["/ground_truth"]
    counter = 0
    for member in range(len(objects)):
        for i in range(len(folder_list)):
            scr_dir2 = scr_dir+objects[member]+folder_list[i]
            labels = os.listdir(scr_dir2)
            for n in range(len(labels)):

                for jpgfile in glob.iglob(os.path.join(scr_dir2+"/"+labels[n], "*.png")):
                    filename = str(uuid.uuid4())+"_"+objects[member]
                    shutil.copy(jpgfile, temp_folder+filename+'.png')

    # Anzahl aller Ground truth datan erfassen
    img_count = os.listdir(temp_folder)
    # berechnen der Validation größe
    val_count = int(len(img_count)*val_size)

    # Daten in train und Validation aufteilen

    for i in range(len(img_count)):
        if i <= val_count:
            shutil.copy(temp_folder+img_count[i], dst_dir+'validation/')
        else:
            shutil.copy(temp_folder+img_count[i], dst_dir+'train/')
    # temp_foler wieder löschen

    try:
        shutil.rmtree(temp_folder)
    except OSError as e:
        print("Error: %s - %s." % (e.filename, e.strerror))
