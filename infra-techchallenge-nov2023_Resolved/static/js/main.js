document.addEventListener("DOMContentLoaded", function() {
    // for debugging
    console.log("edenceHealth");

    // load the job description text
    // Fixing Bug 2, the job_description file name is not correctly mentioned for the python code to format
    //fetch("/content/job")
    fetch('/content/job_description')
      .then(response => response.text())
      .then(html => {
          // Fixing Bug 2, the element id should be in sync with the id mentioned in the html class
          //document.getElementById("job_description").innerHTML = html;
        document.getElementById("job").innerHTML = html;
      });

    // load 10 puppy URLs from the database
    for (let i = 0; i <= 9; i++) {
      fetch(`/puppy/${i}`)
        .then(response => response.json())
        .then(data => {
          let img = document.createElement("img");
          img.src = data["url"];
          img.classList.add("img-responsive");
          // Fixing Bug 3, the element id should be in sync with the id mentioned in the html class
          //document.getElementById("thepuppies").appendChild(img);
          document.getElementById("puppies").appendChild(img);
        });
    }
  });
