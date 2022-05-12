$(document).ready(function () {
    $('#show_list').empty();
    show_list();
});

function show_list() {
    $.ajax({
        type: "GET",
        url: "/musiclist",
        data: {},
        success: function (response) {
            let rows = response['chart']
            for (let i = 0; i < rows.length; i++) {
                let rank = rows[i]['rank']
                let title = rows[i]['title']
                let singer = rows[i]['singer']
                let album = rows[i]['album']
                let cover = rows[i]['cover']
                let temp_html =
                    `
                            <tr onclick="location.href='/detail?rank=${rank}&title=${title}&singer=${singer}&album=${album}&cover=${cover}'" class="lists">
                            <th scope="row" >${rank}</th>
                            <td >${title}</td>
                            <td >${singer}</td>
                            <td ><img src="${cover}"></td>
                            <td >${album}</td>
                            <td><button  type="button"  class="btn btn-outline-success" >담기</button></td>

                     </tr>`
                    console.log(rows)

                $('#show_list').append(temp_html)

                function hey() {
                    $.ajax({
                        type: 'POST',
                        url: '/hey',
                        data: {'text': $('#no').val()},
                        success: response => {
                            if (response.result) {
                                alert(1);
                            } else {
                                alert(2);
                            }
                        }
                    })
                }

                // 로그인하기 창을 누르면 로그인,회원가입 창으로 이동하기위해 만든 함수
                function to_login() {
                    window.location.href = "/user/login"
                }

                function to_mypage() {
                    window.location.href = "/index";
                }
            }
        }
    })
}
