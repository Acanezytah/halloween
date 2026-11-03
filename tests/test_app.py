from app import app
from entities.monster import Monster


def test_save_monster(monkeypatch):
    saved_monsters = []

    def fake_save(monster):
        saved_monsters.append((monster.name, monster.power))

    monkeypatch.setattr(Monster, 'save', fake_save)

    response = app.test_client().post(
        '/monster',
        data={'name': 'eso tilin', 'power': 'el pepe'}
    )

    assert response.status_code == 302
    assert response.headers['Location'] == '/'
    assert saved_monsters == [('eso tilin', 'el pepe')]
