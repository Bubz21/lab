class Television:
    """
    A class that details channels and volumes for a tv
    """
    MIN_CHANNEL = 0     # Minimum TV channel
    MAX_CHANNEL = 3     # Maximum TV channel

    MIN_VOLUME = 0      # Minimum TV volume
    MAX_VOLUME = 2      # Maximum TV volume

    def __init__(self):
        """
        Constructor used to initial the state of the tv
        """
        self.channel = 0
        self.volume = 0
        self.status = 'False'
        
        pass

    def power(self):
        """
        A method that allows the user to switch the power of the tv to on our off
        returns the status of the tv
        """
        if self.status == 'False':
            self.status = 'True'

        if self.status == 'True':
            self.status = 'False'
            
        pass

    def channel_up(self):
        """
        A method that modifies the channel up
        returns the new channel that is chosen
        """
        if self.status == 'True':
            if self.channel < 3:
                self.channel = self.channel + 1
            else:
                self.channel = 0
                
        pass

    def channel_down(self):
        """
        A method that modifies the channel down
        returns the new channel that is chosen
        """
        if self.status == 'True':
            if self.channel > 0:
                self.channel = self.channel - 1
            else:
                self.channel = 3
                
        pass

    def volume_up(self):
        """
        A method that modifies the volume up
        returns the new channel that is chosen
        """
        if self.status == 'True':
            if self.volume < 2:
                self.volume = self.volume + 1
                
        pass

    def volume_down(self):
        """
        A method that modifies the volume down
        returns the new channel that is chosen
        """
        if self.status == 'True':
            if self.volume > 0:
                self.volume = self.volume - 1
                
        pass

    def __str__(self):
        """
        A method that sends back the information of the status, channel, and volume
        """
        self.send = ('TV status: Is on = ', self.status, ', Channel = ', self.channel, ', Volume = ', self.volume)
        return self.send
    
        pass
