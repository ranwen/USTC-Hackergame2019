function post (data) {
　　let url = 'http://localhost:5000/sub3',
　　　　xhr = new XMLHttpRequest();

　　xhr.open('post', url);
　　xhr.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');
　　xhr.send(data);
　　xhr.onreadystatechange = function () {
　　　　if (xhr.readyState === 4 && ( xhr.status === 200 || xhr.status === 304 )){
　　　　　　console.log(xhr.responseText);
　　　　}
　　}
}


function solve(x) {
    document.getElementsByTagName("textarea")[0].value = x
    document.getElementById("calc").click()
    setTimeout(function () {
        sht = document.getElementById("result").children[0].innerText
        console.log(sht)
        post("res="+encodeURIComponent(sht))
    }, 100)
}

function gettask() {
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.onreadystatechange = function () {
        if (xmlHttp.readyState == 4 && xmlHttp.status == 200) {
            var data = xmlHttp.responseText;
            console.log(data)
            if(data!="0")
            {
                solve(data)
            }
        }

    }
    xmlHttp.open("GET", "http://localhost:5000/get3",
        true);
    xmlHttp.send();
}

setInterval("gettask()",200)