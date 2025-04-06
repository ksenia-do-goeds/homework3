from typing import Any, List, Dict, Union

def function_name(search: str, status: bool, *args: Union[int, Any], **kwargs: Dict[str, Any]) -> Union[List[int], str]:
    """
    Обрабатывает аргументы в зависимости от параметров search и status.

    Параметры:
    ----------
    search : str
        Параметр, определяющий логику обработки ('args' или 'kwargs').
    status : bool
        Определяет, как обрабатывать аргументы в *args (True - возвращает список целых чисел, 
        иначе - строку с объединенными аргументами).
    *args : Union[int, Any]
        Дополнительные позиционные аргументы, которые будут обрабатываться в зависимости от 
        значения параметров.
    **kwargs : Dict[str, Any]
        Дополнительные именованные аргументы, которые обрабатываются независимо от 
        значений status и search.

    Возвращает:
    ----------
    Union[List[int], str]
        Возвращает список целых чисел, если search равно "args" и status True,
        строку объединенных аргументов, если search равно "args" и status False,
        или строку с ключами и значениями, если search равно "kwargs".
        В случае неверного значения search вызывает ValueError.
    """
    
    result: List[int] = []
    result_2: str = ""
    
    if search == "args":
        if status:
            for i in args:
                if isinstance(i, int):
                    result.append(i)
            return result
        else:
            for i in args:
                result_2 += f"{i}"
            return result_2
    elif search == "kwargs":
        for k, v in kwargs.items():
            result_2 += "Key: {}, Value: {}; ".format(k, v)
        return result_2
    else:
        raise ValueError("Error for search")
