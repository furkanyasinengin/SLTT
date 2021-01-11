import numpy as np
import cv2 as cv
from keras.models import load_model
import PILasOPENCV as ImageFont

def canlı_algılama():

    model = load_model("modeller/30epoch_tumu.h5")

    def getcnthull(mask_img):
        contours, hierarchy = cv.findContours(mask_img, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
        contours = max(contours, key=lambda x: cv.contourArea(x))
        hull = cv.convexHull(contours)
        return contours, hull

    k = 'sıfır', 'bir', 'iki', 'uc', 'dort', 'bes', 'altı', 'yedi', 'sekiz', 'dokuz'
    label_dict = {}
    for i in range(0, 10):
        label_dict[i] = k[i]
    r = ['aferin', 'araba', 'arkadas', 'bakkal', 'benim', 'bilgisayar', 'ders', 'durust', 'duymak', 'gulmek',
         'gunaydin', 'hastane', 'hesap', 'hızlı', 'icin', 'ihtiyac', 'ileri', 'insallah', 'internet', 'isim',
         'isitme cihazı', 'isitme engelli', 'istanbul', 'kafa', 'kardes', 'kirli', 'kitap', 'kolonya', 'konusmak',
         'lutfen', 'maske', 'memleket', 'merhaba', 'muayene', 'muhendis', 'nasıl', 'nasılsın', 'ne', 'nokta', 'not',
         'sag ol', 'selam', 'tamam', 'telefon', 'turkiye', 'ucgen', 'universite', 'vucut', 'yazmak', 'yurumek']
    for i in range(10, 60):
        label_dict[i] = r[i - 10]
    z = 'ABCDEFGHIJKLMNOPRSTUVYZ'
    for i in range(60, 83):
        label_dict[i] = z[i - 60]



    IMAGE_SIZE = 200
    CROP_SIZE = 400

    classes = label_dict
    cap = cv.VideoCapture(0)

    while (True):

        ret, img = cap.read()
        hsvim = cv.cvtColor(img, cv.COLOR_BGR2HSV)
        lower = np.array([0, 48, 80])
        upper = np.array([20, 255, 255])
        skinMask = cv.inRange(hsvim, lower, upper)

        blurred = cv.blur(skinMask, (2, 2))

        ret, thresh = cv.threshold(blurred, 0, 255, cv.THRESH_BINARY)

        contours, hull = getcnthull(thresh)
        cnt = contours

        x, y, w, h = cv.boundingRect(cnt)
        frame = cv.rectangle(img, (x - 50, y - 20), (x + w + 40, y + h + 10), (0, 255, 0), 2)


        cropped = frame[0:CROP_SIZE, 0:CROP_SIZE]
        resized_frame = cv.resize(cropped, (200, 200))
        reshaped_frame = (np.array(resized_frame)).reshape((1, 200, 200, 3))
        frame_for_model = reshaped_frame / 255


        prediction = np.array(model.predict(frame_for_model))
        predicted_class = classes[prediction.argmax()]
        print(predicted_class)
        with open("dosyalar/ayarlar/renk.txt", "r") as dosya:
            renk = dosya.readline()

        def numbers_to_strings(argument):
            switcher = {
                "red": (255,0,0),
                "blue": (0,0,255),
                "green": (0,255,0),
                "yellow": (255,255,0),
                "black": (0,0,0)
            }
            return switcher.get(argument, "nothing")
        a=numbers_to_strings(renk.lower())

        cv.putText(frame, predicted_class, (10, 450), 1, 2, a, 2, cv.LINE_AA)
        cv.imshow('Canlı Çeviri', frame)


        k = cv.waitKey(1) & 0xFF
        if k == ord('q'):
            break

    cap.release()
    cv.destroyAllWindows()