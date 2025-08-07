#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gerador de Números Aleatórios
Gera sequências de 15 dezenas únicas de 01 a 25
Todas as sequências geradas são diferentes entre si
"""

import random
import sys


def gerar_sequencia():
    """
    Gera uma sequência de 15 números únicos entre 1 e 25
    
    Returns:
        tuple: Sequência ordenada de 15 números únicos
    """
    numeros = random.sample(range(1, 26), 15)
    return tuple(sorted(numeros))


def formatar_sequencia(sequencia):
    """
    Formata a sequência de números com zero à esquerda
    
    Args:
        sequencia (tuple): Sequência de números
        
    Returns:
        str: Sequência formatada
    """
    numeros_formatados = [f"{num:02d}" for num in sequencia]
    return " - ".join(numeros_formatados)


def gerar_sequencias_unicas(quantidade):
    """
    Gera a quantidade especificada de sequências únicas
    
    Args:
        quantidade (int): Número de sequências a gerar
        
    Returns:
        list: Lista de sequências únicas
    """
    sequencias = set()
    tentativas = 0
    max_tentativas = quantidade * 1000  # Limite de segurança
    
    print(f"Gerando {quantidade} sequências únicas...")
    
    while len(sequencias) < quantidade and tentativas < max_tentativas:
        nova_sequencia = gerar_sequencia()
        sequencias.add(nova_sequencia)
        tentativas += 1
        
        # Mostra progresso a cada 10% das sequências geradas
        if len(sequencias) % max(1, quantidade // 10) == 0:
            progresso = (len(sequencias) / quantidade) * 100
            print(f"Progresso: {progresso:.0f}% ({len(sequencias)}/{quantidade})")
    
    if len(sequencias) < quantidade:
        print(f"⚠️  Atenção: Só foi possível gerar {len(sequencias)} sequências únicas.")
        print(f"   Com 15 números de 1-25, existem aproximadamente 3.268.760 combinações possíveis.")
    
    return list(sequencias)


def validar_entrada():
    """
    Valida e obtém a quantidade de sequências desejada do usuário
    
    Returns:
        int: Quantidade válida de sequências
    """
    while True:
        try:
            entrada = input("\nQuantas sequências você deseja gerar? ")
            quantidade = int(entrada)
            
            if quantidade <= 0:
                print("❌ Por favor, digite um número maior que zero.")
                continue
                
            if quantidade > 1000000:
                print("❌ Número muito alto. Por favor, escolha um valor até 1.000.000.")
                continue
                
            return quantidade
            
        except ValueError:
            print("❌ Por favor, digite apenas números inteiros.")
        except KeyboardInterrupt:
            print("\n\n👋 Programa cancelado pelo usuário.")
            sys.exit(0)


def main():
    """
    Função principal do programa
    """
    print("=" * 60)
    print("🎲 GERADOR DE NÚMEROS ALEATÓRIOS")
    print("=" * 60)
    print("📋 Gera sequências de 15 dezenas únicas de 01 a 25")
    print("✨ Todas as sequências são diferentes entre si")
    print("=" * 60)
    
    try:
        # Obter quantidade desejada
        quantidade = validar_entrada()
        
        # Confirmar geração
        print(f"\n🎯 Vou gerar {quantidade} sequência(s) única(s).")
        confirma = input("Deseja continuar? (s/n): ").lower().strip()
        
        if confirma not in ['s', 'sim', 'y', 'yes']:
            print("👋 Operação cancelada.")
            return
        
        print("\n" + "=" * 60)
        
        # Gerar sequências
        sequencias = gerar_sequencias_unicas(quantidade)
        
        # Exibir resultados
        print(f"\n🎉 {len(sequencias)} sequências geradas com sucesso!")
        print("=" * 60)
        
        for i, sequencia in enumerate(sequencias, 1):
            sequencia_formatada = formatar_sequencia(sequencia)
            print(f"Sequência {i:04d}: {sequencia_formatada}")
        
        print("=" * 60)
        print(f"✅ Processo concluído! {len(sequencias)} sequências únicas geradas.")
        
        # Opção de salvar em arquivo
        if len(sequencias) > 10:
            salvar = input("\n💾 Deseja salvar as sequências em um arquivo? (s/n): ").lower().strip()
            if salvar in ['s', 'sim', 'y', 'yes']:
                salvar_arquivo(sequencias)
        
    except KeyboardInterrupt:
        print("\n\n👋 Programa interrompido pelo usuário.")
    except Exception as e:
        print(f"\n❌ Erro inesperado: {e}")


def salvar_arquivo(sequencias):
    """
    Salva as sequências em um arquivo de texto
    
    Args:
        sequencias (list): Lista de sequências para salvar
    """
    try:
        nome_arquivo = f"sequencias_geradas_{len(sequencias)}.txt"
        
        with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
            arquivo.write("SEQUÊNCIAS DE NÚMEROS GERADAS\n")
            arquivo.write("=" * 50 + "\n")
            arquivo.write(f"Total de sequências: {len(sequencias)}\n")
            arquivo.write(f"Formato: 15 dezenas de 01 a 25\n")
            arquivo.write("=" * 50 + "\n\n")
            
            for i, sequencia in enumerate(sequencias, 1):
                sequencia_formatada = formatar_sequencia(sequencia)
                arquivo.write(f"Sequência {i:04d}: {sequencia_formatada}\n")
        
        print(f"✅ Sequências salvas no arquivo: {nome_arquivo}")
        
    except Exception as e:
        print(f"❌ Erro ao salvar arquivo: {e}")


if __name__ == "__main__":
    main()
