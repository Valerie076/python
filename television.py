from typing import override


class Television:
    """
    An instance of a Television
    """
    
    MIN_VOLUME: int = 0
    MAX_VOLUME: int = 2
    MIN_CHANNEL: int = 0
    MAX_CHANNEL: int = 3

    def __init__(self) -> None:
        """
        Instantiates a Television object.
        """
        self.__status: bool = False
        self.__muted: bool = False
        self.__volume: int = self.MIN_VOLUME
        self.__channel: int = self.MIN_CHANNEL
    
    def power(self) -> None:
        """
        Toggles the power status.
        """
        self.__status = not self.__status
    
    def mute(self) -> None:
        """
        Toggles the muted status.
        """
        if self.__status:
            self.__muted = not self.__muted
    
    def channel_up(self) -> None:
        """
        If the power status is True, increases channel by 1, wrapping back to MIN_CHANNEL when surpassing MAX_CHANNEL.
        """
        if self.__status:
            self.__channel = (self.__channel + 1) % (self.MAX_CHANNEL + 1)
    
    def channel_down(self) -> None:
        """
        If the power status is True, decreases channel by 1, wrapping back to MAX_CHANNEL when surpassing MIN_CHANNEL.
        """
        if self.__status:
            self.__channel = (self.__channel - 1) % (self.MAX_CHANNEL + 1)
    
    def volume_up(self) -> None:
        """
        If the power status is True, increases volume by 1, up to MAX_VOLUME. Sets mute status to False.
        """
        if self.__status:
            self.__muted = False
            self.__volume = self.__volume + 1 if self.__volume < self.MAX_VOLUME else self.__volume
    
    def volume_down(self) -> None:
        """
        If the power status is True, decreases volume by 1, down to MIN_VOLUME. Sets mute status to False.
        """
        if self.__status:
            self.__muted = False
            self.__volume = self.__volume - 1 if self.__volume > self.MIN_VOLUME else self.__volume
    
    @override
    def __str__(self) -> str:
        """
        Returns a formatted summary of the object, including power, channel, and volume.

        :return: Formatted summary of power, channel, and volume
        :rtype: str
        """
        return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume if not self.__muted else 0}"