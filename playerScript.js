// JavaScript source code
src = "https://sdk.scdn.co/spotify-player.js"
window.onSpotifyWebPlaybackSDKReady = () => {
    const token = '[My access token]';
    const player = new Spotify.Player({
        name: 'Spotify Bot',
        getOAuthToken: cb => { cb(token); },
        volume: 0.5
    });

    player.connect();

}