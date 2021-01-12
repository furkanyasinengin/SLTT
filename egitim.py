import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras import layers
from tensorflow.keras import Model
from tensorflow.keras.applications import InceptionResNetV2
from tensorflow.keras.optimizers import SGD

TRAINING_DIR = 'D:/veri_seti/veriseti/egitim'


IMAGE_SIZE = 200
BATCH_SIZE = 64

data_generator = ImageDataGenerator(
    samplewise_center=True,
    samplewise_std_normalization=True,
    brightness_range=[0.8, 1.0],
    validation_split=0.1)

train_generator = data_generator.flow_from_directory(TRAINING_DIR, target_size=(IMAGE_SIZE, IMAGE_SIZE), shuffle=True,
                                                     seed=13,
                                                     class_mode='categorical', batch_size=BATCH_SIZE, subset="training")


validation_generator = data_generator.flow_from_directory(TRAINING_DIR, target_size=(IMAGE_SIZE, IMAGE_SIZE),
                                                          shuffle=True, seed=13,
                                                          class_mode='categorical', batch_size=BATCH_SIZE,
                                                          subset="validation")

inception_resv2_model = InceptionResNetV2(
    input_shape=(IMAGE_SIZE, IMAGE_SIZE, 3),
    include_top=False,
    weights='imagenet'
)

for layer in inception_resv2_model.layers[:550]:
    layer.trainable = False
for layer in inception_resv2_model.layers[550:]:
    layer.trainable = True


inception_output = inception_resv2_model.output

x = layers.GlobalAveragePooling2D()(inception_output)
x = layers.Dense(1024, activation='relu')(x)
x = layers.Dense(83, activation='softmax')(x)

model = Model(inception_resv2_model.input, x)

model.compile(
    optimizer=SGD(lr=0.0001, momentum=0.9),
    loss='categorical_crossentropy',
    metrics=['acc']
)
LOSS_THRESHOLD = 0.2
ACCURACY_THRESHOLD = 0.95


class ModelCallback(tf.keras.callbacks.Callback):
    def on_epoch_end(self, epoch, logs={}):
        if logs.get('val_loss') <= LOSS_THRESHOLD and logs.get('val_acc') >= ACCURACY_THRESHOLD:
            print("\nReached", ACCURACY_THRESHOLD * 100, "accuracy, Stopping!")
            self.model.stop_training = True


callback = ModelCallback()
history = model.fit_generator(
    train_generator,
    validation_data=validation_generator,
    steps_per_epoch=100,
    validation_steps=50,
    epochs=30,
    shuffle=True,
    callbacks=[callback])

MODEL_NAME = 'modeller/30epoch_v2.h5'
model.save(MODEL_NAME)
