from ultralytics import YOLO

model = YOLO("yolov8n.pt")

model.train(
    data="Vehicles_Detection.v8i.yolov8/data.yaml",
    epochs=50,
    imgsz=640,
    batch=8,
    project="runs/detect",
    name="vehicle_baseline_v2"
)