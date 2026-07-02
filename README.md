# 💻 Sistema de Cadastro em Python

Um sistema interativo de linha de comando (CLI) desenvolvido em Python para gerenciar o cadastro de pessoas, com foco em persistência de dados e modularização.

## 📖 Sobre o Projeto

Este projeto foi construído como parte do aprofundamento prático em fundamentos essenciais da programação. O objetivo principal foi criar uma aplicação funcional do zero, saindo da teoria e aplicando conceitos avançados de estruturação de código, manipulação de arquivos e tratamento preventivo de erros.

## 🚀 Funcionalidades

- **Menu Interativo:** Interface limpa e amigável direto no terminal.
- **Validação de Dados:** Tratamento de erros robusto para garantir que o usuário digite os tipos corretos de dados (ex: números para idade, opções válidas no menu).
- **Persistência em Arquivo:** Os dados cadastrados (nome e idade) são salvos permanentemente em um arquivo `.txt` (`pessoas.txt`), garantindo que não sejam perdidos ao encerrar o sistema.
- **Criação Automática de Infraestrutura:** Se o arquivo de banco de dados não existir na primeira execução, o sistema se encarrega de criá-lo automaticamente.
- **Leitura Formatada:** Exibição dos cadastros tabulados de forma organizada no terminal.

## 🛠️ Tecnologias e Conceitos Aplicados

- **Python 3**
- Modularização e criação de pacotes (`__init__.py`)
- Manipulação de arquivos I/O (`open`, modos `rt` e `at`)
- Estruturas de repetição com pontos de interrupção (`while True`, `break`)
- Tratamento de Exceções (`try`, `except`, `else`, `finally`)
- Formatação avançada de f-strings

## 📁 Estrutura de Diretórios

O projeto foi organizado separando a lógica principal das funções auxiliares:

```text
sistema/
│
├── lib/
│   ├── arquivo/
│   │   └── __init__.py    # Lógica de leitura e gravação no .txt
│   │
│   └── interface/
│       └── __init__.py    # Lógica de menus, formatação visual e inputs
│
├── pessoas.txt            # Arquivo gerado pelo sistema (Banco de Dados)
├── siste.py               # Script principal (Ponto de entrada)
└── README.md