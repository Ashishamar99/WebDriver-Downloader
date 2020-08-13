# WebDriver-Downloader [Built for Windows]
A tool created with python which automates the procedure for downloading a compatible webdriver. 

#### Here are a few References -
* [An article about this tool.](https://medium.com/@ashishamar1999/selenium-webdriver-downloader-b5653916488a?sk=963420936607681d2f79749c3793554e)
* [A demo video of this tool.]()
----------------------------------------------------------------------------------------------------------------------------------------

#### A simple breakdown of how the code works - 
* fetch_browser_version - fetches the browser version using the batch script.
* fetch_os_architecture - fetches the architecture of the PC.
* open_driver_download_url - downloads the driver automatically.

----------------------------------------------------------------------------------------------------------------------------------------

#### Here are a few things you will have to do before running this code -
* Add the path of the edge executable (msedge.exe) to the system path.
* Make sure that the path to the edge executable in the batch file matches the path your system. (You should do this only if you have changed the installation path of edge.)
* Make sure that the batch file is present in the same folder as the code.
