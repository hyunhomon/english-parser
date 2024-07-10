from modules import NLPPipeline

def main():
    text = "This is an example sentence. Here is another sentence with different structure. And finally, the third sentence."
    pipeline = NLPPipeline()
    tokens, pos_tags, parse_tree = pipeline.process(text)

    print("Tokens:", tokens)
    print("POS Tags:", pos_tags)
    print("Parse Tree:")
    print(parse_tree)

if __name__ == "__main__":
    main()
