"""Módulo 4 — Visualização de Dados.

Complete cada função com o apoio do GitHub Copilot. Cada função deve **gerar um
gráfico e salvá-lo** no caminho ``out_path`` (formato PNG). Use ``matplotlib`` e
``seaborn``. Em ambientes sem interface gráfica (CI), mantenha o backend "Agg".

Valide com:  ``python lab/check.py --module viz``
"""
from __future__ import annotations

import matplotlib

matplotlib.use("Agg")  # backend sem interface gráfica (funciona no CI)
import matplotlib.pyplot as plt  # noqa: E402
import pandas as pd  # noqa: E402
import seaborn as sns  # noqa: E402


def plot_rating_distribution(df: pd.DataFrame, out_path: str):
    """Histograma da distribuição da coluna ``rating``. Inclua título e labels em
    português e salve a figura em ``out_path``."""
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.histplot(df["rating"], bins=20, ax=ax)
    ax.set_title("Distribuição das notas (rating)")
    ax.set_xlabel("Nota (rating)")
    ax.set_ylabel("Quantidade de vinhos")
    fig.savefig(out_path, dpi=100, bbox_inches="tight")
    plt.close(fig)
    return fig


def plot_top_varieties(df: pd.DataFrame, out_path: str):
    """Gráfico de barras horizontais com as 10 variedades (``variety``) com maior
    quantidade de vinhos. Salve a figura em ``out_path``."""
    contagens = df["variety"].value_counts().head(10)
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.barh(contagens.index, contagens.values)
    ax.invert_yaxis()  # maior quantidade no topo
    ax.set_title("Top 10 variedades por quantidade de vinhos")
    ax.set_xlabel("Quantidade de vinhos")
    ax.set_ylabel("Variedade")
    fig.savefig(out_path, dpi=100, bbox_inches="tight")
    plt.close(fig)
    return fig


def plot_boxplot_by_variety(df: pd.DataFrame, out_path: str):
    """Boxplot de ``rating`` para as 5 variedades mais frequentes. Limitar a 5
    variedades mantém o gráfico legível. Salve a figura em ``out_path``."""
    top5 = df["variety"].value_counts().head(5).index
    subconjunto = df[df["variety"].isin(top5)]
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.boxplot(data=subconjunto, x="variety", y="rating", order=top5, ax=ax)
    ax.set_title("Distribuição de rating nas 5 variedades mais frequentes")
    ax.set_xlabel("Variedade")
    ax.set_ylabel("Nota (rating)")
    fig.savefig(out_path, dpi=100, bbox_inches="tight")
    plt.close(fig)
    return fig

