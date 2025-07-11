#!/usr/bin/env python3
import tkinter as tk
from tkinter import scrolledtext
import requests

def analyser_headers():
    url = entry.get().strip()
    if not url.startswith("http"):
        url = "http://" + url

    result_box.delete(1.0, tk.END)
    status_label.config(text="⏳ Analyse en cours...")

    try:
        response = requests.get(url, timeout=5)
        headers = response.headers

        for k, v in headers.items():
            result_box.insert(tk.END, f"{k}: {v}\n")

        status_label.config(text="✅ Analyse terminée")
    except Exception as e:
        result_box.insert(tk.END, f"❌ Erreur : {e}")
        status_label.config(text="❌ Échec")

# Interface
root = tk.Tk()
root.title("HTTP Header Analyzer")
root.geometry("600x450")
root.config(bg="#1a1a1a")

tk.Label(root, text="URL ou domaine :", bg="#1a1a1a", fg="white").pack(pady=5)
entry = tk.Entry(root, width=40)
entry.pack()
entry.insert(0, "https://example.com")

tk.Button(root, text="🔍 Analyser", command=analyser_headers, bg="#2196f3", fg="white").pack(pady=10)

result_box = scrolledtext.ScrolledText(root, width=70, height=15, bg="black", fg="lime")
result_box.pack(padx=10, pady=10)

status_label = tk.Label(root, text="En attente...", bg="#1a1a1a", fg="gray")
status_label.pack()

root.mainloop()
