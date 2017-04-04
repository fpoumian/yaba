/**
 * Class representing a scrobbled LastFM track.
 */
export default class LastFmScrobbledTrack {

  /**
   * Parses the raw track data of a Last.FM API response object and constructs a cleaner object.
   * @param {object} rawTrackData - The raw track data of a Last.FM API response object.
   */
  constructor(rawTrackData) {
    this._name = rawTrackData.name;
    this._artist = rawTrackData.artist['#text'];
    this._album = rawTrackData.album['#text'];
    this._date = rawTrackData.date['#text'];
  }
}
