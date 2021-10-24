from PIL import Image, ImageDraw, ImageFont
import tkinter.messagebox as box
def insertDateTime(path, date, fontSize, fontColor, ext1, ext2):
    try:
        img = Image.open(path)
        ext = path.split('.')[-1]
        p1 = path.split('/')
        path = '/'.join(p1[0:-1])
        imgName = p1[-1].split('.')[0]
        # print("IMAGE : ", img)
        if(fontSize==''):
            fontSize = 148
        if(date==''):
            s = img._getexif()[36867]
            s = s[8:10] + '/' + s[5:7] + '/' + s[0:4] + ' ' + s[11:16]
        else:
            s = date
        if(ext1!=''):
            s += '\n'+ext1
        if(ext2!=''):
            s += '\n'+ext2

        # img = img.rotate(270)
        d1 = ImageDraw.Draw(img)
        w, h = img.size
        font = ImageFont.truetype("arial.ttf", int(fontSize))
        text_w , text_h = d1.textsize(s, font)
        w_pad = int(w*0.1)
        h_pad = int(h*0.1)
        d1.text((w - text_w - w_pad, h - text_h - h_pad), s, fill=fontColor, font=font)
        img.save(path +'/STAMPED' + imgName + '.' + ext)
    except:
        box.showerror("Error", "An Error while executing File : " + imgName +". Probably the file is not an Image or the Image doesn't has a date attribute. Try going in the properties of the image and seeing if the date created exists. If it exists kindly contact the software publisher." )

#DEV MODE
# insertDateTime('./20211021_192316.jpg', '', '', (255, 161, 7), '', '')
