import os
import shutil
import glob
import uuid
import errno
from distutils.dir_util import copy_tree

def list_files(dir):
    r = []
    for root, dirs, files in os.walk(dir):
        for name in files:
            r.append(os.path.join(root, name))
    return r
def make_dir_structure(goal_path):
    #goal_path Struktur erstellen
    if not os.path.exists(goal_path):
        os.makedirs(goal_path)

    if not os.path.exists(goal_path+'/train/'):
        os.makedirs(goal_path+'/train/')
    
    if not os.path.exists(goal_path+'/val/'):
        os.makedirs(goal_path+'/val/')

    return 0

def ground_truth_sort(start_path, goal_path, val_ratio):

    #make_dir_structure(goal_path)
    if not os.path.exists(goal_path):
        os.makedirs(goal_path)

    if not os.path.exists(goal_path+'/train/'):
        os.makedirs(goal_path+'/train/')
    
    if not os.path.exists(goal_path+'/val/'):
        os.makedirs(goal_path+'/val/')

    val_path = str(goal_path)+'/val/'    
    train_path = str(goal_path)+'/train/'

    copy_tree(start_path, train_path)
    first_loop = True

    for root, dirs, files in os.walk(train_path):

        if first_loop:
            base_root = root
            folders = dirs
            first_loop = False

        img_val_count = int(len(files)*val_ratio)

        for name in files:
            folder_name = os.path.basename(root)
            newname = name.rsplit('.', 1)[0]
            newname = newname.rsplit('_', 1)[0]
            if img_val_count > 0:
                os.rename(os.path.join(root, name),os.path.join(val_path, str(folder_name)+"_"+str(newname)+".png"))
                img_val_count -=1
            else:
                os.rename(os.path.join(root, name),os.path.join(base_root, str(folder_name)+"_"+str(newname)+".png"))

    for dirs in folders:
        shutil.rmtree(base_root+dirs)


# Zurzeit wird immer die Struktur vom ground_truth_sort "use_GT_structure = True" benutzt
def img_sort(start_path, goal_path, use_GT_structure = True):

    make_dir_structure(start_path, goal_path)
    val_path = str(goal_path)+'val/'    
    train_path = str(goal_path)+'train/'




    """for root, dirs, files in os.walk(train_path):  # replace the . with your starting directory
        for file in files:
            path_file = os.path.join(root,file)
            shutil.copy2(path_file,str(goal_path)+"train/") # change you destination dir
            
            
        if dingo:
        print("----------")
        print(name)
        print(dirs)
        print(root)
        print(folder_name)
        print("----------")
            """

