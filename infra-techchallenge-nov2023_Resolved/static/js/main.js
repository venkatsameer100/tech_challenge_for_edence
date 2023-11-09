document.addEventListener("DOMContentLoaded", function() {
    // for debugging
    console.log("edenceHealth");

    // load the job description text
    fetch('/content/job_description') //Bug Fix 2
      .then(response => response.text())
      .then(html => {
        document.getElementById("job_description").innerHTML = html;
      });

    // load 10 puppy URLs from the database
    for (let i = 0; i <= 9; i++) {
      fetch(`/puppy/${i}`)
        .then(response => response.json())
        .then(data => {
          let img = document.createElement("img");
          img.src = data["url"];
          img.classList.add("img-responsive");
          document.getElementById("thepuppies").appendChild(img);
        });
    }
  });
