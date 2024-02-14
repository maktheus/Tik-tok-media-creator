from Video.CutVideo import cortar_video_em_segmentos
from Video.DownloadVideo import download_video
# with this snippet from src/main.py:
def main():
    arquivo_video = download_video("https://www.youtube.com/watch?v=PkBokwRPfDI")
    cortar_video_em_segmentos(arquivo_video)


if __name__ == "__main__":
    main()