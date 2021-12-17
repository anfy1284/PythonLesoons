import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"

import numpy as np
import matplotlib.pyplot as plt
#from tensorflow import keras
#import tensorflow.keras.layers as Dense
from tensorflow.keras.layers import Dense
import tensorflow.keras as keras


c = np.array([-40,-10,0,8,15,22,38])
f = np.array([-40,14,32,46,59,72,100])

model = keras.Sequential()
model.add(Dense(units=1, input_shape=(1,), activation='linear'))
model.compile(loss='mean_squared_error', optimizer=keras.optimizers.Adam(0.1))

history = model.fit(c, f, epochs=500, verbose=0)
plt.plot(history.history['loss'])
plt.grid(True)
plt.show()

for i in range(0, 50):
  print(i, model.predict([i]))