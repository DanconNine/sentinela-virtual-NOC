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

''' def detectar_erro_estatico(path_cenario, path_erro, threshold=0.8):
    # 1. Carrega as imagens
    # img_rgb: A tela cheia onde vai procurar
    # img_erro: O gabarito do erro que queremos encontar
    img_rgb = cv2.imread(path_cenario)
    img_erro = cv2.imread(path_erro)

    # Guarda as dimensões do ícone de erro para desenhar o retângulo depois
    w, h = img_erro.shape[:-1]

    # 2. Tranforma as imagens em escala de cinza, o Template Matching trabalha melhor dessa forma
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    template_gray = cv2.cvtColor(img_erro, cv2.COLOR_BGR2GRAY)

    # 3. Executando o Template Matching
    # Ele "arrasta" o template por toda a imagem e calcula a correlação
    res = cv2.matchTemplate(img_gray, template_gray, cv2.TM_CCOEFF_NORMED)

    # 4. Filtra os resultados baseados no Threshold (confiança)
    # Aqui procuramos onde a correlação é maior que 80% (0.8)
    loc = np.where(res >= threshold)

    # 5. Se encontrou correspondências, desenha um retângulo
    encontrou = False
    for pt in zip(*loc[::-1]): # Transpõe as coordenadas
        encontrou = True
        # Desenha um retângulo verde ao redor da falha detectada
        cv2.rectangle(img_rgb, pt, (pt[0] + h, pt[1] + w), (0, 255, 0), 2)
        print(f"⚠️ FALHA DETECTADA!!! Nas coordenadas: X={pt[0]}, Y={pt[1]}")
    
    if encontrou:
        # Mostra a imagem com o resultado
        cv2.imshow('sentinela Visual - Detecção de Falha', img_rgb)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print("✅ Sistema Operando Normalmente. Nenhuma falha visual detectada!")
    

# ===== Teste do Script =====

print("===== Teste 1: Cenário Limpo =====")
# Deve retornar que o sistema está normal
detectar_erro_estatico('image_1.png', 'image_2.png')

print("\n===== Teste 2: Cenário de Falha =====")
# Deve detectar o erro e abrir a janela com o retângulo verde
detectar_erro_estatico('image_2.png', 'image_1.png')''' 