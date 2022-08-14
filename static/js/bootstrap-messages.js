// First Version
setTimeout(() => {
    let alert_messages = document.querySelector('.alert')
    let alert = bootstrap.Alert.getInstance(alert_messages)
    alert.close()
}, 1000);


// Second Version
// window.addEventListener('DOMContentLoaded', event => {

//     setTimeout(() => {
//         var alertList = document.querySelectorAll('.alert')
//         alertList.forEach(function (alert) {
//             new bootstrap.Alert(alert)
//         });
//         alertList.close();
//     }, 1000);

// });