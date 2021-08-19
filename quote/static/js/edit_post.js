$(document).ready(function () {
    $('#delete-btn').on('click', function () {

        const postId = $('#postId').html()

        $.ajax({
            type: 'POST',
            url: '/post-delete/' + postId + '/',
            processData: false,
            contentType: false,
            cache: false,
            success: function () {
                const a = $(`#${postId}`).remove()
                alert("Your post successfully deleted.");

            },
            error: function (e) {
                console.log("ERROR : ", e);
            }
        });
    });
});

