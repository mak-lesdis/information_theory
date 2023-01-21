# 情報理論で使えるクラスなどを配置したmodule
# A module for information theory


import math
from typing import List, Optional


# 情報源のメッセージ
class Message:
    def __init__(self, code_length: int, probability: float) -> None:
        # validation
        if (probability < 0.0 or code_length < 0):
            raise ValueError()
        self.code_length = code_length
        self.probability = probability


# 情報源
class InformationSource:
    def __init__(self, messages: List[Message]) -> None:
        self.messages = messages

    def averageCodewordLength(self) -> float:
        """
        平均符号長を計算
        """
        sum = 0.0
        for message in self.messages:
            sum += message.code_length * message.probability
        return sum

    def informationEntropy(self) -> float:
        """
        Calculates the entropy of a set of probabilities.
        """
        ent = 0.0
        for message in self.messages:
            ent += -message.probability * math.log2(message.probability)
        return ent


class MessgaesFactry:
    @staticmethod
    def generateMessages(probabities: List[float],
                         length: int,
                         code_lengths:
                         Optional[List[int]] = None) -> List[Message]:
        if (length < 0):
            raise ValueError
        if (code_lengths is None):
            code_lengths = [0] * length
        if (len(probabities) != length or len(code_lengths) != length):
            raise ValueError()
        messages: List[Message] = []
        for i in range(length):
            message = Message(code_lengths[i], probabities[i])
            messages.append(message)
        return messages
