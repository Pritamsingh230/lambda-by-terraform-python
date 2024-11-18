def lambda_handler(event, context):
    name = event.get('key1', 'there')
    message = 'Hello {} !'.format(name)
    return {
        'message': message
    }
