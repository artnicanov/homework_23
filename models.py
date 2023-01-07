from marshmallow import Schema, ValidationError, validates_schema, fields

VALID_CMD_COMMANDS = ('filter', 'unique', 'limit', 'map', 'sort')

class RequestSchema(Schema):
	cmd = fields.Str()
	value = fields.Str()

	@validates_schema()
	def check_valid_command(self, values, *args, **kwargs):
		if values['cmd'] not in VALID_CMD_COMMANDS:
			raise ValidationError('проверьте значение команды')

class PackageRequestSchema(Schema):
	queries = fields.Nested(RequestSchema, many=True)