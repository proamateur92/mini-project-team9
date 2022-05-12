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
                    temp_html = ` 
                                    <div class="review-box">
                                    <div class="review-header">
                                    <p class = "span-grid"><span class="id-span">${id}</span> <span style="color: lightgray;">|</span> <span class="id-time">날짜</span> <span style="color: lightgray;">|</span> <span class="get-star">${star_image}</span></p>
                                    </div>
                                    <hr>
                                    <div class="review-footer">
                                        ${comment}
                                    </div>
                                    </div>`
                } else {
                    temp_html = ``
                }
                $('#review-box').append(temp_html)
            }
        }
    });
}

function submit() {
    if($('#comment').val().trim() == '') {
        alert('리뷰를 작성해주세요');
        $('#comment').focus();
        return
    }

    if(!$("input[name='rating']:checked").val()) {
        alert('별점을 입력해주세요');
        return
    }

    let comment = $('#comment').val();
    let star = $("input[name='rating']:checked").val();
    let rank = "{{rank}}"
    $.ajax({
        type: "POST",
        url: "/review",

        data: {comment_give: comment, star_give: star, rank_give: rank},
        success: function (response) {
            alert('리뷰를 등록하였습니다.');
            location.reload();
        }
    })
}

