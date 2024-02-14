from moviepy.editor import VideoFileClip
import math

def cortar_video_em_segmentos(arquivo_video, duracao_segmento=120):
    # Carrega o vídeo
    video = VideoFileClip(arquivo_video)
    duracao_total = int(video.duration)
    
    # Calcula o número de segmentos com base na duração do segmento
    numero_de_segmentos = math.ceil(duracao_total / duracao_segmento)
    
    for i in range(numero_de_segmentos):
        inicio = i * duracao_segmento
        fim = min((i + 1) * duracao_segmento, duracao_total)
        
        # Cria um subclip para cada segmento
        segmento = video.subclip(inicio, fim)
        
        # Define o nome do arquivo para o segmento
        nome_arquivo_segmento = f"{arquivo_video}_segmento_{i+1}.mp4"
        
        # Escreve o segmento para um arquivo
        segmento.write_videofile(nome_arquivo_segmento, codec="libx264", audio_codec="aac")
        
        print(f"Segmento salvo: {nome_arquivo_segmento}")

