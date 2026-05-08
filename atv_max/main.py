from view.cinema_view import CinemaView
from db.database import get_connection

def main():
    # Inicializa o banco de dados e cria as tabelas se não existirem
    get_connection()

    view = CinemaView()
    
    while True:
        print("\n--- SISTEMA DE GESTÃO DE CINEMAS ---")
        print("1. Cadastrar Cinema")
        print("0. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            view.exibir_menu_cadastro()
        elif opcao == '0':
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()