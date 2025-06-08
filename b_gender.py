import cv2
from transformers import pipeline
from PIL import Image

gender_classifier = pipeline("image-classification", model="rizvandwiki/gender-classification")

def classify_gender(face_image):
    if face_image.shape[0] < 10 or face_image.shape[1] < 10:
        return None, None
    rgb_image = cv2.cvtColor(face_image, cv2.COLOR_BGR2RGB)
    
    pil_image = Image.fromarray(rgb_image)
    results = gender_classifier(images=pil_image)

    label = results[0]['label']
    confidence = results[0]['score']

    return label, round(confidence,2)

