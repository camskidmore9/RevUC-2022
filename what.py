import json
import spotipy
import webbrowser

username = '22dg2esbxodtefayaknufmbkq'
clientID = '46677d4b3b424080a06193e810ca8bbb'
clientSecret = '86f67381ef8c440a888d84ccbf7f4076'
redirectURI = 'http://localhost:3000' 

# Create OAuth Object
oauth_object = spotipy.SpotifyOAuth(clientID,clientSecret,redirectURI)

# Create token
token_dict = oauth_object.get_access_token()
token = token_dict['access_token']

# Create Spotify Object
spotifyObject = spotipy.Spotify(auth=token)

user = spotifyObject.current_user()
# To print the response in readable format.
#print(json.dumps(user,sort_keys=True, indent=4))

while True:
    print("Welcome, "+ user['display_name'])
    print("0 - Exit")
    print("1 - Search for a Song")
    choice = int(input("Your Choice: "))
    if choice == 1:
        # Get the Song Name.
        searchQuery = input("Enter Song Name: ")
        # Search for the Song.
        searchResults = spotifyObject.search(searchQuery,1,0,"track")
        # Get required data from JSON response.
        tracks_dict = searchResults['tracks']
        tracks_items = tracks_dict['items']
        song = tracks_items[0]['external_urls']['spotify']
        print(song)
        # Open the Song in Web Browser
        spotifyObject.add_to_queue(song)
        webbrowser.open(song)
        print('Song has opened in your browser.')
    elif choice == 0:
        break
    else:
        print("Enter valid choice.")