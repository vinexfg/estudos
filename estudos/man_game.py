import time

# Função para impressão lenta do texto
def slow_print(text, delay=0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def main():
    slow_print("Bem-vindo ao jogo das emoções!")
    time.sleep(1)
    slow_print("Vamos começar com algumas perguntas que podem mexer com seus sentimentos.")
    time.sleep(1)

    questions = [
        "Qual é sua lembrança mais feliz?",
        "Se pudesse mudar algo no passado, o que seria?",
        "Qual é seu maior medo?",
        "Qual foi o momento mais difícil que já enfrentou?",
        "O que te faz sentir mais vivo?"
    ]

    for question in questions:
        slow_print(question)
        answer = input("> ")
        slow_print("Obrigado por compartilhar.\n")
        time.sleep(1)

    slow_print("Obrigado por jogar! Esperamos que você tenha aproveitado essa experiência.")
    time.sleep(1)

if __name__ == "__main__":
    main()
