var inputElement = document.getElementById('personal-info-input');
var pElement = document.getElementById('personal-info-p');

function replacePtoInput() {
    // var pElement_2 = document.getElementById('personal-info-p');
    // $("#hidden-div").wrap($("#personal-info-p"))
    pElement.replaceWith(inputElement);

}
function replaceInputtoP() {
    // var inputElement_2 = document.getElementById('personal-info-input');
    // var pElement = document.getElementById('personal-info-p');
    // $("#hidden-div").wrap($("#personal-info-p"))
    inputElement.replaceWith(pElement);

}
