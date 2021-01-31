from PIL import Image
import os
imgList=os.listdir("imgs")
convertedImgList=[]
for image in imgList:
    convertedImgList.append(Image.open("imgs//"+image).convert("RGB"))
firstImg=convertedImgList.pop(0)
pdfName = "test.pdf"
firstImg.save(pdfName, "PDF" ,resolution=100.0, save_all=True, append_images=convertedImgList)
os.rename("test.pdf", "pdf/Output.pdf")