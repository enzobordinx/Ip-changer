import wmi
import tkinter as tk
import win32api, sys, os
from tkinter import messagebox

def get_current_network_info():
    c = wmi.WMI()
    for interface in c.Win32_NetworkAdapterConfiguration(IPEnabled=True):
        ip_address = next((ip for ip in interface.IPAddress if len(ip) < 15), "")
        subnet_mask = interface.IPSubnet[0] if interface.IPSubnet else ""
        gateway = interface.DefaultIPGateway[0] if interface.DefaultIPGateway else ""
        return ip_address, subnet_mask, gateway
    return "", "", ""

def DhcpIpChanger():
    nic_configs = wmi.WMI().Win32_NetworkAdapterConfiguration(IPEnabled=True)
    # First network adapto  r
    nic = nic_configs[0]
    # Enable DHCP
    nic.EnableDHCP()
    return True

def StaticIpChanger():
    nic_configs = wmi.WMI('').Win32_NetworkAdapterConfiguration(IPEnabled=True)
    # First network adaptor
    nic = nic_configs[0]
    ip = entryIP.get()
    subnetmask = entrySubnet.get()
    gateway = entryGateway.get()
    dns1, dns2 = entryDNS.get().split(" - ")
    # Set IP address, subnetmask and default gateway
    # Note: EnableStatic() and SetGateways() methods require *lists* of values to be passed
    a = nic.EnableStatic(IPAddress=[ip],SubnetMask=[subnetmask])
    b = nic.SetGateways(DefaultIPGateway=[gateway])
    c = nic.SetDNSServerSearchOrder([dns1, dns2])
    ##d = nic.SetDynamicDNSRegistration(True)
    d = nic.SetDynamicDNSRegistration(FullDNSRegistrationEnabled=1)
    print(a)
    print(b)
    print(c)
    print(d)
    if [a[0], b[0], c[0], d[0]] == [0, 0, 0, 0]:
##        messagebox.showinfo("Done", message="IP Succesfully Change")
        return True
    else:
        errorMessage = """Return error codes are:
%s
%s
%s
%s
Detail information;
https://docs.microsoft.com/windows/desktop/CIMWin32Prov/setdynamicdnsregistration-method-in-class-win32-networkadapterconfiguration
"""%(a[0],b[0],c[0],d[0])
        with open("./ipchanger.txt","w") as f:
            f.write(errorMessage)
        messagebox.showwarning("Error", message="Error description in 'ipchanger.txt'")
        return False

def IpChanger():
    if varRadio.get() == "dhcp":
        if DhcpIpChanger():
            messagebox.showinfo("Done", message="IP Succesfully Change")
    else:
        if StaticIpChanger():
            messagebox.showinfo("Done", message="IP Succesfully Change")

def TrackRadioButton():
    if varRadio.get() == "dhcp":
        entryIP["state"] = "disable"
        entrySubnet["state"] = "disable"
        entryGateway["state"] = "disable"
        entryDNS["state"] = "disable"
    else:
        entryIP["state"] = "normal"
        entrySubnet["state"] = "normal"
        entryGateway["state"] = "normal"
        entryDNS["state"] = "normal"
        
# main part
top = tk.Tk()
top.geometry("250x350+100+100")
top.title("IP Changer")
top.resizable(False, False)
# radio buttons
varRadio = tk.StringVar()
radio1 = tk.Radiobutton(top, text="DHCP", variable=varRadio,
                             value="dhcp", command=TrackRadioButton)
radio1.pack()
tk.Label(text="_"*44, fg="#888888").pack(pady=5)

radio2 = tk.Radiobutton(top, text="Static", variable=varRadio,
                             value="static", command=TrackRadioButton)
radio2.pack()
varRadio.set("dhcp")
# IP entry
tk.Label(text="IP").pack()
entryIP = tk.Entry(top)
entryIP.pack()
c = wmi.WMI()
for interface in c.Win32_NetworkAdapterConfiguration(IPEnabled=1):
    for ip_address in interface.IPAddress:
        entryIP.insert(0, ip_address) if len(ip_address)<15 else entryIP.insert(0, "")
# subnetmask entry
tk.Label(text="\nSubnetmask").pack()
entrySubnet = tk.Entry(top)
entrySubnet.pack()
current_ip, current_subnet_mask, current_gateway = get_current_network_info()
entrySubnet.insert(0, current_subnet_mask)
# gateway entry
tk.Label(text="\nGateway").pack()
entryGateway = tk.Entry(top)
entryGateway.pack()
entryGateway.insert(0, current_gateway)
# dns entry
tk.Label(text="\nDNS").pack()
entryDNS = tk.Entry(top)
entryDNS.pack()
entryDNS.insert(0, "8.8.8.8 - 8.8.4.4")
tk.Label(text=" ").pack()
btnOK = tk.Button(top, text="Change", command=IpChanger)
btnOK.pack()
tk.Label(text=" ").pack()
TrackRadioButton()
top.mainloop()
