from openai import OpenAI
client = OpenAI(
    api_key="")
user_input = ""
mensagens = [
    {"role": "system", "content": "Você é um contador de histórias de fantasia"}]
print("Digite sua mensagem")
while user_input != "fim":
    user_input = input('User >> ')
    mensagens.append({"role": "user", "content": user_input})
    completion = client.chat.completions.create(
        temperature=0.2,
        model="gpt-4o-mini",
        max_tokens=200,
        messages=mensagens
    )

    print("ChatGPT >> ", end="")
    print(completion.choices[0].message.content)
    mensagens.append(
        {"role": "assistant", "content": completion.choices[0].message.content})
