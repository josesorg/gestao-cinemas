from service.cinema_service import CinemaService

class CinemaController:
    def __init__(self):
        self.service = CinemaService()

    def criar_cinema(self, nome, endereco, capacidade_maxima):
        try:
            self.service.cadastrar_cinema(nome, endereco, capacidade_maxima)
            return True, "Cinema cadastrado com sucesso!"
        except Exception as e:
            return False, str(e)