function Work(){
    console.log("hello")


    let name=document.getElementById("inputName").value;
    let email=document.getElementById("inputEmail").value;
    let password=document.getElementById("inputPass").value;
    let confirmPassword=document.getElementById("inputConfPass").value;

// console.log(x,y,z,w)
if (!name || !email || !password || !confirmPassword) {
    document.getElementById("Pa").innerHTML = "All fields are required!";
    return; 
}
if(password != confirmPassword ){
    document.getElementById("Pa").innerHTML="password is not the same !!";
    document.getElementById("inputPass").value= "";
    document.getElementById("inputConfPass").value="";
}

const users = JSON.parse(localStorage.getItem("users")) || {};

console.log("Available users:");
for (const email in users) {
    console.log("Email:", email);
    console.log("User Info:", users[email]); 
}


let newEmail =email;
let newUser = {
    name: name,
    password: password
};

users[newEmail] = newUser;

localStorage.setItem("users", JSON.stringify(users));

document.getElementById("inputName").value="";
document.getElementById("inputEmail").value="";
document.getElementById("inputPass").value="";
document.getElementById("inputConfPass").value="";
}
