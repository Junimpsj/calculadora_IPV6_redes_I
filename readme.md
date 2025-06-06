# 🌐 Calculadora IPv6 - Implementação com Abreviações

## Sobre o Projeto

Implementação educacional de uma **Calculadora IPv6** desenvolvida em Python puro, sem dependências externas. O projeto foi criado como trabalho acadêmico para a disciplina de Redes de Computadores e demonstra a aplicação prática dos conceitos de endereçamento IPv6 e suas regras de abreviação.

## 🎯 Objetivo

O principal objetivo deste projeto é implementar um algoritmo que converta endereços IPv6 completos para sua forma abreviada, seguindo rigorosamente as regras definidas pela RFC 5952, com foco especial na implementação dos conceitos **rightmost** e **leftmost** para compressão de zeros.

### Conceitos Implementados:
- **Rightmost**: Em caso de empate entre sequências de zeros, escolhe a mais à direita
- **Leftmost**: Em caso de empate entre sequências de zeros, escolhe a mais à esquerda

## 🔧 Características Técnicas

### Implementação Pura
- **Zero dependências**: Todo o código foi escrito do zero, sem utilizar bibliotecas de terceiros
- **Python nativo**: Utiliza apenas recursos built-in da linguagem
- **Código limpo**: Estruturado com classes e métodos bem definidos

### Funcionalidades Implementadas
- ✅ **Validação completa** de endereços IPv6
- ✅ **Remoção inteligente** de zeros à esquerda
- ✅ **Compressão otimizada** usando rightmost OU leftmost
- ✅ **Comparação lado a lado** dos dois métodos
- ✅ **Interface interativa** com menu simplificado
- ✅ **Demonstração automática** com exemplos pré-cadastrados

## 📊 Exemplo de Funcionamento

### Diferença entre Rightmost e Leftmost:
```
Endereço: 2001:0000:0000:0db8:0000:0000:0db8:0001/64

Rightmost: 2001::db8:0:0:db8:1/64    (escolhe a sequência da direita)
Leftmost:  2001:0:0:db8::db8:1/64    (escolhe a sequência da esquerda)
```

### Processo de Abreviação:
1. Remove zeros desnecessários (`0390` → `390`)
2. Identifica a maior sequência de zeros consecutivos
3. Aplica rightmost ou leftmost conforme escolhido
4. Substitui a sequência por `::`

## 🚀 Como Executar

### Pré-requisitos:
- Python 3.x instalado
- Nenhuma biblioteca externa necessária

### Execução:
```bash
python calculadora_ipv6.py
```

### Menu Principal:
```
============================================================
           CALCULADORA IPv6 - RIGHTMOST & LEFTMOST
============================================================

Escolha uma opção:

[1] Demonstração com valores pré-cadastrados
[2] Calcular endereço usando RIGHTMOST
[3] Calcular endereço usando LEFTMOST
[0] Sair
```

## 🎮 Modos de Operação

### 1. Demonstração Automática
- Exibe 5 endereços pré-cadastrados
- Mostra o resultado com rightmost e leftmost
- Destaca quando os resultados são diferentes

### 2. Cálculo com Rightmost
- Permite inserir endereços manualmente
- Aplica a regra rightmost (sequência mais à direita)
- Possibilidade de calcular múltiplos endereços

### 3. Cálculo com Leftmost
- Permite inserir endereços manualmente
- Aplica a regra leftmost (sequência mais à esquerda)
- Possibilidade de calcular múltiplos endereços

## 🏗️ Arquitetura

```
CalculadoraIPv6
├── validar_ipv6()                        # Valida formato IPv6
├── remover_zeros_esquerda()              # Remove zeros desnecessários
├── encontrar_sequencia_zeros_rightmost() # Implementa rightmost
├── encontrar_sequencia_zeros_leftmost()  # Implementa leftmost
├── abreviar_ipv6()                       # Orquestra a abreviação
└── processar_com_prefixo()               # Suporte para notação CIDR

Funções do Menu
├── exibir_menu()           # Interface principal
├── demonstracao_automatica() # Exemplos pré-cadastrados
└── calcular_endereco()     # Cálculo interativo
```

## 📋 Exemplos de Teste

### Casos que mostram diferença entre Rightmost e Leftmost:
```
1. 2001:0000:0000:0db8:0000:0000:0db8:0001/64
2. 2001:0db8:0000:0000:0001:0000:0000:0001/64
3. fe80:0000:0000:0001:0000:0000:0001:0001/64
4. 2001:0000:0000:0042:0000:0000:0000:7334/64
5. fc00:0000:0000:0000:0001:0000:0000:0000/7
```

### Casos gerais para teste:
```
- 2801:0390:0080:0000:0100:0000:0000:ff00/64
- 2001:0db8:0000:0000:0000:0000:0000:0001/128
- 0000:0000:0000:0000:0000:0000:0000:0001/128
- fe80:0000:0000:0000:0204:61ff:fe9d:f156/64
- 2001:0db8:85a3:0000:0000:8a2e:0370:7334/64
```

## 📝 Observações Importantes

1. O programa aceita apenas endereços IPv6 completos (8 grupos)
2. Cada grupo deve ter no máximo 4 caracteres hexadecimais
3. O prefixo é opcional (ex: /64, /128)
4. A entrada é convertida para minúsculas no resultado
5. Digite 'voltar' para retornar ao menu durante o cálculo interativo

---

**Disciplina**: Redes de Computadores  
**Linguagem**: Python 3.x  
**Conceitos**: IPv6, Rightmost, Leftmost, Abreviação de Endereços  
**Tags**: `ipv6` `networking` `python` `redes-de-computadores` `educacional` `rightmost` `leftmost`