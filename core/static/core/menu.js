console.log('Do arquivo!')

  var infor = "{{info}}"
  if (infor == "") {
    document.getElementById("index_menu").classList.add('active')
  } else {
    console.log(infor)
    document.getElementById(infor).classList.add('active')
    document.getElementById("index_menu").classList.remove('active')
  }
