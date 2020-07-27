# Retry Backoff

Lib para utilizar estratégias de retry usando Backoff e Nameko


## Instalação
Adicionar ao `requirements.txt` do projeto:

```
git+https://github.com/douglasmoraisdev/backoff_retry#egg=backoff_retry
```

OU manualmente com PIP:
```bash
$ pip install git+https://github.com/douglasmoraisdev/backoff_retry#egg=backoff_retry
```



## Configuração
A Lib utiliza `o arquivo config.yml` para sua configuração. As mesmas podem ser encontradas no arquivo 'sample.config.yml', e consumidas via arquivo .env, se for o padrão do projeto.

```yml
MAX_RETRY: 0 #numero de vezes da retentativa, 0 for infinito
MAX_RETRY_TIME: 13 #numero (fibonati), do tempo de espera máximo gerado por tentativa

```

## Importação e uso
Para utilizar o log basta importar o objeto `backoff_retry` da package e utilizar os decorators nos métodos que deseja utilizar a retentativa. Normalmente métodos de conexão a serviços externos.

#### params
* exception(optional, default=Exception): Tipo de exception a ser capturada

Exemplo:
```py
from backoff_retry import backoff_strategy

@backoff_strategy(FileException)
def algum_metodo_critico(self):
    ...

```
