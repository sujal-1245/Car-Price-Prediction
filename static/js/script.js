document.getElementById("predictBtn").addEventListener("click", function () {
    document.getElementById("formPanel").classList.add("active");
  });
  
  document.getElementById("predictBtn").addEventListener("click", function () {
    document.getElementById("formPanel").classList.add("active");
  });
  
  document.getElementById("predictionForm").addEventListener("submit", function (e) {
    e.preventDefault();
  
    const formData = new FormData(this);
  
    fetch("/predict", {
      method: "POST",
      body: formData,
    })
      .then((response) => response.json())
      .then((data) => {
        const resultDiv = document.getElementById("result");
        if (data.price) {
          resultDiv.innerHTML = `<h3>Predicted Price: ₹${data.price}</h3>`;
          resultDiv.classList.add("show");
        } else {
          resultDiv.innerHTML = `<p class="error">Error: ${data.error}</p>`;
        }
      })
      .catch((err) => console.log(err));
  });

  let slides = document.querySelectorAll(".hero-slider .slide");
let currentSlide = 0;

setInterval(() => {
  slides[currentSlide].classList.remove("active");
  currentSlide = (currentSlide + 1) % slides.length;
  slides[currentSlide].classList.add("active");
}, 4000); // Change image every 4 seconds

document.getElementById("predictBtn").addEventListener("click", function () {
  const formPanel = document.getElementById("formPanel");
  formPanel.classList.toggle("show");
});

  