import tkinter as tk
import subprocess
import re

def show_ip():
    cmd_output = subprocess.check_output('ipconfig').decode('cp1252')
    pattern = re.compile(r'. . . . . . . . :\s(.*)')
    output = ''
    for line in cmd_output.splitlines():
        match = pattern.search(line)
        if match:
            output += match.group(1) + '\n'
    ip_list = pattern.findall(cmd_output)
    output_text.config(state='normal')
    output_text.delete('1.0', 'end')
    output_text.insert('end', f"MAC: {ip_list[0]}\nIPV4: {ip_list[1]}\nSUB-REDE: {ip_list[2]}\nGATEWAY: {ip_list[3]}")
    output_text.config(state='disabled')

# Create GUI
root = tk.Tk()
root.title("IP Configuration")
root.geometry("400x400")

# Add button to show IP
ip_button = tk.Button(root, text="Show IP", command=show_ip)
ip_button.pack(pady=10)

# Add text widget to show IP output
output_text = tk.Text(root, state='disabled')
output_text.pack()

root.mainloop()


