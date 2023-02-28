# Ip-changer
This tkinter code creates a GUI that displays a computer's IP details when 'Show IP' button is pressed. Users can switch between DHCP and static IP settings and input new IP, subnet mask, gateway, and DNS values. Successful changes show a message box while errors prompt an error message.


#README for Checkip:

This Python code provides a graphical user interface (GUI) using the tkinter library to display IP configuration details on a Windows machine. The code uses the subprocess library to execute the 'ipconfig' command in a command prompt window and the re library to search for IP-related information within the command output. Once the IP-related information is found, the output is displayed on the GUI using a text widget. The GUI includes a button that triggers the function to display the IP information.

To run the code, Python 3 must be installed on the Windows machine. The code can be executed in a Python integrated development environment (IDE) or by running the script in a command prompt window. The tkinter and subprocess libraries must be imported for the code to function.

#README for IPchanger_windows:

This Python code provides a GUI using the tkinter library to change the IP configuration of a Windows machine. The code uses the wmi library to interact with the Windows Management Instrumentation (WMI) service to enable or disable DHCP and set static IP, subnet mask, default gateway, and DNS server values. The GUI includes radio buttons to select DHCP or static IP mode and text boxes to input the IP-related values. The code also includes a button to execute the IP configuration changes.

To run the code, Python 3 and the required libraries must be installed on the Windows machine. The code can be executed in a Python IDE or by running the script in a command prompt window. The code requires administrative privileges to change the IP configuration of the machine. The user should review and update the IP-related values in the code to match their network configuration. In addition, the user should review the error codes in the code and the reference link to troubleshoot any configuration issues that may arise.
