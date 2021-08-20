function changeColor(){
    color = document.getElementById('main').style.color;

    if (color == "blue"){
        document.getElementById('main').style = "color: yellow";
    } else {
        document.getElementById('main').style = "color: blue";
    }
    
}

let btn  = document.getElementById('colorChanger');
btn.addEventListener('click', changeColor);


// New button


function sayHi(){
    alert('Hey!!!!!!!!');
}
let hellobtn = document.getElementById('hello');

hellobtn.addEventListener('click', sayHi);
