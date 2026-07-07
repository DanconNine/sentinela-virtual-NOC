import cv2
import numpy as np
import pyautogui
import time

def monitoring_real_time(path_erro, threshold=0.6):
    print("Sentinela Iniciado... Monitorando sua tela a cada 2 segundos.")
    print("Pressione Ctrl + C no terminal para parar.")

    #Carrega o gabarito do erro e converte para cinza
    img_erro = cv2.imread(path_erro)
    template_gray = cv2.cvtColor(img_erro, cv2.COLOR_BGR2GRAY)
    w, h = template_gray.shape[::-1]

    try:
        while True:
            # 1. Tira um print da tela inteira em tempo real
            screenshot = pyautogui.screenshot()

            # 2. Converte a imagem do pyAutoGUI (PIL) para o formato OpenCV (numpy array BGR)
            tela_rgb = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
            tela_gray = cv2.cvtColor(tela_rgb, cv2.COLOR_BGR2GRAY)

            # 3. Procura o erro na tela
            res = cv2.matchTemplate(tela_gray, template_gray, cv2.TM_CCOEFF_NORMED)
            loc = np.where(res >= threshold)

            # Verifica se encontrou alguma coordenada
            pontos = list(zip(*loc[::-1]))

            if len(pontos) > 0:
                # Pegamos o primeiro ponto encontrado
                pt = pontos[0]
                print(f"FALHA VISUAL DETECTADA! Coordenadas na tela: X={pt[0]}, Y={pt[1]}")

                # Desenha na tela onde encontrou o erro
                cv2.rectangle(tela_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 3)
                cv2.imshow("Alerta de Falha Encontrado", tela_rgb)
                cv2.waitKey(5000) # Mantém a janela aberta por 1s
                cv2.waitKey(5000) # Mantém a janela aberta 'por 1s
                cv2.destroyAllWindows()
            else:
                print("Tudo limpo... Monitorando...")
            
            # Aguarda 2s antes de checar a tela de novo (RPA precisa de esperas para processar)
            time.sleep(2)
    except KeyboardInterrupt:
        print("\n Monitoramento encerrado pelo usuário.")

# Executa o Monitor Vivo
# Garanta que 'gabarito_erro.png' seja um pedacinho do erro visível da tela monitorada
monitoring_real_time('gabarito_erro.png', threshold=0.6)
