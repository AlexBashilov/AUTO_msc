import requests
import uuid


PostParams = {
    'item_name': 'Kiska',
    'guid': str(uuid.uuid4()),
    'description': 'Opisani piton',
}

res = requests.post('http://localhost:8080/book_cost_items/create', json=PostParams)
response = res.json()
print(response)


def test_create_item():
    assert res.status_code == 201
    return True

if __name__ == '__main__':
    if test_create_item():
        print("Элемент успешно создан")
    else:
        print("Ошибка при создании элемента")