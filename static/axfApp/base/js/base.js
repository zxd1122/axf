$(function () {
    document.documentElement.style.fontSize = innerWidth / 10 + "px";

    //     http://127.0.0.1:8000/axf/mine/
    urlStr = location.href;
    idStr = urlStr.split("/")[4];
    $span = $(document.getElementById(idStr));
    $span.css("background", "url(/static/axfApp/base/img/"+idStr+"1.png)");
    $span.css("background-size", "30px");
});