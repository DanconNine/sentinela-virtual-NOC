# Sentinela Virtual - NOC (Monitoramento Inteligente com Visão Computacional)

Este projeto foi desenvolvido com foco em segurança operacional e automação de processos para ambientes de missão crítica, como Centrais de Atendimento e Núcleos de Operação de Rede (NOC). O sistema utiliza técnicas avançadas de Visão Computacional Clássica e Machine Learning Aplicado para monitorar tanto interfaces de sistemas quanto a atenção física do operador.

## Arquitetura do Projeto

O projeto foi dividido em duas abordagens estratégicas:

1. **Monitoramento de Interface (Visão Clássica):** Utiliza OpenCV para realizar *Template Matching*. O robô varre telas operacionais buscando por padrões de imagens de erros conhecidos (gabaritos), permitindo o disparo de alertas automáticos de falhas visuais em sistemas legados.
2. **Segurança Física e Atenção (Deep Learning):** Utiliza a API do **Google MediaPipe Tasks** ('face_landmarker') para mapear em tempo real 468 pontos faciais do operador através da webcam. O modelo demonstra altíssima resiliência a ruídos de imagem e baixa  luminosidade.

## Tecnologias Utilizadas

* **Python 3.12** (Ambiente virtualizado estável para produção)
* **OpenCV (cv2)** (Processamento de imagem e Visão Clássica)
* **MediaPipe Tasks** (Incorrência de modelos de Deep Learning em tempo real)
* **PyAutoGUI** (Automação de interface e controle de hardware)
* **Git** (Versionamento e gerenciamento de features)

