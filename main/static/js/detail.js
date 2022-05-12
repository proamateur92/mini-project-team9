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
                let year = rows[i]['year']
                let month = rows[i]['month']
                let date = rows[i]['date']


                let star_image = '⭐'.repeat(star)

                let temp_html = ``

                if ("{{rank}}" == rank) {
                    temp_html = ` 
                                    <div class="review-box">
                                    <div class="review-header">
                                    <p class = "span-grid"><span class="id-span">${id}</span> <span style="color: lightgray;">|</span> <span class="id-time">${year}.${month}.${date}</span> <span style="color: lightgray;">|</span> <span class="get-star">${star_image}</span></p>
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