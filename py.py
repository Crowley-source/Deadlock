from ultralytics import YOLO

# LOad a pretrained YOLOv8n model

model = YOLO('best.pt')

#run infernece on the source

results = model(source=0, show=True , conf = 0.3 , save=True ) 

