import openai as openai


class Davinci():
    def __init__(self):
        openai.api_key = ""

    def request(self, prompt):
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            temperature=0.5,
            max_tokens=512,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.1
        )
        return response['choices'][0]['text'].strip()