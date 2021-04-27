import re


text = "A Random string."

pattern = re.compile("[rdm]")

result = pattern.search(text)

print(result)