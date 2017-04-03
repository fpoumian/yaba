import modal from 'bootstrap';
import LastFmScrobblesTable from './LastFmScrobblesTable.js';
import $ from 'jquery';

export default class Modal {

  constructor(toggle, target) {
    this.toggle = toggle;
    this.target = target;
    this._contentType = '';
    this._content = null;
    this._loading = true;
    this._loadingMessage = this.target.find('.loading-message');
    this._bodySelector = $('.modal-body');
    this._state = this._bodySelector.attr('data-state') || 'empty';
  }

  set contentType(value) {
    if (value == 'scrobbles') {
      this._content = new LastFmScrobblesTable(this._bodySelector);
    }
    this._contentType = value;
  }

  get content() {
    return this._content;
  }

  set state(value) {
    this._state = value;
    this._bodySelector.attr('data-state', value);
  }

  get state() {
    return this._bodySelector.attr('data-state');
  }

  set loading(value) {
    if (!value && this._loadingMessage.length) {
      this._loadingMessage.remove();
    }
    this._loading = value;
  }

  get bodySelector() {
    return this._bodySelector;
  }

  open() {
    this.target.modal('show', this.toggle);
  }

}
