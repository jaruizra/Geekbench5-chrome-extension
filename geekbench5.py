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


url = sys.argv[1]
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
    
    
    dvMViBRCpQ9I60EFmHQlTcSpijC5INnDKpHifcrNm1M0XJV%2FrIxrGzcRW7Vs06LLoZ71wP6XonjU9te%2FqNVRlx43VPmeLvTNOP5ipzsofbPUx1j6CXanqx8RI0%2BmHFA71PQ%2FvDYRalzvYXS44BE%3D--cR0h1TQz4yGW%2F7QJ--uajTJ5V2lirJoVXxAaRShA%3D%3D