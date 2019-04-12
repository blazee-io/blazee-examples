from keras.models import Sequential
from keras.layers import Dense

# Function to create model, required for KerasClassifier
# As this function will need to be deployed with the model, it cannot be declared in the Notebook
def create_model():
    # create model
    model = Sequential()
    model.add(Dense(12, input_dim=8, activation='relu'))
    model.add(Dense(8, activation='relu'))
    model.add(Dense(1, activation='sigmoid'))
    # Compile model
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
    return model