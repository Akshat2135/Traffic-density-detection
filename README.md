# Smart Traffic Density API

A simple API to detect traffic density from images using YOLOv8, designed to work as a backend microservice.

## Installation

1. Make sure you are in this directory:
   ```bash
   cd e:\dti\DataSets\TrafficDensityAPI
   ```
2. (Optional) Create a virtual environment:
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the API

Start the FastAPI server:
```bash
python main.py
```
Or via uvicorn directly:
```bash
uvicorn main:app --reload
```

## How to Test and Use quickly

The fastest way to test your API without writing any client code:
1. When the server is running, open your browser and go to:
   **http://127.0.0.1:8000/docs**
2. This opens the Swagger UI interface.
3. Click on the `POST /detect/density/` endpoint to expand it, then click **Try it out**.
4. You will see a file upload button. Choose an image of traffic and click **Execute**.
5. Scroll down to see the JSON Response!

```json
{
  "status": "success",
  "vehicle_count": 22,
  "density_level": "Medium"
}
```

## Training a Custom Model on your Data

By default, the API will use `yolov8n.pt` (the base pre-trained model) so you can test it immediately out-of-the-box. Check `inference.py`.

Since you have datasets at `e:\dti\DataSets\merged`:
1. You can run the prepared script: `python train.py`.
2. It will fine-tune the model on your dataset for 30 epochs.
3. Once done, locate `best.pt` inside the `runs` folder.
4. Modify `inference.py`, changing `MODEL_PATH = "yolov8n.pt"` to point to your new `best.pt`.
