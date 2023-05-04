import os
import shutil
import glob
from tqdm import tqdm
Raw_DIR="C:/Users/S U B H A M/Downloads/Compressed/Driver-Drowsiness-Detection-using-Deep-Learning-main/Driver-Drowsiness-Detection-using-Deep-Learning-main/mrlEyes_2018_01"
for dirpath, dirname, filenames in os.walk(Raw_DIR):
    for i in tqdm([f for f in filenames if f.endswith('.png')]):
        if i.split('_')[4]=='0':
            shutil.copy(src=dirpath+'/'+i, dst="C:/Users/S U B H A M/Downloads/Compressed/Driver-Drowsiness-Detection-using-Deep-Learning-main/Driver-Drowsiness-Detection-using-Deep-Learning-main/Prepared_Data/Close")
        elif i.split('_')[4]=='1':
            shutil.copy(src=dirpath+'/'+i, dst="C:/Users/S U B H A M/Downloads/Compressed/Driver-Drowsiness-Detection-using-Deep-Learning-main/Driver-Drowsiness-Detection-using-Deep-Learning-main/Prepared_Data/Open")    
            
        
