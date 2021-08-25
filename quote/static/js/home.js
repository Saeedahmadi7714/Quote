function post_by_tag(id) {

    const data = {
        requestType: 'getPostByTag'
    }

    $.ajax({
        type: "GET",
        enctype: 'multipart/form-data',
        url: "/tag-posts/" + id,
        data: data,
        processData: false,
        contentType: false,
        cache: false,
        timeout: 600000,
        success: function(data) {
            // clear current posts
            $('#content').html("");

            // add posts by tag
            for (let post in data) {
                var title = data[post].title
                var title2 = title.charAt(0).toUpperCase() + title.slice(1);

                var content = `<div class="col-md-12 ">
                <div class="row g-0 border rounded overflow-hidden flex-md-row mb-4 shadow-sm h-md-250 position-relative ">
                    <div class="col p-4 d-flex flex-column position-static ">
                        <h3 class="mb-0 ">` + title2 + `</h3>
                        <div class="mb-1 text-muted ">` + data[post].pub_date + `</div>
                        <p class="card-text mb-auto ">` + data[post].content.substring(0, 300) + `</p>
                        <a href="/post/` + data[post]._id + `" class="stretched-link ">Continue
                                    reading</a>
                    </div>
                    <div class="col-auto d-none d-lg-block ">
                        <img src="static/images/posts_images/` + data[post].image + `" alt="post image" class="bd-placeholder-img">
            
                    </div>
                </div>
            </div>`

                $('#content').append(content);

            }
        },
        error: function(e) {
            console.log("ERROR : ", e);
        }
    });

};