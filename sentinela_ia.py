import cv2
import mediapipe as mp
import numpy as np

from mediapipe.tasks import python
from mediapipe.tasks.python import vision

model_path = 'face_landmarker.task'

base_options = python.BaseOptions(model_asset_path=model_path)
options = vision.FaceLandmarkerOptions(
    base_options=base_options,
    output_face_blendshapes=False,
    output_facial_transformation_matrixes=False,
    num_faces=1
)

# 2. Incializa o detector de tarefas de visão
detector = vision.FaceLandmarker.create_from_options(options)

# 3. Liga a Webcam
webcam = cv2.VideoCapture(0)

print("Modelo carregado. Iniciando a WebCam......")
print("Pressione a tecla 'ESC' com a janela de vídeo selecionada para sair do vídeo.")

while webcam.isOpened():
    sucesso, frame = webcam.read()
    if not sucesso:
        print("Aguardando webcam...")
        continue

    # O OpenCV lê em BGR, mas o modelo FaceMesh precisa de RGB.
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    imagem_mediapipe = mp.Image(image_format=mp.ImageFormat.SRGB, data=frame_rgb)

    # Aqui é o ponto de inferência da do modelo (onde vai processar o rosto capturado)
    resultado = detector.detect(imagem_mediapipe)

    # 4. Nesse ponto, o rosto será desenhado com os pontos e conexões
    if resultado.face_landmarks:
        for face_landmarks in resultado.face_landmarks:
            # Desenha a malha geométrica completa do rosto
            h, w, _ = frame.shape
            for landmark in face_landmarks:
                cx, cy = int(landmark.x * w), int(landmark.y * h)

                cv2.circle(frame, (cx, cy), 1, (0, 255, 0), -1)
    
    cv2.imshow('Sentinela IA - API', frame)

    # Montando a saída em ESC
    if cv2.waitKey(5) & 0xFF == 27:
        break

# Limpa a memória e fecha as janelas
webcam.release()
cv2.destroyAllWindows()