import pandas as pd
import matplotlib.pyplot as plt

if __name__ == '__main__':
    df = pd.read_csv('./dados_vendas.csv')
    # Questão 1
    df.loc[df['Região'] == 'Norde', 'Região'] = 'Norte'
    df.loc[df['Região'] == 'Sd', 'Região'] = 'Sul'


    # Questão 2
    df_vendas_validas = df[
        pd.to_numeric(df['Quantidade'], errors='coerce').notnull() & pd.to_numeric(df['Valor_Unitário'],
                                                                                   errors='coerce').notnull() & pd.to_numeric(
            df['Desconto'], errors='coerce').notnull()
        ]
    df_vendas_validas.loc[:, 'Valor_Total'] = (pd.to_numeric(df_vendas_validas['Quantidade'],
                                                                    errors='coerce') * pd.to_numeric(
                                                  df_vendas_validas['Valor_Unitário'],
                                                  errors='coerce')) - pd.to_numeric(df_vendas_validas['Desconto'],
                                                                                    errors='coerce'
                                                                                    )
    # Questão 3
    vendas_por_produto = df_vendas_validas.groupby('Produto')['Valor_Total'].sum()

    plt.figure(figsize=(10, 6))
    vendas_por_produto.plot(kind='bar', color='skyblue')
    plt.title('Total de Vendas X Produto')
    plt.xlabel('Produto')
    plt.ylabel('R$ Vendas')
    plt.xticks(rotation=0)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()

    plt.show()

    print(df)
