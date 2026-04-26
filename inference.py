from ultralytics import YOLO
import cv2
import numpy as np

# Load a pretrained model. 
# Once you have trained a custom model using train.py, replace 'yolov8n.pt' with your custom model path (e.g., 'runs/detect/train/weights/best.pt')
MODEL_PATH = r"e:\dti\DataSets\yolov8n.pt" 
try:
    model = YOLO(MODEL_PATH)
except Exception as e:
    print(f"Error loading YOLO model: {e}")
    model = None

# COCO dataset class indices for vehicles
# 2: car, 3: motorcycle, 5: bus, 7: truck
VEHICLE_CLASSES = [2, 3, 5, 7]

def detect_traffic_density(image_bytes):
    if model is None:
        return {"error": "Model failed to load."}
    
    # Convert bytes to numpy array then to OpenCV format
    nparr = np.frombuffer(image_bytes, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    
    if img is None:
        return {"error": "Invalid image provided."}

    # Run inference
    # Since the custom model is entirely comprised of vehicle classes (bike, car, emv, etc.) 
    # we can remove the explicit COCO class filter.
    results = model.predict(img, imgsz=640, conf=0.25, verbose=False)
    
    # Count detections
    vehicle_count = 0
    if len(results) > 0:
        for box in results[0].boxes:
            cls_id = int(box.cls[0].item())
            if cls_id in VEHICLE_CLASSES:
                vehicle_count += 1
        
    # Determine basic density logic
    density_level = "Low"
    if vehicle_count >= 30:
        density_level = "High"
    elif vehicle_count >= 10:
        density_level = "Medium"
        
    return {
        "status": "success",
        "vehicle_count": vehicle_count,
        "density_level": density_level
    }
