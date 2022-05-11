function logout() {
    $.removeCookie('mytoken', {path: '/'});
    alert('로그아웃되었습니다.');
    window.location.href = "/loginForm";
}