
def get_connection(app):
    app.config['MYSQL_HOST'] = 'localhost'
    app.config['MYSQL_USER'] = 'charlie'
    app.config['MYSQL_PASSWORD'] = 'charlie86'
    app.config['MYSQL_DB'] = 'db_api_students'
    return app
