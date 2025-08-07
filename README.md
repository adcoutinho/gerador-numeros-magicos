# Gerador de Números Aleatórios

Este programa gera sequências de 15 dezenas únicas de 01 a 25, garantindo que todas as sequências sejam diferentes entre si.

## Características

- 🎲 Gera sequências de 15 números únicos de 01 a 25
- ✨ Todas as sequências são diferentes entre si
- 📊 Mostra progresso durante a geração
- 💾 Opção de salvar resultados em arquivo
- 🛡️ Validação de entrada robusta
- 🎯 Interface amigável com emojis e formatação

## Como usar

### Opção 1: Executar diretamente
```bash
python3 gerador_numeros.py
```

### Opção 2: Tornar executável
```bash
chmod +x gerador_numeros.py
./gerador_numeros.py
```

## Exemplo de uso

```
🎲 GERADOR DE NÚMEROS ALEATÓRIOS
============================================================
📋 Gera sequências de 15 dezenas únicas de 01 a 25
✨ Todas as sequências são diferentes entre si
============================================================

Quantas sequências você deseja gerar? 5

🎯 Vou gerar 5 sequência(s) única(s).
Deseja continuar? (s/n): s

============================================================
Gerando 5 sequências únicas...

🎉 5 sequências geradas com sucesso!
============================================================
Sequência 0001: 02 - 04 - 07 - 09 - 11 - 13 - 14 - 16 - 17 - 19 - 20 - 21 - 23 - 24 - 25
Sequência 0002: 01 - 03 - 05 - 06 - 08 - 10 - 12 - 15 - 16 - 18 - 19 - 22 - 23 - 24 - 25
Sequência 0003: 01 - 02 - 04 - 06 - 09 - 11 - 13 - 14 - 17 - 18 - 20 - 21 - 22 - 24 - 25
Sequência 0004: 03 - 05 - 07 - 08 - 10 - 12 - 13 - 15 - 16 - 18 - 19 - 21 - 22 - 23 - 25
Sequência 0005: 01 - 02 - 03 - 05 - 08 - 09 - 12 - 14 - 15 - 17 - 18 - 20 - 22 - 24 - 25
============================================================
✅ Processo concluído! 5 sequências únicas geradas.
```

## Recursos do programa

### Validação de entrada
- Aceita apenas números inteiros positivos
- Limite máximo de 1.000.000 sequências
- Tratamento de erros de digitação

### Geração inteligente
- Algoritmo eficiente para evitar duplicatas
- Indicador de progresso para gerações longas
- Limite de segurança para evitar loops infinitos

### Formatação profissional
- Números formatados com zero à esquerda (01, 02, etc.)
- Sequências ordenadas automaticamente
- Interface colorida e intuitiva

### Salvamento opcional
- Para mais de 10 sequências, oferece opção de salvar
- Arquivo nomeado automaticamente
- Formato organizado e legível

## Informações técnicas

### Probabilidades
- Total de combinações possíveis: C(25,15) = 3.268.760
- Cada sequência tem probabilidade única de 1/3.268.760
- Algoritmo garante não repetição até o limite matemático

### Requisitos
- Python 3.6 ou superior
- Módulos padrão: `random`, `sys`
- Sistema operacional: Qualquer (Linux, Windows, macOS)

### Estrutura do código
- Funções modulares e bem documentadas
- Tratamento robusto de exceções
- Código limpo seguindo PEP 8

## Exemplos de arquivos gerados

O programa pode salvar as sequências em arquivo de texto:

```
SEQUÊNCIAS DE NÚMEROS GERADAS
==================================================
Total de sequências: 100
Formato: 15 dezenas de 01 a 25
==================================================

Sequência 0001: 01 - 03 - 05 - 07 - 09 - 11 - 13 - 15 - 17 - 19 - 21 - 23 - 24 - 25 - 02
Sequência 0002: 02 - 04 - 06 - 08 - 10 - 12 - 14 - 16 - 18 - 20 - 22 - 24 - 01 - 03 - 05
...
```

## Licença

Este projeto é de domínio público. Use livremente!
