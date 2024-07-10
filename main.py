import tkinter as tk

from modules import NLPPipeline
from tkinter import messagebox

def nlp(text):
    pipeline = NLPPipeline()
    tokens, pos_tags, parse_tree = pipeline.process(text)

    return pos_tags

def show_widget(root):
    label = tk.Label(root, text='Enter some text:')
    label.pack()
    entry = tk.Entry(root)
    entry.pack()
    submit_button = tk.Button(root, text='Submit', command=lambda: show_result(entry))
    submit_button.pack()

def show_result(entry):
    text = entry.get()
    messagebox.showinfo('Result', f'pos_tags: { nlp(text) }')

def main():
    root = tk.Tk()
    root.title('english-parser')
    root.geometry("640x400+100+100")
    root.resizable(False, False)

    show_widget(root)

    root.mainloop()

if __name__ == "__main__":
    main()
