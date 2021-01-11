from keras.preprocessing.image  import ImageDataGenerator,array_to_img,img_to_array,load_img
import os

for y in os.listdir("D:/veri_seti/egitim"):
    for x in os.listdir("D:/veri_seti/egitim/"+y):
        datagen=ImageDataGenerator(rescale=1./255,
                                    rotation_range=40,
                                   horizontal_flip=True,
                                   vertical_flip=True)
                                   #fill_mode='nearest')

        img=load_img('D:/veri_seti/egitim/'+y+"/"+x)
        x=img_to_array(img)
        x=x.reshape((1,)+x.shape)
        i=0
        for batch in datagen.flow(x,batch_size=1,
                                  save_to_dir='D:/veri_seti/egitim/'+y,save_prefix=y,seed=1,
                                  save_format='jpg'):
            i+=1
            if i>3517:
                break
        if(1):
            break
