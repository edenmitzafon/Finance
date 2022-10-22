function check(){
  var input = document.getElementById("password").value;
  var len1 = document.getElementById("check0");
  var len2 = document.getElementById("check1");
  var num = document.getElementById("check2");
  var special_char = document.getElementById("check3");
  var upper = document.getElementById("check4");
  var lower = document.getElementById("check5");


  var length8 = input.length >= 8;
  var length20 = input.length <= 20 && input.length > 0;
  var numeric = /[0-9]/i;
  var special = /[^A-Za-z0-9-'']/i;
  var upper_char = /[A-Z]/;
  var lower_char = /[a-z]/;


  input = input.trim();
  document.getElementById("password").value = input;

  if(length8){
    len1.style.color = "green";
  }
  else{
    len1.style.color = "red";
  }

  if(length20){
    len2.style.color = "green";
  }
  else{
    len2.style.color = "red";
  }

  if(input.match(numeric)){
    num.style.color = "green";
  }
  else{
    num.style.color = "red";
  }

  if(input.match(special)){
    special_char.style.color = "green";
  }
  else{
    special_char.style.color = "red";
  }

  if(input.match(upper_char)){
    upper.style.color = "green";
  }
  else{
    upper.style.color = "red";
  }

  if(input.match(lower_char)){
    lower.style.color = "green";
  }
  else{
    lower.style.color = "red";
  }
}
