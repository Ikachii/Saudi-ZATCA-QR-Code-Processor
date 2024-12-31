from qreader import QReader
import cv2
import base64
from CSV_Maker import *
import Images_Processor
import pandas 


def main(input_folder, outputfolder):
    data = {'Name': [], 'Number': [], 'Date and Time' : [], 'Total Price': [], 'VAT 15%' : []}
    df = pd.DataFrame(data)
    images = Images_Processor.load_images_from_folder(input_folder)
    for i in images:
         qreader = QReader()
         image = cv2.cvtColor(i, cv2.COLOR_BGR2GRAY)
         decoded_text = qreader.detect_and_decode(image=image)
         for t in decoded_text:
            if t is None:
                print('QR Code not detected please take a clearer picture')
            else:
                temp = base64.b64decode(t)
                df = add_to_csv(temp)
   


    
    output_final_csv(df,outputfolder)
    
