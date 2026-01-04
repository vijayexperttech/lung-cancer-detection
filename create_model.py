import tensorflow as tf
from tensorflow.keras import layers, models
import os

def create_dummy_model():
    print("Creating dummy CNN model...")
    
    # Simple CNN architecture
    model = models.Sequential([
        # Input layer: expect 224x224 RGB images
        layers.Input(shape=(224, 224, 3)),
        
        # First Convolutional Block
        layers.Conv2D(32, (3, 3), activation='relu'),
        layers.MaxPooling2D((2, 2)),
        
        # Second Convolutional Block
        layers.Conv2D(64, (3, 3), activation='relu'),
        layers.MaxPooling2D((2, 2)),
        
        # Third Convolutional Block
        layers.Conv2D(64, (3, 3), activation='relu'),
        
        # Flatten and Dense Layers
        layers.Flatten(),
        layers.Dense(64, activation='relu'),
        
        # Output Layer: 3 classes (Cancerous, Non-Cancerous, Malignant)
        # Using Softmax for probability distribution
        layers.Dense(3, activation='softmax')
    ])

    model.compile(optimizer='adam',
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])

    model.summary()

    # Save the model
    model_path = 'model.h5'
    model.save(model_path)
    print(f"Model saved to {model_path}")

if __name__ == "__main__":
    create_dummy_model()
