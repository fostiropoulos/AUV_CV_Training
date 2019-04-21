import matplotlib.pyplot as plt

w=15

h=15
fig=plt.figure(figsize=(20, 20))
columns = 4
rows = 4
import glob
from PIL import Image
import random
images=glob.glob("out/*")

random.shuffle(images)
for i in range(0, columns*rows):

	_frame=Image.open(images[i])
	fig.add_subplot(rows, columns, i+1)
	plt.imshow(_frame)
	plt.title(images[i])

plt.show()
