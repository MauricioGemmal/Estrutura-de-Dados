class Paciente:
    """
    Classe que representa um paciente no sistema de triagem hospitalar.
    """
    def __init__(self, nome, idade, descricao, gravidade):
        """
        Inicializa um novo paciente.
        
        Args:
            nome (str): Nome do paciente.
            idade (int): Idade do paciente.
            descricao (str): Descrição do problema de saúde.
            gravidade (str): Nível de gravidade do paciente (Crítico, Grave, Moderado, Leve).
        """
        self.nome = nome
        self.idade = idade
        self.descricao = descricao
        self.gravidade = gravidade
    
    def __str__(self):
        """
        Retorna uma representação em string do paciente.
        """
        return f"Paciente: {self.nome} (Idade: {self.idade}, Gravidade: {self.gravidade})\nDescrição: {self.descricao}"


class FilaPacientes:
    """
    Implementação de uma fila para armazenar pacientes de mesma gravidade.
    """
    def __init__(self):
        """
        Inicializa uma fila vazia.
        """
        self.pacientes = []
    
    def adicionar(self, paciente):
        """
        Adiciona um paciente ao final da fila.
        """
        self.pacientes.append(paciente)
    
    def remover(self):
        """
        Remove e retorna o paciente do início da fila.
        """
        if not self.esta_vazia():
            return self.pacientes.pop(0)
        return None
    
    def frente(self):
        """
        Retorna o paciente do início da fila sem removê-lo.
        """
        if not self.esta_vazia():
            return self.pacientes[0]
        return None
    
    def esta_vazia(self):
        """
        Verifica se a fila está vazia.
        """
        return len(self.pacientes) == 0
    
    def tamanho(self):
        """
        Retorna o número de pacientes na fila.
        """
        return len(self.pacientes)


class GerenciadorTriagem:
    """
    Sistema de gerenciamento de pacientes em triagem hospitalar.
    """
    def __init__(self):
        """
        Inicializa o gerenciador de triagem com filas para cada nível de gravidade.
        """
        self.filas_gravidade = {
            "Crítico": FilaPacientes(),
            "Grave": FilaPacientes(),
            "Moderado": FilaPacientes(),
            "Leve": FilaPacientes()
        }
    
    def adicionar_paciente(self, paciente):
        """
        Adiciona um paciente à triagem de acordo com sua gravidade.
        """
        if paciente.gravidade not in self.filas_gravidade:
            print(f"Erro: Gravidade inválida ({paciente.gravidade})")
            return False
        
        self.filas_gravidade[paciente.gravidade].adicionar(paciente)
        print(f"Paciente '{paciente.nome}' adicionado com gravidade {paciente.gravidade}")
        return True
    
    def proximo_paciente(self):
        """
        Retorna o próximo paciente a ser atendido, removendo-o da fila.
        """
        for gravidade in ["Crítico", "Grave", "Moderado", "Leve"]:
            fila = self.filas_gravidade[gravidade]
            if not fila.esta_vazia():
                return fila.remover()
        
        print("Não há pacientes aguardando atendimento")
        return None
    
    def visualizar_proximo_paciente(self):
        """
        Visualiza o próximo paciente sem removê-lo da fila.
        """
        for gravidade in ["Crítico", "Grave", "Moderado", "Leve"]:
            fila = self.filas_gravidade[gravidade]
            if not fila.esta_vazia():
                return fila.frente()
        
        print("Não há pacientes aguardando atendimento")
        return None
    
    def listar_pacientes(self):
        """
        Lista todos os pacientes agrupados por nível de gravidade.
        """
        print("\n===== LISTA DE PACIENTES EM TRIAGEM =====")
        for gravidade in ["Crítico", "Grave", "Moderado", "Leve"]:
            fila = self.filas_gravidade[gravidade]
            num_pacientes = fila.tamanho()
            print(f"\n--- Gravidade {gravidade} ({num_pacientes} pacientes) ---")
            if fila.esta_vazia():
                print("Nenhum paciente nesta categoria")
                continue
            for i, paciente in enumerate(fila.pacientes):
                print(f"{i+1}. {paciente.nome} - {paciente.descricao[:50]}{'...' if len(paciente.descricao) > 50 else ''}")
        print("========================================")


# Demonstração do sistema
if __name__ == "__main__":
    triagem = GerenciadorTriagem()
    
    pacientes = [
        Paciente("João Silva", 45, "Dor no peito intensa", "Crítico"),
        Paciente("Maria Oliveira", 30, "Febre alta persistente", "Grave"),
        Paciente("Carlos Santos", 60, "Pressão alta", "Moderado"),
        Paciente("Ana Souza", 25, "Tosse leve", "Leve"),
        Paciente("Luiz Fernandes", 50, "Fratura exposta", "Crítico"),
        Paciente("Beatriz Ramos", 33, "Dores abdominais moderadas", "Moderado"),
        Paciente("Ricardo Alves", 40, "Gripe forte", "Grave"),
        Paciente("Fernanda Costa", 28, "Pequeno corte no braço", "Leve")
    ]
    
    print("Adicionando pacientes à triagem...\n")
    for paciente in pacientes:
        triagem.adicionar_paciente(paciente)
    
    triagem.listar_pacientes()
    
    print("\nAtendendo pacientes por ordem de gravidade:")
    for _ in range(5):
        paciente = triagem.proximo_paciente()
        if paciente:
            print(f"\nAtendendo: {paciente}")
            print("-" * 40)
    
    triagem.listar_pacientes()
