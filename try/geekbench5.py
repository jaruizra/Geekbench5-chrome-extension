import json
import requests.exceptions
import analysis
import requests
from bs4 import BeautifulSoup
from jinja2 import Template
import sys


def get_url(url):
    t = url
    url = t + ".gb5"
    with requests.Session() as session:
        page = session.get("https://browser.geekbench.com/session/new")
        html = BeautifulSoup(page.content, "html.parser")
        csrf_token = html.find("input", {"name": "authenticity_token"})["value"]
        data_to_login = {'utf8': "✓",
                         "authenticity_token": csrf_token,
                         "user[username]": "tt7562905",
                         "user[password]": "testtest",
                         "commit": "Log in"
                         }
        r = session.post("https://browser.geekbench.com/session/create", data_to_login)
        t = session.get(url)
        html_dict = json.loads(t.text)
    return html_dict


def get_geekbench_data(url):
    o = get_url(url)
    test_data = analysis.tests(o)
    return test_data



import sys

while True:
    # Read a message from stdin
    message = sys.stdin.readline().strip()
    if not message:
        break

test_data = get_geekbench_data(url)
freq_data = {
    'av_freq': test_data.av_freq,
    'max_freq' : test_data.max_freq,
    'min_freq' : test_data.min_freq,
    'freq_table' : test_data.create_freq_str()
}
with open("template.html") as f:
    template = Template(f.read())

html = template.render(freq_data)

with open("output.html", "w") as g:
    g.write(html)

sys.stdout.write(result + '\n')
sys.stdout.flush()
        
    