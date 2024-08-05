import ctypes
import os
import sys
SPIF_SENDCHANGE = 0x2
SPI_SETDESKWALLPAPER = 0x0014
def ChangeWallpaperW(filename : str):
    User32 = ctypes.WinDLL("User32.dll")
    User32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, filename, SPIF_SENDCHANGE)

def Main():
    name_of_wallpaper = input("Please Write you're Filename for Change Wallpaper: ")
    ChangeWallpaperW(name_of_wallpaper)

if __name__ == "__main__":
    Main()