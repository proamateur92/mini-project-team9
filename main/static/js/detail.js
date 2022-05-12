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
                    temp_html = ` <li class="review-doc">
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
            if ($.trim($('#comment').val())=='') {
                alert("리뷰를 입력해주세요");
                $("#comment").focus();
                return;
            }
            if ($.trim($("input[name='rating']:checked").val())=='') {
                alert("별점을 입력해주세요");
                $("#comment").focus();
                return;
            } else {
                alert('리뷰를 등록하였습니다.');
                location.reload();
            }
        }
    })
}

