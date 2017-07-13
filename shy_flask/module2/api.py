from app import app


@app.route('/api/module2')
def get(self):
    return {'hello': 'world2'}