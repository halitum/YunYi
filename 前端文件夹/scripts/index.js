let left = document.getElementById('jiantou_left');
let right = document.getElementById('jiantou_right');
let son_left = document.getElementById('son_left');
let son_right = document.getElementById('son_right');
let icon_adm = document.getElementById('icon_adm');
let icon_stu = document.getElementById('icon_stu');

son_left.onclick = function(){
    window.location.href = "http://101.200.73.250/登录注册.html"
}
left.onclick = function () {
    son_left.style.transform = "translate3d(0px,0px,0px)";
    son_left.style.transitionProperty = "transform"
    son_left.style.transitionDuration="0.5s"
    son_right.style.transform = "translate3d(100px,-50px,-50px)";
    son_right.style.transitionProperty = "transform";
    son_right.style.transitionDuration = "0.5s";
    icon_adm.style.transform = "transitionZ(50px)";
    icon_stu.style.transform = "transitionZ(-50px)";
    left.style.display = "none";
    right.style.display = "block";
    son_right.style.pointerEvents = "none"
    son_left.style.pointerEvents="visiblePainted"

    son_left.onclick = function(){
        window.location.href = "http://101.200.73.250/登录注册.html"
    }
    


}
right.onclick = function () {
    son_left.style.transform = "translate3d(-360px,0px,-50px)";
    son_left.style.transitionProperty = "transform"
    son_left.style.transitionDuration="0.5s"
    son_right.style.transform = "translate3d(-260px,-50px,0)";
    son_right.style.transitionProperty = "transform";
    son_right.style.transitionDuration = "0.5s";
    icon_adm.style.transform = "transitionZ(-50px)";
    icon_stu.style.transform = "transitionZ(50px)";
    left.style.display = "block";
    right.style.display = "none";
    // son_right.style.pointerEvents="block"
    son_left.style.pointerEvents = "none"
    son_right.style.pointerEvents="visiblePainted"
    son_right.onclick = function () {
        window.location.href = "http://101.200.73.250/登录注册.html"
        
    }
    
    

}