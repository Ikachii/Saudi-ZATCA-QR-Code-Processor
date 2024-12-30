from qreader import QReader
import cv2
import base64
from CSV_Maker import *
import Images_Processor
import pandas 

def main(input_folder, outputfolder):
    df = pandas.DataFrame
    images = Images_Processor.load_images_from_folder(input_folder)
    for i in images:
         qreader = QReader()
         image = cv2.cvtColor(i, cv2.COLOR_BGR2GRAY)
         decoded_text = qreader.detect_and_decode(image=image)
         for t in decoded_text:
            temp = base64.b64decode(t)
            df = add_to_csv(temp)
   


    
    output_final_csv(df,outputfolder)
    
