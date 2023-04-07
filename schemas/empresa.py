from pydantic import BaseModel
from typing import Optional, List
from models.empresa import Empresa


class EmpresaSchema(BaseModel):
    """ Define como uma nova empresa a ser inserida deve ser representada
    """

    nome:str = "XPTO"
    ramo_atuacao:str = "Óleo e gás"
    sobre:str = "Empresa que atua no ramo de upstream"
    link:str = "www.xpto.com.br"
    tamanho:int = 200


class EmpresaViewSchema(BaseModel):
    """ Define como uma empresa será retornada.
    """
    id: int = 1
    nome:str = "XPTO"
    ramo_atuacao:str = "Óleo e gás"
    sobre:str = "Empresa que atua no ramo de upstream"
    link:str = "www.xpto.com.br"
    tamanho:int = 200

class ListagemEmpresasSchema(BaseModel):
    """ Define como a lista de empresas será retornada.
    """
    empresas:list[EmpresaSchema]

def apresenta_empresa(empresa: Empresa):
    """ Retorna uma representação da empresa seguindo o schema definido em
        EmpresaViewSchema.
    """
    return {
        "id": empresa.id,
        "nome": empresa.nome,
        "ramo_atuacao": empresa.ramo_atuacao,
        "sobre": empresa.sobre,
        "link": empresa.link,
        "tamanho": empresa.tamanho
    }

def apresenta_empresas(empresas: List[Empresa]):
    """ Retorna uma representação do produto seguindo o schema definido em
        ProdutoViewSchema.
    """
    result = []
    for empresa in empresas:
        result.append({
            "id": empresa.id,
            "nome": empresa.nome,
            "ramo_atuacao": empresa.ramo_atuacao,
            "sobre": empresa.sobre,
            "link": empresa.link,
            "tamanho": empresa.tamanho,
            "vagas" : len(empresa.vagas)
        })

    return {"empresas": result}