# 📘 Assignment: Jogo da Forca

## 🎯 Objetivo

Construir o clássico jogo da Forca em Python, praticando manipulação de strings, loops e condicionais.
Ao final, o aluno deverá implementar o fluxo completo de uma partida com regras de vitória e derrota.

## 📝 Tarefas

### 🛠️ Implementar o jogo da Forca

#### Descrição
Desenvolva um programa que selecione uma palavra aleatória e permita ao jogador adivinhar letras até vencer ou perder por falta de tentativas.

#### Requisitos
O programa concluído deve:

- Selecionar uma palavra aleatoriamente a partir de uma lista predefinida.
- Aceitar palpites de uma letra por vez e atualizar a palavra oculta no formato `_ _ _`.
- Rastrear e exibir o número de tentativas incorretas restantes.
- Encerrar o jogo quando a palavra for adivinhada ou quando as tentativas acabarem.
- Exibir mensagens claras de vitória e derrota ao final da partida.

Exemplo de execução:
```text
Palavra: _ _ _ _ _
Digite uma letra: a
Boa tentativa! Palavra: _ a _ _ a
Tentativas restantes: 5

Digite uma letra: z
Letra incorreta.
Tentativas restantes: 4
```