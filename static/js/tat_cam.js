$("#off-btn").click(function () {
    off_mess = $('#off-btn').val()
    $.ajax({
        url: '/off_cam',
        type: 'POST',
        contentType: "text/plain",
        data: off_mess,
        success: function (response) {
            if (response == 'stop') {
                var cam = document.querySelector('#container')
                cam.innerHTML =
                    "<img id='camera_frame' class='border border-danger' src='' alt='Camera đã tắt' width='600' height='400'>"
            }
        }
    })
})