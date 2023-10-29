Sources:
- https://blog.finxter.com/openapi-cheat-sheet/
- https://docs.aipower.org/docs/ai-engine/openai/frequency-penalty

**model**: The name of the model you want to use, e.g., ‘gpt-4.0-turbo’. This specifies which version of the model you
want
to interact with.

**prompt**: The input text that you want to provide to the model. This can be a question, a sentence, or any other text
you
want the model to process or complete.

**max_tokens**: The maximum number of tokens (words or word pieces) you want the model to generate in its response. A
lower
value will result in shorter responses, while a higher value allows for more detailed and longer responses.

**temperature**: A value between 0 and 1 that controls the randomness of the model’s output. A higher value (e.g., 0.8)
will
result in more random and creative responses, while a lower value (e.g., 0.2) will produce more focused and
deterministic responses.

**top_p**: A value between 0 and 1 that controls the sampling strategy, also known as nucleus sampling. The model will
only
consider a subset of tokens whose cumulative probability exceeds top_p. This can be useful for controlling the diversity
of generated text.

**n**: The number of independent completions you want the model to generate for the given input. If you set this to a
value
greater than 1, the API will return multiple completions, which can be useful for exploring a range of possible
responses.

**stream**: A boolean value (True or False) that specifies whether to use streaming mode for generating results. When
set to
True, the API will return results incrementally as they become available, which can be useful for real-time
applications.

**echo**: A boolean value (True or False) that controls whether the input prompt should be included in the output. When
set
to True, the output will include both the input prompt and the model-generated completion.

**stop**: A string or list of strings that specifies the stopping sequence(s) for the model. When the model encounters
any
of these sequences, it will stop generating further text.

**presence_penalty**: A value that controls how much the model should penalize new tokens based on the presence of
similar
tokens in the prompt. This can be useful for controlling repetition in the generated text.

**frequency_penalty**: A value that controls how much the model should penalize tokens based on their frequency in the
training data. This can be useful for encouraging the model to generate more novel or uncommon phrases.


