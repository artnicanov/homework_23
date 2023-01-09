import re
from typing import Iterable

def filter_query(value: str, data: Iterable[str]):
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

def regex_query(value, data):
	""" возвращает строки файла, которые содержат регулярное выражение """
	pattern = re.compile(value)
	return filter(lambda x: re.search(pattern, x), data)
