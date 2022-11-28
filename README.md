# Pet-py

> Primeiro sistema que crio, é um trabalho da faculdade em que tive que criar um sistema server side para um pet-shop, onde não era permitido utilizar banco de dados.

## Cada Class foi separada em um arquivo diferente, onde irei explicar brevemente cada uma.

## Class Clientes:

``` sh
A class Cliente é composta por criar, editar e remover cadastros que estarão armazenados em um arquivo json chamando Cliente.json.
```

## Class Servicos:

``` sh
A class Servicos é composta por criar e editar serviços que estarão armazenados em um arquivo json chamando Servicos.json, e agendar serviços que estarão armazenados no arquivo Agendamentos.json.
```

## Class Financeiro:

``` sh
A class Financeiro é composta por estoque e fluxo de caixa, onde no estoque pode-se criar, editar, excluir e exibir os produtos que estarão armazenados em um arquivo json chamando Produtos.json, e no fluxo de caixa será mostrado quanto valor está disponivel em caixa, e todas as transações realizadas.
```

## Class Menu:

``` sh
A class Menu é responsavél apenas pela exibição dos menus para cada tipo de funcionalidade no programa!
```

## Class Choices:

``` sh
A class Choices é a responsável pelo funcionamento do sistema, uma vez que é ela que dita quando cada uma das outras class serão chamadas e para qual metodo será utilizado.
```

