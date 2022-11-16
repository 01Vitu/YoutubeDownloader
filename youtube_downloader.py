import PySimpleGUI as sg
from pytube import YouTube

class TelaDownloader:
    def __init__(self):
        #layout
        layout=[
            [sg.Text("Cole a URL do video desejado:")],
            [sg.Input(key="link_do_video")],
            [sg.Checkbox("Download em HD", key="download_hd")],
            [sg.Checkbox("Download somente áudio", key="baixar_audio")],
            [sg.Button("Download")]
        ]

        #instanciando a janela
        janela=sg.Window("Youtube Dowloader").layout(layout)
        #salvando dados da tela
        self.button, self.values = janela.Read()

    def Download_Video(self):
        print("Baixando video...")
        print(self.values['link_do_video'])
        url=self.values['link_do_video']
        youtube=YouTube(url)
        print('Titulo do vídeo: ', youtube.title)

        res_youtube=youtube.streams.get_lowest_resolution()

        if self.values['baixar_audio']:
            res_youtube=youtube.streams.get_audio_only()
            print("Baixando audio")
        else:
            if self.values['download_hd']:
                res_youtube=youtube.streams.get_highest_resolution()
        res_youtube.download()

tela=TelaDownloader()
tela.Download_Video()   