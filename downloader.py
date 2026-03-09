import requests
from abc import ABC, abstractmethod


#Classes

class Downloader(ABC):

    @abstractmethod
    def __init__(self,url:str):
        pass

    @abstractmethod
    def baixar(self):
        pass


class DowloaderImagem(Downloader):
    
    def __init__(self, url):

        if not isinstance(url,str):
            raise ValueError(f"O valor do atributo tem que ser uma string!")
        
        if not "https" or "http" in url:
            self.url = "https://" + url
        
        self.url = url
    
    def baixar(self):
        
        resp = requests.get(self.url)

        with open("imagem_anime.jpg", "wb") as img:
            img.write(resp.content)


# Função Main

def main():
    
    url = "https://i.pinimg.com/736x/a4/8e/3d/a48e3de37547681f214525b19ed54e22.jpg"

    d = DowloaderImagem(url)
    d.baixar()


if __name__ == "__main__":
    main()