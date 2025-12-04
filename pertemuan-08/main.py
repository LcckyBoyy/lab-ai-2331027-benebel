import cv2
from ultralytics import YOLO
import time

model = YOLO("yolo12n.pt")

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Username atau password RTSP salah")
    exit()

prev_time = time.time()

while True:
    success, frame = cap.read()

    if not success or frame is None:
        print("Gagal membaca frame. coba lagi...")
        cap.release()
        time.sleep(1)
        cap = cv2.VideoCapture(0)
        continue

    # Hitung FPS
    current_time = time.time()
    # fps = 1 / (current_time - prev_time)
    fps = 60
    prev_time = current_time

    # YOLO inference
    results = model(frame)
    
    annotated_frame = frame.copy()  # Copy frame asli

    # Filter dan gambar hanya botol
    for result in results:
        for box in result.boxes:
            if result.names[int(box.cls)] == "bottle":  # Filter botol saja
                print(f"Botol terdeteksi: {box.conf}")
                
                # Ambil koordinat kotak
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                confidence = box.conf[0]
                
                # Gambar kotak hijau
                cv2.rectangle(annotated_frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                
                # Tambah label dan confidence
                label = f"Bottle: {confidence:.2f}"
                cv2.putText(annotated_frame, label, (x1, y1 - 10),
                           cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

    # Tambahkan FPS ke video
    cv2.putText(annotated_frame, f"FPS: {int(fps)}", (10, 60),
                cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 255, 0), 3)

    # Tampilkan hasil
    # cv2.imshow("YOLO RTSP CCTV Inference", annotated_frame)
    cv2.imshow("YOLO Bottle Detection", annotated_frame)

    # Tekan 'q' untuk keluar
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()