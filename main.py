import tkinter as tk
from modules import NLPPipeline

class NLPApplication:
    def __init__(self, root):
        self.root = root
        self.root.title('english-parser')
        self.root.geometry("640x480+100+100")
        self.root.resizable(False, False)

        self.pipeline = NLPPipeline()
        self.initialize_components()
        
    def initialize_components(self):
        label = tk.Label(self.root, text='Enter some text:')
        label.pack()
        entry = tk.Entry(self.root)
        entry.bind('<Return>', lambda event: self.show_result(entry))
        entry.pack()
        submit_button = tk.Button(self.root, text='Submit', command=lambda: self.show_result(entry))
        submit_button.pack()
        
        self.pos_tags_label = tk.Label(self.root, text='POS-Tags will be displayed here.', wraplength=400, justify='left')
        self.pos_tags_label.pack(padx=20, pady=20)
        self.formats_label = tk.Label(self.root, text='Formats will be displayed here.', wraplength=400, justify='left')
        self.formats_label.pack(padx=20, pady=20)
        self.optimized_label = tk.Label(self.root, text='Optimized-Sentence will be displayed here.', wraplength=400, justify='left')
        self.optimized_label.pack(padx=20, pady=20)
        self.translated_label = tk.Label(self.root, text='Translated-Sentence will be displayed here.', wraplength=400, justify='left')
        self.translated_label.pack(padx=20, pady=20)
        
    def show_result(self, entry):
        text = entry.get()
        
        if text:
            pos_tags = self.pipeline.pos_tagging(text)
            format = self.pipeline.format_analysis(text)
            optimized = self.pipeline.sentence_optimize(text)
            translated = self.pipeline.sentence_translate(text)
        else:
            pos_tags, format, optimized, translated = 'Please enter some text.'

        self.pos_tags_label.config(text=pos_tags)
        self.formats_label.config(text=format)
        self.optimized_label.config(text=optimized)
        self.translated_label.config(text=translated)

def main():
    root = tk.Tk()
    app = NLPApplication(root)
    root.mainloop()

if __name__ == "__main__":
    main()
