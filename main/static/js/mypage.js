<!--    메인으로 돌아가는 기능    -->
function to_main(){
    window.location.href="/"
}

// 노래 상세페이지로 이동
function to_detail(){
    window.location.href="/detail?rank=${rank}&title=${title}&singer=${singer}&album=${album}&cover=${cover}";
}
