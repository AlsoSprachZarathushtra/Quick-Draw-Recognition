
from tensorflow import keras
import numpy as np
import heapq
from PIL import Image

class Predictor():
    def __init__(self):
        class_dict_path = 'labels_dict.npy'
        temp_dict = np.load(class_dict_path)
        weights_path = 'best_model_densenet121_binary.ckpt'
        self.labels_dict = {k: v for k, v in enumerate(temp_dict)}
        self.model = self.load_model(weights_path)
        self.model.summary()
        
    def load_model(self, weights_path):
        model = keras.applications.DenseNet121(input_shape=(128,128,1),
                                               include_top=True,
                                               weights=weights_path,
                                               classes=340
                                               )
        return model

        
    def img_preprocess(self,img):
        img = img.resize((128,128))
        img.save('temp.jpg')
        img = np.array(img)
        img = img[np.newaxis,:,:,np.newaxis]
        return img
    
    def nums2label(self,y):
        result = self.labels_dict[y]
        return result
    
    def predict(self, img):
        img = self.img_preprocess(img)
        y_pred = self.model.predict(img)
#        print(y_pred.shape)
        y_pred = np.argmax(y_pred[0])
        result = self.nums2label(y_pred)
#        y_pred = map(list(y_pred[0]).index, heapq.nlargest(3, list(y_pred[0])))
#        y_pred = list(y_pred)
#        print('y_pred',y_pred)
#        result =[]
#        for y in y_pred:
#            y_str = self.nums2label(y)
#            result.append(y_str)
#        print('result',result)
        return result
    
if __name__ == "__main__":
    predictor = Predictor()
    
        