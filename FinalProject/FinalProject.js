// Get the list of users (just in case you need them)
const users = JSON.parse(localStorage.getItem("users")) || {};

// Get the current logged-in user info
const currentUser = JSON.parse(localStorage.getItem("currentUser"));
function Clik_on(){
   
    const x=document.getElementById("inputemail").value;
    const y=document.getElementById("inputpass").value;
    for (const key in users) {
        if (x.trim()==key.trim() && users[key].password==y){
            console.log("bravo");
            window.location.href = "Home.html";
        }else{
            document.getElementById("para").innerHTML="Wrong password !!";
        }
    }
}
