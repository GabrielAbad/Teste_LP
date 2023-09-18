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
    date = date.strip()
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




def time_delta(data_1:str,data_2:str)-> int:
    '''

    Parameters
    ----------
    data_1 : str
        Uma string de formato "numero_dia de nome_mes de ano"
        Exemplo_de_string: date = "28 de Agosto de 2023"
    data_2 : str
        Uma string de formato "numero_dia de nome_mes de ano"
        Exemplo_de_string: date = "28 de Agosto de 2023"

    Returns
    -------
    int
        A diferença de tempo em dias entre as duas datas de entrada. Um valor positivo significa
        que data_1 está após data_2, e um valor negativo significa que data_2 está antes de data_1.
    
    Teste com datas que se distanciam em 1 ano
    >>> time_delta('18 de Janeiro de 2023','18 de Janeiro de 2024')
    datetime.timedelta(days=365)
    
    '''
    date_list1 = parse_date(data_1)
    date_list2 = parse_date(data_2)
    dict_month = {"Janeiro":1, "Fevereiro":2, "Março":3, "Abril":4, 
                  "Maio":5, "Junho":6, "Julho":7, "Agosto":8, "Setembro":9, 
                  "Outubro":10, "Novembro":11, "Dezembro":12}
    dt_translated_month1 = dict_month[date_list1[1]]
    dt_translated_date1 = dt.datetime(int(date_list1[2]),dt_translated_month1,int(date_list1[0]))
    dt_translated_month2 = dict_month[date_list2[1]]
    dt_translated_date2 = dt.datetime(int(date_list2[2]),dt_translated_month2,int(date_list2[0]))

    int_delta = dt_translated_date2-dt_translated_date1
    return int_delta

def extract_lines(s_path:str)->list:
    l_file = []
    l_file2 = []
    with open('input_text.txt') as f:
        for line in f.readlines():
            l_file.append(line)
    l_file2 = l_file[1]
    l_file = l_file[0]
    return (l_file,l_file2)

l_file = extract_lines('input_text.txt')[0]
l_file2 = extract_lines('input_text.txt')[1]
print(l_file)


if __name__ == "__main__":
    doctest.testmod(verbose=True)