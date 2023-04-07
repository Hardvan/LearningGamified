function goToHome() {
  window.location.href = "/#college";
}

document.getElementById("yesBtn").addEventListener("click", function () {
  document.getElementById("result").innerHTML = "An accurate model";
  document.getElementById("result").style.color = "green";
});

document.getElementById("noBtn").addEventListener("click", function () {
  document.getElementById("result").innerHTML = "Models make mistake sometimes";
  document.getElementById("result").style.color = "red";
});
