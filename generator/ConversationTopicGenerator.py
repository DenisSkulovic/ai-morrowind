# TODO add labels and generation for some topics like for religion, politics,... anything else?
import random


class ConversationTopicGenerator:
    def __init__(self, character):
        self.character = character

    def generateGenericTopics(self):
        # Generic topics that any character might know about
        generic_topics = ['weather', 'current events', 'local rumors', 'recent news']
        return self.categorize_topics(generic_topics)

    def generateBiographyTopics(self):
        # Topics based on the character's biography
        biography_topics = [self.character.biography_fact_enum.get(fact, "") for fact in self.character.biography]
        return self.categorize_topics(biography_topics)

    def generatePersonalityTraitsTopics(self):
        # Topics based on the character's personality traits
        personality_topics = self.character.personality_traits
        return self.categorize_topics(personality_topics)

    def generateBackgroundTopics(self):
        # Topics based on the character's background
        background_topics = [self.character.background_type_enum.get(bg, "") for bg in self.character.background]
        return self.categorize_topics(background_topics)

    def categorize_topics(self, topics):
        # Categorize topics into interested, indifferent, bored, knows nothing about
        interested = []
        indifferent = []
        bored = []
        knows_nothing = []

        for topic in topics:
            if self.is_interested_in_topic(topic):
                interested.append(topic)
            elif self.is_indifferent_to_topic(topic):
                indifferent.append(topic)
            elif self.is_bored_with_topic(topic):
                bored.append(topic)
            else:
                knows_nothing.append(topic)

        return {"interested": interested, "indifferent": indifferent, "bored": bored, "knows_nothing": knows_nothing}

    def is_interested_in_topic(self, topic):
        # Determine if the character is interested in the topic
        # Placeholder logic - customize as needed
        return random.choice([True, False])

    def is_indifferent_to_topic(self, topic):
        # Determine if the character is indifferent to the topic
        # Placeholder logic - customize as needed
        return random.choice([True, False])

    def is_bored_with_topic(self, topic):
        # Determine if the character is bored with the topic
        # Placeholder logic - customize as needed
        return random.choice([True, False])
