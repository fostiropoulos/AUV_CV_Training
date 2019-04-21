import glob


train_fl=open("data/train.txt","w")
for file in glob.glob("data/images/*.jpg"):
	train_fl.write("%s\n"%file)


class_num=0

import re
for img_txt in glob.glob("data/images/*.txt"):
	class_img=int(re.split('[^a-zA-Z0-9]', open(img_txt,"r").read())[0])
	class_num=max(class_num,class_img)
class_num+=1

fh=open("data/obj.names","w")

for idx in range(class_num):
	fh.write("class_%s\n"%idx)	
print("Found %s classes"%class_num)

from string import Template

filein = open( 'yolov3_tiny_cfg.template' )
src = Template( filein.read() )

classes=class_num

d={ 'classes':classes, 'filters':(5+classes)*3, 'max_batches':classes*2000, 'steps':"%d,%d"%(int(classes*0.8),int(classes*0.9)) }

result = src.substitute(d)

fh = open("yolov3_tiny.cfg","w")
fh.write(result)

filein = open( 'data/obj.data.template' )
src = Template( filein.read() )

classes=class_num

d={ 'classes':classes}

result = src.substitute(d)

fh = open("data/obj.data","w")
fh.write(result)
