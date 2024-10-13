{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMaulp25gVp6FWjBJnhjj3T",
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
        "<a href=\"https://colab.research.google.com/github/apoorvakote/apoorvamusic/blob/main/basicloop.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ZZzrntjXOxfD",
        "outputId": "0fd31911-0181-4d1b-f9b2-020c2e4876c9"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "pin>> 4567\n",
            "incorrect pin\n"
          ]
        }
      ],
      "source": [
        "pin=int(input(\"pin>> \"))\n",
        "if pin==1234:\n",
        "  print(\"correct pin\")\n",
        "else:\n",
        "  print(\"incorrect pin\")"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "pin=1234\n",
        "trials=0\n",
        "print(\"enter pin\")\n",
        "\n",
        "while trials<=3:\n",
        "  input_pin=int(input(f\"trials-{trials} | pin: \"))\n",
        "  trials+=1\n",
        "  if input_pin==pin:\n",
        "    print(\"correct\")\n",
        "    trials=+1\n",
        "    break\n",
        "else:\n",
        "  print(\"incorrect\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "iq5hmSY2PsbS",
        "outputId": "ec1650d6-fc43-4949-ca3d-645f42592557"
      },
      "execution_count": 16,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "enter pin\n",
            "trials-0 | pin: 4568\n",
            "trials-1 | pin: 1234\n",
            "correct\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "OXnr4JrOUx0D"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}