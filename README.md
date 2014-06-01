Python .env to .yml
=====================

A simple script to generate a `.yml` file from a `.env` file. 


Usage
-----
Assumes existence of `.env` and will generate `env.yml`.    
Both the `.env` and `.yml` filepaths can be specified with `-e` and `-y`, respectively.

```shell
python env-to-yml.py
python env-to-yml.py -e config/.env -y config/vars.yml
```

