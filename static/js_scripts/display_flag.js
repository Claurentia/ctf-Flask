
function do_something() {
    alert("flag{y0u_f0und_yet_an0th3er_fl4g}");
}
function login() {
    var user = document.getElementById('uname').value;
    var pass = document.getElementById('psw').value;
    if (user === 'admin' && pass === 'password'){
        window.location.href = '/task4/loginsuccess';
    }
    else if (user !== 'admin'){
        document.getElementById('error').innerHTML = "Incorrect Username"
    }
    else{
        document.getElementById('error').innerHTML = "Incorrect Password"
    }
}

function decrypt(){
    var pass = document.getElementById('answerField').value;
    if (pass === 'N0t@PhishingSc@m'){
        window.location.href = '/task10/step2';
    }
    else{
        document.getElementById('error').innerHTML = "Incorrect Password"
    }
}