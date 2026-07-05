from transformers import pipeline

generator = pipeline(
    "text2text-generation",
    model="google/flan-t5-base"
)


prompt = """
Create a social media post.

Topic: Pongal Sale
Tone: Catchy

Generate:
1. Caption with emojis
2. 5 hashtags
3. One image idea
4. Two variants
"""

# Generate output
result = generator(
    prompt,
    max_length=150,
    do_sample=True,
    temperature=0.9
)

# Print result
print(result[0]["generated_text"])