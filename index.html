<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>Image Search</title>
  <script src="https://telegram.org/js/telegram-web-app.js"></script>
  <style>
    body {
      font-family: sans-serif;
      padding: 20px;
      text-align: center;
    }
    #loading-spinner {
      display: none;
      font-size: 20px;
      margin-top: 10px;
    }
    #image-container {
      margin-top: 20px;
    }
  </style>
</head>
<body>
  <h2>Search for an Image</h2>
  <input type="text" id="query" placeholder="Type something..." />
  <button onclick="searchImages()">Search</button>

  <div id="loading-spinner">Loading...</div>
  <div id="image-container"></div>

  <script>
    function searchImages() {
      const query = document.getElementById("query").value.trim();
      if (!query) return alert("Enter a search term!");

      document.getElementById("loading-spinner").style.display = "block";
      document.getElementById("image-container").innerHTML = "";

      fetch(`/search?q=${encodeURIComponent(query)}`)
        .then(res => {
          if (!res.ok) throw new Error(`Server responded with ${res.status}`);
          return res.blob();
        })
        .then(blob => {
          const url = URL.createObjectURL(blob);
          document.getElementById("image-container").innerHTML = `<img src="${url}" style="max-width: 100%;">`;
        })
        .catch(err => {
          console.error("Fetch error:", err);
          alert("Error: " + err.message);
        })
        .finally(() => {
          document.getElementById("loading-spinner").style.display = "none";
        });

      // Optional fallback timeout
      setTimeout(() => {
        const spinner = document.getElementById("loading-spinner");
        if (spinner.style.display !== "none") {
          spinner.style.display = "none";
          alert("Took too long. Try again?");
        }
      }, 3000);
    }
  </script>
</body>
</html>
