from classes.creatures.character.Character import Character


class ConversationManager:
    def __init__(self, topic_switch_threshold=3):
        self.current_conversation = None
        self.topic_switch_threshold = topic_switch_threshold

    def start_conversation(self, character1: Character, character2: Character):
        self.current_conversation = {
            "participants": [character1, character2],
            "current_topic": None,
            "history": [], # TODO add logic that after each response, the response topic and summary (gpt generated) will be stored here. When the conversation is ended, the topics on each participant will be updated with the history, according to topic importance. If a character has no such topic on him - nothng to record, signifying that they wont remember anything because they are not interested. Or maybe just make it very quick and easy for them to forget topics that are not inherently interesting to them, modified for personality traits like for good memory, curiosity, intelligence, etc.
            "character1_scores": {
                'enlightening': 0,
                'enjoyable': 0,
                'tense': 0,
                'boring': 0,
                'confusing': 0
            },
            "character2_scores": {
                'enlightening': 0,
                'enjoyable': 0,
                'tense': 0,
                'boring': 0,
                'confusing': 0
            }
        }
        self.select_next_topic(character1)  # Start with character1 for example

    def select_next_topic(self, character: Character):
        relevant_topics = character.topics  # Assuming each character has their own list of topics

        # Filter topics that are still interesting
        interesting_topics = [topic for topic in relevant_topics if topic.is_still_interesting()]

        if not interesting_topics:
            self.end_conversation()
            return

        # Select the most interesting topic based on interest level and importance
        most_interesting_topic = max(
            interesting_topics, 
            key=lambda topic: topic.interest_level + topic.importance - topic.discussed_score,
            default=None
        )

        if most_interesting_topic:
            self.current_conversation["current_topic"] = most_interesting_topic
            most_interesting_topic.discuss()
            print(f"{character.name} switches to a new topic: {most_interesting_topic.name}")
        else:
            print(f"{character.name} continues discussing: {self.current_conversation['current_topic'].name}")

        # Switch the roles of speaker and listener
        self.switch_speaker_and_listener()

    def switch_speaker_and_listener(self):
        self.current_conversation["participants"].reverse()  # Switches the first and second elements

    def continue_conversation(self):
        current_speaker, listener = self.get_speaker_and_listener()

        if self.decide_to_exit_conversation(current_speaker):
            self.end_conversation()
            return

        if self.decide_to_switch_topic(current_speaker):
            self.select_next_topic(current_speaker)
        else:
            self.respond_to_topic(current_speaker, listener)

    def get_speaker_and_listener(self):
        # Returns the current speaker and the listener
        participants = self.current_conversation["participants"]
        speaker = participants[0]  # Assuming the first in the list is the current speaker
        listener = participants[1] if len(participants) > 1 else None
        return speaker, listener

    # TODO it should decide to exit conversation on more factors, like personal traits (compassion - lengthen conversation, some other trait will shorten), talkativeness, mood, overall length of this conversation, and if so far it has been enlightening/enjoyable enough, and not tense/boring/confusing (a ratio of positive/negative experiences?)
    # TODO just ask Chat GPT what would be some natural reasons to end a conversation without exhausting all interesting topics, and then how to model it with the ConversationManager and Character and Topic
    def decide_to_exit_conversation(self, speaker):
        # Example logic: speaker might exit if in a bad mood
        if speaker.current_mood == 'irritated' or speaker.current_mood == 'tired':
            return True
        return False

    def decide_to_switch_topic(self, speaker: Character):
        current_topic = self.current_conversation["current_topic"]
        if not current_topic:
            return True  # If no current topic, choose one

        # Find the next most interesting topic
        next_topic = self.find_next_interesting_topic(speaker)

        if next_topic and self.is_significant_difference(current_topic, next_topic):
            return True

        return False
    
    def find_next_interesting_topic(self, speaker: Character):
        # Assuming each character has their own list of topics
        relevant_topics = speaker.topics
        interesting_topics = [topic for topic in relevant_topics if topic.is_still_interesting()]

        # Exclude the current topic
        interesting_topics = [t for t in interesting_topics if t != self.current_conversation["current_topic"]]

        if not interesting_topics:
            return None

        # Select the most interesting topic based on interest level and importance
        return max(interesting_topics, key=lambda topic: topic.interest_level + topic.importance - topic.discussed_score, default=None)

    def is_significant_difference(self, current_topic, next_topic):
        current_interest = current_topic.interest_level + current_topic.importance - current_topic.discussed_score
        next_interest = next_topic.interest_level + next_topic.importance - next_topic.discussed_score
        return (next_interest - current_interest) >= self.topic_switch_threshold


    def respond_to_topic(self):
        current_speaker, listener = self.get_speaker_and_listener()
        
        # Logic for current speaker to respond to the current topic
        # Placeholder for actual response generation logic
        print(f"{current_speaker.name} responds to the topic: {self.current_conversation['current_topic'].name}")

        # Switch the roles of speaker and listener
        self.switch_speaker_and_listener()

    def update_conversation_score(self, speaker: Character, listener: Character, topic):
        # Determine which score set belongs to the speaker and listener
        if speaker == self.current_conversation["participants"][0]:
            speaker_scores = self.current_conversation["character1_scores"]
            listener_scores = self.current_conversation["character2_scores"]
        else:
            speaker_scores = self.current_conversation["character2_scores"]
            listener_scores = self.current_conversation["character1_scores"]

        # Update scores based on speaker's interaction with the topic
        self.adjust_scores_based_on_interaction(speaker_scores, speaker, topic)

        # Update scores based on listener's reaction to the topic
        self.adjust_scores_based_on_interaction(listener_scores, listener, topic)
        
    def adjust_scores_based_on_interaction(self, scores, character: Character, topic, chosen_by_other):
        # Assess the topic based on the character's perception, not just its inherent interest level
        perceived_interest = self.assess_topic_interest(character, topic, chosen_by_other)

        # Example scoring logic based on personality traits
        if 'Curious' in character.personality_traits and perceived_interest > 5:
            scores['enlightening'] += 1
        if 'Compassionate' in character.personality_traits and topic.name == 'Helping Others':
            scores['enjoyable'] += 1
        if 'Cautious' in character.personality_traits and perceived_interest < 3:
            scores['tense'] += 1
        # ... Additional conditions and logic as needed ...


    def end_conversation(self, abrupt=False):
        speaker, listener = self.get_speaker_and_listener()

        if not abrupt:
            speaker_assessment = self.get_conversation_assessment(speaker)
            speaker_response = self.generate_parting_response(speaker, speaker_assessment)
            print(f"{speaker.name} says: \"{speaker_response}\"")

            if listener and self.listener_wants_to_respond(listener):
                listener_assessment = self.get_conversation_assessment(listener)
                listener_response = self.generate_parting_response(listener, listener_assessment)
                print(f"{listener.name} says: \"{listener_response}\"")

        self.current_conversation = None
        
    def get_conversation_assessment(self, character: Character):
        # Determine the assessment of the conversation for a specific character
        if character == self.current_conversation["participants"][0]:
            scores = self.current_conversation["character1_scores"]
        else:
            scores = self.current_conversation["character2_scores"]

        return max(scores, key=scores.get)

    def assess_interest_in_topic(self, character: Character, topic, chosen_by_other):
        # Check if the topic exists in the character's list and get the base interest
        if chosen_by_other:
            base_interest = self.find_base_interest_in_character_topics(character, topic)
        else:
            base_interest = self.calculate_personal_interest(character, topic)

        # Adjust interest based on character's personality traits and mood
        interest_adjustment = self.calculate_interest_adjustment(character, topic)

        # Calculate final perceived interest
        perceived_interest = base_interest + interest_adjustment
        return max(0, min(perceived_interest, 10))  # Ensure it stays within 0-10 range

    def find_base_interest_in_character_topics(self, character: Character, topic):
        # Search for the topic in character's list and return its interest level
        for character_topic in character.topics:
            if character_topic.name == topic.name:
                return (character_topic.interest_level + character_topic.importance) / 2
        # If topic is not found, use calculate_personal_interest
        return self.calculate_personal_interest(character, topic)

    def calculate_interest_adjustment(self, character: Character, topic):
        interest_adjustment = 0
        if "Curious" in character.personality_traits:
            interest_adjustment += 1
        if "Cautious" in character.personality_traits:
            interest_adjustment -= 1
        # ... other trait adjustments ...

        # Mood adjustments
        if character.current_mood == "happy":
            interest_adjustment += 0.5
        elif character.current_mood == "irritated":
            interest_adjustment -= 0.5
        # ... other mood adjustments ...

        return interest_adjustment

    def generate_parting_response(self, character: Character, assessment):
        # Generate a parting response based on the conversation's assessment and character's personality
        # Example responses
        if assessment == 'enlightening':
            return "That was a truly insightful conversation."
        elif assessment == 'enjoyable':
            return "I had a great time talking with you."
        elif assessment == 'tense':
            return "This conversation was quite intense."
        elif assessment == 'boring':
            return "Well, I suppose we had an alright chat."
        elif assessment == 'confusing':
            return "I'm not quite sure what to make of our discussion."
        # ... Additional responses based on character's personality traits

        # Default response if no specific case applies
        return "Thank you for the conversation."
    

    def calculate_personal_interest(self, character: Character, base_interest = 5):
        # Adjust interest based on character's personality traits
        for trait in character.personality_traits:
            base_interest += self.interest_adjustment_for_trait(character, trait)

        # Ensure the interest level is within a reasonable range
        return max(0, min(base_interest, 10))

    def interest_adjustment_for_trait(self, character: Character, trait):
        # Define how each trait affects interest in a new topic
        # Example adjustments for a few traits
        trait_adjustments = {
            "Curious": 2,
            "Cautious": -2,
            "Compassionate": 1,
            "Practical": 0,
            "Adventurous": 1.5,
            "Analytical": 1,
            # ... other trait adjustments ...
        }
        return trait_adjustments.get(trait, 0)