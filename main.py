import tkinter as tk
from modules import NLPPipeline

class NLPApplication:
    def __init__(self, root):
        self.root = root
        self.root.title('english-parser')
        self.root.geometry('640x480+100+100')
        self.root.configure(bg='#fff')

        self.pipeline = NLPPipeline()
        self.initialize_components()

        self.root.state('zoomed')
        
    def initialize_components(self):
        self.text = tk.Text(self.root, wrap=tk.WORD, font=('Arial', 12), bg='#fff', fg='#000', bd=0, relief='flat')
        self.text.pack(fill=tk.BOTH, padx=20, pady=(28, 4), expand=True)

        bottom_frame = tk.Frame(self.root)
        bottom_frame.pack(side=tk.BOTTOM, fill=tk.X, padx=20, pady=(4, 28))

        self.entry = tk.Entry(bottom_frame, font=('Arial', 16), bg='#F2F2F2', fg='#000', bd=0, relief='flat')
        self.entry.bind('<Return>', lambda event: self.show_result())
        self.entry.pack(side=tk.LEFT, ipady=8, fill=tk.X, expand=True)
        photo_button = tk.Button(bottom_frame, text='Photo', font=('Arial', 12), bg='#F2F2F2', fg='#000', bd=1, relief='solid', command=self.load_photo)
        photo_button.pack(side=tk.LEFT, padx=12, pady=8)
        submit_button = tk.Button(bottom_frame, text='Submit', font=('Arial', 12), bg='#F2F2F2', fg='#000', bd=1, relief='solid', command=self.show_result)
        submit_button.pack(side=tk.LEFT, padx=12, pady=8)

    def load_photo(self):
        pass

    def show_result(self):
        text = self.entry.get()
        result = 'Please enter some text.'

        if text: result = f'원본 문장:\n{text}\n\n품사를 포함한 문장:\n{self.pipeline.pos_tagging(text)}\n\n구문이 분리된 문장:\n{self.pipeline.format_analysis(text)}\n\n최적화된 문장:\n{self.pipeline.sentence_optimize(text)}\n\n한글로 번역된 문장:\n{self.pipeline.sentence_translate(text)}\n\n---\n\n'
        self.text.insert(tk.END, result)

if __name__ == "__main__":
    root = tk.Tk()
    app = NLPApplication(root)
    root.mainloop()
