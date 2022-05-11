$(document).ready(function () {
    add();
    image()
    listing();
});

function image() {
    $.ajax({
        type: "GET",
        url: "/detail",
        data: {},
        success: function (response) {
            let rows = response['musics']
            for (let i = 0; i < rows.length; i++) {
                let cover = rows[i]['cover']


                let temp_html = `
                                    <div class="somg-image">
                                        <img src="${cover}"
                                             style="margin-right: 30px;">
                                    </div>


                         `
                $('#music-info').append(temp_html)
            }
        }
    })
}

function listing() {
    $.ajax({
        type: "GET",
        url: "/detail",
        data: {},
        success: function (response) {
            let rows = response['musics']
            for (let i = 0; i < rows.length; i++) {
                let title = rows[i]['title']
                let singer = rows[i]['singer']
                let album = rows[i]['album']

                let temp_html = `
                                       <h2 class="title">${title}</h2>

                                <li class="list">
                                    <span class="attr">
                                        가수명
                                    </span>
                                    <span class="attr">
                                        ${singer}
                                    </span>
                                </li>
                                <li class="list">
                                    <span class="attr">
                                        앨범
                                    </span>
                                    <span class="attr">
                                        ${album}
                                    </span>
                                </li>

                         `

                $('#song-info').append(temp_html)
            }
        }
    })
}

function add() {
    $.ajax({
        type: "GET",
        url: "/review",
        data: {},
        success: function (response) {
            let rows = response['reviews']
            for (let i = 0; i < rows.length; i++) {
                let comment = rows[i]['comment']
                let star = rows[i]['star']
                let id = rows[i]['id']

                let temp_html = `<li class="review-doc">
                                    <span class="review-text" id="review-id">
                                        ${id}
                                    </span>
                                    <span class="review-text" id="review-comment">
                                        ${comment}
                                    </span>
                                    <span class="review-text" id="review-star">
                                        ${star}
                                    </span>
                                    <span class="review-text" id="review-time">
                                        작성시간
                                    </span>
                                </li>`
                $('#review-box').append(temp_html)
            }

        }
    });
}
function submit() {
    let comment = $('#comment').val()
    let star = $("input[name='rating']:checked").val()

    $.ajax({
        type: "POST",
        url: "/review",
        data: {comment_give: comment, star_give: star},
        success: function (response) {
            if(response.result == 'fail') {
                alert(response['msg']);
                location.href = '/loginForm';
            } else {
                alert('리뷰를 등록하였습니다.');
                location.reload();
            }
        }
    })
}