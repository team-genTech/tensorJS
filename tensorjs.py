import tensorflowjs as tfjs
from keras.models import load_model
model=load_model('prop_improp_adam.h5')
tfjs.converters.save_keras_model(model,'tfjsmodel.json')