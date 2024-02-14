import cv2
import os
import time

def crop_video(video_path):
    # Abre o vídeo
    cap = cv2.VideoCapture(video_path)

    # Pega as propriedades do vídeo
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    # Determina se o vídeo está no formato paisagem ou retrato
    is_landscape = width > height

    # Define as dimensões do corte
    if is_landscape:
        new_width = height
        new_height = height
        start_x = int((width - new_width) / 2)
        start_y = 0
    else:
        new_width = width
        new_height = width
        start_x = 0
        start_y = int((height - new_height) / 2)

    # Define o nome do arquivo para o vídeo cortado cropeed_video+timestamp
    nameFile =  'cropped_video' + str(int(time.time())) + '.avi'
    filep = 'video_files/' + nameFile

    # Cria o objeto para escrever o vídeo de saída
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    #salve dentro de video_files
    output_video = cv2.VideoWriter(filep, fourcc, 30, (new_width, new_height))

    # Loop para processar cada frame
    while True:
        ret, frame = cap.read()

        if not ret:
            break

        # Faz o corte no frame
        cropped_frame = frame[start_y:start_y + new_height, start_x:start_x + new_width]

        # Escreve o frame cortado no vídeo de saída
        output_video.write(cropped_frame)

    # Libera os recursos
    cap.release()
    output_video.release()
    cv2.destroyAllWindows()

    #retorne o caminho do vídeo cortado
    return filep


def cleanAllCroppedVideos():
    for file in os.listdir("video_files"):
        if file.startswith("cropped_video"):
            os.remove(f"video_files/{file}")




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

    # Libera os recursos
    cap1.release()
    cap2.release()
    output_video.release()
    cv2.destroyAllWindows()

    cleanAllCroppedVideos()

    return 'output_video.avi'

#UnifyVideos('video_files/the_strange_and_dark_cartoon_network_iceberg.mp3_segmento_1.mp4',
#            'video_files/the_strange_and_dark_cartoon_network_iceberg.mp3_segmento_2.mp4')
UnifyVideos(crop_video('video_files/the_strange_and_dark_cartoon_network_iceberg.mp3_segmento_1.mp4'),
            crop_video('video_files/the_strange_and_dark_cartoon_network_iceberg.mp3_segmento_2.mp4'))