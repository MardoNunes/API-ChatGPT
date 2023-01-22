import openai

openai.api_key = " SUA_CHAVE_API "
num = 0
print('-> 0: Para fazer um pergunta;')
print('-> 1: Para sair;')
num = int(input('Entre com sua opção: '))
while(num != 1):
	ask = input('Pergunta: ')
	response = openai.Completion.create(
  		model="text-davinci-003",
  		prompt=ask,
  		temperature=0.9,
  		max_tokens=150,
  		top_p=1,
  		frequency_penalty=0,
  		presence_penalty=0.6,
  		stop=[" Human:", " AI:"]
		)

	text = response['choices'][0]['text']
	print ('Resposta: '+text)
	print('-> 0: Para Continuar;')
	print('-> 1: Para sair;')
	num = int(input('Entre com sua opção: \n'))
    
	
	
