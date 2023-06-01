# Geekbench5-chrome-extension
This is a chrome extension that will add frequency tables to test on the geekbench5 page. By default, geekbench doesn’t show frequency of the processor in the test, however the data is recorded in the test.

![Captura de pantalla 2023-06-01 214609](https://github.com/jaruizra/Geekbench5-chrome-extension/assets/121313957/e2c88e47-90eb-483e-b9cb-724f181c91da)

# How does it work
It is an upgraded version of the Geekbench5-data-analysis-tool I created a time ago, but instead of python it is now JavaScript, so that it runs nicely as a chrome extension.

1. The manifest file of the extension detects when you are on a test page.
2. The JavaScript script starts and given a username and password of geekbench5, it logins to the page.
3. The scripts request the dictionary with all the test data.
4. It formats it and treats it to get the data needed for the frequency.
5. It modifies an html template with the html code that will be inserted into the main page of the test.
6. The frequency tables and statistics can be seen in the page like it was original of the page.

This can change by the minute, as I am learning about new ways to do this, I am also learning node, JavaScript, and chrome extension development on the fly.

# Thing to finish
Right know I’m having issues with JavaScript and the request of the data file from geekbench databases.
1. In python there was a library that handle login session_cookies and in JavaScript I haven’t find it, I need to do a lot of web scrapping

Main focus right now is issue 1 as soon as I can get the test data I can continue with other things.

3. The html code is done, however, the frequency table and max and min, need values that need to be inserted form the JavaScript. I have the data treatment done in python I only need to code it on JavaScript so that it works more easily.
4. I need to research how does normally an html extension add code to a page; however, I need to fix thing before this. 


# Things to change in the future.
The user logins to the page, so that the script doesn’t have to.
Upgraded functionality and general stability.
Only work when pressed, not all the time.
Upgraded frequency html format and code.
support for more CPUs and tests.

# Important
It is a working project, it has only been designed with Samsung phones CPU test, I haven’t checked the new Geekbench6 test data format, haven’t have time. No idea if it will show good information for other brands. It should work for general android phones; I don’t know about iPhone or desktop or arm cps. Gpu has not the frequency data, at least on phones. It will not show.


