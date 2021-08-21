// $(document).ready(function () {
//     $("#categoryUl").on("click", ".categoryDrop", function (event) {
//             const categoryName = $('#categoryDrop').val()
//             const data = {
//                 requestType: 'getCategories'
//             }
//
//             $.ajax({
//                 type: "GET",
//                 enctype: 'multipart/form-data',
//                 url: '/post-delete/' + categoryName + '/',
//                 data: data,
//                 processData: false,
//                 contentType: false,
//                 cache: false,
//                 timeout: 600000,
//                 success: function (data) {
//                     // for (let food in data) {
//                     //     // Food is are doc in database
//                     //     if (data[food].name === orderSelect) {
//                     //         $('#orderPrice').html(data[food].price * Number($('#count').val()))
//                     //         console.log(food)
//                     //     }
//                     // }
//                     console.log(categoryName)
//                     console.log("SUCCESS :", data);
//                 },
//                 error: function (e) {
//                     console.log("ERROR : ", e);
//                 }
//             });
//
//         }
//     );
// });
