from keytotext import pipeline
# external dependencies required! run !pip install keytotext --upgrade in terminal
# run as a collab notebook for in browser functionality

gen = pipeline("mrm8488/t5-base-finetuned-common_gen")

print("This is Build 3 of the (not) new dumpster fire(c) AI\nsay something to the funny AI")

while True:

  userinput = input()
  userinput = userinput.lower()

  print("AI:" + gen(userinput.split()))