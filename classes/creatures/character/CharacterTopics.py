from classes.dialogue.Topic import Topic


class CharacterTopics:
    
    def __init__(self):
        self.topics = {}
        pass
    
    def get_topic(self, topic_name: str) -> Topic:
        return self.topics[topic_name]
    
    def set_topic(self, topic_name: str, topic: Topic) -> None:
        self.topics[topic_name] = topic
