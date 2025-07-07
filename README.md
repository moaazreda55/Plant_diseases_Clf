# Plant_diseases_Clf

docker build -f app.Dockerfile -t plant_img . if you have app_img from last session
docker build -f plant.Dockerfile -t plan2_img . if ou build from scratch
docker run -p 8501:8501 --name my_container plant_img   according to what you have built
docker run -p 8501:8501 --name my_container plan2_img   according to what you have built