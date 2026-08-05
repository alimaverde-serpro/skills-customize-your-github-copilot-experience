"""Starter code: Automação de Relatórios com Python.

Implemente os TODOs para ler vários CSVs, consolidar dados e gerar um relatório final.
"""

from __future__ import annotations

import argparse
import csv
from collections import defaultdict
from datetime import datetime
from pathlib import Path
from typing import Dict, List


def list_csv_files(input_dir: Path) -> List[Path]:
    """Retorna todos os arquivos CSV de um diretório."""
    # TODO: implementar listagem de arquivos CSV
    return []


def load_rows(csv_file: Path) -> List[dict]:
    """Carrega linhas de um CSV e retorna uma lista de dicionários."""
    rows: List[dict] = []
    # TODO: implementar leitura segura com csv.DictReader
    return rows


def parse_value(raw_value: str) -> float:
    """Converte valores como '120.50' para float, tratando erros."""
    # TODO: tratar valores inválidos sem quebrar o programa
    return float(raw_value)


def build_summary(rows: List[dict]) -> Dict[str, object]:
    """Gera métricas gerais e resumo por categoria."""
    total_records = 0
    total_value = 0.0
    by_category = defaultdict(lambda: {"count": 0, "sum": 0.0})

    # TODO: consolidar dados em total_records, total_value e by_category

    return {
        "total_records": total_records,
        "total_value": total_value,
        "by_category": dict(by_category),
    }


def write_report(summary: Dict[str, object], output_file: Path) -> None:
    """Escreve um relatório textual com os resultados da execução."""
    # TODO: gerar arquivo de relatório legível
    pass


def main() -> None:
    parser = argparse.ArgumentParser(description="Automação de Relatórios com Python")
    parser.add_argument(
        "--input-dir",
        default=".",
        help="Diretório contendo os arquivos CSV",
    )
    parser.add_argument(
        "--output",
        default="relatorio.txt",
        help="Arquivo de saída do relatório",
    )

    args = parser.parse_args()
    input_dir = Path(args.input_dir)
    output_file = Path(args.output)

    csv_files = list_csv_files(input_dir)

    all_rows: List[dict] = []
    for csv_file in csv_files:
        all_rows.extend(load_rows(csv_file))

    summary = build_summary(all_rows)

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    summary["generated_at"] = timestamp

    write_report(summary, output_file)
    print(f"Relatório gerado em: {output_file.resolve()}")


if __name__ == "__main__":
    main()
