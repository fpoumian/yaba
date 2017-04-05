/**
 * Class representing a scrobbled LastFM track.
 */
export default class LastFmScrobbledTrack {

  /**
   * Parses the raw track data of a Last.FM API response object and constructs a cleaner object.
   * @param {object} rawTrackData - The raw track data of a Last.FM API response object.
   */
  constructor(rawTrackData) {
    console.log(rawTrackData);
    this._name = rawTrackData.name;
    this._artist = rawTrackData.artist['#text'];
    this._album = rawTrackData.album['#text'];
    // If track data is missing date property, that means the track is being scrobbled right now
    this._date = rawTrackData.date ? rawTrackData.date['#text'] : 'Now playing...';
  }
}
