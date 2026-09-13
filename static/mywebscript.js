// Calls the /emotionDetector Flask endpoint with the text typed by the
// user and shows the result (or the error message) on the page.
function RunSentimentAnalysis() {
  const textToAnalyze = document.getElementById("textToAnalyze").value;

  fetch(`/emotionDetector?textToAnalyze=${encodeURIComponent(textToAnalyze)}`)
    .then((response) => response.text())
    .then((data) => {
      document.getElementById("system_response").innerText = data;
    })
    .catch(() => {
      document.getElementById("system_response").innerText =
        "Something went wrong. Please try again.";
    });
}
