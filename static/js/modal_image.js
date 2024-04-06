// Function to display image modal
function displayImageModal(imageUrl) {
  var modal = document.getElementById("myModal");
  var modalImg = document.getElementById("img01");
  var captionText = document.getElementById("caption");

  modal.style.display = "block";
  modalImg.src = imageUrl;
  modalImg.alt = "Image";
  captionText.innerHTML = "Image Caption";
}

var span = document.getElementsByClassName("close")[0];

span.onclick = function () {
  var modal = document.getElementById("myModal");
  modal.style.display = "none";
};