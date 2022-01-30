# API EvoCondo
### Desenvolvido em Django 
___
### Para rodar o Ambiente vitual e dependencias: 
###### Não Rodar no Pycharm(rodar na pasta raiz)

~~~
core\venv\Scripts\Activate
~~~

### Rodar Servidor
###### Não Rodar no Pycharm(rodar na pasta raiz)
~~~
python manage.py runserver
~~~

<details><summary>Residents Request</summary>
<p>

#### 
~~~json
{
    "rg": "",
    "cpf": "",
    "telefone": "",
    "name": "",
    "block": "",
    "apartament": "",
    "expiration": null,
    "last_access": null,
    "familyID": null
}
~~~

</p>
</details>

<details><summary>Garage Request</summary>
<p>

#### 
~~~json
{
    "rg": "",
    "name": "",
    "number": "",
    "vieicle": "",
    "model": "",
    "license": ""
}
~~~

</p>
</details>

<details><summary>Operator Request</summary>
<p>

#### 
~~~json
{
    "rg": "",
    "cpf": "",
    "telefone": "",
    "name": "",
    "birthday": null,
    "permissions": "",
    "administratorSystem": false
}
~~~

</p>
</details>

<details><summary>Visitor Request</summary>
<p>

#### 
~~~json
{
    "rg": "",
    "cpf": "",
    "telefone": "",
    "name": "",
    "block": "",
    "apartament": "",
    "expiration": null,
    "last_access": null
}
~~~

</p>
</details>
