import $ from 'jquery';
import LastFmScrobbledTrack from './LastFmTrack.js';

export default class LastFmAPI {

  /**
   * Constructs a new LastFmAPI object
   *
   * @param {string} key - The LastFM API key.
   * @param {string} username - The LastFM username.
   * @param {number} limit - The number of tracks to be displayed on the modal.
   */
  constructor(key, username, limit) {
    this._key = key;
    this._username = username;
    this._format = 'json';
    this._limit = limit;
    this._endpointBaseURL = 'http://ws.audioscrobbler.com/2.0/?method=user.getrecenttracks';
  }


  /**
   * @callback onFetchCompleteCallback
   */

  /**
   * @callback onFetchSuccessCallback
   * @param {object} rawData
   */

  /**
   * @callback onFetchErrorCallback
   * @param {object} error
   */

  /**
   * Fetch a user's recent tracks from Last.FM API
   *
   * @param {onFetchCompleteCallback} complete - The callback that handles the complete method.
   * @param {onFetchSuccessCallback} success - The callback that handles the success method.
   * @param {onFetchErrorCallback} error - The callback that handles the error method.
   */
  fetchUserRecentTracks(complete, success, error) {

    $.ajax({
      url: this._endpointBaseURL,
      type: "GET",
      async: true,
      dataType: "json",
      data: {
        user: this._username,
        api_key: this._key,
        format: this._format,
        limit: this._limit
      },
      accepts: {
        json: "application/json, text/javascript"
      },
      complete: complete,
      success: success,
      error: error
    });
  }


  /**
   * @callback onValidationErrorCallback
   * @param {object} errorMessage
   */

  /**
   * @callback onValidationSuccessCallback
   * @param {object} validData
   */

  /**
   *
   * @param {object} data - The LastFM response data we want to validate.
   * @param {onValidationErrorCallback} callback - Handles errors on response object.
   * @param {onValidationSuccessCallback} callback - What to do is data is succesfully validated.
   */
  static validateResponseData(data, onError, onSuccess) {
    if (data.error) {
      onError(data.message);
    } else {
      onSuccess(data);
    }
  }


  /**
   * @callback onFilteredCallback
   * @param {object} filteredData
   */

  /**
   *
   * @param {object} data - The LastFM response data we want to filter.
   * @param {onFilteredCallback} callback - The callback that handles what to do with the filtered data.
   */
  static filterResponseData(data, callback) {
    let filteredData = data.recenttracks.track.map((track) => {
      return new LastFmScrobbledTrack(track);
    })
    callback(filteredData);
  }
}