# -*- coding: utf-8 -*-

"""
Testing image_processing module.
Some basic tests.

@author Rodrigo Hernandez-Mota
"""

from image_processing import getImage, meanTransform, \
                             detectPattern, vectorizeImage
import matplotlib.pyplot as plt
import os


# -- test
os.chdir("/home/rhdzmota/Documents/github_rhdzmota/spaceImage")
random_url = ["https://scontent-dft4-3.cdninstagram.com/t51.2885-15/e15/1" +
              "1117123_1573315852918334_958981448_n.jpg", "", "", "", "", "",
              "", "", "", "", "", "", "", "", "", ""]
random_url[1] = "https://scontent-dft4-3.xx.fbcdn.net/v/t1.0-9/11102659_1" + \
                "0206374473751244_5351125610966806514_n.jpg?oh=e2ee4dac0b" + \
                "49b4de1db13e7508cd215b&oe=59E7F059"
random_url[2] = "https://scontent-dft4-3.xx.fbcdn.net/v/t1.0-9/18274950_10" + \
                "158584551555534_9137790487492861207_n.jpg?oh=4e4aa99af5e9" + \
                "713b046f80710e5456a3&oe=59E9BEB7"
random_url[3] = "https://scontent-dft4-3.xx.fbcdn.net/v/t1.0-9/1382846_1015" +\
                "3387587430534_1418636478_n.jpg?oh=4755c85ae224f69d9a21b0ef" +\
                "c62b8f4d&oe=599CD22A"
random_url[4] = "https://scontent-dft4-3.xx.fbcdn.net/v/t1.0-9/1000622_1015" +\
                "1737353751169_763976283_n.jpg?oh=86e8da9a8594614099fc98124" +\
                "882fc20&oe=59B12321"
random_url[5] = "https://scontent-dft4-3.xx.fbcdn.net/v/t1.0-9/r270/1379898" +\
                "_10151737376816169_453056682_n.jpg?oh=e43ab7ddde09e1e2872b" +\
                "545bd30ae552&oe=59DD05E9"
random_url[6] = "https://scontent-dft4-3.xx.fbcdn.net/v/t1.0-9/r270/1378297" +\
                "_10151737377531169_651130858_n.jpg?oh=827cac15981780a06f12" +\
                "f5295f4b3e9a&oe=59DC8CF2"
random_url[7] = "https://scontent-dft4-3.xx.fbcdn.net/v/t1.0-9/1391615_1015" +\
                "1737398611169_747950142_n.jpg?oh=4dd7e2380d414087451e370f7" +\
                "4432176&oe=59E6BB2E"
random_url[8] = "https://scontent-dft4-3.xx.fbcdn.net/v/t1.0-9/1422461_1015" +\
                "1737397161169_1864502925_n.jpg?oh=2c15e53b81c03abfd374788a" +\
                "a61a2181&oe=599C9F72"
random_url[9] = "https://scontent-dft4-3.xx.fbcdn.net/v/t1.0-9/580572_10151" +\
                "737400951169_1558192568_n.jpg?oh=0eba48014ffa1fe6cc8612c40" +\
                "38aa536&oe=59A133A4"
random_url[10] = "https://scontent-dft4-3.xx.fbcdn.net/v/t1.0-9/16196083_67" +\
                 "2829416231962_2029245584193018892_n.jpg?oh=8750f2e551bae3" +\
                 "c67745b49e5fd01e71&oe=59AA4FA2"
random_url[11] = "https://scontent-dft4-3.cdninstagram.com/t51.2885-15/e35/" +\
                 "18812311_133619987206952_5150552995003367424_n.jpg"
random_url[12] = "https://scontent-dft4-3.cdninstagram.com/t51.2885-19/s600" +\
                 "x600/18809150_233913160428683_742831631978463232_a.jpg"
random_url[13] = "https://scontent-dft4-3.cdninstagram.com/t51.2885-15/e35/" +\
                 "17267618_1279120348803656_1506801989181243392_n.jpg"
random_url[14] = "https://scontent-dft4-3.cdninstagram.com/t51.2885-15/s640" +\
                 "x640/sh0.08/e35/14474004_1184781951597153_412250564589309" +\
                 "1328_n.jpg"
random_url[15] = "https://scontent-dft4-3.cdninstagram.com/t51.2885-15/s640" +\
                 "x640/sh0.08/e35/13249646_660859247395150_196297464_n.jpg"


imgs = [getImage(i) for i in random_url]

shapes = [i.shape for i in imgs]

img = imgs[0]

plt.imshow(img)
plt.show()

temp = meanTransform(img)
temp.shape
plt.imshow(temp)
plt.show()

data = detectPattern(temp)
vect = vectorizeImage(data)
