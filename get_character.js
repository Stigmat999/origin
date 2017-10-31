function get_name() {

  var xhr = new XMLHttpRequest();

  xhr.open('GET', 'https://gateway.marvel.com:443/v1/public/characters/1011334?ts=1&apikey=204e691d22c22c092ea42a42b12cf6ae&hash=0dd119037baf98be90f0044cec645d1a', false);
  xhr.send();

  if (xhr.status != 200) {
    alert('Ошибка ' + xhr.status + ': ' + xhr.statusText);
  } 
    else {
      var xhr = xhr.responseText;
      xhr = JSON.parse(xhr);
      return xhr.data.results[0].name;
      }
    
}

function get_img() {

  var xhr = new XMLHttpRequest();

  xhr.open('GET', 'https://gateway.marvel.com:443/v1/public/characters/1011334?ts=1&apikey=204e691d22c22c092ea42a42b12cf6ae&hash=0dd119037baf98be90f0044cec645d1a', false);
  xhr.send();

  if (xhr.status != 200) {
    alert('Ошибка ' + xhr.status + ': ' + xhr.statusText);
  } 
    else {
      var xhr = xhr.responseText;
      xhr = JSON.parse(xhr);
      var img = xhr.data.results[0].thumbnail.path + "." + xhr.data.results[0].thumbnail.extension;

      return img;
      }

}

window.onload = function() {
  var name = get_name();
  var hero_name = document.getElementById("id1");
  console.log(name);
  hero_name.innerHTML = name;

  var image = get_img();
  var hero_image = document.getElementById("id2");
  console.log(image);
  hero_image.src = image;
};
