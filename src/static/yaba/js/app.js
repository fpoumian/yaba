import $ from 'jquery';
import LastFmAPI from './modules/LastFmAPI.js';
import Modal from './modules/Modal.js';

$('document').ready(function () {


    /**
     * Last.FM Modal
     */

    const modal = new Modal($('.js-modal'), $('#modal'));

    // Last.FM API
    const lastFmAPIKey = lastFmConfig.getApiKey() || null;
    const username = lastFmConfig.getUsername() || null;
    const limit = lastFmConfig.getLimit() || 10;
    const lastFmAPI = new LastFmAPI(lastFmAPIKey, username, limit);

    // Modal event handlers
    modal.toggle.on('click', function () {
        modal.contentType = $(this).data('modal-content');
        modal.open();
    });

    modal.target
        .on('shown.bs.modal', () => {

            if (modal.state === 'loaded') {
                return;
            }

            lastFmAPI.fetchUserRecentTracks(
                // complete callback
                () => {
                    modal.loading = false;
                },

                // success callback
                (rawData) => {
                    LastFmAPI.validateResponseData(rawData,

                        // onError
                        (error) => {
                            modal.bodySelector.append(`<span>${error}</span>`);
                        },

                        //onSuccess
                        (validRawData) => {
                            LastFmAPI.filterResponseData(validRawData, (filteredData) => {
                                modal.content.data = filteredData;
                                modal.content.append(() => {
                                    modal.state = 'loaded';
                                });
                            })
                        })
                },

                // error callback
                (error) => {
                    let errorMessage = error.responseJSON.message || 'There was an unspecified error while making this request.'
                    modal.bodySelector.append(`<span>${errorMessage}</span>`);
                });

        });
});
