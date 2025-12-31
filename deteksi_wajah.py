import cv2
import mediapipe as mp
import numpy as np
import time
from playsound import playsound # <-- LIBRARY BARU UNTUK MP3
import os 

# --- INISIALISASI MEDIA PIPE ---
mp_face_mesh = mp.solutions.face_mesh
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

# --- KONFIGURASI UMUM ---
WIDTH, HEIGHT = 1280, 720 # RESOLUSI KAMERA
OVAL_CENTER = (WIDTH // 2, HEIGHT // 2) 
OVAL_THICKNESS = 4
TOLERANCE_PX = 40 

# --- KONFIGURASI OVAL PERMANEN ---
OVAL_AXES = (150, 200) 

# --- KONFIGURASI KOTAK INTERAKSI (5 Kotak & Path Suara LOKAL) ---
BOX_SIZE = 100

# !!! ⚠️ NAMA FILE DARI FOLDER CAM PY: do.mp3, re.mp3, dst. !!!
AUDIO_FILENAMES = [
    "do.mp3",  # Menggunakan format .mp3 dari folder lo
    "re.mp3",
    "mi.mp3",
    "fa.mp3",
    "sol.mp3",
]

BOXES_DATA = [
    {"center": (100, 100), "color": (0, 0, 255), "name": "MERAH (DO)", "sound_path": AUDIO_FILENAMES[0]},      
    {"center": (WIDTH - 100, 100), "color": (0, 255, 0), "name": "HIJAU (RE)", "sound_path": AUDIO_FILENAMES[1]}, 
    {"center": (100, HEIGHT - 100), "color": (255, 0, 0), "name": "BIRU (MI)", "sound_path": AUDIO_FILENAMES[2]},  
    {"center": (WIDTH - 100, HEIGHT - 100), "color": (0, 255, 255), "name": "KUNING (FA)", "sound_path": AUDIO_FILENAMES[3]}, 
    {"center": (WIDTH // 2, HEIGHT // 2), "color": (255, 0, 255), "name": "UNGU (SOL)", "sound_path": AUDIO_FILENAMES[4]}, 
]
TIP_INDEX = 8 

# --- VARIABEL STATE ---
face_validated = False 
last_played_box = None 
# Dengan playsound, kita tidak perlu memuat file ke memori (loaded_audio)

# ----------------------------------------------------------------
## PRAPROSES: Cek keberadaan file sebelum memulai kamera
# ----------------------------------------------------------------
for box in BOXES_DATA:
    if not os.path.exists(box['sound_path']):
        print(f"ERROR: File '{box['sound_path']}' tidak ditemukan. Suara untuk {box['name']} dinonaktifkan.")
        box['sound_path'] = None 
    else:
        print(f"Sukses menemukan {box['sound_path']}.")

print("Inisialisasi audio selesai. Memulai kamera...")
# ----------------------------------------------------------------


# Buka Kamera (Set resolusi frame)
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, WIDTH)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, HEIGHT)

# Inisialisasi Detektor
with mp_face_mesh.FaceMesh(max_num_faces=3, min_detection_confidence=0.5, min_tracking_confidence=0.5) as face_mesh, \
     mp_hands.Hands(max_num_hands=6, min_detection_confidence=0.7, min_tracking_confidence=0.7) as hands:

    while cap.isOpened():
        success, image = cap.read()
        if not success:
            continue
        
        image = cv2.flip(image, 1) 
        h, w, c = image.shape

        # --- PREPROCESSING ---
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image_rgb.flags.writeable = False
        face_results = face_mesh.process(image_rgb)
        hand_results = hands.process(image_rgb)
        image.flags.writeable = True

        OVAL_COLOR = (0, 0, 255) 
        ALERT_TEXT = "Posisikan Wajah Tepat di Tengah Oval"
        
        # --- 1. VALIDASI WAJAH (OVAL LOGIC) ---
        if face_results.multi_face_landmarks:
            nose_tip = face_results.multi_face_landmarks[0].landmark[4]
            face_center_x = int(nose_tip.x * w)
            face_center_y = int(nose_tip.y * h)
            
            dx = OVAL_CENTER[0] - face_center_x
            dy = OVAL_CENTER[1] - face_center_y
            distance_sq = dx**2 + dy**2
            
            if distance_sq < TOLERANCE_PX**2:
                OVAL_COLOR = (0, 255, 0) # Hijau
                ALERT_TEXT = "Wajah Tepat, OK!"
                face_validated = True
            else:
                OVAL_COLOR = (0, 0, 255) # Merah
                face_validated = False
        else:
            face_validated = False

        # Gambar Oval & Text
        cv2.ellipse(image, OVAL_CENTER, OVAL_AXES, 0, 0, 360, OVAL_COLOR, OVAL_THICKNESS)
        cv2.putText(image, ALERT_TEXT, (OVAL_CENTER[0] - 250, HEIGHT - 30), 
                    cv2.FONT_HERSHEY_SIMPLEX, 1, OVAL_COLOR, 2, cv2.LINE_AA)
        
        # --- 2. INTERAKSI TANGAN & SUARA ---
        current_hovered_box = None

        if hand_results.multi_hand_landmarks:
            for hand_landmarks in hand_results.multi_hand_landmarks:
                
                # Visualisasi Landmark Tangan
                mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS, 
                                          mp_drawing.DrawingSpec(color=(0, 255, 0), thickness=2, circle_radius=2),
                                          mp_drawing.DrawingSpec(color=(255, 255, 255), thickness=2, circle_radius=2))
                
                # Dapatkan koordinat ujung jari telunjuk (Index 8)
                tip_landmark = hand_landmarks.landmark[TIP_INDEX]
                finger_x = int(tip_landmark.x * w)
                finger_y = int(tip_landmark.y * h)
                cv2.circle(image, (finger_x, finger_y), 10, (255, 255, 0), -1)

                # Cek Interaksi dengan Kotak
                for idx, box in enumerate(BOXES_DATA):
                    cx, cy = box['center']
                    
                    is_hovering = cx - BOX_SIZE//2 < finger_x < cx + BOX_SIZE//2 and \
                                  cy - BOX_SIZE//2 < finger_y < cy + BOX_SIZE//2

                    if is_hovering:
                        current_hovered_box = idx 
                        
                        # Kotak yang dipilih: Visual Feedback
                        border_color = (255, 255, 255)
                        scale = 1.1 
                        cv2.putText(image, f"Memilih: {box['name']}", (WIDTH//2 - 150, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, border_color, 2, cv2.LINE_AA)
                    else:
                        border_color = (100, 100, 100)
                        scale = 1.0

                    # Gambar Kotak Interaksi
                    w_scaled = int(BOX_SIZE * scale)
                    h_scaled = int(BOX_SIZE * scale)
                    cv2.rectangle(image, (cx - w_scaled//2, cy - h_scaled//2), 
                                  (cx + w_scaled//2, cy + h_scaled//2), 
                                  box['color'], -1) 
                    cv2.rectangle(image, (cx - w_scaled//2, cy - h_scaled//2), 
                                  (cx + w_scaled//2, cy + h_scaled//2), 
                                  border_color, 3) 

        # --- LOGIKA MEMUTAR SUARA ---
        if current_hovered_box is not None and current_hovered_box != last_played_box:
            # Mainkan suara jika kotak baru terdeteksi
            box_data = BOXES_DATA[current_hovered_box]
            if box_data['sound_path'] is not None:
                # playsound(..., block=False) memutar MP3 tanpa memblokir thread utama
                try:
                    playsound(box_data['sound_path'], block=False)
                    last_played_box = current_hovered_box
                except Exception as e:
                    print(f"Gagal memutar {box_data['name']} menggunakan playsound: {e}")
                    last_played_box = current_hovered_box # Mencegah spam error
            else:
                 last_played_box = current_hovered_box 
        
        elif current_hovered_box is None:
            last_played_box = None

        # --- Tampilkan Frame ---
        cv2.imshow('Face Alignment & Hand Interaction System', image)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# Bersihkan dan tutup semua window
cap.release()
cv2.destroyAllWindows()
