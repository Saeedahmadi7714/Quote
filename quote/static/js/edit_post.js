$(document).ready(function () {
    $(".delete-btn").unbind().click(function () {
        const postId = $(this).attr("value")
        // console.log(postId);
        $.ajax({
            type: 'POST',
            url: '/api/post-delete/' + postId + '/',
            processData: false,
            contentType: false,
            cache: false,
            success: function () {
                $(`#${postId}`).remove()
                alert("Your post was successfully deleted");
                // console.log(postId)
            },
            error: function (e) {
                console.log("ERROR : ", e);
            }
        });
    });
});