#!/usr/bin/python3

import pyrealsense2 as rs
import numpy as np
import math
import cv2
from ultralytics import YOLO

# object classes
classNames = ["person", "bicycle", "car", "motorbike", "aeroplane", "bus", "train", "truck", "boat",
    "traffic light", "fire hydrant", "stop sign", "parking meter", "bench", "bird", "cat",
    "dog", "horse", "sheep", "cow", "elephant", "bear", "zebra", "giraffe", "backpack", "umbrella",
    "handbag", "tie", "suitcase", "frisbee", "skis", "snowboard", "sports ball", "kite", "baseball bat",
    "baseball glove", "skateboard", "surfboard", "tennis racket", "bottle", "wine glass", "cup",
    "fork", "knife", "spoon", "bowl", "banana", "apple", "sandwich", "orange", "broccoli",
    "carrot", "hot dog", "pizza", "donut", "cake", "chair", "sofa", "pottedplant", "bed",
    "diningtable", "toilet", "tvmonitor", "laptop", "mouse", "remote", "keyboard", "cell phone",
    "microwave", "oven", "toaster", "sink", "refrigerator", "book", "clock", "vase", "scissors",
    "teddy bear", "hair drier", "toothbrush"
]

# define yolo model
model = YOLO("yolov8n.pt")

# ストリームの設定
config = rs.config()
config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)
config.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 30)

# ストリーミング開始
pipeline = rs.pipeline()
pipeline.start(config)

# Alignオブジェクト生成
align_to = rs.stream.color
align = rs.align(align_to)

try:
    while True:
        # フレーム待ち
        frames = pipeline.wait_for_frames()

        # RGBとDepthの位置ずれを修正
        aligned_frames = align.process(frames)

        # RGB
        color_frame = aligned_frames.get_color_frame()
        color_image = np.asanyarray(color_frame.get_data())

        # 深度
        depth_frame = aligned_frames.get_depth_frame()
        depth_image = np.asanyarray(depth_frame.get_data())        

        # 2次元データをカラーマップに変換
        depth_colormap = cv2.applyColorMap(cv2.convertScaleAbs(depth_image, alpha=0.02), cv2.COLORMAP_JET)


        results = model(color_image)

        for r in results:
            boxes = r.boxes

            for box in boxes:
                cls = int(box.cls[0])
                if not (cls == 0):
                    continue

                # bounding box
                x1, y1, x2, y2 = box.xyxy[0]
                x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2) # convert to int values

                # put box in cam
                cv2.rectangle(color_image, (x1, y1), (x2, y2), (255, 0, 255), 3)

                # confidence
                confidence = math.ceil((box.conf[0]*100))/100

                # object details
                org = [x1, y1]
                px = int((x1 + x2) / 2)
                py = int((y1 + y2) / 2)
                font = cv2.FONT_HERSHEY_SIMPLEX
                fontScale = 1
                color = (255, 0, 0)
                thickness = 2

                cv2.putText(color_image, classNames[cls], org, font, fontScale, color, thickness)

                ### 画像処理 ###

                # ポイントで指定した箇所の奥行きを計算
                depth_data = depth_frame.get_distance(px, py)

                # ポイントにマーカーと距離を表示
                depth_str = str(round(depth_data, 2)) + "m"
                cv2.drawMarker(color_image, (px,py), (0,0,255))
                cv2.putText(color_image, depth_str, (px,py), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,0,255), thickness=2)
                cv2.drawMarker(depth_colormap, (px,py), (0,0,255))
                cv2.putText(depth_colormap, depth_str, (px,py), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,0,255), thickness=2)

                break
                ### 画像処理 end ### 

        # イメージの結合
        images = np.hstack((color_image, depth_colormap))

        # 表示
        cv2.namedWindow('RealSense', cv2.WINDOW_AUTOSIZE)
        cv2.imshow('RealSense', images)

        # q キー入力で終了
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break

finally:
    # ストリーミング停止
    pipeline.stop()

