def make_album(artiste_name, album_title, songs_num=None):
    album = {'artiste' : artiste_name.title(), 'album_title' : album_title.title()}
    
    if songs_num:
        album['songs'] = songs_num
    return album

"""
album_name = make_album('kk fosu', 'why me')
print(album_name)

album_name = make_album('liwin', 'benedicta')
print(album_name)

album_name = make_album('dada kd', 'im sorry')
print(album_name)

album_name = make_album('dada kd', 'im sorry', 12)
print(album_name)
"""

while True:
    print("\nEnter an album title and the artiste")
    print("type 'q' any time to quit")
    
    title_album = input("Enter the title of the ablum: ")
    if title_album == 'q':
        break
    
    artiste = input("Enter the name of the artiste: ")
    if artiste == 'q':
        break

    album_name = make_album(artiste, title_album)
    print(album_name)