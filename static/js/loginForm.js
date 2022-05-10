function login() {
    $.ajax({
        type: "POST",
        url: "/user/login",
        data: {id_give: $('#userid').val(), pw_give: $('#userpw').val()},
        success: function (response) {
            if (response['result'] == 'success') {
                // 로그인이 정상적으로 되면, 토큰을 받아온다
                // 이 토큰을 mytoken이라는 키 값으로 쿠키에 저장한다.
                $.cookie('mytoken', response['token']);

                alert('로그인 완료!')
                window.location.href = '/'
            } else {
                // 로그인이 안되면 에러메시지를 띄웁니다.
                alert(response['msg'])
            }
        }
    })
}

// 아이디 중복 체크해주는 변수 false면 불가능, true면 가능
let isJoin = false;

function blockJoin() {
    console.log(isJoin);
    isJoin = false;
}

function idCheck() {
    $.ajax({
        type: 'POST',
        url: '/user/idChecker',
        data: {'id_give': $('#userid').val()},
        success: (response) => {
            isJoin = response.result
            alert(response.msg);
        }
    })
}

function buttonShow() {
    $('.id-checker').toggleClass('hidden');
    $('.real-join').toggleClass('hidden');
    $('.cancel').toggleClass('hidden');
    $('.fake-join').toggleClass('hidden');
    $('.login').toggleClass('hidden');
    $('#userid').val('');
    $('#userpw').val('');
}

function cancel() {
    $('.id-checker').toggleClass('hidden');
    $('.real-join').toggleClass('hidden');
    $('.cancel').toggleClass('hidden');
    $('.fake-join').toggleClass('hidden');
    $('.login').toggleClass('hidden');
}

// 정규식을 사용한 아이디 값 체크
// 영대소문자, 숫자를 사용하여 4~12글자만 입력가능하도록
function is_id(asValue) {
    let regExp = /^(?=.*[a-zA-Z])[-a-zA-Z0-9_.]{4,12}$/;
    return regExp.test(asValue);
}

// 정규식을 사용한 비밀번호 값 체크
// 영대소문자, 숫자, 특수문자를 사용하여 8~20글자만 입력가능하도록
function is_password(asValue) {
    let regExp = /^(?=.*\d)(?=.*[a-zA-Z])[0-9a-zA-Z!@#$%^&*]{8,20}$/;
    return regExp.test(asValue);
}

function join() {
    // 테스트할 때만 주석처리
    // if($('#userid').val() === '') {
    //     alert('아이디를 입력해주세요.');
    //     $('#userid').focus();
    //     return;
    // }
    //
    // if(!is_id($('#userid').val())) {
    //     alert('영문과 숫자만 입력가능합니다.(4~10 글자)');
    //     $('#userid').focus();
    //     return;
    // }
    //
    // if($('#userpw').val() === '') {
    //     alert('비밀번호를 입력해주세요.');
    //     $('#userpw').focus();
    //     return;
    // }
    //
    // if(!is_password($('#userpw').val())) {
    //     alert('영문과 숫자는 최소 1개 포함되어야 합니다.(8~20 글자)');
    //     $('#userid').focus();
    //     return;
    // }
    if (!isJoin) {
        alert('아이디 중복 체크해주세요');
        return;
    }
    $.ajax({
        type:'POST',
        url: 'user/register',
        data: {'id_give':$('#userid').val(), 'pw_give':$('#userpw').val()},
        success: (response) => {
            alert(response.msg);
            location.reload();
        }
    })
}
