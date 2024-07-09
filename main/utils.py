from django.db.models import Q

def q_search(obj, search: str) -> Q:
    """
    Возвращает Q - объект для поиска товара по имени и описанию
    
    Args:
        obj: QuerySet
        search: str
        
    Returns:
        Q - object
    """
    res_q = Q()
    for word in search.split():
        res_q |= Q(name__icontains=word)
        res_q |= Q(description__icontains=word)
    return res_q