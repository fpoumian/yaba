export const appendError = function ($field, errorMessage) {

    // check if the field is not displaying an error already
    if ($field.parent('.form-group').find('.alert').length) {
        // return;
    }

    const $error = $('<div class="alert alert-danger"></div>');
    // add error message to markup and append it to field
    $error.text(`Error: ${errorMessage}`);
    $field.parent('.form-group').append($error);

}

export const removeError = function ($field) {
    // check if the field is not displaying an error already
    if ($field.parent('.form-group').find('.alert').length) {
        $field.parent('.form-group').find('.alert').remove();
    }
}