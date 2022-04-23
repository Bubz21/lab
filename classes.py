class Television:
    MIN_CHANNEL = 0     # Minimum TV channel
    MAX_CHANNEL = 3     # Maximum TV channel

    MIN_VOLUME = 0      # Minimum TV volume
    MAX_VOLUME = 2      # Maximum TV volume

    def __init__(self):
        self.channel = 0
        self.volume = 0
        self.status = 'False'
        """
        - Create a private variable to store the TV channel. It should be set to the minimum TV channel by default.
        - Create a private variable to store the TV volume. It should be set to the minimum TV volume by default.
        - Create a private variable to store the TV status. The TV should start when it is off.
        """
        pass

    def power(self):
        if self.status == 'False':
            self.status = 'True'

        if self.status == 'True':
            self.status = 'False'
        """
        - This method should be used to turn the TV on/off.
        - If called on a TV object that is off, the TV object should be turned on.
        - If called on a TV object that is on, the TV object should be turned off.
        """
        pass

    def channel_up(self):
        if self.status == 'True':
            if self.channel < 3:
                self.channel = self.channel + 1
            else:
                self.channel = 0
        """
        - This method should be used to adjust the TV channel by incrementing its value.
        - It should only work for a TV that is on.
        - If the method is called when one is on the MAX_CHANNEL, it should take the TV channel back to the MIN_CHANNEL.
        """
        pass

    def channel_down(self):
        if self.status == 'True':
            if self.channel > 0:
                self.channel = self.channel - 1
            else:
                self.channel = 3
        """
        - This method should be used to adjust the TV channel by decrementing its value.
        - It should only work for a TV that is on.
        - If the method is called when one is on the MIN_CHANNEL, it should take the TV channel back to the MAX_CHANNEL.
        """
        pass

    def volume_up(self):
        if self.status == 'True':
            if self.volume < 2:
                self.volume = self.volume + 1
        """
        - This method should be used to adjust the TV volume by incrementing its value.
        - It should only work for a TV that is on.
        - If the method is called when one is on the MAX_VOLUME, the volume should not be adjusted.
        """
        pass

    def volume_down(self):
        if self.status == 'True':
            if self.volume > 0:
                self.volume = self.volume - 1
        """
        - This method should be used to adjust the TV volume by decrementing its value.
        - It should only work for a TV that is on.
        - If the method is called when one is on the MIN_VOLUME, the volume should not be adjusted.
        """
        pass

    def __str__(self):
        self.send = ('TV status: Is on = ', self.status, ', Channel = ', self.channel, ', Volume = ', self.volume)
        return self.send
        """
        - This method should be used to return the TV status using the format shown in the comments of main.py
        """
        pass
