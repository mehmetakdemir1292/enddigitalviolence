import language_tool_python

tool = language_tool_python.LanguageTool('en-US')
with open("example_sentences.txt", "r") as f:
    sentences = f.readlines()

for sentence in sentences:
    matches = tool.check(sentence)
    print(f"Sentence: {sentence.strip()}")
    for match in matches:
        print(f" - Issue: {match.message}")
    print()
