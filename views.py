from flask import Blueprint, request, jsonify
from builder import build_query
from models import PackageRequestSchema
from marshmallow import ValidationError

main_blueprint = Blueprint('main', __name__)
FILE_NAME = 'apache_log.txt'

@main_blueprint.route('/perform_query', methods=['POST'])
def perform_query():
	# принимаем запрос от пользователя
	data = request.json

	# валидируем значения запроса
	try:
		valid_data = PackageRequestSchema().load(data)
	except ValidationError as error:
		# в ответе вернется json с номером элемента списка queriesб в котором допущена ошибка
		return jsonify(error.messages), 400

	# выполняем запрос
	result = None
	for query in valid_data['queries']:
		result = build_query(
			cmd = query['cmd'],
			value = query['value'],
			file_name = FILE_NAME,
			data = result
		)
	return jsonify(result)