# the name of the file should be main otherwise got an error ImportError: cannot import name 'FASTAPI' from 'fastapi' 

from fastapi import FastAPI, File, UploadFile
from predictor import DepthEstimationModel
import os
import uuid

app = FastAPI()

depth_estimator = DepthEstimationModel()

ALLOWED_EXTENSIONS = {".JPG", ".jpeg", ".png"}
TEMP_FOLDER = "api_images"
os.makedirs(TEMP_FOLDER, exist_ok=True)


@app.post('/predict')  # API sorgusu atacak bir root
async def predict(file: UploadFile = File(...)):
    try:
        file_ext = os.path.splitext(file.filename)[1]  # extension'ı ayırır => e.g ".jpg" ".png"
        if file_ext not in ALLOWED_EXTENSIONS:
            return {"error": "Uploaded file must be in JPG, JPEG, PNG format."}
        
        filename_base = str(uuid.uuid4())  # random bir isim vericek isimlere
        filename = filename_base + file_ext

        destination_path = os.path.join(TEMP_FOLDER, filename)
        output_path = os.path.join(TEMP_FOLDER, "output_" + filename_base + ".png")  # image png olarak kaydedilir.

        # Save the uploaded file
        with open(destination_path, 'wb') as image_data:
            image_data.write(file.file.read())

        # Perform depth estimation
        depth_estimator.calculate_depthmap(destination_path, output_path)

        # Return to inform
        return {"Image has ben saved."}

    except Exception as e:
        return {"error": str(e)}
