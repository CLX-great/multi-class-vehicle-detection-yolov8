from ultralytics import YOLO

# 1. load trained model
model = YOLO("runs/detect/runs/vehicle_grayscale_aug/weights/best.pt")

# 2. run inference on video
results = model.predict(
    source="videos/Sample_Video_HighQuality.mp4",
    save=True,
    imgsz=640,
    conf=0.25,
    project="outputs",
    name="video_demo",
    show=False
)

print("Video inference completed.")