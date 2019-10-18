# MacLabel
## Sistema simples para criação de etiquetas utilizando Django


## Como rodar o projeto?

* Clone esse repositório.
* Crie um virtualenv com Python 3.
* Ative o virtualenv.
* Instale as dependências.
* Rode as migrações.

```
git clone https://github.com/robertaponzio/macmilianetiqueta.git
cd macmilianetiqueta
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
python contrib/env_gen.py
python manage.py migrate
```

### Populando o banco de dados

- Cria usuário
```
python manage.py createsuperuser --username dev --email dev@foo.bar
```

### Rodando no servidor local
```
python manage.py runserver
```
