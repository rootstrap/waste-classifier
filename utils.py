from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.mobilenet import preprocess_input

import numpy as np
import matplotlib.pyplot as plt


def classify_image(img_path, model):
    img = image.load_img(img_path, target_size=(224, 224))
    arr_img = image.img_to_array(img)
    arr_img = np.expand_dims(arr_img, axis=0)
    arr_img = preprocess_input(arr_img)
    preds = model.predict(arr_img)
    return preds # [(class, description, probability)]


def plot_results(history):
    # summarize history for accuracy
    plt.plot(history.history['accuracy'])
    plt.plot(history.history['val_accuracy'])
    plt.title('model accuracy')
    plt.ylabel('accuracy')
    plt.xlabel('epoch')
    plt.legend(['train', 'val'], loc='upper left')
    plt.show()
    # summarize history for loss
    plt.plot(history.history['loss'])
    plt.plot(history.history['val_loss'])
    plt.title('model loss')
    plt.ylabel('loss')
    plt.xlabel('epoch')
    plt.legend(['train', 'val'], loc='upper left')
    plt.show()
