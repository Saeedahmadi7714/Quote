$(document).ready(function () {
    $('#delete-btn').on('click', function () {

        const postId = $('#postId').html()
        console.log(postId);
        $.ajax({
            type: 'POST',
            url: '/api/post-delete/' + postId + '/',
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