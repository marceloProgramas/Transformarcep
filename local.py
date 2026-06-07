import pandas as pd
import transform
import enviar

def main():
    caminho_arquivo = "planilha.xlsx"
    df = pd.read_excel(caminho_arquivo)
    linhas = len(df)
    for Lin in range(linhas):
            
            enviar.salvar_local(
            str(df.loc[Lin,'nome']),
            str(df.loc[Lin,'endereço']),
            transform.transform(str(df.loc[Lin,'cep'])),
            str(df.loc[Lin,'horario']),
            str(df.loc[Lin,'obs'])                   
            )
    
main()