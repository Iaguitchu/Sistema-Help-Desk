var email_input = document.getElementById("email")
var password_input = document.getElementById("password")
var btn_enviar = document.getElementById("enviar")

btn_enviar.addEventListener("click",function() {

    var email = email_input.value
    var password = password_input.value

    fetch('/login', {
        method:"POST",
        headers:{
            "Content-Type":"application/json"
        },
        body: JSON.stringify({
            email:email,
            password:password,
        }),
    }).then(response => {
        if (response.redirected) {
            window.location.href = response.url; // redireciona se o back-end mandar redirect
        } else {
            return response.json();
        }
    })
    .then(data => {
        console.log(data);
    })
    .catch(error => console.error("Erro:", error));
});
