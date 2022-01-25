from kivy.properties import StringProperty

from components.cards.fake_card import FakeCard


class FriendCard(FakeCard):
    online = StringProperty("online")
    name = StringProperty()
    avatar = StringProperty()
