# --- CLASSE (O MOLDE DO SISTEMA) ---
class Veiculo:
    """
    Classe para gerir veículos num estacionamento.
    """
    def __init__(self, placa, modelo, hora_entrada):
        # Guarda os dados iniciais do carro
        self.placa = placa
        self.modelo = modelo
        self.hora_entrada = hora_entrada

    def informações(self):
        # Retorna os dados formatados
        return f"Carro: {self.modelo} | Placa: {self.placa} | Entrada: {self.hora_entrada}h"

    def finalizar(self, hora_saida):
        # Guarda a saída e faz os cálculos
        self.hora_saida = hora_saida
        tempo = self.hora_saida - self.hora_entrada
        valor_total = tempo * 5  # 5 reais por hora

        # Exibe o recibo final
        print("\n" + "="*20)
        print("   RECIBO")
        print("="*20)
        print(f"Tempo: {tempo} horas")
        print(f"Total: R$ {valor_total:.2f}")
        print("="*20)

# --- FLUXO PRINCIPAL (INTERAÇÃO COM O UTILIZADOR) ---

# 1. Entrada de dados
p = input("Digite a placa: ")
m = input("Digite o modelo: ")
e = float(input("Hora de entrada (ex: 9.5): "))

# 2. Criação do objeto
carro1 = Veiculo(p, m, e)
print(f"\nRegistado: {carro1.informações()}")

# 3. Saída e Cálculo
s = float(input("\nDigite a hora de saída (ex: 12.0): "))
carro1.finalizar(s)
