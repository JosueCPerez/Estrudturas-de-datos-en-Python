
function login(){
    username = document.getElementById("Username").value
    password = document.getElementById("Password").value
    alert(username +" , "+ password)
}

function agregar(){
    var dato = document.getElementById("valor").value
    var data = JSON.stringify({
        "dato": dato
    });

    alert(data)

    fetch('http://localhost:3000/insertar', {
        method: 'post',
        headers: {
          'Content-Type': 'application/json'
        },
        body: data
      })
        .then(response => response.json())
        .then(data => {
            console.log(data)
          alert(data.response)
        });

}