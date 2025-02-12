from pytubefix import YouTube

def download_youtube(url):
    youtube_download = YouTube(url, use_oauth=False, 
                               allow_oauth_cache=True)
    try:
        download = youtube_download.streams.get_highest_resolution()
        download.download(output_path="media/")
        print(f"Download do video: '{download.title}', realizado com sucesso")
    except Exception as error:
        print(f"Aconteceu um erro: {error}")

url_youtube = input("Informe a url: ")
download_youtube(url=url_youtube)