Name: Srihari Chandramouli
Uta Id: 1001529776
Programming Language: Python
Version: 3.6
ABOUT THE PROGRAM
*********
This program has two parts:
1. The first part is connecting to the weather server with the help of the connect() which takes the url and requests
the weather server which then returns the desired outputs like the temperature, wind speed, wind direction et cetera.

2. In the second part, I have converted the link given by the professor which was in JSON format. I have converted the JSON format
to XML file in a file called convertjsonweather.xml . Then I have parsed it using ElementTree and then I have retrieved the details using
ElementTree syntax for achieving the desired output.

3. In order to access the 2 parts, we have to comment several lines:
    3a) Initially, the program is in the second part where we use the XML parsing
    3b) In order to access the first part, comment the WeatherParser() and the Refresh() function and Uncomment the connect(). Similarly comment the 84th
    line and uncomment the 83rd line and likewise, comment the 87th line and uncomment the 86th line
EXECUTION
*********
1. First execute the program
2. Enter the latitude and longitude
3. You will be asked to enter the period
4. Desired output will come.

CITATIONS
*********
1. https://docs.python.org/3.4/howto/sockets.html
2. https://docs.python.org/3/library/tkinter.html
3. http://www.diveintopython3.net/xml.html
4. https://www.youtube.com/watch?v=LNYoFo1sdwg
5. https://stackoverflow.com/questions/21179272/parsing-a-url-xml-with-the-the-elementtree-xml-api
6. https://docs.python.org/3.4/library/xml.etree.elementtree.html
7. https://stackoverflow.com/questions/35120250/python-3-get-and-parse-json-api
8. https://stackoverflow.com/questions/23131227/how-to-readlines-from-urllib
