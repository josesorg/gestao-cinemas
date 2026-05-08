from controller.cinema_controller import CinemaController

class CinemaView:
    def __init__(self):
        self.controller = CinemaController()

    def exibir_menu_cadastro(self):
        print("\n--- CADASTRAR NOVO CINEMA ---")
        nome = input("Nome do Cinema: ")
        endereco = input("Endereço: ")
        capacidade = int(input("Capacidade Máxima: "))

        sucesso, mensagem = self.controller.criar_cinema(nome, endereco, capacidade)
        
        if sucesso:
            print(f"✅ {mensagem}")
        else:
            print(f"❌ Erro: {mensagem}")