# Jogo da Forca Funcional (Python & Clojure)

![Demonstração do Jogo](demo.gif)

## 📖 Sobre o Projeto

Este projeto é uma implementação do clássico **Jogo da Forca** para o terminal, desenvolvido com uma abordagem estritamente funcional em duas linguagens diferentes: Python e Clojure.

O objetivo principal foi explorar e aplicar na prática os conceitos fundamentais da programação funcional, como **funções puras**, **imutabilidade** e a **separação de responsabilidades** (isolando a lógica de negócio dos efeitos colaterais de entrada e saída).

## ✨ Funcionalidades & Conceitos

* **Lógica de Jogo Pura:** Todas as regras do jogo (processar um palpite, verificar vitória/derrota, etc.) são contidas em funções puras, sem efeitos colaterais.
* **Estado Imutável:** O estado do jogo nunca é modificado. A cada jogada, um novo estado é gerado e passado para a próxima iteração do loop principal.
* **Separação de I/O:** As funções que interagem com o terminal (imprimindo na tela e lendo a entrada do usuário) são completamente separadas da lógica do jogo.
* **Implementação Dupla:** O mesmo design foi aplicado em duas linguagens para comparar como os princípios funcionais se manifestam em um ambiente multiparadigma (Python) e em um ambiente funcional por natureza (Clojure).

## 🚀 Como Executar

Para rodar o projeto, clone este repositório e siga os passos abaixo para a versão desejada.

### Versão em Python

1.  Navegue até a pasta `python`:
    ```sh
    cd python
    ```
2.  Execute o jogo com o seguinte comando:
    ```sh
    python3 main.py
    ```

### Versão em Clojure

1.  Certifique-se de ter o [Babashka](https://babashka.org/) instalado em seu sistema.
2.  Navegue até a pasta `clojure`:
    ```sh
    cd clojure
    ```
3.  Execute o jogo com o seguinte comando:
    ```sh
    bb hangman.clj
    ```

## 🛠️ Tecnologias Utilizadas

* **Python 3**
* **Clojure**
* **Babashka** (como interpretador de scripts Clojure)