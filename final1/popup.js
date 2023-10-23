document.addEventListener('DOMContentLoaded', function() {
    // Get the HTML text from storage
    chrome.storage.local.get('htmlText', function(data) {
        const htmlText = data.htmlText;

        // Display the HTML text in the popup
        const htmlTextElement = document.getElementById('htmlText');
        htmlTextElement.textContent = htmlText;
    });
});
