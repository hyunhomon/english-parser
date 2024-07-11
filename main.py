import tkinter as tk
from modules import NLPPipeline

class NLPApplication:
    def __init__(self, root):
        self.root = root
        self.root.title('english-parser')
        self.root.geometry("600x400+100+100")
        self.root.resizable(False, False)
        
        self.initialize_components()
        
    def initialize_components(self):
        label = tk.Label(self.root, text='Enter some text:')
        label.pack()
        entry = tk.Entry(self.root)
        entry.bind('<Return>', lambda event: self.show_result(entry))
        entry.pack()
        submit_button = tk.Button(self.root, text='Submit', command=lambda: self.show_result(entry))
        submit_button.pack()
        
        self.result_label = tk.Label(self.root, text='POS Tags will be displayed here.', wraplength=400, justify='left')
        self.result_label.pack(padx=20, pady=20)
        
    def show_result(self, entry):
        text = entry.get()
        result = self.nlp(text) if text else 'Please enter some text.'
        self.result_label.config(text=result)
    
    def nlp(self, text):
        pipeline = NLPPipeline()
        pos_tags = pipeline.process(text)
        return pos_tags

def main():
    root = tk.Tk()
    app = NLPApplication(root)
    root.mainloop()

if __name__ == "__main__":
    main()
