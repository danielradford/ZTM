import sys
import os
from PIL import Image

image_folder = sys.argv[1]
out_folder = sys.argv[2]

if not os.path.exists(out_folder):
    os.makedirs(out_folder)


    
ext=['jpg']
for filename in os.listdir(image_folder):
    print(filename)
    if filename[-3:] in ext:
        img = Image.open(f"{image_folder}{filename}")
        clean_name = os.path.splitext(filename)[0]
        img.save(f"{out_folder}{clean_name}.png",'png')
        print("All done")
        
    
    
    

