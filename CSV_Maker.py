import pandas as pd
import uttlv

data = {'Name': [], 'Number': [], 'Date and Time' : [], 'Total Price': [], 'VAT 15%' : []}
df = pd.DataFrame(data)

def add_to_csv(temp):
    try:
        t = uttlv.TLV()
        t.parse_array(temp)
        df.loc[len(df)] = [t[0x01].decode('utf-8'), t[0x02].decode("utf-8-sig"),t[0x03].decode("utf-8"),t[0x04].decode("utf-8"),t[0x05].decode("utf-8")]
        print('Decoded Successfully!')
        return df
    except:
        print('Failure to decode 1 qr code please ensure all qr codes are ZATCA')
        return df

    

def output_final_csv(dff, output_folder_path):
    dff.to_csv(output_folder_path + '/' + 'output.csv', index = False)






