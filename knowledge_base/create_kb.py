import json

def create_knowledge_base():
    with open('data/restaurant_data.json', 'r') as f:
        restaurant_data = json.load(f)

    knowledge_base = {}
    for restaurant in restaurant_data:
        knowledge_base[restaurant['name']] = {
            'location': restaurant['location'],
            'menu_items': restaurant['menu_items'],
            'special_features': restaurant['special_features'],
            'operating_hours': restaurant['operating_hours'],
            'contact_info': restaurant['contact_info']
        }

    # Save the knowledge base
    with open('data/knowledge_base.json', 'w') as f:
        json.dump(knowledge_base, f, indent=4)

if __name__ == "__main__":
    create_knowledge_base()