import pygame
import os

class MusicController:
    def __init__(self):
        pygame.mixer.init()

        # Gunakan path absolut
        base_path = os.path.abspath(os.path.dirname(__file__))
        self.playlists = {
            'playlist1': [
                os.path.join(base_path, 'music/playlist1/song1.mp3'),
                os.path.join(base_path, 'music/playlist1/song2.mp3')
            ],
            'playlist2': [
                os.path.join(base_path, 'music/playlist2/song1.mp3'),
                os.path.join(base_path, 'music/playlist2/song2.mp3')
            ]
        }

    def play_playlist(self, playlist_name):
        if playlist_name in self.playlists:
            playlist = self.playlists[playlist_name]
            if playlist:
                song_path = playlist[0]  # Memutar lagu pertama dari playlist
                if os.path.exists(song_path):
                    pygame.mixer.music.load(song_path)
                    pygame.mixer.music.play()
                else:
                    print(f"Lagu {song_path} tidak ditemukan.")
            else:
                print("Playlist kosong.")
        else:
            print("Playlist tidak ditemukan.")

    def stop_music(self):
        pygame.mixer.music.stop()
