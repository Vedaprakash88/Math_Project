import os
import ocrmypdf as op
import pytesseract
import easygui

file = easygui.fileopenbox(default="C:\\Users\\vedap\\*.pdf", msg="Please select a PDF file", title="PDF OCR Task")
file_name = os.path.basename(file)
s_file_name = os.path.splitext(file_name)
s_file_name = s_file_name[0] + "_OCR" + s_file_name[1]
save_def = os.path.join(os.path.dirname(file), s_file_name)


save_file = easygui.filesavebox(default=save_def, msg="Please select a folder to save file", title="PDF OCR Task")
try:
    pytesseract.pytesseract.tesseract_cmd = r'C:\Users\vedap\AppData\Local\Tesseract-OCR\tesseract.exe'
    op.ocr(input_file=file, output_file=save_file, output_type="pdf", skip_text=True)
except:
    print("!!!!!!! OPERATION ABORTED !!!!!!!!!!! \nCheck the following: \n      --input file path"
          "\n      --output file path \n      --if the pdf already has text")
