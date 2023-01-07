def filter_query(value, data):
	""" возвращает строки файла, которые содержат нужное знаечение"""
	return filter(lambda x: value in x, data)

def unique_query(data, *args, **kwargs):
	""" возвращает только уникальные значение"""
	return set(data)

def limit_query(value, data):
	""" возвращает ограниченную выборку"""
	limit: int = int(value)
	return list(data)[:limit]

def map_query(value, data):
	"""возвращает только одну колонку из файла"""
	col_number = int(value)
	return map(lambda x: x.split(" ")[col_number], data)

def sort_query(value, data):
	""" сортирует результат по убыванию или возрастанию"""
	reverse = value == "desc"
	return sorted(data, reverse=reverse)
