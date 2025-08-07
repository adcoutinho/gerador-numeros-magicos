#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de demonstração - Como usar o gerador
"""

print("""
╔══════════════════════════════════════════════════════════════╗
║                 COMO USAR O GERADOR                         ║
╚══════════════════════════════════════════════════════════════╝

🎯 OBJETIVO:
   Gerar sequências de 15 dezenas únicas de 01 a 25
   Todas as sequências são diferentes entre si

📋 COMO EXECUTAR:

   1. Execute o programa:
      python3 gerador_numeros.py

   2. Digite quantas sequências você quer:
      Exemplo: 5, 10, 100, etc.

   3. Confirme a geração digitando 's'

   4. As sequências serão exibidas na tela

   5. Para muitas sequências, você pode salvar em arquivo

╔══════════════════════════════════════════════════════════════╗
║                      EXEMPLO DE USO                         ║
╚══════════════════════════════════════════════════════════════╝

$ python3 gerador_numeros.py

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
Sequência 0001: 01 - 05 - 07 - 09 - 11 - 13 - 15 - 17 - 19 - 20 - 21 - 22 - 23 - 24 - 25
Sequência 0002: 02 - 04 - 06 - 08 - 10 - 12 - 14 - 16 - 18 - 19 - 20 - 21 - 23 - 24 - 25
...

✅ Processo concluído! 5 sequências únicas geradas.

╔══════════════════════════════════════════════════════════════╗
║                     CARACTERÍSTICAS                         ║
╚══════════════════════════════════════════════════════════════╝

✨ Cada sequência tem exatamente 15 números
🎯 Números sempre entre 01 e 25
🔢 Números sempre únicos dentro de cada sequência
📊 Todas as sequências são diferentes entre si
💾 Opção de salvar em arquivo para muitas sequências
🛡️ Validação robusta de entrada
🎨 Interface amigável e colorida

╔══════════════════════════════════════════════════════════════╗
║                      ARQUIVOS CRIADOS                       ║
╚══════════════════════════════════════════════════════════════╝

📄 gerador_numeros.py  - Programa principal
📄 teste.py           - Script de teste automatizado
📄 README.md          - Documentação completa
📄 demonstracao.py    - Este arquivo de demonstração

╔══════════════════════════════════════════════════════════════╗
║                     PRONTO PARA USAR!                       ║
╚══════════════════════════════════════════════════════════════╝

Execute agora: python3 gerador_numeros.py

""")
