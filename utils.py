import doctest
import datetime as dt


def parse_date(date:str)-> list:
    """
    

    Parameters
    ----------
    date : str
        Uma string de formato "numero_dia de nome_mes de ano"
        Exemplo_de_string: date = "28 de Agosto de 2023"

    Returns
    -------
    list
        A função retorna uma lista com a string repartida em itens, removendo os itens "de"
        ["nº do dia","nome_do_mês","ano"]
        Exemplo: ['28', 'de', 'Agosto', 'de', '2023']
    
    Teste com uma data qualquer no formato desejado
    >>> parse_date("28 de Agosto de 2023")
    ['28', 'Agosto', '2023']
    
    Teste com uma data inválida com número maior que o ideal
    >>> parse_date("32 de Agosto de 2023")
    Número de dia inválido
    
    Teste com uma data inválida com número menor que o ideal
    >>> parse_date("-1 de Agosto de 2023")
    Número de dia inválido

    """
    list_parsed_string = date.split(sep=' ')
    try:    
        if int(list_parsed_string[0]) > 31:
            raise ValueError
        if int(list_parsed_string[0]) < 0:
            raise ValueError
        for el in list_parsed_string:
            if el.lower() == 'de':
                list_parsed_string.remove(el)
    except ValueError:
        print("Número de dia inválido")
    else:
        return list_parsed_string




data_1 = parse_date('18 de Janeiro de 2023')
data_2 = parse_date('18 de Janeiro de 2024')

def time_delta(date_list1:list,date_list2:list)-> int:
    '''

 Parâmetros
    ----------
    date_list1 : list
        Uma lista contendo os componentes da data no formato ["dia", "nome do mês", "ano"].
    date_list2 : list
        Uma lista contendo os componentes da data no formato ["dia", "nome do mês", "ano"].

    Retorna
    -------
    int
        A diferença de tempo em dias entre as duas datas de entrada. Um valor positivo significa
        que date_list2 está após date_list1, e um valor negativo significa que date_list2 está antes de date_list1.
    
    Teste com datas que se distanciam em 1 ano
    >>> time_delta(data_1,data_2)
    365 days, 0:00:00
    
    '''
    dict_month = {"Janeiro":1, "Fevereiro":2, "Março":3, "Abril":4, 
                  "Maio":5, "Junho":6, "Julho":7, "Agosto":8, "Setembro":9, 
                  "Outubro":10, "Novembro":11, "Dezembro":12}
    dt_translated_month1 = dict_month[date_list1[1]]
    dt_translated_date1 = dt.datetime(int(date_list1[2]),dt_translated_month1,int(date_list1[0]))
    dt_translated_month2 = dict_month[date_list2[1]]
    dt_translated_date2 = dt.datetime(int(date_list2[2]),dt_translated_month2,int(date_list2[0]))

    int_delta = dt_translated_date2-dt_translated_date1
    return int_delta


if __name__ == "__main__":
    doctest.testmod(verbose=True)