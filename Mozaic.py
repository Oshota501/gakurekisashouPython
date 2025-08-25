import tkinter as tk
import tkinter.filedialog as fd
import PIL.Image
import PIL.ImageTk
from PIL import ImageDraw,ImageFont,ImageOps,Image
from pathlib import Path

try:
    # Windows
    font=ImageFont.truetype("c:/Windows/Fonts/meiryo.ttc",54)
except OSError:
    # Mac
    font=ImageFont.truetype("/System/Library/Fonts/ヒラギノ角ゴシック W6.ttc",54)



def dispPhoto(path):
    newImage=PIL.Image.open(path)
    #imageX=newImage.width
    #imageY=newImage.height
    imageX, imageY = newImage.size

    newImage=PIL.Image.open(path)
    #.resize((newImage.width//5,newImage.height//5)).resize((imageX,imageY),resample=0)

    top_left = (0, 0)
    top_right = (imageX - 1, 0)
    bottom_left = (0, imageY - 1)
    bottom_right = (imageX - 1, imageY - 1)
    
    draw=ImageDraw.Draw(newImage)
    
    
    
    


    small_Image=newImage.resize((int(imageX*2/3),int(imageY*2/3)))
    small_ImageX,small_ImageY=small_Image.size
    small_Image=ImageOps.expand(small_Image,border=5,fill="red")

    

    back=Image.new("RGB",(imageX,imageY),(0,192,192))
    #back.resize((imageX,imageY),resample=0)

    newImage.paste(back,(0,0))
    newImage.paste(small_Image,((imageX-small_ImageX)//2,(imageY-small_ImageY)//2))

    #罪状
    zaizyou="学\n歴\n詐\n称"
    draw.multiline_text(((imageX-small_ImageX)//2-60,(imageY-small_ImageY)//2),zaizyou,fill=(0,0,0,255),font=font,stroke_width=3,stroke_fill="white")
    


    text="重要指名手配"

    bbox=draw.textbbox((0,0),text,font=font)
    textX=bbox[2]-bbox[0]
    textY=bbox[3]-bbox[1]

    text2="懸賞金100万円"
    bbox2=draw.textbbox((0,0),text2,font=font)
    text2X=bbox2[2]-bbox2[0]
    text2Y=bbox2[3]-bbox2[1]

    draw.text(((imageX-textX)/2,(imageY-textY)/12),text,fill=(255,0,0),font=font,stroke_width=3,stroke_fill="yellow")

    draw.text(((imageX-text2X)/2,(imageY-text2Y*2)),text2,fill=(255,0,0),font=font,stroke_width=3,stroke_fill="yellow")

    newImage=ImageOps.expand(newImage,border=5,fill="yellow")

    newImage.save("_Image.png")
    


    imageData=PIL.ImageTk.PhotoImage(newImage)
    imageLabel.configure(image=imageData)
    imageLabel.image=imageData

def openFile():
    fpath=fd.askopenfilename()
    if fpath:
        dispPhoto(fpath)

root=tk.Tk()
root.geometry("2000x1200")

btn=tk.Button(text="ファイルを開く",command=openFile)
imageLabel=tk.Label()
btn.pack()
imageLabel.pack()
root.mainloop()



