class UrnaEletronica:
    def __init__(self):
        self.candidatos = {
            "Fernando Hugo": "Partido do Brasil",
            "Arya Mendes": "Partido Honesto",
            "Patrick Queiroz": "Seita do Bem",
            "Leandro Melo": "Juntos e Unidos"
        }

    def listar_candidatos(self):
        print("-"*45)
        for nome, partido in self.candidatos.items():    
            print(f"Candidato: {nome} - Partido: {partido} ")
        print("-"*45)

    def exclui_candidato(self):
        self.candidatos.popitem()

    def adiciona_candidato(self, nome, partido):
        self.candidatos[nome] = partido

    def atualiza_candidato(self, nome):
        novoPartido = input(f"Digite o novo partido de {nome}: ")
        self.candidatos[nome] = novoPartido


urna = UrnaEletronica()

urna.listar_candidatos()

urna.exclui_candidato()

urna.listar_candidatos()

urna.adiciona_candidato("Alamo Almeida", "Sem Pobreza")

urna.listar_candidatos()

urna.atualiza_candidato("Alamo Almeida")

urna.listar_candidatos()