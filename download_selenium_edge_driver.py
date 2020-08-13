import os
import sys

class download_selenium_edge_driver():

    def __init__(self):
        self.my_version = ''
        self.architecture = ''

    def fetch_browser_version(self):
        my_version = self.my_version
        my_current_path = os.getcwd()
        path_to_my_batch_file = f'{my_current_path}\\get_edge_browser_version.bat'

        my_version = os.popen(path_to_my_batch_file).read() # Batch file contains code which fetches the browser version.
        my_version = my_version.strip().replace(' ','') # Clean the output of the batch file.
        my_version = my_version.split('=')[1] # Output of batch file is in format 'version = <browser_version>, we are interested only in the version number.

        return my_version

    def fetch_os_architecture(self):
        architecture = self.architecture
        command_to_fetch_pc_architecture = 'wmic os get osarchitecture'
        
        architecture = os.popen(command_to_fetch_pc_architecture).read() # Fetching system architecture
        architecture = architecture.split('\n')[2] # Cleaning the output of the command, fetching the os architecture
        architecture = architecture.strip()

        if architecture == '64-bit':
            return 'edgedriver_win64.zip' # If architecture is 64 bit, then return the string else return the string as 32 bit.
        else:
            return 'edgedriver_win32.zip'

    def open_driver_download_url(self, driver_download_url):
        command_to_open_my_url = f'start msedge {driver_download_url}'
        os.system(command_to_open_my_url) # Launching the edge browser with the appropriate URL for downloading the edge driver.

if __name__ == '__main__':

    try:
        automate = download_selenium_edge_driver()
        my_edge_browser_version = automate.fetch_browser_version()
        my_driver_package_to_download = automate.fetch_os_architecture()

        # Multiline string as a menu.
        my_menu = '''
Do you want to view the driver download page or automatically download the driver ?

1)Enter \'v\' to view the link
2)Enter \'d\' to automatically download the driver

'''

        print(f'\nEdge Browser version = {my_edge_browser_version}\n')
        print(f'Package to download = {my_driver_package_to_download}\n')

        view_driver_url = f'https://msedgewebdriverstorage.z22.web.core.windows.net/?prefix={my_edge_browser_version}/'
        driver_download_url = f'https://msedgedriver.azureedge.net/{my_edge_browser_version}/{my_driver_package_to_download}'

        my_choice = input(my_menu)
        if my_choice == 'v' or my_choice == 'V' or my_choice == '1':
            print(f'Visit {view_driver_url} to download the webdriver of your PC architecture')
            input('Press Any key to exit ...')

        elif my_choice == 'd' or my_choice == 'D' or my_choice == '2':
            automate.open_driver_download_url(driver_download_url)
        else:
            print(f'Visit {view_driver_url} to download the webdriver of your PC architecture')
            input('Press Any key to exit ...')

    except Exception as e:
        print(str(e))

    finally:
        sys.exit()