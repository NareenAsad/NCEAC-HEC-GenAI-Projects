import gradio as gr
import numpy as np
from PIL import Image
import tensorflow as tf
import json

# 1. LOAD MODEL

MODEL_PATH = "animal_classifier_model.h5"
model = tf.keras.models.load_model(MODEL_PATH)

# 2. LOAD CLASS INDICES
with open("class_indices.json", "r") as f:
    class_indices = json.load(f)

# Convert index → class name (VERY IMPORTANT)
class_names = list(class_indices.keys())

print("Loaded classes:", class_names)

# 3. PREDICT FUNCTION

def predict(img):
    try:
        img = img.convert("RGB")
        img = img.resize((224, 224))

        img_array = np.array(img) / 255.0
        img_array = np.expand_dims(img_array, axis=0)

        pred = model.predict(img_array)
        idx = np.argmax(pred)

        return f"Predicted Animal: {class_names[idx]}"

    except Exception as e:
        return f"❌ Error during prediction: {str(e)}"


# 4. GRADIO UI

demo = gr.Interface(
    fn=predict,
    inputs=gr.Image(type="pil"),
    outputs="text",
    title="🐾 Animal Classifier",
    description="Upload an animal image and the model will classify it.",
)

# 5. LAUNCH APP

demo.launch()