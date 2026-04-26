from ultralytics import YOLO

def train_custom_model():
    """
    Train a custom YOLOv8 model using your existing dataset.
    This uses transfer learning from the base 'yolov8n.pt' model.
    """
    print("Loading base YOLOv8 model...")
    model = YOLO("yolov8n.pt")
    
    print("Starting training process...")
    # Adjust `data` path to point exactly to your dataset's yaml file.
    # Adjust `epochs` based on how long you want to train.
    results = model.train(
        data=r"e:\dti\DataSets\merged\data.yaml", 
        epochs=30,      # Number of training epochs
        imgsz=640,      # Image size
        batch=16,       # Batch size
        project="runs", # Output directory for trained weights
        name="traffic_density_custom"
    )
    
    print("Training complete! The best model weights will be saved in runs/traffic_density_custom/weights/best.pt")
    print("You can copy best.pt and assign its path to MODEL_PATH in inference.py to use it.")

if __name__ == "__main__":
    # Because multiprocessing is used during training in Windows, 
    # it is standard practice to wrap the script execution in this block.
    train_custom_model()
