import cv2


def UnifyVideos(FirstVideo, SecondVideo):


    # Abre os vídeos
    cap1 = cv2.VideoCapture(FirstVideo)
    cap2 = cv2.VideoCapture(SecondVideo)

    # Pega as propriedades dos vídeos
    frame_width = int(cap1.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap1.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(cap1.get(cv2.CAP_PROP_FPS))
    total_frames = int(cap1.get(cv2.CAP_PROP_FRAME_COUNT))

    # Cria o objeto para escrever o vídeo de saída
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    output_video = cv2.VideoWriter('output_video.avi', fourcc, fps, (frame_width, frame_height * 2))  # Alterado o tamanho da altura

    # Loop para processar cada frame
    while True:
        ret1, frame1 = cap1.read()
        ret2, frame2 = cap2.read()

        # Se algum vídeo acabar, sai do loop
        if not ret1 or not ret2:
            break

        # Redimensiona o segundo frame para que tenha a mesma largura que o primeiro
        frame2_resized = cv2.resize(frame2, (frame_width, frame_height))

        # Empilha os frames verticalmente
        stacked_frame = cv2.vconcat([frame1, frame2_resized])

        # Escrever o frame empilhado no vídeo de saída
        output_video.write(stacked_frame)

        # Mostrar o frame na tela (opcional)
        cv2.imshow('Stacked Video', stacked_frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Libera os recursos
    cap1.release()
    cap2.release()
    output_video.release()
    cv2.destroyAllWindows()

    return 'output_video.avi'

UnifyVideos('video_files/the_strange_and_dark_cartoon_network_iceberg.mp3_segmento_1.mp4',
             'video_files/the_strange_and_dark_cartoon_network_iceberg.mp3_segmento_2.mp4')
