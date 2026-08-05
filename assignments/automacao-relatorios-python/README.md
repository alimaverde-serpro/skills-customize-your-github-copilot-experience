# 📘 Assignment: Automação de Relatórios com Python

## 🎯 Objective

Construir um script de automação em Python para consolidar dados de múltiplos arquivos CSV e gerar um relatório final reutilizável. O foco é transformar uma tarefa manual em um fluxo executável e verificável.

## 📝 Tasks

### 🛠️ Ler arquivos CSV de uma pasta

#### Descrição
Implemente a etapa inicial do pipeline: localizar arquivos CSV em uma pasta de entrada e carregar seus registros com segurança.

#### Requisitos
O programa completo deve:

- Receber o diretório de entrada por argumento de linha de comando
- Encontrar automaticamente todos os arquivos com extensão `.csv`
- Ignorar arquivos inválidos ou vazios sem interromper toda a execução


### 🛠️ Calcular métricas consolidadas

#### Descrição
A partir dos registros lidos, consolide informações para gerar indicadores úteis de acompanhamento.

#### Requisitos
O programa completo deve:

- Calcular o total de registros processados
- Calcular o total acumulado da coluna `valor`
- Gerar um resumo por categoria (contagem e soma por `categoria`)


### 🛠️ Gerar relatório final em arquivo

#### Descrição
Converta os resultados da consolidação em um relatório textual salvo em disco, pronto para avaliação prática.

#### Requisitos
O programa completo deve:

- Criar um arquivo de saída com data/hora da execução
- Escrever as métricas gerais e o resumo por categoria em formato legível
- Exibir no terminal o caminho do relatório gerado ao finalizar
