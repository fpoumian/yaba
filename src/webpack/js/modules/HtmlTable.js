import $ from 'jquery';

/**
 * Class representing an HTML table in the DOM.
 */
export default class HTMLTable {

  /**
   * Constructs a new HTML table using jQuery.
   * @param {object} parentDOMElement - The parent DOM element that we want to append this table to.
   */
  constructor(parentDOMElement) {
    this._parentDOMElement = parentDOMElement;
    this._topElement = $('<table>');
    this._topElement.addClass('table table-stripped');
    this._head = $('<thead>').append($('<tr>'));
    this._body = $('<tbody>');
    this._topElement.append(this._head);
    this._topElement.append(this._body);
    this._columns = [];
    this._data = null;
    this._rowItemType = Object;
  }

  set data(value) {
    this._data = value;
    this.setColumns();
    this.addRows();
  }

  /**
   * Set the columns for HTML table.
   */
  setColumns() {

    if (this._columns.constructor !== Array)
      throw TypeError('Not an array');

    this._columns.forEach((column) => {
      let $th = $('<th>');
      $th.html(column);
      this._head.find('tr').append($th);
    });
  }

  /**
   * Add rows to HTML table.
   */
  addRows() {
    if (this._data.constructor !== Array)
      throw TypeError('data property of table is not an array');

    this._data.forEach((item) => {

      if (item.constructor !== this._rowItemType)
        throw TypeError('invalid item type for table row');

      let $tr = $('<tr>');

      for (const prop in item) {
        let $td = $('<td>');
        $td.html(item[prop]);
        $tr.append($td);
      }

      this._body.append($tr);
    })
  }

  /**
   * Append table to the parent DOM element.
   * @param {onTableAppendedCallback} callback
   */
  append(callback) {
    this._parentDOMElement.append(this._topElement);
    callback();
  }
}
