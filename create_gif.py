import imageio.v2 as imageio
filenames= ['gaif1.jpg','gaif2.jpg']
images= []
for filename in filenames:
    images.append(imageio.imread(filename))
imageio.mimsave('gaif.gif',images,duration= 600, loop=0)