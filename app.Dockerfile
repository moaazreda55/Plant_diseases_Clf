FROM python:3.11

WORKDIR /app

COPY . .

RUN pip install torch torchvision streamlit Pillow


RUN python download_model.py

CMD [ "streamlit" ,"run","streamlit.py"]