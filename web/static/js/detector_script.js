const api = 'http://192.168.0.103:5000/detector/upload';
let leran_more_url = 'https://github.com/asadali27232/AFD-Detector_DIP-Project';

document.getElementById('btn-more').addEventListener('click', function () {
    window.open(leran_more_url, '_blank');
});

// Function to handle the image upload
function uploadImage(event) {
    // Create a file input element
    const input = document.createElement('input');
    input.type = 'file';
    input.accept = 'image/*'; // Accept all image types

    // Handle file selection
    input.onchange = (e) => {
        const file = e.target.files[0];
        if (!file) return;

        // Set the image as the background of the div
        const reader = new FileReader();
        reader.onload = function (readEvent) {
            document.getElementById(
                'upload-image'
            ).style.backgroundImage = `url(${readEvent.target.result})`;
        };
        reader.readAsDataURL(file);

        // Send the file to the server
        sendFileToServer(file);
    };

    // Trigger the file input dialog
    input.click();
}
let response;
// Function to send the file to the server
function sendFileToServer(file) {
    document.getElementById('d-title').innerHTML = 'Predicting Disease';
    document.getElementById('d-name').innerHTML = '';
    document.getElementById('d-desc').innerHTML = '';
    document.getElementsByClassName('loader')[0].style.display = 'block';
    document.getElementById('btn-more').style.display = 'none';

    const formData = new FormData();
    formData.append('file', file);

    fetch(api, {
        method: 'POST',
        body: formData,
    })
        .then((response) => response.json())
        .then((data) => {
            updateApp(data);
        })
        .catch((error) => {
            console.error('Error:', error);
        });
}

// Function to update the app
function updateApp(data) {
    document.getElementsByClassName('loader')[0].style.display = 'none';
    document.getElementById('d-name').innerHTML = data.name;
    document.getElementById('d-desc').innerHTML = data.description;
    document.getElementById('d-title').innerHTML = 'Predicted Disease';
    leran_more_url = data.url;
    document.getElementById('btn-more').style.display = 'block';
}
