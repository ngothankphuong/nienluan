$('#on-btn').click(function () {
    on_mess = $('#on-btn').val()
    $.ajax({
        url: '/on_cam',
        type: 'POST',
        contentType: 'text/plain',
        data: on_mess,
        success: function (res) {
            window.location.reload()
        }
    })
})