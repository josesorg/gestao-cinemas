from repository.cinema_repository import CinemaRepository
from model.cinema import Cinema

class CinemaService:
    def __init__(self):
        self.repository = CinemaRepository()

    def cadastrar_cinema(self, nome, endereco, capacidade_maxima):
        # Validação simples de Regra de Negócio
        if capacidade_maxima <= 0:
            raise ValueError("A capacidade máxima deve ser maior que zero!")
        
        novo_cinema = Cinema(nome, endereco, capacidade_maxima)
        self.repository.salvar(novo_cinema)