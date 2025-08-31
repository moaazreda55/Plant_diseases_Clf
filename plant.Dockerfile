# if you don't have any img 

FROM python:3.11

WORKDIR /app

RUN pip install torch torchvision streamlit Pillow gdown

COPY . .

RUN python download_model.py

CMD ["streamlit", "run", "streamlit.py"]
