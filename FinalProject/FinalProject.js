const users = JSON.parse(localStorage.getItem("users")) || {};
console.log(users)
function Clik_on() {
    const x = document.getElementById("inputemail").value.trim();
    const y = document.getElementById("inputpass").value;

    if (users[x] && users[x].password === y) {
        console.log("bravo ");
        localStorage.setItem("currentUser", JSON.stringify({
            name: users[x].name,
            email: x
        }));

        window.location.href = "Home.html";
    }else if(x=="admin@quiz.com" && users[x].password =="admin123"){
        window.location.href = "AdminResult.html"; 

    } else {
        document.getElementById("para").innerHTML = "Wrong email or password ";
    }
}
