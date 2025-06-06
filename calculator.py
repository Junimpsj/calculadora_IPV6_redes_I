class CalculadoraIPv6:
    """
    Implementação das regras de abreviação usando os conceitos rightmost e leftmost para IPV6 para escolha de sequências de zeros.
    """
    
    def __init__(self):
        """
        Aqui estamos inicializando a calculadora sem modo fixo, O modo será escolhido na hora de processar cada endereço.
        """
        pass
    
    def validar_ipv6(self, endereco):
        """
        Função para checar se o endereço IPv6 tá no formato certo. IPv6 tem que ter 8 octetos separados por ':' e cada grupo
        tem que ser um hexadecimal válido de até 4 caracteres.
        """
        partes = endereco.split(':')
        
        #Sempre tem 8 octetos
        if len(partes) != 8:
            return False
        
        #Verifica cada octeto
        for parte in partes:
            if len(parte) > 4:
                return False
            try:
                int(parte, 16) if parte else 0
            except ValueError:
                return False
        
        return True
    
    def remover_zeros_esquerda(self, grupo):
        """
        Remove zeros à esquerda
        """
        resultado = grupo.lstrip('0')
        return resultado if resultado else '0'
    
    def encontrar_sequencia_zeros_rightmost(self, grupos):
        """
        No rightmost quando há empate, escolhe a sequência mais à direita.
        """
        max_inicio = -1
        max_tamanho = 0
        
        #Procura todas as sequências de zeros
        i = 0
        while i < len(grupos):
            if grupos[i] == '0':
                inicio = i
                tamanho = 0
                while i < len(grupos) and grupos[i] == '0':
                    tamanho += 1
                    i += 1
                
                if tamanho >= max_tamanho and tamanho >= 2:
                    max_inicio = inicio
                    max_tamanho = tamanho
            else:
                i += 1
        
        return max_inicio, max_tamanho
    
    def encontrar_sequencia_zeros_leftmost(self, grupos):
        """
        No leftmost quando há empate, escolhe a sequência mais à esquerda.
        """
        max_inicio = -1
        max_tamanho = 0
        
        #Procura todas as sequências de zeros
        i = 0
        while i < len(grupos):
            if grupos[i] == '0':
                inicio = i
                tamanho = 0
                while i < len(grupos) and grupos[i] == '0':
                    tamanho += 1
                    i += 1
                
                if tamanho > max_tamanho and tamanho >= 2:
                    max_inicio = inicio
                    max_tamanho = tamanho
            else:
                i += 1
        
        return max_inicio, max_tamanho
    
    def abreviar_ipv6(self, endereco_completo, modo='rightmost'):
        """
        Abrevia um endereço IPv6 usando o modo escolhido pelo usuário
        """
        #Limpa e padroniza
        endereco_completo = endereco_completo.strip().lower()
        
        #Validando aqui
        if not self.validar_ipv6(endereco_completo):
            return "Endereço IPv6 inválido"
        
        #Separando em grupos
        grupos = endereco_completo.split(':')
        
        #Removendo zeros à esquerda
        grupos_sem_zeros = [self.remover_zeros_esquerda(grupo) for grupo in grupos]
        
        #Escolhe o método baseado no modo
        if modo == 'rightmost':
            inicio, tamanho = self.encontrar_sequencia_zeros_rightmost(grupos_sem_zeros)
        else:
            inicio, tamanho = self.encontrar_sequencia_zeros_leftmost(grupos_sem_zeros)
        
        #Aplicando a compressão se encontrou sequência válida
        if tamanho >= 2 and inicio != -1:
            parte_esquerda = grupos_sem_zeros[:inicio]
            parte_direita = grupos_sem_zeros[inicio + tamanho:]
            
            if parte_esquerda and parte_direita:
                endereco_abreviado = ':'.join(parte_esquerda) + '::' + ':'.join(parte_direita)
            elif parte_esquerda:
                endereco_abreviado = ':'.join(parte_esquerda) + '::'
            elif parte_direita:
                endereco_abreviado = '::' + ':'.join(parte_direita)
            else:
                endereco_abreviado = '::'
        else:
            #Definindo quando não tem compressão
            endereco_abreviado = ':'.join(grupos_sem_zeros)
        
        return endereco_abreviado
    
    def processar_com_prefixo(self, entrada, modo='rightmost'):
        """
        Processa endereços com ou sem prefixo (ex: /64)
        """
        partes = entrada.strip().split('/')
        
        if len(partes) == 2:
            endereco = partes[0].strip()
            prefixo = partes[1].strip()
            endereco_abreviado = self.abreviar_ipv6(endereco, modo)
            return f"{endereco_abreviado}/{prefixo}"
        else:
            return self.abreviar_ipv6(entrada, modo)


def exibir_menu():
    """
    Mostra o menu principal bonito e organizado
    """
    print("\n" + "="*60)
    print("           CALCULADORA IPv6 - RIGHTMOST & LEFTMOST")
    print("="*60)
    print("\nEscolha uma opção:")
    print("\n[1] Demonstração com valores pré-cadastrados")
    print("[2] Calcular endereço usando RIGHTMOST")
    print("[3] Calcular endereço usando LEFTMOST")
    print("[0] Sair")
    print("\n" + "="*60)


def demonstracao_automatica(calc):
    """
    Mostrando exemplos pré-cadastrados comparando rightmost e leftmost
    """
    print("\n" + "="*60)
    print("        DEMONSTRAÇÃO - COMPARAÇÃO RIGHTMOST vs LEFTMOST")
    print("="*60)
    
    #Endereços que mostram diferença entre os dois métodos (endereços gerados por I.A para serem utilizados como teste)
    exemplos = [
        "2001:0000:0000:0db8:0000:0000:0db8:0001/64",
        "2001:0db8:0000:0000:0001:0000:0000:0001/64",
        "fe80:0000:0000:0001:0000:0000:0001:0001/64",
        "2001:0000:0000:0042:0000:0000:0000:7334/64",
        "fc00:0000:0000:0000:0001:0000:0000:0000/7"
    ]
    
    for i, exemplo in enumerate(exemplos, 1):
        print(f"\nExemplo {i}:")
        print(f"Original:  {exemplo}")
        
        #Calcula com rightmost
        resultado_right = calc.processar_com_prefixo(exemplo, 'rightmost')
        print(f"Rightmost: {resultado_right}")
        
        #Calcula com leftmost
        resultado_left = calc.processar_com_prefixo(exemplo, 'leftmost')
        print(f"Leftmost:  {resultado_left}")
        
        #Destaca quando são diferentes
        if resultado_right != resultado_left:
            print("          !Resultados diferentes!")
        else:
            print("          !Resultados iguais")
        
        print("-" * 60)
    
    input("\nPressione ENTER para voltar ao menu...")


def calcular_endereco(calc, modo):
    """
    Permite ao usuário inserir um endereço e calcula usando o modo especificado
    """
    print("\n" + "="*60)
    print(f"         CALCULAR ENDEREÇO IPv6 - MODO {modo.upper()}")
    print("="*60)
    
    while True:
        print("\nDigite o endereço IPv6 (ou 'voltar' para retornar ao menu)")
        print("Formato: xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx/prefixo")
        entrada = input("\n> ").strip()
        
        if entrada.lower() == 'voltar':
            break
        
        #Processa o endereço
        resultado = calc.processar_com_prefixo(entrada, modo)
        
        print("\n" + "-"*40)
        print(f"Original:  {entrada}")
        print(f"Abreviado: {resultado}")
        print("-"*40)
        
        #Pergunta se quer calcular outro
        continuar = input("\nCalcular outro endereço? (s/n): ").lower()
        if continuar != 's':
            break


def main():
    """
    Função principal com menu simplificado
    """
    calc = CalculadoraIPv6()
    
    while True:
        exibir_menu()
        
        try:
            opcao = input("\nDigite sua opção: ")
            
            if opcao == '1':
                demonstracao_automatica(calc)
            
            elif opcao == '2':
                calcular_endereco(calc, 'rightmost')
            
            elif opcao == '3':
                calcular_endereco(calc, 'leftmost')
            
            elif opcao == '0':
                print("\n Obrigado por usar a Calculadora IPv6!")
                print("Até a próxima!\n")
                break
            
            else:
                print("\n Opção inválida! Por favor, escolha 0, 1, 2 ou 3.")
                input("Pressione ENTER para continuar...")
        
        except KeyboardInterrupt:
            print("\n\n Programa interrompido pelo usuário.")
            break
        except Exception as e:
            print(f"\n Erro: {e}")
            input("Pressione ENTER para continuar...")


if __name__ == "__main__":
    main()