from bs4 import BeautifulSoup
import requests
import json

agent = "Mozilla/5.0 (Windows NT 6.0; WOW64; rv:24.0) \
        Gecko/20100101 Firefox/24.0"
headers = {"User-Agent": agent}
source = "https://www.azlyrics.com/"


class SearchArtists:

    def __init__(self, query, result_count=20, max_result=False):
        """
        :param query: str
        :param result_count: int default 20, set 0 for max
        :param max_result: bool
        """
        self.query = query.lower()
        self.result_count = result_count
        self.max_result = max_result

    def get_names(self):
        try:
            if not self.query.isalpha():
                raise Exception("Input query string can only be alphabets from A-Z")

            if len(self.query) != 1:
                raise Exception("Input query string length should not be greater than 1")

            if self.result_count == 0:
                self.max_result = True

            url = source + self.query + ".html"
            req = requests.get(url, headers=headers)
            soup = BeautifulSoup(req.content, "html.parser")
            data = []

            for div in soup.find_all("div", {"class": "container main-page"}):
                links = div.findAll("a") if self.max_result else div.findAll("a")[:self.result_count]
                for item in links:
                    data.append(item.text.strip())
            return json.dumps(data)
        except Exception as e:
            raise Exception(f"Error Occurred: {e}")


class SearchSongsByArtists:

    def __init__(self, artist_name):
        """
        :param artist_name:
        """
        self.artist_name = artist_name.lower().replace(" ", "")

    def get_songs(self):
        try:
            first_char = self.artist_name[0]
            url = source + first_char + "/" + self.artist_name + ".html"
            req = requests.get(url, headers=headers)
            soup = BeautifulSoup(req.content, "html.parser")
            all_albums = soup.find("div", id="listAlbum")
            first_album = all_albums.find("div", class_="album")
            artist = {"artist": self.artist_name, "albums": []}
            all_items = str(first_album.find_next_siblings(["a", "div"])[0].parent.text).split("\n")
            album_data = {"album_name": "", "songs": []}

            for item in all_items:
                if item != "":
                    if item.startswith("album:"):
                        artist["albums"].append(album_data)
                        album_data = {"album_name": item, "songs": []}
                    else:
                        album_data["songs"].append(item)

            del artist["albums"][0]
            return json.dumps(artist)

        except Exception as e:
            raise Exception(f"Error Occurred: {e}")


class GetLyricsByArtistAndSong:

    def __init__(self, artist, song):
        """
        :param artist: str
        :param song: str
        """
        self.artist = artist.lower().replace(" ", "")
        self.song = song.lower().replace(" ", "")

    def get_lyrics(self):
        try:
            response = {"artist": self.artist, "song": self.song, "lyrics": ""}
            url = source + "lyrics/" + self.artist + "/" + self.song + ".html"
            req = requests.get(url, headers=headers)
            soup = BeautifulSoup(req.content, "html.parser")
            lyrics = soup.find_all("div", attrs={"class": None, "id": None})
            if not lyrics:
                return json.dumps({"Error": "Unable to find " + self.song + " by " + self.artist})
            elif lyrics:
                lyrics = [x.getText() for x in lyrics]
                response["lyrics"] = lyrics
            return json.dumps(response)

        except Exception as e:
            raise Exception(f"Error Occurred: {e}")
