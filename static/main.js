document.querySelector('form').onsubmit = function(){
    if(!document.querySelector('input').value){
        alert("You must provide your name");
        return false;
    } else if(!document.querySelector('select').value){
        alert("You must provide your favorit sport");
        return false
    }
    return true
};