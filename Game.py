class Game:
    TOTAL_NUMBER_OF_PINS = 10

    def __init__(self):
        self._rolls = []

    def roll(self, pins):
        self._rolls.append(pins)

    @property
    def score(self):
        calculated_score = 0
        roll_index = 0

        for frame_index in range(10):
            if self._is_strike(roll_index):
                calculated_score += self._get_score_for_strike(roll_index)
                roll_index += 1
            elif self._is_spare(roll_index):
                calculated_score += self._get_score_for_spare(roll_index)
                roll_index += 2
            else:
                calculated_score += self._get_score_for_non_marking_frame(roll_index)
                roll_index += 2

        return calculated_score

    def _is_strike(self, roll_index):
        return self._rolls[roll_index] == self.TOTAL_NUMBER_OF_PINS

    def _get_score_for_strike(self, roll_index):
        return self.TOTAL_NUMBER_OF_PINS + self._rolls[roll_index + 1] + self._rolls[roll_index + 2]

    def _is_spare(self, roll_index):
        return self._rolls[roll_index] + self._rolls[roll_index + 1] == self.TOTAL_NUMBER_OF_PINS

    def _get_score_for_spare(self, roll_index):
        return self.TOTAL_NUMBER_OF_PINS + self._rolls[roll_index + 2]

    def _get_score_for_non_marking_frame(self, roll_index):
        return self._rolls[roll_index] + self._rolls[roll_index + 1]

