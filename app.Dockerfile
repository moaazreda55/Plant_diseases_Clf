# if you already have app_img from last session  or electropi_img
FROM app_img:latest

WORKDIR /app

RUN pip install torch torchvision 

COPY . .

RUN python download_model.py

CMD [ "streamlit" ,"run","streamlit.py"]