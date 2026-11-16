import pytest
from television import Television

class TestTelevision:
    def setup_method(self) -> None:
        self.t1: Television = Television()
    
    def teardown_method(self) -> None:
        del self.t1
    
    def test_init(self) -> None:
        assert self.t1.MIN_VOLUME == 0
        assert self.t1.MAX_VOLUME == 2
        assert self.t1.MIN_CHANNEL == 0
        assert self.t1.MAX_CHANNEL == 3

        assert self.t1.__str__() == "Power = False, Channel = 0, Volume = 0"
    
    def test_power(self) -> None:
        self.t1.power()
        assert self.t1.__str__() == "Power = True, Channel = 0, Volume = 0"

        self.t1.power()
        assert self.t1.__str__() == "Power = False, Channel = 0, Volume = 0"

    def test_mute(self) -> None:
        self.t1.mute()
        assert self.t1.__str__() == "Power = False, Channel = 0, Volume = 0"

        self.t1.power()
        self.t1.mute()
        assert self.t1.__str__() == "Power = True, Channel = 0, Volume = 0"

        self.t1.volume_up()
        self.t1.mute()
        assert self.t1.__str__() == "Power = True, Channel = 0, Volume = 0"

        self.t1.power()
        assert self.t1.__str__() == "Power = False, Channel = 0, Volume = 0"

        self.t1.mute()
        assert self.t1.__str__() == "Power = False, Channel = 0, Volume = 0"

        self.t1.power()
        self.t1.mute()
        assert self.t1.__str__() == "Power = True, Channel = 0, Volume = 1"

        self.t1.volume_down()
        assert self.t1.__str__() == "Power = True, Channel = 0, Volume = 0"
    
    def test_channel_up(self) -> None:
        self.t1.channel_up()
        assert self.t1.__str__() == "Power = True, Channel = 1, Volume = 0"

        self.t1.power()
        self.t1.channel_up()
        assert self.t1.__str__() == "Power = False, Channel = 1, Volume = 0"

        self.t1.power()
        self.t1.channel_up()
        assert self.t1.__str__() == "Power = True, Channel = 2, Volume = 0"

        self.t1.channel_up()
        assert self.t1.__str__() == "Power = True, Channel = 3, Volume = 0"
        
        self.t1.channel_up()
        assert self.t1.__str__() == "Power = True, Channel = 0, Volume = 0"

    def test_channel_down(self) -> None:
        self.t1.channel_down()
        assert self.t1.__str__() == "Power = True, Channel = 3, Volume = 0"

        self.t1.channel_down()
        assert self.t1.__str__() == "Power = True, Channel = 2, Volume = 0"

        self.t1.power()
        self.t1.channel_down()
        assert self.t1.__str__() == "Power = False, Channel = 2, Volume = 0"

        self.t1.power()
        self.t1.channel_down()
        assert self.t1.__str__() == "Power = True, Channel = 1, Volume = 0"

        self.t1.channel_down()
        assert self.t1.__str__() == "Power = True, Channel = 0, Volume = 0"

    def test_volume_up(self) -> None:
        self.t1.volume_up()
        assert self.t1.__str__() == "Power = True, Channel = 0, Volume = 1"

        self.t1.power()
        self.t1.volume_up()
        assert self.t1.__str__() == "Power = False, Channel = 0, Volume = 1"

        self.t1.power()
        self.t1.volume_up()
        assert self.t1.__str__() == "Power = True, Channel = 0, Volume = 2"

        self.t1.volume_up()
        assert self.t1.__str__() == "Power = True, Channel = 0, Volume = 2"

        self.t1.volume_down()
        assert self.t1.__str__() == "Power = True, Channel = 0, Volume = 1"
        self.t1.mute()
        assert self.t1.__str__() == "Power = True, Channel = 0, Volume = 0"
        self.t1.volume_up()
        assert self.t1.__str__() == "Power = True, Channel = 0, Volume = 2"

    def test_volume_down(self) -> None:
        self.t1.volume_down()
        assert self.t1.__str__() == "Power = True, Channel = 0, Volume = 1"

        self.t1.power()
        self.t1.volume_down()
        assert self.t1.__str__() == "Power = False, Channel = 0, Volume = 1"

        self.t1.power()
        self.t1.volume_down()
        assert self.t1.__str__() == "Power = True, Channel = 0, Volume = 0"

        self.t1.volume_down()
        assert self.t1.__str__() == "Power = True, Channel = 0, Volume = 0"

        self.t1.volume_up()
        self.t1.volume_up()
        assert self.t1.__str__() == "Power = True, Channel = 0, Volume = 2"
        self.t1.mute()
        assert self.t1.__str__() == "Power = True, Channel = 0, Volume = 0"
        self.t1.volume_down()
        assert self.t1.__str__() == "Power = True, Channel = 0, Volume = 1"