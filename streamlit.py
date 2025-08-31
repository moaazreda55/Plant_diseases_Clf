import streamlit as st
from PIL import Image
import torch
from torchvision import transforms


MODEL_PATH = "models/plant.pth"

model = torch.load(MODEL_PATH, map_location='cpu', weights_only=False)
model.eval()

CLASS_NAMES = {
    0: "Healthy", 
    1: "Powdery",
    2: "Rust"
}

st.title("Plant Image Classifier")

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png"])

if uploaded_file is not None:
   
    image = Image.open(uploaded_file).convert('RGB')
    
    transform = transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
    ])

    input_tensor = transform(image).unsqueeze(0)  
    
    with torch.no_grad():
        output = model(input_tensor)
        _, predicted = torch.max(output, 1)
        disease = CLASS_NAMES[predicted.item()]
    
    st.image(image, use_column_width=True)
    st.write(f"Predicted class is :  {disease}")