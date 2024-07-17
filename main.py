import tkinter as tk
from tkhtmlview import HTMLLabel
from modules import NLPPipeline

class NLPApplication:
    def __init__(self, root):
        self.root = root
        self.root.title('english-parser')
        self.root.geometry('480x640+100+100')
        self.root.configure(bg='#fff')

        self.content = ''
        self.pipeline = NLPPipeline()
        self.set_widgets()

        self.root.state('zoomed')
        
    def set_widgets(self):
        bottom_frame = tk.Frame(self.root)
        bottom_frame.pack(side=tk.BOTTOM, fill=tk.X, padx=20, pady=(4, 28))

        self.entry = tk.Entry(bottom_frame, font=('Arial', 16), bg='#f2f2f2', relief='flat')
        self.entry.bind('<Return>', lambda event: self.show_result())
        self.entry.pack(side=tk.LEFT, fill=tk.X, expand=True)

        photo_button = tk.Button(bottom_frame, text='Photo', font=('Arial', 12), command=self.load_photo)
        photo_button.pack(side=tk.LEFT, padx=8, pady=8)
        
        submit_button = tk.Button(bottom_frame, text='Submit', font=('Arial', 12), command=self.show_result)
        submit_button.pack(side=tk.LEFT, padx=8, pady=8)

        self.text = HTMLLabel(self.root, background="#fff")
        self.text.pack(fill=tk.BOTH, padx=20, pady=(28, 4), expand=True)

    def load_photo(self):
        file_path = tk.filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif;*.bmp;*.tiff")])
        recognized = self.pipeline.image_recognition(file_path)
        self.entry.delete(0, tk.END)
        self.entry.insert(0, recognized)

    def show_result(self):
        text = self.entry.get()

        if text:
            self.content += f"""
                <div style='background-color: #fff;'>
                    <h4>원본 문장:</h4>
                    <p>{text}</p>
                    
                    <h4>품사를 포함한 문장:</h4>
                    <p>{self.pipeline.pos_tagging(text)}</p>
                    
                    <h4>구문이 분리된 문장:</h4>
                    <p>{self.pipeline.format_analysis(text)}</p>
                    
                    <h4>최적화된 문장:</h4>
                    <p>{self.pipeline.sentence_optimize(text)}</p>
                    
                    <h4>한글로 번역된 문장:</h4>
                    <p>{self.pipeline.sentence_translate(text)}</p>
                </div>
            """
            self.text.set_html(self.content)

if __name__ == "__main__":
    root = tk.Tk()
    app = NLPApplication(root)
    root.mainloop()
