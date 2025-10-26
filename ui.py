import tkinter as tk
from tkinter import font, filedialog

global uds_path
uds_path = None

root = tk.Tk()

root.title("UDS Configurator")
root.geometry("600x600")
root.resizable(False, False)

def uds_save_reset(*a):
    uds_save_options.config(text="Save")

tk.Label(root, text="Unturned Dedicated Server Configurator", font=("Consolas", 16)).pack(pady=20)

tk.Label(root, text="Unturned Dedicated Server Path:", font=("Consolas", 12)).pack(pady=8)
def uds_choose_folder():
    uds_folder_path = filedialog.askdirectory()
    if uds_folder_path:
        file = f"{uds_folder_path}/Servers/Default/Server/Commands.dat"
        try:
            with open(file, "r") as file:
                uds_choose_button.config(text=f"{uds_folder_path}")
                global uds_path
                uds_path = f"{uds_folder_path}"
                uds_save_reset()
        except FileNotFoundError:
            uds_choose_button.config(text="This folder does not contain \Servers\Default\Server\Commands.dat file!")
uds_choose_button = tk.Button(root, text="Choose Folder", command=uds_choose_folder, font=("Consolas", 10))
uds_choose_button.pack()

tk.Label(root, text="Server Options:", font=("Consolas", 12)).pack(pady=30)

# Choose Difficulty
difficulty_optionMenu_selected_option = tk.StringVar(root)
difficulty_optionMenu_options = ["Easy", "Normal", "Hard"]
difficulty_optionMenu_selected_option.set(difficulty_optionMenu_options[0])
difficulty_optionMenu_option_menu = tk.OptionMenu(root, difficulty_optionMenu_selected_option, *difficulty_optionMenu_options, command=uds_save_reset)
difficulty_optionMenu_option_menu.place(relx=0.27, rely=0.4, anchor=tk.CENTER)
difficulty_optionMenu_option_menu.config(font=("Consolas", 10))
root.nametowidget(difficulty_optionMenu_option_menu.menuname).config(font=("Consolas", 10))
tk.Label(root, text="Difficulty:", font=("Consolas", 12)).place(relx=0.115, rely=0.4, anchor=tk.CENTER)

# Choose Map
map_optionMenu_selected_option = tk.StringVar(root)
map_optionMenu_options = ["Germany", "PEI", "Russia", "Washington", "Yukon"]
map_optionMenu_selected_option.set(map_optionMenu_options[1])
map_optionMenu_option_menu = tk.OptionMenu(root, map_optionMenu_selected_option, *map_optionMenu_options, command=uds_save_reset)
map_optionMenu_option_menu.place(relx=0.27, rely=0.475, anchor=tk.CENTER)
map_optionMenu_option_menu.config(font=("Consolas", 10))
root.nametowidget(map_optionMenu_option_menu.menuname).config(font=("Consolas", 10))
tk.Label(root, text="Map:", font=("Consolas", 12)).place(relx=0.115, rely=0.475, anchor=tk.CENTER)

# Choose Perspective
perspective_optionMenu_selected_option = tk.StringVar(root)
perspective_optionMenu_options = ["First", "Third", "Both"]
perspective_optionMenu_selected_option.set(perspective_optionMenu_options[2])
perspective_optionMenu_option_menu = tk.OptionMenu(root, perspective_optionMenu_selected_option, *perspective_optionMenu_options, command=uds_save_reset)
perspective_optionMenu_option_menu.place(relx=0.27, rely=0.55, anchor=tk.CENTER)
perspective_optionMenu_option_menu.config(font=("Consolas", 10))
root.nametowidget(perspective_optionMenu_option_menu.menuname).config(font=("Consolas", 10))
tk.Label(root, text="Perspective:", font=("Consolas", 12)).place(relx=0.115, rely=0.55, anchor=tk.CENTER)

# Change Port
def on_entry_change(*args):
    try:
        uds_save_reset()
    except:
        pass

def validate_entry(new_value):
    max_length = 5
    if len(new_value) <= max_length and new_value.isdigit():
        return True
    else:
        return False
vcmd = root.register(validate_entry)
port_var = tk.StringVar()
port_var.trace_add('write', on_entry_change)
port_entry = tk.Entry(root, width=5, justify="center", font=("Consolas", 12), validate="key", validatecommand=(vcmd, '%P'), textvariable=port_var)
port_entry.insert(0, "27015")
port_entry.place(relx=0.55, rely=0.4, anchor=tk.CENTER)
tk.Label(root, text="Port:", font=("Consolas", 12)).place(relx=0.45, rely=0.4, anchor=tk.CENTER)

# Change IP
def validate_entry(new_value):
    uds_save_reset()
    return True
vcmd = root.register(validate_entry)
ip_var = tk.StringVar()
ip_var.trace_add('write', on_entry_change)
ip_entry = tk.Entry(root, width=16, justify="center", font=("Consolas", 12), validatecommand=(vcmd, '%P'), textvariable=ip_var)
ip_entry.insert(0, "localhost")
ip_entry.place(relx=0.55, rely=0.475, anchor=tk.CENTER)
tk.Label(root, text="IP:", font=("Consolas", 12)).place(relx=0.4, rely=0.475, anchor=tk.CENTER)

# Change MaxPlayers
def validate_entry(new_value):
    #uds_save_reset()
    max_length = 3
    if len(new_value) <= max_length:
        return True
    else:
        return False
vcmd = root.register(validate_entry)
maxplayers_var = tk.StringVar()
maxplayers_var.trace_add('write', on_entry_change)
maxplayers_entry = tk.Entry(root, width=3, justify="center", font=("Consolas", 12), validate="key", validatecommand=(vcmd, '%P'), textvariable=maxplayers_var)
maxplayers_entry.insert(0, "8")
maxplayers_entry.place(relx=0.625, rely=0.55, anchor=tk.CENTER)
tk.Label(root, text="Max Players:", font=("Consolas", 12)).place(relx=0.485, rely=0.55, anchor=tk.CENTER)

# Edit & Save UDS files
def save_options():
    if uds_path is None:
        uds_save_options.config(text="UDS Path not choosed!")
    else:
        file = f'{uds_path}/Servers/Default/Server/Commands.dat'
        difficulty = difficulty_optionMenu_selected_option.get()
        map = map_optionMenu_selected_option.get()
        perspective = perspective_optionMenu_selected_option.get()
        port = port_entry.get()
        ip = ip_entry.get()
        maxplayers = maxplayers_entry.get()
        with open(file, "r+") as f:
            f.seek(0)
            f.truncate()
        with open(file, 'a') as f:
            f.write(f"mode {difficulty}\n")
            f.write(f"map {map}\n")
            f.write(f"perspective {perspective}\n")
            f.write(f"port {port}\n")
            f.write(f"ip {ip}\n")
            f.write(f"maxplayers {maxplayers}\n")
        uds_save_options.config(text="Saved!")
uds_save_options = tk.Button(root, text="Save", font=("Consolas", 12), command=save_options)
uds_save_options.place(relx=0.5, rely=0.95, anchor=tk.CENTER)

root.mainloop()