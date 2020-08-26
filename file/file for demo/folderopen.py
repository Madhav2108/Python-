import os
import sys          #module for terminating 
import glob
import tkinter as tk
from tkinter import filedialog
count=0
root = tk.Tk()
root.withdraw()
targetdir = filedialog.askdirectory()
for root, subFolders, files in os.walk(targetdir):
    print(root,"",subfolder,"",files)
    os.chdir(root)
