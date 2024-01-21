from openai import OpenAI

api_key = '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'


def get_car_ai_bio(model, brand, year):
    prompt = f"""
    Me mostre uma descrição de venda pra o carro
    {model} {brand} {year} em apenas 200 caracteres. Fale coisas
    especificas sobre esse modelo de carro, fale sobre especificações
    técnicas sobre esse carro
    """
    client = OpenAI(api_key=api_key)
    response = client.chat.completions.create(
        model='gpt-3.5-turbo',
        messages=[
            {"role": "assistant", "content": prompt}
        ]
    )

    return response.choices[0].message.content
