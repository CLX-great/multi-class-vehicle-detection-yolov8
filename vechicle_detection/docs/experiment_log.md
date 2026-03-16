# Experiment Log

## Baseline v1
- Model: YOLOv8n
- Epochs: 20
- Image size: 640
- Batch size: 8

## Results
- Precision: 0.551
- Recall: 0.478
- mAP50: 0.492
- mAP50-95: 0.311

## Per-class Results
- Bus: mAP50 = 0.233
- Car: mAP50 = 0.777
- Motorcycle: mAP50 = 0.579
- Pickup: mAP50 = 0.455
- Truck: mAP50 = 0.415

## Notes
- Car achieved the best performance, likely due to larger sample size.
- Bus and Truck were less stable because of limited validation instances.
- Motorcycle showed high precision but relatively lower recall.

## Baseline v2
- Model: YOLOv8n
- Epochs: 50
- Image size: 640
- Batch size: 8

## Results
- Precision: 0.795
- Recall: 0.563
- mAP50: 0.655
- mAP50-95: 0.419

## Notes
- Increasing training epochs from 20 to 50 significantly improved overall detection performance.
- Car remained the strongest class.
- Bus and Truck were still less stable due to limited validation instances.
- Pickup and Motorcycle showed clear gains compared with the 20-epoch baseline.

## Baseline v3
- Model: YOLOv8n
- Data setting: Grayscale-augmented
- Epochs: 50
- Image size: 640
- Batch size: 8

## Results
- Precision: 0.766
- Recall: 0.662
- mAP50: 0.729
- mAP50-95: 0.491

## Notes
- Grayscale augmentation improved overall recall and both mAP metrics compared with the RGB 50-epoch setting.
- Bus and Truck showed particularly strong gains, though their validation sizes remained limited.
- Motorcycle benefited less consistently than the other classes.