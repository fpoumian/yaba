import LastFmTrack from './LastFmTrack.js';
import HtmlTable from './HtmlTable.js';
import $ from 'jquery';

/**
 * A class representing a HTML Table with Last.FM content
 */
export default class LastFmScrobblesTable extends HtmlTable {

  /**
   * Constructs a new HTML table using jQuery.
   * @param {object} parentDOMElement - The parent DOM element that we want to append this table to.
   */
  constructor(parentDOMElement) {
    super(parentDOMElement);
    this._columns = ['Song', 'Artist', 'Album', 'Date'];
    this._rowItemType = LastFmTrack;
  }

}
