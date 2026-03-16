# Multi-Class Vehicle Detection Using YOLOv8

This project explores multi-class vehicle detection in traffic scenes using YOLOv8.

## Vehicle Categories
- Bus
- Car
- Motorcycle
- Pickup
- Truck

## Project Goals
- Build a baseline vehicle detector using YOLOv8
- Compare different training settings and model variants
- Analyze per-class detection performance
- Extend the project to video inference

## Dataset
The dataset is organized in YOLO format with:
- train
- valid
- test
- data.yaml

## Baseline Results (YOLOv8n, 20 epochs)

### Overall Performance
- Precision: 0.551
- Recall: 0.478
- mAP50: 0.492
- mAP50-95: 0.311

### Key Observations
- Car achieved the strongest detection performance.
- Bus and Truck were less stable, likely due to fewer validation samples.
- Motorcycle showed relatively high precision but lower recall.

### Training Curve
![Results](assets/v1_results.png)

### Confusion Matrix
![Confusion Matrix](assets/v1_confusion_matrix.png)

### Label Distribution
![Labels](assets/v1_labels.jpg)

### Prediction Example
![Prediction](assets/v1_prediction.jpg)

## Current Progress
- [x] Dataset prepared
- [x] YOLOv8n baseline trained for 20 epochs
- [ ] 50-epoch experiment
- [ ] Model comparison
- [ ] Grayscale vs RGB comparison
- [ ] Video inference demo