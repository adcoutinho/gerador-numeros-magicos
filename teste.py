#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Teste automatizado do gerador de números
Demonstra o funcionamento do programa
"""

from gerador_numeros import gerar_sequencias_unicas, formatar_sequencia

def teste_basico():
    """
    Teste básico do gerador
    """
    print("🧪 TESTE DO GERADOR DE NÚMEROS")
    print("=" * 50)
    
    # Teste com 3 sequências
    print("Gerando 3 sequências de teste...")
    sequencias = gerar_sequencias_unicas(3)
    
    print(f"\n✅ {len(sequencias)} sequências geradas com sucesso!")
    print("-" * 50)
    
    for i, sequencia in enumerate(sequencias, 1):
        sequencia_formatada = formatar_sequencia(sequencia)
        print(f"Sequência {i}: {sequencia_formatada}")
    
    print("-" * 50)
    print("🎉 Teste concluído com sucesso!")
    
    # Verificar se todas são diferentes
    if len(set(sequencias)) == len(sequencias):
        print("✅ Todas as sequências são únicas!")
    else:
        print("❌ Encontradas sequências duplicadas!")
    
    # Verificar se cada sequência tem 15 números
    for i, seq in enumerate(sequencias, 1):
        if len(seq) == 15:
            print(f"✅ Sequência {i} tem 15 números")
        else:
            print(f"❌ Sequência {i} tem {len(seq)} números (esperado: 15)")

if __name__ == "__main__":
    teste_basico()
