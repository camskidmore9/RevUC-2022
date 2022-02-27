// JavaScript source code

function SPlay(SToken) {
    src = "https://sdk.scdn.co/spotify-player.js"
    window.onSpotifyWebPlaybackSDKReady = () => {
        const token = SToken;
        const player = new Spotify.Player({
            name: 'Spotify Bot',
            getOAuthToken: cb => { cb(token); },
            volume: 0.5
        });

        player.connect();

    }
}