// Active
$(document).ready(function () {
    $('#active-btn').on('click', function () {

        const postId = $('#postId').html()

        $.ajax({
            type: 'POST',
            url: '/api/post_deactivate/' + postId + '/',
            processData: false,
            contentType: false,
            cache: false,
            success: function () {
                if ($(`#${postId}`).status === true) {
                    $(`#${postId}`).status = false;
                } else {
                    $(`#${postId}`).status = true;
                }

                alert("Are you ready?");
            },
            error: function (e) {
                console.log("ERROR : ", e);
            }
        });
    });
});