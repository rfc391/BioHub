#!/usr/bin/env python3

import tkinter as tk
import subprocess

def launch_main():
    subprocess.Popen(["python3", "main.py"])

def launch_scan():
    subprocess.Popen(["python3", "scripts/scan_module.py"])

def quit_app():
    root.destroy()

root = tk.Tk()
root.title("BioHub Launcher")
root.geometry("400x200")
root.configure(bg="#1e1e1e")

btn1 = tk.Button(root, text="🧬 Launch BioHub", command=launch_main, height=2, width=25, bg="#333", fg="white")
btn1.pack(pady=10)

btn2 = tk.Button(root, text="🛰 Run Scan Module", command=launch_scan, height=2, width=25, bg="#444", fg="white")
btn2.pack(pady=10)

btn3 = tk.Button(root, text="❌ Exit", command=quit_app, height=2, width=25, bg="#550000", fg="white")
btn3.pack(pady=10)

root.mainloop()
