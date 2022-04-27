
from .context import app, json

def test_add_user():
    
    with app.test_client() as client:
        response = client.post(
            '/users',
            data=json.dumps(dict(
                first_name='saloni',
                last_name='sinha'
                
            )),
            content_type='application/json',
        )
        assert response.status_code == 201
        