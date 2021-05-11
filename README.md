# openclassroom - projet7 - algorithm & optimisation

_owner: [Amélie].(https://github/ameliebnpp)

## Developpement guide

### Dependencies

Install dependencies :
```bash
pip install requirements.txt
```

### Installation

First, clone the project:

```bash
git clone --recursive git@github.com:/amelieBNPP/openclassroom_projet7_algorithme && cd openclassroom_projet7_algorithme
```

## Optimisation

portfolio_capacity = 500€
----------------------------------------
|Share_name |share_price |share_return |
|share_1    | 5€         | 4%          |
|share_2    | 12€        | 5%          |
| ...       | ...        | ...         |
|share_n    | 21€        |  12%        |
----------------------------------------

We want to find nb_share_1, nb_share_2, ..., nb_share_n we want to buy to get the maximum return.

The optimisation should maximize : 
nb_share_1 * share_return_1 + nb_share_2 * share_return_2 + ... + nb_share_n * share_return_n 

with the following constraints :
nb_share_1, nb_share_2, ..., nb_share_n are integer
nb_share_1 * share_price_1 + nb_share_2 * share_price_2 + ... + nb_share_n * share_price_n < portfolio_capacity


### Brute force

The first part of the project is an optimisation using brut force program that means testing all solutions and choose the best one

### Optimisation

The second part of the project is to increase the speed of the process using optimiser :
- Pulp
- Scipy

