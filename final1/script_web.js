const parser = new DOMParser();
var token = ""

function savetofile(content, name) {
    writeFile(name, content)
        .then(() => {
            console.log("Html saved");
            chrome.storage.local.set({htmlText: htmlText });

            chrome.widows.create({
                url: chrome.extensions.getURL("popup.html"),
                type: "popup",
                width: 600,
                height: 400
            })
            .catch((error) => {
                console.log("error al salvar")
                console.error('Error saving HTML file:', error);
            });
        })
    
}
function fetchdata(url) {
    console.log("2");
    fetch("https://browser.geekbench.com/session/new")
        .then((response) => {
            console.log("3");
            console.log(response)
            const jj = response.text()
            console.log(jj)
            return jj
        })
        .then((html) => {
            console.log("4");
            console.log(html)
            const parser = new DOMParser();
            const doc = parser.parseFromString(html, "text/html");
            token = doc.querySelector("input[name='authenticity_token']").value;
            console.log("5");
            const data_to_login = {
                method: 'POST',
                "utf8": "✓",
                "authenticity_token": token,
                "user[username]": "tt7562905",
                "user[password]": "testtest",
                "commit": "Log in"
            };
            const options = {
                method: 'POST',
                body: JSON.stringify(data_to_login),
            };
            console.log(options)
            console.log("6");
            const sesion_create = fetch("https://browser.geekbench.com/session/create", data_to_login);
            return sesion_create
        })
        .then((response) => {
            console.log("7");

            const jj2 = fetch(url)
            console.log(jj2)
            return jj2
        })
        .then((response) => {
            console.log("8");
            return response.text();
        })
        .then((html_text) => {
            console.log("9");
            //console.log(html_text);
            console.log(html_text)
            //savetofile(html_text, "page.html")
            return html_text;
        })
        .catch((error) => {
            console.log("error1")
            console.error('Error:', error);
        });
}

var currenturl = window.location.href;

url = currenturl + ".gb5"
console.log("1");
console.log(url)
fetchdata(url) 
        
