from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse
import uvicorn
from inference import detect_traffic_density

app = FastAPI(
    title="Smart Traffic Density API", 
    description="Minimal API to detect traffic density from images using YOLOv8."
)

@app.get("/", response_class=FileResponse)
def read_root():
    return FileResponse("index.html")

@app.post("/detect/density/")
async def analyze_density(image: UploadFile = File(...)):
    """
    Upload a traffic image to get the vehicle count and density status.
    """
    # Read the image bytes from the uploaded file
    image_bytes = await image.read()
    
    # Run our YOLOv8 density detection logic
    result = detect_traffic_density(image_bytes)
    
    # Handle possible inference errors
    if "error" in result:
        return {"status": "error", "message": result["error"]}
        
    return result

if __name__ == "__main__":
    # Start the server on port 8000
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
