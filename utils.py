class WordData(object):
    def __init__(self, word=None, translations=None, definitions=None, transcriptions=None,
                 audio_links=None):
        self.word = word if word else ''
        self.translations = translations if translations else []
        self.definition_list = definitions
        self.transcriptions = transcriptions if transcriptions else []
        self.audio_links = audio_links if audio_links else []

    @property
    def definition_list(self):
        return self._definition_list

    @definition_list.setter
    def definition_list(self, definitions):
        if definitions is None:
            self._definition_list = []
            return
        elif not isinstance(definitions, list):
            raise TypeError('Invalid type for definition')
        else:
            for element in definitions:
                if not isinstance(element, Definition):
                    raise TypeError('Invalid type for definition')
            self._definition_list = definitions

    def to_json(self):
        return {
            'word': self.word[0].upper() + self.word[1:],
            'translations': self.translations,
            'pronunciations': {
                'text': self.transcriptions,
                'audio': self.audio_links
            },
            'definitions': [definition.to_json() for definition in self._definition_list]
        }


class Definition(object):
    def __init__(self, part_of_speech=None, additional_info=None, text=None, example_uses=None):
        self.part_of_speech = part_of_speech if part_of_speech else ''
        self.additional_info = additional_info if additional_info else ''
        self.text = text if text else ''
        self.example_uses = example_uses if example_uses else []

    def to_json(self):
        return {
            'partOfSpeech': self.part_of_speech,
            'additionalInfo': self.additional_info,
            'text': self.text,
            'examples': self.example_uses
        }
