$(document).ready(function () {
    add();
});
function add() {
    $.ajax({
        type: "GET",
        url: "/review",
        data: {},
        success: function (response) {
            let rows = response['reviews']
            for (let i = 0; i < rows.length; i++) {
                let rank = rows[i]['rank']
                let comment = rows[i]['comment']
                let star = rows[i]['star']
                let id = rows[i]['id']

                let star_image = '⭐'.repeat(star)

                let temp_html = ``

                if ("{{rank}}" == rank) {
                    temp_html = `<li class="review-doc">
                                    <span class="review-text" id="review-id">
                                        ${id}
                                    </span>
                                    <span class="review-text" id="review-comment">
                                        ${comment}
                                    </span>
                                    <span class="review-text" id="review-star">
                                        ${star_image}
                                    </span>
                                </li>`
                } else {
                    temp_html = ``
                }
                $('#review-box').append(temp_html)
            }
        }
    });
}

function submit() {
    let comment = $('#comment').val()
    let star = $("input[name='rating']:checked").val()
    let rank = "{{rank}}"

    $.ajax({
        type: "POST",
        url: "/review",

        data: {comment_give: comment, star_give: star, rank_give: rank},
        success: function (response) {

            if (response.result == 'fail') {
                alert(response['msg']);
                location.href = '/loginForm';
            } else {
                alert('리뷰를 등록하였습니다.');
                location.reload();
            }
        }
    })
}

function get() {
    let cover = "{{cover}}"
    let singer = "{{singer}}"
    let album = "{{album}}"
    let title = "{{title}}"

    $.ajax({
        type: "POST",
        url: "/detail",
        data: {cover_give: cover, title_give: title, singer_give: singer, album_give: album,},
        success: function (response) {
             if (response.result == 'fail') {
                alert(response['msg']);
                location.href = '/loginForm';
            } else {
                alert('담기에 성공하셨습니다.');
                location.reload();
            }
        }
    })
}

function remove(rank) {
    alert(rank)
    $.ajax({
        type: "POST",
        url: "/remove",
        data: {},
        success: function (response) {
            alert('담기 취소하였습니다.')
        }
    })
}

function remove() {
    let cover = "{{cover}}"
    let singer = "{{singer}}"
    let album = "{{album}}"
    let title = "{{title}}"

    $.ajax({
        type: "POST",
        url: "/detail",
        data: {cover_give: cover, title_give: title, singer_give: singer, album_give: album},
        success: function (response) {
             if (response.result == 'fail') {
                alert(response['msg']);
                location.href = '/loginForm';
            } else {
                alert('취소에 성공하셨습니다.');
                location.reload();
            }
        }
    })
}
