{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "mount_file_id": "1qMPgMVUCGsAcnMBWOET2cBkhLvNWsphu",
      "authorship_tag": "ABX9TyO0Ga1aXyy5maVvkcDbGnYH",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Peukz/extractpdf/blob/main/Extrair_PDF.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!pip install PyPDF2\n",
        "\n",
        "import PyPDF2"
      ],
      "metadata": {
        "id": "qJ6UlIM705FJ"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# abrir o arquivo PDF\n",
        "pdf_file = open('ResultadoVale.pdf', 'rb')"
      ],
      "metadata": {
        "id": "EJ41AQwz1HMt"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# criar objeto PDFReader\n",
        "pdf_reader = PyPDF2.PdfReader(pdf_file)"
      ],
      "metadata": {
        "id": "p38JnHpv41GB"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# extrair texto de todas as páginas\n",
        "for page_num in range(len(pdf_reader.pages)):\n",
        "    page = pdf_reader.pages[page_num]\n",
        "    print(page.extract_text())"
      ],
      "metadata": {
        "id": "oG4TXpix5Fge"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}